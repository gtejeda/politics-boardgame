# The Political Path - Game Components Design

## Table of Contents
1. [Game Board](#game-board)
2. [Card Systems](#card-systems)
3. [Tokens & Markers](#tokens--markers)
4. [Dice System](#dice-system)
5. [Player Components](#player-components)
6. [Quick Reference Materials](#quick-reference-materials)

---

## Game Board

### Board Layout Overview

The board uses a **linear path design** representing a single government term (4-year cycle metaphor). The path contains **40 spaces** divided into 5 thematic zones.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           THE POLITICAL PATH                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║                         NATION STATE PANEL                            ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ STABILITY                                                        │  ║  │
│  ║  │ COLLAPSE◀──[-5][-4][-3][-2][-1][0][ 1][ 2][ 3][ 4][ 5]...       │  ║  │
│  ║  │            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░        │  ║  │
│  ║  │                  DANGER ZONE        SAFE      ...[ 6][ 7][ 8]   │  ║  │
│  ║  │                                               ...[ 9][10][11]   │  ║  │
│  ║  │                                     START→[10]...[12][13][14]   │  ║  │
│  ║  │                                               PROSPERITY→[15]   │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────┘  ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ BUDGET                                                           │  ║  │
│  ║  │ COLLAPSE◀──[-5][-4][-3][-2][-1][0][ 1][ 2][ 3][ 4][ 5]...       │  ║  │
│  ║  │            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░        │  ║  │
│  ║  │                  DEFICIT ZONE       BALANCED  ...[ 6][ 7][ 8]   │  ║  │
│  ║  │                                               ...START→[ 8]     │  ║  │
│  ║  │                                               ...[ 9][10][11]   │  ║  │
│  ║  │                                               ...[12][13][14]   │  ║  │
│  ║  │                                                  SURPLUS→[15]   │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────┘  ║  │
│  ║                                                                       ║  │
│  ║  ⚠ COLLAPSE WARNING: Stability ≤ 0 OR Budget ≤ -5 = ALL PLAYERS LOSE ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                              POLITICAL PATH                                  │
│                                                                              │
│   ZONE 1: EARLY TERM          ZONE 2: MID-TERM           ZONE 3: CRISIS     │
│   (Spaces 1-8)                (Spaces 9-18)              (Spaces 19-28)      │
│   ┌──┬──┬──┬──┬──┬──┬──┬──┐   ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐             │
│   │01│02│03│04│05│06│07│08├───┤09│10│11│12│13│14│15│16│17│18├──...        │
│   └──┴──┴──┴──┴──┴──┴──┴──┘   └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘             │
│   START▲                                                                     │
│   (All players begin here)                                                   │
│                                                                              │
│   ...──┐  ZONE 4: LATE TERM      ZONE 5: END OF GOVERNMENT                  │
│        │  (Spaces 29-36)         (Spaces 37-40)                              │
│   ┌──┬─┴┬──┬──┬──┬──┬──┬──┐     ┌──┬──┬──┬══╗                               │
│   │19│20│21│22│23│24│25│26├─────┤37│38│39│40║                               │
│   └──┴──┴──┴──┴──┴──┴──┴──┘     └──┴──┴──┴══╝                               │
│   ZONE 3: CRISIS                         ▲                                   │
│   (Spaces 19-28)               FINISH (Requires ≥3 Influence)               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Zone Descriptions

| Zone | Spaces | Theme | Card Difficulty | Visual Style |
|------|--------|-------|-----------------|--------------|
| **1. Early Term** | 1-8 | Coalition building, establishing agenda | Easy - moderate tradeoffs | Light blue/green, hopeful |
| **2. Mid-Term** | 9-18 | Major policy, external pressures | Medium - harder choices | Yellow/amber, challenging |
| **3. Crisis Zone** | 19-28 | High-stakes events, potential gridlock | Hard - dire consequences | Red/orange, tense |
| **4. Late Term** | 29-36 | Legacy building, final negotiations | Medium - positioning focused | Purple/twilight, strategic |
| **5. End of Government** | 37-40 | Victory determination | N/A - No new cards | Gold, triumphant |

### Special Spaces

Some spaces on the path have special effects:

| Space | Name | Effect |
|-------|------|--------|
| 1 | **Inauguration** | All players start here |
| 10 | **First Budget Review** | Draw an extra card this turn (choose one) |
| 15 | **Media Scrutiny** | All players reveal their Support Token deals |
| 20 | **Crisis Point** | If Stability < 5, draw from Crisis deck instead |
| 25 | **Opposition Rally** | Player in last place gains +1 Influence |
| 30 | **Coalition Strain** | All Support Token promises expire (return tokens) |
| 35 | **Legacy Decision** | Your next vote counts as 2 votes |
| 37-39 | **Waiting Room** | If Influence < 3, stop here until you have 3 |
| 40 | **Presidential Palace** | Victory! (if Influence ≥ 3) |

### Player Track Panel

Located on each side of the board (or as separate player boards):

```
┌────────────────────────────────────────────────────────────┐
│                    PLAYER TRACK                             │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [IDEOLOGY CARD SLOT]                                    │ │
│ │                                                         │ │
│ │      ┌─────────────────────────────────────────────┐   │ │
│ │      │              PROGRESSIVE                    │   │ │
│ │      │         ⚖️ Social Reform & Equality         │   │ │
│ │      └─────────────────────────────────────────────┘   │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                             │
│ INFLUENCE TRACK:                                            │
│ ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐                            │
│ │ 0│ 1│ 2│ 3│ 4│ 5│ 6│ 7│ 8│ 9│                            │
│ └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘                            │
│  ▓▓▓▓▓▓▓▓▓│         │▲        │░░░░░░░░░░                  │
│   WEAK    │  NORMAL │START    │ POWERFUL                    │
│   (-1 mv) │         │         │ (+1 mv)                     │
│                                                             │
│ MY SUPPORT TOKENS:    [●] [●] [●]    (3 max)               │
│ TOKENS I HOLD:        [○Bruno] [○Clara]                     │
│                                                             │
│ CURRENT POSITION: Space ___                                 │
└────────────────────────────────────────────────────────────┘
```

---

## Card Systems

### 1. Decision Cards

The core of gameplay. 5 separate decks, one per zone.

#### Card Template

```
┌─────────────────────────────────────────────────────────────┐
│ ZONE: [Early Term/Mid-Term/Crisis/Late Term]    [ICON]      │
│ CATEGORY: [Economic/Social/Security/Institutional/Crisis]   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                    ╔═══════════════════╗                     │
│                    ║   [CARD TITLE]    ║                     │
│                    ╚═══════════════════╝                     │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                                                         │ │
│  │              [SITUATION DESCRIPTION]                    │ │
│  │         2-3 sentences describing the scenario           │ │
│  │                                                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ═══════════════════════════════════════════════════════════ │
│                         OPTIONS                              │
│  ═══════════════════════════════════════════════════════════ │
│                                                              │
│  ┌─ A) [OPTION NAME] ─────────────────────────────────────┐ │
│  │  NATION: [Budget +/-X] [Stability +/-X]                 │ │
│  │  ✓ ADVANCE: [Ideology +X], [Ideology +X]                │ │
│  │  ✗ RETREAT: [Ideology -X], [Ideology -X]                │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ B) [OPTION NAME] ─────────────────────────────────────┐ │
│  │  NATION: [Budget +/-X] [Stability +/-X]                 │ │
│  │  ✓ ADVANCE: [Ideology +X], [Ideology +X]                │ │
│  │  ✗ RETREAT: [Ideology -X], [Ideology -X]                │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ C) [OPTION NAME] ─────────────────────────────────────┐ │
│  │  NATION: [Budget +/-X] [Stability +/-X]                 │ │
│  │  ✓ ADVANCE: [Ideology +X], [Ideology +X]                │ │
│  │  ✗ RETREAT: [Ideology -X]                               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│ ⚠ NO MAJORITY = Active player stuck (no movement)          │
├─────────────────────────────────────────────────────────────┤
│ 📚 HISTORICAL NOTE: [Brief real-world parallel]             │
└─────────────────────────────────────────────────────────────┘
```

#### Card Dimensions
- **Size:** Standard poker size (63mm x 88mm / 2.5" x 3.5")
- **Material:** 300gsm cardstock with linen finish

#### Deck Sizes
| Zone | Number of Cards | Difficulty Level |
|------|-----------------|------------------|
| Early Term | 20 cards | Easy |
| Mid-Term | 25 cards | Medium |
| Crisis | 20 cards | Hard |
| Late Term | 15 cards | Medium-Hard |
| **Total** | **80 cards** | - |

#### Category Distribution Per Deck

| Category | Early Term | Mid-Term | Crisis | Late Term |
|----------|------------|----------|--------|-----------|
| Economic | 5 | 6 | 4 | 4 |
| Social | 5 | 5 | 3 | 3 |
| Security | 3 | 5 | 6 | 3 |
| Institutional | 4 | 4 | 3 | 3 |
| Crisis | 3 | 5 | 4 | 2 |

#### Movement Values by Zone

| Zone | ✓ Advance Range | ✗ Retreat Range |
|------|-----------------|-----------------|
| Early Term | +1 to +2 | -1 |
| Mid-Term | +2 to +3 | -1 to -2 |
| Crisis | +2 to +4 | -1 to -2 |
| Late Term | +1 to +3 | -1 |

---

### 2. Ideology Cards

5 cards, one per ideology. Each player receives one.

#### Card Template

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│                    ╔═══════════════════╗                     │
│                    ║    PROGRESSIVE    ║                     │
│                    ╚═══════════════════╝                     │
│                                                              │
│                      [IDEOLOGY SYMBOL]                       │
│                           ⚖️                                  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ CORE CONCERN                                            │ │
│  │ Social reform, equality, progressive change             │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ YOU TYPICALLY GAIN FROM:                                │ │
│  │  • Social spending increases                            │ │
│  │  • Rights expansion                                     │ │
│  │  • Environmental protection                             │ │
│  │  • Wealth redistribution                                │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ YOU TYPICALLY LOSE FROM:                                │ │
│  │  • Austerity measures                                   │ │
│  │  • Security-focused policies                            │ │
│  │  • Traditional values emphasis                          │ │
│  │  • Market deregulation                                  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ NATURAL ALLIES: Populist                                │ │
│  │ NATURAL RIVALS: Conservative, Nationalist               │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  COLOR: 🟣 Purple         SYMBOL: ⚖️ Scales                 │
└─────────────────────────────────────────────────────────────┘
```

#### All Five Ideologies

| Ideology | Symbol | Color | Natural Allies | Natural Rivals |
|----------|--------|-------|----------------|----------------|
| **Progressive** | ⚖️ Scales | Purple | Populist | Conservative, Nationalist |
| **Conservative** | 🏛️ Pillar | Blue | Liberal | Progressive, Populist |
| **Liberal** | 🗽 Liberty | Yellow | Conservative | Nationalist, Populist |
| **Nationalist** | 🛡️ Shield | Red | Conservative | Liberal, Progressive |
| **Populist** | ✊ Fist | Orange | Progressive | Liberal, Conservative |

---

### 3. Collapse Debrief Cards

8-10 cards explaining different collapse scenarios.

#### Card Template

```
┌─────────────────────────────────────────────────────────────┐
│                    ⚠️ GOVERNMENT COLLAPSE ⚠️                 │
│                                                              │
│                    ╔═══════════════════╗                     │
│                    ║  BUDGET COLLAPSE  ║                     │
│                    ╚═══════════════════╝                     │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ WHAT HAPPENED:                                          │ │
│  │ The nation's budget fell to dangerous deficit levels.   │ │
│  │ Unable to pay debts, essential services collapsed,      │ │
│  │ and international lenders lost confidence.              │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ REAL-WORLD PARALLELS:                                   │ │
│  │ • Greece 2010-2015: Sovereign debt crisis               │ │
│  │ • Argentina 2001: Default and peso collapse             │ │
│  │ • Venezuela 2010s: Hyperinflation spiral                │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ THE LESSON:                                             │ │
│  │ Short-term popularity often conflicts with long-term   │ │
│  │ fiscal sustainability. Compromise on spending was       │ │
│  │ needed, but ideological rigidity prevented it.          │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ WHAT COULD HAVE BEEN DIFFERENT:                         │ │
│  │ • Earlier austerity with social safety nets             │ │
│  │ • Cross-ideology compromise on spending priorities      │ │
│  │ • Trading political wins for fiscal responsibility      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  📖 Discuss: What decisions led to this collapse?           │
└─────────────────────────────────────────────────────────────┘
```

#### Collapse Card Types

| Collapse Type | Trigger | Real-World Examples |
|---------------|---------|---------------------|
| Budget Collapse | Budget ≤ -5 | Greece, Argentina, Venezuela |
| Stability Collapse (Political) | Stability ≤ 0 (civil unrest) | Arab Spring, Jan 6 |
| Stability Collapse (Institutional) | Stability ≤ 0 (coup) | Chile 1973, Brazil 1964 |
| Stability Collapse (Secession) | Stability ≤ 0 (fragmentation) | Yugoslavia, Sudan |

---

### 4. Reference Cards (Player Aid)

One per player (5 total).

```
┌─────────────────────────────────────────────────────────────┐
│                      QUICK REFERENCE                         │
├─────────────────────────────────────────────────────────────┤
│ TURN STRUCTURE                                               │
│ 1. Roll dice → Draw card from current zone                   │
│ 2. Read decision aloud                                       │
│ 3. Deliberate (3 min timer)                                  │
│ 4. Vote (Yes / No / Abstain)                                 │
│ 5. Resolve → Move pawns → Update Nation Track                │
│ 6. Check for Collapse                                        │
├─────────────────────────────────────────────────────────────┤
│ SPENDING INFLUENCE                                           │
│ • 1 Influence = +1 vote weight                               │
│ • 1 Influence = Negate your backward movement                │
│ • 2 Influence = +1 bonus movement                            │
│ • 2 Influence = Force re-vote                                │
│ • 4 Influence = Veto (once per game)                         │
├─────────────────────────────────────────────────────────────┤
│ SUPPORT TOKENS                                               │
│ Give token = Promise to vote YES on their next proposal      │
│ If you break promise: They keep token + gain +1 Influence    │
│                       You lose -1 Influence                  │
├─────────────────────────────────────────────────────────────┤
│ MOVEMENT MODIFIERS                                           │
│ Your Influence ≥ 8: +1 movement                              │
│ Your Influence ≤ 2: -1 movement                              │
│ Nation Stability ≥ 12: All +1 movement                       │
│ Nation Stability ≤ 3: All -1 movement                        │
├─────────────────────────────────────────────────────────────┤
│ VICTORY: First to Space 40 with ≥3 Influence                 │
│ COLLAPSE: Stability ≤ 0 OR Budget ≤ -5 → ALL LOSE           │
└─────────────────────────────────────────────────────────────┘
```

---

## Tokens & Markers

### 1. Player Pawns

**Quantity:** 5 (one per player)
**Shape:** Political figure silhouette (standing person at podium)
**Colors:** Match ideology colors
- Purple (Progressive)
- Blue (Conservative)
- Yellow (Liberal)
- Red (Nationalist)
- Orange (Populist)

**Size:** 25mm tall, 15mm base

### 2. Support Tokens

**Quantity:** 15 total (3 per player)
**Shape:** Handshake symbol or checkmark
**Colors:** Match player colors
**Size:** 20mm diameter, 3mm thick
**Material:** Wood or thick cardboard

```
    ┌─────────┐
    │  🤝    │  ← Handshake symbol
    │ PURPLE  │  ← Player color indicator
    └─────────┘
```

### 3. Nation Track Markers

**Quantity:** 2
**Shape:** Custom shapes for visual distinction

| Marker | Shape | Color | Size |
|--------|-------|-------|------|
| Stability | Star or Shield | Gold | 20mm |
| Budget | Coin or Dollar sign | Silver | 20mm |

### 4. Influence Markers

**Quantity:** 5 (one per player)
**Shape:** Small cube or disc
**Colors:** Match player colors
**Size:** 10mm cube or 15mm disc

### 5. First Player Marker

**Quantity:** 1
**Shape:** Gavel or Capitol dome
**Color:** Gold
**Size:** 30mm

Passes clockwise each round.

### 6. Zone Indicator

**Quantity:** 1
**Shape:** Arrow or banner
**Purpose:** Marks which zone deck to draw from
**Movement:** Moves when majority of players enter a new zone

---

## Dice System

### Recommendation: 2d6 (Bell Curve)

**Why 2d6:**
- Range: 2-12 (average 7)
- Bell curve creates more predictable, strategic gameplay
- Common results (6-8) create balanced movement
- Rare extremes (2, 12) create memorable moments

### Movement Distribution

| Roll | Probability | Effect |
|------|-------------|--------|
| 2 | 2.8% | Very slow turn (crisis) |
| 3-4 | 8.3% | Below average |
| 5-6 | 13.9% | Slightly below average |
| 7 | 16.7% | Most common |
| 8-9 | 13.9% | Slightly above average |
| 10-11 | 8.3% | Above average |
| 12 | 2.8% | Excellent turn (momentum) |

### Special Roll Effects (Optional)

| Roll | Name | Effect |
|------|------|--------|
| 2 | **Political Crisis** | Draw from Crisis deck regardless of zone |
| 7 | **Compromise** | +1 to all ✓ movements on your decision |
| 12 | **Mandate** | Your vote counts as 3 this turn |

### Dice Specifications

**Quantity:** 2 standard d6
**Color:** White with black pips, or custom political themed
**Optional Custom Faces:**
- Face 1: "1"
- Face 2: "2"
- Face 3: "3"
- Face 4: "4"
- Face 5: "5"
- Face 6: "6" + small star (bonus indicator)

---

## Player Components

### Complete Player Kit (per player)

| Component | Quantity | Purpose |
|-----------|----------|---------|
| Player Pawn | 1 | Position on path |
| Ideology Card | 1 | Identity and bonuses |
| Support Tokens | 3 | Deal tracking |
| Influence Marker | 1 | Influence track |
| Reference Card | 1 | Rules summary |
| Veto Token | 1 | One-time veto (optional) |

### Veto Token (Optional Component)

**Purpose:** Physical reminder of one-time 4-Influence veto power
**Shape:** Red octagon (stop sign)
**Size:** 25mm
**Usage:** Flip face-down after using veto

```
    ┌─────────┐
    │  VETO   │  Front: Active
    │   ✋    │
    └─────────┘

    ┌─────────┐
    │  USED   │  Back: Exhausted
    │   ✗     │
    └─────────┘
```

---

## Quick Reference Materials

### 1. Turn Summary Card (Table Center)

Large card visible to all players:

```
┌─────────────────────────────────────────────────────────────┐
│                    TURN STRUCTURE                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   1. 🎲 ROLL & DRAW                                         │
│      Roll 2d6 → Draw from current zone deck                  │
│                                                              │
│   2. 📖 READ DECISION                                        │
│      Read the card aloud to all players                      │
│                                                              │
│   3. 🗣️ DELIBERATE (3 minutes)                              │
│      Negotiate, make deals, trade Support Tokens             │
│                                                              │
│   4. ✋ VOTE                                                  │
│      All vote simultaneously: Yes / No / Abstain             │
│      Spend Influence for extra votes if desired              │
│                                                              │
│   5. ✓ RESOLVE                                               │
│      If majority: Apply card effects, all move               │
│      If no majority: Active player stuck                     │
│                                                              │
│   6. ⚠️ CHECK COLLAPSE                                       │
│      Stability ≤ 0 OR Budget ≤ -5 = GAME OVER               │
│                                                              │
│   7. ➡️ NEXT PLAYER                                          │
│      Pass First Player marker clockwise                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2. Ideology Quick Reference (Table Center)

```
┌─────────────────────────────────────────────────────────────┐
│                    IDEOLOGY SUMMARY                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🟣 PROGRESSIVE  │ Social reform, equality, spending        │
│  🔵 CONSERVATIVE │ Tradition, stability, fiscal restraint   │
│  🟡 LIBERAL      │ Markets, individual liberty, free trade  │
│  🔴 NATIONALIST  │ Sovereignty, security, borders           │
│  🟠 POPULIST     │ Anti-establishment, redistribution       │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  TYPICAL ALLIANCES                                           │
│  Progressive ↔ Populist (social spending)                    │
│  Conservative ↔ Liberal (fiscal policy)                      │
│  Conservative ↔ Nationalist (security)                       │
│  Liberal ↔ Progressive (social issues)                       │
└─────────────────────────────────────────────────────────────┘
```

### 3. Sand Timer

**Duration:** 3 minutes
**Purpose:** Deliberation phase time limit
**Alternative:** Phone timer app

---

## Complete Component List

### Box Contents

| Component | Quantity | Notes |
|-----------|----------|-------|
| Game Board | 1 | Folding, approx. 50cm x 50cm |
| Decision Cards - Early Term | 20 | Blue-green back |
| Decision Cards - Mid-Term | 25 | Yellow back |
| Decision Cards - Crisis | 20 | Red back |
| Decision Cards - Late Term | 15 | Purple back |
| Ideology Cards | 5 | Unique backs |
| Collapse Debrief Cards | 8 | Black back |
| Player Reference Cards | 5 | One per player |
| Turn Summary Card | 1 | Large, table center |
| Ideology Summary Card | 1 | Large, table center |
| Player Pawns | 5 | 5 colors |
| Support Tokens | 15 | 3 per color |
| Influence Markers | 5 | 5 colors |
| Stability Marker | 1 | Gold star |
| Budget Marker | 1 | Silver coin |
| First Player Marker | 1 | Gavel |
| Zone Indicator | 1 | Arrow |
| Veto Tokens | 5 | Optional rule |
| Standard Dice (d6) | 2 | White |
| Sand Timer | 1 | 3 minutes |
| Rulebook | 1 | - |

---

## Design Notes & Rationale

### Why 40 Spaces?

- **Average rolls:** 7 per turn with 2d6
- **Turns to finish:** ~6-7 turns just rolling (without bonuses/penalties)
- **With mechanics:** 8-12 turns typical game
- **Time estimate:** 45-60 minutes with 4 players

### Why Linear Over Circular?

- **Clear goal:** Finish line creates urgency
- **Thematic fit:** Government term has a defined end
- **Simpler teaching:** No lap counting or position confusion
- **Tension curve:** Natural escalation through zones

### Card Balance Philosophy

Each decision card should:
1. **Never have an obvious choice** - All options trade something
2. **Create coalitions** - Two ideologies benefit from each option
3. **Affect the nation** - Budget and/or Stability always change
4. **Enable deals** - Players marked ✗ can negotiate for compensation

### Support Token Design Rationale

Physical tokens for deals because:
- **Visible accountability** - Everyone sees who owes whom
- **Strategic depth** - Token management becomes a resource
- **Social pressure** - Breaking visible promises feels worse
- **Memory aid** - No "did you promise me?" arguments
