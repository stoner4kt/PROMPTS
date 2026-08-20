# Role: You are a Technical Project Manager

Role: You are a Technical Project Manager.

Task: Generate a professional "Project Architecture & Service Overview" document for a client. The goal is to explain the lead generation system built for them, justifying the tools used and explaining how they interact.

Project Stack Context:

Frontend: HTML5, CSS3, and Vanilla JavaScript.

Backend/Database: Supabase (PostgreSQL, Authentication).

Email Service: Resend (for lead verification and notifications).

Data Storage: Automated sync to a Google Spreadsheet.

Hosting: Domains.co.za (cPanel environment).

Document Requirements:

Executive Summary: A brief overview of the system's purpose (automated lead capture and verification).

Service Breakdown: For each service (Supabase, Resend, Google Sheets), explain:

What it is: (e.g., Supabase as the "engine" and secure database).

Why it was chosen: (Security, real-time data, scalability).

The Workflow: A step-by-step "Path of a Lead" explaining how data moves from the HTML form -> Supabase -> Resend -> Spreadsheet.

Hosting & Maintenance: Explain how the frontend sits on cPanel while communicating with these cloud services via APIs.

Security & Reliability: Highlight that data is backed up in the database even if the spreadsheet is edited, and that emails are verified to prevent spam.

Tone: Professional, clear, and reassuring. Avoid overly dense jargon where a business-focused explanation suffices.

Output : Generate a interactive, informative pdf i can share with my client. Use bold headings and bullet points for readability.

[Analyze the attached repository code to ensure specific technical details, like function names or specific data fields, are accurately reflected in the descriptions.]
