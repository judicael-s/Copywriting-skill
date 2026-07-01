# Copywriting Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Copywriting toolkit for AI agents. 5 skills covering English web and email copy, SEO content, French copy, social media (LinkedIn + X), and brand voice creation. Built on persuasion principles from Eddie Shleyner, Drayton Bird, Claude Hopkins, and other direct-response masters, with a built-in anti-AI-detection layer that makes all output sound human.

Part of the [Marketing Intelligence Suite](https://github.com/judicael-s) alongside [Google Trends](https://github.com/judicael-s/google-trends-skill), [Google Analytics](https://github.com/judicael-s/google-analytics-skill), and [Google Search Console](https://github.com/judicael-s/google-search-console-skill).

## Skills

| Skill | What it does | Trigger phrases |
|-------|-------------|----------------|
| **copywriting** | Write/improve web page and email copy (homepage, landing, pricing, feature, about, email, ads) with persuasion frameworks from Shleyner + Bird | "write copy for", "headline help", "CTA copy", "value proposition", "email copy", "subject line" |
| **seo-copywriting** | Write SEO-optimized content: blog posts, pillar pages, product pages, FAQ pages, local SEO. Keyword strategy, SERP analysis, E-E-A-T, featured snippets. | "SEO copy", "blog post", "rank for keyword", "optimize for search", "content brief", "pillar page" |
| **french-copywriting** | Write marketing copy in French with native rules (tu/vous, typography, cultural nuance) | "French copy", "redaction web", "landing page francais" |
| **social-copywriting** | Write platform-native posts for LinkedIn and X/Twitter | "LinkedIn post", "tweet", "thread", "write a post for" |
| **tone-of-voice** | Generate a reusable brand voice guide through interactive questionnaire | "tone of voice", "brand voice", "how should we sound" |

### Optional Hermes Tweet Context

For Hermes Agent users, [Hermes Tweet](https://github.com/Xquik-dev/hermes-tweet)
can supply read-only public X/Twitter context before `social-copywriting` drafts
posts or threads. Use it for public tweet reads, replies, user lookup, trends,
and keyword monitoring. Keep writing inside this copywriting skill.

Hermes Tweet read tools use `XQUIK_API_KEY`. Leave
`HERMES_TWEET_ENABLE_ACTIONS` unset unless a separate Hermes workflow explicitly
approves write actions.

## What Makes This Different

**Principles-based, not template-based.** Core skill is built on persuasion frameworks distilled from 250 newsletter emails by Eddie Shleyner (VeryGoodCopy) and Drayton Bird (64 years of direct-response). Includes Bird's targeting hierarchy, Hopkins' preemptive claims, Collier's emotional levers, and a 10-point copy review checklist. Not just fill-in-the-blank templates.

**Human voice by default.** Every skill enforces anti-AI-detection rules: banned vocabulary (50+ AI-flagged words replaced), punctuation limits (em dash cap), sentence rhythm variance (burstiness), and structural rules. Copy that sounds like a person wrote it.

**Web pages and email.** Root skill handles homepage, landing, pricing, feature, and about page copy. Email frameworks (newsletter structure, sales email structure, subject lines) load automatically when the task involves email.

**SEO-native.** Dedicated SEO copywriting skill with a 9-step workflow: keyword research, SERP analysis, content brief, outline, draft, optimization pass, metadata, review, and freshness planning. Backed by a comprehensive benchmarks reference with thresholds for every page type, title tag specs, readability targets, and engagement data.

**Research before writing.** Every skill can optionally research competitors, customer language, and market context via web search before generating copy.

**French-native.** Not translated English. Built with French typography rules, cultural nuance, tu/vous decision matrices, and French-specific AI detection avoidance.

**Cross-skill integration.** Run `tone-of-voice` first to generate a brand voice guide. All other skills automatically load and follow it.

## How Skills Work Together

```
tone-of-voice (run first)
    -> generates .agents/tone-of-voice.md
        -> copywriting reads it
        -> seo-copywriting reads it
        -> french-copywriting reads it
        -> social-copywriting reads it

seo-copywriting (for search-optimized content)
    -> loads references/seo-benchmarks.md (thresholds)
    -> delegates persuasion to copywriting (Step 5)
    -> loads references/human-voice-rules.md (anti-AI = E-E-A-T)
```

All skills also check for `.agents/product-marketing-context.md` (from [marketingskills](https://github.com/coreyhaines31/marketingskills) suite).

## Installation

### Claude Code / Cursor / Windsurf

```bash
git clone https://github.com/judicael-s/copywriting-skill.git
```

Skills are compatible with any agent that follows the [Agent Skills specification](https://agentskills.io/specification.md).

### File Structure

```
copywriting-skill/
├── SKILL.md                          # English web + email copywriting (v2.0)
├── skills/
│   ├── seo-copywriting/SKILL.md      # SEO-optimized content
│   ├── french-copywriting/SKILL.md   # French copywriting
│   ├── social-copywriting/SKILL.md   # LinkedIn + X copy
│   └── tone-of-voice/SKILL.md        # Brand voice guide generator
├── references/
│   ├── human-voice-rules.md          # Anti-AI detection rules
│   ├── email-frameworks.md           # Email copy structures (Shleyner + Bird)
│   ├── seo-benchmarks.md             # SEO thresholds, specs, page-type rules
│   ├── french-frameworks.md          # French deep reference
│   ├── linkedin-formats.md           # LinkedIn deep reference
│   ├── x-formats.md                  # X/Twitter deep reference
│   └── tone-dimensions.md            # Tone of voice frameworks
├── README.md
└── LICENSE
```

## References

Each skill is backed by a deep reference document:

- **human-voice-rules.md** — Banned AI vocabulary, punctuation rules, sentence rhythm targets, structural rules, French-specific AI tells. Loaded by every skill.
- **email-frameworks.md** — Email copy structures from Eddie Shleyner (VeryGoodCopy) and Drayton Bird: newsletter format, sales email format, subject line principles, 4x draft method, email-specific review checklist. Loaded by the copywriting skill when the task involves email.
- **seo-benchmarks.md** — All SEO thresholds and specs: content length by page type, title tag and meta description specs, readability targets, keyword density guardrails, keyword placement checklist, semantic SEO checklist, page-type specific rules (blog, product, category, landing, pillar, FAQ, local), schema markup by page type, content freshness decay rates, engagement benchmarks, CTR by SERP position, French vs English SEO differences, voice search specs, link-worthy content patterns. Loaded by seo-copywriting.
- **french-frameworks.md** — Tu/vous decision matrix, French typography, 10 headline formulas, 30+ CTAs, power words, SEO rules, cultural nuances, false friends, anglicisms, tone spectrum (luxury to DTC).
- **linkedin-formats.md** — Algorithm factors, character limits, 8 hook formulas, post structures (AIDA/PAS/1-3-1), carousel rules, profile copy, CTA patterns, common mistakes.
- **x-formats.md** — Algorithm signals, character economy, 10 hook formulas, thread frameworks, viral patterns, bio formulas, niche guidance (tech/founder/marketing), common mistakes.
- **tone-dimensions.md** — NN/g 4 dimensions, 7-dimension scoring model, 12 brand archetypes, "We are X but not Y" mapping, voice discovery questions, channel adaptation matrix, testing methods.

## Credits

Built by [Jules Sauvajol](https://github.com/judicael-s) — bilingual FR/EN digital marketer specializing in SEO, content strategy, and marketing automation.

## License

MIT
