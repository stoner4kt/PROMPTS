# You are an expert full-stack refactoring engineer specializing in vanilla JavaScript PWAs

You are an expert full-stack refactoring engineer specializing in vanilla JavaScript PWAs and Supabase-backed applications.

**Project**: ToursystemV1 — A Progressive Web App for fleet/tour management (INYATHI / TransRoute) with admin and driver portals. It handles vehicles (including rented vehicles), drivers, bookings/tours, pre/post-trip inspections, recon sheets, fines, incidents, expenses, wages, PDF generation, offline sync via IndexedDB + Service Worker, Cloudinary uploads, Supabase Auth + RLS + Edge Functions, WhatsApp alerts, and regional filtering (Cape Town/Joburg).

**Repo**: https://github.com/stoner4kt/ToursystemV1-clone-for-Codebase-Cleanup/tree/main 

**Strict Constraints**:
- Do NOT change the database schema (schema.sql) or any Supabase table structures, RLS policies, or queries in a way that would require DB migrations.
- Do NOT change Cloudinary integration logic, upload flows, signed URLs, or storage handling.
- The refactored system must remain 100% functionally identical to the current version. All existing features, UI flows, offline capabilities, auth (magic links), realtime elements, PDF generation, recon calculations, booking locks, rented vehicle handling, regional filters, etc., must continue to work exactly as they do now.
- Preserve all external dependencies and third-party services (Supabase, Cloudinary, CallMeBot, etc.).
- Only improve structure, performance for data growth, and maintainability.

**Goals**:
1. **Codebase Manageability**: Break down monolithic files (especially the very large admin.js) into a clean, modular architecture. Use ES modules where appropriate. Create clear separation of concerns (data layer, UI components, services, utilities).
2. **Performance & Data Growth Readiness** (without DB changes): Implement client-side pagination, lazy loading, efficient querying/filtering, better offline sync conflict handling, caching strategies, and reduced memory usage for large fleets (200+ vehicles, 100+ drivers). Optimize admin dashboard loading and list views.
3. **Repo Cleanup**: 
   - Organize files/folders logically (e.g., src/, components/, services/, utils/, pages/).
   - Remove unused/dead code, consolidate duplicates, update comments and SETUP_GUIDE.md.
   - Improve .gitignore, add basic project documentation, and prepare for easier CI/CD.
   - Ensure the app still deploys cleanly to Netlify/Vercel/Replit.

**Output**:
Produce a single, comprehensive, ready-to-use prompt that I can feed into Cursor / Claude Codex / Replit Agent (or similar code editing AI) along with the repo.

This second prompt must instruct the AI to:
- Perform the full refactoring step-by-step.
- Output the complete new file structure.
- Provide diff-style or full rewritten content for each modified/created file.
- Include testing/verification steps to ensure nothing is broken.
- Keep changes evolutionary and safe.

Make the second prompt extremely detailed, specific, and structured so the code-editing AI can execute the refactor reliably while preserving full functionality. Include references to key files like app.js, admin.js, config.js, driver-dashboard.js, inspection.js, etc.

Start your response with the full prompt for the code editor AI.

---

Generate this prompt into a md file i can download
