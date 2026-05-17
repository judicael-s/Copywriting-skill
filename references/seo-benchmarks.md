# SEO Benchmarks Reference

Loaded by the seo-copywriting skill. Contains all thresholds, specs, and page-type rules. Data sourced from Ahrefs, Backlinko, Moz, SEMrush, Surfer SEO, Clearscope, Google Search Central, Zyppy, and other authoritative sources (2025-2026).

---

## Content Length by Page Type

| Page Type | Word Count | Notes |
|---|---|---|
| Blog post (standard) | 1,500-2,000 | Positions 1-3 average 2,100-2,500 |
| Blog post (competitive) | 2,000-2,500 | Benchmark against top 5 SERPs |
| Landing page (lead gen) | 300-600 | Conversion-focused, minimal friction |
| Landing page (SaaS/feature) | 600-1,200 | More room for benefits and proof |
| Product page | 200-500 | Tight descriptions, specs, social proof |
| Category page | 150-300 intro | Above product grid, expanded below |
| Pillar page | 3,000-5,000+ | Traffic and shares improve up to 7,000+ |
| FAQ page | 2,000-3,500 | Covers multiple sub-questions |
| Local SEO page | 500-1,000 | Per location, with unique local content |

**Critical rule:** Length is a benchmark, not a target. 800-word posts outrank 3,000-word posts when the shorter piece fully addresses intent. Always check top 3-5 results for your specific keyword.

---

## Title Tag Specs

| Parameter | Value |
|---|---|
| Optimal length | 51-60 characters (Google uses ~600px width) |
| Keyword placement | Front-load in first 5 words |
| Separators | Dashes preferred (19.7% removal rate) over pipes (41% removal rate) |
| Brackets vs parentheses | Parentheses preferred (19.7% removal rate) over brackets (32.9%) |
| Year marker | Include current year for dated queries (+20-30% CTR) |
| Google rewrite rate | ~76% of titles get rewritten; at 51-60 chars only 39-42% |
| Uniqueness | Every page must have a unique title |
| Brand suffix | Strip `| Brand` style suffixes from title tag. Wastes 12-15c of SERP-visible width on a signal users already get from the favicon and domain row. |

## H1 Specs

| Parameter | Value |
|---|---|
| Optimal length | ≤70 characters |
| Why distinct from title tag | H1 displays in browser tabs, CMS admin lists, social cards, breadcrumbs — anywhere over 70c truncates. Title tag has its own SERP-pixel cap (51-60c). |
| Uniqueness | One H1 per page; never duplicated across pages |
| Keyword placement | Primary keyword required (matches title tag) |

**Power words that lift CTR 20-30%:**
- Exclusivity: Proven, Ultimate, Definitive, Battle-Tested
- Simplicity: Simple, Easy, Quick, Step-by-Step, Beginner's Guide
- Thoroughness: Complete, Comprehensive, Deep Dive, A to Z
- Urgency: Now, Today, [Year] Update, New

---

## Meta Description Specs

| Parameter | Value |
|---|---|
| Optimal length | 140-160 characters (~920px on desktop) |
| Primary keyword | Include once, naturally |
| Content | 1-2 sentence summary matching searcher intent + reason to click |
| Don't | Duplicate title wording, stuff keywords |
| Google override rate | 60-70% of snippets are auto-generated from page content |
| Impact | Optimized descriptions see 20-30% CTR improvement over missing ones |

---

## Readability Targets

| Parameter | Target |
|---|---|
| Flesch Reading Ease | 60-70 (general audience) |
| Flesch-Kincaid Grade Level | 7-8 (general), 10-12 (B2B/technical) |
| Average sentence length | Under 20 words |
| Paragraph length | 2-4 sentences, max 120 words |
| Single-sentence paragraphs | Fine for emphasis |

**Evidence:** Content scoring 60-70 Flesch generates 30% more leads. Shortening average sentence length from 25 to 15 words: bounce rate dropped, time-on-page jumped to 3:45, organic traffic grew 34%.

---

## Keyword Density Guardrails

| Parameter | Value |
|---|---|
| Primary keyword density | 0.5-1.5% (sweet spot 1-1.5%) |
| Absolute ceiling | 2.5% (above = stuffing risk) |
| Primary keyword occurrences | 3-5 in body: intro, 1-2x in body, conclusion |
| Overoptimization signal | Above 3% triggers stuffing detection |

**Keyword density is a guardrail, not an optimization lever.** A study of 1,500+ results found no consistent correlation between density and ranking. Focus on semantic coverage instead.

---

## Keyword Placement Checklist

| Location | Rule |
|---|---|
| Title tag | Primary keyword in first 5 words |
| H1 | Must contain primary keyword. One H1 per page. |
| H2/H3 | Secondary and long-tail keywords in at least 2-3 H2s |
| First 100 words | Primary keyword naturally in introduction |
| Last 100 words | Reinforce primary keyword in conclusion |
| Meta description | Primary keyword once |
| URL slug | Primary keyword, short, hyphenated |
| Image alt text | Descriptive, primary keyword on main image |

---

## Semantic SEO Checklist

- [ ] 8-15 semantically related terms identified from SERP analysis
- [ ] All related terms covered naturally in the content (not forced)
- [ ] Core entities and their relationships described accurately
- [ ] Topic covered comprehensively — passes "would a subject expert add anything?" test
- [ ] Synonyms and variations used naturally (no synonym cycling)
- [ ] PAA questions addressed within the content
- [ ] Content structured for topic cluster (links to pillar and related cluster pages)

**Key stat:** Topic-cluster sites achieve 38% more organic traffic than single-keyword structured sites (SEMrush). Semantic completeness has r=0.87 correlation with AI Overview selection.

---

## Page-Type Specific Rules

### Blog Posts / Articles

| Parameter | Threshold |
|---|---|
| H2 headings | Every 200-350 words |
| Internal links | 3-5 per 1,000 words |
| External links | 2-4 to authoritative sources |
| Images | 1 per 300-500 words |
| Table of contents | Required for posts over 1,500 words |
| Featured snippet block | Direct answer in first 40-60 words under target H2 |
| Schema | Article or BlogPosting |

### Product Pages

| Parameter | Threshold |
|---|---|
| H1 | Product name + primary modifier keyword |
| Sections | Benefits > Features > Specs > Social proof > FAQ |
| Schema | Product (price, availability, reviews, SKU) |
| CTA | Above the fold, repeated after key sections |
| Unique content | Required per product (no manufacturer copy) |

### Category Pages

| Parameter | Threshold |
|---|---|
| Intro copy | 150-300 words above product grid |
| Expanded copy | Below grid for depth |
| Schema | CollectionPage, BreadcrumbList |
| Unique content | No boilerplate shared across categories |

### Landing Pages

| Parameter | Threshold |
|---|---|
| Above-fold | H1, value prop, primary CTA, hero image |
| CTA frequency | Every ~300 words (each scroll section) |
| Form fields | Minimize (each field reduces conversion ~7%) |
| Keyword density | 0.5-1% (enough for ranking, no stuffing) |
| Schema | WebPage, FAQPage if FAQ exists |
| Page speed | LCP under 2.5s is critical |

### Pillar Pages

| Parameter | Threshold |
|---|---|
| Cluster articles | 5-10 to start, expand over time |
| Structure | Table of contents, section summaries linking to clusters |
| Internal linking | Pillar links to every cluster; every cluster links back |
| Update frequency | Pillar refreshed quarterly; clusters as needed |
| Schema | Article, BreadcrumbList |

### FAQ Pages

| Parameter | Threshold |
|---|---|
| Questions per page | 5-15, focused on a single topic |
| Answer length | 50-250 words per answer |
| Question source | Real customer questions, PAA data, GSC queries |
| Schema | FAQPage JSON-LD (all Q&A visible on page) |
| Headings | Each question as its own H2/H3 |
| AI search impact | FAQPage markup = 3.2x more likely to appear in AI Overviews |

### Local SEO Pages

| Parameter | Threshold |
|---|---|
| H1 | Service + City/Area name |
| H2s | Local region in 2-3 headings |
| Unique content | Location-specific testimonials, landmarks, transit |
| Schema | LocalBusiness, GeoCoordinates, OpeningHours |
| NAP | Name, Address, Phone consistent across all pages |
| Voice search | Include "near me" and conversational question variants |

---

## Schema Markup by Page Type

| Page Type | Schema | Key Properties |
|---|---|---|
| Blog/Article | Article, BlogPosting | author, datePublished, dateModified, headline, image |
| Product | Product | name, price, availability, review, sku, brand |
| FAQ | FAQPage > Question > Answer | name (question), text (answer) |
| How-To | HowTo | step, name, text, image, totalTime |
| Local | LocalBusiness | name, address, telephone, openingHours, geo |
| Category | CollectionPage, BreadcrumbList | name, numberOfItems |
| Landing | WebPage | name, description |

Use JSON-LD format (Google's recommended). Keep markup separate from HTML content.

---

## Content Freshness Decay Rates

| Content Type | Decay Window | Refresh Cycle |
|---|---|---|
| Technology | 4-6 months | Every 3-6 months |
| Finance | 6-9 months | Every 6-9 months |
| Healthcare | 8-12 months | Every 8-12 months |
| Educational/Reference | 12-18 months | When facts change |
| Statistics/data posts | 12 months | Annually with new data |

Changing only the publication date produces no freshness benefit and can harm trust. Google evaluates actual content changes.

---

## Drop / Sunset Thresholds

Use these signals to decide when to deprecate or stop investing in a cluster/page:

| Signal | Threshold | Action |
|---|---|---|
| CTR floor (cluster) | <2% on >500 impressions per 180d | Drop candidate — keyword family isn't earning clicks even when shown |
| Impression floor (cluster) | 0 impressions per 180d | Drop candidate — no surfaceable demand at current ranking |
| Demographic targeting floor | <1000 sessions per 28d in GA4 | Don't pursue parent/age/gender segmentation — k-anonymity blocks reliable signal |
| Parent-intent caveat (GSC) | "Parent" / age-cohort regex queries returning 1 row per 180d | k-anonymity floor hides traffic; don't size a content investment off this signal alone |
| Conversion crater | ≥80 sessions per 28d / 0 purchases | Audit CTAs FIRST (not content) — usually a styling/placement/targeting bug |

These complement the **Tier-A / Tier-B / DROP** framework in the `seo-copywriting` skill's Post-Publish Audit Loop.

---

## Engagement Benchmarks

### CTR by SERP Position (2025-2026)

| Position | CTR (no AI Overview) | CTR (with AI Overview) |
|---|---|---|
| #1 | 35-40% | 15-20% |
| #2 | 12-18% | — |
| #3-5 | 5-10% | — |
| Positions 1-3 combined | 55-70% of all clicks | — |

- AI Overviews appear on ~31% of SERPs
- Sites cited in AI Overviews get 35% more clicks
- Position 1 CTR dropped 32% year-over-year due to AI Overviews

### Dwell Time

- 0.84 correlation with rankings (one of strongest behavioral signals)
- Pages with video average 6+ minutes vs 3 minutes without
- 73% of users leave within 10 seconds if content is hard to read

---

## French vs English SEO Differences

| Dimension | English | French |
|---|---|---|
| Text length | Baseline | 15-20% longer for same content |
| Long-tail keywords | Abundant, fragmented | Fewer variations, more formal queries |
| Content tone | Can be casual, direct | More formal register expected (FR-FR) |
| Title tags | Standard 51-60 chars | Same pixel limit, fewer words fit |
| Regional variants | US/UK spelling | FR-FR vs FR-CA vs FR-CH vocabulary |
| Keyword research | Standard tools | Same tools, but use .fr/.ca TLD, check regional volume |

**Never machine-translate.** Rewrite/localize. Separate keyword research per language. See `french-copywriting` skill for full French rules.

---

## Voice Search Specs

| Parameter | Value |
|---|---|
| Answer length | 29-40 words (voice assistants read ~29 from snippets) |
| Question targeting | Full questions as H2/H3 headings |
| Triggers | "how," "what," "where," "who," "when," "why," "can," "does," "is" |
| Local intent | 46% of voice searches have local intent |
| Page speed | Must load under 2.5s LCP |

---

## Link-Worthy Content Patterns

94% of published content earns zero backlinks (Ahrefs). Content with original data receives 5.2x more backlinks.

**Top linkable asset types:**
1. Original research / data studies (highest authority)
2. Statistics hubs / data roundups (most consistent)
3. Tools and calculators
4. Visual assets (infographics, charts)

**Copy patterns that earn links:**
- Lead with a specific, quotable finding in the first 200 words
- Include methodology (sample size, time period, data source)
- Format data for easy citation (tables, charts, labeled figures)
- Contrarian or surprising findings get shared and linked more

---

## Related References

- **`references/human-voice-rules.md`** — AI detection avoidance and readability serve the same goal. The burstiness rules (Section 3) complement the readability targets above. Both contribute to E-E-A-T "trustworthiness" signals.
- **`references/tone-dimensions.md`** — Authority dimension (score 4-5) is especially important for link-worthy content and E-E-A-T expertise signals.
- **`references/french-frameworks.md`** — For full French SEO guidance beyond the brief comparison table above, see Section 6 (SEO en français) in french-frameworks.md. Includes URL rules, meta description conventions, and keyword suffix patterns specific to French.
