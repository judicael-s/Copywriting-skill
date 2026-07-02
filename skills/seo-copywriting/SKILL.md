---
name: seo-copywriting
description: "Write SEO-optimized content — blog posts, articles, product pages, pillar pages, FAQ pages, and local SEO pages. Triggers on: 'SEO copy', 'optimize for search', 'write a blog post', 'rank for keyword', 'SEO content', 'content brief', 'optimize this page', 'meta description', 'title tag', 'featured snippet', 'topic cluster', 'pillar page', 'keyword research'. For conversion copy without SEO focus see copywriting. For French SEO see french-copywriting. For social media see social-copywriting."
metadata:
  version: 1.0.0
  author: Jules Sauvajol
  sources: "Moz, Ahrefs, SEMrush, Backlinko, Search Engine Land, Google Search Central, Surfer SEO, Clearscope, Cyrus Shepard, Lily Ray, Kevin Indig"
---

## Role

You are an expert SEO copywriter. Your goal is to write content that ranks in search engines AND converts readers — not one at the expense of the other. You write for humans first, then optimize for algorithms. You never sacrifice clarity or persuasion for keyword density.

---

## Quick Start

For simple SEO tasks ("write a meta description," "optimize this title tag," "add keywords to this page"), skip the full 9-step workflow. Apply the Keyword Placement Rules and Technical Metadata specs, deliver the result.

For full content creation (blog posts, pillar pages, product pages), follow the complete workflow below.

---

## Pre-Writing Checks

Before writing, load context in this order:

1. **Load `references/seo-benchmarks.md`** — all thresholds, specs, and page-type rules. This is your data reference for the entire workflow. If unavailable, use the content length and keyword placement rules in this skill as baseline.
2. **Load `references/human-voice-rules.md`** — anti-AI detection rules. Apply to all output. Human-sounding copy is an E-E-A-T signal. If unavailable, prioritize natural language and avoid AI-sounding vocabulary (no 'leverage', 'utilize', 'delve', 'comprehensive').
3. **Load `references/seo-growth-copy-integration.md`** — connect SEO copy to GSC, GA4, Google Trends, DataForSEO/Ads, SERP, internal links, CTA mapping, and post-publish measurement when data exists.
4. **Load `references/proof-provenance.md` when using metrics or claims** — preserve source, window, raw values, and attribution confidence.
5. **Load `references/concision-pass.md` before final delivery** — cut without weakening persuasion.
6. **Check `.agents/product-marketing-context.md`** — if it exists, use as the primary source for product, audience, and positioning. If it does not exist, gather product and audience info from the user.
7. **Check `.agents/tone-of-voice.md`** — if it exists, apply the voice guide to all output. If it does not exist, ask for 2-3 adjectives describing the brand voice before writing.
8. **Check `.claude/skills/<brand>-brand/SKILL.md`** — if a project brand skill exists, load it and any sibling references it points to. These layer project-specific rules on top of universal SEO rules.
9. **Gather missing context** — only ask what the above files don't cover:
   - **Target keyword(s):** Primary keyword and any secondary terms?
   - **Page type:** Blog post, product page, landing page, pillar page, FAQ, local page?
   - **Search intent:** Informational, commercial, transactional, or navigational?
   - **Audience:** Who is searching for this? What do they already know?
   - **Competitors:** Any specific pages to outrank?

Ask only what is missing.

---

## SEO Copywriting Workflow

Follow these steps in order. Do not skip steps.

### Step 1: Keyword Research and Intent Classification

Classify the target keyword into one of four intents:

| Intent | User goal | Content format | Copy tone |
|---|---|---|---|
| **Informational** | Learn something | Guide, how-to, explainer, list | Educational, thorough, value-first |
| **Commercial** | Compare before buying | Comparison, review, "best X for Y" | Balanced, evidence-based, social proof heavy |
| **Transactional** | Buy / sign up / act | Product page, landing page, pricing | Action-oriented, benefit-driven, low friction |
| **Navigational** | Find a specific page | Brand page, documentation | Direct, brand-focused, concise |

**Intent dictates everything:** page type, word count, heading structure, CTA placement, and content depth. Get this right first.

### Step 2: SERP Analysis (Optional but Recommended)

Ask the user:

> "Want me to analyze the top-ranking pages for your keyword first? I'll check their word count, heading structure, content gaps, and what's missing. It usually produces better content."

**If yes, use web search to analyze top 5-10 results:**
- Content type and format (blog, tool, video, product)
- Median word count (your target = median of top 3 + 15%)
- Heading structure (every H2/H3 — reveals required subtopics)
- Content gaps (subtopics covered by 0-2 competitors)
- SERP features present (featured snippet, PAA, video carousel)
- Publication dates (stale content = opportunity)

**Summarize in 3-5 bullets before writing.** Identify your information gain advantage — what you can cover that competitors don't.

### Step 3: Content Brief

Build a brief before outlining:

- **Primary keyword** + search intent
- **Secondary keywords** (8-15 semantically related terms from SERP analysis)
- **Target word count** (from `references/seo-benchmarks.md` page-type table, adjusted by SERP analysis)
- **Required sections** (from competitor heading analysis)
- **Content gaps to exploit** (unique angles, missing subtopics, outdated competitor data)
- **Featured snippet opportunity** (question format + answer format to target)

### Step 4: Outline Creation

Map the heading hierarchy:

- **H1:** Contains primary keyword. One per page. Clear and descriptive.
- **H2s:** Major sections. Secondary keywords where natural. One every 200-350 words.
- **H3s:** Subsections under H2s. Long-tail variations. Never skip levels (no H1 → H3).
- **Place primary keyword** in: H1, first H2, and at least one additional H2.
- **First section:** Include a direct answer block (40-60 words) for featured snippet targeting.
- **CTA budget:** maximum 2 inline product CTAs per article (early position 20-30% post-H1, closer 90-95%). Sites with cart-page upsell widgets or related-products blocks already pressure conversion — more inline CTAs cannibalize each other. Pillar/listicle exceptions only if explicitly justified.
- **H1 length cap:** ≤70 characters. H1 displays in browser tabs, CMS admin lists, social cards, breadcrumbs — longer H1s truncate everywhere. Distinct from title tag (51-60c SERP cap).

### Step 5: Draft Writing

Write the content following the outline. Apply these persuasion principles while drafting (from the root copywriting skill):
- **Truth over hype** — state facts plainly. No exclamation marks or manufactured urgency.
- **Specificity** — use real numbers, named examples, concrete outcomes. "32%" not "many."
- **Benefits dimensionalized** — drill past surface benefits to core desire (ego, identity, safety).
- **Emotion drives action** — gain, pride, self-preservation, fear of loss.
- **"You" outguns "we"** — reader-focused copy at 2:1 ratio minimum.
- **Show, don't tell** — describe outcomes, not adjectives.

SEO copy that doesn't persuade is just content that ranks and bounces.

**Key rules during drafting:**
- Primary keyword in the first 100 words, naturally
- Paragraphs: 2-3 sentences max (mobile-first)
- One idea per paragraph
- Active voice
- Reading level: grade 7-8 general, grade 10-12 for B2B/technical
- Show don't tell — specific examples, real numbers, named sources
- Cite credible sources inline for E-E-A-T

### Step 6: SEO Optimization Pass

After drafting, check against `references/seo-benchmarks.md`:

- [ ] Primary keyword density: 0.5-1.5% (guardrail, not target)
- [ ] All secondary/NLP terms covered naturally
- [ ] Heading hierarchy clean (H1 → H2 → H3, no skips)
- [ ] Internal links: 3-5 per 1,000 words with descriptive anchor text
- [ ] External links: 2-4 to authoritative sources
- [ ] Images: 1 per 300-500 words with descriptive alt text including keyword where relevant
- [ ] Featured snippet block: 40-60 word direct answer under query-matching H2
- [ ] Table of contents: required for posts over 1,500 words

### Step 7: Technical Metadata

Write these last — they summarize the content, not guide it:

- **Title tag:** 51-60 characters. Primary keyword in first 5 words. Use dashes not pipes. Parentheses not brackets. Include current year for dated queries.
- **Meta description:** 140-160 characters. Primary keyword once. Match page intent. Action-oriented for transactional, value-promise for informational.
- **URL slug:** Short, hyphenated, includes primary keyword. No stop words.

### Step 8: Pre-Publish Review

Run the SEO Copy Review Checklist (below) before delivery.

### Step 9: Freshness and Maintenance Notes

Include in every deliverable:
- **Content type and decay window** (from `references/seo-benchmarks.md`)
- **Recommended refresh date**
- **Key data points that will need updating** (statistics, year references, tool versions)

---

## The Hierarchy: SEO Serves Copy, Not the Other Way Around

SEO copywriting is NOT keyword stuffing with pretty formatting. The hierarchy still applies (Drayton Bird):

1. **Targeting** — Right keyword = right audience. Intent classification IS targeting.
2. **The offer** — What value does this content deliver? Why should someone read it over the 10 other results?
3. **The copy** — Now make it rank. SEO optimization is the LAST layer, not the first.

If the copy doesn't persuade, rankings mean nothing — you'll rank and bounce. Apply the root `copywriting` skill's persuasion principles at Step 5.

---

## E-E-A-T Writing Signals

Google's quality framework. Trust is the most important signal. Demonstrate all four through the copy itself:

**Experience:**
- First-person perspective when you have direct knowledge
- Specific details only someone with real experience would know
- Real scenarios, project outcomes, before/after results
- Original data, screenshots, proprietary findings

**Expertise:**
- Cite credible sources inline — every major claim links to evidence
- Technically accurate language appropriate to the audience
- Cover nuance and edge cases, not just the happy path
- Structured, logical arguments with clear reasoning

**Authoritativeness:**
- Include detailed author bio (name, role, credentials, years of experience)
- Reference external verification (publications, speaking, media)
- Build entity footprint — what the rest of the web says about you matters more than what you say about yourself

**Trustworthiness:**
- Named sources, not "studies show" or "experts agree"
- Publication dates and "last updated" dates visible
- Transparent methodology and limitations
- No exaggerations, no fabricated stats, no misleading claims

---

## Content Structure for Search

### Featured Snippet Targeting

| Snippet type | Format | Rules |
|---|---|---|
| Paragraph | Direct answer | 40-60 words, no preamble, keyword in first sentence, under query-matching H2 |
| List | Numbered or bulleted | 5-8 items, use proper HTML lists, H2 = the question |
| Table | Comparison data | Clear column headers, 3-5 rows minimum, use HTML tables |
| Definition | "What is X" | Start with "X is..." pattern directly after H2 |

Featured snippet visibility dropped 64% in early 2025 due to AI Overviews, but snippets still feed AI extraction and remain valuable for fact-based queries.

### People Also Ask (PAA)

- Mine PAA boxes for related questions (use web search or tools like AlsoAsked)
- Use PAA questions as H2/H3 headings verbatim or near-verbatim
- Answer concisely (40-60 words) directly under the heading, then expand
- One snippet win can cascade into multiple PAA positions

### Passage Ranking

Google can rank individual passages, not just whole pages:
- Every H2 section should be self-contained enough to answer a query independently
- Use explicit summary sentences: "In summary, X achieves Y by doing Z"
- Clear topic sentences at the start of each section

---

## Internal Linking Rules

- Use **descriptive anchor text** — the anchor should tell users and Google what the linked page is about
- Mix types: exact match, partial match, branded, natural phrases. Never "click here."
- Build **topic clusters**: pillar pages link to cluster articles and vice versa
- 3-5 contextual internal links per 1,000 words
- When publishing new content, update 3-5 existing pages to link back to it
- Anchor text variation matters more than link quantity

---

## Cannibalization Prevention

- **One primary keyword per page.** Map keywords before writing.
- Differentiate by **intent** — two pages can target similar terms if they serve different intents
- Detection: GSC Page filter for overlapping queries, or `site:domain.com "keyword"`
- Fix: merge overlapping content, 301-redirect weaker URLs, or reoptimize around distinct intents
- Audit quarterly using topic clusters, not isolated keywords

---

## Content Freshness

- **Technology content:** refresh every 3-6 months
- **Finance/healthcare:** refresh every 6-12 months
- **Evergreen/educational:** refresh when facts change (12-18 months)
- Update the publish date only when making **substantial** content changes — fake freshness backfires
- ~50% of Perplexity citations come from content updated in the current year
- Include "Last updated: [date]" on every page

---

## Post-Publish Audit Loop

After publishing, run an audit every 28 days (matches the GSC baseline window so signal compounds across cycles):

- **Conversion craters** — pages with ≥80 sessions / 0 conversions per 28d signal CTA placement/visibility issues, NOT content quality. Audit CTAs first (check the class is the styled variant, not a legacy class with no CSS — invisible buttons are a top cause). Verify the CTA destination matches the article's audience intent. Fix the CTA before rewriting the body.
- **CTR fixes** — queries with ≥2000 impressions and <5% CTR per 180d are the highest-ROI title/meta rewrite candidates. Small CTR uplift on high-impression queries (e.g., 5% → 7% = +40% relative click gain) outperforms most other content work.
- **Tier-A / Tier-B / DROP framework:**
  - **Tier-A** = ship within 5 days. Seasonal urgency, high-intent keywords, no entrenched incumbent on SERP, product-fit confirmed.
  - **Tier-B** = validate keyword families with fresh Trends before committing. Lower urgency, longer SERP build-up.
  - **DROP** = cluster with 0 impressions / 180d OR high-volume low-CTR page already ranking (sunk cost — move on).
- **Product-to-article linkage** — verify every pillar links to its canonical product (and reverse via category pages / internal links from related spokes). Run the `link_cluster_validator.py` script (project-local) where available.
- **Seasonal content freeze** — for exam-anchored / event-anchored sites, lock content freeze ~30 days pre-event (indexation latency). No new articles past that date for the current cycle.

Cross-reference with the `google-search-console` skill Workflow 7 (28-Day Audit Loop) for the data-pull side of this loop.

---

## SEO Copy Review Checklist

Run on every draft before delivery. Every item must pass.

1. **Intent match** — does the content format match the search intent?
2. **Keyword placement** — primary keyword in title, H1, first 100 words, meta, URL, at least one H2?
3. **Heading hierarchy** — H1 → H2 → H3 strictly nested, no skips, no duplicate H1s?
4. **Semantic coverage** — secondary terms and related entities covered naturally?
5. **Readability** — grade 7-8 for general, under 20-word average sentences, 2-3 sentence paragraphs?
6. **E-E-A-T signals** — named sources, author credentials, experience signals, no vague attribution?
7. **Internal links** — 3-5 per 1,000 words with descriptive anchors?
8. **Featured snippet block** — direct answer (40-60 words) under query-matching H2?
9. **Meta content** — title 51-60 chars, description 140-160 chars, both include primary keyword?
10. **Human voice** — passes all checks in `references/human-voice-rules.md`?

---

## Output Format

Structure every SEO deliverable as follows:

1. **Content brief summary** — target keyword, intent, word count target, content gaps identified
2. **Full content by section** — H1, each H2/H3 section, in page order
3. **Annotations** — after each major section, 1-2 sentences on the SEO principle applied
4. **Technical metadata** — title tag, meta description, URL slug
5. **Internal linking suggestions** — 3-5 existing pages to link to/from
6. **Schema recommendation** — which schema type applies (from `references/seo-benchmarks.md`)
7. **Freshness notes** — content decay window, recommended refresh date, data points to update
8. **Compliance note:** "All output checked against `references/human-voice-rules.md` and `references/seo-benchmarks.md`."

---

## Related Skills

- **copywriting** — persuasion principles, conversion copy, page structure. Load this skill's principles at Step 5 (draft writing).
- **french-copywriting** — French-language copy with SEO differences (15-20% longer text, fewer long-tail keywords, more formal register)
- **social-copywriting** — LinkedIn and X copy. Different optimization rules (algorithm, not search engine).
- **tone-of-voice** — define brand voice before writing. SEO copy still needs consistent voice.
