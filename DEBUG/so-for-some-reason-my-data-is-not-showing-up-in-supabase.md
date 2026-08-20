# So for some reason my data is not showing up in supabase

So for some reason my data is not showing up in supabase when I try to add I external driver or client driver profile and when I add them to the booking and create the booking it doesn't show up in the database, I am using supabase for this

---

Okay so it's creating the booking in the UI but disappears afterwards

---

This is the repo I'm referring to https://github.com/stoner4kt/ToursystemV2refactored.git I'm working on the Edits3 branch and my schema is at supabase/functions/schema-final.sql

---

I ran both scripts but it's still not working,

---

| tablename | policyname                    | permissive | roles           | cmd    | qual                                                                                                    | with_check |
| --------- | ----------------------------- | ---------- | --------------- | ------ | ------------------------------------------------------------------------------------------------------- | ---------- |
| bookings  | Admins can create bookings    | PERMISSIVE | {authenticated} | INSERT | null                                                                                                    | is_admin() |
| bookings  | Admins can update bookings    | PERMISSIVE | {authenticated} | UPDATE | is_admin()                                                                                              | is_admin() |
| bookings  | bookings_admin_all            | PERMISSIVE | {public}        | ALL    | is_admin()                                                                                              | is_admin() |
| bookings  | bookings_authenticated_insert | PERMISSIVE | {authenticated} | INSERT | null                                                                                                    | true       |
| bookings  | bookings_authenticated_read   | PERMISSIVE | {authenticated} | SELECT | true                                                                                                    | null       |
| bookings  | bookings_authenticated_update | PERMISSIVE | {authenticated} | UPDATE | true                                                                                                    | true       |
| bookings  | bookings_driver_read_own      | PERMISSIVE | {public}        | SELECT | (assigned_driver_id = ( SELECT profiles.driver_id
   FROM profiles
  WHERE (profiles.id = auth.uid()))) | null       |

---

When I run the last snippet it says this :Failed to run sql query: ERROR:  23514: new row for relation "bookings" violates check constraint "bookings_status_check"
DETAIL:  Failing row contains (6d7ca20a-1fe7-4234-ac59-bb7d313d4030, TEST-2026-07-06 21:23:54.298338+00, Test Client, null, 2026-07-06, 2026-07-07, null, null, pending, null, 2026-07-06 21:23:54.298338+00, 2026-07-06 21:23:54.298338+00, unpaid, f, null, null, null, null, [], null, null, null, null, null, null, null, null, null, null, null, f, null, 2026-07-05 22:00:00+00, 2026-07-07 21:59:59+00, ["2026-07-05 22:00:00+00","2026-07-07 22:00:00+00"), f, null, null, null, Cape Town, null, external_driver).

---

Analyze my components/AdminDashboard.tsx , lib/storage.tsx and components/RentalClientForm.tsx as the snippet above inserts a row into my bookings table

---

Okay generate me a prompt I can feed into with my repo to analyze it and tell me exactly what to fix for it to work
