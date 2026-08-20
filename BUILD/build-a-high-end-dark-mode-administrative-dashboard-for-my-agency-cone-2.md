# Build a high-end, dark-mode administrative dashboard for my agency, **Conextsol**, using only

Build a high-end, dark-mode administrative dashboard for my agency, **Conextsol**, using only **Vanilla HTML5, Tailwind CSS (via CDN), and Vanilla JavaScript**. This dashboard is the manual data-entry interface for my 'Rick Sanchez Brain' system, which uses **Supabase** as the backend.

**Design Aesthetic:**
- Theme: Deep Zinc/Black (SaaS Dark Mode).
- Background: `#09090b`, Cards: `#18181b`, Borders: `#27272a`.
- Accents: Rick Sanchez Blue (`#3b82f6`) and Purple (`#a855f7`).
- Feel: Clean, industrial, mobile-responsive, and fast.

**Functional Requirements:**
1. **Supabase Integration**: Use the Supabase JS CDN. Include an initialization section where I can paste my `SUPABASE_URL` and `SUPABASE_ANON_KEY`.
2. **Data Entry Modules (Manual Forms)**:
   - **Client Onboarding**: Fields for Name, Contact Person, Email, Industry, and Status (Dropdown: Lead, Active, Paused, Completed, Lost).
   - **Project Manager**: Fields for Client Selection (Dropdown), Project Name, Phase (Dropdown: Discovery, Design, Development, QA, Launch, Live), Tech Stack, and Budget.
   - **Task Board**: Fields for Task Title, Client Selection, Priority (Dropdown: Low, Medium, High, Urgent), and Due Date.
   - **Knowledge Base**: A simple Markdown-friendly textarea to save notes and meeting summaries.
3. **One-Shot 'Rick Mode' Onboarding**: A special wizard form that allows me to create a Client AND a Project simultaneously in one submission.
4. **Activity Logging**: Every time a form is submitted successfully, the script must also insert a record into the `activity_log` table with the action 'created' and the corresponding entity type.
5. **Security**: Do NOT include any credential/password fields. This UI is for non-sensitive agency data only.

**Technical Specifics:**
- Use `lucide-icons` (via CDN) for a premium look.
- Ensure all forms use `async/await` for Supabase inserts.
- Add success/error toast notifications that feel 'Rick-themed' (e.g., 'Data saved. *Burp*').
- Layout: A sticky sidebar for navigation and a main content area for the active form.

**Deliverable**: Provide the code in a single-file `index.html` structure (containing CSS and JS) so I can easily run it in Spck Editor or a browser and host on netlify and optimize the design of the dashboard for mobile screens and devices ensure i am able to add data on my mobile device

---

Fix the navbar not working

---

So i want to secure Rick and have the supabase anon key and url in the secrets and also have a login page to add more security. Generate me the frontend for this system using html, css, js , giving each form a detailed page according to Rick and create a dashboard to view the overall performance of the system, like active projects, active tasks, etc. I want to use this interface, I'm building as  a alternative way for me to enter data into my database and use Rick's telegram interface to query this data. Optimize it for all screens and devices especially mobile and laptops ensuring no overflow. Generate this in a repo I can download and host on netlify
