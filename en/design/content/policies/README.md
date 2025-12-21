# Policy Cards

This directory contains policy card designs organized by category.

---

## Policy Design Principles

> Charter Ref: Principle 2 - "Tradeoffs Are Mandatory"
> Charter Ref: Principle 5 - "Consequences Are Often Delayed"

Every policy card must have:

1. **Clear effect:** What it does mechanically
2. **Tradeoff:** What pressure it creates
3. **Institutional path:** How it gets implemented
4. **Timing:** Immediate vs. delayed effects

---

## Policy Card Template

```yaml
name: [Policy Name]
category: [economic | social | security | institutional | foreign]
ideological_lean: [left | right | neutral]  # For balance tracking only, not gameplay

# Costs
budget_cost: [number]
political_cost: [number]  # Legitimacy spent to propose
institutional_requirement: [legislature_majority | supermajority | executive_only | etc.]

# Immediate Effects
immediate:
  - resource: [resource_name]
    change: [+/- number]

# Delayed Effects
delayed:
  - resource: [resource_name]
    change: [+/- number]
    delay_rounds: [number]
    condition: [optional trigger condition]

# Tradeoffs
tradeoff_pressure:
  - resource: [resource_name]
    effect: [description of pressure created]

# Flavor
description: [Brief neutral description]
historical_parallel: [Optional real-world reference]

# Charter Compliance
charter_check:
  - has_tradeoff: [yes/no]
  - neutral_framing: [yes/no]
  - institutional_path: [yes/no]
  - delayed_component: [yes/no/na]
```

---

## Categories

### /economic
Tax policy, spending, regulation, trade, monetary policy

### /social
Welfare, education, healthcare, housing, labor

### /security
Military, police, intelligence, emergency powers, borders

### /institutional
Electoral reform, judicial changes, constitutional amendments

### /foreign
Diplomacy, alliances, sanctions, international agreements

---

## Balance Tracking

When adding policies, update the balance tracker:

| Category | Left-Lean | Neutral | Right-Lean | Total |
|----------|-----------|---------|------------|-------|
| Economic | | | | |
| Social | | | | |
| Security | | | | |
| Institutional | | | | |
| Foreign | | | | |

Goal: Rough parity across ideological leans within each category.
