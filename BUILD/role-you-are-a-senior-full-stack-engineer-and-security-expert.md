# **Role:** You are a Senior Full-Stack Engineer and Security Expert

**Role:** You are a Senior Full-Stack Engineer and Security Expert.
**Context:** I am building a high-end, dark-mode administrative dashboard for my agency, **Conextsol**. This is the manual data-entry interface for my 'Rick Sanchez Brain' system. I have attached the system's codebase and schema in the zip file.

**Objective:** Build a complete, mobile-optimized "Brain OS" Dashboard that I can host on Netlify.

**Security Requirements (Strict):**

1. **Frontend Privacy:** The frontend must ONLY use the `SUPABASE_ANON_KEY`. It must never see or store the `SERVICE_ROLE_KEY`.
2. **Auth Gate:** The dashboard must be locked behind a Supabase Auth login screen (Email/Password).
3. **The Bridge:** Create a **Netlify Function** (Node.js) that acts as a secure bridge. The frontend will call this function; the function will pull `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` from Netlify Environment Variables to perform administrative writes (bypassing RLS for me, the admin).
4. **No Password Storage:** This UI is for data management, not for viewing sensitive credentials (the Telegram bot handles the vault).

**Design Aesthetic:**

* **Theme:** Deep Zinc/Black (`#09090b`).
* **Cards/Borders:** `#18181b` / `#27272a`.
* **Accents:** Rick Sanchez Blue (`#3b82f6`) and Purple (`#a855f7`).
* **Responsiveness:** Mobile-first design with a bottom navigation bar for small screens and a sticky sidebar for laptops. No horizontal overflows.

**Functional Requirements:**

1. **Dashboard Overview:** A summary view showing total active projects, open tasks, and a live activity feed pulling from the `activity_log` table.
2. **Management Modules:** Detailed, mobile-friendly forms and list views for:
* **Clients:** (Name, Contact, Email, Industry, Status).
* **Projects:** (Linked to Client, Phase, Tech Stack, Budget).
* **Tasks:** (Title, Client, Priority, Due Date).
* **Knowledge Base:** Markdown-ready notes storage.


3. **Rick Mode (One-Shot Onboarding):** A specialized wizard to create a Client and their first Project in a single transaction.
4. **Activity Integration:** Every action taken in this dashboard must trigger a log entry in the `activity_log` table (Action: 'created', Entity: corresponding type).

**Deliverables:**

1. **`index.html`**: A single-file frontend using Vanilla JS, Tailwind CSS (via CDN), and Lucide Icons.
2. **`netlify/functions/brain-bridge.js`**: The Node.js code for the Netlify function to handle secure database writes.
3. **`README.md`**: A step-by-step setup guide for Netlify, including which environment variables to set and how to invite the first admin user in Supabase.

**Reference the attached `schema.sql` and `worker.js` to ensure all field names and Enum types (Client Status, Project Phase, etc.) match my existing database exactly.**

---

---

Build me this entire repo into a zip file I can download with all the necessary files and a step by step setup guide on how to setup everything on mobile indepth
