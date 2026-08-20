# I want to make these edits to my system, this is the

I want to make these edits to my system, this is the prompt I will feed into codex, :[Act as an expert Full-Stack Software Engineer specializing in the Supabase and Cloudinary ecosystems. 

I have a fleet management system built using a frontend stack of HTML, CSS, and vanilla JavaScript, backed by Supabase for data storage and auth. Currently, my system allows both Admins and Drivers to upload, view, and download documents (such as IDs, permits, and vehicle photos) via multiple UI sections. 

Right now, the project relies on an insecure, completely "unsigned" public Cloudinary setup, which is causing permission blocks (HTTP 401 errors) and exposing direct media links. 

I want to migrate this entire project to a bulletproof, secure architecture using a Signed Cloudinary Storage strategy powered by a Supabase Edge Function middleman.

Please analyze the codebase and implement/refactor the following changes across the repository:

### 1. THE ARCHITECTURE GOAL
- Frontend NEVER handles Cloudinary API secrets.
- All uploads use an "authenticated" or "private" delivery type preset.
- All asset view and download requests must call a Supabase Edge Function to get a short-lived (e.g., 10-minute) cryptographic Signed URL.
- Database entries in Supabase should store ONLY the Cloudinary `public_id` and `resource_type` (e.g., 'image' or 'raw' for PDFs), rather than static, absolute URLs.

### 2. BACKEND: SUPABASE EDGE FUNCTION
Draft a complete, production-ready Supabase Edge Function (written in TypeScript/Deno using the `npm:cloudinary` SDK) named `get-signed-url`. This function must:
- Handle CORS preflight options safely.
- Authenticate the incoming request session if necessary.
- Accept a payload containing `publicId` and `resourceType`.
- Initialize Cloudinary securely via server-side environment variables (`CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`).
- Generate and return a secure, signed URL using `sign_url: true` and an expiration timestamp (`expires_at`) set to 10 minutes in the future.

### 3. FRONTEND REFACTOR (HTML / JS Files)
Scan the repository for all upload, preview, and download logic across both the Admin and Driver dashboards. Refactor them to match these updated mechanics:

- **Upload Sections:** Update the file upload handlers. When a driver or admin uploads an image or a PDF document, ensure it targets the correct secure asset preset. Ensure the JavaScript payload handles files with `resource_type: 'auto'` so that PDFs, ZIPs, and images are all accepted seamlessly. Save only the resulting `public_id` and the format type to our Supabase database tables.
- **View/Preview Sections:** Refactor image `src` bindings or PDF `iframe`/`window.open` calls. Instead of reading a static URL from the database, intercept the event, call `supabase.functions.invoke('get-signed-url')` with the asset's `public_id`, and feed the resulting short-lived signed URL to the DOM.
- **Download Sections:** Ensure that when a user clicks a "Download" button for a document, the signed URL generated enforces an attachment download download flag or handles the stream cleanly so it saves natively to their mobile device or desktop.

Please review all relevant `.js` and `.html` files in the repository, pinpoint where these media elements are handled, and provide the exact file diffs or replacement code blocks needed to complete this migration.
