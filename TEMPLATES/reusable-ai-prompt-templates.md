# Reusable AI Prompt Templates

This document contains standardized, production-ready prompt templates designed to
maintain consistent data sorting and structure across projects and clients. Replace
the bracketed variables (e.g., `[CLIENT_NAME]`) with your specific project details
before execution.

## 1. Content & Copywriting Strategy Template

**Sorting Rule:** Group outputs strictly by content pillar and intent stage (Top,
Middle, Bottom of Funnel).

- **Role:** Direct-Response Copywriter & Content Strategist
- **Context:** You are generating marketing copy for `[CLIENT_NAME]` in the
  `[INDUSTRY/NICHE]` industry.
- **Input Data:**
  - Target Audience: `[TARGET_AUDIENCE]`
  - Core Value Proposition: `[VALUE_PROPOSITION]`
  - Content Pillars: `[CONTENT_PILLAR_LIST]`
  - Primary Goal: `[PROJECT_GOAL]` (e.g., Lead Generation, Brand Awareness,
    Conversions)
- **Instructions:**
  1. Take `[RAW_TOPIC_IDEAS]` and assign each item to its corresponding content
     pillar from `[CONTENT_PILLAR_LIST]`.
  2. For each sorted pillar, generate `[NUMBER]` distinct `[CONTENT_TYPE]` concepts.
  3. Sort final recommendations by conversion priority (High Intent to Low Intent).
  4. Maintain a `[TONE_OF_VOICE]` tone throughout and include a clear CTA pointing to
     `[CTA_DESTINATION]`.
- **Output Format:** Provide the results in a structured table.

| Pillar Category | Intent Stage | Headline | Core Message / Body Copy | CTA |
| --- | --- | --- | --- | --- |
| `[Pillar Name]` | `[ToFU / MoFU / BoFU]` | `[Headline Copy]` | `[Body Copy]` | `[Call to Action]` |

## 2. Technical SEO & Asset Map Template

**Sorting Rule:** Organize site architecture and metadata strictly by URL hierarchy and
search intent clusters.

- **Role:** Technical SEO Strategist
- **Context:** You need to optimize content for `[CLIENT_NAME]` to rank for specific
  search intent clusters.
- **Input Data:**
  - Primary Keyword Cluster: `[PRIMARY_KEYWORD_CLUSTER]`
  - Secondary Keywords: `[SECONDARY_KEYWORDS_LIST]`
  - Page Types List: `[PAGE_TYPES_LIST]` (e.g., Blog Post, Service Page, Product
    Description)
- **Instructions:**
  1. Analyze `[RAW_KEYWORD_DATA]` and sort keywords into primary clusters based on
     search intent (Informational, Commercial, Transactional).
  2. Assign each sorted cluster to its designated page type from `[PAGE_TYPES_LIST]`.
  3. Generate `[NUMBER]` optimized Meta Titles (under 60 characters) and Meta
     Descriptions (under 155 characters).
  4. Outline an H2/H3 header structure incorporating the secondary keywords naturally.
  5. List 3–5 internal linking opportunity concepts related to `[TOPIC_AREA]`.
- **Output Format:** Organize using clean heading hierarchy per intent cluster.

| Intent Cluster | Page Type | Meta Title & Description | Heading Outline (H2/H3) |
| --- | --- | --- | --- |
| `[Search Intent Cluster]` | `[Page Type]` | `[Meta Copy]` | `[H2/H3 Outline]` |

## 3. Data Analysis & Action Matrix Template

**Sorting Rule:** Group findings strictly by performance metric category, priority level,
and operational impact.

- **Role:** Lead Data Analyst
- **Context:** You are analyzing raw export data for `[PROJECT_NAME]`.
- **Input Data:**
  - Raw Data Input: `[UNSORTED_METRIC_DATA]`
  - Metric Categories: `[METRIC_CATEGORIES]` (e.g., Acquisition, Retention, Revenue)
  - Key Metrics Focus: `[METRICS_LIST]`
- **Instructions:**
  1. Process `[UNSORTED_METRIC_DATA]` and organize entries by `[METRIC_CATEGORIES]`.
  2. Sort identified issues within each category by urgency/priority: High, Medium, Low.
  3. Provide 1 actionable strategic recommendation per sorted data group.
- **Output Format:**
  - Executive Summary: Concise 2-sentence overview.
  - Sorted Action Matrix Table containing Category, Priority, Finding, Impact, and
    Action Step.

| Metric Category | Priority Level | Data Finding | Impact Analysis | Action Step |
| --- | --- | --- | --- | --- |
| `[Category Name]` | `[High / Medium / Low]` | `[Metric Finding]` | `[Impact Details]` | `[Recommended Action]` |