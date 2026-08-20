# You are an expert full-stack developer specializing in Next

You are an expert full-stack developer specializing in Next.js 14+ (App Router), Tailwind CSS, Supabase, and Postgres. 

Please build a complete, production-ready internal Client & Project Management Portal for my agency, "Conextsol". The interface must be fully optimized for mobile devices first, scaling gracefully to desktop, and styled with a professional, clean "purplish-green" modern UI theme (e.g., deep purples for primary branding/sidebars, accented with vibrant energetic emerald or mint greens for actions, positive statuses, and highlights, balanced with neutral grays).

Secure the entire dashboard using Supabase's built-in Email/Password Authentication.

---

### 1. UX WORKFLOW & INTERFACE REQUIREMENTS

- **Linear Onboarding Wizard (Crucial Feature):** When adding a new client, do not treat "Add Client", "Add Project", and "Add Documentation" as separate standalone features. Instead, build a chained, step-by-step modal or wizard interface. 
  1. **Step 1:** Fill out Client Information. Upon clicking submit, the system inserts the client and receives the generated `client_id`.
  2. **Step 2:** The UI automatically forwards to the "Add Project" form, implicitly passing and linking that new `client_id` behind the scenes. 
  3. **Step 3:** Once the project is submitted and the `project_id` is generated, the UI forwards to the "Add Initial Documentation" form, automatically linking it to the project.
- **Mobile Optimization:** Every table, form, modal, and navigation element must be optimized for mobile screens. Use responsive grids, collapsible sidebars/bottom navigation bars for mobile, stackable table rows (cards) on small viewports, and touch-friendly button sizes.
-- All documents should be editable by me the admin only
---

### 2. EXACT DATABASE SCHEMA (SUPABASE / POSTGRES SQL)

Generate and provide the exact PostgreSQL migration scripts to create these tables, including appropriate foreign keys (`ON DELETE CASCADE`), indexes for performance, and timestamps:

1. **`clients` Table:**
   - `id`: UUID (Primary Key, default: `gen_random_uuid()`)
   - `company_name`: Text (Required)
   - `primary_contact_name`: Text (Required)
   - `email`: Text (Required)
   - `phone`: Text
   - `status`: Text (e.g., 'active', 'paused', 'inactive')
   - `created_at` / `updated_at`: Timestamptz

2. **`projects` Table:**
   - `id`: UUID (Primary Key)
   - `client_id`: UUID (Foreign Key linking to `clients.id`)
   - `project_name`: Text (Required)
   - `start_date`: Date
   - `end_date`: Date
   - `invoiced_amount`: Numeric (Representing the fixed amount invoiced)
   - `short_note`: Text (A brief operational summary)
   - `staging_url`: Text
   - `production_url`: Text
   - `github_url`: Text
   - `services_listed`: Text[] or JSONB (Array of specific project services delivered)
   - `associated_emails`: Text[] or JSONB (Emails specifically tied to managing these services)
   - `created_at` / `updated_at`: Timestamptz

3. **`retainers` Table:** (Kept separate from one-off projects but references the client)
   - `id`: UUID (Primary Key)
   - `client_id`: UUID (Foreign Key linking to `clients.id`)
   - `service_type`: Text (e.g., 'web hosting', 'web maintenance', 'SEO', 'Google Ads')
   - `billing_amount`: Numeric (Fixed recurring price)
   - `billing_cycle_day`: Integer (The day of the month the payment is due, e.g., 1 for the 1st of every month)
   - `is_active`: Boolean (Default: true)
   - `created_at` / `updated_at`: Timestamptz

4. **`documents_and_notes` Table:**
   - `id`: UUID (Primary Key)
   - `project_id`: UUID (Foreign Key linking to `projects.id`)
   - `title`: Text
   - `content`: Text (Support for Markdown or Rich Text notes)
   - `file_references`: Text[] (Array of URLs/paths for files uploaded to Supabase Storage or external assets)
   - `created_at` / `updated_at`: Timestamptz

---

### 3. AUTOMATION, EDGE FUNCTIONS & NOTIFICATIONS

Please write the complete code and configuration setup for the following automated tasks:

1. **Project Deadline Alerts (Cron Job):**
   - Create a scheduled background function (or pg_cron script calling a Supabase Edge Function) that runs once a day.
   - It must scan the `projects` table for any records where `end_date` is exactly **2 days away**.
   - Trigger an external notification (provide placeholders/boilerplate code for a webhook call to Telegram or WhatsApp API). Include the project name and client details in the alert. Ensure the architecture allows adding more custom alert types easily in the future.

2. **Retainer Invoicing Alerts(Edge Function):**
   - Create a scheduled function that runs daily to check the `retainers` table.
   - It must identify any active retainers where the current day of the month matches `billing_cycle_day`.
   - When triggered, it must execute a Supabase Edge Function that :
     1. Send a  notification alert to me (the agency admin) via webhook Telegram telling me which client is due to for payment 

---

### 4. DELIVERABLES REQUIRED

Please output the following across a structured, production-ready framework:
1. **System Architecture & Directory Tree:** A clean text-map of the entire Next.js repository using TypeScript, layout files, components, and Supabase integration directories.
2. **PostgreSQL Schema Script:** The exact raw SQL to copy-paste into the Supabase SQL editor (including tables, constraints, Row Level Security (RLS) basics protecting data behind auth, and sample helper indexes).
3. **Frontend Code:** Clean, fully responsive Next.js functional components using Tailwind CSS for the main layout, dashboard summary view, the chained onboarding wizard, and client/project detail views.
4. **Edge Function & Cron Configuration:** Complete TypeScript file for the automated notifications and email triggers.
5. **Detailed Comprehensive README & Setup Guide:** A complete step-by-step deployment and operational manual explaining how to initialize the local Next.js workspace, connect the `.env` parameters to Supabase, launch the SQL schema, configure the cron jobs, and push the Edge Functions to live production.
