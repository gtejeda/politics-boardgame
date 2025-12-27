# Event Cards

This directory contains event card designs that introduce external pressures and uncertainty.

---

## Event Design Principles

> Charter Ref: Principle 4 - "Information Is Imperfect but Not Arbitrary"

Events create uncertainty but should:
1. Be explainable (players understand why this could happen)
2. Create pressure without determining outcomes
3. Offer response choices, not just impose effects
4. Reflect systemic causes, not random chaos

---

## Event Card Template

```yaml
name: [Event Name]
category: [economic | social | political | international | natural]
severity: [minor | moderate | major | crisis]

# Trigger Conditions (why this event makes sense now)
trigger_logic:
  - condition: [What state makes this plausible]
  - probability_modifier: [What increases/decreases likelihood]

# Event Effects
immediate_pressure:
  - resource: [resource_name]
    effect: [description]

# Response Options
responses:
  - name: [Response A]
    cost: [resources required]
    effect: [immediate result]
    delayed_effect: [future consequences]

  - name: [Response B]
    cost: [resources required]
    effect: [immediate result]
    delayed_effect: [future consequences]

# If no response / insufficient response
default_outcome:
  - effect: [What happens if players cannot or do not respond]

# Flavor
description: [Neutral description of what's happening]
historical_parallels: [Optional real-world examples]

# Charter Compliance
charter_check:
  - explainable_randomness: [yes/no]
  - offers_choice: [yes/no]
  - neutral_framing: [yes/no]
```

---

## Categories

### /economic
Market crashes, trade disruptions, resource shocks, technological shifts

### /social
Public movements, demographic changes, cultural shifts, public health

### /political
Scandals, electoral surprises, coalition shifts, institutional challenges

### /international
Wars, treaties, sanctions, global crises, migration

### /natural
Disasters, climate events, pandemics, resource discoveries

---

## Event Deck Composition

The event deck should be composed to:
- Avoid long stretches of same-type events
- Scale severity appropriately (more minor, fewer crisis)
- Include some predictable cycles (elections, budget deadlines)
- Allow for "quiet" periods where players drive action

Suggested ratio:
- Minor: 40%
- Moderate: 35%
- Major: 20%
- Crisis: 5%
