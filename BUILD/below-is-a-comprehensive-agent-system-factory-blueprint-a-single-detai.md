# Below is a comprehensive **"Agent System Factory Blueprint"** — a single, detailed

Below is a comprehensive **"Agent System Factory Blueprint"** — a single, detailed prompt you can feed into any AI (Replit Agent, Codex, OpenHands, etc.) to build out the entire repository structure, all agent prompts, and the supporting documentation.

---

## The Master Prompt: "Build My Agent System Factory"

---

### INSTRUCTIONS FOR THE AI

You are tasked with building a complete **Agent System Factory** — a reusable, version-controlled repository that serves as a "blueprint" for generating static websites through a phased, multi-agent workflow.

**Repository Name:** `agent-system-factory`

**Repository Type:** Private template repository on GitHub

**Core Philosophy:** This is a "factory blueprint" that gets cloned fresh for each client project. The client's final website code lives in a `/site/` subfolder, which gets exported to a clean repository at the end — leaving all agent logic, prompts, and business context behind in the factory workspace.

---

### PART 1: Repository Structure

Create the following folder and file structure:

```
agent-system-factory/
│
├── AGENTS.md                         # Master instruction file for any AI agent entering this repo
├── README.md                         # Human-readable documentation
├── .gitignore                        # Standard ignores + business-info.json protection
│
├── business-info.json                # Single source of truth for client data (starts empty)
│
├── /prompts/                         # All phase-specific agent instructions
│   ├── 00_context_setup.md
│   ├── 01_scaffolder.md
│   ├── 02_designer.md
│   ├── 03_logic_engineer.md
│   ├── 04_seo_aeo.md
│   └── 05_production_export.md
│
├── /rules/
│   └── constraints.md                # Global rules EVERY agent must follow
│
├── /templates/
│   └── /base-scaffold/               # The starter HTML/CSS/JS skeleton
│       ├── index.html
│       ├── /css/
│       │   └── style.css
│       ├── /js/
│       │   └── app.js
│       └── /assets/
│           └── (empty)
│
└── /scripts/                         # Optional helper scripts
    ├── new-client.sh                 # One-command client onboarding
    └── export-site.sh                # One-command production export
```

---

### PART 2: File Contents

#### 2.1 `AGENTS.md` — The Master Instruction File

This file is the "operating manual" for any AI agent entering this repository. It should contain:

```markdown
# AGENTS.md — Agent System Factory

## Project Identity
This is the **Agent System Factory** — a reusable blueprint for building static websites through a phased, multi-agent workflow.

**Critical Rule:** You are operating inside the FACTORY, not the final client repository. The client's website lives in `/site/`. Everything else is factory infrastructure.

## Repository Map
| Path | Purpose |
|------|---------|
| `/business-info.json` | Single source of truth for client data. READ FIRST. |
| `/prompts/` | Phase-specific agent instructions (00–05). |
| `/rules/constraints.md` | Global rules ALL agents must follow. |
| `/templates/base-scaffold/` | Starter HTML/CSS/JS skeleton. |
| `/site/` | **THE CLIENT WEBSITE** — this is the ONLY folder you modify. |

## The Golden Rule
**You are ONLY allowed to modify files inside `/site/`.** Never edit files in `/prompts/`, `/rules/`, `/templates/`, or `/business-info.json` unless explicitly instructed to do so by the user.

## Setup Commands
- Copy scaffold to site: `cp -r templates/base-scaffold/* site/`
- Initialize client Git: `cd site && git init && git add . && git commit -m "Initial scaffold"`

## Code Style (for files inside /site/)
- HTML: Semantic HTML5, indentation 2 spaces
- CSS: Mobile-first, BEM naming convention
- JS: Vanilla ES6, no frameworks

## Boundaries
- Never commit secrets or API keys
- Never use absolute paths (always relative: `./css/style.css`)
- Never modify `package.json` (there is none — pure static site)
- Always read `business-info.json` before starting any phase
```

---

#### 2.2 `README.md` — Human Documentation

```markdown
# Agent System Factory

A reusable blueprint for generating static websites through a phased, multi-agent workflow.

## Quick Start

### 1. Clone the factory
```bash
git clone https://github.com/you/agent-system-factory.git client-project-name
cd client-project-name
```

### 2. Initialize the client site
```bash
cp -r templates/base-scaffold/* site/
cd site && git init && git add . && git commit -m "Initial scaffold"
```

### 3. Run Phase 0: Context Setup
Open this workspace in Replit, Codex, or OpenHands and paste the contents of `/prompts/00_context_setup.md`.

### 4. Run Phases 1–5 sequentially
Each phase builds on the previous one. Review the output after each phase before proceeding.

### 5. Export the final site
```bash
cp -r site/* ~/Desktop/client-name-final/
```

## The 6 Phases

| Phase | Agent | Task |
|-------|-------|------|
| 0 | Context Setup | Populate `business-info.json` |
| 1 | Scaffolder | Build HTML structure |
| 2 | Designer | Apply CSS styling |
| 3 | Logic Engineer | Add JavaScript functionality |
| 4 | SEO/AEO | Inject meta tags & structured data |
| 5 | Production Export | Fix paths, create deployable package |

## Upgrading an Existing Client

1. Clone the factory fresh
2. Pull the client's live code into `/site/`
3. Run the relevant phase(s)
4. Export `/site/` back to the client's repo

## License

MIT — use freely, improve constantly.
```

---

#### 2.3 `business-info.json` — The Context File

```json
{
  "business_name": "",
  "industry": "",
  "tagline": "",
  "description": "",
  "contact_email": "",
  "contact_phone": "",
  "address": "",
  "social_links": {
    "facebook": "",
    "twitter": "",
    "instagram": "",
    "linkedin": ""
  },
  "brand_colors": {
    "primary": "",
    "secondary": "",
    "accent": ""
  },
  "target_audience": "",
  "geo_location": ""
}
```

---

#### 2.4 `/rules/constraints.md` — Global Rules

```markdown
# GLOBAL CONSTRAINTS — Read Before Any Phase

## Rule 0: Business Context Priority
- Before ANY task, read `../business-info.json` (or `./business-info.json` if running from root).
- **If a field is populated (non-empty string):** You MUST use that exact value.
- **If a field is empty:** Generate a realistic placeholder specific to the `industry` field.
- **Email/Phone Fallback:** Use domain-specific placeholders (e.g., if business is "BlueWave", use "hello@bluewave.com").

## Rule 1: File Boundaries
- You are ONLY allowed to modify files inside `/site/`.
- NEVER touch `/prompts/`, `/rules/`, `/templates/`, or `/business-info.json`.

## Rule 2: Paths
- ALL asset paths MUST be relative: `./css/style.css`, `../assets/logo.png`.
- NEVER start a path with a slash `/` (unless it's a full URL like `https://`).

## Rule 3: No Frameworks
- Pure HTML, CSS, and vanilla JavaScript only.
- No React, Vue, Angular, or any npm packages.

## Rule 4: Mobile-First
- All CSS must be mobile-first with responsive breakpoints.

## Rule 5: Accessibility
- All images must have `alt` attributes.
- All interactive elements must be keyboard-navigable.
- Proper ARIA labels where needed.

## Rule 6: Validation
- All HTML must pass W3C validation.
- All CSS must be valid.
- All JavaScript must have no console errors.
```

---

#### 2.5 Phase Prompts (`/prompts/`)

##### 2.5.1 `00_context_setup.md` — Context Setup Agent

```markdown
# PHASE 0: Context Setup Agent

## Your Task
Initialize the business context by populating `business-info.json`.

## Instructions

1. **Read the user's current message.** Extract any business details provided (name, industry, email, phone, etc.).

2. **Examine the workspace.** Look at the folder name or any context clues.

3. **Open `business-info.json`** at the root of the workspace.

4. **If the user provided specific info:**
   - Write it into the JSON fields exactly as given.
   - Overwrite any existing values.

5. **If the user provided no info:**
   - Infer the industry from the folder name or prompt context.
   - Generate realistic placeholders:
     - If `bakery` or `cafe` → "Sweet Delights Bakery", "hello@bakery.com", "(555) 234-5678"
     - If `tech`, `ai`, or `software` → "Nexus AI Solutions", "contact@nexus.ai", "(555) 890-1234"
     - If `fitness` or `gym` → "Peak Performance Gym", "info@peakgym.com", "(555) 456-7890"
     - If `restaurant` → "The Gourmet Kitchen", "reservations@gourmetkitchen.com", "(555) 789-0123"
     - If unknown → "Acme Corporation", "info@acme.com", "(555) 000-0000"

6. **Save the file** with these values.

7. **Output to the user:**
   ```
   ✅ Business context initialized for [business_name] in the [industry] industry.
   📧 Email: [contact_email]
   📞 Phone: [contact_phone]
   ```

## Success Criteria
- `business-info.json` is populated with valid data.
- No fields contain placeholder text like "Your Business" — they are either real data or industry-appropriate generated values.
```

---

##### 2.5.2 `01_scaffolder.md` — HTML Scaffolder Agent

```markdown
# PHASE 1: Scaffolder Agent

## Your Task
Build the complete HTML structure for the client's website inside `/site/index.html`.

## Pre-requisites
- `/site/` folder exists with the base scaffold copied in.
- `business-info.json` is populated (run Phase 0 first).

## Instructions

### Step 1: Read Context
- Open `../business-info.json` (or `./business-info.json`).
- Extract: `business_name`, `tagline`, `description`, `contact_email`, `contact_phone`.

### Step 2: Build the HTML Structure
Create or overwrite `/site/index.html` with:

1. **DOCTYPE and HTML tag** with language attribute.
2. **Head section** containing:
   - `<title>`: `[business_name] - [tagline]`
   - `<meta name="description">`: `[description]`
   - `<meta charset="UTF-8">`
   - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
   - `<link rel="stylesheet" href="./css/style.css">`
3. **Body section** with semantic HTML5 structure:
   - `<header>`: Business name + navigation
   - `<main>`: 
     - Hero section with tagline
     - About section with description
     - Services/Features section (3–4 placeholder items)
     - Contact section with email and phone from business-info
   - `<footer>`: Business name, email, phone, copyright

### Step 3: Use Placeholder Content
- For any content not specified in `business-info.json`, use industry-appropriate placeholders.
- All placeholder images should use `https://via.placeholder.com/` or similar.

### Step 4: Save and Report
- Save the file.
- Output: `✅ Scaffold created for [business_name] at /site/index.html`

## Success Criteria
- Valid HTML5.
- All business-info fields are correctly injected.
- Semantic structure is complete.
- All links use relative paths.
```

---

##### 2.5.3 `02_designer.md` — CSS Designer Agent

```markdown
# PHASE 2: Designer Agent

## Your Task
Apply professional CSS styling to the website inside `/site/css/style.css` and add appropriate classes to `/site/index.html`.

## Pre-requisites
- Phase 1 completed (`/site/index.html` exists).
- `business-info.json` is populated.

## Instructions

### Step 1: Read Context
- Open `business-info.json`.
- Extract: `industry`, `brand_colors` (primary, secondary, accent).

### Step 2: Design the CSS
Create or overwrite `/site/css/style.css` with:

1. **CSS Reset/Normalize** at the top.
2. **Global Styles**: Font family, base font size, line height, color.
3. **Color Palette**:
   - If `brand_colors.primary` is set → use it as the primary color.
   - If not → generate a color palette appropriate for the `industry`:
     - Bakery/Cafe → warm browns, creams
     - Tech/AI → blues, purples, dark mode
     - Fitness/Gym → bold reds, blacks, neon accents
     - Restaurant → warm oranges, deep reds
     - Default → clean blues and whites
4. **Layout**: Mobile-first flexbox/grid layout.
5. **Typography**: Appropriate font sizes, weights, and spacing.
6. **Components**: Style all HTML elements (header, hero, sections, buttons, forms, footer).
7. **Responsive Breakpoints**: At minimum: mobile (default), tablet (768px), desktop (1024px).

### Step 3: Add Classes to HTML
- Open `/site/index.html`.
- Add appropriate CSS classes to all elements.
- Ensure class names follow BEM convention (e.g., `.hero__title`, `.nav__link`).

### Step 4: Save and Report
- Save both files.
- Output: `✅ Design applied with [color_palette_name] palette.`

## Success Criteria
- Mobile-first responsive design.
- All pages look professional and on-brand.
- No inline styles (all in CSS file).
- All colors are accessible (sufficient contrast ratio).
```

---

##### 2.5.4 `03_logic_engineer.md` — JavaScript Logic Agent

```markdown
# PHASE 3: Logic Engineer Agent

## Your Task
Add all JavaScript functionality to the website inside `/site/js/app.js`.

## Pre-requisites
- Phase 2 completed (`/site/index.html` and `/site/css/style.css` exist).
- `business-info.json` is populated.

## Instructions

### Step 1: Read Context
- Open `business-info.json`.
- Extract: `contact_email`, `contact_phone`.

### Step 2: Build the JavaScript
Create or overwrite `/site/js/app.js` with:

1. **DOM Ready Check**: Wrap all code in a DOMContentLoaded event listener.

2. **Mobile Navigation Toggle**:
   - Hamburger menu toggle for mobile.
   - Smooth open/close animation.

3. **Contact Form Handling** (if a contact form exists in HTML):
   - Form validation (email format, required fields).
   - Submit handler with preventDefault.
   - Success/error message display.
   - Pre-fill email field with `contact_email` from business-info.

4. **Smooth Scrolling** for anchor links.

5. **Interactive Elements**:
   - Any buttons with hover/click feedback.
   - Any carousels or sliders (if present).
   - Any accordion or tab components.

6. **Console Log Prevention**: No console.log statements in production code.

### Step 3: Link the Script
- Ensure `/site/index.html` includes `<script src="./js/app.js" defer></script>` before the closing `</body>` tag.

### Step 4: Save and Report
- Save the file.
- Output: `✅ JavaScript logic added with [number] features.`

## Success Criteria
- All interactive elements work.
- No console errors.
- Form validation works.
- Mobile navigation functions correctly.
- Code is clean and well-commented.
```

---

##### 2.5.5 `04_seo_aeo.md` — SEO & AEO Optimization Agent

```markdown
# PHASE 4: SEO & AEO Optimization Agent

## Your Task
Optimize the website for search engines (SEO) and AI engines (AEO).

## Pre-requisites
- Phase 3 completed.
- `business-info.json` is populated.

## Instructions

### Step 1: Read Context
- Open `business-info.json`.
- Extract: `business_name`, `description`, `contact_email`, `contact_phone`, `address`, `social_links`.

### Step 2: Enhance Meta Tags in `/site/index.html`
Add or update these tags in the `<head>`:

```html
<!-- Primary Meta -->
<meta name="description" content="[description]">
<meta name="keywords" content="[industry-related keywords]">

<!-- Open Graph (Social Sharing) -->
<meta property="og:title" content="[business_name]">
<meta property="og:description" content="[description]">
<meta property="og:type" content="website">
<meta property="og:url" content="https://[business_name].com">
<meta property="og:image" content="./assets/og-image.jpg">

<!-- Twitter Cards -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[business_name]">
<meta name="twitter:description" content="[description]">

<!-- Robots -->
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://[business_name].com">
```

### Step 3: Add JSON-LD Structured Data
Insert this `<script type="application/ld+json">` block in the `<head>`:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[business_name]",
  "description": "[description]",
  "email": "[contact_email]",
  "telephone": "[contact_phone]",
  "address": "[address]",
  "url": "https://[business_name].com",
  "sameAs": [
    "[facebook_url]",
    "[twitter_url]",
    "[instagram_url]",
    "[linkedin_url]"
  ]
}
```

**Rules:**
- If any field is empty, omit it from the JSON-LD.
- Ensure all URLs are valid.
- If the site has FAQ content, add `FAQPage` schema as well.

### Step 4: Create Supporting Files
- Create `/site/robots.txt`:
  ```
  User-agent: *
  Allow: /
  Sitemap: https://[business_name].com/sitemap.xml
  ```
- Create `/site/sitemap.xml`:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://[business_name].com/</loc>
      <lastmod>[today's date]</lastmod>
      <priority>1.0</priority>
    </url>
  </urlset>
  ```

### Step 5: Image Optimization
- Add `loading="lazy"` to all `<img>` tags.
- Ensure all images have descriptive `alt` attributes.
- If using placeholder images, note they should be replaced with real images.

### Step 6: Save and Report
- Save all files.
- Output: `✅ SEO/AEO optimization complete. Schema added. Robots.txt and sitemap.xml created.`

## Success Criteria
- All meta tags are present and populated.
- JSON-LD validates with Google's Rich Results Test.
- robots.txt and sitemap.xml are valid.
- All images have alt text and lazy loading.
```

---

##### 2.5.6 `05_production_export.md` — Production Export Agent

```markdown
# PHASE 5: Production Export Agent

## Your Task
Prepare the `/site/` folder for production deployment.

## Pre-requisites
- Phase 4 completed.
- All files are in `/site/`.

## Instructions

### Step 1: Verify All Paths Are Relative
- Scan all HTML, CSS, and JS files.
- Ensure NO paths start with `/` (root-absolute).
- Convert any absolute paths to relative:
  - `/images/logo.png` → `./assets/logo.png`
  - `/css/style.css` → `./css/style.css`
- **Why:** cPanel deployments live in subdirectories; absolute paths break.

### Step 2: Create Deployment Configs

**For Vercel** — Create `/site/vercel.json`:
```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

**For Netlify** — Create `/site/netlify.toml`:
```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Step 3: Minify Assets (Optional)
- If the user requests it, minify CSS and JS.
- Create `.min` versions alongside originals.

### Step 4: Create Export Package
```bash
cd site
zip -r ../site-export.zip .
```

### Step 5: Report
Output to the user:
```
✅ Production export complete!

📦 Package: site-export.zip
📁 Location: /site/

Deployment options:
- Vercel/Netlify: Push the /site/ folder to your Git repo
- cPanel: Upload site-export.zip to public_html and extract
```

## Success Criteria
- All paths are relative.
- Deployment configs exist.
- No console errors when opening index.html directly.
- Site works when opened from a file:// path.
```

---

#### 2.6 Helper Scripts (`/scripts/`)

##### 2.6.1 `new-client.sh` — One-Command Onboarding

```bash
#!/bin/bash
# Usage: ./scripts/new-client.sh client-name

CLIENT_NAME=$1
if [ -z "$CLIENT_NAME" ]; then
  echo "❌ Usage: ./scripts/new-client.sh client-name"
  exit 1
fi

echo "🚀 Creating new client: $CLIENT_NAME"

# Create the client site folder
mkdir -p site
cp -r templates/base-scaffold/* site/

# Initialize Git inside site
cd site
git init
git add .
git commit -m "Initial scaffold for $CLIENT_NAME"

echo "✅ Client $CLIENT_NAME initialized at /site/"
echo "📋 Next: Run Phase 0 (Context Setup) with your business details"
```

##### 2.6.2 `export-site.sh` — One-Command Export

```bash
#!/bin/bash
# Usage: ./scripts/export-site.sh ~/Desktop/client-final

OUTPUT_DIR=$1
if [ -z "$OUTPUT_DIR" ]; then
  echo "❌ Usage: ./scripts/export-site.sh /path/to/output"
  exit 1
fi

echo "📦 Exporting /site/ to $OUTPUT_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Copy site contents
cp -r site/* "$OUTPUT_DIR/"

# Remove .git from the export (clean client repo)
rm -rf "$OUTPUT_DIR/.git"

echo "✅ Site exported to $OUTPUT_DIR"
echo "📋 Next: Initialize a fresh Git repo and push to client's repository"
```

---

### PART 3: How to Use This Factory

#### Starting a New Client Project

1. **Clone the factory:**
   ```bash
   git clone https://github.com/you/agent-system-factory.git client-acme
   cd client-acme
   ```

2. **Run the onboarding script:**
   ```bash
   ./scripts/new-client.sh acme-corp
   ```

3. **Open in your AI environment:**
   - **Replit:** Import the repository.
   - **Codex/OpenHands:** Navigate to the folder in your terminal.
   - **Grok API:** Write a script that reads the prompt files.

4. **Execute Phase 0:**
   - Paste the contents of `/prompts/00_context_setup.md` into your AI.
   - Provide any business details you have.

5. **Execute Phases 1–5 sequentially:**
   - After each phase, review the output.
   - Commit changes inside `/site/` if desired.

6. **Export the final product:**
   ```bash
   ./scripts/export-site.sh ~/Desktop/acme-final
   ```

7. **Push to client's repository:**
   ```bash
   cd ~/Desktop/acme-final
   git init
   git add .
   git commit -m "Initial production release"
   git remote add origin https://github.com/client/acme-site.git
   git push -u origin main
   ```

8. **Delete the factory workspace:**
   ```bash
   rm -rf client-acme
   ```

#### Upgrading an Existing Client

1. **Clone the factory fresh** (with your latest improved prompts).
2. **Pull the client's live code** into `/site/`.
3. **Run the relevant phase(s).**
4. **Export `/site/`** back to the client's repo.
5. **Delete the factory workspace.**

---

### PART 4: Open-Source References to Study

Here are excellent open-source repositories that informed this design and can serve as inspiration:

| Repository | What It Teaches | Key Takeaway |
|------------|-----------------|--------------|
| **[better-agents](https://github.com/langwatch/better-agents)** | Production agent structure with tests, evaluations, and versioned prompts. | Version your prompts like code. Use `AGENTS.md` as the entrypoint. |
| **[agentic-engineering-starter-pack](https://github.com/tngwilkins/agentic-engineering-starter-pack)** | Knowledge-base approach where the repo is the single source of truth. | Every decision lives in the repo. Agents read from it, humans review it. |
| **[SDD_Flow](https://github.com/Ataden/SDD_Flow)** | Spec-Driven Development with AI coding agents. | "Specs are the new code." Use structured templates for each phase. |
| **[seven-layer-prompt](https://github.com/LidienFu/seven-layer-prompt)** | Production prompt architecture with FIXED vs CONFIG layers. | Separate shared core (FIXED) from per-client config (CONFIG). |
| **[one-prompt-agents](https://github.com/ivanpostolski/one-prompt-agents)** | Lightweight agent definition with prompt + config file. | Each agent is self-contained in its own directory. |
| **[gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)** | Focused agent workflows for SEO/AEO optimization. | Each skill ships a concrete artifact — audit, plan, or code fix. |
| **[Agents as Code](https://arinco.com.au/blog/agents-as-code-treating-ai-agents-as-versioned-artifacts/)** | Treating agents as versioned artifacts, not throwaway prompts. | `AGENTS.md` is the operating manual for any AI agent. |

---

### PART 5: Development Environment Notes

#### For Replit
- Import the factory repository directly.
- The `AGENTS.md` file is automatically detected by Replit Agent.
- Copy-paste each phase prompt from `/prompts/` into the chat.
- Use checkpoints to review after each phase.

#### For Codex / OpenHands
- Navigate to the factory folder in your terminal.
- Use file references: `@/prompts/01_scaffolder.md` to load prompts.
- Codex loads `AGENTS.md` automatically.
- OpenHands uses `AGENTS.md` as permanent context.

#### For Grok / Other API-based Agents
- Write a simple script that reads the prompt file and sends it to the API.
- Example Python snippet:
  ```python
  with open('prompts/02_designer.md', 'r') as f:
      prompt = f.read()
  # Send prompt to Grok API with the /site/ folder as context
  ```

#### For Cursor / Windsurf
- Place the factory folder in your workspace.
- The IDE's AI will read `AGENTS.md` automatically.
- Use `@` to reference specific prompt files.

---

### PART 6: The One Golden Rule (Repeated for Emphasis)

> **You are ONLY allowed to modify files inside `/site/`.** 
> 
> The factory (`AGENTS.md`, `/prompts/`, `/rules/`, `/templates/`, `/business-info.json`) is sacred infrastructure. It gets cloned fresh for each client. Never mutate it during a client build.

This ensures:
- Your prompts improve over time (you update the master repo).
- No client ever sees your proprietary agent logic.
- You can delete a client workspace without losing your factory.
- Upgrading a client is as simple as cloning the factory fresh.

---

Yes go ahead and build the entire repo with all files necessary that I can download

---

So how would I go about setting up my first environment for a client step by step indepth

---

I will do option a making my agent repo a template repo that I could just update and reuse and guide me on how I'd go about the on my mobile device as I'll be using replit and codex form the browser

---

What if i don't want to use the shell and just do commits normally with pr

---

But now I don't want to have to do manual edit, I just want to prompt the model and it should work of the agents

---

Can you bake these necessary steps in into file having the model ask my for the destination repo when I want to do the final export ensure that I can easily switch between codex/replit/hermes/openhands when I use it

---

Okay so when ever I want to start a phase with a agent, I will paste this in only changing the prompt  file I'm targeting :Read AGENTS.md in this repo first. Follow the instructions in prompts/02_designer.md. Work on a new branch and open a PR against main.

---

Can i have phase 0 ask me for business information if I don't already have it in my business.json file and don't upload it in the prompt. Add also in the feature to not commit directly to the main under any circumstances
