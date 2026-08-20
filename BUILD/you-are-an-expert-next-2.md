# You are an expert Next

You are an expert Next.js + Supabase architect. I have a production fleet management system called INYATHI https://github.com/stoner4kt/Fleet-system/tree/main that is currently working well for a client. I want you to perform a complete **Phase 3 Architecture & Code Quality Overhaul** without breaking existing functionality.

**Repository Context** (Next.js 15 App Router, TypeScript, Supabase, Tailwind):
- Main logic is in `lib/storage.ts` (very large monolithic file with types, Supabase client, localStorage sync, CRUD for all entities, transforms, etc.).
- Key files: `app/page.tsx`, `components/AdminDashboard.tsx`, `components/DriverDashboard.tsx`, `components/AuthContainer.tsx`, `lib/storage.ts`, Supabase schema in `supabase/schema/`, Edge Functions.
- It uses hybrid localStorage + Supabase with fallback.
- Goal: Improve maintainability, scalability, and developer experience while keeping 100% backward compatibility and operational.

**Exact Requirements for Phase 3**:

1. **Restructure the Project**:
   - Introduce feature-sliced architecture: `features/` folder (bookings, vehicles, recons, inspections, auth, etc.).
   - Move business logic to `lib/services/` (one service per domain).
   - Keep `lib/supabase.ts` minimal (client init only).
   - Centralize shared utilities.

2. **Refactor `lib/storage.ts`**:
   - Split it completely into clean, focused service files.
   - Extract common helpers (transforms, sync, Cloudinary, CSV export, etc.).
   - Maintain all existing public APIs during transition (add deprecation notes if needed).

3. **Add Modern Best Practices**:
   - Generate and use proper Supabase types.
   - Add TanStack Query (or recommend strong integration) for data management.
   - Improve error handling, loading states, and TypeScript strictness.
   - Refactor large dashboard components into smaller feature components.
   - Add consistent layout components.
   - Ensure all changes are backward compatible.

4. **Critical Constraints**:
   - **The system must remain fully operational** after changes — no breaking changes to UI flows, auth, data sync, or Supabase interactions.
   - Preserve hybrid localStorage + Supabase behavior.
   - Provide step-by-step migration instructions.
   - Include before/after file examples or full refactored files where practical.
   - Output a clear new folder structure and summary of changes.

Analyze the full repository first, then execute the refactor plan in clear, actionable steps with code where possible. Prioritize safety and incremental changes.

Start by showing the proposed new folder structure and the plan for splitting `storage.ts`.

---

**Tips for Using This Prompt**:
- Feed it in chunks if Claude has token limits (e.g., first ask for structure + plan, then specific files).
- After Claude responds, share specific file contents with it for precise refactors.
- Test thoroughly after each major change (especially auth and data sync).

Once you get the output from Claude, we can review it together here and fine-tune anything. Would you like any adjustments to the prompt before you use it?

---

Okay so generate me a prompt I can feed into codex/ replit to perform this task while ensuring the functionality of the system and that it works exactly as it does
