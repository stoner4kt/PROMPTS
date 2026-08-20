# TASK: Create a **fully self-contained, lightweight, zero-dependency** horizontal logo carousel for t

TASK:
Create a **fully self-contained, lightweight, zero-dependency** horizontal logo carousel for this website that, without touching or breaking any current layout, theme, colors, fonts, or content.

Requirements for the carousel:
1. Display all 6 logos in a smooth, infinite, auto-scrolling carousel (pause on hover).
2. Logos must remain large, prominent, high-contrast, and fully visible on every screen size (minimum 120px height on desktop, scale gracefully on mobile).
3. Use only vanilla HTML + CSS + a tiny bit of vanilla JS (no external libraries, no Tailwind unless I already use it — keep it theme-agnostic with inline styles + CSS variables so it blends perfectly).
4. Make it 100% responsive and mobile-optimized (touch swipe support, no horizontal scroll overflow, fast performance).
5. Add a clear disclaimer directly underneath the carousel:  
   “We repair and service appliances from these leading brands. We are an independent repair service and are not officially affiliated, authorized, or endorsed by any of these manufacturers.”
6. The entire section must be wrapped in a semantic <section> with a unique ID (id="brands-we-service") and neutral class names so I can easily insert it at the bottom of the main content area on the homepage AND on any other service/repair pages without layout shifts.
7. Keep loading fast: use lazy loading on images, proper aspect-ratio preservation, and minimal JS.

Additionally:
- Update my existing footer to include a new link: “Privacy Policy” that points to privacy-policy.html (add it as the last link in the footer, using the exact same styling as my current footer links — do not change any other footer content).
- Create a complete, ready-to-use privacy-policy.html page (full HTML document) with professional, South African-compliant privacy policy content for an appliance repair business. Include sections on: data we collect, how we use it, cookies, contact info, last updated date, and a clear statement that we respect user privacy. Make the page match the same header/footer style as the rest of the site (use the same CSS variables or inline styles so it looks native). Add a prominent “Back to Home” button.

Output format:
1. First, output the complete <section id="brands-we-service">…</section> HTML + CSS + JS code (ready to copy-paste into any page).
2. Second, output the exact footer link code snippet to add.
3. Third, output the full privacy-policy.html file content.
4. Finally, give me 3 short instructions on exactly where to place each piece so nothing breaks.

Ensure exceptional UX: smooth 60fps animation, accessible (ARIA labels, keyboard navigation), no CLS, fully optimized for all devices especially mobile, and the logos stay crisp and prominent at every breakpoint. Do not suggest any changes to my existing layout, theme, or content — only add this new section and the privacy page.
