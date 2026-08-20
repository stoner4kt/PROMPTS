# Prompt Library

A structured, reusable prompt library extracted from exported LLM conversation
history across multiple providers (Claude, Grok, ChatGPT/Perplexity). Only the
core user-prompt content is retained — model outputs, metadata, auto-generated
titles, and conversational filler are stripped.

## Source data

Raw exports live in `RAW-DATA/`. The extraction pipeline parses:

| Provider | Source files | Format |
| --- | --- | --- |
| Claude | `conversations*.json` | `chat_messages[]` with `sender` = `human` |
| Claude Projects | `019b*.json`, `019c*.json` | `prompt_template` + embedded `docs[]` |
| Grok (X) | `prod-grok-backend.json` | `conversations[].responses[]`, `tasks`, `media_posts` |
| ChatGPT / Perplexity | `conversations-20260820_*.json` | `conversations[].entries[].query` |

Gemini and DeepSeek exports in `RAW-DATA/` contained no conversation content
(empty HTML shells and profile-only JSON) and therefore produced no threads.

## Directory structure

Each directory holds standardized Markdown files — one file per prompt thread,
with follow-up prompts within a thread separated by `---`.

| Category | Threads | Purpose |
| --- | ---: | --- |
| `BUILD/` | 266 | Building features, sites, apps, bots, integrations |
| `SEO/` | 39 | SEO / AEO / GEO, ranking, Google Ads & Business Profile |
| `DEBUG/` | 33 | Bug fixes, errors, login/auth issues, troubleshooting |
| `DESIGN/` | 30 | UI/UX, branding, logos, media-generation prompts |
| `REVIEW AND IMPROVE/` | 24 | Refactoring, audits, code review, optimization, docs |
| `MARKETING/` | 19 | Client acquisition, outreach, pricing, strategy |
| `GENERAL/` | 10 | Everything else |

**Total: 421 threads · 1,356 prompts**

`MARKETING/` and `GENERAL/` are new directories created to accommodate growth
in the agency's web-development and marketing services.

## Templates

`TEMPLATES/` holds standardized, parameterized prompt *templates* (distinct from
the verbatim extracted prompts above). Replace the bracketed variables
(e.g., `[CLIENT_NAME]`) before use.

| File | Purpose |
| --- | --- |
| `TEMPLATES/reusable-ai-prompt-templates.md` | Content & copywriting strategy, technical SEO & asset map, and data-analysis action-matrix templates |

## File format

Each `.md` file contains:

```
# <short title derived from the user's own words>

<first user prompt>

---

<second user prompt>
```

No external information is added; content is taken verbatim from the exports.

## Regenerating

```
python3 sort_prompts.py
```

The script re-parses `RAW-DATA/`, re-classifies every thread, and rewrites the
category directories. It is deterministic and safe to re-run as new exports are
dropped into `RAW-DATA/`.