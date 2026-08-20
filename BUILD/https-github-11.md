# https://github

https://github.com/stoner4kt/ToursystemV2refactored/tree/main Good, the relevant edge functions exist already: `fault-alert`, `notify-driver-fine`, `notify-expense-submitted`, `send-otp-email`, `verify-otp`. Let me check each one against your requirements, plus the schema and how the frontend calls them.This looks solid. Let me check the other functions.Now the OTP functions for the edit-request flows (bookings and Transfer Recon):Now let's check whether the frontend actually calls these edge functions — this is where things usually break.Found a real bug. The frontend is calling function names that don't match the deployed functions. Let's look closer:This modal has real bugs. Let me check how it's actually invoked for booking edits and recon edit requests.Let me check the auth system, since `notify-driver-fine` requires a real Supabase JWT bearer token to identify the admin.I cloned and audited the repo. Good news: the schema and the core edge functions are almost all in place. Bad news: several are **not wired up correctly** on the frontend, so right now most of these flows will silently fail in production. Here's the breakdown per requirement:

## 1. Inspection fault alert → main admin ⚠️ works, but duplicated
`fault-alert` edge function is correctly built and correctly invoked from `lib/storage.ts` (`saveInspection`). However, `saveInspection` **also** fires a second, separate email via a Next.js API route (`app/api/alert/route.ts`) on the exact same condition. That means every logged fault sends **two** emails to admin, using two different sets of env vars (`RESEND_APIKEY`/`ADMIN_EMAIL` set in Vercel/Next.js env for the API route, vs `RESEND_API_KEY`/`ADMIN_EMAIL` set in Supabase secrets for the edge function). If only one of those is configured, you'll get exactly one email and think it's fine — but it's fragile duplication that should be trimmed to one path.

## 2. Traffic fine → driver notification ❌ broken
- `notify-driver-fine` edge function is correctly built (looks up the driver's email, requires an admin bearer token, sends via Resend).
- But `lib/storage.ts` calls `supabase.functions.invoke('notify-drivers-fines', ...)` — **wrong function name** (extra "s", doesn't exist) — this will 404 every time.
- It also sends `{ fine: prepared }` in the body, but the function expects `{ traffic_fine_id }`.
- It's also fired immediately after an **un-awaited** `pushToSupabase()` call, so even once the name/payload are fixed, the DB row may not exist yet when the function tries to read it back.

## 3. Expense/damage → main admin alert ❌ broken
Same pattern as above: `notify-expenses` is invoked, but the real function is `notify-expense-submitted`, and it's sent `{ expense: prepared }` instead of the expected `{ expense_id }`. Same race condition with the un-awaited DB push.

## 4. Admin booking edit → OTP to main admin ❌ broken
- The OTP gate is wired up (`executeWithOtpGuard('booking_edit', b.invoice_no, ...)`), but it passes `b.invoice_no` (e.g. `"INV-2026-114"`) as `resource_id`. The `otp_verifications.resource_id` column is `uuid NOT NULL` — an invoice number isn't a UUID, so the insert will fail with a Postgres type error.
- Worse: `OTPModal.tsx` hardcodes `admin_id: 'DRV-ADM001'` (the admin's `driver_id` text code, not their UUID `profiles.id`). `otp_verifications.admin_id` is also `uuid NOT NULL`, so **every single OTP request fails this insert**, regardless of resource type.
- When `send-otp-email` fails, `OTPModal` silently falls back to generating a code **locally in the browser** and displaying it right there in a toast — so the "security" step currently does nothing at all; whoever clicks the button sees their own OTP on screen.
- Several other OTP-gated actions (`driver_deactivate`, `recon_approval`, `transfer_approval`, `review_edit_request`, `booking_delete_reject`) use `resource_type` strings that aren't in the DB's `CHECK` constraint (`recon_edit, booking_edit, booking_delete, expense_approval, incident_delete, transfer_recon_edit`), so those all hit the same silent-fallback failure too.

## 5. Driver Transfer Recon edit request → OTP to admin ❌ not implemented
`transferReconApi.requestEdit()` (and the identical `reconApi.requestEdit()` for weekly recon) just flips `edit_request_status` to `'pending'` in local/Supabase storage. There is **no call to `send-otp-email` anywhere in this path** — driver or admin side. The admin's later "review edit request" approval is nominally OTP-gated, but with the broken `admin_id`/`resource_type` issues above, and it approves the request rather than gating the driver's actual edit — so no OTP ever reaches the admin's inbox for this flow.

---

### Root causes, summarized
1. Frontend/edge-function name and payload mismatches (fine + expense notifiers).
2. Fire-and-forget DB writes racing against edge function reads.
3. `OTPModal` sends a fake admin identifier that can never satisfy the DB schema — this alone silently disables the entire OTP system.
4. `resource_type` values used in the UI don't match what the DB allows.
5. Transfer/weekly recon edit requests never call the OTP function at all.
6. Duplicate fault-alert email path.

I can fix all of this — it mostly means: correcting the function names/payloads in `lib/storage.ts`, awaiting the Supabase push before invoking the notifier (or having the edge functions accept the payload directly instead of re-querying), making `send-otp-email` resolve the real main-admin UUID itself (safer than trusting the client), fixing the `resource_id`/`resource_type` values used across the admin dashboard, and adding the missing OTP trigger to the recon edit-request flow. Want me to go ahead and implement these fixes now?

---

This is the Repo I'm referring to https://github.com/stoner4kt/ToursystemV2refactored/tree/main

---

This is my fault-alert function, send-otp-email and  verify-otp function along with my otpmodal and storage.ts

---

Here's my notify-expense-submitted and notify-driver-fine functions, Guide me on what exactly to change and where to insert what code to ensure all my functions works seamlessly
