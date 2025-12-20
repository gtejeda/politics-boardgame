# Scenarios

Scenarios define the starting conditions, available policies, and special rules for a game session.

---

## Scenario Design Principles

> Charter Ref: Principle 14 - "Design for Expansion Without Rewrites"

Scenarios should:
1. Use base mechanics without modifications
2. Adjust starting conditions and available content
3. Represent different political contexts faithfully
4. Be balanced for the same player experience quality

---

## Scenario Template

```yaml
name: [Scenario Name]
setting: [Country/Region, Time Period]
player_count: [Recommended range]
game_length: [Rounds or time estimate]

# Starting Conditions
initial_resources:
  budget: [number]
  legitimacy: [number]
  stability: [number]
  growth: [number]
  liberty: [number]

# Institutional Setup
institutions:
  legislature:
    type: [unicameral | bicameral | etc.]
    special_rules: [any modifications]
  judiciary:
    independence_level: [low | medium | high]
    special_rules: [any modifications]
  # ... etc.

# Available Content
policy_deck:
  include: [list of policy categories/cards]
  exclude: [list of excluded content]
  special_additions: [scenario-specific policies]

event_deck:
  include: [list of event categories/cards]
  exclude: [list of excluded content]
  guaranteed_events: [events that will definitely occur]

# Victory Condition Modifications
victory_adjustments:
  - [Any scenario-specific victory conditions]

# Special Rules
scenario_rules:
  - rule: [Description]
    rationale: [Why this reflects the scenario's reality]

# Historical Context (for educational value)
context:
  background: [Brief neutral description]
  key_tensions: [What makes this scenario interesting]
  historical_outcome: [What actually happened, for post-game discussion]

# Charter Compliance
charter_check:
  - uses_base_mechanics: [yes/no]
  - ideologically_neutral_framing: [yes/no]
  - playable_from_multiple_perspectives: [yes/no]
```

---

## Scenario Categories

### /base-game
The default scenario(s) included in the core game. Should be:
- Accessible to new players
- Representative of core mechanics
- Not tied to a specific controversial context

### /historical
Real historical settings. Extra care needed for:
- Neutral framing
- Multiple valid perspectives
- Educational accuracy

### /contemporary
Modern settings. Highest risk for bias, requires:
- Careful balance review
- Explicit neutrality checks
- Possibly regional variants

### /hypothetical
Fictional or abstract settings. Useful for:
- Exploring mechanics without baggage
- Teaching specific concepts
- Avoiding real-world controversy

---

## Base Game Scenario Candidates

1. **"The Republic"** - A fictional democratic nation facing modernization
2. **"Transition"** - A country moving from one system to another
3. **"Federation"** - A multi-region system with federal dynamics
4. **"The Crisis"** - A nation facing multiple simultaneous pressures
