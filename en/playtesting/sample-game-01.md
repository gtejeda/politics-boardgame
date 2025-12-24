# Sample Game Simulation #1: Four-Player Session

> **Purpose:** This document simulates a complete game session to illustrate how mechanics interact, demonstrate strategic decisions, and identify potential design issues.

---

## Setup

### Players and Factions

| Player | Faction | Starting Influence | Bonus |
|--------|---------|-------------------|-------|
| **Alice** | The Progressives | 5 | +1 Legitimacy when passing Social policies |
| **Bob** | The Conservatives | 5 | +1 Stability when blocking rapid change |
| **Carol** | The Liberals | 5 | +1 Growth when passing Economic deregulation |
| **David** | The Nationalists | 5 | +1 Stability when passing Security policies |

### Secret Legacy Priorities (Revealed at Game End)

- **Alice**: Equality, Freedom
- **Bob**: Order, Institutions
- **Carol**: Prosperity, Influence
- **David**: Order, Prosperity

### Starting National Resources

| Resource | Starting Value |
|----------|----------------|
| Budget | 8 |
| Legitimacy | 10 |
| Stability | 10 |
| Growth | 5 |
| Liberty | 10 |
| Inequality | 0 |
| Public Approval | 5 |

### Starting Institutional Strength (All at 3)

| Institution | Strength |
|-------------|----------|
| Legislature | 3 |
| Judiciary | 3 |
| Executive | 3 |
| Markets | 3 |
| Public Opinion | 3 |
| Civil Society | 3 |

### Initial Hands (5 Policy Cards Each)

**Alice (Progressives):**
1. Universal Healthcare (Social) - Budget -3, Legitimacy +2, delayed: Inequality -1
2. Green Infrastructure (Economic) - Budget -2, Growth +1, delayed: Growth +1
3. Workers' Rights Act (Social) - Liberty +1, Growth -1
4. Education Reform (Social) - Budget -2, delayed: Growth +2, Legitimacy +1
5. Progressive Taxation (Economic) - Budget +2, Growth -1, Inequality -1

**Bob (Conservatives):**
1. Law and Order Initiative (Security) - Stability +2, Liberty -1
2. Traditional Values Act (Social) - Stability +1, Liberty -1, Legitimacy +1
3. Military Expansion (Security) - Budget -3, Stability +2
4. Tax Cuts (Economic) - Budget -2, Growth +1, Inequality +1
5. Border Security (Security) - Budget -1, Stability +1

**Carol (Liberals):**
1. Free Trade Agreement (Economic) - Growth +2, delayed: Budget +1, Inequality +1
2. Deregulation Act (Economic) - Growth +2, Liberty +1, delayed: Stability -1
3. Privatization Program (Economic) - Budget +2, Legitimacy -1, Inequality +1
4. Digital Rights Bill (Social) - Liberty +1
5. Small Business Support (Economic) - Budget -1, Growth +1

**David (Nationalists):**
1. National Security Act (Security) - Stability +2, Liberty -2, requires Judiciary review
2. Immigration Control (Security) - Stability +1, Growth -1, Legitimacy -1
3. Industrial Policy (Economic) - Budget -2, Growth +1, Stability +1
4. Defense Contracts (Security) - Budget -2, Stability +1, Growth +1
5. Sovereignty Protection (Institutional) - Stability +1, Liberty -1

---

## Round 1

### Phase 1: Events

*Draw 4 Event cards (1 per player)*

**Events Revealed:**

1. **Economic Uncertainty** (Minor, Immediate)
   - Effect: Markets roll at -1 this round

2. **Public Health Concern** (Moderate, Pending +2)
   - Effect: In 2 rounds, if no Healthcare policy passed: Legitimacy -2, Approval -1

3. **Regional Trade Negotiations** (Minor, Immediate)
   - Effect: Trade policies get +1 to implementation roll this round

4. **Border Incident** (Moderate, Pending +1)
   - Effect: In 1 round, if no Security response: Stability -1

**Timeline Updated:**
```
Round:    1 (Current) | 2           | 3
Effects:     --       | Border Incident | Public Health
```

### Phase 2: Deliberation (5 minutes)

> **Alice:** "We have a health crisis coming in two rounds. I have Universal Healthcare - expensive but it'll solve it and boost Legitimacy."
>
> **David:** "And Border Incident next round. I can handle that with Immigration Control, but it hurts Growth."
>
> **Carol:** "Growth is only at 5. We can't afford to lose it. What about Law and Order, Bob? That addresses security without hurting Growth."
>
> **Bob:** "Law and Order is good but costs Liberty. The Judiciary might block it."
>
> **Alice:** "I don't love the Liberty hit, but we need to address these threats. If you support my Healthcare bill next round, I'll support Law and Order now."
>
> **Bob:** "Deal."
>
> **Carol:** "I want to push Free Trade - we need Growth before we can afford these expensive social programs."
>
> **David:** "Free Trade increases Inequality though. I'd rather do Industrial Policy - balanced growth."
>
> **Carol:** "Let's see what happens."

**Selected policies to potentially sponsor:**
- Alice: Education Reform (saving Healthcare for later)
- Bob: Law and Order Initiative
- Carol: Free Trade Agreement
- David: Industrial Policy

### Phase 3: Policy Actions

**First Player: Alice** (determined by highest influence roll at game start)

---

**Alice's Turn - Sponsors: Education Reform**

*Alice pays 2 Influence (now at 3)*

"Education Reform: Costs Budget -2. Delayed effect in 3 rounds: Growth +2, Legitimacy +1"

**30-second negotiation:**
> **Carol:** "I'll support it - we need long-term growth."
> **David:** "It's expensive and we have threats to deal with. I'm voting No."
> **Bob:** "I'll abstain - want to save influence for my policy."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | Abstain | 0 | 0 |
| Carol | Yes | 0 | +1 |
| David | No | 0 | -1 |

**Result:** Yes: 2, No: 1 → **PASSES**

*Alice gains +1 Influence for passing (back to 4)*
*Alice gains +1 Legitimacy (Progressive faction bonus for Social policy)*

---

**Bob's Turn - Sponsors: Law and Order Initiative**

*Bob pays 2 Influence (now at 3)*

"Law and Order Initiative: Stability +2, Liberty -1"

**This affects Liberty - requires Judiciary Review**

**30-second negotiation:**
> **Alice:** "I said I'd support it. But that Liberty hit worries me."
> **David:** "I'll vote Yes - we need stability for the border situation."
> **Carol:** "Liberty -1 puts us at 9. Not dangerous yet. I'll support."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | Yes | 1 | +2 |
| Carol | Yes | 0 | +1 |
| David | Yes | 0 | +1 |

**Result:** Yes: 5, No: 0 → **PASSES**

*Bob now at 2 Influence (spent 2 to sponsor, 1 to vote)*
*Bob gains +1 Influence for passing (now at 3)*

---

**Carol's Turn - Sponsors: Free Trade Agreement**

*Carol pays 2 Influence (now at 3)*

"Free Trade Agreement: Growth +2 now, delayed in 2 rounds: Budget +1, but Inequality +1"

**30-second negotiation:**
> **David:** "The Inequality increase is a problem long-term."
> **Alice:** "I don't like Inequality going up, but we need Growth. Reluctant Yes."
> **Bob:** "Growth is fine at 5. I'll vote No."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | No | 0 | -1 |
| Carol | Yes | 1 | +2 |
| David | No | 0 | -1 |

**Result:** Yes: 3, No: 2 → **PASSES**

*Carol now at 2 Influence, gains +1 for passing (now at 3)*
*Carol gains +1 Growth (Liberal faction bonus for Economic deregulation)*

---

**David's Turn - Sponsors: Industrial Policy**

*David pays 2 Influence (now at 3)*

"Industrial Policy: Budget -2, Growth +1, Stability +1"

**30-second negotiation:**
> **Alice:** "Budget at 8-2-2 = 4 after this and Education. That's getting low."
> **Bob:** "We already passed 3 policies. This one is tabled."

**Result:** Maximum 3 policies passed this round. Industrial Policy is **TABLED** (returns to David's hand).

*David gets his 2 Influence back (now at 5)*

---

### Phase 4: Implementation

**Policy 1: Education Reform**
- No Judiciary review needed (doesn't affect Liberty)
- Executive roll for implementation: Roll d6 = **4** vs Executive Strength 3
  - 4 > 3 → **Partial Implementation** (50% effect)
- Immediate: Budget -2 (reduced to -1 for partial? **[DESIGN NOTE: Rules unclear on Budget costs]**)
- **Decision: Budget costs are not reduced.** Budget -2 applied.
- Delayed effect placed on Round 4: "Growth +1, Legitimacy +0.5 (rounded to +1)"

**Policy 2: Law and Order Initiative**
- Judiciary Review required (affects Liberty)
- Roll d6 = **5** vs Judiciary Strength 3
  - 5 > 3 → **NOT BLOCKED** (only blocked if roll ≤ Strength)
- Executive roll: d6 = **2** vs Executive Strength 3
  - 2 ≤ 3 → **Full Implementation**
- Effects applied: Stability +2, Liberty -1

**Policy 3: Free Trade Agreement**
- No Judiciary review needed
- Executive roll: d6 = **3** vs Executive Strength 3
  - 3 ≤ 3 → **Full Implementation**
- Immediate: Growth +2
- Delayed effect placed on Round 3: Budget +1, Inequality +1

**Timeline Updated:**
```
Round:    1 | 2               | 3                      | 4
Effects:  -- | Border Incident | Public Health,         | Education
            |                 | Free Trade delayed     | delayed
```

### Phase 5: Consequences

**Delayed Effects:** None scheduled for Round 1

**Resource Changes This Round:**
- Budget: 8 → 6 (Education Reform -2)
- Stability: 10 → 12 (Law and Order +2)
- Liberty: 10 → 9 (Law and Order -1)
- Growth: 5 → 7 (Free Trade +2) + Carol's faction bonus +1 = **8**

**Feedback Loop Check:**
- Growth at 8: No automatic trigger (need 2 consecutive rounds at ≥8 for Boom)
- Stability at 12: Above 10 but below 15, no Security State check yet
- All other resources in safe zones

**Market Phase:**
- Event modified: -1 to roll
- Roll d6 = **4** - 1 = **3**
- Market Strength = 3
- 3 ≤ 3 → Growth +1

**Public Opinion Update:**
- Resources generally improved (Stability up, Growth up)
- But Liberty down slightly
- Net: Approval stays at 5 (no dramatic changes)

### Phase 6: Refresh

**Draw Phase:**
- Alice draws 2, discards to 5 (draws: Housing Program, Media Freedom Act)
- Bob draws 2, discards to 5 (draws: Fiscal Responsibility, Emergency Powers)
- Carol draws 2, discards to 5 (draws: Tech Sector Investment, Financial Deregulation)
- David draws 2, discards to 5 (draws: Patriot Act, Infrastructure Investment)

**First Player passes to Bob**

**Collapse Check:** All resources safe

---

### End of Round 1 Summary

| Resource | Value | Change |
|----------|-------|--------|
| Budget | 6 | -2 |
| Legitimacy | 11 | +1 (Alice's faction bonus) |
| Stability | 12 | +2 |
| Growth | 9 | +4 |
| Liberty | 9 | -1 |
| Inequality | 0 | -- |
| Approval | 5 | -- |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 4 | 1 |
| Bob | 3 | 1 |
| Carol | 3 | 1 |
| David | 5 | 0 |

---

## Round 2

### Phase 1: Events

**Events Revealed:**

1. **Corporate Scandal** (Moderate, Immediate)
   - Effect: If Growth > 7, Legitimacy -1

2. **Diplomatic Summit** (Minor, Immediate)
   - Effect: Foreign policy decisions get +1 Legitimacy this round

3. **Housing Crisis Begins** (Moderate, Pending +3)
   - Effect: In 3 rounds if not addressed: Stability -2, Approval -1

4. **Tech Boom** (Minor, Immediate)
   - Effect: Economic policies get +1 Growth effect this round

**Immediate Resolution:**
- Corporate Scandal: Growth is 9 (> 7) → Legitimacy -1 (10 now)
- Tech Boom and Diplomatic Summit: Bonuses noted

**Pending Effect from Round 1 triggers: Border Incident**
- No Security response was passed → Stability -1 (12 → 11)

**Timeline Updated:**
```
Round:  2      | 3                      | 4               | 5
Effects: --    | Public Health,         | Education       | Housing Crisis
               | Free Trade delayed     | delayed         |
```

### Phase 2: Deliberation

> **David:** "We just lost Stability from the Border Incident because we didn't respond. I should have pushed harder for my Security policy."
>
> **Bob:** "Public Health crisis hits next round. Alice, you need to sponsor Healthcare."
>
> **Alice:** "It costs 3 Budget and we're at 6. If I pass it, we're at 3. That's tight."
>
> **Carol:** "But Growth is high. The feedback loop gives us +1 Budget next round if Growth stays above 10."
>
> **Bob:** "Growth is 9, not 10."
>
> **Carol:** "I can fix that. Tech Sector Investment would push us to 11 with the Tech Boom bonus."
>
> **David:** "I'm concerned about Inequality. Free Trade adds +1 next round and Carol's policies keep pushing it up."
>
> **Alice:** "We're at 0 Inequality. We have room. But I want to see some balance - maybe pass my Progressive Taxation eventually."
>
> **David:** "Fine. This round: Healthcare and Tech Investment. I'll save my policy."

**Selected policies:**
- Alice: Universal Healthcare
- Bob: Fiscal Responsibility (Budget +2, delays Social spending)
- Carol: Tech Sector Investment
- David: Passes (saving influence)

### Phase 3: Policy Actions

**First Player: Bob**

---

**Bob's Turn - Sponsors: Fiscal Responsibility**

*Bob pays 2 Influence (now at 1)*

"Fiscal Responsibility: Budget +2 immediately. But all Social policy costs +1 Budget for 3 rounds."

> **Alice:** "What?! That makes my Healthcare cost 4 instead of 3! We can't afford that!"
>
> **Bob:** "We need Budget security. We're at 6 and you want to spend 3."
>
> **Carol:** "This is a trap. Bob, you're sabotaging Alice."
>
> **Bob:** "I'm trying to keep us solvent. Alice can wait one round."
>
> **David:** "The Public Health crisis is next round. We can't wait."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | No | 1 | -2 |
| Bob | Yes | 0 | +1 |
| Carol | No | 0 | -1 |
| David | No | 0 | -1 |

**Result:** Yes: 1, No: 4 → **FAILS**

*Bob's Influence: spent 2 to sponsor, no gain. Now at 1.*

> **Bob (frustrated):** "You're going to regret this when Budget crashes."

---

**Carol's Turn - Sponsors: Tech Sector Investment**

*Carol pays 2 Influence (now at 1)*

"Tech Sector Investment: Budget -1, Growth +2. With Tech Boom: Growth +3 total."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | Abstain | 0 | 0 |
| Carol | Yes | 0 | +1 |
| David | Yes | 0 | +1 |

**Result:** Yes: 3, No: 0 → **PASSES**

*Carol gains +1 Influence (now at 2)*

---

**Alice's Turn - Sponsors: Universal Healthcare**

*Alice pays 2 Influence (now at 2)*

"Universal Healthcare: Budget -3, Legitimacy +2 immediately. Delayed (3 rounds): Inequality -1."

> **Carol:** "Budget at 6-1-3 = 2. That's dangerous."
>
> **Alice:** "But Growth is about to hit 12. The feedback loop will help. And the Health Crisis is coming!"
>
> **David:** "The delayed Inequality reduction is good. I'll support."
>
> **Bob:** "Budget 2 is insane. I'm voting No with all my remaining Influence."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | No | 1 | -2 |
| Carol | Yes | 0 | +1 |
| David | Yes | 1 | +2 |

**Result:** Yes: 4, No: 2 → **PASSES**

*Alice gains +1 Influence (now at 3)*
*Alice gains +1 Legitimacy (faction bonus)*

*Bob now at 0 Influence*

---

**David's Turn - Passes**

"I'm saving my influence. We've passed enough this round."

---

### Phase 4: Implementation

**Policy 1: Tech Sector Investment**
- Executive roll: d6 = **1** → Full implementation
- Effects: Budget -1, Growth +2 (+1 Tech Boom) = Growth +3

**Policy 2: Universal Healthcare**
- No Judiciary review (doesn't reduce Liberty)
- Executive roll: d6 = **5** vs Executive Strength 3
  - 5 > 3 → Partial implementation
- Effects: Budget -3 (full cost), Legitimacy +1 (reduced from +2)
- Delayed placed on Round 5: Inequality -1

**Timeline Updated:**
```
Round:  2      | 3                      | 4               | 5
Effects: --    | Public Health,         | Education       | Housing Crisis,
               | Free Trade delayed     | delayed         | Healthcare delayed
```

### Phase 5: Consequences

**Delayed Effects:** None this round

**Resource Changes:**
- Budget: 6 → 6 - 1 - 3 = 2
- Growth: 9 → 9 + 3 = 12
- Legitimacy: 10 → 10 + 1 (partial) + 1 (Alice bonus) = 12

**Feedback Loop Check:**
- **Growth > 10:** Budget +1 (tax revenue) → Budget 2 → 3
- Growth at 12 for first round (need 2 consecutive for Boom)
- Stability at 11, Liberty at 9: No Security State

**Market Phase:**
- Roll d6 = **6** vs Market Strength 3
- 6 > 3 → Roll 1d3-2 = (roll d6/2 rounded up) **3**, so d3=2, result = 2-2 = **0**
- Growth unchanged

**Approval Update:**
- Legitimacy went up, Growth high: Approval +1 → 6

### Phase 6: Refresh

**Draw and Collapse Check**
- Budget at 3: Above 0, safe
- All other resources safe

**First Player passes to Carol**

---

### End of Round 2 Summary

| Resource | Value | Change |
|----------|-------|--------|
| Budget | 3 | -3 (+1 feedback) |
| Legitimacy | 12 | +2 |
| Stability | 11 | -1 (event) |
| Growth | 12 | +3 |
| Liberty | 9 | -- |
| Inequality | 0 | -- |
| Approval | 6 | +1 |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 3 | 2 |
| Bob | 0 | 1 |
| Carol | 2 | 2 |
| David | 5 | 0 |

> **Observation:** Bob is in a weak position with 0 Influence. He can't sponsor policies and his voting power is minimal. David has been patient, accumulating influence while others spent theirs.

---

## Round 3

### Phase 1: Events

**Events Revealed:**

1. **Banking Instability** (Major, Immediate)
   - Effect: If Budget < 5, roll d6. On 1-2: Budget -2

2. **Environmental Protest** (Moderate, Immediate)
   - Effect: Civil Society strength check. If Strength ≥ 3: Stability -1 unless Green policy passed this round

3. **Pension Crisis** (Moderate, Pending +2)
   - Effect: In 2 rounds: Budget -2 unless addressed

4. **International Investment Opportunity** (Minor, Immediate)
   - Effect: Any Economic policy passed gains +1 Growth effect

**Immediate Resolution:**
- Banking Instability: Budget is 3 (< 5). Roll d6 = **2** → Budget -2! Budget now at 1!
- Environmental Protest: Civil Society is 3 (≥ 3). Need Green policy or Stability -1

**Pending Effects Trigger:**

**Public Health Concern from Round 1:**
- Was Healthcare passed? YES! → Effect negated

**Free Trade Agreement delayed effect:**
- Budget +1, Inequality +1
- Budget: 1 → 2
- Inequality: 0 → 1

**Timeline Updated:**
```
Round:  3      | 4               | 5                    | 6
Effects: --    | Education       | Housing Crisis,      | Pension Crisis
               | delayed         | Healthcare delayed   |
```

### Phase 2: Deliberation

> **Carol:** "Budget at 2! One more hit and we're at collapse risk!"
>
> **Bob:** "I told you. I TOLD you fiscal responsibility mattered."
>
> **Alice:** "We had to pass Healthcare. The crisis would have cost Legitimacy."
>
> **David:** "We need budget repair NOW. Who has something?"
>
> **Carol:** "I have Privatization Program: Budget +2, but Legitimacy -1 and Inequality +1."
>
> **Alice:** "Inequality is at 1, that's fine. But Legitimacy -1 when we're at 12... still safe."
>
> **Bob:** "I can't sponsor anything. I have no influence. But I'll vote."
>
> **David:** "We also need to handle the Environmental Protest or lose Stability."
>
> **Alice:** "I have Green Infrastructure! Budget -2, Growth +1, delayed Growth +1. But we can't afford -2 Budget right now."
>
> **Carol:** "Pass Privatization first, then we can afford Green Infrastructure."

**Selected policies:**
- Alice: Green Infrastructure (if Budget allows)
- Carol: Privatization Program
- David: Infrastructure Investment (Budget -1, Growth +1)

### Phase 3: Policy Actions

**First Player: Carol**

---

**Carol's Turn - Sponsors: Privatization Program**

*Carol pays 2 Influence (now at 0)*

"Privatization Program: Budget +2, Legitimacy -1, Inequality +1"

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | Yes | 0 | +1 |
| Carol | Yes | 0 | +1 |
| David | Yes | 0 | +1 |

**Result:** Yes: 4, No: 0 → **PASSES unanimously**

*Carol gains +1 Influence (now at 1)*

---

**David's Turn - Sponsors: Infrastructure Investment**

*David pays 2 Influence (now at 3)*

"Infrastructure Investment: Budget -1, Growth +1. With event bonus: Growth +2"

> **Alice:** "Wait, I still need to pass Green Infrastructure for the protest!"
>
> **David:** "After Privatization, Budget is 4. My policy makes it 3. Then yours makes it 1. That's too risky."
>
> **Alice:** "Then don't pass yours! Let me handle the protest!"
>
> **David:** "My policy grows the economy. Yours costs more. We need Growth to generate Budget through feedback."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | No | 1 | -2 |
| Bob | Yes | 0 | +1 |
| Carol | Yes | 0 | +1 |
| David | Yes | 1 | +2 |

**Result:** Yes: 4, No: 2 → **PASSES**

*David gains +1 Influence (now at 4)*
*Alice now at 2 Influence*

---

**Alice's Turn - Sponsors: Green Infrastructure**

*Alice pays 2 Influence (now at 0)*

"Green Infrastructure: Budget -2, Growth +1 now, delayed Growth +1"

> **David:** "Budget at 3. This makes it 1. We're one bad event from collapse."
>
> **Carol:** "But the Environmental Protest..."
>
> **Bob:** "If we don't pass it, Stability -1. If we do pass it, Budget risk. Pick your poison."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | No | 0 | -1 |
| Carol | Yes | 0 | +1 |
| David | No | 0 | -1 |

**Result:** Yes: 2, No: 2 → **TIE - FAILS**

*Alice stays at 0 Influence*

> **Alice:** "Great. Now we lose Stability."

**Environmental Protest resolves:** No Green policy passed → Stability -1

---

### Phase 4: Implementation

**Policy 1: Privatization Program**
- Executive roll: d6 = **2** → Full implementation
- Effects: Budget +2, Legitimacy -1, Inequality +1

**Policy 2: Infrastructure Investment**
- Executive roll: d6 = **4** → Partial implementation
- Effects: Budget -1, Growth +1 (reduced from +2 due to partial)

**Resources after implementation:**
- Budget: 2 + 2 - 1 = 3
- Legitimacy: 12 - 1 = 11
- Growth: 12 + 1 = 13
- Inequality: 1 + 1 = 2

### Phase 5: Consequences

**Stability from Environmental Protest:** -1 (11 → 10)

**Feedback Loop Check:**
- **Growth > 10:** Budget +1 → Budget 3 → 4
- **Boom Check:** Growth ≥ 8 for 2nd consecutive round? Yes (12 last round, 13 now)
  - BOOM: Budget +2, Stability -1 (inequality effects)
  - Budget: 4 → 6, Stability: 10 → 9

**Market Phase:**
- Roll d6 = **4** vs Market Strength 3
- 4 > 3 → Roll 1d3-2 = **1** - 2 = -1
- Growth -1 → 12

**Approval Update:** Strong economy but stability dropping → Approval stays at 6

### Phase 6: Refresh

---

### End of Round 3 Summary

| Resource | Value | Change |
|----------|-------|--------|
| Budget | 6 | +4 (policies + feedback + boom) |
| Legitimacy | 11 | -1 |
| Stability | 9 | -2 (protest + boom) |
| Growth | 12 | -1 (market) |
| Liberty | 9 | -- |
| Inequality | 2 | +1 |
| Approval | 6 | -- |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 0 | 2 |
| Bob | 0 | 1 |
| Carol | 1 | 3 |
| David | 4 | 1 |

> **Critical Observation:** Alice and Bob are both at 0 Influence - they cannot sponsor policies! Power has shifted to David (4) and Carol (1). The game's political dynamics have changed dramatically.

---

## Round 4

### Phase 1: Events

**Events Revealed:**

1. **Judicial Reform Proposal** (Major, Immediate)
   - Effect: Players may vote to change Judiciary Strength by +1 or -1

2. **Labor Strike** (Moderate, Immediate)
   - Effect: If Inequality ≥ 2: Stability -1, Growth -1

3. **Foreign Aid Request** (Minor, Choice)
   - Options: A) Give aid: Budget -1, Legitimacy +1 B) Refuse: Legitimacy -1

4. **Media Scandal** (Moderate, Immediate)
   - Effect: Highest Influence player loses 1 Legitimacy. Wait—that's a national resource. [DESIGN NOTE: Should this affect personal Influence instead?]
   - **Revised:** Highest Influence player (David) loses 1 Influence

**Immediate Resolution:**
- Labor Strike: Inequality is 2 (≥ 2) → Stability -1, Growth -1
- Judicial Reform: Vote to modify Judiciary
- Media Scandal: David loses 1 Influence (4 → 3)
- Foreign Aid: Vote needed

**Pending Effects Trigger:**

**Education Reform delayed effect from Round 1:**
- Growth +1, Legitimacy +1 (was +0.5 rounded up from partial implementation)

**Resources after events and delayed effects:**
- Stability: 9 - 1 = 8
- Growth: 12 - 1 + 1 = 12
- Legitimacy: 11 + 1 = 12

**Judicial Reform Vote:**

> **Alice:** "Weakening Judiciary makes it easier to pass Liberty-reducing policies. As a Freedom priority, I vote to strengthen it."
>
> **David:** "I want Order. Strong Judiciary might block Security policies. I vote to weaken it."
>
> **Carol:** "Neutral on this."
>
> **Bob:** "Institutions are my priority. Strengthen."

**Vote:** Strengthen: 2, Weaken: 1, Abstain: 1 → Judiciary +1 (now Strength 4)

**Foreign Aid Vote:**

**Vote:** Give aid wins (Alice, Carol, Bob) → Budget -1, Legitimacy +1
- Budget: 6 - 1 = 5
- Legitimacy: 12 + 1 = 13

### Phase 2: Deliberation

> **David:** "Alice and Bob, you can't do anything without Influence. You need us."
>
> **Alice:** "I get +1 Influence if I'm on the winning side of a contested vote. Help me get some back."
>
> **Carol:** "The Pension Crisis hits in 2 rounds. We need Budget policies."
>
> **David:** "I have Defense Contracts: Budget -2, Stability +1, Growth +1. The Stability helps."
>
> **Bob:** "I still have Tax Cuts: Budget -2, Growth +1, Inequality +1."
>
> **Carol:** "Both cost Budget and we're at 5. What gains Budget?"
>
> **David:** "I could sponsor Patriot Act but it's Security and reduces Liberty by 2. Judiciary might block it now that it's Strength 4."

### Phase 3: Policy Actions

**First Player: David** (passed from Carol)

---

**David's Turn - Sponsors: Defense Contracts**

*David pays 2 Influence (now at 1)*

"Defense Contracts: Budget -2, Stability +1, Growth +1"

> **Alice:** "Stability is at 8. This helps. I'll vote Yes."
>
> **Bob:** "I'll support too."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Alice | Yes | 0 | +1 |
| Bob | Yes | 0 | +1 |
| Carol | Yes | 0 | +1 |
| David | Yes | 0 | +1 |

**Result:** Yes: 4, No: 0 → **PASSES**

*David gains +1 Influence (now at 2)*
*David gains +1 Stability (Nationalist faction bonus)*

---

**Alice's Turn - Cannot sponsor (0 Influence)**

> **Alice:** "I hate this. I just have to watch."

---

**Bob's Turn - Cannot sponsor (0 Influence)**

> **Bob:** "Same. We need contested votes to gain Influence."

---

**Carol's Turn - Sponsors: Financial Deregulation**

*Carol pays 2 Influence (now at -1? Can't go negative)*

**WAIT - Carol only has 1 Influence. Cannot sponsor!**

> **Carol:** "I... can't afford to sponsor either. I only have 1."

---

**Only 1 policy passes this round.**

### Phase 4: Implementation

**Policy 1: Defense Contracts**
- Executive roll: d6 = **3** → Full implementation
- Effects: Budget -2, Stability +1, Growth +1 (+1 David bonus = +2 Stability total)

**Resources after implementation:**
- Budget: 5 - 2 = 3
- Stability: 8 + 2 = 10
- Growth: 12 + 1 = 13

### Phase 5: Consequences

**Feedback Loops:**
- Growth > 10: Budget +1 → 4
- Boom continues (3rd round): Budget +2, Stability -1 → Budget 6, Stability 9

**Market Phase:**
- Roll d6 = **5** → 5 > 3, roll d3-2 = **2** - 2 = 0
- Growth unchanged at 13

**Inequality Check:**
- Inequality at 2, Stability at 9: No crisis yet

### Phase 6: Refresh

**Influence from being on winning side:**
- Alice: Was on winning side of Defense Contracts vote → +1 Influence (now at 1)
- Bob: Same → +1 Influence (now at 1)

---

### End of Round 4 Summary

| Resource | Value | Change |
|----------|-------|--------|
| Budget | 6 | +1 |
| Legitimacy | 13 | +1 |
| Stability | 9 | +1 |
| Growth | 13 | +1 |
| Liberty | 9 | -- |
| Inequality | 2 | -- |
| Approval | 6 | -- |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 1 | 2 |
| Bob | 1 | 1 |
| Carol | 1 | 3 |
| David | 2 | 2 |

---

## Round 5 (Critical Round)

### Phase 1: Events

**Events Revealed:**

1. **Economic Bubble Warning** (Major, Pending +2)
   - Effect: In 2 rounds, if Growth > 12: Roll d6. On 1-3: Growth -4, Stability -2

2. **Constitutional Crisis** (Crisis, Immediate)
   - Effect: All players must vote: Support Constitution (Judiciary +1, Liberty +1) or Reject (Judiciary -2)

3. **Pandemic Outbreak** (Major, Immediate)
   - Effect: Stability -2, Budget -1 unless Healthcare policy exists
   - Healthcare was passed in Round 2! Effect: Stability -1 only

4. **Energy Crisis** (Moderate, Immediate)
   - Effect: Growth -2 unless Industrial/Infrastructure policy exists
   - Infrastructure Investment passed in Round 3! Effect negated

**Immediate Resolution:**
- Pandemic: Stability -1 (Healthcare mitigates)
- Constitutional Crisis: Vote needed

**Pending Effects Trigger:**

**Housing Crisis from Round 2:**
- Not addressed → Stability -2, Approval -1

**Healthcare delayed effect:**
- Inequality -1 → Inequality: 2 → 1

**Resources after events:**
- Stability: 9 - 1 - 2 = 6
- Approval: 6 - 1 = 5
- Inequality: 1

**Constitutional Crisis Vote:**

> **Alice:** "Support Constitution! Liberty and Judiciary up!"
>
> **David:** "This is actually good. Strong institutions help everyone."
>
> **Bob:** "Finally, something for my Institutions legacy. Support!"

**Vote:** Support: 4, Reject: 0 → Judiciary +1 (now 5), Liberty +1 (now 10)

### Phase 2: Deliberation

> **Alice:** "Stability at 6! That's close to the danger zone. We need stabilization."
>
> **Bob:** "And Pension Crisis is still coming next round."
>
> **David:** "I have Patriot Act: Stability +2, Liberty -2. But Judiciary is now at 5. It'll almost certainly block it."
>
> **Carol:** "Liberty just went to 10. A -2 puts us at 8. Judiciary roll would need 6 to pass (only fails on roll ≤ 5). That's only 17% chance of passing."
>
> **David:** "Too risky. What else stabilizes?"
>
> **Bob:** "My Law and Order is already used. Traditional Values Act: Stability +1, Liberty -1, Legitimacy +1."
>
> **Alice:** "Liberty -1 is a Judiciary check. Roll needs to beat 5. 33% chance of blocking."

### Phase 3: Policy Actions

**First Player: Alice**

---

**Alice sponsors: Progressive Taxation**

*Alice pays 1 Influence (wait, needs 2 to sponsor)*

**Cannot sponsor with only 1 Influence!**

> **Alice:** "Ugh. Still stuck."

---

**Bob sponsors: Cannot (1 Influence, needs 2)**

---

**Carol sponsors: Cannot (1 Influence, needs 2)**

---

**David sponsors: Sovereignty Protection**

*David pays 2 Influence (now at 0)*

"Sovereignty Protection: Stability +1, Liberty -1"

**Judiciary Check Required**

**Voting first:**
| Player | Vote | Total |
|--------|------|-------|
| Alice | Yes | +1 |
| Bob | Yes | +1 |
| Carol | Yes | +1 |
| David | Yes | +1 |

**Result:** PASSES

**Judiciary Review:** Roll d6 = **4** vs Judiciary Strength 5
- 4 ≤ 5 → **BLOCKED!**

> **David:** "The Judiciary blocked my policy! The institution we just strengthened stopped me!"

*Sovereignty Protection is blocked. No effect.*

*David loses his 2 Influence spent, gains nothing.*

---

### Phase 4: Implementation

No policies implemented this round (only one sponsored, and it was blocked).

### Phase 5: Consequences

**Feedback Loops:**
- Growth > 10: Budget +1 → 7
- Boom (4th consecutive round): Budget +2, Stability -1 → Budget 9, Stability 5

**ALERT: Stability at 5!**
- Legitimacy -1 (Stability < 5? No, it's exactly 5. Rule says "< 5" so not triggered)
- But close to danger!

**Market Phase:**
- Roll d6 = **1** → 1 ≤ 3, Growth +1 → 14

**Approval:** Stability dropping, but Legitimacy high → Approval stays at 5

### Phase 6: Refresh

**All players draw 2 cards**

**Influence recovery:**
- Passive: None gained this round (no winning votes on contested policies)
- David at 0, everyone else at 1

---

### End of Round 5 Summary

| Resource | Value | Change | Alert |
|----------|-------|--------|-------|
| Budget | 9 | +3 | |
| Legitimacy | 13 | -- | |
| Stability | 5 | -4 | DANGER! |
| Growth | 14 | +1 | |
| Liberty | 10 | +1 (Constitution) | |
| Inequality | 1 | -1 | |
| Approval | 5 | -- | |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 1 | 2 |
| Bob | 1 | 1 |
| Carol | 1 | 3 |
| David | 0 | 2 |

> **CRISIS:** Stability is at 5. One more drop and feedback loops kick in hard. If it hits 2, game over!

---

## Round 6 (Survival Round)

### Phase 1: Events

**Pension Crisis triggers (from Round 3):**
- Budget -2 → 9 - 2 = 7

**Events Revealed:**

1. **Civil Unrest** (Major, Immediate)
   - Effect: If Stability ≤ 5: Stability -1, draw another Crisis event

2. **International Markets Crash** (Crisis, Immediate)
   - Effect: Growth -3, Budget -1

3. **Populist Movement** (Moderate, Immediate)
   - Effect: If Inequality ≥ 3 OR Approval ≤ 4: Legitimacy -2. Otherwise no effect.
   - Inequality 1, Approval 5 → No effect

4. **Government Efficiency Drive** (Minor, Immediate)
   - Effect: Executive Strength +1 for this round

**Economic Bubble Warning (from Round 5) placed on timeline for Round 7**

**Immediate Resolution:**
- Civil Unrest: Stability is 5 (≤ 5) → Stability -1 → **4**
  - Draw another Crisis: **Mass Protests** - Stability -1 if Liberty < 10
  - Liberty is 10, not < 10 → No additional effect
- Markets Crash: Growth -3 → 11, Budget -1 → 6

**Resources after events:**
- Stability: 4 (CRITICAL!)
- Growth: 11
- Budget: 6

### Phase 2: Deliberation

> **Bob:** "Stability at 4! We're two points from collapse!"
>
> **David:** "I can't sponsor anything. I'm at 0 Influence."
>
> **Alice:** "Neither can I effectively. Only 1 Influence."
>
> **Carol:** "Same. We're all nearly broke."
>
> **Bob:** "The only way to get Influence fast is... wait. 3 Influence to 'Force a policy to vote.' We don't have that."
>
> **Alice:** "There must be something. What gives Influence?"
>
> **David:** "+2 for predicting a crisis outcome. But that's not helpful now."
>
> **Carol:** "We're stuck. Unless we just pass whatever David proposes and rebuild from there?"
>
> **David:** "I CAN'T propose. I have ZERO Influence!"

**The table realizes: With David at 0 and everyone else at 1, NO ONE can sponsor a policy (costs 2).**

> **Bob:** "This is a design problem. We're gridlocked with no way to recover."

### Design Note Intervention

> **[PLAYTEST OBSERVATION]:** The game has reached a state where no player can sponsor policies. This reveals a potential design flaw - there needs to be a passive Influence recovery mechanism or alternative sponsorship rules.
>
> **Proposed House Rule for This Simulation:** At the start of each round, each player gains +1 Influence (simulating natural political capital regeneration). Retroactively applying:
> - Alice: 1 → 2
> - Bob: 1 → 2
> - Carol: 1 → 2
> - David: 0 → 1

**Continuing with house rule applied...**

### Phase 3: Policy Actions

**First Player: Bob**

---

**Bob sponsors: Law and Order Initiative** (from new hand - assuming he drew it again)

Actually, Bob already passed this in Round 1. Let's use: **Border Security**

*Bob pays 2 Influence (now at 0)*

"Border Security: Budget -1, Stability +1"

**Voting:**
Everyone votes Yes (desperate situation)

**Result:** PASSES

*Bob gains +1 Influence (now at 1)*

---

**Carol sponsors: Small Business Support**

*Carol pays 2 Influence (now at 0)*

"Small Business Support: Budget -1, Growth +1"

> **David:** "We need Stability, not Growth!"
> **Carol:** "Growth keeps Budget flowing through feedback. Trust me."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Alice | No | -1 |
| Bob | No | -1 |
| Carol | Yes | +1 |
| David | No | -1 |

**Result:** FAILS

---

**Alice sponsors: Workers' Rights Act**

*Alice pays 2 Influence (now at 0)*

"Workers' Rights Act: Liberty +1, Growth -1"

> **Bob:** "We can't afford Growth -1!"

**Voting:**
All No except Alice → FAILS

---

**David - Cannot sponsor (only 1 Influence)**

---

### Phase 4: Implementation

**Border Security:**
- No Judiciary review (doesn't reduce Liberty)
- Executive roll: d6 = **2** (with +1 from Efficiency Drive = **3**) → Full implementation
- Effects: Budget -1 → 5, Stability +1 → 5

### Phase 5: Consequences

**Stability at 5 - Check:**
- If Stability < 5: Legitimacy -1. Stability is exactly 5. Not triggered.

**Feedback Loops:**
- Growth at 11 > 10: Budget +1 → 6
- Boom (5th round): Budget +2, Stability -1 → Budget 8, Stability 4

**STABILITY AT 4!**

**New trigger: Stability < 5 → Legitimacy -1 → 12**

**Market Phase:**
- Roll: 3 ≤ 3 → Growth +1 → 12

---

### End of Round 6 Summary

| Resource | Value | Change | Alert |
|----------|-------|--------|-------|
| Budget | 8 | +2 | |
| Legitimacy | 12 | -1 | |
| Stability | 4 | -1 | CRITICAL! |
| Growth | 12 | +1 | |
| Liberty | 10 | -- | |
| Inequality | 1 | -- | |
| Approval | 5 | -- | |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 0 | 2 |
| Bob | 1 | 2 |
| Carol | 0 | 3 |
| David | 1 | 2 |

---

## Round 7 (Make or Break)

### Applying House Rule: All players +1 Influence

- Alice: 0 → 1
- Bob: 1 → 2
- Carol: 0 → 1
- David: 1 → 2

### Phase 1: Events

**Economic Bubble Warning triggers:**
- Growth is 12 (> 12? No, 12 is not > 12)
- Condition not met, no effect!

**Events Revealed:**

1. **Unity Government Proposal** (Major, Immediate)
   - Effect: All players may agree to form coalition. If unanimous: All gain +2 Influence, Stability +2

2. **Agricultural Boom** (Minor, Immediate)
   - Effect: Growth +1, Budget +1

3. **Terrorist Threat** (Major, Pending +1)
   - Effect: Next round if no Security response: Stability -3!

4. **Healthcare Workers Strike** (Moderate, Immediate)
   - Effect: If Universal Healthcare active: Legitimacy -1. If not: Stability -1
   - Healthcare is active → Legitimacy -1 → 11

**Unity Government Vote:**

> **Alice:** "We need this. +2 Stability would save us!"
> **Everyone:** "Agreed!"

**Unanimous approval:** All +2 Influence, Stability +2

**Resources:**
- Stability: 4 + 2 = 6
- Growth: 12 + 1 = 13
- Budget: 8 + 1 = 9

**Influence after Unity:**
- Alice: 1 + 2 = 3
- Bob: 2 + 2 = 4
- Carol: 1 + 2 = 3
- David: 2 + 2 = 4

### Phase 2: Deliberation

> **Alice:** "We're back in the game! Stability at 6, everyone has Influence."
>
> **David:** "But Terrorist Threat next round. We NEED a Security policy now."
>
> **Bob:** "I have Emergency Powers: Stability +3, Liberty -2. It's extreme."
>
> **Carol:** "Liberty at 10 - 2 = 8. Judiciary at 5. That's almost guaranteed to be blocked."
>
> **David:** "What about Military Expansion? Stability +2, Budget -3, no Liberty hit."
>
> **Bob:** "Budget 9 - 3 = 6. Manageable."

### Phase 3: Policy Actions

**Bob sponsors: Military Expansion**

*Bob pays 2 Influence (now at 2)*

"Military Expansion: Budget -3, Stability +2"

**Voting:**
All Yes → PASSES

*Bob gains +1 Influence (now at 3)*
*Bob gains +1 Stability (Conservative blocking rapid change? Actually this is Security, David's bonus)*

Wait - this is a Security policy, so David gets +1 Stability (Nationalist bonus).

*David's faction bonus: Stability +1 when passing Security policies*

**Resources:** Stability +2 + 1 = +3 → 6 + 3 = 9

---

**David sponsors: National Security Act**

*David pays 2 Influence (now at 2)*

"National Security Act: Stability +2, Liberty -2, requires Judiciary review"

> **Alice:** "Liberty -2 is risky with Judiciary at 5."
> **Carol:** "But we need every point of Stability we can get."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Alice | No | -1 |
| Bob | Yes | +1 |
| Carol | Yes | +1 |
| David | Yes | +1 |

**Result:** PASSES

**Judiciary Review:** Roll d6 = **6** vs Judiciary Strength 5
- 6 > 5 → **NOT BLOCKED!**

*David gains +1 Influence (now at 3)*
*David's faction bonus: +1 Stability*

**Resources:** Stability +2 +1 = +3 → 9 + 3 = 12, Liberty -2 → 8

---

**Carol sponsors: Deregulation Act**

*Carol pays 2 Influence (now at 1)*

"Deregulation Act: Growth +2, Liberty +1, delayed Stability -1"

**Voting:**
All Yes (Growth is good, Liberty recovery) → PASSES

*Carol gains +1 Influence (now at 2)*

---

### Phase 4: Implementation

All policies implemented with Executive rolls...

**Final Resources after Round 7:**
- Budget: 9 - 3 = 6
- Stability: 6 + 3 + 3 = 12
- Liberty: 10 - 2 + 1 = 9
- Growth: 13 + 2 = 15 (CAPPED at 15)

### Phase 5: Consequences

**Stability back above 10 - feedback loops stabilized**

**Growth at cap:** Budget feedback still applies. Budget +1 → 7

---

### End of Round 7 Summary

| Resource | Value | Change |
|----------|-------|--------|
| Budget | 7 | -2 |
| Legitimacy | 11 | -1 |
| Stability | 12 | +8! |
| Growth | 15 | +3 (cap) |
| Liberty | 9 | -1 |
| Inequality | 1 | -- |
| Approval | 6 | +1 |

| Player | Influence | Policies Passed |
|--------|-----------|-----------------|
| Alice | 3 | 2 |
| Bob | 3 | 3 |
| Carol | 2 | 4 |
| David | 3 | 3 |

---

## Round 8 (Final Round - Game End Check)

The rules state game can end at Round 8+ with 4 players. Let's check endgame conditions.

### Phase 1: Events

**Terrorist Threat triggers:**
- Security response passed (Military Expansion, National Security Act) → Effect negated!

**Deregulation delayed effect triggers:**
- Stability -1 → 11

### Final State Check

No collapse conditions:
- Budget 7 > 0 ✓
- Legitimacy 11 > 2 ✓
- Stability 11 > 2 ✓
- Liberty 9 > 3 ✓
- No Revolution (Inequality 1, Stability 11)

**THE NATION SURVIVES! Proceed to scoring.**

---

## Final Scoring

### Final Resource Values

| Resource | Final Value |
|----------|-------------|
| Budget | 7 |
| Legitimacy | 11 |
| Stability | 11 |
| Growth | 15 |
| Liberty | 9 |
| Inequality | 1 |
| Approval | 6 |

### Institution Strengths

| Institution | Final Strength |
|-------------|----------------|
| Legislature | 3 |
| Judiciary | 5 |
| Executive | 3 |
| Markets | 3 |
| Public Opinion | 3 |
| Civil Society | 3 |

### Legacy Scoring

**Alice (Priorities: Equality, Freedom)**
- Equality: Inequality ≤ 3 → +3 points
- Freedom: Liberty above 10? No (9). 0 points
- Bonus: Predicted Approval? No
- Bonus: Most policies? No (Carol has most)
- Bonus: Never broke deal? Yes → +2 points
- **Alice Total: 5 points**

**Bob (Priorities: Order, Institutions)**
- Order: Stability above 10 → +1 per point = 11-10 = +1 point
- Institutions: Institutions at Strength 4+ → Judiciary (5) = +1 point
- Bonus: Most policies? No
- Bonus: Never broke deal? Yes → +2 points
- **Bob Total: 4 points**

**Carol (Priorities: Prosperity, Influence)**
- Prosperity: Growth above 5 = 15-5 = +10 points, Budget above 10? No (7). 0 extra.
- Influence: 2 remaining / 3 = 0 points (rounded down)
- Bonus: Most policies passed (4) → +3 points
- Bonus: Never broke deal? Yes → +2 points
- **Carol Total: 15 points**

**David (Priorities: Order, Prosperity)**
- Order: Stability above 10 = 11-10 = +1 point
- Prosperity: Growth above 5 = +10 points
- Bonus: Never broke deal? Yes → +2 points
- **David Total: 13 points**

---

## Final Results

| Place | Player | Faction | Points | Key Strategy |
|-------|--------|---------|--------|--------------|
| 1st | **Carol** | Liberals | 15 | Focused on Growth, passed most policies |
| 2nd | David | Nationalists | 13 | Growth + Order combo, Security specialist |
| 3rd | Alice | Progressives | 5 | Equality priority paid off, Freedom didn't |
| 4th | Bob | Conservatives | 4 | Strong institutions, but order gave few points |

---

## Post-Game Analysis

### What Worked Well

1. **Semi-cooperative tension**: Players had to balance survival (collective) with scoring (individual)
2. **Feedback loops created urgency**: The Stability crisis in Rounds 5-6 forced cooperation
3. **Delayed effects created anticipation**: Players could see threats coming
4. **Influence economy created meaningful scarcity**: Running out of Influence was devastating

### Design Issues Identified

1. **Influence Starvation (CRITICAL)**
   - In Rounds 5-6, all players were at or near 0 Influence
   - No passive recovery mechanism meant gridlock
   - **Recommendation**: Add +1 Influence per round passive gain, or reduce sponsor cost to 1

2. **Boom Feedback Loop Imbalance**
   - Boom gives Budget +2 but also Stability -1
   - Extended booms nearly caused collapse
   - **Recommendation**: Consider capping boom duration or reducing Stability penalty

3. **Legacy Scoring Variance**
   - Prosperity (Growth) gave 10 points; Order (Stability) gave 1 point
   - This seems imbalanced
   - **Recommendation**: Adjust thresholds or scoring curves

4. **Judiciary Blocking Randomness**
   - David's policy blocked purely by dice luck felt frustrating
   - **Recommendation**: Consider alternative mechanics (spend Influence to override?)

5. **Faction Bonuses Underutilized**
   - Bonuses only triggered 3-4 times all game
   - **Recommendation**: Make faction bonuses more impactful or frequent

### Memorable Moments

- **Round 3**: Banking crisis nearly caused collapse, saved by Privatization
- **Round 5**: Constitutional Crisis vote that strengthened Judiciary, which then blocked David
- **Round 6**: Gridlock crisis - the "we can't do anything" moment
- **Round 7**: Unity Government saved the game

---

## Appendix: Turn-by-Turn Resource Tracking

| Round | Budget | Legitimacy | Stability | Growth | Liberty | Inequality | Approval |
|-------|--------|------------|-----------|--------|---------|------------|----------|
| Start | 8 | 10 | 10 | 5 | 10 | 0 | 5 |
| 1 | 6 | 11 | 12 | 9 | 9 | 0 | 5 |
| 2 | 3 | 12 | 11 | 12 | 9 | 0 | 6 |
| 3 | 6 | 11 | 9 | 12 | 9 | 2 | 6 |
| 4 | 6 | 13 | 9 | 13 | 9 | 2 | 6 |
| 5 | 9 | 13 | 5 | 14 | 10 | 1 | 5 |
| 6 | 8 | 12 | 4 | 12 | 10 | 1 | 5 |
| 7 | 7 | 11 | 12 | 15 | 9 | 1 | 6 |
| 8 | 7 | 11 | 11 | 15 | 9 | 1 | 6 |

---

*End of Sample Game Simulation #1*
*Version 1.0 - Ready for design discussion*
