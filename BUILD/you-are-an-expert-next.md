# You are an expert Next

You are an expert Next.js 15 + Supabase full-stack architect specializing in maintainable, production-grade fleet management systems.

My project is on the **Edits branch**: https://github.com/stoner4kt/Fleet-system/tree/Edits 
My supabase schema and functions are at https://github.com/stoner4kt/SCHEMAS-AND-SCRIPTS/tree/main/Inyathi/** 
Phase 3 (Code Quality & Architecture refactor) has been applied: `lib/storage.ts` has been split into modular services under `lib/`, with better organization.

**My Goals** (apply all of these on top of the current Edits branch):

1. **Comprehensive Audit Logging**:
   - Create an `audit_logs` table that tracks every significant change (who, what, when, old vs new values, reason).
   - Automatic logging from services (create/update/delete/approve actions).
   - Admin-only view page for audit logs.

2. **Enhanced RBAC (Role-Based Access Control)**:
   - Extend current role system with granular `permissions` array on profiles.
   - `has_permission()` helper function.
   - Permission checks in services and frontend (hook + components).

3. **Settings & Configurability System**:
   - Expand or use `system_config` / new settings table for business-level configuration (branding, defaults, notifications, fleet rules, etc.).
   - Dedicated Admin Settings page with forms and live preview where possible.
   - Make key parts of the app (logo, company name, defaults, colors) pull from settings.

**Requirements**:
- Keep the system **fully operational** at every step — no breaking changes.
- Build on the existing Phase 3 services architecture.
- Provide step-by-step instructions with exact SQL, code snippets, file creations/edits, and integration points.
- Suggest good folder locations for new files (e.g., `lib/services/audit.service.ts`, `features/settings/`, etc.).
- Include how to test each part safely.

First, analyze the current repository structure and key files (especially services in `lib/`, profiles handling, and dashboards). Then give me a complete, prioritized implementation plan with code.

Start by showing the proposed new files/folders and the SQL migrations.

---

Okay I want to do everything except for the system config and the settings feature
