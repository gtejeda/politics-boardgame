# Version 1: Initial Design

**Status:** Archived (Playtest Complete)
**Date:** December 2024

## Overview

This is the original design of the political governance board game. It represents the first complete iteration of the core systems, mechanics, and content.

## What This Version Contains

### Core Design
- **5 Factions**: Progressives, Conservatives, Liberals, Nationalists, Populists
- **5 National Resources**: Budget, Legitimacy, Stability, Growth, Liberty
- **6 Institutions**: Legislature, Judiciary, Executive, Markets, Public Opinion, Civil Society
- **Semi-cooperative gameplay**: Survive together, but only one wins

### Game Structure
- 8-12 rounds (90-120 minutes)
- 6 phases per round: Events → Deliberation → Policy Actions → Implementation → Consequences → Refresh
- Delayed effects timeline system
- Secret legacy priorities for individual scoring

### Content
- 60 Policy cards (12 per category)
- 40 Event cards
- Sample scenarios

## Playtest Results

Two simulated games were conducted:
- `game-01`: 4 players, focused on basic mechanics
- `game-02`: 5 players, focused on negotiation and deal-making

### Key Findings

**Onboarding Issues:**
- Faction selection process unclear (random vs. preference-based)
- Influence bonus sources not explained at start
- Secret legacy priority selection lacks clear procedure
- Starting hand cards are random, creating disconnect with faction identity

**Cognitive Load Issues:**
- Events require political expertise to evaluate effectively
- Coalition formation mechanics unclear
- Card secrecy rules not explicitly stated
- Deliberation phase complexity barrier

**Structural Issues:**
- 6 institutions may be too many to track
- First player event draw procedure unclear
- Connection between events, policies, and player goals not intuitive

## Files in This Version

```
v1/
├── design/
│   ├── rules/
│   │   ├── core-rules-v1.md      # Full rulebook
│   │   └── quick-start-v1.md     # 1-page summary
│   ├── core-systems/
│   │   ├── resources.md          # Resource definitions
│   │   ├── institutions.md       # Institution mechanics
│   │   └── feedback-loops.md     # Automatic effects
│   ├── mechanics/
│   │   ├── turn-structure.md     # Phase breakdown
│   │   └── victory-conditions.md # Win/lose states
│   ├── content/
│   │   ├── events/               # Event card designs
│   │   ├── policies/             # Policy card designs
│   │   └── scenarios/            # Game scenarios
│   └── graphic/                  # Visual assets (PNG)
├── docs/
│   ├── charter.md                # Project charter
│   ├── design-decisions.md       # Decision log
│   └── glossary.md               # Term definitions
└── assets/
    └── README.md                 # Asset guidelines
```

## Lessons for v2

Based on playtest feedback, the next version should address:

1. **Simplify onboarding** - Reduce decisions required before understanding the system
2. **Reduce cognitive load** - Make tradeoffs immediately visible without expertise
3. **Clarify procedures** - Explicit step-by-step setup and turn structure
4. **Consider reducing complexity** - Fewer institutions, simpler event resolution
5. **Faction-aligned starting hands** - Connect identity to agency from turn 1
