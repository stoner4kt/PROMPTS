# I want to make these changes to my system, analyze my repo

I want to make these changes to my system, analyze my repo and guide me what to do https://github.com/stoner4kt/ToursystemV2refactored.git  :  (Because I get this error in the admin panel when I try to review and signoff a sheet in the Trip Recon dashboard on the admin side) my edge functions are at supabase/functions/**  and my schema is at supabase/schema/schema-latest.sql. Look at my edge functions notify-transfer-edit-request and fault alert as I want the to send it alert to the admin via email when a driver requests a edit on a Recon sheet

---

Okay so I don't want to edit notify-transfer-edit-requests as it works with the Transfer Recon and I want to setup a function for the  Recon sheet (drivers side)  Trip Recons ( admin side)

---

So I still get the function 2xx error but I don't want it to send a OTP, just the alert when a driver requests a edit, it should do the same as the Transfer Recon  ( admin can review the current sheet and why the driver is requesting a edit and approve or reject it , when a admin approves it the driver can then edit that sheet through their dashboard) . I am handling Transfer Recons like that and I want to handle the Recon sheet aswell . I have already deployed the function I gave me and the driver dashboard

---

I get the error when I want to approve/vrevew/reject a edit on the Trip Recons dashboard on the admin side

---

So I meant a OTP should not be sent, only the alert to the admin when a driver requests a edit and the admin should be able to review/approve/reject edits and if a admin clicks director sign off approval it shouldnt send a OTP at all.

---

Give me the DriverDashboard.tsx for this AdminDashboard.tsx the I can upload to my GitHub repo as I already have the notify-recon-edit-request function deployed,
