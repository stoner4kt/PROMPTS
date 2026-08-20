# Please analyze our repository and prepare the changes needed to implement our

Please analyze our repository and prepare the changes needed to implement our regional data and calendar toggle strategy.
First, modify the database schema to add a location column to both the drivers and bookings tables, using values like Joburg or Cape Town to distinguish between the locations.
Second, update the relevant frontend components and API queries to ensure that when an admin uses a toggle, the application fetches and displays bookings only for the specific region selected.
Lastly, make sure that when an admin is creating new bookings or assigning drivers, the location context is automatically applied to preserve the separation of data. Generate me a prompt I can feed into replit/codex to make these changes for me

---

Yes they will use a shared vehicle fleet, however vehicles and drivers won't need to be separated by location and both shouldn't be able to be double booked even if the locations differ
Only bookings should be scoped, by region and drivers and vehicles should be able to be double booked. Regenerate me the updated prompt

---

Yes they will use a shared vehicle fleet, however vehicles and drivers should be scoped as to prevent booking a vehicle or driver in a location that they are not available in eg. Booking a driver/vehicle in Cape Town for a booking that starts in Joburg and allows admins to see where a vehicle/ drivers is located when assigning a booking. They should have the option to filter by location on both vehicles and drivers page aswell as active and non active vehicles and drivers
