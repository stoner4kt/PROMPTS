# Look at my repo https://github

Look at my repo https://github.com/stoner4kt/ToursystemV2refactored.git  So the send-otp-email function responds with a two 200 (options & post) and then a 500 post error but the email is sent but in the systems
When I try to request a edit on bookings in the admin side and request edit on the transfer recon sheet on the drivers side, it shows that in the attached images look at supabase/schema/schema-latest.sql and supabase/functions/** . Here is the error from the function logs : {
  "event_message": "send-otp-email error: DB insert failed: invalid input syntax for type uuid: \"DRV-ADM001\"\n",
  "id": "78353b27-4f35-4f45-a775-cba02ea135ed",
  "metadata": [
    {
      "boot_time": null,
      "cpu_time_used": null,
      "deployment_id": "jxsesdcwdjrxydkvhpsh_beca9b51-4f39-4a9a-9a5a-b290a5338342_26",
      "event_type": "Log",
      "execution_id": "51b407d3-066a-4144-9b35-e2b191cb4788",
      "function_id": "beca9b51-4f39-4a9a-9a5a-b290a5338342",
      "level": "error",
      "memory_used": [],
      "project_ref": "jxsesdcwdjrxydkvhpsh",
      "reason": null,
      "region": "eu-west-3",
      "served_by": "supabase-edge-runtime-1.74.2 (compatible with Deno v2.1.4)",
      "timestamp": "2026-07-02T17:33:01.578Z",
      "version": "26"
    }
  ],
  "timestamp": 1783013581578000
}

---

But the frontend shouldn't send the a hard coded "DRV-ADM001" , it should send the drivers I'd who is making the request or the admin who is making the request

---

This is the repo I am refactoring and the database is the exact same, how was I handling it in this repo https://github.com/stoner4kt/ToursystemV1.git and Guide me on the exact fixes to make so it works

---

admin_id: currentUserId || null,

---

I updated my OTPModal only with the admin call and got a deployment error: 

4
Find in logs
CtrlF
21:31:11.778 
Running build in Washington, D.C., USA (East) – iad1
21:31:11.779 
Build machine configuration: 2 cores, 8 GB
21:31:11.921 
Cloning github.com/stoner4kt/ToursystemV2refactored (Branch: Edits, Commit: b9eb617)
21:31:12.759 
Cloning completed: 834.000ms
21:31:14.665 
Restored build cache from previous deployment (qQ9qQamudkt2xTcKLunywYEYnFcn)
21:31:15.403 
Running "vercel build"
21:31:15.434 
Vercel CLI 54.18.7
21:31:15.928 
Installing dependencies...
21:31:22.411 
21:31:22.412 
up to date in 6s
21:31:22.412 
21:31:22.413 
229 packages are looking for funding
21:31:22.413 
  run `npm fund` for details
21:31:23.372 
Detected Next.js version: 15.5.19
21:31:23.373 
Running "npm run build"
21:31:23.537 
21:31:23.538 
> ai-studio-applet@0.1.0 build
21:31:23.538 
> next build
21:31:23.539 
21:31:25.257 
   ▲ Next.js 15.5.19
21:31:25.258 
21:31:25.299 
   Creating an optimized production build ...
21:31:33.885 
 ✓ Compiled successfully in 8.4s
21:31:33.889 
   Skipping linting
21:31:33.889 
   Checking validity of types ...
21:31:43.053 
Failed to compile.
21:31:43.054 
21:31:43.055 
./components/OTPModal.tsx:63:23
21:31:43.055 
Type error: Cannot find name 'currentUserId'.
21:31:43.056 
21:31:43.056 
  61 |             resource_type: resType,
21:31:43.056 
  62 |             resource_id: resId,
21:31:43.057 
> 63 |             admin_id: currentUserId || null, // Sends to the Main Chief Admin
21:31:43.057 
     |                       ^
21:31:43.057 
  64 |             context_label: title || 'Admin action authorization'
21:31:43.057 
  65 |           }
21:31:43.058 
  66 |         });
21:31:43.122 
Next.js build worker exited with code: 1 and signal: null
21:31:43.222 
Error: Command "npm run build" exited with 1
. And these are my files tell exactly what to paste and where for the function to work
