# Copywriting Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A free copywriting skill library for AI agents.

It helps agents write copy that sounds human and sells clearly.

Not louder.
Not more polished.
More specific.
More believable.
More useful to the reader.

It works with Hermes, Open Claw Agent, Claude Code, Codex, Cursor, Windsurf, Cline, and any agent that can follow markdown workflows.

## What it does

This library gives agents practical workflows for:

- web and landing page copy
- email and outreach
- SEO content
- French copywriting
- LinkedIn and X posts
- tone of voice
- CVs, cover letters, and LinkedIn profiles
- copy critique before rewrite
- proof-backed claims
- human voice editing

## The idea

Most AI copy has the same problem.

It sounds finished before it says anything true.

This skill pushes the agent to do the harder work first:

1. know the reader
2. clarify the offer
3. find the proof
4. choose the hook
5. write simply
6. cut what does not earn its place
7. end with a line that lands

## Skills

| Skill | What it does | Use when |
|---|---|---|
| `copywriting` | Web, landing page, email, CTA, headline, value proposition, sales copy | You need conversion copy |
| `seo-copywriting` | SEO briefs, articles, product pages, pillar pages, metadata, refresh planning | You need search content that still converts |
| `french-copywriting` | Native French copy with French typography, tu/vous, cultural nuance | You need French marketing text |
| `social-copywriting` | LinkedIn posts, X posts, threads, carousels | You need platform-native social copy |
| `tone-of-voice` | Brand voice guide and channel adaptation | You need a reusable voice system |
| `career-copywriting` | CVs, cover letters, LinkedIn profiles, recruiter-facing copy | You need personal positioning or applications |

## What makes it different

### It is principles-based

The library is built on direct-response fundamentals from Drayton Bird, Eddie Shleyner, Claude Hopkins, David Ogilvy, Eugene Schwartz, John Caples, Robert Collier, and other copywriters who cared about response.

It does not only give templates.

It teaches the agent what to look for.

### It has a human voice layer

The reference file `references/human-voice-rules.md` helps remove common AI tells:

- generic vocabulary
- over-smooth rhythm
- fake insight phrases
- weak openings
- announced conclusions
- overused punctuation

The goal is not to trick a detector.

The goal is copy that a real person might have written because it has texture, judgment, and restraint.

### It uses the Eddie and Drayton layer

`references/drayton-eddie-principles.md` gives the working method:

- write to one real prospect
- prove early
- do the complete selling job
- find hooks like a sales detective
- teach through micro-lessons
- use vivid words
- qualify big promises
- close the loop

### It critiques before it rewrites

Bad rewrites erase good material.

The library includes a critique workflow so the agent first identifies:

- the job of the copy
- the reader’s awareness stage
- the strongest existing line
- what must be preserved
- the real conversion leak

Then it rewrites.

### It connects SEO and conversion

The SEO skill does not treat ranking as the finish line.

It links keyword intent, SERP format, internal links, CTA mapping, analytics evidence, and post-publish measurement.

Search traffic only matters if the page moves demand toward an action.

## How the skills work together

```text
tone-of-voice
  -> creates a voice guide
  -> all other skills follow it

copywriting
  -> handles persuasion, pages, email, and offers

seo-copywriting
  -> adds search intent, SERP structure, metadata, internal links, and refresh planning

french-copywriting
  -> adapts copy for native French rhythm and rules

social-copywriting
  -> adapts ideas to LinkedIn and X formats

career-copywriting
  -> turns experience into proof for recruiters and hiring managers
```

All skills can also use `.agents/product-marketing-context.md` when it exists.

## File structure

```text
copywriting-skill/
  SKILL.md
  skills/
    seo-copywriting/SKILL.md
    french-copywriting/SKILL.md
    social-copywriting/SKILL.md
    tone-of-voice/SKILL.md
    career-copywriting/SKILL.md
  references/
    drayton-eddie-principles.md
    micro-lesson-workflow.md
    hook-discipline.md
    shared-mental-images.md
    close-the-loop-endings.md
    concision-pass.md
    copy-critique-before-rewrite.md
    career-application-copywriting.md
    proof-provenance.md
    seo-growth-copy-integration.md
    human-voice-rules.md
    email-frameworks.md
    seo-benchmarks.md
    french-frameworks.md
    linkedin-formats.md
    x-formats.md
    tone-dimensions.md
  examples/
    landing-page-before-after.md
    french-landing-page-example.md
    linkedin-micro-lesson-example.md
    seo-brief-example.md
    tone-of-voice-guide-example.md
  tests/
    test_skill_contract.py
```

## Installation

```bash
git clone https://github.com/judicael-s/Copywriting-skill.git
```

Install it wherever your agent expects skill folders.

For Claude Code, Cursor, Windsurf, and other Agent Skills compatible tools, keep the folder structure intact.

For Hermes, copy or symlink it into a profile skills directory.

Example:

```bash
mkdir -p ~/.hermes/profiles/organicagent/skills/writing
cd ~/.hermes/profiles/organicagent/skills/writing
git clone https://github.com/judicael-s/Copywriting-skill.git copywriting
```

## Common workflows

### Improve a landing page

1. Load `copywriting`.
2. Diagnose before rewriting.
3. Preserve the strongest existing line.
4. Rewrite headline, subheadline, sections, CTA, proof, and objections.
5. Run the human voice and concision passes.

### Write an SEO page

1. Load `seo-copywriting`.
2. Classify intent.
3. Analyze SERP structure if available.
4. Build the brief.
5. Draft for humans first.
6. Add metadata, internal links, CTA mapping, and refresh plan.

### Write a LinkedIn micro-lesson

1. Load `social-copywriting`.
2. Use `references/micro-lesson-workflow.md`.
3. Start from a small scene.
4. Teach one idea.
5. End when the lesson lands.

### Write French copy

1. Load `french-copywriting`.
2. Decide `tu` or `vous`.
3. Apply French typography.
4. Rewrite from intent, not from English.
5. Run the French human voice check.

### Write a cover letter or CV bullets

1. Load `career-copywriting`.
2. Identify the role’s proof needs.
3. Select real evidence.
4. Preserve metric provenance.
5. Write scanner-friendly bullets before narrative.
6. Close the loop between hook and final line.

## References

Each reference exists because one recurring copy problem needed a reusable answer.

| Reference | Use it for |
|---|---|
| `drayton-eddie-principles.md` | direct-response fundamentals and Eddie-style lesson craft |
| `micro-lesson-workflow.md` | LinkedIn, newsletters, educational posts |
| `hook-discipline.md` | choosing a stronger entry point |
| `shared-mental-images.md` | memorable openings through objects, rituals, and scenes |
| `close-the-loop-endings.md` | endings that echo the hook |
| `concision-pass.md` | cutting without weakening persuasion |
| `copy-critique-before-rewrite.md` | diagnosing before rewriting |
| `career-application-copywriting.md` | CVs, applications, LinkedIn positioning |
| `proof-provenance.md` | claims, metrics, case studies, attribution |
| `seo-growth-copy-integration.md` | SEO copy tied to GSC, GA4, Trends, and conversion |
| `human-voice-rules.md` | human voice and anti-generic editing |
| `french-frameworks.md` | native French copy rules |
| `seo-benchmarks.md` | SEO content thresholds and specs |
| `linkedin-formats.md` | LinkedIn formats and constraints |
| `x-formats.md` | X post and thread formats |
| `tone-dimensions.md` | brand voice design |

## Credits

Built by [Jules Sauvajol](https://github.com/judicael-s), bilingual FR/EN digital marketer focused on SEO, content strategy, and marketing automation.

## License

MIT
