# I need you to generate a detailed implementation prompt that I can

I need you to generate a detailed implementation prompt that I can feed into Codex/Replit to update my website (https://appliance-911.co.za). The goal is to boost leads and revenue by expanding our service offerings and improving our SEO presence.

### Context

I run Appliance-911, a same-day appliance and gas repair service based in Cape Town. Our website currently promotes repairs for:
- Gas stoves, gas cooktops, gas ovens
- Gas braais (barbecues/grills)
- Gas fireplaces (ALREADY EXISTS - do not create a new page for this)
- Refrigerators, washing machines, dryers, dishwashers, microwaves

### New Services to Add (7 New Categories)

I want to expand my service pages to include these additional gas appliance repair services (note: Gas Fireplace is EXCLUDED from this list because it already exists):

1. Gas Geysers (Water Heaters)
2. Gas Space Heaters
3. Gas Central Heating Boilers
4. Gas Pool Heaters
5. Gas Patio Heaters
6. Gas Tumble Dryers
7. Gas Range Cookers

### Required Updates

Please generate a prompt for Codex/Replit that will:

1. **Update the About Us page** (`/about.html` - create if missing, otherwise update) to:
   - Reflect that we are Cape Town's comprehensive gas appliance repair specialists
   - List ALL services (current + new + existing fireplace) in a clear, scannable format. The full combined list should be: Gas Stoves, Gas Ovens, Gas Cooktops, Gas Braais, Gas Fireplaces, Gas Geysers, Gas Space Heaters, Gas Central Heating Boilers, Gas Pool Heaters, Gas Patio Heaters, Gas Tumble Dryers, and Gas Range Cookers.
   - Emphasize our certifications (SAQCC Gas registered technicians)
   - Highlight our 2-year warranty, same-day service, and upfront pricing
   - Include trust signals (certified technicians, warranty, service areas)
   - Maintain a professional, trustworthy tone that converts visitors into leads

2. **Create individual service pages** for EACH of the 7 new services (do NOT create one for gas fireplaces):
   - URL structure: `/services/gas-geyser-repair.html`, `/services/gas-space-heater-repair.html`, `/services/gas-boiler-repair.html`, `/services/gas-pool-heater-repair.html`, `/services/gas-patio-heater-repair.html`, `/services/gas-tumble-dryer-repair.html`, `/services/gas-range-cooker-repair.html`
   - Each page must have unique, SEO-optimized content (300+ words minimum)
   - Include common problems, benefits of professional repair, safety considerations
   - Include a clear call-to-action (book now / get a quote)
   - Add schema markup (Service schema, LocalBusiness schema)
   - Include location-specific content (Cape Town, Atlantic Seaboard, Southern Peninsula, Northern Suburbs)

3. **Update the homepage** (`/index.html`) to:
   - Add the 7 new services to the "What We Fix" section (keep gas fireplace as it is already there)
   - Ensure the meta description and title tag reflect the expanded service range
   - Update any "popular services" or featured sections if needed

4. **Update robots.txt** (currently at `/robots.txt`) to:
   - Ensure all 7 new service pages are crawlable
   - Keep `Disallow: /success.html` as is
   - Add any necessary directives for the new content

5. **Create/Update sitemap.xml** (currently referenced but may return an error) to:
   - Include all existing pages (including the already-existing gas fireplace page) AND the 7 new service page URLs
   - Include the About Us page
   - Include lastmod, changefreq, and priority tags
   - Generate the sitemap in the proper XML format so it validates

### SEO Requirements

- Target keywords for each service (e.g., "gas geyser repair Cape Town", "gas pool heater repair near me")
- Optimize title tags and meta descriptions for each new page
- Use proper heading hierarchy (H1, H2, H3)
- Include internal linking between related service pages (and link back to the existing fireplace page where relevant)
- Ensure all new content is original and not duplicated
- Add location-specific content to capture local search traffic in Cape Town and surrounding suburbs

### Technical Requirements

- The site appears to be a static HTML site (based on the source code I've seen)
- Generate clean, semantic HTML
- Ensure mobile responsiveness
- Maintain the existing design language and branding (blue theme #0066cc)
- No breaking changes to existing functionality

### Conversion Goals

- Make it easy for visitors to book a repair (prominent phone number and booking button)
- Include trust signals throughout (certifications, warranty, reviews if available)
- Add emergency/same-day service calls to action
- Generate leads through contact forms or phone calls

### Output Format

Please generate a single, comprehensive prompt that I can copy and paste into Codex/Replit. This prompt should:

1. Clearly state the project goal
2. List all files to be created/modified with their full paths
3. Provide detailed specifications for each file's content
4. Include SEO metadata for each new page
5. Specify any configuration changes needed

The prompt should be so detailed that Codex/Replit can generate the complete code without additional clarification.

---

### Files to be created/modified: /services/gas-geyser-repair.html (CREATE)
/services/gas-space-heater-repair.html (CREATE)
/services/gas-boiler-repair.html (CREATE)
/services/gas-pool-heater-repair.html (CREATE)
/services/gas-patio-heater-repair.html (CREATE)
/services/gas-tumble-dryer-repair.html (CREATE)
/services/gas-range-cooker-repair.html (CREATE)
/about.html (CREATE or UPDATE)
/index.html (UPDATE)
/robots.txt (UPDATE)
/sitemap.xml (CREATE or UPDATE)### Additional Notes

- The existing site uses a blue theme (#0066cc) - maintain this
- The site has a "Book Now" / "Schedule Repair" CTA - ensure this is consistent across all new pages
- The site mentions service areas: Sea Point, Camps Bay, Fish Hoek, Noordhoek, Durbanville, and surrounding areas - incorporate these into new content
- Our technicians are SAQCC Gas registered - this is a key differentiator
- **DO NOT create a page for Gas Fireplaces** - it already exists on the live site, just ensure the sitemap and About Us page reference it correctly alongside the new services

---

Generate me the into a MD file I can download
