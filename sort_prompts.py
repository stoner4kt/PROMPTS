#!/usr/bin/env python3
"""Sort exported LLM conversation threads into a reusable prompt library.

Parses multi-provider export formats found in RAW-DATA/, extracts only the
core user-prompt content (stripping metadata, model outputs, and auto-titles),
and sorts each prompt thread into the agency's directory structure.

Categories (existing labels + new growth categories):
    BUILD, DEBUG, DESIGN, REVIEW AND IMPROVE, SEO, MARKETING, GENERAL
"""
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "RAW-DATA")

CATEGORIES = [
    "BUILD",
    "DEBUG",
    "DESIGN",
    "REVIEW AND IMPROVE",
    "SEO",
    "MARKETING",
    "GENERAL",
]

# Strong phrases count more than weak ones; title matches count more than body.
STRONG = {
    "DEBUG": [
        "not working", "isn't working", "is not working", "doesn't work",
        "doesnt work", "broken", "bug", "debug", "error", "failing", "failure",
        "fix the", "fixing", "stuck", "hanging", "infinite", "loop", "crash",
        "won't", "wont", "can't", "cant", "not saving", "not displaying",
        "not showing", "not loading", "login issue", "login redirect",
        "login loop", "login hanging", "login loading", "500", "404", "403",
        "401", "exception", "traceback", "disappear", "not persisting",
    ],
    "SEO": [
        "seo", "aeo", "geo", "search engine", "search console", "google ads",
        "google business", "gmb", "gbp", "keyword", "sitemap", "serp",
        "meta tag", "backlink", "local seo", "organic", "rank on google",
        "ranking", "visibility", "ga4", "google analytics", "conversion tracking",
        "ctr", "cpa", "crawl", "indexing", "schema", "roi",
    ],
    "DESIGN": [
        "flyer", "mascot", "logo", "favicon", "navbar", "carousel", "typography",
        "color palette", "colour palette", "branding", "rebrand", "gsap",
        "animation", "cinematic", "photograph", "render", "poster", "ui ",
        "ux ", "user interface", "user experience", "look and feel", "aesthetic",
    ],
    "REVIEW AND IMPROVE": [
        "refactor", "refactoring", "audit", "code review", "code guardian",
        "review the", "review this", "analyze this", "analyze the",
        "documentation", "readme", "best practice", "clean up", "cleanup",
        "restructure", "reorganize", "modernize", "upgrade", "optimization",
        "optimize", "improve", "performance", "load fast", "load faster",
    ],
    "MARKETING": [
        "get clients", "getting clients", "client acquisition", "lead generation",
        "generate leads", "find leads", "find me leads", "get leads",
        "getting leads", "scrape", "scraper", "outreach", "close leads",
        "closing", "sales pitch", "pitch", "proposal", "quote", "pricing",
        "how much should i charge", "charge ", "budget", "invoice", "contract",
        "follow-up", "follow up", "marketing", "strategy", "side hustle",
        "revenue", "business plan", "retainer", "campaign", "advertise",
    ],
    "BUILD": [
        "build a", "build an", "building a", "build me", "create a", "create me",
        "creating a", "make a", "make me", "making a", "develop a", "developing",
        "set up a", "set up the", "setting up", "setup", "implement",
        "generate a", "generate me", "write a", "code a", "website for",
        "landing page", "from scratch", "scaffold", "boilerplate", "new feature",
        "add a", "add feature", "integrate", "integration", "deploy",
        "hosting", "host ", "dashboard", "portal", "pwa", "web app", "webapp",
        "app for", "system for", "chatbot", "bot for", "automation", "cron",
        "edge function", "cloudflare worker", "cloudflare function", "supabase",
        "firebase", "netlify", "vercel", "next.js", "react", "telegram",
        "whatsapp", "prd", "website", "site ",
    ],
}

WEAK = {
    "DEBUG": ["issue", "problem", "resolve", "unable", "mismatch", "revert",
              "reinstall", "dependency", "auth", "login", "refresh", "timezone"],
    "SEO": ["analytics", "lead", "leads", "traffic", "rank"],
    "DESIGN": ["design", "redesign", "css", "style", "styling", "responsive",
               "mobile", "layout", "theme", "font", "color", "icon", "image",
               "visual", "video"],
    "REVIEW AND IMPROVE": ["review", "analyze", "enhance", "enhancement",
                           "simplify", "speed", "docs"],
    "MARKETING": ["clients", "client", "sales", "growth", "promote", "promotion",
                  "cost", "business"],
    "BUILD": ["create", "build", "make", "develop", "code", "page", "section"],
}


def _score_blob(blob: str) -> Counter:
    scores = Counter()
    for cat in CATEGORIES:
        for phrase in STRONG.get(cat, []):
            if phrase in blob:
                scores[cat] += 3
        for phrase in WEAK.get(cat, []):
            if phrase in blob:
                scores[cat] += 1
    return scores


def classify(title: str, prompts) -> str:
    title_blob = (title or "").lower()
    body_blob = "\n".join(p.lower() for p in prompts if p)
    # title matches count double
    scores = Counter()
    ts = _score_blob(title_blob)
    bs = _score_blob(body_blob)
    for cat in CATEGORIES:
        scores[cat] = ts[cat] * 2 + bs[cat]
    # no signal -> GENERAL
    non_general = {c: s for c, s in scores.items() if c != "GENERAL" and s > 0}
    if not non_general:
        return "GENERAL"
    best = max(non_general.items(), key=lambda kv: kv[1])
    top_score = best[1]
    top = [c for c, s in non_general.items() if s == top_score]
    priority = ["DEBUG", "SEO", "DESIGN", "REVIEW AND IMPROVE", "MARKETING", "BUILD"]
    order = {c: i for i, c in enumerate(priority)}
    top.sort(key=lambda c: order.get(c, 99))
    return top[0]


def derive_title(prompt: str) -> str:
    """A short navigable title drawn from the user's own words."""
    clean = re.sub(r"\s+", " ", prompt.strip())
    words = clean.split(" ")
    if len(words) <= 12:
        return clean[:100]
    head = " ".join(words[:12])
    body = re.split(r"[.!?]", head)[0].strip()
    return (body or head)[:100]


def slugify(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.strip()).strip("-").lower()
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:70] or "untitled"


def write_thread(category, prompts, used_names):
    prompts = [p.strip() for p in prompts if p and p.strip()]
    if not prompts:
        return None
    base = slugify(derive_title(prompts[0]))
    count = used_names.get((category, base), 0)
    used_names[(category, base)] = count + 1
    if count:
        base = f"{base}-{count + 1}"
    dpath = os.path.join(ROOT, category)
    os.makedirs(dpath, exist_ok=True)
    fpath = os.path.join(dpath, base + ".md")

    lines = [f"# {derive_title(prompts[0])}", ""]
    for i, p in enumerate(prompts):
        if i:
            lines += ["", "---", ""]
        lines.append(p)
    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines).rstrip() + "\n")
    return (category, base + ".md", len(prompts))


def iter_claude():
    for fn in ["conversations.json", "conversations1.json", "conversations3.json",
               "conversations4.json", "conversations5.json"]:
        path = os.path.join(RAW, fn)
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("conversations", [])
        for conv in data:
            prompts = [m.get("text", "").strip()
                       for m in conv.get("chat_messages", [])
                       if (m.get("sender") or "").lower() == "human"
                       and (m.get("text") or "").strip()]
            if prompts:
                yield conv.get("name") or "", prompts, "Claude", fn


def iter_templates():
    files = [
        "019bf0f8-d6f6-7282-9465-4f3b2ea93d7a.json",
        "019c03c0-4c5e-7284-9be2-6852f20cdba2.json",
        "019c03c6-ee6a-77be-9f0d-8c5cc15deb85.json",
        "019c57ef-a827-770c-9d14-10bc622e4619.json",
        "019c7712-03e8-706b-a1c2-9ac2ce32a1ef.json",
    ]
    for fn in files:
        path = os.path.join(RAW, fn)
        if not os.path.exists(path):
            continue
        d = json.load(open(path, encoding="utf-8"))
        name = d.get("name") or ""
        parts = [(d.get("prompt_template") or "").strip()]
        for doc in d.get("docs", []) or []:
            if isinstance(doc, dict) and doc.get("content"):
                parts.append(doc["content"].strip())
        body = "\n\n".join(p for p in parts if p)
        if body:
            prompts = [body]
        elif name:
            prompts = [name]
        else:
            continue
        yield name, prompts, "Claude Project Template", fn


def iter_grok():
    path = os.path.join(RAW, "prod-grok-backend.json")
    if not os.path.exists(path):
        return
    g = json.load(open(path, encoding="utf-8"))
    for c in g.get("conversations", []):
        conv = c.get("conversation", {})
        prompts = [r.get("response", {}).get("message", "").strip()
                   for r in c.get("responses", [])
                   if (r.get("response", {}).get("sender") or "").lower() == "human"
                   and (r.get("response", {}).get("message") or "").strip()]
        if prompts:
            yield conv.get("title") or "", prompts, "Grok", "prod-grok-backend.json"
    for m in g.get("media_posts", []):
        p = (m.get("original_prompt") or "").strip()
        if p:
            yield "", [p], "Grok (media)", "prod-grok-backend.json"
    for t in g.get("tasks", []):
        task = t.get("task", {})
        p = (task.get("prompt") or "").strip()
        if p:
            yield task.get("name") or "", [p], "Grok (task)", "prod-grok-backend.json"


def iter_chatgpt():
    path = os.path.join(RAW, "conversations-20260820_120758-1e472968.json")
    if not os.path.exists(path):
        return
    cg = json.load(open(path, encoding="utf-8"))
    for c in cg.get("conversations", []):
        prompts = [e.get("query", "").strip() for e in c.get("entries", [])
                   if (e.get("query") or "").strip()]
        if prompts:
            yield c.get("context_title") or "", prompts, c.get("mode") or "ChatGPT", \
                "conversations-20260820_120758-1e472968.json"


def main():
    used_names = {}
    stats = Counter()
    manifest = []

    for title, prompts, provider, source in list(iter_claude()) + list(iter_templates()) \
            + list(iter_grok()) + list(iter_chatgpt()):
        # media posts are always design
        if provider == "Grok (media)":
            cat = "DESIGN"
        else:
            cat = classify(title, prompts)
        res = write_thread(cat, prompts, used_names)
        if res:
            stats[cat] += 1
            manifest.append({
                "category": cat, "file": res[1], "prompts": res[2],
                "title": derive_title(prompts[0]), "provider": provider, "source": source,
            })

    print("=== SORTED OUTPUT ===")
    for c in CATEGORIES:
        print(f"  {c}: {stats[c]}")
    print(f"  TOTAL: {sum(stats.values())} threads")


if __name__ == "__main__":
    main()