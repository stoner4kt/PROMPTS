# I want to make these changes to my system, analyze my repo

I want to make these changes to my system, analyze my repo and guide me what to do https://github.com/stoner4kt/ToursystemV2refactored.git :  (Fix the displays of tables on certain pages  and ensure all models have close button on the Admin side ( Manage Drivers, Bookings List, Traffic Fines) 
Ensure that when drivers are verified they disappear from the Active invite list in the Manage Drivers dashboard
 On the vehicle Expenses tab, admin should be able to view the expense before approving or rejecting , the same with the Transfer Recon sheets )

---

Okay. So I'm I'm etched. I'm making the changes to the airman, the s x airman dashboard, the s x, and I'm... what what changed? One one c. And I made the change, and now it's giving me a deployment error. I will share the error below, and then I will continue with change two.

---

Here is my deployment error : 
Usage
Support
Settings
Vercel Agent
Code reviews that catch bugs before they reach production.

Avatar for stoner4kt
stoner4kt


Deployments
7dpG6T5DX

Deployment
Logs
Resources
Source
Open Graph
Build Failed
Command "npm run build" exited with 1
Created
github/stoner4kt
stoner4kt
6m ago
Status
Error
Latest
Duration
17s
5m ago
Environment
Production
Domains
toursystem-v2refactored-git-edits-stoner4kts-projects.vercel.app
toursystem-v2refactored-lsnk2koel-stoner4kts-projects.vercel.app
Source
Edits
42f7c66
Refactor fines table to support horizontal scrolling

Deployment Settings
Build Logs
17s
1 line selected

3
Find in logs
CtrlF
11:26:42.770 
./components/AdminDashboard.tsx
11:26:42.771 
Error:   x Unexpected token. Did you mean `{'}'}` or `&rbrace;`?
11:26:42.771 
      ,-[/vercel/path0/components/AdminDashboard.tsx:2114:1]
11:26:42.771 
 2111 | 
11:26:42.772 
 2112 |               </div>
11:26:42.772 
 2113 |             </div>
11:26:42.772 
 2114 |           )}
11:26:42.772 
      :            ^
11:26:42.772 
 2115 | 
11:26:42.773 
 2116 |           {/* ==================== EXPENSES LOG TAB ==================== */}
11:26:42.773 
 2117 |           {activeTab === 'expenses' && (
11:26:42.773 
      `----
11:26:42.774 
  x Expression expected
11:26:42.774 
      ,-[/vercel/path0/components/AdminDashboard.tsx:3338:1]
11:26:42.774 
 3335 |           )}
11:26:42.774 
 3336 | 
11:26:42.775 
 3337 |         </main>
11:26:42.775 
 3338 |       </div>
11:26:42.775 
      :       ^
11:26:42.776 
 3339 | 
11:26:42.776 
 3340 |       {/* ==================== BOOKING ADD/EDIT MODAL ==================== */}
11:26:42.776 
 3341 |       {showBookingModal && (
11:26:42.776 
      `----
11:26:42.777 
  x Unterminated regexp literal
11:26:42.777 
      ,-[/vercel/path0/components/AdminDashboard.tsx:3338:1]
11:26:42.778 
 3335 |           )}
11:26:42.778 
 3336 | 
11:26:42.778 
 3337 |         </main>
11:26:42.778 
 3338 |       </div>
11:26:42.779 
      :        ^^^^^
11:26:42.779 
 3339 | 
11:26:42.779 
 3340 |       {/* ==================== BOOKING ADD/EDIT MODAL ==================== */}
11:26:42.779 
 3341 |       {showBookingModal && (
11:26:42.780 
      `----

---

Okay I'm busy with step 5c and I need to know exactly where to paste the snippet

---

I am at step 6b , do I remove the  {rec.status === 'submitted' && ( aswell or just the code below it

---

I am at step 6c , where exactly do I paste the snippet
