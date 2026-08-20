# To get a clean, downloadable file from Claude, you need a prompt

To get a clean, downloadable file from Claude, you need a prompt that explicitly tells it to merge your current logic with the new optimizations while maintaining the "Rick Sanchez" personality and the existing security features[cite: 1, 2].

### The Prompt for Claude
Copy and paste the text below into Claude, then **upload or paste your `worker.js` and `schema.sql.txt` files** along with it.

---

**PROMPT:**
"I am providing you with my current `worker.js` and `schema.sql.txt` for a Cloudflare Worker bot named 'Rick Sanchez Conextsol Brain'[cite: 2, 3]. Please provide a complete, updated `worker.js` file that implements the following two optimizations:

1. **AI Efficiency & Vector Search (RAG):**
   - Use the `text-embedding-004` model to generate embeddings for any text sent to the Knowledge Base via the `create_kb` tool[cite: 1].
   - In the `cmdAI` function, before calling Gemini, perform a semantic search by calling the Supabase RPC function `match_kb`[cite: 1].
   - Inject the retrieved relevant notes into the system context so Rick can 'remember' details accurately[cite: 1].

2. **History Pruning & Summarization:**
   - Implement a logic that monitors the conversation history length[cite: 1].
   - When history exceeds `MAX_HISTORY`, use Gemini to summarize the oldest messages into a concise 'Memory' block, then replace those messages with the summary to keep the context window clean[cite: 1].

**Requirements:**
- **Preserve Personality:** Maintain the blunt, sarcastic Rick Sanchez persona in all responses[cite: 2].
- **Preserve Security:** Do not change the AES-GCM encryption/decryption logic for credentials[cite: 2].
- **Complete File:** Output the ENTIRE updated `worker.js` file in a single code block so I can use your 'Download' feature.
- **Dependencies:** Ensure the code uses standard `fetch` for API calls to Gemini and Supabase as it currently does[cite: 2]."

---

### Step-by-Step Implementation Guide
Since you are updating a **live bot** from South Africa using a mobile-first workflow (like Spck Editor or Termux), follow these steps to avoid downtime[cite: 1]:

1.  **Update the Database First:**
    *   Before you deploy the new code, go to your Supabase SQL Editor and run the SQL provided in the previous turn (enabling `pgvector` and adding the `embedding` column)[cite: 1, 3]. If the column doesn't exist when the new code tries to write to it, the bot will crash.
2.  **Generate the File in Claude:**
    *   Feed Claude the prompt above with your files.
    *   Click the **"Download"** button on the Claude "Artifact" window to get the `.js` file directly to your device.
3.  **Deploy via Cloudflare:**
    *   Open your Cloudflare Dashboard.
    *   Copy the code from the downloaded file and paste it into the Worker editor.
    *   **Crucial:** Check your environment variables. Ensure `GEMINI_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, and `ENCRYPTION_KEY` are still correctly set[cite: 2].
4.  **Test the Memory:**
    *   Tell the bot something specific: *"Rick, the client Acme uses a custom port 8081 for their staging server."*
    *   Ask it later: *"What port does Acme use?"*
    *   If it works, the RAG (Vector Search) is successfully pulling data from your Supabase Knowledge Base[cite: 1].

Would you like me to clarify the specific SQL code again to ensure your Supabase instance is ready for this update?

---

"I am providing you with my current `worker.js` and `schema.sql.txt` for a Cloudflare Worker bot named 'Rick Sanchez Conextsol Brain'[cite: 2, 3]. Please provide a complete, updated `worker.js` file that implements the following two optimizations:

1. **AI Efficiency & Vector Search (RAG):**
   - Use the `text-embedding-004` model to generate embeddings for any text sent to the Knowledge Base via the `create_kb` tool[cite: 1].
   - In the `cmdAI` function, before calling Gemini, perform a semantic search by calling the Supabase RPC function `match_kb`[cite: 1].
   - Inject the retrieved relevant notes into the system context so Rick can 'remember' details accurately[cite: 1].

2. **History Pruning & Summarization:**
   - Implement a logic that monitors the conversation history length[cite: 1].
   - When history exceeds `MAX_HISTORY`, use Gemini to summarize the oldest messages into a concise 'Memory' block, then replace those messages with the summary to keep the context window clean[cite: 1].

**Requirements:**
- **Preserve Personality:** Maintain the blunt, sarcastic Rick Sanchez persona in all responses[cite: 2].
- **Preserve Security:** Do not change the AES-GCM encryption/decryption logic for credentials[cite: 2].
- **Complete File:** Output the ENTIRE updated `worker.js` file in a single code block so I can use your 'Download' feature.
- **Dependencies:** Ensure the code uses standard `fetch` for API calls to Gemini and Supabase as it currently does[cite: 2]."
