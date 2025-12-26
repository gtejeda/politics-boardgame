# Sample Game Simulation #2: Five Factions - The Art of the Deal

> **Purpose:** This simulation focuses on negotiations, coalition-building, deal-making, and the dramatic consequences of breaking promises. Designed to explore the social dynamics that make political games memorable.

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

### Phase 1: Events

**Events Revealed (5 cards for 5 players):**

1. **Coalition Formation Pressure** (Immediate) - First Player must declare a governing coalition of 2-3 players. Coalition members get +1 Influence but share responsibility.

2. **Economic Downturn Warning** (Pending +2) - In 2 rounds: Growth -2 unless Economic policy passed

3. **Border Tensions** (Pending +1) - In 1 round: Stability -1 unless Security response

4. **Civil Rights Movement** (Immediate) - If Liberty < 10: Legitimacy -1. Currently Liberty = 10, no effect.

5. **Corruption Scandal** (Immediate) - Lowest Influence player gains +1 Influence (public sympathy). All tied at 5, so no effect.

**Coalition Formation - The First Big Negotiation:**

> **Anna (First Player):** "I need to form a governing coalition. Who wants in?"
>
> **Diego:** "I'll join if you promise to support a Security policy for the border tensions."
>
> **Anna:** "Security usually hurts Liberty. That's against my principles."
>
> **Diego:** "Then find someone else. But good luck passing anything without votes."
>
> **Clara:** "I'll join your coalition, Anna. I just want Economic policies to pass. I won't demand anything ideological."
>
> **Bruno:** "I'm interested too. I want institutional stability. If you promise not to weaken the Judiciary, I'm in."
>
> **Elena:** "Coalition governments are just elite power-sharing. Count me out. I'll be the opposition."
>
> **Anna:** "Okay. Clara and Bruno - we're the governing coalition."

**DEAL #1 RECORDED:**
- Coalition: Anna, Clara, Bruno
- Anna promises: No policies weakening Judiciary
- Clara promises: Support Anna's Social policies
- Bruno promises: General coalition support

*Coalition members (Anna, Clara, Bruno) each gain +1 Influence → now at 6*

### Phase 2: Deliberation

> **Diego:** "So the three of you run everything now? That's 3 votes automatically. You only need simple majority."
>
> **Elena:** "We'll see how long that lasts. Coalitions always break."
>
> **Anna:** "Let's focus. Border tensions hit next round. We need a plan."
>
> **Bruno:** "I have Law and Order Initiative: Stability +2, Liberty -1. It's Security-adjacent."
>
> **Anna:** "Liberty -1... I don't love it, but it's not as bad as Diego's options."
>
> **Diego:** "My National Security Act is better. Stability +2, but Liberty -2."
>
> **Anna:** "Absolutely not."
>
> **Clara:** "What about Economic policy? The downturn warning is coming."
>
> **Elena:** "You're all just protecting your own interests. What about the people? I have Wealth Redistribution: Budget -1, Inequality -2, but Growth -1."
>
> **Clara:** "Growth -1 when we're at 5? That's dangerous."
>
> **Elena:** "See? The elite coalition protects Growth over equality. Typical."

**Coalition Sidebar (Anna, Clara, Bruno huddle):**

> **Anna (whispered):** "Let's pass Free Trade for Clara, and Law and Order for the border issue."
>
> **Clara:** "Deal. I'll sponsor Free Trade."
>
> **Bruno:** "I'll sponsor Law and Order. But Anna, you promised no Judiciary weakening. This might get reviewed."
>
> **Anna:** "It reduces Liberty, so Judiciary reviews it. If it's blocked, that's fine with me honestly."

**Diego approaches the coalition:**

> **Diego:** "I'll vote for your Law and Order if you vote for my Industrial Policy next round."
>
> **Bruno:** "What's Industrial Policy?"
>
> **Diego:** "Budget -2, Growth +1, Stability +1. Nothing controversial."
>
> **Anna:** "That's acceptable. Deal?"
>
> **Bruno:** "Deal."

**DEAL #2 RECORDED:**
- Diego supports Law and Order (Round 1)
- Coalition supports Industrial Policy (Round 2)

### Phase 3: Policy Actions

**Clara sponsors: Free Trade Agreement**

*Clara pays 2 Influence (now at 4)*

"Free Trade: Growth +2 now, delayed (2 rounds): Budget +1, Inequality +1"

> **Elena:** "Inequality +1? I'm voting No."
>
> **Diego:** "What do I get if I vote Yes?"
>
> **Clara:** "You already have a deal for Industrial Policy."
>
> **Diego:** "That's with Bruno, not you. I want something else."
>
> **Clara:** "Fine. I'll support one Economic policy of your choice later."
>
> **Diego:** "Deal."

**DEAL #3 RECORDED:**
- Diego supports Free Trade (Round 1)
- Clara supports one Diego Economic policy (future)

**Voting:**
| Player | Vote | Influence Spent | Total | Notes |
|--------|------|-----------------|-------|-------|
| Anna | Yes | 0 | +1 | Coalition obligation |
| Bruno | Yes | 0 | +1 | Coalition support |
| Clara | Yes | 0 | +1 | Sponsor |
| Diego | Yes | 0 | +1 | Deal #3 |
| Elena | No | 0 | -1 | Ideological opposition |

**Result:** Yes: 4, No: 1 → **PASSES**

*Clara gains +1 Influence (5), +1 Growth faction bonus*

---

**Bruno sponsors: Law and Order Initiative**

*Bruno pays 2 Influence (now at 4)*

"Law and Order: Stability +2, Liberty -1. Requires Judiciary review."

> **Elena:** "Liberty erosion begins. The authoritarians show their true colors."
>
> **Anna:** "It's -1, Elena. We need Stability for the border crisis."
>
> **Elena:** "You're already compromising your principles, Progressive."

**Voting:**
| Player | Vote | Influence Spent | Total |
|--------|------|-----------------|-------|
| Anna | Yes | 0 | +1 |
| Bruno | Yes | 0 | +1 |
| Clara | Yes | 0 | +1 |
| Diego | Yes | 0 | +1 |
| Elena | No | 1 | -2 |

**Result:** Yes: 4, No: 2 → **PASSES**

**Judiciary Review:** Roll d6 = **4** vs Judiciary Strength 3
- 4 > 3 → NOT BLOCKED

*Bruno gains +1 Influence (5)*

---

**Anna sponsors: Education Reform**

*Anna pays 2 Influence (now at 4)*

"Education Reform: Budget -2, delayed (3 rounds): Growth +2, Legitimacy +1"

> **Diego:** "Why should I support this? It doesn't help me."
>
> **Anna:** "Because the nation needs educated citizens. And I'm asking nicely."
>
> **Diego:** "Asking nicely doesn't pay bills. Give me something."
>
> **Elena:** "I'll support it. Education helps equality."
>
> **Diego:** "Without my vote it's 3-1. It passes anyway. I'll abstain."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | Yes | +1 |
| Bruno | Yes | +1 |
| Clara | Yes | +1 |
| Diego | Abstain | 0 |
| Elena | Yes | +1 |

**Result:** Yes: 4, No: 0 → **PASSES**

*Anna gains +1 Influence (5), +1 Legitimacy faction bonus*

---

**Maximum 3 policies passed. Diego and Elena cannot sponsor this round.**

### Phase 4: Implementation

| Policy | Judiciary | Executive Roll | Result |
|--------|-----------|----------------|--------|
| Free Trade | N/A | 3 ≤ 3 | Full: Growth +2 |
| Law and Order | Passed (4>3) | 2 ≤ 3 | Full: Stability +2, Liberty -1 |
| Education Reform | N/A | 5 > 3 | Partial: Budget -2 |

**Delayed Effects Placed:**
- Round 3: Free Trade → Budget +1, Inequality +1
- Round 4: Education Reform → Growth +1, Legitimacy +1 (reduced)

### Phase 5: Consequences

**Resource Changes:**
- Budget: 8 - 2 = 6
- Stability: 10 + 2 = 12
- Growth: 5 + 2 + 1 (Clara bonus) = 8
- Liberty: 10 - 1 = 9
- Legitimacy: 10 + 1 (Anna bonus) = 11

**Feedback Loops:** None triggered

**Market Roll:** d6 = 5 > 3 → Roll d3-2 = 1-2 = -1 → Growth 8-1 = 7

### End of Round 1 Summary

| Resource | Value | | Player | Influence | Deals Active |
|----------|-------|--|--------|-----------|--------------|
| Budget | 6 | | Anna | 5 | Coalition, #2 |
| Legitimacy | 11 | | Bruno | 5 | Coalition, #2 |
| Stability | 12 | | Clara | 5 | Coalition, #3 |
| Growth | 7 | | Diego | 5 | #2, #3 |
| Liberty | 9 | | Elena | 4 | None |

**Active Deals:**
1. Coalition Agreement (Anna-Clara-Bruno)
2. Industrial Policy Deal (Diego ↔ Coalition)
3. Economic Policy Deal (Diego ↔ Clara)

---

## Round 2: The First Test of Trust

### Phase 1: Events

**Border Tensions triggers:**
- Security policy passed (Law and Order) → Effect negated!

**New Events:**

1. **Media Investigation** (Immediate) - Reveal one random player's Legacy priority. Roll d6 for player: **3 = Clara**
   - Clara's Prosperity priority revealed!

2. **Labor Union Demands** (Immediate) - If no Worker policy passed: Legitimacy -1, Growth -1

3. **Foreign Investment Offer** (Immediate) - Accept: Growth +2, Liberty -1. Reject: Nothing.

4. **Infrastructure Decay** (Pending +2) - In 2 rounds: Stability -2 unless Infrastructure policy

> **Elena:** "Clara's priority is Prosperity. Of course the Liberal wants Growth above all else. Don't trust her deals."
>
> **Clara:** "My priorities are public now. So what? Growth helps everyone."
>
> **Diego:** "Interesting. So you'll do anything to maximize Growth..."

**Foreign Investment Vote:**

> **Anna:** "Accept means Liberty -1. We're already at 9."
>
> **Clara:** "But Growth +2! That's huge!"
>
> **Diego:** "I'll vote Accept if Clara gives me a better deal on her promise."
>
> **Clara:** "What do you want?"
>
> **Diego:** "Support TWO of my Economic policies, not one."
>
> **Clara:** "That's extortion."
>
> **Diego:** "That's negotiation. Your priority is exposed. I know you want this."

**DEAL #3 MODIFIED:**
- Clara now owes Diego support on TWO Economic policies

**Vote on Foreign Investment:** Accept: 3 (Clara, Diego, Bruno), Reject: 2 (Anna, Elena)
- Growth +2 → 9, Liberty -1 → 8

**Labor Union Demands:** No Worker policy → Legitimacy -1 → 10, Growth -1 → 8

### Phase 2: Deliberation - The Coalition Fractures

> **Diego:** "Time for you to honor Deal #2. I want votes for Industrial Policy."
>
> **Bruno:** "We agreed. Anna, Clara - we have to support it."
>
> **Anna:** "I never agreed to that deal. Bruno made it without asking me."
>
> **Bruno:** "You were standing right there!"
>
> **Anna:** "I was negotiating the coalition terms. I didn't agree to Industrial Policy."
>
> **Diego:** "Are you breaking the deal?"
>
> **Anna:** "I'm not bound by deals I didn't make."
>
> **Bruno:** "Anna, if you don't support this, Diego will never work with us again."
>
> **Clara:** "And I owe him two Economic policies now. I need him cooperative."
>
> **Elena (watching with amusement):** "The coalition is cracking already. Beautiful."

**Anna's Dilemma:**
- Support Industrial Policy: Maintains coalition unity but sets precedent that others can make deals for her
- Oppose: Breaks coalition trust, makes Diego an enemy, but maintains her independence

> **Anna:** "Fine. I'll support Industrial Policy. But Bruno - never make deals for me again without my explicit agreement. Understood?"
>
> **Bruno:** "Understood. I apologize."

**Elena approaches Diego privately:**

> **Elena (whispered):** "The coalition is weak. Anna almost defected. Help me destabilize them and I'll support your Security policies."
>
> **Diego:** "Why would I trust you? You're anti-establishment."
>
> **Elena:** "Exactly. I want to tear down their cozy arrangement. You want power. We can help each other."
>
> **Diego:** "I'll consider it. But I want a specific commitment."
>
> **Elena:** "Name it."
>
> **Diego:** "When I sponsor National Security Act, you vote Yes."
>
> **Elena:** "That's Liberty -2. My voters would hate that."
>
> **Diego:** "Do you want to break the coalition or not?"
>
> **Elena:** "...Deal. But only if you help me pass Wealth Redistribution afterward."

**SECRET DEAL #4 RECORDED:**
- Elena supports National Security Act (Diego's)
- Diego supports Wealth Redistribution (Elena's)
- Goal: Destabilize coalition

### Phase 3: Policy Actions

**First Player: Bruno**

---

**Diego sponsors: Industrial Policy** (Deal #2)

*Diego pays 2 Influence (now at 3)*

"Industrial Policy: Budget -2, Growth +1, Stability +1"

> **Elena:** "I'm voting No. Not part of any elite deal."
>
> **Anna (reluctantly):** "I'll honor the coalition agreement."

**Voting:**
| Player | Vote | Total | Notes |
|--------|------|-------|-------|
| Anna | Yes | +1 | Reluctant coalition support |
| Bruno | Yes | +1 | Deal #2 |
| Clara | Yes | +1 | Coalition + owes Diego |
| Diego | Yes | +1 | Sponsor |
| Elena | No | -1 | Opposition |

**Result:** Yes: 4, No: 1 → **PASSES**

*Diego gains +1 Influence (4), +1 Stability faction bonus*

**Deal #2 HONORED** ✓

---

**Clara sponsors: Deregulation Act**

*Clara pays 2 Influence (now at 3)*

"Deregulation: Growth +2, Liberty +1, delayed (2 rounds): Stability -1"

> **Anna:** "Liberty +1 helps recover from Foreign Investment. I'll support."
>
> **Bruno:** "But delayed Stability -1. That's concerning."
>
> **Clara:** "We're at 13 Stability. We can afford it."
>
> **Diego:** "This counts as one of the two Economic policies you owe me, Clara."
>
> **Clara:** "Wait, you're supposed to support MY policies, not the other way around."
>
> **Diego:** "You owe me support. I don't owe you anything on this one."
>
> **Clara:** "Then vote Yes and I'll count it as you supporting me."
>
> **Diego:** "Hmm. Deal. Yes."

**Voting:**
| Player | Vote | Total |
|--------|------|-------|
| Anna | Yes | +1 |
| Bruno | Yes | +1 |
| Clara | Yes | +1 |
| Diego | Yes | +1 |
| Elena | No | -1 |

**Result:** PASSES

*Clara gains +1 Influence (4), +1 Growth faction bonus*

---

**Elena sponsors: Wealth Redistribution**

*Elena pays 2 Influence (now at 2)*

"Wealth Redistribution: Budget -1, Inequality -2, Growth -1"

> **Clara:** "Growth -1?! We're only at 9 after my policy. No way."
>
> **Anna:** "But Inequality -2 is good. I care about equality."
>
> **Bruno:** "Coalition solidarity says we vote together. Clara opposes, so we all oppose?"
>
> **Anna:** "I'm not bound by coalition on everything. This aligns with my values."
>
> **Bruno:** "Anna, if you break coalition discipline, we're done."
>
> **Diego (to Elena, quietly):** "I can't support this publicly. It kills Growth. I'm abstaining."
>
> **Elena:** "You promised!"
>
> **Diego:** "I promised to support it. Abstain is not opposing. Technically keeping my word."
>
> **Elena:** "That's a betrayal of spirit!"
>
> **Diego:** "Welcome to politics."

**Voting:**
| Player | Vote | Influence Spent | Total | Notes |
|--------|------|-----------------|-------|-------|
| Anna | Yes | 0 | +1 | Values over coalition |
| Bruno | No | 0 | -1 | Coalition with Clara |
| Clara | No | 1 | -2 | Opposes Growth hit |
| Diego | Abstain | 0 | 0 | Technicality |
| Elena | Yes | 0 | +1 | Sponsor |

**Result:** Yes: 2, No: 3 → **FAILS**

> **Elena:** "Diego, you traitor! You abstained!"
>
> **Diego:** "I didn't vote against you. That was the deal."
>
> **Elena:** "The deal was SUPPORT, not abstain!"
>
> **Anna:** "You two had a secret deal?"

**SECRET DEAL #4 EXPOSED - CONTESTED**
- Diego claims: "Abstain is not opposition, deal honored"
- Elena claims: "Support means Yes vote, deal broken"

**Group Ruling Required:**
> **Bruno:** "Let's vote on whether Diego broke the deal."
>
> Vote: Diego broke deal (Anna, Elena) vs Diego kept deal (Clara, Diego)
> Bruno abstains as arbiter.
>
> **Bruno:** "Tied. As neutral party, I rule: The word 'support' implies active Yes vote. Diego broke the deal in spirit."

**DEAL #4 RULING: BROKEN by Diego**

*Diego loses "never broke a deal" bonus eligibility*

> **Diego:** "Fine. But Elena, our arrangement for National Security Act is void then."
>
> **Elena:** "Gladly. I was going to betray you anyway."

### Phase 4: Implementation

| Policy | Executive Roll | Result |
|--------|----------------|--------|
| Industrial Policy | 2 ≤ 3 | Full: Budget -2, Growth +1, Stability +1 +1 (Diego) |
| Deregulation Act | 4 > 3 | Partial: Growth +1, Liberty +1 |

**Delayed Effects Placed:**
- Round 4: Deregulation → Stability -1

**Resources after Round 2:**
- Budget: 6 - 2 = 4
- Stability: 13 + 2 = 15
- Growth: 8 + 1 + 1 + 1 (partial) = 11 (Wait, let me recalculate)
  - Start: 8, Industrial +1, Deregulation partial +1, Clara bonus +1 = 11
- Liberty: 8 + 1 = 9

### Phase 5: Consequences

**Feedback Loops:**
- Growth > 10: Budget +1 → 5
- Stability > 15 AND Liberty < 8? Stability is 15, Liberty is 9. No Security State.

**Market Roll:** d6 = 2 ≤ 3 → Growth +1 → 12

### End of Round 2 Summary

| Resource | Value | | Player | Influence | Deal Status |
|----------|-------|--|--------|-----------|-------------|
| Budget | 5 | | Anna | 5 | Coalition (strained) |
| Legitimacy | 10 | | Bruno | 5 | Coalition |
| Stability | 15 | | Clara | 4 | Coalition, owes Diego 1 more |
| Growth | 12 | | Diego | 4 | BROKE Deal #4 |
| Liberty | 9 | | Elena | 2 | Betrayed, isolated |

**Trust Status:**
- Anna-Bruno: Tense (Anna broke coalition discipline)
- Diego-Elena: Hostile (deal broken)
- Coalition: Fragile

---

## Round 3: Revenge Politics

### Phase 1: Events

**Free Trade delayed effect triggers:**
- Budget +1 → 6, Inequality +1 → 1

**Events:**

1. **Political Assassination Attempt** (Crisis, Immediate) - Target: Highest Influence player. Roll d6: 1-2 = loses 3 Influence, 3-4 = loses 1 Influence, 5-6 = no effect
   - Highest: Anna and Bruno tied at 5. Roll for target: Anna
   - Roll for effect: **2** → Anna loses 3 Influence! (5 → 2)

2. **Economic Boom Celebration** (Immediate) - If Growth ≥ 10: Approval +2

3. **Religious Tensions** (Moderate, Pending +1) - Next round: Stability -1 unless addressed

4. **Anti-Corruption Campaign** (Immediate) - All players vote: Support (Legitimacy +2, but reveal another Legacy priority) or Oppose (Legitimacy -1)

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

> **Anna:** "Bruno, we're done. You just passed a policy that specifically targets my faction."
>
> **Bruno:** "Anna, the nation's finances—"
>
> **Anna:** "I'm leaving the coalition."

**COALITION BROKEN by Anna**

*Anna loses "never broke a deal" bonus eligibility (left coalition without mutual agreement)*

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
