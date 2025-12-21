# Collaboration Workflow

A practical guide for running productive game design sessions.

---

## Before the Meeting

### 1. Choose a Focus Area (Pick ONE)

| Session Type | Focus | Duration | Best For |
|--------------|-------|----------|----------|
| **Core Mechanics** | Rules, systems, flow | 60-90 min | Early design, major changes |
| **Content Review** | Cards, events, balance | 45-60 min | Mid-design, filling gaps |
| **Playtest Debrief** | What worked/didn't | 30-45 min | After any playtest |
| **Quick Decision** | Resolve 2-3 [DISCUSS] items | 30 min | Unblocking progress |

### 2. Send Pre-Reading (24-48 hours ahead)

**For Core Mechanics sessions:**
```
Read: design/rules/quick-start-v1.md (5 min)
Skim: design/rules/core-rules-v1.md - sections relevant to topic (10 min)
```

**For Content Review sessions:**
```
Read: Relevant card file (policies or events) (10 min)
Note: Which cards feel off? Which excite you?
```

**For Playtest Debrief:**
```
Read: Nothing - come with fresh memories
Bring: Any notes taken during play
```

### 3. Prepare Materials

Print or share screens for:
- [ ] Quick-start rules (everyone needs this)
- [ ] Specific section under discussion
- [ ] CHECKLIST.md open for tracking decisions
- [ ] Blank paper for sketching ideas

---

## Meeting Structure

### Opening (5 min)

```
1. State the session goal in ONE sentence
   Example: "Today we decide if 6 institutions is too many"

2. Confirm time box
   "We have 60 minutes. Hard stop at [time]."

3. Establish decision mode
   - "We'll decide by consensus"
   - "I'll take input and decide after"
   - "We'll vote if stuck"
```

### Context Setting (5-10 min)

**Read aloud together** the relevant section. Don't assume everyone read pre-work.

For mechanics discussions, read from `quick-start-v1.md`:
- The specific phase or system in question
- Any [DISCUSS] notes from `core-rules-v1.md`

For content discussions, read 2-3 example cards aloud.

### Structured Discussion (30-45 min)

Use this format for each topic:

```
┌─────────────────────────────────────────────┐
│ TOPIC: [Specific question]                  │
├─────────────────────────────────────────────┤
│ CURRENT DESIGN: [What the doc says now]     │
├─────────────────────────────────────────────┤
│ CONCERNS: [What's wrong or unclear?]        │
│  - Person A: ...                            │
│  - Person B: ...                            │
├─────────────────────────────────────────────┤
│ ALTERNATIVES: [Other options]               │
│  1. ...                                     │
│  2. ...                                     │
│  3. Keep as-is                              │
├─────────────────────────────────────────────┤
│ DECISION: [What we chose]                   │
│ RATIONALE: [Why - one sentence]             │
└─────────────────────────────────────────────┘
```

**Facilitation tips:**
- One topic at a time. Park tangents in a "parking lot" list.
- Ask quieter people directly: "What do you think?"
- If stuck after 10 min: Vote or defer to next session.

### Closing (5-10 min)

```
1. Recap decisions made (read them back)
2. Assign action items with names and dates
3. Set next session date and focus
4. Quick pulse: "Rate this session 1-5, anything to improve?"
```

---

## Discussion Guides by Topic

### Session A: Player Experience

**Read first:** `core-rules-v1.md` sections: "What Players Represent", "Influence", "Voting"

**Key questions:**
1. Does being a "faction leader" feel right? Alternatives?
2. Is Influence (personal resource) engaging or fiddly?
3. Is simultaneous voting exciting or chaotic?
4. Are the 5 named factions problematic?

**Decision needed:** Confirm or change player identity concept.

---

### Session B: Core Loop & Pacing

**Read first:** `quick-start-v1.md` full page, `core-rules-v1.md` "Turn Structure"

**Key questions:**
1. Are 6 phases per round too many? Which could merge?
2. Is 5-minute deliberation enough? Too much?
3. Should there be a timer or open discussion?
4. Is "max 3 policies per round" the right limit?

**Decision needed:** Confirm or simplify turn structure.

---

### Session C: Institutions

**Read first:** `core-rules-v1.md` section "Institutions"

**Key questions:**
1. Are 6 institutions too complex? Which could merge or cut?
2. Is dice-based Judiciary review too random?
3. Do Markets need their own mechanic or just affect Growth?
4. Is Public Opinion distinct enough from Legitimacy?

**Decision needed:** Final institution count and mechanics.

---

### Session D: Victory & Tension

**Read first:** `core-rules-v1.md` sections "Victory Conditions", "Feedback Loops"

**Key questions:**
1. Is semi-cooperative mode (survive together, compete for legacy) the right tension?
2. Are collapse thresholds too punishing? Too lenient?
3. Are Legacy priorities interesting choices?
4. Does the Governing Coalition mechanic add fun?

**Decision needed:** Confirm victory structure.

---

### Session E: Content Balance

**Read first:** `sample-policies-v1.md` and `sample-events-v1.md`

**Key questions:**
1. Do policies feel meaningfully different?
2. Are tradeoffs clear on each card?
3. Is any ideology systematically advantaged?
4. Are events interesting to respond to?

**Decision needed:** Content direction and any cards to cut/revise.

---

### Session F: First Playtest Planning

**Read first:** `base-scenario-v1.md`, `quick-start-v1.md`

**Key questions:**
1. What's the minimum viable prototype? (Paper? Digital?)
2. Who will play the first test? (Designer solo? Friends?)
3. What are we specifically testing? (Pacing? Fun? Clarity?)
4. How will we capture feedback?

**Decision needed:** Playtest date and materials list.

---

## Capturing Decisions

After each session, update these files:

### 1. Update `CHECKLIST.md`
Mark items as complete, add new items discovered.

### 2. Update `docs/design-decisions.md`
Add entry for each decision:

```markdown
## [Date]: [Decision Title]

**Question:** What were we deciding?
**Options Considered:**
1. Option A - pros/cons
2. Option B - pros/cons
3. Option C - pros/cons

**Decision:** We chose Option B

**Rationale:** One sentence why.

**Impact:** What files/systems this affects.
```

### 3. Update Source Files
If a decision changes rules, update `core-rules-v1.md` directly.
- Change the text
- Update version note at bottom
- Mark old [DISCUSS] items as resolved

---

## Meeting Cadence Suggestions

| Phase | Frequency | Focus |
|-------|-----------|-------|
| **Early Design** | 1-2x/week | Core mechanics, player identity |
| **Content Creation** | 1x/week | Card design, balance |
| **Playtesting** | After each test | Debrief, iteration |
| **Polish** | As needed | Edge cases, wording |

---

## Remote Collaboration Tips

If meeting virtually:

1. **Shared screen:** One person shares the relevant doc
2. **Comments:** Use a shared doc where everyone can add comments
3. **Voting:** Use quick polls (1, 2, or 3 in chat)
4. **Miro/Figma:** For visual card layout discussions
5. **Record decisions:** Someone types decisions in real-time, visible to all

---

## Quick Reference: Files to Know

| File | When to Use |
|------|-------------|
| `quick-start-v1.md` | Every session - the "source of truth" for rules |
| `core-rules-v1.md` | Deep dives on specific mechanics |
| `sample-policies-v1.md` | Content balance discussions |
| `sample-events-v1.md` | Content balance discussions |
| `base-scenario-v1.md` | Playtest setup |
| `CHECKLIST.md` | Track progress, assign next steps |
| `docs/charter.md` | When debating if something fits the vision |
| `docs/design-decisions.md` | Log all decisions for future reference |

---

## First Session Recommendation

If this is your first design meeting, start here:

### Session 0: Vision Alignment (45 min)

**Agenda:**
1. **(5 min)** Read `quick-start-v1.md` together
2. **(10 min)** Each person shares: "What excites you about this game?"
3. **(10 min)** Each person shares: "What concerns you?"
4. **(15 min)** Discuss: Do we agree on the core experience we want?
5. **(5 min)** Pick next session focus from the guides above

**No decisions required** - just alignment and excitement.

---

*Workflow v1.0 - Ready to use*
