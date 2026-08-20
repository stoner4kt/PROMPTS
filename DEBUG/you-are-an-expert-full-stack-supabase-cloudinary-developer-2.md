# You are an expert full-stack Supabase + Cloudinary developer

You are an expert full-stack Supabase + Cloudinary developer.

**Repo:** https://github.com/stoner4kt/ToursystemV1

**Problem:**
When trying to upload documents (e.g. PDFs) in the New Booking form, the upload fails with:

> POST https://api.cloudinary.com/v1_1/dzf97vyjs/auto/upload 403 (Forbidden)
> Upload preset 'inyathi_signed' not found or not available for unsigned uploads.

The user is intentionally using a **signed** upload preset (`inyathi_signed`).

**Task:**
1. Analyze the entire repo, especially:
   - All files related to file uploads (`uploadToCloudinary`, document upload logic)
   - The booking form (`admin.js`, any NewBooking component)
   - Supabase Edge Functions (especially `sign-upload` or similar)
   - Any Cloudinary configuration

2. Identify exactly why the current implementation is failing.

3. Provide a **complete, production-ready fix** including:
   - Corrected `uploadToCloudinary` function (or equivalent) that properly calls the Supabase Edge Function first to get a signature.
   - Any necessary updates to the Edge Function (`supabase/functions/sign-upload/index.ts`).
   - Required environment variables / secrets for Supabase.
   - Any other code changes needed (form handling, error handling, etc.).

4. Give clear step-by-step instructions on what to change, with **exact code diffs** where possible.

5. Also suggest whether they should switch to an unsigned preset as a simpler alternative, and the pros/cons.

Focus especially on the current upload flow in the admin booking section. Be precise and thorough and then apply the fixes to the other places where uploads are
