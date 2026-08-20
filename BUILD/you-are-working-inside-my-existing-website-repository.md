# You are working inside my existing website repository

You are working inside my existing website repository.

My stack:
- Frontend: HTML, CSS, JavaScript
- Hosting: cPanel basic hosting for the website
- Backend services: Supabase
- Email provider: Resend

Goal:
Build a full booking system that:
1. Shows a calendar with available and booked time slots.
2. Prevents double bookings.
3. Stores booking data in Supabase.
4. Sends an OTP verification email before a booking is finalized.
5. After successful booking, redirects the user to /thank-you.html.
6. Sends an automated confirmation email to the customer after the booking is confirmed.
7. Keeps all secret keys out of the frontend code.
8. Works cleanly with my existing HTML, CSS, and JS site.

What to inspect in the repo:
- Find the booking form files.
- Find the calendar UI files.
- Find the current form submission logic.
- Find any existing API calls, fetch requests, or booking-related code.
- Find the project structure and identify where to add new files without breaking the site.

What to implement:
Frontend:
- Add or update a calendar UI that displays booked slots and available times.
- Make booked slots clearly visible and disabled/unselectable.
- Add form fields for:
  - full name
  - email
  - phone number
  - service type
  - booking date
  - booking time
- Add an OTP verification step before final booking submission.
- After success, redirect to /thank-you.html.

Backend:
- Use Supabase as the main booking database.
- Create the necessary Supabase table(s) for bookings and OTP records.
- Create Supabase Edge Functions for:
  - send-otp
  - verify-otp
  - create-booking
  - send-confirmation-email
- Use Resend inside Edge Functions for sending the OTP and confirmation emails.
- Include server-side conflict checking so two users cannot book the same time slot.
- Make sure the booking is only saved after OTP verification and final availability check.

Security:
- Do not expose Supabase service role keys or Resend API keys in the frontend.
- Use environment variables/secrets for backend-only keys.
- Recommend best-practice validation on both frontend and backend.
- Make sure the booking flow is resilient against double-booking and race conditions.

Output required:
1. A concise summary of what you changed.
2. The exact files changed or created.
3. The code for each new or updated file.
4. Step-by-step setup guidance for me to:
   - create the Supabase project
   - create the database tables
   - configure Edge Functions
   - add Resend API key as a secret
   - connect the frontend to the backend
   - test OTP verification
   - test booking creation
   - deploy to cPanel
5. If anything in the repo is missing, tell me exactly what to add.

Important:
- Keep the existing design unless a change is necessary.
- Use plain HTML, CSS, and JavaScript if possible.
- If you need a library for the calendar, choose the lightest practical option and explain why.
- Write production-minded code.
- Make the instructions beginner-friendly but still precise.
