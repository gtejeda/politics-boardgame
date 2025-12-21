# Core Rules v1.0 - Initial Design Draft

> **Design Note:** This is an opinionated first draft. Every decision is intentional but negotiable. Items marked with [DISCUSS] are particularly open to change.

---

## Game Overview

**Players:** 3-5 (optimal: 4)
**Time:** 90-120 minutes
**Mode:** Semi-cooperative with individual victory

Players are **faction leaders** within a single democratic nation. You share responsibility for governing but compete for influence and legacy. If the nation collapses, everyone loses. Among survivors, the player whose legacy dimensions score highest wins.

---

## What Players Represent

Each player leads a **Political Faction** - a coalition of interests, ideology, and supporters. Factions are not strictly "left" or "right" but have **starting leanings** that give minor bonuses to certain policy types.

### The 5 Factions

| Faction | Starting Lean | Bonus |
|---------|---------------|-------|
| **The Progressives** | Social reform | +1 Legitimacy when passing Social policies |
| **The Conservatives** | Stability focus | +1 Stability when blocking rapid change |
| **The Liberals** | Market & liberty | +1 Growth when passing Economic deregulation |
| **The Nationalists** | Security & sovereignty | +1 Stability when passing Security policies |
| **The Populists** | Anti-establishment | +1 Legitimacy when opposing institutional policies |

[DISCUSS] Are named factions too on-the-nose? Alternative: Abstract colors with no preset identity.

---

## Resources

Five national resources tracked on a central board. All players share these - the nation succeeds or fails together.

| Resource | Range | Starts At | Collapse Threshold |
|----------|-------|-----------|-------------------|
| **Budget** | -10 to +20 | 8 | ≤0 for 2 consecutive rounds |
| **Legitimacy** | 0 to 20 | 10 | ≤2 |
| **Stability** | 0 to 20 | 10 | ≤2 |
| **Growth** | -5 to +15 | 5 | ≤-3 for 2 consecutive rounds |
| **Liberty** | 0 to 20 | 10 | ≤3 (triggers Authoritarian Lock) |

### Resource Interactions (Built-in Tensions)

These automatic adjustments happen during the Consequences phase:

- **Growth > 10:** Budget +1 (tax revenue)
- **Growth < 0:** Budget -1, Stability -1 (recession effects)
- **Stability < 5:** Legitimacy -1 (public loses faith)
- **Liberty < 5:** Legitimacy -1 (repression breeds resentment)
- **Legitimacy < 5:** All policy costs +1 (resistance to government)
- **Budget < 0:** Cannot pass policies costing Budget (austerity)

---

## Influence (Individual Resource)

Each player has personal **Influence** (0-15, starts at 5). This represents your faction's political capital.

**Gaining Influence:**
- +1 when a policy you sponsored passes
- +2 when you successfully predict a crisis outcome
- +1 when you're on the winning side of a contested vote

**Spending Influence:**
- 1 Influence: Add +1 to any vote you're part of
- 2 Influence: Sponsor a policy from your hand (required to propose)
- 3 Influence: Force a policy to a vote (bypass deliberation)
- 5 Influence: Veto a policy after it passes (once per game)

---

## Institutions

Six institutions constrain what players can do. Each has a **Strength** rating (1-5, starts at 3).

### Legislature
- All policies must pass here by majority vote
- **Strength effect:** Higher = more votes needed (Strength 3 = simple majority, Strength 5 = supermajority)
- Players vote with their Influence weight (base 1 + spent Influence)

### Judiciary
- Reviews policies that affect Liberty or Institutional categories
- **Strength effect:** Higher = more likely to block unconstitutional policies
- Roll 1d6: Policy blocked if roll ≤ Judiciary Strength AND policy reduces Liberty

### Executive
- Implements passed policies
- **Strength effect:** Higher = better implementation (full effect). Lower = reduced effect or delay
- Roll 1d6: Full implementation if roll ≤ Executive Strength, otherwise 50% effect

### Markets
- Generate Growth automatically but resist control
- **Strength effect:** Higher = more stable but less dynamic. Lower = volatile but higher peaks
- Each round: Roll 1d6. If ≤ Market Strength: Growth +1. If > Market Strength: Growth +1d3-2 (range -1 to +1)

### Public Opinion
- Tracked as a separate meter (Approval: 0-10, starts at 5)
- **Strength effect:** Higher = more electoral pressure, policies affecting Legitimacy amplified
- If Approval < 3: Governing faction loses 1 Influence per round

### Civil Society
- Organized interests that respond to policies
- **Strength effect:** Higher = more active response to policy
- When a policy passes: If Civil Society Strength ≥ 4 AND policy is controversial, trigger Backlash event

[DISCUSS] Are 6 institutions too many to track? Could merge some.

---

## Turn Structure

Each game round represents approximately 1 year of governance. Play 8-12 rounds (scales with player count).

### Phase 1: Events (Simultaneous)

1. Draw 1 Event card per player (e.g., 4 players = 4 events)
2. Reveal all events simultaneously
3. Events with "Immediate" timing resolve now
4. Events with "Pending" timing are placed on the timeline

### Phase 2: Deliberation (5 minutes max)

1. Players discuss the situation openly
2. Negotiate support, make deals, form temporary coalitions
3. No binding commitments - deals can be broken
4. Each player selects 1 Policy card from hand to potentially sponsor

### Phase 3: Policy Actions (Clockwise from First Player)

Each player in turn order:

1. **Sponsor** (optional): Pay 2 Influence to put your selected Policy up for vote
2. **Vote**: All players vote Yes/No/Abstain on sponsored policy
   - Yes = +1 vote (can spend Influence for more)
   - No = -1 vote (can spend Influence for more)
   - Abstain = 0
3. **Resolve**: If Yes > No, policy passes. If tie, policy fails.
4. Repeat for next player's sponsored policy

Maximum 1 policy sponsored per player per round. Maximum 3 policies can pass per round (others are tabled).

### Phase 4: Implementation

For each passed policy:

1. Check Judiciary (if applicable): Roll vs. Judiciary Strength
2. Check Executive: Roll vs. Executive Strength for implementation quality
3. Apply immediate effects (modified by implementation roll)
4. Place delayed effect markers on timeline

### Phase 5: Consequences

1. **Delayed Effects**: Resolve any effects scheduled for this round
2. **Feedback Loops**: Check and apply resource interactions
3. **Institutional Decay/Growth**: Adjust institution strengths based on round events
4. **Market Phase**: Roll for Market-generated Growth
5. **Approval Update**: Adjust Public Opinion based on resource changes

### Phase 6: Refresh

1. Draw 2 Policy cards, discard down to 5
2. Pass First Player marker clockwise
3. Check for collapse conditions
4. If Round 8+ : Check for endgame trigger

---

## Voting in Detail

When a policy is sponsored:

1. Sponsor states the policy and its effects
2. 30 seconds for final negotiation
3. Simultaneous vote reveal (use hidden tokens or fingers)
4. Count votes: Each player = 1 base vote + any spent Influence
5. Ties fail. Majority passes.

**Whip System** [DISCUSS]: Before vote reveal, one player can spend 2 Influence to become Whip. The Whip votes last and openly, seeing all other votes first.

---

## Delayed Effects System

Many policies have effects that trigger 2-4 rounds later. Track using a **Timeline Board**:

```
Round:  Current | +1 | +2 | +3 | +4 | +5
Effects:   --   | A  | B,C|  D |    | E
```

When placing a delayed effect:
1. Put a numbered token on the timeline
2. Record the effect on the tracking sheet
3. When the round arrives, the effect triggers automatically

Players can see what's coming but not always remember exact effects (simulates policy complexity).

---

## Feedback Loops (Automatic)

These trigger during Consequences phase when conditions are met:

### Economic Cycle
- **Boom**: If Growth ≥ 8 for 2 consecutive rounds → Budget +2, but Stability -1 (inequality)
- **Bust**: If Growth ≤ 0 for 2 consecutive rounds → Budget -2, Legitimacy -1

### Legitimacy Spiral
- **Mandate**: If Legitimacy ≥ 15 → All policy implementation +1
- **Crisis of Faith**: If Legitimacy ≤ 5 → All policy costs +1 Influence

### Stability-Liberty Tension
- **Security State**: If Stability > 15 AND Liberty < 8 → Liberty -1 per round (automatic erosion)
- **Unrest**: If Stability < 5 → Draw 1 extra Crisis event

### Inequality Accumulation (Tracked Separately)
- **Inequality Counter**: Starts at 0, max 10
- Certain policies add to Inequality (marked on cards)
- If Inequality ≥ 7 AND Legitimacy < 10 → Stability -2 (unrest)
- If Inequality ≥ 10 → Trigger Revolution event

### Institutional Erosion
- Each time Judiciary is bypassed: Judiciary Strength -1
- Each time Executive acts without Legislature: Legislature Strength -1
- If any Institution Strength ≤ 1: That institution stops functioning

---

## Victory Conditions

### Collective Loss (Everyone Loses)
If ANY collapse condition triggers, the game ends immediately and all players lose:

- **Fiscal Collapse**: Budget ≤ 0 for 2 consecutive rounds
- **Legitimacy Crisis**: Legitimacy ≤ 2
- **Systemic Breakdown**: Stability ≤ 2
- **Authoritarian Lock**: Liberty ≤ 3 AND any Security policy passed this round
- **Revolution**: Inequality ≥ 10 AND Stability ≤ 5

### Individual Victory (Among Survivors)

If the nation survives to the end (Round 8-12 based on player count), players score:

**Legacy Scoring:**

Before the game, each player secretly chooses 2 Legacy priorities from:

| Legacy | Scoring |
|--------|---------|
| **Prosperity** | 1 point per Growth above 5, 1 point per Budget above 10 |
| **Equality** | 3 points if Inequality ≤ 3, -2 points if Inequality ≥ 7 |
| **Freedom** | 1 point per Liberty above 10 |
| **Order** | 1 point per Stability above 10 |
| **Institutions** | 1 point per Institution at Strength 4+ |
| **Influence** | 1 point per 3 personal Influence remaining |

**Bonus Points:**
- +3 for most policies passed
- +2 for predicting final Approval rating (within 1)
- +2 for never breaking a deal

Highest total wins. Ties go to highest remaining Influence.

---

## Policy Cards

Each policy card contains:

```
┌─────────────────────────────────┐
│ [CATEGORY]           [COST]     │
│                                 │
│ POLICY NAME                     │
│                                 │
│ Immediate: [Effect]             │
│ Delayed (Xr): [Effect]          │
│                                 │
│ Tradeoff: [Negative effect]     │
│                                 │
│ Requires: [Institutional path]  │
│ ───────────────────────────     │
│ [Ideology lean: L/C/R]  [#ID]   │
└─────────────────────────────────┘
```

**Cost**: Influence to sponsor (usually 2) + any Budget cost
**Requires**: Which institutions must approve (all policies need Legislature; some need Judiciary review)

---

## Event Cards

```
┌─────────────────────────────────┐
│ [SEVERITY]          [CATEGORY]  │
│                                 │
│ EVENT NAME                      │
│                                 │
│ [Narrative text]                │
│                                 │
│ Effect: [What happens]          │
│                                 │
│ Response Options:               │
│ A) [Choice]: [Consequence]      │
│ B) [Choice]: [Consequence]      │
│ C) Ignore: [Consequence]        │
│                                 │
│ ───────────────────────────     │
│ [Timing: Immediate/Pending +X]  │
└─────────────────────────────────┘
```

**Severity**: Minor (small effects), Moderate (meaningful), Major (significant), Crisis (game-changing)
**Response**: Players vote on which response to take (or individual faction responses where noted)

---

## Component List (Prototype)

- 1 Central Board (Resource tracks, Institution strengths, Timeline)
- 5 Faction boards (Influence track, Legacy selection)
- 60 Policy cards (12 per category)
- 40 Event cards
- 5 sets of voting tokens (Yes/No/Abstain per player)
- Resource markers (cubes or tokens)
- Influence tokens (personal supply per player)
- Delayed effect markers (numbered 1-10)
- 2 six-sided dice
- First Player marker
- Tracking sheet pad

---

## Design Decisions Log

| Decision | Chosen Option | Rationale | Alternatives Considered |
|----------|---------------|-----------|------------------------|
| Player count | 3-5 | Enough for meaningful votes, not too chaotic | 2-player variant, 6+ party mode |
| Player role | Faction leaders | Allows competition within shared governance | Single government, pure parties |
| Game mode | Semi-cooperative | Creates tension: must cooperate to survive, compete to win | Pure co-op, pure competitive |
| Voting | Majority with Influence | Simple but allows political capital spending | Ranked choice, unanimous |
| Institutions | 6 with Strength ratings | Each constrains differently | Fewer institutions, binary on/off |
| Delayed effects | Timeline board | Visual, trackable, creates anticipation | Hidden effects, dice-based |
| Victory | Legacy priorities | Multiple valid strategies, chosen secretly | Single score, faction-specific |

---

## Open Questions in This Design

1. [DISCUSS] Is 90-120 minutes too long for the target audience?
2. [DISCUSS] Are the 5 named factions too politically charged?
3. [DISCUSS] Is the Judiciary review mechanic (dice roll) too random?
4. [DISCUSS] Should deals be binding or always breakable?
5. [DISCUSS] Is Inequality tracked well enough or too hidden?
6. [DISCUSS] Are 6 institutions too complex for first playtest?

---

*Version 1.0 - Initial Draft*
*Ready for discussion and iteration*
