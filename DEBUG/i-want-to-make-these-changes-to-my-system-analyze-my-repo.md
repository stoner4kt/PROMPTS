# I want to make these changes to my system, analyze my repo

I want to make these changes to my system, analyze my repo and guide me what to do repo https://github.com/stoner4kt/ToursystemV2refactored.git   branch https://github.com/stoner4kt/ToursystemV2refactored/tree/Edits2  :  (When admin request to delete a booking the send otp email function responds with a error but when I request to edit it it sends it successfully check my schema in supabase/schema/schema-latest.sql and supabase/functions/** send otp email and verify-otp functions

I also have multiple other places I am using it and it is failing,
ON Trip Recons, after a admin reviews the sheet a driver has requested to edit and wants to approve it so the driver can Edit it when they click to approve the edit a otp should be sent using the send-otp-email function to the main admin, the admin shares it with them, they enter it and make the edit  , When a admin wants to delete a booking or vehicle a otp gets sent to the main admin using the send otp email function and verify it using the verify otp function it is currently working when I want to edit bookings using the current functions perfectly but not for the places I explained above (ADMIN_EMAIL & RESEND_API_KEY IS ALREADY SET AND SENDER_EMAIL)And the same for rented vehicles
So all otp request are admin side now. It's currently working when I request to edit bookings but not with others, Analyze the repo and tell me why it works with the booking edits but not the others)

---

Okay so tell me exactly what to edit and exactly where to insert it to apply these changes

---

These are all in the admin side correct

---

I still get a error on the vehicle when I click delete on a booking 
 and when I want to suspend a driver ( it say no active session) 
, it doesn't work when a admin approves a sign off on a Trip Recon sheets 

And now the send otp email function is saying no active session but it was working on vehicle removal, booking edits 
 
I already applied the above steps

---

Bookings and vehicles removal still responding with 2xx error on the function send-otp-email 

Bookings deletes still fail to send the otp

Vehicle removal aswell is not sending the otp (however vehicles in active/scheduled bookings cannot be deleted by default in the system)

Trip Recon is successfully working and the others are too

---

But it was working as the database is in my old system I don't want to change the database
