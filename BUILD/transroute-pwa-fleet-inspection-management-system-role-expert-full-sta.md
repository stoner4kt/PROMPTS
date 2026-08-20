# "TransRoute PWA" - Fleet & Inspection Management System **Role:** Expert Full-Stack Developer

"TransRoute PWA" - Fleet & Inspection Management System

**Role:** Expert Full-Stack Developer specializing in Serverless Architecture.
**Objective:** Build a production-ready, mobile-first PWA for a transport company with **ZERO monthly subscriptions**.

### 1. Technical Stack (Mandatory)
*   **Frontend:** Vanilla HTML5, CSS3, Vanilla JavaScript.
*   **Backend:** Supabase (Auth, PostgreSQL, Edge Functions).
*   **Media:** Cloudinary (Unsigned Upload Preset).
*   **PDF:** jsPDF + html2canvas for branded reports.
*   **Notifications:** CallMeBot API (Fault Alerts) & WhatsApp Links (Manual Reminders).

### 2. Core Modules & Logic
*   **Admin Dashboard:** 
    *   **Calendar View:** Manage bookings and confirm invoices.
    *   **Fleet Management:** A dedicated section to **Add/Edit Vehicles** (Reg No, Model, Mileage, Next Service).
    *   **Report Center:** View completed inspections and download branded PDFs.
*   **Driver Authentication:** Self-service Magic Link login. Map users to a `driver_id` in the `profiles` table.
*   **Mobile Inspection Form:**
    *   **Vehicle Selection:** Drivers must select a vehicle from a dropdown of active fleet members.
    *   **Media Capture:** `<input capture="environment">` for "Before/After" photos/videos.
    *   **Offline-First:** Sync to Supabase/Cloudinary via `IndexedDB` when signal returns.
    *   **Checklist:** Mark items as "OK" or "Critical Fault."
*   **Automated Logic:** A Supabase Edge Function that triggers on new inspections. If a "Critical Fault" is logged, send a WhatsApp alert to Admin via **CallMeBot**.

### 3. Deliverables
Full code for: `index.html` (Admin + Fleet Tab), `inspection.html`, `login.html`, `style.css`, `app.js`, `sw.js`, and `manifest.json`. Include the `supabase/functions/fault-alert/index.ts` file.

### 4. Database Schema (SQL)
Provide SQL for:
*   `profiles` (id, driver_id, name).
*   `vehicles` (registration_no, model, current_mileage, next_service_km, status).
*   `bookings` (invoice_no, tour_date, status).
*   `inspections` (invoice_no, vehicle_reg, driver_id, faults_json, media_urls).

### 5. Deployment Guide
Step-by-step for  everything, Supabase RLS, Cloudinary presets, Netlify hosting, and CallMeBot setup.
