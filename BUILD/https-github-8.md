# https://github

https://github.com/stoner4kt/ToursystemV2refactored/tree/main  Analyze my repo and tell me why when I create bookings it doesn't create the booking in supabase, it just store it in the UI and after a few seconds it disappears and no booking was created in my booking table in supabase

---

This is the repo u must analyze https://github.com/stoner4kt/ToursystemV2refactored/tree/main

---

My invoice column didn't have a unique key because admins will enter a invoice number manually. Give me the complete code I need to insert and exactly where I must insert it for it to work

---

I made the edits but now my deployment is failing to compile here is the logs : 14:10:27.973 Failed to compile.
14:10:28.021 Error: Command "npm run build" exited with 1

---

14s
1 line selected

2
Find in logs
CtrlF
Running build in Washington, D.C., USA (East) – iad1
Build machine configuration: 2 cores, 8 GB
Cloning github.com/stoner4kt/ToursystemV2refactored (Branch: Edits, Commit: 37afe52)
Cloning completed: 415.000ms
Restored build cache from previous deployment (Byys2Piw9wX9p72kgDz4BrPfhN94)
Running "vercel build"
Vercel CLI 54.18.6
Installing dependencies...
up to date in 5s
229 packages are looking for funding
  run `npm fund` for details
Detected Next.js version: 15.5.19
Running "npm run build"
> ai-studio-applet@0.1.0 build
> next build
   ▲ Next.js 15.5.19
   Creating an optimized production build ...
Failed to compile.
./lib/storage.ts
Module parse failed: Identifier 'mergeLocalAndRemote' has already been declared (796:9)
File was processed with these loaders:
 * ./node_modules/next/dist/build/webpack/loaders/next-flight-client-module-loader.js
 * ./node_modules/next/dist/build/webpack/loaders/next-swc-loader.js
You may need an additional loader to handle the result of these loaders.
| // Local wins if its updated_at is newer; remote wins otherwise.
| // Any local record not found in Supabase is kept (it hasn't synced yet).
> function mergeLocalAndRemote(localItems, remoteItems, primaryKey) {
|     const merged = [
|         ...remoteItems
Import trace for requested module:
./lib/storage.ts
./app/page.tsx
> Build failed because of webpack errors
Error: Command "npm run build" exited with 1

---

So even after the fix it still doesn't save the bookings to the database
