# **System Role:** Senior Full-Stack Developer specializing in Supabase, Deno, and Google Sheets

**System Role:** Senior Full-Stack Developer specializing in Supabase, Deno, and Google Sheets API.

**The Mission:** Upgrade the "ClearPath Finance" website (files attached) to a production-ready lead generation system. The goal is to verify user emails via Supabase Auth and then route the data to specific tabs in a Google Spreadsheet based on the user's service selection.

**1. Design & UI Integrity:**
* **Strict Constraint:** Maintain the exact Tailwind CSS theme, "High-end SaaS" aesthetic, typography (`Plus Jakarta Sans`), and layout from the attached `index.html`.
* **Mobile-First:** Ensure all new UI elements (verification modals/states) are perfectly optimized for mobile screens.

**2. The Backend Logic (Supabase + Google Sheets):**
* **Verification Flow:** Use `supabase.auth.signInWithOtp` (Magic Link) to verify the user's email. 
* **Data Routing:** Once the user is verified, trigger a **Supabase Edge Function** (Deno).
* **Multi-Sheet Logic:**
    * The Edge Function must receive the user's data and an array of selected services (e.g., `['Debt', 'Wealth']`).
    * For each service selected, the function must append a row to the **correspondingly named tab** in a single Google Spreadsheet (e.g., if "Debt" is chosen, write to the "Debt" tab).
* **No Admin Panel:** The client will use the Google Spreadsheet as their dashboard.

**3. Technical Deliverables:**
* **`index.html` Update:** Provide the JavaScript logic to handle the OTP verification flow and the call to the Edge Function.
* **Supabase Edge Function (`index.ts`):** Provide the full Deno script using the Google Sheets API (v4). Use a Service Account for authentication.
* **Environment Setup:** List the secrets required in Supabase (Spreadsheet ID, Service Account JSON, etc.).
* **Security:** Include Row Level Security (RLS) and instructions on how to ensure the Edge Function is only callable after valid Auth verification.

**4. Instructions for the Build:**
* Provide the code in a modular format easy to use in a mobile editor (Spck).
* Ensure the Google Sheets integration uses the `append` method to avoid overwriting existing data.

---

Keep this setup only changed that each services leads should be sent to thier own separate spreadsheet
