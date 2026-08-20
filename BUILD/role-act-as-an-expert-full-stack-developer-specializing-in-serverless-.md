# Role: Act as an Expert Full-Stack Developer specializing in Serverless Architecture and

Role: Act as an Expert Full-Stack Developer specializing in Serverless Architecture and AI Integrations.
Objective: Build a "Second Brain & Project Manager" bot for my Web Dev Agency.
The Tech Stack:

   1. Frontend: Telegram Bot (User Interface).
   2. Backend: Cloudflare Workers (Runtime).
   3. LLM: Google Gemini 1.5 Flash (via Google AI Studio Free API).
   4. Database: Notion (For Task Tracking and Knowledge Base).

What I need from you:

   1. Notion Setup: Explain how to structure a "Tasks & Projects" database in Notion (properties/columns like 'Status', 'Due Date', 'Priority' needed) so the API can read/write to it correctly.
   2. Cloudflare Worker Code (index.js): Provide a complete, production-ready JavaScript file for a Cloudflare Worker that:
   * Authenticates incoming Webhooks from Telegram.
      * Routes messages to the Gemini 1.5 Flash API using a System Prompt that defines its persona as an "Agency Project Manager."
      * Includes Function Calling (Tool Use) so Gemini can decide when to "Create a Task in Notion" or "Search my Notion Knowledge Base."
      * Handles the fetch requests to the Notion API and Telegram sendMessage API.
   3. Environment Variables: List the specific Secrets needed to set in the Cloudflare Dashboard (e.g., TELEGRAM_TOKEN, GEMINI_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID).
   4. Step-by-Step Mobile Instructions: Provide a clear guide on how to deploy this using only a mobile browser (Cloudflare Quick Edit) and how to set the Telegram Webhook using a URL string.

Persona for the Bot: The bot should be professional, concise, and focused on web development workflows (UI/UX, Frontend, Backend, SEO). It should automatically suggest deadlines or tech stacks when a new project is mentioned.
So i want to use the second brain to store project details, data, documentation etc and client data and information, using telegram to insert it into the database where necessary, also I want to be able to add/edit things. I'll use the gemini api to query the databases if I need quick information on something. Also I'm doing this build on mobile so I need a setup that doesn't require wrangler. Okay so how would I get the data into the database from telegram, let's say I want to store specific information, details or documentation for a specific client, edit or pull up certain info Or how I add information on to the database, let's say I want to add a new client with their respective information. Create the notion database for me aswell as the telegram command/ KV's aswell as step by step how to setup everything in a readme setup guide and all the others files I might need and explain to me what the capabilities of the gemini free api is and and what I can use the bot for as well as the limitations. I'll also be using Zoho invoices so the bot can track my financies, draft invoices for my approval and zoho mail so it can help my draft email outreach and responses
