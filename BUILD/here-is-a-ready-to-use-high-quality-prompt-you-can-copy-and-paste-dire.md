# **Here is a ready-to-use, high-quality prompt** you can copy and paste directly

**Here is a ready-to-use, high-quality prompt** you can copy and paste directly into Claude, Cursor, Codex, Replit Agent, or any other coding AI that can analyze your repository.

---

**Prompt:**

You are an expert Google Ads + front-end tracking implementation specialist.

**Project:** Analyze the entire repository for the website **appliance-911.co.za**.

**Goal:** Implement complete conversion tracking for Google Ads using the official Google tag (gtag.js) with the following Tracking ID:  
**AW-18049545656**

### Requirements:

1. **Add the Google tag (gtag.js)** exactly as shown below to every page (ideally in the main layout/template file, inside the `<head>` section before the closing `</head>` tag):

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18049545656"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-18049545656');
</script>
```

2. **Create three separate conversion actions** by firing specific events:

   - **Form Submissions** → Event name: `conversion` with `send_to: 'AW-18049545656 / [Form Label]'`
   - **Call Button Clicks** (`tel:` links) → Event name: `conversion`
   - **WhatsApp Button Clicks** (`wa.me`, `api.whatsapp.com`, or WhatsApp floating button) → Event name: `conversion`

3. **Implementation Strategy:**
   - First, explore the full project structure (`tree` or list files) and identify:
     - Main layout / header / template files (where `<head>` lives)
     - All contact / quote / service request forms
     - Phone number / click-to-call buttons
     - WhatsApp buttons or floating widgets
   - Prefer using **dataLayer pushes** for reliability.
   - For forms: Handle both traditional form submits and AJAX / single-page form submissions.
   - For buttons: Use event listeners on `tel:` links and WhatsApp links.
   - Make the code clean, reusable, and non-intrusive.

4. **Provide the exact code changes** I need to make, including:
   - Where to add the main Google tag
   - JavaScript code for each conversion type (with comments)
   - Recommended trigger selectors (class, ID, href patterns, etc.)
   - Any necessary modifications to existing form handlers

5. **Also provide a GTM (Google Tag Manager) version** as an alternative recommendation, explaining why it's better for long-term maintenance.

6. **Best Practices to include:**
   - Enhanced Conversions (if email or phone is collected)
   - Prevent duplicate conversions
   - Mobile-friendly tracking
   - Testing instructions (GTM Preview, Tag Assistant, Google Ads debug)

After analyzing the repo, output:
- Summary of files that will be modified
- Full updated code for each changed file (with clear `diff` style or full file)
- Any additional files to create (e.g. tracking.js)
- Step-by-step implementation guide

Start by exploring the repository structure and key files.
Based on the above prompt and analysis of the repo generate me a prompt I can feed into codex/replit to make these changes so that my conversions are tracked accordingly
