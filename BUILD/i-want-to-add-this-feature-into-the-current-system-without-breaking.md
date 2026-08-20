# I want to add this feature into the current system without breaking

I want to add this feature into the current system without breaking the existing build , : [ Okay so den the booking form should allow admins to select & add rented vehicles  and with this drivers will be able to enter the vehicle registration & model to the booking, only if the admin marks the booking as rented vehicle and not a vehicle from the fleet 
And the inspection sheets for these trips should be saved to the correct booking with the label if it was a rented vehicle or internal vehicle with its registration number and model
Rental vehicle data should also be track for which vehicle was assigned to which booking, driver etc(this is logged in the rented vehicles dashboard, showing active, past vehicles rented for which bookings. ]. I also want to fix this bug codex found:[  Build rental periods in the fleet timezone

When bookings still come from the existing date-only form, casting start_date/end_date directly to timestamptz makes the full-day range use the database session timezone, while the fine UI captures local times and the notification renders Africa/Johannesburg. In a Supabase UTC database this shifts South African bookings by two hours, so fines between 00:00–01:59 on the local start date can miss the booking, and fines just after the local end date can match incorrectly.] Generate me a prompt I can feed into codex to implement these necessary changes to the current system

---

The prompt should add the rented-in-vehicles.html dashboard aswell and add it to both  admin and driver sidebars
