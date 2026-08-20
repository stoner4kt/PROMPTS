# Create 3 Notion databases under parent page ID: PASTE_PAGE_ID_HERE Use Notion token:

Create 3 Notion databases under parent page ID: PASTE_PAGE_ID_HERE
Use Notion token: PASTE_SECRET_HERE
Databases:
1. Clients — properties: Name (title), Contact (text), Email (email), Phone (phone), Status (select: active, paused, inactive), Supabase ID (text), Created At (date), Updated At (date)
2. Projects — properties: Name (title), Client ID (text), Start Date (date), End Date (date), Invoiced Amount (number dollar), Short Note (text), Staging URL (url), Production URL (url), GitHub URL (url), Services (text), Associated Emails (text), Supabase ID (text), Created At (date), Updated At (date)
3. Documents & Notes — properties: Name (title), Project ID (text), Content (text), File References (text), Supabase ID (text), Created At (date), Updated At (date)
Use Notion API version 2022-06-28.
POST https://api.notion.com/v1/databases
Print each database id at the end so I can save them as:
NOTION_DB_CLIENTS=
NOTION_DB_PROJECTS=
NOTION_DB_DOCUMENTS=

---

Yes create it and create a new parent page for these

---

You are helping me set up a one-way Supabase → Notion sync for my agency portal.

## Repo
https://github.com/stoner4kt/Conextsol-Agencyv2.git 

Read the existing code, especially:
- supabase-schema.sql
- supabase/functions/deadline-alerts/index.ts (use this as the style/pattern for the new Edge Function)
- src/types.ts
- src/supabaseService.ts

## Goal
When rows are inserted, updated, or deleted in Supabase, sync them to Notion.
Also backfill all EXISTING data from Supabase into Notion once.

ONLY these 3 tables:
1. clients
2. projects
3. documents_and_notes

Do NOT sync retainers or ai_tool_accounts.

## What I need you to do

### 1. Create the Edge Function file
Create/edit this file in the repo:

supabase/functions/sync-to-notion/index.ts

Requirements for the function:
- Deno Edge Function, same style as deadline-alerts (cors, serve, env secrets)
- Handle Supabase Database Webhook payloads:
  { type: "INSERT"|"UPDATE"|"DELETE", table: string, record: {...}, old_record: {...} }
- On INSERT/UPDATE: upsert into the matching Notion database
- On DELETE: archive the Notion page (archived: true)
- Match existing Notion pages by a text property named exactly "Supabase ID" (equals the row uuid)
- Support one-time backfill: if the request URL has query param ?backfill=1, use SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY to select * from clients, projects, documents_and_notes and upsert every row into Notion (with ~350ms delay between Notion calls for rate limits)
- Notion API version: 2022-06-28
- Secrets used:
  - NOTION_TOKEN
  - NOTION_DB_CLIENTS
  - NOTION_DB_PROJECTS
  - NOTION_DB_DOCUMENTS
  - SUPABASE_URL (auto in Edge Functions)
  - SUPABASE_SERVICE_ROLE_KEY (auto in Edge Functions)

### 2. Notion property mapping (exact names)

**clients** → NOTION_DB_CLIENTS
- Name (title) ← company_name
- Contact (rich_text) ← primary_contact_name
- Email (email) ← email
- Phone (phone_number) ← phone
- Status (select) ← status
- Supabase ID (rich_text) ← id
- Created At (date) ← created_at (date only YYYY-MM-DD)
- Updated At (date) ← updated_at (date only)

**projects** → NOTION_DB_PROJECTS
- Name (title) ← project_name
- Client ID (rich_text) ← client_id
- Start Date (date) ← start_date
- End Date (date) ← end_date
- Invoiced Amount (number) ← invoiced_amount
- Short Note (rich_text) ← short_note (truncate 2000)
- Staging URL (url) ← staging_url
- Production URL (url) ← production_url
- GitHub URL (url) ← github_url
- Services (rich_text) ← services_listed joined with ", "
- Associated Emails (rich_text) ← associated_emails joined with ", "
- Supabase ID (rich_text) ← id
- Created At (date) ← created_at
- Updated At (date) ← updated_at

**documents_and_notes** → NOTION_DB_DOCUMENTS
- Name (title) ← title
- Project ID (rich_text) ← project_id
- Content (rich_text) ← content (truncate 2000)
- File References (rich_text) ← file_references joined with ", "
- Supabase ID (rich_text) ← id
- Created At (date) ← created_at
- Updated At (date) ← updated_at

Handle nulls safely. Truncate long text to 2000 chars. Skip tables not in the map with 200 + skipped.

### 3. Also output for me (in your reply, clearly labeled)

A) The COMPLETE contents of supabase/functions/sync-to-notion/index.ts (ready to copy/upload)

B) Exact secrets to set in Supabase Dashboard → Project Settings → Edge Functions → Secrets:

| Secret name | What value to put |
|-------------|-------------------|
| NOTION_TOKEN | (my Notion integration secret_...) |
| NOTION_DB_CLIENTS | (Clients Notion database UUID) |
| NOTION_DB_PROJECTS | (Projects Notion database UUID) |
| NOTION_DB_DOCUMENTS | (Documents & Notes Notion database UUID) |

Note: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are already available — do not ask me to set those.

C) Deploy command:
npx supabase functions deploy sync-to-notion

D) One-time backfill curl (with placeholders for PROJECT_REF and KEY):
curl -X POST "https://PROJECT_REF.supabase.co/functions/v1/sync-to-notion?backfill=1" \
  -H "Authorization: Bearer YOUR_ANON_OR_SERVICE_ROLE_KEY" \
  -H "Content-Type: application/json"

E) Database Webhooks setup — create 3 webhooks in Supabase Dashboard → Database → Webhooks:

For each of tables: clients, projects, documents_and_notes
- Events: Insert, Update, Delete
- Type: HTTP Request, Method POST
- URL: https://PROJECT_REF.supabase.co/functions/v1/sync-to-notion
- Headers:
  Authorization: Bearer YOUR_ANON_KEY
  Content-Type: application/json

F) Order of operations checklist:
1. Set the 4 secrets
2. Deploy function
3. Run backfill once
4. Create the 3 webhooks
5. Test by editing a client in Supabase and confirming Notion updates

### 4. Optional: short README section
If you edit the repo, add a short section to README-SUPABASE-VERCEL.md titled "Notion Sync" with the secrets, deploy, backfill, and webhook steps.

## Constraints
- Do not invent extra tables
- Do not require Notion relations (store client_id / project_id as text)
- Idempotent: backfill and webhooks both upsert by Supabase ID
- Match coding style of existing edge functions in this repo

Generate the complete edge function first, then the secrets table, then the exact steps I should follow.

---

Where do i run the backfill as i have already deployed the function and set the secret

---

Can i run it in termux or a replit and how do i do so step by step guide please

---

This is what i get  when i run the curl command in a replit ( /workspace$ curl -X POST "https://lutlyvmcddmennmppbgw.supabase.co/functions/v1/sync-to-notion?backfill=1" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx1dGx5dm1jZGRtZW5ubXBwYmd3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQxMjc1NjYsImV4cCI6MjA5OTcwMzU2Nn0.ob8vKtgYyleyNtwfCeUTeJ9t1qjPZpCohe-KRtOUc_A" \
     -H "Content-Type: application/json"
{"success":true,"backfill":true,"summary":{"clients":{"total":11,"results":[{"id":"d2d17e3c-4d6e-4f1c-860c-512f1e5a4749","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"23c5f325-3357-4ba9-882b-2e41e764895f\"}"},{"id":"98aa2aff-ea54-442d-a961-b370a3942d8e","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"3d7efb1d-a747-4d91-900e-629984ef4cb7\"}"},{"id":"d55d13ed-fe87-40ce-9c6b-e65307297f38","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"2f2a1a8f-a9d3-4ab5-b4c7-e550b8a132aa\"}"},{"id":"4b15f409-1ec4-4bc5-aeb7-1f57e5ff20da","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"f4af7c6c-e8c1-4a01-ba32-528bca9b3d0c\"}"},{"id":"82130fd0-fe6a-4020-9fac-ebd616818b76","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"7b4791b2-e97d-4c38-943c-9833a891feb6\"}"},{"id":"3e468323-3e12-4384-a82b-0361908ab32d","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"54542a77-606f-4487-a0ec-b478717d7092\"}"},{"id":"bbdcbc65-1789-4e50-82cb-2f6065ae1163","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"5afa16f1-cd73-4e64-9580-d2af161191b2\"}"},{"id":"ca5bbea4-0472-4418-880e-28f710d68d0e","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"e0c3d698-945b-4986-bc7b-da040a780c10\"}"},{"id":"a55f574a-f5b5-4743-b6ae-d8ea33a61b58","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"e96601c6-7715-478c-b48a-e756f4b75702\"}"},{"id":"a9e822d5-927e-4651-9766-1e2e84e57110","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"be530a35-8199-424e-9be5-8b6111427b9a\"}"},{"id":"b2fb4186-e828-4f60-9c01-f1ed20301693","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: 9d13b0e6-f0f8-4832-a776-5ad1bd754586. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"7784fc92-b632-4deb-b8e8-bcdc1fa22764\"}"}]},"projects":{"total":12,"results":[{"id":"a6ac4f2c-fe73-46f9-9c01-975f6c00c57a","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"872d798f-83df-4e44-ba0b-b3077afb8462\"}"},{"id":"000835c7-f460-4f84-8fba-fe494742767c","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"bfc06135-f056-4290-9b69-0971018d58cf\"}"},{"id":"57c5e965-82c3-4842-a555-a5d9d87150bc","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"35bb771d-1411-4a37-a8fc-57e22d885891\"}"},{"id":"c04e0910-4cff-4073-99de-940ec490559a","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"44b49768-b8aa-47fb-a1be-a7c92815aa03\"}"},{"id":"85364948-21e0-45ac-94dd-947ec8a4416a","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"c4457668-a91b-4ae8-a3b8-d9bf6861a6e4\"}"},{"id":"06f59ffc-7203-4af4-831d-d771c2212ac8","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"69e3ad9d-4dfd-4c02-9b6a-aec14c26988e\"}"},{"id":"cc21bd1e-2dd6-47d3-86f3-b3021d89f4e9","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"dd7ad76b-45d4-4091-a703-59c71324724e\"}"},{"id":"95f0f007-fd98-438a-b254-4d9d252ea7c2","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"a0d63ef9-c17d-455f-8392-11ad8fadc986\"}"},{"id":"b35dfc59-cd74-4692-8e55-d73e5a17f401","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"6463b7cc-a734-4470-b118-34177566e37d\"}"},{"id":"3760e0ec-a254-4eb2-a28f-a1415b14f4de","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"6f088408-27ad-4142-abf8-1f14a3285025\"}"},{"id":"fcb261a3-2905-4ca6-98e5-e1b759103be6","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"355c6af2-8e98-4504-b1da-9d034ebebc6e\"}"},{"id":"9cacfaf2-11fa-4d08-ad7d-f7a448a9bb52","action":"error","error":"Notion query failed (404): {\"object\":\"error\",\"status\":404,\"code\":\"object_not_found\",\"message\":\"Could not find database with ID: b9f1872c-2a6a-4b77-99f9-580952a6029c. Make sure the relevant pages and databases are shared with your integration \\\"Conextsol Supabase sync\\\".\",\"additional_data\":{\"integration_id\":\"3aed913d-282f-8144-8e44-00279a59dba2\"},\"request_id\":\"5e0f13dc-d64
~/workspace$ )
