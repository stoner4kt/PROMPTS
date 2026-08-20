# Act as an expert Senior Frontend Developer and Conversion Rate Optimization (CRO)

Act as an expert Senior Frontend Developer and Conversion Rate Optimization (CRO) specialist. 

I need you to generate a fully complete, production-ready landing page project for a premium local plumbing business. The business details are:
- Business Name: Onedays Plumbing Services
- Target Aesthetic: High-end SaaS design (Dark mode, clean typography, spacious modern layouts, neon accent colors, premium feel instead of a basic "plumbing site").

### Technical Constraints:
1. Stack: Vanilla HTML5, CSS (via Tailwind CSS CDN), and pure Vanilla JavaScript only. No React, no external heavy libraries.
2. Structure: Everything must be modular and clean so I can easily move this into code editors like Spck or Termux on Android.
3. Forms: The main contact/lead capture form must use native Netlify form attributes (`data-netlify="true"`, `name="onedays-lead-form"`, and proper POST methods) so it works seamlessly out-of-the-box when deployed to Netlify, but behaves gracefully if hosted on Vercel.

### Required Files & Code Outputs:
Provide the full, un-truncated file contents for the following root-level files so I can easily save them into a project directory:

1. `index.html` (Must include):
   - Semantic HTML5 layout with a high-converting structure: Sticky Navigation Header, a conversion-focused Hero section with a dual-CTA (Get Quote / Call Direct), a "Core Specialties" feature grid, an "Emergency 24/7 Response" urgency banner, a Testimonials section, a highly polished interactive Lead Capture Form, and a Footer.
   - Google Search Console meta tag placeholder: `<meta name="google-site-verification" content="GSC_VERIFICATION_PLACEHOLDER" />`
   - Google Analytics (GA4) Global Site Tag tracking boilerplate setup using a `GA_MEASUREMENT_ID_PLACEHOLDER`.
   - Tailwind custom configuration embedded in the head to define the dark theme colors (`bg-brandDark: #0B0F19`, custom accent blue or emerald tracking values).

2. `app.js` (Must include):
   - Lightweight, optimized vanilla JS.
   - Smooth scroll behavior fallback for anchor navigation links.
   - Form submission listener that catches the event and triggers a placeholder Google Analytics `gtag('event', 'generate_lead', ...)` tracking code before completing the form submission natively.

3. `robots.txt`
   - Correctly configured to allow all user agents and pointing directly to a placeholder domain's `sitemap.xml`.

4. `sitemap.xml`
   - A valid XML sitemap structure referencing the home URL (`https://www.onedaysplumbing.co.za/` or a placeholder production URL), set to a `monthly` change frequency and a `1.0` priority ranking.

### Copywriting & SEO Context:
The copywriting should be sharp, professional, and focus heavily on pain points (e.g., burst pipes, leak detection, emergency repairs, blocked drains) while emphasizing reliability, speed, and premium local expertise. Avoid lorem ipsum; use actual high-converting sales copy tailored for "Onedays Plumbing Services".

Please output the complete code blocks for these 4 files cleanly, without placeholders or clipping the code short, so I can package them up into a zip repository for my client review layout immediately.
