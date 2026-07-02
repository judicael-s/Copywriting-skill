# Human Voice Rules

This file is the anti-AI detection layer for the entire copywriting skill suite. Every sub-skill — French, social, tone-of-voice — loads this reference before generating output. These rules exist because AI writing has measurable statistical signatures: vocabulary overuse rates, punctuation patterns, and sentence-length variance that differ sharply from human prose. Apply every rule here without exception.

Sources: AI writing detection rates based on Originality.ai corpus analysis (2024), Scribbr AI detection benchmarks, and GPTZero statistical analysis of 100K+ documents. Burstiness thresholds from Sadasivan et al. (2023) "Can AI-Generated Text be Reliably Detected?"

---

## Section 1: Banned Vocabulary

### Tier 1 — Never Use

These words appear in AI-generated text at 10x–269x the rate found in human writing. Using any of them is an immediate detection signal.

| Banned Word / Phrase | Replace With |
|---|---|
| delve | dig into, look at, explore, examine |
| leverage | use |
| utilize | use |
| crucial | important, key, matters because… (say why) |
| pivotal | important, decisive, the turning point |
| landscape | space, market, field, industry |
| robust | strong, solid, reliable, built to handle X |
| seamless | smooth, easy, invisible, frictionless |
| comprehensive | covers X, Y, and Z (name the things) |
| cutting-edge | new, latest, first-to-market |
| navigate | manage, handle, figure out, work through |
| foster | build, grow, encourage, create |
| moreover / furthermore | (delete — just start the next sentence) |
| streamline | simplify, speed up, cut steps |
| innovative | (say what specifically is new about it) |
| tapestry | (be specific — what exactly is mixed or layered?) |
| realm | world, field, area |
| intersection | where X meets Y (name them) |
| unlock / unleash / harness | (describe what actually happens — "you get X") |
| unprecedented | rare, first, unusual, never seen before in X |
| game-changer | (describe the actual impact in concrete terms) |
| supercharge | (say what improves and by how much) |
| future-proof | built for X condition, survives Y change |
| best-in-class | (state the specific metric or benchmark) |
| next-generation | (say what actually changed from the previous version) |
| showcasing | showing |
| impacting | affecting, changing, hurting, helping |
| aligns | fits, matches, works with |
| empower | let, allow, give people the ability to |
| journey | process, path, experience, project |
| synergy | working together, combined effect (name what combines) |
| holistic | covers everything, end-to-end (name the parts) |
| ecosystem | platform, network, set of tools (name them) |
| transformative | changes how you do X (be specific) |
| paradigm shift | fundamental change in how X works |

### Tier 2 — Avoid

These are softer signals, but they accumulate. Avoid them in the same piece.

- indeed
- it's worth noting
- it's important to consider
- arguably
- dynamic (as an adjective for a company, team, or market)
- scalable (unless talking about literal technical architecture)
- agile (outside a strict Scrum context)
- proactive
- tailored (use "built for" or "designed for X person")
- elevated (as a marketing adjective)
- intricate
- nuanced (use it; don't announce it)
- underscore (as a verb meaning "to emphasize")
- foster meaningful connections
- ensure (replace with "make sure," "confirm," or just state the action)
- leverage synergies (double-banned — never)
- de plus (French — see Section 8)
- en outre (French — see Section 8)

---

## Section 2: Punctuation Rules

### Em Dashes (—)

AI text uses em dashes at 4.7x the rate of human writers. One or two per 500 words is the general ceiling.

**User or brand override wins.** If a user, brand, or project says dashes feel AI-coded, use zero em dashes and zero en dashes in user-facing copy. Prefer commas, colons, semicolons, parentheses, line breaks, or short sentences.

| AI Pattern | Human Alternative |
|---|---|
| "The solution — which took three years — launched quietly." | Break into two sentences. |
| "There's one thing — consistency — that matters most." | "Consistency matters most." |
| "We built this — and it works." | "We built this. It works." |
| "Speed — not features — wins." | "Speed wins. Not features." |

Use an em dash only when a pause genuinely changes the meaning and no other structure works.

### Setup Colons — Banned Phrases

Never introduce a point with these:

- "Here's the thing:"
- "The result:"
- "The bottom line:"
- "Here's why:"
- "The answer:"
- "Here's what that means:"

Just make the point directly. The setup colon is a tell that you're performing insight rather than delivering it.

### Semicolons

Use them rarely. Most semicolons should become periods. If the two clauses can stand alone, make them stand alone.

### Exclamation Marks

- Maximum 1 per piece in professional writing.
- Zero in B2B copy.
- Never in headlines or subject lines unless it is a genuine command or call-to-action.

---

## Section 3: Sentence Rhythm (Burstiness)

Burstiness is the strongest AI detection signal. Human writers show a standard deviation of 4.8–7.2 words per sentence. AI text clusters between 2.0–3.8. Every sentence is a similar length. It reads smooth. Too smooth.

### Rules

**Vary length aggressively.** A three-word sentence. Followed by a much longer one that builds on it, adds context, and earns the short sentence before it. Then another short one.

**Use fragments when appropriate.** Not always. But sometimes. Especially for emphasis.

**Break parallel structures.** "We design, we build, we deliver" is AI rhythm. Human rhythm trips over itself intentionally.

**Kill "Not only X but also Y."** This construction appears in AI text at high rates. Rewrite it as two sentences or choose one claim.

**No participial openers as a pattern.** Opening every paragraph with "Having done X, we…" or "Recognizing Y, the team…" is an AI tell. Use it once if it fits; never as a default.

**No "It's not just X, it's Y."** This is a filler reframe. Make the real point directly.

**No "In a world where X, Y matters more than ever."** Delete the whole first clause.

---

## Section 4: Paragraph Rules

**Vary paragraph length.** Some paragraphs are one sentence. Some run five or six. Never write three paragraphs in a row of the same length.

**Do not always lead with the topic sentence.** Human writing buries the point, circles around it, or saves it for last. AI always front-loads.

**Drop transition sentences.** Sentences like "Now let's look at…" or "With that in mind…" are scaffolding. Delete them. Move directly to the next point.

**No symmetrical structure.** If section 1 has 3 paragraphs and section 2 has 3 paragraphs and section 3 has 3 paragraphs, rewrite it. Symmetry signals generation.

---

## Section 5: Opening and Closing Blacklist

### Never Open With

1. "In today's fast-paced world…"
2. "In an era where…"
3. "As [topic] continues to evolve…"
4. "Whether you're a [persona A] or a [persona B]…"
5. "Have you ever wondered…"
6. "[Topic] is more important than ever."
7. "It's no secret that…"
8. "At [Company], we believe…"
9. "In this article, we'll explore…"
10. Any restatement of the brief or question as the first sentence.

**Instead:** open with a specific fact, a sharp question that assumes the reader's problem, a bold claim you can back, or a story that drops in mid-action.

### Never Close With

1. "In conclusion…"
2. "As we've seen…"
3. "I hope this helps."
4. "Feel free to reach out if you have any questions."
5. "The possibilities are endless."
6. "The future is bright."
7. Any variation of "Together, we can [vague positive outcome]."

**Instead:** just end. State the last point, make the ask, or leave the reader with the sharpest line in the piece. Conclusions don't need to announce themselves.

---

## Section 6: Tone Rules

### Take Positions

AI hedges. Humans have opinions. Replace "it may be worth considering" with "do this." Replace "some experts argue" with "the evidence says" or "I'd argue."

### Remove Hedging Language

Audit every draft for:
- "somewhat," "rather," "quite," "fairly," "relatively"
- "in many cases," "often," "typically," "generally speaking"
- "it could be argued that," "one might say"

Delete them unless the hedge is itself the point ("this only works in some markets — specifically X").

### No Performative Enthusiasm

Never write "Great question!" or "Absolutely!" in copy. Never write "I'm excited to share…" The reader does not care about your excitement. Share the thing.

### No Commenting on the Question

Do not open a response or piece by describing what you are about to do. ("This piece will walk you through X.") Walk through X.

### Show Empathy Through Specificity

Instead of "We understand how challenging this can be," name the specific challenge. "You've spent three hours reformatting the same spreadsheet" lands harder than any sympathy statement.

### Replace Vague Attribution

- "Studies show…" → name the study, the institution, the year.
- "Experts agree…" → name one expert and quote them.
- "Research suggests…" → cite it or cut it.

---

## Section 7: Structural Rules

**Odd numbers for lists.** 3, 5, 7. Never 4, 6, or 10 unless the content genuinely has that many items. Even numbers signal padding or artificial symmetry.

**Asymmetric sections.** If you have three sections, they should not each be the same length. Let the most important section breathe. Cut the least important.

**No synonym cycling.** AI rotates synonyms to avoid repetition. Humans repeat the right word and vary sentence structure instead. If "conversion" is the right word, use it every time.

**No "Key Takeaways" sections.** If the piece needed a summary section, it was too long. Cut the piece.

**Rule of three — use sparingly.** It is a rhetorical device, not a default structure. When everything comes in threes, nothing lands.

---

## Section 8: French-Specific Anti-AI Rules

### Banned French Vocabulary

| Banned | Replace With |
|---|---|
| crucial | important, décisif, ça change tout |
| paysage (as in "le paysage digital") | secteur, marché, environnement |
| approfondir | creuser, aller plus loin, examiner |
| de surcroit | en plus, aussi, par ailleurs |
| mettre en lumière | montrer, révéler, souligner |
| vibrant (applied to communities or ecosystems) | actif, engagé, en mouvement |
| murmure (literary atmospheric opener) | (cut entirely — start with the fact) |
| promesse (used as brand abstraction) | (say what the brand actually delivers) |
| instant suspendu | (cut — overused in French lifestyle copy) |
| secret brûlant | (cut — tabloid cliché) |

### Banned French AI Openings

1. "Dans un monde où [phénomène] s'accélère…"
2. "À l'heure où [industrie] se transforme…"
3. "Que vous soyez [persona A] ou [persona B]…"
4. "Aujourd'hui plus que jamais…"

### French-Specific Principles

1. **Write colloquial French.** French AI copy is often formal and Latinate. Real French marketing uses contractions, shortcuts, and spoken rhythm. "C'est" beats "Il est." "On" beats "Nous."

2. **Use cultural references that land locally.** Generic global references ("like Netflix did…") feel imported. Anchor to French media, markets, or moments when the reference actually fits.

3. **Preserve rough edges.** French copywriting at its best has a certain directness that sounds slightly impolite in English. Don't sand it down into international-English politeness.

4. **Use real French idioms, not translated ones.** "Ça tombe à pic" is French. "C'est un game-changer" is not — it's English wearing a French accent. Choose one language per phrase.

5. **Anchor claims in specific French data.** "En France, 67% des PME…" is more credible than "Many businesses across Europe…" Use French sources, French statistics, French examples.

---

## Section 9: Human Voice Check (Mandatory Output Checklist)

Run this on every draft before delivery. Every item must pass.

- [ ] 1. **Tier 1 vocabulary scan:** zero banned words from the Tier 1 table.
- [ ] 2. **Em dash count:** 2 or fewer per 500 words.
- [ ] 3. **Setup colons:** none of the 6 banned intro phrases present.
- [ ] 4. **Burstiness check:** at least 3 sentence lengths present; no 4 consecutive sentences within 3 words of each other.
- [ ] 5. **Opening check:** does not begin with any of the 10 banned opening patterns.
- [ ] 6. **Closing check:** does not end with any of the 7 banned closing patterns.
- [ ] 7. **Hedging audit:** "somewhat," "rather," "quite," "in many cases," "typically" appear zero times unless doing specific argumentative work.
- [ ] 8. **Attribution check:** no "studies show," "experts agree," or "research suggests" without a named source.
- [ ] 9. **(French only) Colloquial register:** uses "on" over "nous," contractions, spoken rhythm.
- [ ] 10. **(French only) Banned French vocabulary scan:** zero entries from the French banned table.

---

## Related References

- **`references/tone-dimensions.md`** — Tone dimensions (especially Directness and Formality) interact with these rules. A brand scoring Directness 1-2 may legitimately use some hedging language that Section 6 flags. Check the brand's tone guide before enforcing hedging rules absolutely.
- **`references/seo-benchmarks.md`** — Readability targets (Flesch 60-70, grade 7-8) complement the burstiness and rhythm rules in Section 3. Both serve the same goal: natural-sounding, reader-friendly content.
- **`references/email-frameworks.md`** — Email copy should follow all rules in this file. Section 5 (Opening/Closing Blacklist) is especially relevant for email subject lines and openers.
