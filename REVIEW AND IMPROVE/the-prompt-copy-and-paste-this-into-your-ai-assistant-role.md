# ### The Prompt (Copy and paste this into your AI assistant) **Role:**

### The Prompt (Copy and paste this into your AI assistant)

**Role:** Act as a Senior DevOps Engineer and Code Architect specializing in repository hygiene and dependency analysis.

**Context & Goal:** I want to clean up my repository to reduce its size, remove clutter, and improve maintainability—**without breaking any existing functionality**. I need a detailed, surgical audit of my files.
Repo: https://github.com/stoner4kt/ToursystemV1-clone-for-Codebase-Cleanup/tree/main 
**Step 1: Analyze the following context:**
I will provide you with:
1. The output of my project's folder tree (e.g., `tree -a -I "node_modules|.git|venv|__pycache__" > structure.txt`).
2. The contents of my dependency files (e.g., `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `Gemfile`, etc.).
3. My `.gitignore` file.
4. *(Optional)* The contents of my main entry point files (e.g., `index.js`, `main.py`, `app.py`).

**Step 2: Perform the "Clutter Cleanup" Analysis:**
You must scan for and categorize the following items. For each item you suggest removing, provide a **clear, technical justification** and a **Risk Level**.

**Category A: [SAFE TO DELETE] - 100% Redundant (No Functional Impact)**
- Compiled Python bytecode (`__pycache__/`, `*.pyc`, `*.pyo`).
- System junk files (`.DS_Store`, `Thumbs.db`, `*.tmp`, `*.log`).
- Dependency lockfiles that are no longer standard (e.g., `yarn.lock` if using `npm`, or vice versa).
- Duplicate backup files (e.g., `file~`, `file.bak`).

**Category B: [SAFE TO IGNORE] - Files to add to .gitignore (not delete from local, just stop tracking)**
- Local environment configs (`.env.local`, `.env.development`).
- Editor-specific folders (`.vscode/`, `.idea/`).
- Build caches (`.vite/`, `.next/`, `.nuxt/`, `.parcel-cache/`).
- Package manager install folders (`node_modules/`, `venv/`, `vendor/`).
- Test coverage folders (`coverage/`, `.nyc_output`).

**Category C: [REQUIRES VERIFICATION] - Dead Code & Unused Assets**
- Analyze `package.json` / `requirements.txt` - identify **unused dependencies** by checking if they are imported anywhere in the source code.
- Analyze the `assets/`, `images/`, or `static/` folders for files that are not referenced in any `.js`, `.html`, `.md`, or `.css` file.
- Identify JavaScript/Typescript files that are never imported or required in the entry points.
- *Action:* Suggest these for deletion but require manual confirmation.

**Category D: [DO NOT DELETE] - Critical Infrastructure**
- Explicitly flag `.git`, `Dockerfile`, `docker-compose.yml`, `README.md`, `LICENSE`, `.github/` workflows, and core configuration files (e.g., `vite.config.js`, `webpack.config.js`, `next.config.js`) as **untouchable** unless explicitly confirmed by the user.

**Step 3: Generate a "Surgical Cleanup Report":**
Structure your output exactly as follows:

1. **Executive Summary:** Total files, total size, and estimated size savings.
2. **Recommended `.gitignore` Update:** Provide the exact lines to add to my `.gitignore`.
3. **Deletion Checklist (Grouped by Safety):**
   - **Group 1 (Run immediately):** List files/folders to delete via terminal commands.
   - **Group 2 (Verify & Delete):** List unused dependencies with the command to uninstall them.
   - **Group 3 (Review manually):** List potentially unused source-code files with a note on why they seem redundant.
4. **Post-Cleanup Validation Checklist:** A list of commands I should run *after* deleting to ensure the build/test/pipeline still passes (e.g., `npm run build`, `pytest`, `cargo check`).

**Final Instruction:** Before I execute anything, I want you to write a small bash/PowerShell script that performs *only* the **Group 1 (Run immediately)** deletions, so I can review the script before running it. Do not automatically run destructive commands.
Or Generate me a prompt I can feed into codex/replit to perform the changes for me and also explain why and what get removed
---
