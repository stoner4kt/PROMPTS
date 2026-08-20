# -FIRST MASTER PROMPT Role: Expert Automation Architect & Mobile Developer

-FIRST MASTER PROMPT
Role: Expert Automation Architect & Mobile Developer.
Context: I am a solo web developer working entirely from a mobile device (using Spck Editor and mobile browsers). I am building a "Business Second Brain" to move from manual management to passive monitoring.

Objective: Provide a production-ready system to manage my agency workflows via a single Telegram bot connected to Notion via Cloudflare Workers.

Please provide the following in a mobile-optimized format:

1. The Notion Blueprint (Mobile-Friendly Setup):

The Notion Schema: Define the exact properties (columns) I need for 3 databases:

Client CRM: Name, Status (Select), Hosting Info (Text), Total Projects (Rollup).

Project Tracker: Name, Client (Relation), Status (Status), GitHub Repo (URL), Last Update (Date).

Snippet Vault: Topic (Title), Code (Text), Tags (Multi-select), Related Project (Relation).
2. The "Single Bot" Worker Code (ES Module):

Provide a complete worker.js script for a Cloudflare Worker using Standard Fetch (no external npm libraries or SDKs) to ensure I can edit it directly in the Cloudflare Dashboard mobile editor.

The code must handle these specific commands:

/status: Lists active projects from the tracker.

/client [name]: Returns hosting/contact info from the CRM.

/log [note]: Adds a timestamped entry to the Daily Log or Inbox.

/snippet [tag]: Searches the Vault and returns code in a Markdown code block.

Include a switch statement for command routing and a simple notionQuery helper function.

3. Mobile Setup Guide:

Step-by-step for BotFather (Telegram).

Step-by-step for creating an Internal Integration at developers.notion.com.

Instructions for adding Secrets (Environment Variables) in the Cloudflare Mobile Dashboard (NOTION_TOKEN, BOT_TOKEN, DB_CLIENTS, DB_PROJECTS, DB_SNIPPETS).

Provide the exact Browser URL I need to visit to set my Telegram Webhook without using a terminal.

4. Constraints:

The entire build must remain in the Free Tiers of all three services.

Ensure all code blocks are formatted for easy selection/copying on a smartphone screen

---

Uhm
