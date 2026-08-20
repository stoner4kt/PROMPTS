# So sometimes bookings have self drive clients and external drivers and currently

So sometimes bookings have self drive clients and external drivers and currently I only have assigned drivers which is like staff This is my repo https://github.com/stoner4kt/ToursystemV2refactored/tree/main   analyze it and guide me on the changes I need to make (This is a response I got from chatgpt without sharing my repo:
Yes, you need a separate workflow for external renters because they are not your staff drivers. Think of it as a new booking type:

Booking Type

Company Driver Booking
Client Self-Drive Rental
Third-Party Driver Rental
Third-Party Vehicle Booking
For your case, I would add this option in the booking form:

Rental Type

With INYATHI Driver
Self-Drive Client Rental
External Driver Rental
Then the app can show different required fields depending on the type.

For Client Self-Drive Rental, add a client/renter role like:

Client / Renter Profile

Full name
Phone number
Email
Address
Rental agreement document ( upload field like with the other upload fields using cloudinary and edge functions )


For External Driver Rental, where someone else drives the vehicle:

External Driver Profile:
Driver full name
Phone number
Linked client/company responsible for booking
Rental agreement document ( upload field like with the other upload fields using cloudinary and edge functions )

Then for inspections, I would create two inspection records linked to the booking:

Vehicle Handover Inspection :

Date/time out
Odometer out
Fuel level out
Exterior condition
Interior condition
Tyres
Windscreen/windows
Lights
Tools/spare wheel/jack
Existing damages with photos
Client/renter signature field 
Staff/admin signature field 
Vehicle Return Inspection 

Date/time returned
Odometer in
Fuel level in
New damages
Extra mileage
Fuel charges
Cleaning charges
Damage charges
Final status: Returned Clean, Returned With Damage, Late Return, Pending Claim
Client/renter signature field 
Staff/admin signature field
In your booking screen, instead of only Assign Driver and Assign Vehicle, you could have:

Driver Assignment

INYATHI Staff Driver
Client Driving Self
External Driver
If Client Driving Self or External Driver is selected, then driver selection becomes a Renter/External Driver details section, not your staff driver list.

Good statuses for this rental flow:

Draft
Documents Pending
Inspection Pending
Ready for Handover
Vehicle Out
Return Inspection Pending
Returned
Damage Review
Closed
The cleanest idea: keep your current booking system, but add a rental_mode field. Then the booking can still require a vehicle, but the “driver” can either be one of your staff drivers or an external renter/driver profile.
)
, analyze my repo, my schema is at supabase/schema/schema-latest.sql my edge functions are at supabase/functions/**

---

Okay for part 2 before I begin with everything, tell exactly where to insert the code and what to edit. Then I will begin with everything

---

Generate me the complete AdminDashboard.tsx, storage.tsx, RentalClientForm.tsx with all these edit in place. I will run the schema scripts in the supabase dashboard myself, and I will update the sign-upload function myself

---

Continue with what you were doing

---

Continue with what you were doing

---

Okay so now I can upload these files and run the sql scripts above and update the sign-upload function
