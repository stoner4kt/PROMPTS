# To upgrade your **Rick Sanchez Conextsol Brain** to v2

To upgrade your **Rick Sanchez Conextsol Brain** to v2.1, you can use the prompt below. I have structured it to ensure the AI understands how to integrate the new "One-Shot Onboarding" and "JSON Export" features into your existing `worker.js` logic while maintaining the "Rick" personality.

### 📝 The Claude Prompt

Copy and paste the entire block below into Claude:

***

**Role:** Expert Cloudflare Workers & JavaScript Developer.
**Task:** Update the provided `worker.js` for an AI agent named "Rick Sanchez."

**New Features to Add:**
1.  **Combo Onboarding Tool:** Create a tool named `onboard_client_project`. It must create a client in the `clients` table, retrieve the generated `id`, and then immediately create a project in the `projects` table linked to that client ID.
2.  **JSON File Export Tool:** Create a tool named `export_to_file`. It should fetch data from a specified Supabase table (clients, projects, or tasks) and send it to the user as a `.json` file using the Telegram `sendDocument` API instead of a standard message.
3.  **Prompt Updates:** Update the `SYSTEM_PROMPT` to include these new capabilities and instructions on when to use the file export (e.g., when the user asks for a "report" or "file").

**Technical Requirements:**
- **Telegram File Handling:** Implement a helper function `sendTelegramFile` using `FormData` and `Blob` to handle the `sendDocument` request.
- **Atomic-ish Logic:** Ensure the onboarding tool checks for the successful creation of the client before attempting to create the project.
- **Maintain Style:** Keep all existing v2.0 features (Vector search, history pruning, encryption, and the Rick Sanchez personality).
- **Output:** Provide the full, updated `worker.js` code in a downloadable file
