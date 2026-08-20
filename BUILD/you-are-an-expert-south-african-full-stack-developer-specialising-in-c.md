# You are an expert South African full-stack developer specialising in clean, high-conversion

You are an expert South African full-stack developer specialising in clean, high-conversion lead-generation websites for finance businesses.

Build me the COMPLETE ready-to-deploy website for a company that connects clients with loan providers, debt review companies, and financial services in South Africa.

Requirements:

1. Public website (index.html)
   - Modern, clean, professional design using Tailwind CSS via CDN (blue and white colour scheme with trust signals)
   - Hero section: "Get Matched with the Best Loans & Debt Solutions – Free & Confidential"
   - Clean multi-field form with these exact fields:
     • Full Name (required)
     • Email (required)
     • Phone Number (required)
     • ID Number (optional)
     • Province (dropdown with all 9 South African provinces)
     • Services needed (multi-select checkboxes): Personal Loan, Home Loan, Vehicle Finance, Debt Review, Debt Consolidation, Credit Card Debt, Business Loan
     • Additional Message / Notes (textarea)
     • POPIA consent checkbox (required)
   - On submit, the form must send data to Google Apps Script and show success message
   - Fully responsive, mobile-first

2. Admin Panel (admin.html – separate page)
   - Simple password protection (hardcoded in JS, password: "Admin2026" – clearly note this can be changed)
   - Live dashboard that pulls ALL leads from the same Google Sheet via a GET endpoint
   - Clean data table showing:
     Timestamp | Full Name | Email | Phone | ID Number | Province | Services | Message | Consent | Status (dropdown: New / Contacted / Closed)
   - Features:
     • Real-time search bar
     • Filters: by Province, by Service, by Date range
     • "Mark as Contacted" button that updates the sheet
     • "Export to Excel (.xlsx)" button using SheetJS (include via CDN) – must download a proper .xlsx file with all columns
     • Delete row button (with confirmation)
     • Responsive table (scrollable on mobile)
   - Beautiful dashboard look with total leads count, today's leads count, and quick stats

3. Google Apps Script (provide the full code for one script)
   - Must include:
     • doPost(e) – to receive form data and append new row to "Leads" sheet
     • doGet(e) – to return all rows as JSON for the admin panel
     • Simple update function to change "Status" column when admin marks as contacted
   - Columns in Google Sheet (exactly): Timestamp, Full Name, Email, Phone, ID Number, Province, Services, Message, Consent, Status

4. Output format:
   Return 5 separate, clearly labelled code blocks:
   1. COMPLETE index.html (public form page)
   2. COMPLETE admin.html (with password gate and full admin functionality)
   3. FULL Google Apps Script code (paste-ready)
   4. Step-by-step deployment instructions (create sheet, deploy web app, get URLs, how to set password, how to host on Vercel/Netlify for free)
   5. Any extra notes (how to change colours, add logo, make password stronger later, security note about public GET)

Make everything production-ready, beautiful, fast-loading, and 100% copy-paste functional. Use only CDNs (Tailwind + SheetJS). No external files needed. Include helpful comments in the code.

Start your reply with "Here is the complete build:" and then the 5 blocks.
