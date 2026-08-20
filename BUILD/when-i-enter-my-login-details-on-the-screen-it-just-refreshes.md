# When I enter my login details on the screen, it just refreshes

When I enter my login details on the screen, it just refreshes and doesn't log me in. Why is that and how do I fix it.

---

My email is in the supabase dashboard and my credentials are set correctly

---

No logs are captured in netlify or in the browser console, this is a bug that codex gave on my last pull request [P1 Badge Use the authenticated user's UID for bridge writes

When these newly authenticated bridge calls reach netlify/functions/brain-bridge.js, the bridge still discards the JWT and verifyToken() returns { id: 'verified-user' }; handleCreate()/handleRickMode() then write that value into owner_id. In the documented schema owner_id is a UUID and RLS reads are scoped to owner_id = auth.uid(), so any successful create/Rick Mode request from this UI will either fail with an invalid UUID or create records that the signed-in user cannot read back after loadClients()/loadProjects().]

---

Generate me a prompt I can feed into codex to make these necessary changes without changing anything else in the system
