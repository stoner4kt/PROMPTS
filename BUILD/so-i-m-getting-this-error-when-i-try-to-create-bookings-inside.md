# So I'm getting this error when I try to create bookings inside

So I'm getting this error when I try to create bookings inside my system . Please analyze me repo any tell me why it's doing this and also how. I can fix this https://github.com/stoner4kt/ToursystemV2refactored/tree/main

---

Where exactly should I place the code and what exactly should I run or remove

---

Okay it's working and bookings save to the database, now I want to ensure my edge functions work successfully this is what they are supposed to do < Notifications and alerts 

The inspection sheet should send a alert to the main admin when a fault is log on it whether a driver or admin logs it

Traffic fines are logged by admins and a notification is sent to the driver who the fines is logged for using resend and is sent to thier email

Expense or damage
A alert is sent to the main admin when a expense/damage is logged on a vehicle

Admins should be able to edit bookings, but should request a edit and a otp is sent to the main admin which will share it with them before they can make
 the edit

Transfer Recon ( Driver edit requests)
A driver should be able to request a edit on their Transfer Recon sheet and a otp must be sent to the main admin which will share it with them before they can make
 the edit

Check the schema in supabase/schema/schema-latest.sql and supabase/functions/**
