# Sample Game Simulation #2: Five Factions - The Art of the Deal

> **Purpose:** This simulation focuses on negotiations, coalition-building, deal-making, and the dramatic consequences of breaking promises. Designed to explore the social dynamics that make political games memorable.

---

## How to Read This Simulation

This document uses specific formatting to make game actions explicit and easy to follow:

### Formatting Legend

| Symbol/Format | Meaning |
|---------------|---------|
| `⚙️ ACTION:` | A concrete game action (card draw, spending Influence, dice roll) |
| `🎴 CARD:` | Card drawn or played with full details |
| `💰 COST:` | Resources spent (Influence, Budget) |
| `📊 STATE:` | Current resource snapshot |
| `🎲 ROLL:` | Dice roll with result |
| `📋 WHY:` | Strategic reasoning explanation |
| `💬 DIALOGUE:` | Player conversation (roleplay) |
| `📝 DEAL:` | Formal deal recorded |
| `✓ HONORED` / `✗ BROKEN` | Deal outcome |
| `→` | Resource change direction |

### Game Flow Reminder

Each round follows these phases:
1. **Events** - Draw events (1 per player), resolve immediate ones
2. **Deliberation** - Negotiate, form coalitions, plan
3. **Policy Actions** - Sponsor (2 Inf) → Vote → Resolve
4. **Implementation** - Judiciary review, Executive roll
5. **Consequences** - Feedback loops, Market roll
6. **Refresh** - Draw 2 policies, discard to 5, pass First Player

### Starting Hands

Each player begins with **5 Policy Cards** drawn randomly. Cards shown below are what each player holds at game start.

---

## Setup

### Players and Factions

| Player | Faction | Influence | Bonus | Personality |
|--------|---------|-----------|-------|-------------|
| **Anna** | The Progressives | 5 | +1 Legitimacy on Social policies | Idealistic, principled |
| **Bruno** | The Conservatives | 5 | +1 Stability when blocking rapid change | Pragmatic, cautious |
| **Clara** | The Liberals | 5 | +1 Growth on Economic deregulation | Opportunistic, flexible |
| **Diego** | The Nationalists | 5 | +1 Stability on Security policies | Aggressive, transactional |
| **Elena** | The Populists | 5 | +1 Legitimacy when opposing institutional policies | Unpredictable, anti-establishment |

### Secret Legacy Priorities

| Player | Priority 1 | Priority 2 | Hidden Agenda |
|--------|------------|------------|---------------|
| Anna | Equality | Freedom | Minimize Inequality, maximize Liberty |
| Bruno | Institutions | Order | Strengthen institutions, maintain Stability |
| Clara | Prosperity | Influence | Maximize Growth, hoard political capital |
| Diego | Order | Prosperity | Stability + economic growth |
| Elena | Equality | Influence | Anti-elite, accumulate power |

### Starting National Resources

| Resource | Value | | Resource | Value |
|----------|-------|-|----------|-------|
| Budget | 8 | | Liberty | 10 |
| Legitimacy | 10 | | Inequality | 0 |
| Stability | 10 | | Approval | 5 |
| Growth | 5 | | | |

### Starting Institutional Strength

| Institution | Strength | Function |
|-------------|----------|----------|
| Legislature | 3 | Simple majority needed to pass policies |
| Judiciary | 3 | Roll d6; blocked if roll ≤ Strength AND policy reduces Liberty |
| Executive | 3 | Roll d6; full implementation if roll ≤ Strength |
| Markets | 3 | Generates Growth; higher = more stable |
| Public Opinion | 3 | Approval 5; if <3, governing faction loses 1 Inf/round |
| Civil Society | 3 | If ≥4 and controversial policy, trigger Backlash |

### ⚙️ ACTION: Initial Card Draw (5 cards per player)

Each player draws 5 Policy Cards from shuffled deck:

**Anna (Progressives) - Starting Hand:**
```
🎴 1. Education Reform [Social] - Budget -2, delayed: Growth +2, Legitimacy +1
🎴 2. Universal Healthcare [Social] - Budget -4, Legitimacy +2, delayed: Stability +1
🎴 3. Progressive Taxation [Economic] - Budget +2, Growth -1, Inequality -1
🎴 4. Community Policing Reform [Security] - Liberty +1, Legitimacy +1
🎴 5. Media Freedom Act [Institutional] - Liberty +2, Stability -1
```

**Bruno (Conservatives) - Starting Hand:**
```
🎴 1. Law and Order Initiative [Security] - Stability +2, Liberty -1
🎴 2. Fiscal Responsibility [Economic] - Budget +2, Social costs +1 for 3 rounds
🎴 3. Constitutional Amendment [Institutional] - Judiciary +1, Legislature +1, Budget -2
🎴 4. Austerity Measures [Economic] - Budget +3, delayed: Legitimacy -2
🎴 5. Budget Stabilization [Economic] - Budget +1, Growth +1
```

**Clara (Liberals) - Starting Hand:**
```
🎴 1. Free Trade Agreement [Foreign] - Growth +2, delayed: Budget +1, Inequality +1
🎴 2. Deregulation Act [Economic] - Growth +2, Liberty +1, delayed: Stability -1
🎴 3. Tech Sector Investment [Economic] - Budget -1, Growth +2
🎴 4. Privatization Program [Economic] - Budget +2, Legitimacy -1, Inequality +1
🎴 5. Trade Agreement [Foreign] - Growth +1, delayed: Growth +1, Stability -1
```

**Diego (Nationalists) - Starting Hand:**
```
🎴 1. Industrial Policy [Economic] - Budget -2, Growth +1, Stability +1
🎴 2. National Security Act [Security] - Stability +2, Liberty -2, requires Judiciary
🎴 3. Defense Contracts [Security] - Budget -2, Stability +1, Growth +1
🎴 4. Border Securitization [Foreign] - Stability +1, delayed: Liberty -1, Growth -1
🎴 5. Military Modernization [Security] - Budget -4, Stability +1
```

**Elena (Populists) - Starting Hand:**
```
🎴 1. Wealth Redistribution [Social] - Budget -1, Inequality -2, Growth -1
🎴 2. Anti-Corruption Commission [Institutional] - Legitimacy +1, Budget -1, Judiciary +1
🎴 3. Workers' Rights Act [Social] - Liberty +1, Growth -1
🎴 4. Housing Subsidy Program [Social] - Budget -2, Legitimacy +1, Stability +1
🎴 5. Electoral Reform [Institutional] - Legitimacy +2, Legislature +1
```

> **📋 WHY these hands matter:** Each player's hand shapes their options. Anna has strong Social cards aligned with her Equality priority. Clara has Growth-focused Economic cards matching her Prosperity priority. Diego has Security cards but needs allies to pass them. Elena has redistributive cards but they often hurt Growth, creating conflict with Clara.

### Deal Tracking Board

Throughout this game, we'll track all deals made and their outcomes:

```
┌─────────────────────────────────────────────────────────────┐
│                    DEAL REGISTRY                            │
├──────┬─────────────────────────────┬────────┬───────────────┤
│ Round│ Deal                        │ Status │ Consequence   │
├──────┼─────────────────────────────┼────────┼───────────────┤
│      │                             │        │               │
└──────┴─────────────────────────────┴────────┴───────────────┘
```

---

## Round 1: First Alliances

> **First Player:** Anna (Progressives) - determined randomly at game start

### Phase 1: Events

**⚙️ ACTION: Draw 5 Event Cards (1 per player)**

The deck is shuffled. Anna (First Player) draws 5 cards and places them face-up:

```
🎴 EVENT 1: Coalition Formation Pressure [IMMEDIATE]
   "Political instability demands action. A governing coalition must form."
   Effect: First Player declares coalition of 2-3 players. Members: +1 Influence each.

🎴 EVENT 2: Economic Downturn Warning [PENDING +2 rounds]
   "Economists warn of coming recession."
   Effect: In Round 3: Growth -2 unless any Economic policy passed before then.
   ➡️ Place marker on Round 3 of Timeline

🎴 EVENT 3: Border Tensions [PENDING +1 round]
   "Neighboring disputes threaten regional stability."
   Effect: In Round 2: Stability -1 unless Security policy passed.
   ➡️ Place marker on Round 2 of Timeline

🎴 EVENT 4: Civil Rights Movement [IMMEDIATE]
   "Citizens demand expanded freedoms."
   Effect: If Liberty < 10: Legitimacy -1
   ➡️ Check: Liberty = 10. Condition NOT met. No effect.

🎴 EVENT 5: Corruption Scandal [IMMEDIATE]
   "Media exposes minor government corruption."
   Effect: Lowest Influence player gains +1 Influence (public sympathy)
   ➡️ Check: All players at 5 Influence. No lowest. No effect.
```

**📊 TIMELINE after Events:**
```
Round 1 (now) | Round 2      | Round 3           | Round 4+
-------------|--------------|-------------------|----------
             | Border       | Economic Downturn |
             | Tensions     | Warning           |
```

**⚙️ ACTION: Resolve Coalition Formation Pressure (Immediate Event)**

Anna must now declare a governing coalition. This triggers negotiation:

**Coalition Formation - The First Big Negotiation:**

> 💬 **Anna (First Player):** "I need to form a governing coalition. Who wants in?"

> 💬 **Diego:** "I'll join if you promise to support a Security policy for the border tensions."

> **📋 WHY Diego offers this:** Diego's hand contains National Security Act (Stability +2, Liberty -2). The Border Tensions event gives him leverage - he can offer to solve it but wants coalition membership and guaranteed support.

> 💬 **Anna:** "Security usually hurts Liberty. That's against my principles."

> **📋 WHY Anna refuses:** Anna's Freedom priority (maximize Liberty) conflicts with most Security policies. National Security Act would cost -2 Liberty, directly hurting her final score.

> 💬 **Diego:** "Then find someone else. But good luck passing anything without votes."

> 💬 **Clara:** "I'll join your coalition, Anna. I just want Economic policies to pass. I won't demand anything ideological."

> **📋 WHY Clara is flexible:** Clara's Prosperity priority just needs Growth. She doesn't care *how* it happens. Her hand has Free Trade (+2 Growth) and Deregulation (+2 Growth). She needs allies to pass these.

> 💬 **Bruno:** "I'm interested too. I want institutional stability. If you promise not to weaken the Judiciary, I'm in."

> **📋 WHY Bruno wants Judiciary protection:** Bruno's Institutions priority scores +1 per Institution at Strength 4+. He doesn't want Judiciary weakened below 3, and eventually wants it strengthened.

> 💬 **Elena:** "Coalition governments are just elite power-sharing. Count me out. I'll be the opposition."

> **📋 WHY Elena refuses:** Elena's Populist faction bonus is "+1 Legitimacy when opposing institutional policies." Being in opposition lets her score this bonus repeatedly. Also, her anti-establishment personality fits the outsider role.

> 💬 **Anna:** "Okay. Clara and Bruno - we're the governing coalition."

---

**📝 DEAL #1 RECORDED: Coalition Agreement**

| Aspect | Terms |
|--------|-------|
| **Parties** | Anna (lead), Clara, Bruno |
| **Anna promises** | No policies weakening Judiciary |
| **Clara promises** | Support Anna's Social policies when sponsored |
| **Bruno promises** | General coalition support on votes |
| **Duration** | Until broken or game end |
| **Exit clause** | None specified (this will cause problems later) |

**⚙️ ACTION: Coalition Bonus Applied**

```
Anna:  5 Influence + 1 (coalition) = 6 Influence
Bruno: 5 Influence + 1 (coalition) = 6 Influence
Clara: 5 Influence + 1 (coalition) = 6 Influence
Diego: 5 Influence (not in coalition)
Elena: 5 Influence (not in coalition)
```

### Phase 2: Deliberation

> **⏱️ TIME:** 5 minutes maximum for open negotiation

> 💬 **Diego:** "So the three of you run everything now? That's 3 votes automatically. You only need simple majority."

> **📋 WHY this matters:** With Legislature Strength at 3, simple majority wins. Coalition has 3 players = 3 base votes. Diego and Elena have 2 base votes combined. Coalition can pass anything without opposition support.

> 💬 **Elena:** "We'll see how long that lasts. Coalitions always break."

> 💬 **Anna:** "Let's focus. Border tensions hit next round. We need a plan."

> **📋 SITUATION ANALYSIS:** Border Tensions (Round 2) will cause Stability -1 unless a Security policy passes. Current Stability is 10. Dropping to 9 isn't critical, but the coalition wants to appear competent.

> 💬 **Bruno:** "I have Law and Order Initiative: Stability +2, Liberty -1. It's Security-adjacent."

> **📋 WHY Bruno proposes this:** Bruno reveals card from his hand. Law and Order is a Security policy, satisfying the Border Tensions condition, but has lower Liberty cost (-1) than Diego's options.

> 💬 **Anna:** "Liberty -1... I don't love it, but it's not as bad as Diego's options."

> 💬 **Diego:** "My National Security Act is better. Stability +2, but Liberty -2."

> 💬 **Anna:** "Absolutely not."

> **📋 HIDDEN INFO:** Diego is testing if Anna will compromise. She won't on Liberty. Diego files this information away for later leverage.

> 💬 **Clara:** "What about Economic policy? The downturn warning is coming."

> **📋 CLARA'S STRATEGY:** Clara has Free Trade in hand (+2 Growth). If passed, it addresses Economic Downturn Warning AND scores her Prosperity priority. She's advocating for her own interest disguised as national interest.

> 💬 **Elena:** "You're all just protecting your own interests. What about the people? I have Wealth Redistribution: Budget -1, Inequality -2, but Growth -1."

> 💬 **Clara:** "Growth -1 when we're at 5? That's dangerous."

> **📋 WHY Clara opposes:** If Growth drops to 4, it gets closer to the -3 collapse threshold. More importantly, lower Growth means fewer Prosperity points for Clara. Her objection is self-interested.

> 💬 **Elena:** "See? The elite coalition protects Growth over equality. Typical."

---

**Coalition Sidebar (Anna, Clara, Bruno huddle):**

> 💬 **Anna (whispered):** "Let's pass Free Trade for Clara, and Law and Order for the border issue."

> 💬 **Clara:** "Deal. I'll sponsor Free Trade."

> 💬 **Bruno:** "I'll sponsor Law and Order. But Anna, you promised no Judiciary weakening. This might get reviewed."

> **📋 WHY Bruno mentions Judiciary:** Law and Order reduces Liberty, so it requires Judiciary review (per the rules). If Judiciary blocks it, Bruno wasted his 2 Influence sponsoring. He's checking if Anna is okay with that risk.

> 💬 **Anna:** "It reduces Liberty, so Judiciary reviews it. If it's blocked, that's fine with me honestly."

> **📋 ANNA'S SECRET RELIEF:** Anna publicly supports Law and Order for coalition unity, but secretly hopes Judiciary blocks it, preserving Liberty without her having to oppose her allies.

---

**Diego approaches the coalition:**

> 💬 **Diego:** "I'll vote for your Law and Order if you vote for my Industrial Policy next round."

> 💬 **Bruno:** "What's Industrial Policy?"

> **📋 CARD REVEAL - Diego shows from hand:**
> ```
> 🎴 Industrial Policy [Economic]
> Immediate: Budget -2, Growth +1, Stability +1
> No delayed effects. No Liberty impact.
> ```

> 💬 **Diego:** "Budget -2, Growth +1, Stability +1. Nothing controversial."

> 💬 **Anna:** "That's acceptable. Deal?"

> 💬 **Bruno:** "Deal."

> **⚠️ PROCESS FAILURE:** Anna says "deal" but this is during Deliberation, which allows "no binding commitments." Bruno made this deal WITH Anna present, but Anna later claims she didn't explicitly agree. The ambiguity will cause problems in Round 2.

---

**📝 DEAL #2 RECORDED: Industrial Policy Exchange**

| Aspect | Terms |
|--------|-------|
| **Parties** | Diego ↔ Coalition (specifically Bruno, Anna present) |
| **Diego promises** | Vote Yes on Law and Order (Round 1) |
| **Coalition promises** | Vote Yes on Industrial Policy (Round 2) |
| **Ambiguity** | Did Anna actually agree? She said "deal?" but Bruno answered. |

### Phase 3: Policy Actions

> **Turn Order:** Clockwise from First Player: Anna → Bruno → Clara → Diego → Elena
> **Rule:** Each player may sponsor 1 policy. Max 3 policies can pass per round.

---

#### Policy #1: Free Trade Agreement (Clara sponsors)

**⚙️ ACTION: Clara sponsors Free Trade Agreement**

```
💰 COST: Clara pays 2 Influence
   Clara: 6 Influence → 4 Influence

🎴 POLICY: Free Trade Agreement [Foreign]
   Immediate: Growth +2
   Delayed (2 rounds): Budget +1, Inequality +1
   Requires: Legislature (majority vote)

   ➡️ If passed, place marker on Round 3 for delayed effect
```

**30-Second Final Negotiation:**

> 💬 **Elena:** "Inequality +1? I'm voting No."

> **📋 WHY Elena opposes:** Elena's Equality priority scores +3 if Inequality ≤ 3 at game end. This policy increases Inequality by +1 (delayed), making that harder to achieve.

> 💬 **Diego:** "What do I get if I vote Yes?"

> 💬 **Clara:** "You already have a deal for Industrial Policy."

> 💬 **Diego:** "That's with Bruno, not you. I want something else."

> **📋 DIEGO'S CALCULATION:** Diego knows the coalition has 3 votes - they don't *need* him. But he can extract a favor by offering unnecessary support. Clara wants unanimous backing for her first policy.

> 💬 **Clara:** "Fine. I'll support one Economic policy of your choice later."

> 💬 **Diego:** "Deal."

---

**📝 DEAL #3 RECORDED: Economic Policy Favor**

| Aspect | Terms |
|--------|-------|
| **Parties** | Diego ↔ Clara |
| **Diego promises** | Vote Yes on Free Trade (Round 1) |
| **Clara promises** | Support one Economic policy of Diego's choice (future) |

---

**⚙️ ACTION: Simultaneous Vote Reveal**

All players secretly select vote tokens, then reveal simultaneously:

**Voting:**
| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Coalition obligation to Clara |
| Bruno | Yes | 0 | +1 | Coalition support |
| Clara | Yes | 0 | +1 | Sponsor (automatic Yes) |
| Diego | Yes | 0 | +1 | Deal #3 |
| Elena | No | 0 | -1 | Opposes Inequality increase |

**Vote Count:** Yes = 4, No = 1

**⚙️ RESULT: PASSES (majority achieved)**

```
📊 IMMEDIATE EFFECTS:
   Growth: 5 + 2 = 7

📊 DELAYED EFFECTS SCHEDULED:
   Round 3: Budget +1, Inequality +1

💰 SPONSOR REWARD:
   Clara: 4 Influence + 1 (policy passed) = 5 Influence

🏆 FACTION BONUS:
   Clara (Liberal): +1 Growth on Economic deregulation
   Growth: 7 + 1 = 8
```

**📊 STATE after Free Trade:**
```
Budget: 8 | Legitimacy: 10 | Stability: 10 | Growth: 8 | Liberty: 10 | Inequality: 0
```

---

#### Policy #2: Law and Order Initiative (Bruno sponsors)

**⚙️ ACTION: Bruno sponsors Law and Order Initiative**

```
💰 COST: Bruno pays 2 Influence
   Bruno: 6 Influence → 4 Influence

🎴 POLICY: Law and Order Initiative [Security]
   Immediate: Stability +2, Liberty -1
   Delayed: None
   Requires: Legislature (majority) + Judiciary Review (reduces Liberty)

   ⚖️ JUDICIARY REVIEW REQUIRED: This policy reduces Liberty
```

**30-Second Final Negotiation:**

> 💬 **Elena:** "Liberty erosion begins. The authoritarians show their true colors."

> 💬 **Anna:** "It's -1, Elena. We need Stability for the border crisis."

> 💬 **Elena:** "You're already compromising your principles, Progressive."

> **📋 ELENA'S STRATEGY:** Elena spends 1 Influence to add -1 to her vote. She knows she'll lose, but she's signaling ideological opposition and demonstrating her willingness to spend resources on principles.

**⚙️ ACTION: Simultaneous Vote Reveal**

**Voting:**
| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Coalition + addresses Border Tensions |
| Bruno | Yes | 0 | +1 | Sponsor |
| Clara | Yes | 0 | +1 | Coalition support |
| Diego | Yes | 0 | +1 | Deal #2 (promised to support) |
| Elena | No | 1 | -2 | Ideological opposition + Influence spent |

```
💰 Elena spends Influence:
   Elena: 5 Influence → 4 Influence
```

**Vote Count:** Yes = 4, No = 2

**⚙️ RESULT: PASSES (majority achieved)**

But wait - this policy requires **Judiciary Review** because it reduces Liberty!

---

**⚙️ ACTION: Judiciary Review**

```
⚖️ JUDICIARY REVIEW
   Policy reduces Liberty? YES (Liberty -1)
   Current Judiciary Strength: 3

   Rule: Policy blocked if d6 roll ≤ Judiciary Strength AND policy reduces Liberty

🎲 ROLL: d6 = 4

   4 > 3 → Roll exceeds Judiciary Strength
   ➡️ JUDICIARY DOES NOT BLOCK
   ➡️ Policy proceeds to implementation
```

> **📋 WHY this matters:** Anna secretly hoped the Judiciary would block this (saving Liberty without her having to oppose allies). The d6 roll of 4 meant the courts didn't intervene. Anna must now live with the Liberty loss.

---

**⚙️ IMMEDIATE EFFECTS APPLIED:**

```
📊 RESOURCE CHANGES:
   Stability: 10 + 2 = 12
   Liberty: 10 - 1 = 9

💰 SPONSOR REWARD:
   Bruno: 4 Influence + 1 (policy passed) = 5 Influence

✅ BORDER TENSIONS ADDRESSED:
   Security policy passed - the pending event in Round 2 is now NEGATED
```

**📊 STATE after Law and Order:**
```
Budget: 8 | Legitimacy: 10 | Stability: 12 | Growth: 8 | Liberty: 9 | Inequality: 0
```

---

#### Policy #3: Education Reform (Anna sponsors)

**⚙️ ACTION: Anna sponsors Education Reform**

```
💰 COST: Anna pays 2 Influence
   Anna: 6 Influence → 4 Influence

🎴 POLICY: Education Reform [Social]
   Immediate: Budget -2
   Delayed (3 rounds): Growth +2, Legitimacy +1
   Requires: Legislature (majority)

   ➡️ If passed, place marker on Round 4 for delayed effect
```

**30-Second Final Negotiation:**

> 💬 **Diego:** "Why should I support this? It doesn't help me."

> 💬 **Anna:** "Because the nation needs educated citizens. And I'm asking nicely."

> 💬 **Diego:** "Asking nicely doesn't pay bills. Give me something."

> **📋 DIEGO'S POSITION:** Diego already has Deal #2 (Industrial Policy support) and Deal #3 (Clara's favor). He could extract more from Anna, but the coalition has 3 votes without him.

> 💬 **Elena:** "I'll support it. Education helps equality."

> **📋 WHY Elena supports:** Elena's Equality priority benefits from policies that help everyone. Education indirectly reduces Inequality over time. Also, supporting Anna's Social policy costs Elena nothing.

> 💬 **Diego:** "Without my vote it's 4-0. It passes anyway. I'll abstain."

> **📋 DIEGO'S CALCULATION:** Abstaining preserves his neutrality. If he votes Yes, he gives Anna a favor without getting anything. If he votes No, he seems hostile for no reason. Abstaining is strategically optimal.

**⚙️ ACTION: Simultaneous Vote Reveal**

**Voting:**
| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Sponsor |
| Bruno | Yes | 0 | +1 | Coalition support |
| Clara | Yes | 0 | +1 | Coalition + Deal #1 (promised to support Anna's Social policies) |
| Diego | Abstain | 0 | 0 | No benefit to vote either way |
| Elena | Yes | 0 | +1 | Supports equality-adjacent policies |

**Vote Count:** Yes = 4, Abstain = 1, No = 0

**⚙️ RESULT: PASSES (majority achieved)**

---

**⚙️ IMMEDIATE EFFECTS APPLIED:**

```
📊 RESOURCE CHANGES:
   Budget: 8 - 2 = 6

📊 DELAYED EFFECTS SCHEDULED:
   Round 4: Growth +2, Legitimacy +1

💰 SPONSOR REWARD:
   Anna: 4 Influence + 1 (policy passed) = 5 Influence

🏆 FACTION BONUS:
   Anna (Progressive): +1 Legitimacy on Social policies
   Legitimacy: 10 + 1 = 11
```

**📊 STATE after Education Reform:**
```
Budget: 6 | Legitimacy: 11 | Stability: 12 | Growth: 8 | Liberty: 9 | Inequality: 0
```

---

#### Policy Limit Reached

**⚠️ ROUND LIMIT: Maximum 3 policies passed this round.**

Diego and Elena cannot sponsor policies this round. Their unspent policy selections remain in hand for next round.

> **📋 WHY this rule exists:** The 3-policy limit forces prioritization. With 5 players but only 3 policy slots, players must compete or cooperate for limited legislative time. The coalition used all 3 slots (Clara, Bruno, Anna), leaving opposition without a voice this round.

### Phase 4: Implementation

For each passed policy, check Executive implementation quality:

**⚙️ ACTION: Executive Implementation Rolls**

```
Rule: Roll d6 for each policy.
      If roll ≤ Executive Strength (3): Full implementation
      If roll > Executive Strength: Partial implementation (50% effect)
```

---

**Policy 1: Free Trade Agreement**

```
⚖️ Judiciary Review: NOT REQUIRED (doesn't affect Liberty)
🎲 Executive Roll: d6 = 3
   3 ≤ 3 → FULL IMPLEMENTATION
   ✅ Growth +2 applied in full (already done during vote phase)
```

---

**Policy 2: Law and Order Initiative**

```
⚖️ Judiciary Review: ALREADY PASSED (rolled 4 > 3)
🎲 Executive Roll: d6 = 2
   2 ≤ 3 → FULL IMPLEMENTATION
   ✅ Stability +2, Liberty -1 applied in full (already done)
```

---

**Policy 3: Education Reform**

```
⚖️ Judiciary Review: NOT REQUIRED
🎲 Executive Roll: d6 = 5
   5 > 3 → PARTIAL IMPLEMENTATION

   ⚠️ Full effect would be: Budget -2 immediate, delayed Growth +2, Legitimacy +1
   ⚠️ Partial effect: Budget -2 immediate, delayed effects REDUCED by 50%

   📊 ADJUSTED DELAYED EFFECTS:
   Round 4: Growth +1 (was +2), Legitimacy +1 (round up from 0.5)
```

> **📋 WHY partial implementation hurts Anna:** The Executive's poor implementation (rolled 5 > 3) means Education Reform delivers less benefit. Anna paid the full Budget cost but only gets half the future payoff. This simulates bureaucratic inefficiency.

---

**📊 TIMELINE after Implementation:**

```
Round 1 (now) | Round 2      | Round 3              | Round 4
-------------|--------------|----------------------|------------------
[COMPLETE]   | Border       | Free Trade delayed:  | Education delayed:
             | Tensions ✓   | Budget +1            | Growth +1
             | (negated)    | Inequality +1        | Legitimacy +1
```

### Phase 5: Consequences

**⚙️ ACTION: Check Feedback Loops**

```
Automatic effects that trigger when conditions are met:

1. Growth > 10: Budget +1 (tax revenue)
   → Growth = 8. NOT > 10. No effect.

2. Growth < 0: Budget -1, Stability -1 (recession)
   → Growth = 8. NOT < 0. No effect.

3. Stability < 5: Legitimacy -1 (public loses faith)
   → Stability = 12. NOT < 5. No effect.

4. Liberty < 5: Legitimacy -1 (repression breeds resentment)
   → Liberty = 9. NOT < 5. No effect.

5. Boom check (Growth ≥ 8 for 2 rounds): Budget +2, Stability -1
   → Growth = 8 (first round at 8+). Counter starts. Check next round.

6. Stability > 15 AND Liberty < 8: Security State
   → Stability = 12, Liberty = 9. Neither condition met.

✅ NO FEEDBACK LOOPS TRIGGERED THIS ROUND
```

---

**⚙️ ACTION: Market Phase**

```
Rule: Markets generate Growth based on Market Strength (3).
      Roll d6:
      - If ≤ Market Strength: Growth +1
      - If > Market Strength: Roll d3-2 (range -1 to +1)

🎲 Market Roll: d6 = 5

   5 > 3 → Markets are volatile this round
   🎲 Volatility Roll: d3 = 1
   1 - 2 = -1

📊 MARKET EFFECT:
   Growth: 8 - 1 = 7
```

> **📋 WHY markets are volatile:** High Market Strength (4-5) means stable but slow growth. Low strength (1-2) means volatile but potentially high growth. At Strength 3, there's a 50% chance of volatility each round.

---

**📊 FINAL STATE - END OF ROUND 1:**

```
NATIONAL RESOURCES:
┌──────────────┬───────┬────────────────────────────────┐
│ Resource     │ Value │ Change This Round              │
├──────────────┼───────┼────────────────────────────────┤
│ Budget       │ 6     │ 8 → 6 (-2 Education)           │
│ Legitimacy   │ 11    │ 10 → 11 (+1 Anna bonus)        │
│ Stability    │ 12    │ 10 → 12 (+2 Law and Order)     │
│ Growth       │ 7     │ 5 → 8 (+2 Free Trade, +1 Clara)│
│              │       │ 8 → 7 (-1 Market volatility)   │
│ Liberty      │ 9     │ 10 → 9 (-1 Law and Order)      │
│ Inequality   │ 0     │ No change                      │
│ Approval     │ 5     │ No change                      │
└──────────────┴───────┴────────────────────────────────┘

PLAYER INFLUENCE:
┌─────────┬───────────┬─────────────────────────────────┐
│ Player  │ Influence │ Change                          │
├─────────┼───────────┼─────────────────────────────────┤
│ Anna    │ 5         │ 6 → 4 (sponsor) → 5 (pass)      │
│ Bruno   │ 5         │ 6 → 4 (sponsor) → 5 (pass)      │
│ Clara   │ 5         │ 6 → 4 (sponsor) → 5 (pass)      │
│ Diego   │ 5         │ No change                       │
│ Elena   │ 4         │ 5 → 4 (spent on vote)           │
└─────────┴───────────┴─────────────────────────────────┘
```

### Phase 6: Refresh

**⚙️ ACTION: Draw New Policy Cards**

Each player draws 2 new Policy Cards, then discards down to 5 if over:

```
Anna draws: Workers' Rights Act, Progressive Taxation
   Hand: 5 cards → 7 cards → discard 2 → 5 cards
   Discards: Universal Healthcare, Community Policing Reform

Bruno draws: Budget Stabilization (2nd copy), Judicial Appointment
   Hand: 4 cards (used Law and Order) → 6 cards → discard 1 → 5 cards
   Discards: Austerity Measures

Clara draws: Infrastructure Investment, Trade Agreement (2nd copy)
   Hand: 4 cards (used Free Trade) → 6 cards → discard 1 → 5 cards
   Discards: Trade Agreement (duplicate)

Diego draws: Veterans Support Act, Border Security Enhancement
   Hand: 5 cards → 7 cards → discard 2 → 5 cards
   Discards: Military Modernization, Border Securitization

Elena draws: Public Housing Initiative, Labor Rights Protection
   Hand: 5 cards → 7 cards → discard 2 → 5 cards
   Discards: Housing Subsidy Program, Electoral Reform
```

**⚙️ ACTION: Pass First Player Marker**

```
First Player: Anna → Bruno (clockwise)
Bruno will lead Round 2 events and policy ordering.
```

**⚙️ ACTION: Check Collapse Conditions**

```
□ Budget ≤ 0 for 2 rounds? NO (Budget = 6)
□ Legitimacy ≤ 2? NO (Legitimacy = 11)
□ Stability ≤ 2? NO (Stability = 12)
□ Liberty ≤ 3? NO (Liberty = 9)
□ Revolution (Inequality ≥ 10 AND Stability ≤ 5)? NO

✅ NATION SURVIVES - PROCEED TO ROUND 2
```

---

### End of Round 1 Summary

**ACTIVE DEALS:**

| # | Parties | Terms | Status |
|---|---------|-------|--------|
| 1 | Anna-Bruno-Clara | Coalition: mutual support, no Judiciary weakening | Active |
| 2 | Diego ↔ Coalition | Diego voted for Law & Order; Coalition owes Industrial Policy support | Pending (Round 2) |
| 3 | Diego ↔ Clara | Diego voted for Free Trade; Clara owes 1 Economic policy support | Pending |

**CARDS USED THIS ROUND:**
- Free Trade Agreement (Clara) - passed
- Law and Order Initiative (Bruno) - passed
- Education Reform (Anna) - passed

---

## Round 2: The First Test of Trust

> **First Player:** Bruno (Conservatives)

### Phase 1: Events

**⚙️ ACTION: Check Pending Events from Timeline**

```
📊 TIMELINE CHECK - Round 2:
   Border Tensions was scheduled: Stability -1 unless Security policy passed

   ✅ Security policy passed in Round 1 (Law and Order Initiative)
   ➡️ Border Tensions NEGATED - no effect
```

---

**⚙️ ACTION: Draw 5 New Event Cards**

Bruno (First Player) draws 5 events:

```
🎴 EVENT 1: Media Investigation [IMMEDIATE]
   "Journalists uncover a politician's true motivations."
   Effect: Reveal one random player's Legacy priority.
   🎲 Roll d6 to select player: 1=Anna, 2=Bruno, 3=Clara, 4=Diego, 5=Elena, 6=reroll
   🎲 Roll: 3 = CLARA

   ⚠️ Clara's Priority 1 (Prosperity) is now PUBLIC KNOWLEDGE
   All players now know Clara's goal is to maximize Growth and Budget.

🎴 EVENT 2: Labor Union Demands [IMMEDIATE]
   "Workers demand better conditions and threaten strikes."
   Effect: If no Worker/Labor policy passed this round: Legitimacy -1, Growth -1

🎴 EVENT 3: Foreign Investment Offer [IMMEDIATE]
   "International investors propose a major economic deal."
   Effect: Players vote: Accept (Growth +2, Liberty -1) OR Reject (nothing)

🎴 EVENT 4: Infrastructure Decay [PENDING +2 rounds]
   "Aging infrastructure threatens public safety."
   Effect: In Round 4: Stability -2 unless Infrastructure policy passed
   ➡️ Place marker on Round 4 Timeline

🎴 EVENT 5: Economic Boom Celebration [IMMEDIATE]
   "Citizens celebrate recent prosperity."
   Effect: If Growth ≥ 10: Approval +2
   → Check: Growth = 7. NOT ≥ 10. No effect.
```

---

**⚙️ RESOLVE: Media Investigation**

> 💬 **Elena:** "Clara's priority is Prosperity. Of course the Liberal wants Growth above all else. Don't trust her deals."

> 💬 **Clara:** "My priorities are public now. So what? Growth helps everyone."

> 💬 **Diego:** "Interesting. So you'll do anything to maximize Growth..."

> **📋 WHY this revelation matters:** Diego now knows Clara NEEDS high Growth to score well. He can use this leverage to extract concessions. Clara's negotiating position just weakened significantly.

---

**⚙️ RESOLVE: Foreign Investment Offer**

This requires a group vote:

**30-Second Negotiation:**

> 💬 **Anna:** "Accept means Liberty -1. We're already at 9."

> 💬 **Clara:** "But Growth +2! That's huge!"

> **📋 CLARA'S DESPERATION:** With her Prosperity priority exposed, Clara needs Growth. She'll push hard for Accept.

> 💬 **Diego:** "I'll vote Accept if Clara gives me a better deal on her promise."

> 💬 **Clara:** "What do you want?"

> 💬 **Diego:** "Support TWO of my Economic policies, not one."

> 💬 **Clara:** "That's extortion."

> 💬 **Diego:** "That's negotiation. Your priority is exposed. I know you want this."

---

**📝 DEAL #3 MODIFIED: Economic Policy Favor (Updated)**

| Aspect | Original | Modified |
|--------|----------|----------|
| **Clara owes** | 1 Economic policy support | **2** Economic policy supports |
| **Diego gave** | Vote Yes on Free Trade | Vote Yes on Free Trade + Accept |

> **📋 WHY Clara accepts:** She calculates: Growth +2 now is worth committing to 2 future votes. Her Prosperity priority scores +1 per Growth above 5. At Growth 9, that's 4 points. At Growth 7, only 2 points.

---

**⚙️ ACTION: Foreign Investment Vote**

| Player | Vote | Reasoning |
|--------|------|-----------|
| Anna | Reject | Opposes Liberty -1 (Freedom priority) |
| Bruno | Accept | Growth helps Budget stability |
| Clara | Accept | Prosperity priority demands it |
| Diego | Accept | Modified deal secured |
| Elena | Reject | Opposes Liberty erosion |

**Result:** Accept: 3, Reject: 2 → **ACCEPTED**

```
📊 IMMEDIATE EFFECTS:
   Growth: 7 + 2 = 9
   Liberty: 9 - 1 = 8
```

---

**⚙️ RESOLVE: Labor Union Demands**

```
Check: Was any Worker/Labor policy passed this round?
→ No policies passed yet (Round 2 just started)
→ Condition NOT MET

📊 PENALTY APPLIED:
   Legitimacy: 11 - 1 = 10
   Growth: 9 - 1 = 8
```

> **📋 WHY this hurts:** The coalition focused on Economic (Free Trade) and Security (Law and Order) in Round 1, ignoring Labor. Now they pay the price.

---

**📊 STATE after Round 2 Events:**
```
Budget: 6 | Legitimacy: 10 | Stability: 12 | Growth: 8 | Liberty: 8 | Inequality: 0
```

**📊 UPDATED TIMELINE:**
```
Round 2 (now)  | Round 3              | Round 4
---------------|----------------------|------------------
               | Free Trade delayed:  | Education delayed:
               | Budget +1            | Growth +1
               | Inequality +1        | Legitimacy +1
               |                      | Infrastructure Decay:
               |                      | Stability -2 (unless fixed)
```

### Phase 2: Deliberation - The Coalition Fractures

> **⏱️ TIME:** 5 minutes maximum for open negotiation

---

**The Deal #2 Test - Diego Calls In His Favor:**

> 💬 **Diego:** "Time for you to honor Deal #2. I want votes for Industrial Policy."

> 💬 **Bruno:** "We agreed. Anna, Clara - we have to support it."

> 💬 **Anna:** "I never agreed to that deal. Bruno made it without asking me."

> 💬 **Bruno:** "You were standing right there!"

> 💬 **Anna:** "I was negotiating the coalition terms. I didn't agree to Industrial Policy."

> **📋 THE AMBIGUITY SURFACES:** In Round 1 Deliberation, Anna said "That's acceptable. Deal?" and Bruno answered "Deal." Anna now claims she was asking a question, not committing. This is exactly the kind of deal ambiguity that causes table conflicts.

> 💬 **Diego:** "Are you breaking the deal?"

> 💬 **Anna:** "I'm not bound by deals I didn't make."

> 💬 **Bruno:** "Anna, if you don't support this, Diego will never work with us again."

> 💬 **Clara:** "And I owe him two Economic policies now. I need him cooperative."

> 💬 **Elena (watching with amusement):** "The coalition is cracking already. Beautiful."

---

**Anna's Dilemma:**

```
OPTION A: Support Industrial Policy
+ Maintains coalition unity
+ Keeps Diego as potential ally
+ Bruno and Clara stay happy
- Sets precedent that others can commit her to deals
- She gets nothing in return

OPTION B: Oppose Industrial Policy
+ Maintains independence
+ Establishes that she controls her own votes
- Breaks coalition trust
- Makes Diego hostile
- May fracture the coalition entirely
```

> **📋 WHY this matters for the game:** This moment tests whether informal agreements during Deliberation are binding. The rules say "no binding commitments," but socially, people expect deals to be honored. Anna is technically correct but may face social consequences.

> 💬 **Anna:** "Fine. I'll support Industrial Policy. But Bruno - never make deals for me again without my explicit agreement. Understood?"

> 💬 **Bruno:** "Understood. I apologize."

> **📋 ANNA'S CHOICE:** She yields to preserve coalition unity, but this resentment will resurface later. She's making a strategic choice to avoid immediate conflict while storing up grievance.

---

**Secret Negotiation: Elena Approaches Diego**

*Elena and Diego step away from the table for 30 seconds:*

> 💬 **Elena (whispered):** "The coalition is weak. Anna almost defected. Help me destabilize them and I'll support your Security policies."

> 💬 **Diego:** "Why would I trust you? You're anti-establishment."

> 💬 **Elena:** "Exactly. I want to tear down their cozy arrangement. You want power. We can help each other."

> **📋 ELENA'S CALCULATION:** Elena is at 4 Influence, lowest in the game. She can't pass policies alone. Diego has 5 Influence but no coalition allies. Together they have 9 Influence - still less than the coalition's 15, but enough to cause problems.

> 💬 **Diego:** "I'll consider it. But I want a specific commitment."

> 💬 **Elena:** "Name it."

> 💬 **Diego:** "When I sponsor National Security Act, you vote Yes."

> 💬 **Elena:** "That's Liberty -2. My voters would hate that."

> **📋 ELENA'S CONFLICT:** Elena claims to care about Liberty (her populist base), but she cares more about power (Influence priority). She's about to betray her stated values for tactical advantage.

> 💬 **Diego:** "Do you want to break the coalition or not?"

> 💬 **Elena:** "...Deal. But only if you help me pass Wealth Redistribution afterward."

---

**📝 SECRET DEAL #4 RECORDED: Opposition Alliance**

| Aspect | Terms |
|--------|-------|
| **Parties** | Diego ↔ Elena (secret from others) |
| **Diego promises** | Support Wealth Redistribution (vote Yes) |
| **Elena promises** | Support National Security Act (vote Yes) |
| **Goal** | Destabilize the coalition |
| **Risk** | Both are sacrificing their stated principles for power |

> **⚠️ KEY DISTINCTION:** Diego promises to "support" Wealth Redistribution. As we'll see, he interprets "support" as "not oppose" rather than "vote Yes." This ambiguity will cause Deal #4 to explode.

### Phase 3: Policy Actions

> **Turn Order:** Clockwise from First Player: Bruno → Clara → Diego → Elena → Anna
> **Note:** Diego goes before Elena this round, so he sponsors Industrial Policy first

---

#### Policy #1: Industrial Policy (Diego sponsors)

**⚙️ ACTION: Diego sponsors Industrial Policy**

```
💰 COST: Diego pays 2 Influence
   Diego: 5 Influence → 3 Influence

🎴 POLICY: Industrial Policy [Economic]
   Immediate: Budget -2, Growth +1, Stability +1
   Delayed: None
   Requires: Legislature (majority vote)
```

**30-Second Final Negotiation:**

> 💬 **Elena:** "I'm voting No. Not part of any elite deal."

> **📋 ELENA'S PUBLIC POSITION:** Elena publicly opposes to maintain her anti-establishment image, even though she secretly wants Diego as an ally. She needs to appear consistent.

> 💬 **Anna (reluctantly):** "I'll honor the coalition agreement."

> **📋 ANNA'S BODY LANGUAGE:** Notice Anna says "coalition agreement" not "my deal." She's signaling she feels coerced, not willing.

**⚙️ ACTION: Simultaneous Vote Reveal**

| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Reluctant - honoring Bruno's deal for coalition unity |
| Bruno | Yes | 0 | +1 | Deal #2 - he made this promise |
| Clara | Yes | 0 | +1 | Coalition + she owes Diego 2 policies anyway |
| Diego | Yes | 0 | +1 | Sponsor |
| Elena | No | 0 | -1 | Maintains anti-establishment image |

**Vote Count:** Yes = 4, No = 1

**⚙️ RESULT: PASSES (majority achieved)**

```
📊 IMMEDIATE EFFECTS:
   Budget: 6 - 2 = 4
   Growth: 8 + 1 = 9
   Stability: 12 + 1 = 13

💰 SPONSOR REWARD:
   Diego: 3 Influence + 1 (policy passed) = 4 Influence

🏆 FACTION BONUS:
   Diego (Nationalist): +1 Stability on Security policies?
   → Industrial Policy is ECONOMIC, not Security
   → No faction bonus applies
```

**📊 STATE after Industrial Policy:**
```
Budget: 4 | Legitimacy: 10 | Stability: 13 | Growth: 9 | Liberty: 8 | Inequality: 0
```

**✓ DEAL #2 HONORED**
- Diego voted Yes on Law and Order (Round 1) ✓
- Coalition voted Yes on Industrial Policy (Round 2) ✓

---

#### Policy #2: Deregulation Act (Clara sponsors)

**⚙️ ACTION: Clara sponsors Deregulation Act**

```
💰 COST: Clara pays 2 Influence
   Clara: 5 Influence → 3 Influence

🎴 POLICY: Deregulation Act [Economic]
   Immediate: Growth +2, Liberty +1
   Delayed (2 rounds): Stability -1
   Requires: Legislature (majority vote)
```

**30-Second Final Negotiation:**

> 💬 **Anna:** "Liberty +1 helps recover from Foreign Investment. I'll support."

> **📋 WHY Anna supports despite being coalition:** Deregulation increases Liberty (+1), which helps her Freedom priority. She's voting in self-interest, but it aligns with coalition this time.

> 💬 **Bruno:** "But delayed Stability -1. That's concerning."

> 💬 **Clara:** "We're at 13 Stability. We can afford it."

> 💬 **Diego:** "This counts as one of the two Economic policies you owe me, Clara."

> 💬 **Clara:** "Wait, you're supposed to support MY policies, not the other way around."

> 💬 **Diego:** "You owe me support. I don't owe you anything on this one."

> **📋 DEAL MECHANICS CONFUSION:** Deal #3 says Clara owes Diego support on 2 Economic policies. Diego is trying to count Clara's OWN policy as one of the two. This is a creative (some would say sleazy) interpretation.

> 💬 **Clara:** "Then vote Yes and I'll count it as you supporting me."

> 💬 **Diego:** "Hmm. Deal. Yes."

**⚙️ ACTION: Simultaneous Vote Reveal**

| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Liberty +1 helps her Freedom priority |
| Bruno | Yes | 0 | +1 | Coalition support |
| Clara | Yes | 0 | +1 | Sponsor |
| Diego | Yes | 0 | +1 | Gets to count this toward Deal #3 |
| Elena | No | 0 | -1 | Opposes anything that helps the coalition |

**Vote Count:** Yes = 4, No = 1

**⚙️ RESULT: PASSES**

```
📊 IMMEDIATE EFFECTS:
   Growth: 9 + 2 = 11
   Liberty: 8 + 1 = 9

📊 DELAYED EFFECTS SCHEDULED:
   Round 4: Stability -1

💰 SPONSOR REWARD:
   Clara: 3 Influence + 1 (policy passed) = 4 Influence

🏆 FACTION BONUS:
   Clara (Liberal): +1 Growth on Economic deregulation
   Growth: 11 + 1 = 12
```

**📊 STATE after Deregulation:**
```
Budget: 4 | Legitimacy: 10 | Stability: 13 | Growth: 12 | Liberty: 9 | Inequality: 0
```

> **📋 GROWTH BREAKPOINT:** Growth is now 12, which is > 10. This will trigger the Budget +1 feedback loop during Consequences phase!

---

#### Policy #3: Wealth Redistribution (Elena sponsors)

> **⚠️ THIS IS THE PIVOTAL MOMENT: Deal #4 will be tested and broken here.**

**⚙️ ACTION: Elena sponsors Wealth Redistribution**

```
💰 COST: Elena pays 2 Influence
   Elena: 4 Influence → 2 Influence

🎴 POLICY: Wealth Redistribution [Social]
   Immediate: Budget -1, Inequality -2, Growth -1
   Delayed: None
   Requires: Legislature (majority vote)
```

**30-Second Final Negotiation:**

> 💬 **Clara:** "Growth -1?! We're at 12 now. It would drop to 11. I oppose."

> **📋 CLARA'S PRIORITY EXPOSED:** Everyone knows Clara's Prosperity priority. She MUST protect Growth. She will spend Influence to strengthen her No vote.

> 💬 **Anna:** "But Inequality -2 is good. I care about equality."

> 💬 **Bruno:** "Coalition solidarity says we vote together. Clara opposes, so we all oppose?"

> 💬 **Anna:** "I'm not bound by coalition on everything. This aligns with my values."

> 💬 **Bruno:** "Anna, if you break coalition discipline, we're done."

> **📋 COALITION TENSION:** Anna is about to vote AGAINST her coalition partner Clara. This is the second time Anna has pushed back against coalition expectations.

---

**The Deal #4 Betrayal:**

> 💬 **Diego (to Elena, quietly):** "I can't support this publicly. It kills Growth. I'm abstaining."

> 💬 **Elena:** "You promised!"

> 💬 **Diego:** "I promised to support it. Abstain is not opposing. Technically keeping my word."

> 💬 **Elena:** "That's a betrayal of spirit!"

> 💬 **Diego:** "Welcome to politics."

> **📋 DIEGO'S WORD GAMES:** Diego made Deal #4 using the word "support." He's now claiming that abstaining (0 vote) counts as "not opposing" which equals "support." This is technically defensible but morally dubious.

---

**⚙️ ACTION: Simultaneous Vote Reveal**

| Player | Vote | Influence Spent | Total | Reasoning |
|--------|------|-----------------|-------|-----------|
| Anna | Yes | 0 | +1 | Equality priority overrides coalition |
| Bruno | No | 0 | -1 | Stays loyal to Clara/coalition |
| Clara | No | 1 | -2 | SPENDS 1 INFLUENCE to strengthen opposition |
| Diego | Abstain | 0 | 0 | "Technical" compliance with Deal #4 |
| Elena | Yes | 0 | +1 | Sponsor |

```
💰 Clara spends Influence to strengthen vote:
   Clara: 4 Influence → 3 Influence
   Clara's vote: -1 base → -2 total
```

**Vote Count:** Yes = 2, No = 3

**⚙️ RESULT: FAILS (No majority)**

---

**The Fallout - Deal #4 Explodes:**

> 💬 **Elena:** "Diego, you traitor! You abstained!"

> 💬 **Diego:** "I didn't vote against you. That was the deal."

> 💬 **Elena:** "The deal was SUPPORT, not abstain!"

> 💬 **Anna:** "You two had a secret deal?"

> **📋 SECRET EXPOSED:** The table now knows Diego and Elena were conspiring. This changes the political landscape.

---

**⚙️ ACTION: Group Ruling on Deal Interpretation**

```
DISPUTE: Did Diego break Deal #4?

Diego's position: "Support" = "not oppose" = abstaining is valid
Elena's position: "Support" = "vote Yes" = abstaining is betrayal

TABLE VOTE ON INTERPRETATION:
- Diego broke deal: Anna, Elena (2 votes)
- Diego kept deal: Clara, Diego (2 votes)
- Abstain as arbiter: Bruno

Bruno's ruling: "The word 'support' implies active Yes vote.
                 Diego broke the deal in spirit."
```

**📝 DEAL #4 RULING: ✗ BROKEN by Diego**

```
⚠️ CONSEQUENCE: Diego loses "never broke a deal" bonus eligibility
   This costs him 2 Legacy points at game end.
```

> 💬 **Diego:** "Fine. But Elena, our arrangement for National Security Act is void then."

> 💬 **Elena:** "Gladly. I was going to betray you anyway."

> **📋 DESIGN INSIGHT:** This moment demonstrates why deal language matters. If Diego had promised to "vote Yes" instead of "support," there would be no ambiguity. Players should be specific in their deal terms.

**📊 STATE after Wealth Redistribution (failed):**
```
Budget: 4 | Legitimacy: 10 | Stability: 13 | Growth: 12 | Liberty: 9 | Inequality: 0
(No changes - policy failed)
```

### Phase 4: Implementation

**⚙️ ACTION: Executive Implementation Rolls**

```
Policy 1: Industrial Policy
🎲 Executive Roll: d6 = 2
   2 ≤ 3 → FULL IMPLEMENTATION
   ✅ Budget -2, Growth +1, Stability +1 applied

Policy 2: Deregulation Act
🎲 Executive Roll: d6 = 4
   4 > 3 → PARTIAL IMPLEMENTATION
   ⚠️ Full: Growth +2, Liberty +1
   ⚠️ Partial: Growth +1, Liberty +1 (Growth reduced by 50%)

📊 DELAYED EFFECTS SCHEDULED:
   Round 4: Deregulation → Stability -1
```

### Phase 5: Consequences

**⚙️ ACTION: Check Feedback Loops**

```
1. Growth > 10: Budget +1 (tax revenue)
   → Growth = 12. YES > 10.
   📊 Budget: 4 + 1 = 5

2. Boom check (Growth ≥ 8 for 2 rounds): Budget +2, Stability -1
   → Growth was 8 (R1), now 12 (R2). Two consecutive rounds!
   📊 Budget: 5 + 2 = 7, Stability: 13 - 1 = 12
   Wait - rechecking original values... (simulation note)

3. Stability > 15 AND Liberty < 8: Security State
   → Stability = 13-15, Liberty = 9. NOT triggered.
```

**⚙️ ACTION: Market Phase**

```
🎲 Market Roll: d6 = 2
   2 ≤ 3 → Stable market
   📊 Growth: 12 + 1 = 13
   Wait - Growth was already at 12, so Growth: 12 + 1 = 13
```

### End of Round 2 Summary

**📊 FINAL STATE - END OF ROUND 2:**

```
NATIONAL RESOURCES:
┌──────────────┬───────┐
│ Budget       │ 5     │
│ Legitimacy   │ 10    │
│ Stability    │ 15    │
│ Growth       │ 12    │
│ Liberty      │ 9     │
│ Inequality   │ 0     │
└──────────────┴───────┘

PLAYER INFLUENCE:
┌─────────┬───────────┬────────────────────────────────┐
│ Player  │ Influence │ Status                         │
├─────────┼───────────┼────────────────────────────────┤
│ Anna    │ 5         │ Coalition (strained with Bruno)│
│ Bruno   │ 5         │ Coalition (solid)              │
│ Clara   │ 4         │ Coalition, owes Diego 1 more   │
│ Diego   │ 4         │ BROKE Deal #4, isolated        │
│ Elena   │ 2         │ Betrayed, angry, isolated      │
└─────────┴───────────┴────────────────────────────────┘
```

**TRUST MATRIX after Round 2:**

```
         Anna   Bruno  Clara  Diego  Elena
Anna     --     TENSE  OK     COLD   OK
Bruno    TENSE  --     GOOD   OK     COLD
Clara    OK     GOOD   --     WARY   COLD
Diego    COLD   OK     WARY   --     HOSTILE
Elena    OK     COLD   COLD   HOSTILE --
```

**ACTIVE DEALS:**
| # | Status | Notes |
|---|--------|-------|
| 1 (Coalition) | Strained | Anna defied coalition on Wealth Redistribution |
| 2 (Industrial) | ✓ HONORED | Both sides delivered |
| 3 (Clara-Diego) | Partial | Clara owes 1 more Economic vote |
| 4 (Secret) | ✗ BROKEN | Diego abstained; lost deal bonus |

---

## Round 3: Revenge Politics

> **📋 FORMATTING NOTE:** Rounds 3-6 continue with the same explicit formatting patterns established above:
> - ⚙️ ACTION markers for game mechanics
> - 🎴 CARD displays for policies and events
> - 📋 WHY boxes for strategic reasoning
> - 📝 DEAL tracking for agreements
> - 📊 STATE snapshots after major changes
>
> Key events in remaining rounds: Anna leaves coalition (Round 3), Unity Government saves everyone (Round 4), Election bonus contested (Round 5), Final scoring (Round 6).

> **First Player:** Clara (Liberals)

### Phase 1: Events

**⚙️ ACTION: Resolve Delayed Effects from Timeline**

```
📊 ROUND 3 TIMELINE CHECK:
   Free Trade Agreement (from Round 1) triggers:
   → Budget: 5 + 1 = 6
   → Inequality: 0 + 1 = 1

⚠️ INEQUALITY RISES: First point of Inequality in the game.
   Elena's Equality priority needs Inequality ≤ 3.
   Anna's hidden agenda also cares about Inequality.
```

**⚙️ ACTION: Draw 5 Event Cards**

```
🎴 EVENT 1: Political Assassination Attempt [CRISIS, IMMEDIATE]
   "A radical attempts to assassinate a prominent political figure."
   Effect: Target highest Influence player.
   🎲 Roll d6: 1-2 = lose 3 Inf, 3-4 = lose 1 Inf, 5-6 = no effect

   Highest Influence: Anna and Bruno tied at 5
   🎲 Roll to select target: d6 = 1 (odd = first alphabetically) = ANNA
   🎲 Roll for effect: d6 = 2

   ⚠️ RESULT: Anna loses 3 Influence!
   Anna: 5 Influence → 2 Influence

   > **📋 WHY this matters:** Anna was a coalition leader with power.
   > Now at 2 Influence, she can barely sponsor policies (costs 2).
   > She's suddenly vulnerable and dependent on allies.

🎴 EVENT 2: Economic Boom Celebration [IMMEDIATE]
   "Citizens celebrate unprecedented prosperity."
   Effect: If Growth ≥ 10: Approval +2
   → Growth = 12. YES ≥ 10.
   📊 Approval: 5 + 2 = 7

🎴 EVENT 3: Religious Tensions [PENDING +1 round]
   "Interfaith conflicts threaten social cohesion."
   Effect: Round 4: Stability -1 unless addressed
   → Place on Timeline

🎴 EVENT 4: Anti-Corruption Campaign [IMMEDIATE]
   "Citizens demand accountability from leaders."
   Effect: Group vote - Support (Legitimacy +2, reveal priority) or Oppose (Legitimacy -1)
```

> **Anna (shaken):** "I just lost most of my Influence to an assassination attempt. This is a disaster."
>
> **Elena:** "Funny how the Progressive gets targeted. Maybe it's karma for abandoning your coalition on my vote."
>
> **Bruno:** "That's uncalled for, Elena."
>
> **Clara:** "Anna, you need protection. You can't sponsor anything now."

**Anti-Corruption Vote:**

> **Elena:** "Support it. Expose more priorities. Let's see who else is hiding what."
>
> **Diego:** "I'll oppose. I don't want my priorities exposed."
>
> **Bruno:** "The Legitimacy gain is worth it. Support."

**Vote:** Support: 3 (Anna, Bruno, Elena), Oppose: 2 (Clara, Diego)
- Legitimacy +2 → 12
- Random priority revealed: Roll d6 = **2 = Bruno** → Institutions priority revealed!

> **Elena:** "Bruno wants strong Institutions. No surprise there, Conservative."
>
> **Diego:** "So Bruno will always vote against anything that weakens Judiciary or Legislature. Good to know."

**Economic Boom:** Growth at 12 ≥ 10 → Approval +2 → 7

### Phase 2: Deliberation - The Power Vacuum

> **Diego:** "Anna has only 2 Influence. She can't sponsor. The coalition is weakened."
>
> **Clara:** "Bruno and I can still carry things."
>
> **Elena:** "Actually, Diego and I have a combined 6 Influence. You two have 9. It's close."
>
> **Diego:** "Wait, I thought you hated me after the deal."
>
> **Elena:** "I hate everyone equally. But I hate the coalition slightly more. Want to form an opposition bloc?"
>
> **Diego:** "...I'm listening."
>
> **Elena:** "We coordinate votes. Force them to negotiate with us instead of ignoring us."
>
> **Diego:** "And what do I get specifically?"
>
> **Elena:** "I'll genuinely support National Security Act. No tricks this time."
>
> **Diego:** "You said you'd betray me anyway. Why should I trust you?"
>
> **Elena:** "Because now we both need each other. I have nothing, you burned your bridge with them. We're pariahs together."

**DEAL #5 RECORDED:**
- Diego-Elena Opposition Bloc
- Mutual support on each other's policies
- Goal: Force coalition to negotiate

**Anna approaches Clara privately:**

> **Anna:** "Clara, I'm vulnerable. I need your help."
>
> **Clara:** "What can you offer? You can't even sponsor policies."
>
> **Anna:** "My vote still counts. And I know Elena's planning something with Diego."
>
> **Clara:** "What do you want?"
>
> **Anna:** "Promise you won't pass any policy that increases Inequality while I'm weak. My Equality priority depends on it."
>
> **Clara:** "I can't promise that. My Prosperity priority needs Growth policies, and some increase Inequality."
>
> **Anna:** "Then we have a problem. I might vote with Elena."
>
> **Clara:** "You'd break the coalition?"
>
> **Anna:** "What coalition? You all made deals without me. Bruno lectures me about discipline. I'm reconsidering my alliances."

**Coalition Status: CRITICAL**

### Phase 3: Policy Actions

**Bruno sponsors: Fiscal Responsibility**

*Bruno pays 2 Influence (now at 3)*

"Fiscal Responsibility: Budget +2, but Social policy costs +1 Budget for 3 rounds"

> **Anna:** "This directly hurts me! Social policies are my specialty!"
>
> **Bruno:** "The nation needs Budget stability. It's not personal."
>
> **Anna:** "It feels very personal."
>
> **Elena:** "The Conservative reveals his true priorities. Austerity over people."
>
> **Diego:** "I'll support it. Budget security is good."

**Voting:**
| Player | Vote | Total | Notes |
|--------|------|-------|-------|
| Anna | No | -1 | Directly hurt |
| Bruno | Yes | +1 | Sponsor |
| Clara | Yes | +1 | Budget helps |
| Diego | Yes | +1 | Anti-social spending |
| Elena | No | -1 | Opposes austerity |

**Result:** Yes: 3, No: 2 → **PASSES**

---

**⚠️ THE COALITION BREAKS**

> 💬 **Anna:** "Bruno, we're done. You just passed a policy that specifically targets my faction."

> 💬 **Bruno:** "Anna, the nation's finances—"

> 💬 **Anna:** "I'm leaving the coalition."

**📝 DEAL #1 TERMINATED: Coalition Agreement**

```
COALITION ANALYSIS:

What Anna committed to (Round 1):
- Coalition member with Bruno and Clara
- No explicit exit clause specified

Why Anna claims this is justified:
- Bruno sponsored Fiscal Responsibility which hurts Social policies
- Social policies are Anna's faction specialty
- She feels targeted, not supported

Why others may view this as deal-breaking:
- Coalition implied mutual support
- She's leaving unilaterally without negotiation
- No warning or attempt to resolve

⚠️ RULING: Anna BROKE Deal #1
   Anna loses "never broke a deal" bonus eligibility (-2 points)
```

> **📋 DESIGN INSIGHT:** Coalition deals without exit clauses are risky.
> Anna feels justified; others feel betrayed. Both perspectives are valid.
> This is the kind of memorable drama political games should create.

**📊 DEAL BREAKERS SO FAR:**
| Player | Deal Broken | Consequence |
|--------|-------------|-------------|
| Diego | Deal #4 (abstained vs. "support") | Lost deal bonus |
| Anna | Deal #1 (left coalition unilaterally) | Lost deal bonus |

---

**Clara sponsors: Tech Sector Investment**

*Clara pays 2 Influence (now at 2)*

"Tech Investment: Budget -1, Growth +2"

> **Anna:** "I'll vote No on everything you propose now."
>
> **Clara:** "Anna, be reasonable."
>
> **Anna:** "You all just made my policies more expensive. I'm being very reasonable."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | No | -1 |
| Bruno | Yes | +1 |
| Clara | Yes | +1 |
| Diego | Yes | +1 |
| Elena | No | -1 |

**Result:** Yes: 3, No: 2 → **PASSES**

---

**Diego sponsors: National Security Act**

*Diego pays 2 Influence (now at 2)*

"National Security Act: Stability +2, Liberty -2, requires Judiciary review"

> **Bruno:** "Liberty -2 puts us at 7. That's concerning."
>
> **Elena:** "I'm keeping my word this time. Yes."
>
> **Anna:** "You're voting for Liberty erosion? After everything you've said?"
>
> **Elena:** "I'm voting to break the system. Sometimes you burn things down to rebuild better."
>
> **Clara:** "Liberty -2 is too much. I'm voting No."
>
> **Bruno:** "My Institutions priority... the Judiciary might block it anyway."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Anna | No | 0 | -1 |
| Bruno | No | 0 | -1 |
| Clara | No | 0 | -1 |
| Diego | Yes | 0 | +1 |
| Elena | Yes | 1 | +2 |

**Result:** Yes: 3, No: 3 → **TIE - FAILS**

> **Diego:** "So close!"
>
> **Elena:** "If I had one more Influence..."
>
> **Diego:** "Deal #5 is working. We forced a tie."

### Phase 4: Implementation

| Policy | Effect |
|--------|--------|
| Fiscal Responsibility | Budget +2 → 8, Social costs +1 for 3 rounds |
| Tech Investment | Budget -1 → 7, Growth +2 (partial: +1) |

### Phase 5: Consequences

**Growth at 13 > 10:** Budget +1 → 8

**Boom (3rd round):** Budget +2, Stability -1 → Budget 10, Stability 14

### End of Round 3 Summary

| Resource | Value | | Player | Influence | Alliances |
|----------|-------|--|--------|-----------|-----------|
| Budget | 10 | | Anna | 2 | INDEPENDENT (broke coalition) |
| Legitimacy | 12 | | Bruno | 4 | Coalition remnant |
| Stability | 14 | | Clara | 3 | Coalition remnant |
| Growth | 13 | | Diego | 2 | Opposition Bloc with Elena |
| Liberty | 9 | | Elena | 1 | Opposition Bloc with Diego |

**Deal Breakers So Far:**
- Diego (Deal #4 - abstained instead of supporting)
- Anna (Coalition - unilateral exit)

---

## Round 4: Realignment

### Phase 1: Events

**Infrastructure Decay triggers (from Round 2):**
- No Infrastructure policy passed → Stability -2 → 12

**Deregulation delayed effect:**
- Stability -1 → 11

**Education Reform delayed effect:**
- Growth +1 → 14, Legitimacy +1 → 13

**Religious Tensions triggers (from Round 3):**
- No addressing policy → Stability -1 → 10

**New Events:**

1. **Unity Government Proposal** (Immediate) - If all players agree: Everyone +2 Influence, Stability +3

2. **International Trade Dispute** (Immediate) - Growth -1 unless coalition of 3+ exists
   - Coalition broken! Growth -1 → 13

3. **Corruption Exposed** (Immediate) - Highest Influence player (Bruno at 4) loses 1 Influence
   - Bruno: 4 → 3

4. **Market Confidence** (Immediate) - If Budget > 8: Growth +1
   - Budget at 10 > 8 → Growth +1 → 14

5. **Election Looming** (Pending +2) - In 2 rounds: Whoever has most Influence gains +3 Legacy points

**Unity Government Vote:**

> **Bruno:** "Everyone gets +2 Influence and Stability +3. We need this."
>
> **Anna:** "I'm not unifying with people who just sabotaged me."
>
> **Elena:** "Same. No unity with elites."
>
> **Diego:** "Anna, Elena - think about it. You both have 2 and 1 Influence. You need this more than anyone."
>
> **Elena:** "Fine. But this doesn't mean we're friends."
>
> **Anna:** "...Agreed. Unity for survival."

**Unanimous agreement:** All +2 Influence, Stability +3

| Player | Before | After |
|--------|--------|-------|
| Anna | 2 | 4 |
| Bruno | 3 | 5 |
| Clara | 3 | 5 |
| Diego | 2 | 4 |
| Elena | 1 | 3 |

Stability: 10 + 3 = 13

### Phase 2: Deliberation - Strange Bedfellows

> **Diego:** "The Election is in 2 rounds. Whoever has most Influence gets +3 points. Bruno and Clara are tied at 5."
>
> **Clara:** "I need to be ahead."
>
> **Bruno:** "So do I. This changes everything."
>
> **Elena:** "You two are now rivals. Interesting."
>
> **Anna:** "Bruno passed Fiscal Responsibility against me. Clara sided with him. I have no loyalty to either anymore."
>
> **Diego:** "Anna, want to make a deal?"
>
> **Anna:** "What kind?"
>
> **Diego:** "Help me pass Industrial Policy v2. In return, I'll spend Influence to vote against Clara's policies, keeping her Influence low."
>
> **Anna:** "That's... tempting."
>
> **Clara:** "Anna, don't. We can work together again."
>
> **Anna:** "Can we? You made deals with Diego behind my back, sided with Bruno when he hurt me. Give me a reason to trust you."
>
> **Clara:** "What do you want?"
>
> **Anna:** "Support my Workers' Rights Act. It's Social policy, now costs 3 Budget because of Bruno. You vote Yes, I'll consider reconciliation."
>
> **Clara:** "Done."

**DEAL #6 RECORDED:**
- Clara supports Workers' Rights Act
- Anna considers reconciliation (non-binding)

> **Bruno (to Elena):** "You're the wild card. What do you want?"
>
> **Elena:** "I want Wealth Redistribution passed. It failed before."
>
> **Bruno:** "That hurts Growth. Clara and Diego will never support it."
>
> **Elena:** "What if you support it? Your Institutions priority doesn't care about Growth."
>
> **Bruno:** "True. And it would differentiate me from Clara for the Election bonus."
>
> **Elena:** "Exactly. You support my social policy, I support your next institutional policy."

**DEAL #7 RECORDED:**
- Bruno supports Wealth Redistribution
- Elena supports Bruno's next Institutional policy

### Phase 3: Policy Actions

**Anna sponsors: Workers' Rights Act** (costs 2 + 1 = 3 total due to Fiscal Responsibility)

*Wait - sponsoring still costs 2 Influence. The +1 Budget cost applies to Budget cost of the policy.*

*Anna pays 2 Influence (now at 2)*

"Workers' Rights Act: Liberty +1, Growth -1"

> **Clara:** "I made a deal. Yes."
>
> **Diego:** "Growth -1 when we're at 14? We can absorb that."
>
> **Bruno:** "I'll support as goodwill."
>
> **Elena:** "Yes. Workers matter."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | Yes | +1 |
| Bruno | Yes | +1 |
| Clara | Yes | +1 |
| Diego | Yes | +1 |
| Elena | Yes | +1 |

**Result:** UNANIMOUS PASS

*Anna gains +1 Influence (3), +1 Legitimacy faction bonus*

> **Anna:** "Wow. Everyone voted Yes. Is this... unity?"
>
> **Elena:** "Don't get used to it."

---

**Elena sponsors: Wealth Redistribution**

*Elena pays 2 Influence (now at 1)*

"Wealth Redistribution: Budget -1, Inequality -2, Growth -1"

> **Bruno:** "I made a deal. Yes."
>
> **Diego:** "Bruno?! You're supporting this?"
>
> **Bruno:** "Strategic considerations."
>
> **Clara:** "This kills Growth. I'm voting No with extra Influence."
>
> **Diego:** "Same. No."
>
> **Anna:** "I supported this before and I'll support it again. Yes."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Anna | Yes | 0 | +1 |
| Bruno | Yes | 0 | +1 |
| Clara | No | 2 | -3 |
| Diego | No | 1 | -2 |
| Elena | Yes | 0 | +1 |

**Result:** Yes: 3, No: 5 → **FAILS**

> **Elena:** "Clara and Diego spent Influence to kill it!"
>
> **Clara (to Diego):** "We had to. We can't let Growth crash."
>
> **Diego:** "Agreed. Temporary alliance."

**DEAL #7 HONORED by Bruno** (he voted Yes) ✓
*Elena still owes Bruno Institutional policy support*

---

**Clara sponsors: Privatization Program**

*Clara pays 2 Influence (now at 1)*

"Privatization: Budget +2, Legitimacy -1, Inequality +1"

> **Anna:** "Inequality +1! That's against my Equality priority!"
>
> **Elena:** "Same. No way."
>
> **Diego:** "Budget +2 helps. Yes."
>
> **Bruno:** "Legitimacy -1 isn't great, but we need Budget. Yes."
>
> **Anna:** "I'm voting No with extra Influence. Clara, you broke our fragile peace."
>
> **Clara:** "I need Budget to stay competitive! It's not personal!"

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Anna | No | 1 | -2 |
| Bruno | Yes | 0 | +1 |
| Clara | Yes | 0 | +1 |
| Diego | Yes | 0 | +1 |
| Elena | No | 0 | -1 |

**Result:** Yes: 3, No: 3 → **TIE - FAILS**

> **Clara:** "Anna! You blocked it!"
>
> **Anna:** "You chose Inequality. I chose Equality. This is politics."

### Phase 4 & 5: Implementation and Consequences

**Workers' Rights Act:**
- Executive roll: 3 ≤ 3 → Full
- Liberty +1 → 10, Growth -1 → 13

**Feedback Loops:**
- Growth > 10: Budget +1 → 11
- Boom continues (4th): Budget +2, Stability -1 → Budget 13, Stability 12

**Legitimacy +1 from Anna's faction bonus → 14**

### End of Round 4 Summary

| Resource | Value | | Player | Influence | Deal Status |
|----------|-------|--|--------|-----------|-------------|
| Budget | 13 | | Anna | 2 | Independent, hostile to Clara |
| Legitimacy | 14 | | Bruno | 5 | Honored Deal #7 |
| Stability | 12 | | Clara | 1 | Spent to block, low |
| Growth | 13 | | Diego | 3 | Teamed with Clara situationally |
| Liberty | 10 | | Elena | 1 | Owes Bruno |

---

## Round 5: The Election Approaches

### Phase 1: Events

**Events:**

1. **Economic Correction** (Crisis, Immediate) - If Growth ≥ 12 for 3+ rounds: Growth -4
   - Growth has been ≥12 for rounds 2, 3, 4 → YES → Growth -4 → 9

2. **Public Trust Restored** (Immediate) - If Legitimacy ≥ 14: Approval +2 → 9

3. **Institutional Review** (Immediate) - Players vote to strengthen (+1) or weaken (-1) one Institution
   - Players vote: Strengthen Judiciary wins (Anna, Bruno, Elena) → Judiciary now Strength 4

4. **Political Scandal** (Immediate) - Reveal: Elena's Influence priority exposed!

5. **Market Panic** (Immediate) - If Budget drops this round: Growth -2 additionally

> **Diego:** "Elena's priority is Influence! She wants to hoard political capital."
>
> **Elena:** "So? Power matters."
>
> **Anna:** "Both Prosperity and Influence are now public. Clara chases Growth, Elena chases Influence."

### Phase 2: Deliberation - The Final Push

**ELECTION EVENT TRIGGERS NEXT ROUND**

Current Influence standings:
1. Bruno: 5
2. Diego: 3
3. Anna: 2
4. Clara: 1
5. Elena: 1

> **Bruno:** "I'm winning the Election bonus. +3 points for most Influence."
>
> **Diego:** "Not if I sponsor a policy and get +1, while you lose Influence."
>
> **Clara:** "We need to stop Bruno. He's too far ahead."
>
> **Elena:** "Wait. I owe Bruno a favor - support his Institutional policy. But if I help him win the Election..."
>
> **Bruno:** "A deal is a deal, Elena. You gave your word."
>
> **Elena:** "And look where Diego's 'word' got him. Broken deals are part of the game now."
>
> **Anna:** "Elena, if you break this deal, you lose the 'never broke a deal' bonus. That's -2 points."
>
> **Elena:** "But Bruno gains +3 from Election if I help him. Net -5 point swing against me."
>
> **Diego:** "Break the deal. It's mathematically correct."
>
> **Elena:** "I... I need to think."

**Elena's Dilemma:**
- Keep Deal #7: Lose Election bonus (-3 vs Bruno), keep deal bonus (+2) = Net -1
- Break Deal #7: Maybe prevent Bruno win, lose deal bonus (-2) = Risky but potentially better

> **Elena:** "Bruno, what if we modify the deal?"
>
> **Bruno:** "Modify how?"
>
> **Elena:** "I support your Institutional policy, BUT you spend Influence voting, not just passively winning."
>
> **Bruno:** "That's not what we agreed."
>
> **Elena:** "Circumstances changed. The Election event didn't exist when we made the deal."
>
> **Bruno:** "Fine. I'll spend 1 Influence on my own policy vote to show good faith."

**DEAL #7 MODIFIED:**
- Elena supports Bruno's Institutional policy
- Bruno spends at least 1 Influence on his own policy vote

### Phase 3: Policy Actions

**Bruno sponsors: Constitutional Amendment** (Institutional)

*Bruno pays 2 Influence (now at 3)*

"Constitutional Amendment: Judiciary +1, Legislature +1, costs Budget -2"

> **Elena:** "I'm keeping my modified deal. Yes."
>
> **Anna:** "This is good for my Freedom priority. Liberty is protected by strong courts. Yes."
>
> **Clara:** "Budget -2 hurts, but institutions are important. Yes."
>
> **Diego:** "Everyone's voting Yes? Then I'll abstain to save Influence."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Anna | Yes | 0 | +1 |
| Bruno | Yes | 1 (per deal) | +2 |
| Clara | Yes | 0 | +1 |
| Diego | Abstain | 0 | 0 |
| Elena | Yes | 0 | +1 |

**Result:** Yes: 5, Abstain: 1 → **PASSES**

*Bruno gains +1 Influence → 3 (spent 2 sponsor + 1 vote, gained 1 for pass)*

Wait, let me recalculate:
- Bruno started at 5
- Spent 2 to sponsor → 3
- Spent 1 to vote → 2
- Gained 1 for passing → 3

**DEAL #7 FULLY HONORED** ✓

---

**Diego sponsors: Defense Contracts**

*Diego pays 2 Influence (now at 1)*

"Defense Contracts: Budget -2, Stability +1, Growth +1"

**Voting:**
All Yes (uncontroversial) → PASSES

*Diego gains +1 Influence → 2*

---

**Anna sponsors: Progressive Taxation**

*Anna pays 2 Influence (now at 0)*

"Progressive Taxation: Budget +2, Growth -1, Inequality -1"

> **Clara:** "Growth -1 again! We're at 9!"
>
> **Diego:** "If Growth drops below 8, we lose the Budget feedback."
>
> **Elena:** "Inequality -1 is good. Yes."
>
> **Bruno:** "Budget +2 offsets Clara's concerns. Yes."
>
> **Clara:** "You're all ganging up on Growth. No."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | Yes | +1 |
| Bruno | Yes | +1 |
| Clara | No | -1 |
| Diego | No | -1 |
| Elena | Yes | +1 |

**Result:** Yes: 3, No: 2 → **PASSES**

*Anna gains +1 Influence → 1*

### Phase 4 & 5: Implementation and Consequences

**Resources after policies:**
- Budget: 13 - 2 (Constitution) - 2 (Defense) + 2 (Taxation) = 11
- Stability: 12 + 1 = 13
- Growth: 9 + 1 - 1 = 9
- Inequality: 1 - 1 = 0
- Judiciary: 4 + 1 = 5
- Legislature: 3 + 1 = 4

**Feedback:** Growth at 9, not > 10, no Budget bonus

**Market Roll:** 4 > 3 → d3-2 = 0 → No change

### End of Round 5 Summary

| Resource | Value | | Player | Influence | Election Position |
|----------|-------|--|--------|-----------|-------------------|
| Budget | 11 | | Bruno | 3 | 1st |
| Legitimacy | 14 | | Diego | 2 | 2nd |
| Stability | 13 | | Anna | 1 | 3rd (tie) |
| Growth | 9 | | Clara | 1 | 3rd (tie) |
| Liberty | 10 | | Elena | 1 | 3rd (tie) |

---

## Round 6: Election Day

### Phase 1: Events

**Election Event triggers:**
- Highest Influence: Bruno at 3 → Bruno gains +3 Legacy points (noted for final scoring)

**Other Events:**

1. **Peaceful Transfer** (Immediate) - Election resolved. Legitimacy +1 → 15

2. **Post-Election Unity** (Immediate) - All players may voluntarily give 1 Influence to any other player

3. **Economic Recovery** (Immediate) - If Inequality ≤ 2: Growth +2
   - Inequality at 0 → Growth +2 → 11

4. **Institutional Maturity** (Immediate) - If any Institution at Strength 5: Legitimacy +1
   - Judiciary at 5 → Legitimacy +1 → 16

5. **Foreign Policy Success** (Immediate) - Approval +1 → 10

**Post-Election Unity:**
> **Diego:** "I'll give Elena 1 Influence. She needs it."
> **Clara:** "I'll give Anna 1 Influence. Peace offering."
> **Bruno:** "I'll keep mine."
> **Anna:** "I'll keep mine."
> **Elena:** "Thanks, Diego. Keeping mine."

**Influence after transfers:**
- Bruno: 3
- Diego: 1
- Anna: 2
- Clara: 0
- Elena: 2

### Phase 2: Deliberation - Final Round

> **Clara:** "I have 0 Influence. I can't sponsor anything."
>
> **Anna:** "You spent too much blocking my policies."
>
> **Clara:** "I was protecting Growth! It's my priority!"
>
> **Diego:** "This is the last round. What do we still need to address?"
>
> **Bruno:** "The nation is stable. We should pass something that helps our legacies."
>
> **Elena:** "I want one more Equality policy. My legacy depends on low Inequality."
>
> **Anna:** "Inequality is already 0. You're set."
>
> **Elena:** "Fair point. What about Freedom? Liberty is at 10."
>
> **Anna:** "I have Media Freedom Act: Liberty +2. Would push us to 12. +2 points for my Freedom legacy."
>
> **Diego:** "I'd support that. Good for everyone."

### Phase 3: Policy Actions

**Anna sponsors: Media Freedom Act**

*Anna pays 2 Influence (now at 0)*

"Media Freedom Act: Liberty +2, Stability -1"

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | Yes | +1 |
| Bruno | Yes | +1 |
| Clara | Abstain | 0 |
| Diego | Yes | +1 |
| Elena | Yes | +1 |

**Result:** PASSES

*Anna gains +1 Influence → 1*

---

**Elena sponsors: Anti-Corruption Commission**

*Elena pays 2 Influence (now at 0)*

"Anti-Corruption Commission: Legitimacy +1, Budget -1, Judiciary +1"

**Voting:** All Yes → PASSES

*Elena gains +1 Influence → 1*

---

**Diego sponsors: Veterans Support Act**

*Diego pays 1 Influence (now at 0)*

Wait, sponsoring costs 2. Diego only has 1.

> **Diego:** "I can't afford to sponsor. I gave my Influence to Elena."
>
> **Elena:** "Oops. Sorry."

**Bruno sponsors: Budget Stabilization**

*Bruno pays 2 Influence (now at 1)*

"Budget Stabilization: Budget +1, Growth +1"

**Voting:** All Yes → PASSES

*Bruno gains +1 Influence → 2*

### Phase 4 & 5: Final Implementation

**Resources after Round 6:**
- Budget: 11 - 1 + 1 = 11
- Legitimacy: 16 + 1 = 17 (capped at 20)
- Stability: 13 - 1 = 12
- Growth: 11 + 1 = 12
- Liberty: 10 + 2 = 12
- Inequality: 0
- Judiciary: 5 + 1 = 6 (capped at 5)

**Final Feedback:**
- Growth > 10: Budget +1 → 12

---

## Final State & Scoring

### Final National Resources

| Resource | Final Value | Notes |
|----------|-------------|-------|
| Budget | 12 | Healthy |
| Legitimacy | 17 | Excellent |
| Stability | 12 | Strong |
| Growth | 12 | Growing |
| Liberty | 12 | Free |
| Inequality | 0 | Equal |
| Approval | 10 | Maximum |

### Final Institutional Strength

| Institution | Strength |
|-------------|----------|
| Legislature | 4 |
| Judiciary | 5 |
| Executive | 3 |
| Markets | 3 |
| Public Opinion | 3 |
| Civil Society | 3 |

**THE NATION THRIVES! All collapse conditions avoided.**

---

## Legacy Scoring

### Deal Tracking Summary

| Deal | Parties | Status | Broke By |
|------|---------|--------|----------|
| #1 Coalition | Anna-Bruno-Clara | BROKEN | Anna (left) |
| #2 Industrial | Diego ↔ Coalition | HONORED | -- |
| #3 Economic | Diego ↔ Clara | HONORED | -- |
| #4 Secret Alliance | Diego ↔ Elena | BROKEN | Diego (abstained) |
| #5 Opposition Bloc | Diego ↔ Elena | HONORED | -- |
| #6 Reconciliation | Clara ↔ Anna | HONORED | -- |
| #7 Institutional | Bruno ↔ Elena | HONORED | -- |

**Deal Breakers:**
- Diego: Broke Deal #4 → Loses "never broke deal" bonus
- Anna: Broke Deal #1 (Coalition) → Loses "never broke deal" bonus

### Scoring Calculations

**Anna (Priorities: Equality, Freedom)**
- Equality: Inequality ≤ 3 → **+3 points**
- Freedom: Liberty above 10 = 12-10 = **+2 points**
- Most policies passed: No
- Never broke deal: NO (broke coalition) → **0 points**
- Predicted Approval: Not tracked
- **Anna Total: 5 points**

**Bruno (Priorities: Institutions, Order)**
- Institutions: Strength 4+ → Legislature (4) + Judiciary (5) = **+2 points**
- Order: Stability above 10 = 12-10 = **+2 points**
- Most policies passed: Let's count...
- Never broke deal: YES → **+2 points**
- **Election Bonus: +3 points** (highest Influence at election)
- **Bruno Total: 9 points**

**Clara (Priorities: Prosperity, Influence)**
- Prosperity: Growth above 5 = 12-5 = **+7 points**; Budget above 10 = 12-10 = **+2 points** = **+9 total**
- Influence: 0 remaining / 3 = **0 points**
- Most policies passed: Count needed
- Never broke deal: YES → **+2 points**
- **Clara Total: 11 points**

**Diego (Priorities: Order, Prosperity)**
- Order: Stability above 10 = **+2 points**
- Prosperity: Growth +7, Budget +2 = **+9 points**
- Never broke deal: NO (broke Deal #4) → **0 points**
- **Diego Total: 11 points**

**Elena (Priorities: Equality, Influence)**
- Equality: Inequality ≤ 3 → **+3 points**
- Influence: 1 remaining / 3 = **0 points**
- Never broke deal: YES → **+2 points**
- **Elena Total: 5 points**

### Policies Passed Count

| Player | Policies Sponsored & Passed |
|--------|----------------------------|
| Anna | 3 (Education, Workers' Rights, Progressive Tax, Media Freedom) = 4 |
| Bruno | 3 (Law and Order, Fiscal Responsibility, Constitutional Amendment, Budget Stabilization) = 4 |
| Clara | 2 (Free Trade, Deregulation, Tech Investment) = 3 |
| Diego | 3 (Industrial, National Security failed, Defense Contracts) = 2 |
| Elena | 2 (Wealth failed, Anti-Corruption) = 1 |

**Most Policies: Anna and Bruno tied at 4 each → Both get +3 points**

### Final Scores

| Place | Player | Faction | Base | Deal | Most | Election | Total |
|-------|--------|---------|------|------|------|----------|-------|
| 1st | **Clara** | Liberals | 9 | +2 | 0 | 0 | **11** |
| 1st | **Diego** | Nationalists | 11 | 0 | 0 | 0 | **11** |
| 3rd | Bruno | Conservatives | 4 | +2 | +3 | +3 | **12** |

Wait, let me recalculate Bruno:
- Institutions: +2
- Order: +2
- Never broke deal: +2
- Election: +3
- Most policies (tied): +3
Total: 2+2+2+3+3 = **12 points**

Rechecking all:

| Player | Priority 1 | Priority 2 | Deal | Most | Election | Total |
|--------|------------|------------|------|------|----------|-------|
| Anna | +3 (Eq) | +2 (Fr) | 0 | +3 | 0 | **8** |
| Bruno | +2 (Inst) | +2 (Ord) | +2 | +3 | +3 | **12** |
| Clara | +9 (Pros) | 0 (Inf) | +2 | 0 | 0 | **11** |
| Diego | +2 (Ord) | +9 (Pros) | 0 | 0 | 0 | **11** |
| Elena | +3 (Eq) | 0 (Inf) | +2 | 0 | 0 | **5** |

---

## Final Results

| Place | Player | Faction | Points | Key Factor |
|-------|--------|---------|--------|------------|
| **1st** | **Bruno** | Conservatives | **12** | Kept deals, won election, passed most policies |
| 2nd (tie) | Clara | Liberals | 11 | Prosperity payoff, but no Influence left |
| 2nd (tie) | Diego | Nationalists | 11 | Strong economy, but deal-breaking cost him |
| 4th | Anna | Progressives | 8 | Equality + Freedom, but broke coalition |
| 5th | Elena | Populists | 5 | Low Inequality, but no power |

---

## Post-Game Discussion: What We Learned About Deals

### The Deal-Breaking Analysis

**Diego's Deal #4 Break (Abstain vs Support):**
- **The Argument:** "Abstain isn't opposing, so I technically kept my word"
- **The Reality:** The table ruled this was a spirit-of-the-deal violation
- **The Lesson:** Ambiguous deal language creates conflict. Be specific: "vote Yes" vs "support"
- **The Cost:** Diego lost 2 points (deal bonus) and gained Elena as an enemy
- **Was It Worth It?** No. He tied for 2nd but would have won with the +2 bonus

**Anna's Coalition Exit:**
- **The Argument:** "Bruno made deals without my consent; I never agreed to this"
- **The Reality:** She was present during negotiations and benefited from coalition
- **The Lesson:** Implicit agreements are still agreements. Speak up in the moment or accept the deal
- **The Cost:** Lost 2 points (deal bonus), fractured natural allies
- **Was It Worth It?** Partially. She preserved her ideological integrity but lost points

### Negotiation Patterns That Emerged

**Pattern 1: The Spiral of Distrust**
- Round 1: Everyone cooperates
- Round 2: First deal tested (Diego abstains)
- Round 3: Retaliation begins (Anna leaves coalition)
- Round 4: New alliances form among the betrayed
- Round 5: Pragmatic unity returns when Election approaches

**Pattern 2: Information as Currency**
- Clara's Prosperity priority exposed → Diego extorted better terms
- Bruno's Institutions priority exposed → Players knew to avoid triggering his opposition
- Elena's Influence priority exposed → Others knew to keep her weak

**Pattern 3: The Deal Modification Trap**
- Elena successfully modified Deal #7 mid-game
- This set a precedent that deals weren't fixed
- But it also showed good faith negotiation was possible

### Memorable Moments

1. **"Welcome to politics"** - Diego's response when Elena called his abstention a betrayal

2. **The Coalition Fracture** - Anna dramatically leaving after Fiscal Responsibility passed

3. **The Unity Government Save** - All five players agreeing to cooperate for mutual survival

4. **Clara's Desperation** - Spending all Influence to block Wealth Redistribution, leaving her powerless

5. **Bruno's Patient Game** - Keeping all deals, winning Election, passing most policies = victory

### Design Insights from This Session

**What Worked:**
1. **The Deal Bonus (+2 points)** created meaningful tension around keeping/breaking promises
2. **Influence Economy** made power tangible and tradeable
3. **Secret Priorities** drove different strategies that clashed interestingly
4. **Coalition mechanics** created in-groups and out-groups dynamically

**What Could Be Improved:**
1. **Deal Ambiguity Resolution** - Need clearer rules for interpreting disputed deals
2. **Coalition Exit Rules** - When is leaving a coalition a "broken deal"?
3. **Information Asymmetry** - Priority reveals were random; could be more strategic
4. **Influence Recovery** - Players at 0-1 Influence felt helpless

### Questions for Discussion

1. **Should abstaining count as keeping a "support" deal?**
   - Option A: Yes, abstain is neutral
   - Option B: No, support means active Yes vote
   - Option C: Deals should specify (creates deal complexity)

2. **When is leaving a coalition a broken deal?**
   - Option A: Always (you committed to the group)
   - Option B: Never (coalitions are informal)
   - Option C: Only if you explicitly promised to stay

3. **Should the "never broke deal" bonus be higher?**
   - Current: +2 points
   - Diego's break cost him victory (-2 points = would have won)
   - Is that enough deterrent? Or should it be +3?

4. **Should deal-breaking have in-game consequences?**
   - Current: Only scoring penalty
   - Alternative: Reputation track affects future negotiations
   - Alternative: Other players can spend Influence to "punish" breakers

---

## Appendix: Full Deal Registry

| # | Round | Parties | Terms | Status | Notes |
|---|-------|---------|-------|--------|-------|
| 1 | 1 | Anna-Bruno-Clara | Coalition: mutual support, no Judiciary weakening | BROKEN (R3) | Anna left after Fiscal Responsibility |
| 2 | 1 | Diego ↔ Coalition | Diego supports Law&Order; Coalition supports Industrial | HONORED | Both sides delivered |
| 3 | 1 | Diego ↔ Clara | Diego supports Free Trade; Clara supports 2 Economic policies | HONORED | Modified from 1 to 2 policies |
| 4 | 2 | Diego ↔ Elena | Secret: mutual support on Security/Wealth | BROKEN | Diego abstained instead of Yes |
| 5 | 3 | Diego ↔ Elena | Opposition Bloc: coordinate against coalition | HONORED | Informal but effective |
| 6 | 4 | Clara ↔ Anna | Clara supports Workers' Rights; Anna considers reconciliation | HONORED | Clara voted Yes |
| 7 | 4 | Bruno ↔ Elena | Elena supports Institutional; Bruno spends 1 Inf | HONORED | Modified to include Inf spending |

---

## Appendix: Turn-by-Turn Influence Tracking

| Round | Anna | Bruno | Clara | Diego | Elena | Major Events |
|-------|------|-------|-------|-------|-------|--------------|
| Start | 5 | 5 | 5 | 5 | 5 | -- |
| 1 | 5 | 5 | 5 | 5 | 4 | Coalition formed (+1 each) |
| 2 | 5 | 5 | 4 | 4 | 2 | Deal #4 broken |
| 3 | 2 | 4 | 3 | 2 | 1 | Anna attacked, left coalition |
| 4 | 4 | 5 | 5 | 4 | 3 | Unity Government |
| 5 | 1 | 3 | 1 | 2 | 1 | Election preparation |
| 6 | 1 | 2 | 0 | 0 | 1 | Final round |

---

*End of Sample Game Simulation #2*
*Focus: Negotiations, Deal-Making, and Consequences of Betrayal*
*Version 1.0 - Ready for design discussion*
