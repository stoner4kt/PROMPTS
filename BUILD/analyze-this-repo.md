# Analyze this repo

Analyze this repo. I'm having issues logging in when I enter the email and password I created, nothing happens. Gemini says it a cookie issue and suggested this [I am experiencing a Next.js Middleware redirect loop when logging in. The console shows: "A soft navigation has been detected: .../auth/login?redirected_from=%2Fdashboard". 

The issue is a cookie timing gap: the client-side Supabase authentication (`signInWithPassword`) triggers `router.push('/dashboard')` before the browser completely writes the session cookies. The Cloudflare Edge Middleware intercepts the request, sees no cookies, and silently redirects back to the login page.

Please fix this issue by refactoring the form submission to use Next.js Server Actions (or migrating the logic to a server-safe pattern) using `@supabase/ssr`. 

CRITICAL CONSTRAINTS:
1. Do NOT change, remove, or modify any UI layouts, HTML structures, Tailwind CSS classes, styling, or unrelated client states. Keep the visuals design identical.
2. Ensure the inputs retain their original attributes, but make sure they have the correct `name` attributes (`name="email"` and `name="password"`) so the Server Action can read the FormData.
3. Provide the code for the server action file (e.g., `actions.ts`) and the updated login page file.] Analyze if the issue could be anything else. I using Cloudflare for hosting and supabase as a backend

---

Generate me a prompt i can feed into codex to make these necessary changes to my project so I can deploy it on Cloudflare and generate the neededs steps I must take and what exactly I must edit for the Build to work.
