# You are a Senior Staff Engineer specializing in serverless architectures, Supabase, Cloudflare

You are a Senior Staff Engineer specializing in serverless architectures, Supabase, Cloudflare Workers, and Notion API integrations.

Analyze the existing repository:
https://github.com/stoner4kt/Conextsol-Agencyv2.git 

Current system summary (already implemented):
- Vite + React 19 + TypeScript + Tailwind frontend
- Supabase PostgreSQL (clients, projects, retainers, documents_and_notes, ai_tool_accounts, alerts)
- Existing Supabase Edge Functions: deadline-alerts, retainer-billing
- Admin vs client RLS policies based on email domain @conextsol.co.za or reeqieric41@gmail.com
- Pattern: Sidebar + multiple Dashboard components + supabaseService.ts + types.ts

GOAL
Add a complete automated morning lead-generation agent that:
1. Runs on Cloudflare Workers (cron at 07:00 UTC + manual /run endpoint)
2. Scrapes three sources in parallel (Reddit, Upwork RSS, niche directory via Cloudflare Browser Rendering)
3. Writes every lead FIRST to a new Supabase `leads` table, THEN to a Notion database
4. Supports an on/off toggle (stored in Cloudflare KV) that can be controlled from the UI
5. Provides a full admin dashboard inside the existing React app to view, filter, update status, and delete leads
6. Creates the Notion database schema programmatically so no manual column setup is required
7. Deploys automatically via GitHub Actions

YOUR DELIVERABLES (in this exact order)

### PART 1 – Backend / Worker / Schema (do this yourself)

1. Full project structure for the new Cloudflare Worker (recommended folder: `lead-agent-worker/` at repo root).
   - Complete `wrangler.toml` (cron, browser binding, KV binding, compatibility flags)
   - Complete production-ready `src/index.js` (ES modules) with:
     - GET /init-database → creates the Notion database under env.NOTION_PARENT_PAGE_ID and returns the new database ID
     - GET /run → forces a scrape run
     - POST /toggle → body { "enabled": true|false } (protected by shared secret)
     - GET /status → returns enabled state + last run summary
     - Cron handler that respects the enabled flag
     - Parallel scrapers with Promise.allSettled
     - Write pipeline: Supabase first → Notion second
     - Proper error boundaries, truncation (100 char title, 2000 char summary), deduplication by origin_url
     - Uses env vars only – never hardcode secrets
   - package.json for the worker

2. Exact SQL migration I must run in the Supabase SQL Editor (CREATE TABLE leads + indexes + RLS + trigger). Make it idempotent and match the existing style of supabase-schema.sql.

3. Precise secrets & configuration checklist:
   - Cloudflare secrets (wrangler secret put …)
   - Cloudflare KV namespace creation commands
   - Supabase environment variables needed
   - Notion integration requirements (parent page sharing, token scopes)
   - Optional shared secret for protecting /run, /toggle, /init-database
   - Exact list of environment variable names that must exist in the Worker

4. After the worker is ready, instruct me how to call /init-database (with the correct headers) so that Claude itself can tell me the Notion Database ID that is returned. You must generate the full curl command I should run, and then wait for me to paste the returned database_id back to you so you can confirm the configuration.

### PART 2 – Generate a SECOND, self-contained prompt

After you have finished PART 1, generate a completely separate, copy-paste-ready prompt that I can feed into Codex or Google AI Studio.

That second prompt must:
- Assume the Worker + SQL + secrets from PART 1 are already done
- Instruct the model to make ONLY the frontend + deployment changes to the same repo
- Add a new “Leads” tab and full LeadsDashboard component that matches the existing design system (Sidebar, DashboardStats style, Tailwind, lucide icons)
- Extend types.ts, supabaseService.ts, App.tsx, Sidebar.tsx
- Implement the agent on/off toggle that calls the Worker /toggle endpoint
- Show last-run status from /status
- Allow admin users to change lead status and delete leads
- Create the necessary GitHub Actions workflow(s) so that:
  - The Cloudflare Worker deploys automatically on push to main (using cloudflare/wrangler-action)
  - The frontend continues to deploy to Cloudflare  Pages (or whatever is already configured)
- Include any new environment variables that need to be added to the frontend (.env.example, Vercel, etc.)
- Be extremely precise about file paths and code style so the model can implement without asking clarifying questions

Do not implement the UI yourself in PART 1. Only produce the second prompt.

Start by examining the real repository structure, then produce PART 1 completely, then the second prompt.

---

Is my notion database already created

---

Please generate the notion database and provide me with the id's and the sql schema for them and the prompt to finish the others steps and what secrets to set
