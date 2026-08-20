# You are an expert full-stack refactoring engineer specializing in vanilla JavaScript Progressive

You are an expert full-stack refactoring engineer specializing in vanilla JavaScript Progressive Web Apps and Supabase applications. Your task is to perform a deep, clean architectural refactor while preserving 100% of the existing functionality.

**Project**: ToursystemV1 — Fleet/Tour management PWA (INYATHI / TransRoute) with admin + driver portals. Features include vehicles (owned + rented), bookings/tours with calendar, pre/post-trip inspections, recon/transfer sheets, fines, incidents, expenses, wages, PDF generation, offline-first IndexedDB + Service Worker sync, Cloudinary uploads, Supabase Auth/RLS/Edge Functions, WhatsApp alerts via CallMeBot, regional filtering.

**Repo**: https://github.com/stoner4kt/ToursystemV1-clone-for-Codebase-Cleanup/tree/main 

**Strict Non-Negotiable Constraints**:
- Do NOT change the database schema, any Supabase queries, RLS policies, table structures, or Edge Functions. Preserve ALL Supabase Edge Functions and migrations exactly as they are.
- Do NOT change Cloudinary upload logic, signed URLs, or storage handling.
- The refactored system MUST remain 100% functionally identical. Preserve all flows exactly: login → booking creation/locking → inspection (pre/post on same page) → recon sheets → uploads → PDF generation → alerts → offline sync → etc.
- No new third-party libraries unless absolutely necessary (prefer vanilla JS).
- Keep PWA capabilities (manifest, sw.js) intact.

**Refactoring Goals**:
1. **Deep Modularization & Unbulking**:
   - Completely break down the large monolithic `admin.js` and `driver-dashboard.js` into small, focused files.
   - Give every major "sheet"/feature its own dedicated HTML page + JS file.
   - Pre- and post-trip inspections stay together on one page (`inspection.html` + `inspection.js`).

2. **New Folder Structure** (exactly as follows):
   ```
   /
   ├── index.html                  (landing page that redirects to login)
   ├── login.html                  (main login page)
   ├── src/
   │   ├── core/                   # Shared foundational logic
   │   │   ├── auth.js
   │   │   ├── supabase-client.js
   │   │   ├── offline-sync.js
   │   │   ├── utils.js
   │   │   ├── config.js
   │   │   └── api.js              # Central data access layer
   │   ├── admin/                  # Admin role
   │   │   ├── admin-dashboard.html + admin-dashboard.js   (main hub with persistent sidebar)
   │   │   ├── admin-fleet.html + admin-fleet.js
   │   │   ├── admin-bookings.html + admin-bookings.js
   │   │   ├── admin-inspections.html + admin-inspections.js
   │   │   ├── admin-recon.html + admin-recon.js
   │   │   ├── admin-fines.html + admin-fines.js
   │   │   ├── admin-incidents.html + admin-incidents.js
   │   │   ├── admin-rented-vehicles.html + admin-rented-vehicles.js
   │   │   ├── admin-expenses.html + admin-expenses.js
   │   │   └── [any  and all other admin sections currently in admin.js]
   │   ├── driver/                 # Driver role
   │   │   ├── driver-dashboard.html + driver-dashboard.js (main with persistent sidebar)
   │   │   └── inspection.html + inspection.js             (pre/post together)
   │   ├── shared/                 # Reusable across roles
   │   │   ├── components/         # Reusable UI: sidebar-nav.js, modals, tables, forms
   │   │   ├── services/           # Data services (vehicles.js, bookings.js, inspections.js, etc.)
   │   │   ├── pdf-generator.js
   │   │   └── upload.js
   │   ├── assets/
   │   │   ├── css/style.css
   │   │   └── icons/
   │   └── pages/                  # Any remaining standalone pages
   ├── supabase/                   # Keep Edge Functions untouched
   ├── migrations/                 # Keep untouched
   ├── SETUP_GUIDE.md (updated)
   └── ARCHITECTURE.md (new)
   ```

3. **Key Requirements**:
   - **Navigation**: Implement a persistent sidebar (in admin and driver sections) that links to all separate HTML pages. Use vanilla JS for navigation.
   - **Auth Flow**: Visiting the root (`index.html`) should redirect to `login.html`. Only logged-in users can access the app, with role-based routing (admin → admin-dashboard, driver → driver-dashboard).
   - Use ES modules (`import/export`) with dynamic imports for lazy loading to improve performance with large data.
   - Implement client-side pagination, search, filtering, and efficient loading in all list-heavy pages to prepare for data growth (200+ vehicles, 100+ drivers).
   - Centralize shared utilities and services while keeping modules loosely coupled.
   - Improve code comments, error handling, remove dead code, and ensure clean separation by role and feature.
   - Update all internal links, script sources, and imports after restructuring.
   - Update `SETUP_GUIDE.md` with new structure instructions and create `ARCHITECTURE.md`.

**Output Format**:
- First, show the complete new file tree.
- Then, for every modified or new file, provide the full file content (or clear unified diff if only small changes).
- Finally, provide a detailed step-by-step verification checklist covering all critical flows (login, role routing, bookings, inspections, recon, uploads, offline sync, etc.) to confirm nothing is broken.

Ensure the refactored codebase is clean, highly maintainable, future-proof, and easy to navigate for long-term development

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Yes

---

Continue with pass 3 both the admin and driver  files
