# I have a client wants me to build them a website for

I have a client wants me to build them a website for their jumping castle hire business. I want to build a professional website with a landing page built for leads conversion using html, css, js and the contact form should store data in netlify and I will deploy it on netlify. I want a buetiful design with image  animations and transitions.

---

Can you put all these files into the repo https://github.com/stoner4kt/Sipho-Jumping-Castle.git in my github, it's a new repo just for this project

---

Act as an expert frontend developer. I need you to fix the mobile responsiveness and layout alignment issues on my website based on the video "SVID_20260628_225113_1.mp4". 

Please generate ONLY the necessary HTML/CSS or React adjustments to fix these bugs. Do NOT change the branding, copy, color scheme, typography, button text, or overall structure. Keep everything else exactly as is.

Here are the specific layout bugs from the video "SVID_20260628_225113_1.mp4" that need to be fixed for all devices (especially mobile):

1. **Fix Header & Hero Section Scaling:**
   - In the first 2 seconds of "SVID_20260628_225113_1.mp4", the hero section elements (text, buttons, and "Fully Insured / Same-Day Setup / 1000+ Happy Kids" badges) look vertically constrained or squished. Ensure proper padding, line-heights, and flexible flexbox/grid layout handling so they scale beautifully on small screens without overlapping.

2. **Fix Overlapping Icons in "Our Jumping Castles" Section:**
   - At timestamp 0:01 of "SVID_20260628_225113_1.mp4", the small castle icons are completely overlapping the section heading text ("Our Jumping Castles"). 
   - Remove any absolute positioning or breaking margins causing this overlap. Ensure these decorative elements sit cleanly inline, above, or below the heading using safe CSS flex/grid gaps.

3. **Fix Product Card & Gallery Image Layouts:**
   - From 0:02 to 0:06 of "SVID_20260628_225113_1.mp4", the product cards (Classic Castle, Mega Slide Combo, Princess Palace) and the "Gallery of Joy" images are stacked in a single stretched column with no container constraints.
   - Ensure that on mobile, these images and cards have a clean max-width (e.g., using `max-width: 100%; height: auto; object-fit: cover;`) so they don't distort.
   - Provide a CSS media query so that these elements elegantly transition into side-by-side rows/grids on desktop screens while remaining perfectly stacked on mobile.

4. **Ensure Global Viewport Responsiveness:**
   - Make sure the global configuration handles mobile scaling correctly. Ensure the standard `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is implemented so mobile browsers render the mobile layouts natively rather than shrinking a desktop frame.

Please output the clean, refactored CSS/HTML code snippets needed to resolve these specific layout breaks while leaving all other aspects of the site entirely untouched. Bouncing Bee Castles is the business name update it. Then commit these changes to a new branch for me to review name Fixes

---

You didn't make the changes please apply the fixes
