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
-

---

Create the notion database for me aswell as the telegram command/ KV's aswell as step by step how to setup everything in a readme setup guide and all the others files I might need and explain to me what the capabilities of the gemini free api is and and what I can use the bot for as well as the limitations

---

So i want to use the second brain to store project details, data, documentation etc and client data and information, using telegram to insert it into the database where necessary, also I want to be able to add/edit things. I'll use the gemini api to query the databases if I need quick information on something. Also I'm doing this build on mobile so I need a setup that doesn't require wrangler

---

Okay so how would I get the data into the database from telegram, let's say I want to store specific information, details or documentation for a specific client, edit or pull up certain info Or how I add information on to the database, let's say I want to add a new client with their respective information

---

Now  i want to link client with their data and projects, so I can make notes for a specific client and edit, track or query like the system currently does

---

So Shopr ZA is just a placeholder for my client business name

---

Okay generate me all the files I need togather with the set up guide step by step , with a guide for commands and what they do and how to add, edit data

---

Build me this complete build with a step by step setup and how to use it and how to set everything up step by step on mobile. Include all the current features with the features discussed in the pdf

---

"I have built a dual-agent 'AgencyOS' system consisting of:

A Cloudflare Worker (index.js): Handles reactive Telegram messages and website form leads.

A PicoClaw VPS Agent (config.json): Handles proactive background tasks like uptime monitoring and cron jobs on a GCP free tier.

I want to expand this system to support Discord as a secondary output channel while keeping Telegram active. Specifically, I want to:

In the Cloudflare Worker: When a new lead comes in via the contact form or a critical error is logged, I want it to post to a Discord Webhook in addition to sending a Telegram message.

In the PicoClaw VPS Agent: I want the cron job summaries (like the morning standup and weekly reports) to be sent to a specific Discord channel so I have a persistent log there.

Infrastructure: I want to maintain the 'Free Tier' status, so I prefer using Discord Webhooks (no heavy libraries) for the Worker and updating the channels configuration in PicoClaw.

Please provide:

The updated index.js logic for the Cloudflare Worker to include a sendToDiscord helper function and its implementation in the lead-capture flow.

The updated config.json structure for PicoClaw to enable the Discord channel alongside Telegram.

A list of the new Environment Variables/Secrets I need to add to my Cloudflare Dashboard and my .secrets file.

I have attached my current index.js, config.json, and schema.sql for reference. Please ensure the Discord 'Embeds' are formatted professionally with colors (Green for success, Red for alerts. Build me this complete build with a step by step setup and how to use it and how to set everything up step by step on mobile. Include all the current features with the features discussed above

---

Provide me with all the files, code, workers I need with a step by step setup guide on how to setup this build on mobile step by step. Provide me with a setup readme and a how to use it aswell as i will be starting to move my data from my brain and scattered notes for each client into this system. Also generate a documentation guide listing all the tools and services we used and the role they play also what variables goes where

---

Provide me with all the files I need to setup this build with a step by step guide to setting everything up from the vps completely to the notion database, discord channels and the website form connection step by step on mobile.

---

# CONEXTSOL AI AGENT V3: FINAL "RICK" DEPLOYMENT PROMPT

I am Tashreeq, the owner of Conextsol. I have uploaded my "AgencyOS v6" files (index.js, config.json, setup-vps.sh, schema.sql, notion-setup.js). 

I need you to perform a final, complete reconstruction of these files to transform the agent into "Rick" — my Virtual COO, PA, Second Brain, Finance Advisor, and Marketing Advisor.

## 1. MISSION & IDENTITY
- **Agent Name:** Rick.
- **Primary Goal:** Generate $100k (ZAR 1.8M) in the next 3 months.
- **Roles:** - **Second Brain:** Persistent documentation/credential storage via Supabase Vector Search.
  - **Marketing Advisor:** Automated "Social Growth Packs" for FB, IG, TikTok, and Twitter.
  - **Finance Advisor:** Tracking the 100k goal and drafting Zoho Invoices.
  - **PA/Employee:** Managing Notion, emails, and monitoring uptime.

## 2. ZOHO INTEGRATION (FREE TIER)
Modify index.js and config.json to support:
- **Zoho Invoice:** Rick must pull budget data from Notion and DRAFT branded invoices in Zoho. He provides the draft link for my approval (no auto-sending).
- **Zoho Mail:** Rick must scan my inbox, summarize client requests, and draft reply suggestions to Telegram (no auto-reply).

## 3. MULTI-MODEL "SPECIALIST" ROUTING
Update the architecture to route tasks based on strengths:
- **COO (Gemini 2.0 Flash):** Primary brain for Notion, Zoho, and Big-Picture strategy.
- **Speedster (Llama 3 via Groq):** Quick Telegram responses and technical terminal commands.
- **Writer (Mistral via Hugging Face):** Generating the creative social media content.

## 4. OMNICHANNEL MARKETING CRON
Add a cron job to config.json that scans 'Done' tasks in Notion and generates:
- 📘 Facebook: High-engagement professional post.
- 📸 Instagram: Caption + Carousel visual description.
- 🎵 TikTok: 30-second script focusing on the 'Result'.
- 🐦 Twitter: 3-tweet thread on the technical 'Win'.

## 5. REVENUE-DRIVEN PRICING ADVISOR
In the system_prompt, instruct Rick to generate 3-tier value-based quotes (ZAR) for every lead:
- **Tier 1 (Anchor):** Premium DFY.
- **Tier 2 (Growth):** The target offer.
- **Tier 3 (Entry):** Low-friction foot-in-the-door.

## 6. OUTPUT REQUIRED
Please generate the full code for:
1. **index.js** (Cloudflare Worker with Zoho & Multi-Model logic).
2. **config.json** (VPS Config with all 100k Growth crons).
3. **A Step-by-Step Setup Guide** for Tashreeq on how to:
   - Setup the Google e2-micro VPS and run the setup-vps.sh.
   - Configure the 6 Notion databases (adding 'Invoices' and 'Finances').
   - Connect Zoho (Console setup), Groq, and Hugging Face.
   - Connect the website form-integration.js to the new Rick system.

---

Provide me with all the files, code, workers I need with a step by step setup guide on how to setup this build on mobile step by step. Provide me with a setup readme and a how to use it aswell as i will be starting to move my data from my brain and scattered notes for each client into this system. Also generate a documentation guide listing all the tools and services we used and the role they play also what variables goes where. Provide me with all the files I need to setup this build with a step by step guide to setting everything up from the vps completely to the notion database, discord channels and the website form connection step by step on mobile and everything else

---

Okay instead let's remove discord and have all the notifications we would have sent to discord go to the telegram bot with labels for each

---

Okay instead let's remove discord and have all the notifications we would have sent to discord go to the telegram bot with labels for each. Remove Pico and the vps as we will use a server less build, we will only use one api (gemini api).
