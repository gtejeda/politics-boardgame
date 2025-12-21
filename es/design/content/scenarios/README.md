# Escenarios

Los escenarios definen las condiciones iniciales, políticas disponibles y reglas especiales para una sesión de juego.

---

## Principios de Diseño de Escenarios

> Ref. de Carta: Principio 14 - "Diseñar para Expansión Sin Reescrituras"

Los escenarios deben:
1. Usar mecánicas base sin modificaciones
2. Ajustar condiciones iniciales y contenido disponible
3. Representar diferentes contextos políticos fielmente
4. Estar equilibrados para la misma calidad de experiencia del jugador

---

## Plantilla de Escenario

```yaml
name: [Nombre del Escenario]
setting: [País/Región, Período de Tiempo]
player_count: [Rango recomendado]
game_length: [Rondas o estimación de tiempo]

# Condiciones Iniciales
initial_resources:
  budget: [número]
  legitimacy: [número]
  stability: [número]
  growth: [número]
  liberty: [número]

# Configuración Institucional
institutions:
  legislature:
    type: [unicameral | bicameral | etc.]
    special_rules: [cualquier modificación]
  judiciary:
    independence_level: [bajo | medio | alto]
    special_rules: [cualquier modificación]
  # ... etc.

# Contenido Disponible
policy_deck:
  include: [lista de categorías/cartas de política]
  exclude: [lista de contenido excluido]
  special_additions: [políticas específicas del escenario]

event_deck:
  include: [lista de categorías/cartas de evento]
  exclude: [lista de contenido excluido]
  guaranteed_events: [eventos que definitivamente ocurrirán]

# Modificaciones de Condición de Victoria
victory_adjustments:
  - [Cualquier condición de victoria específica del escenario]

# Reglas Especiales
scenario_rules:
  - rule: [Descripción]
    rationale: [Por qué esto refleja la realidad del escenario]

# Contexto Histórico (para valor educativo)
context:
  background: [Breve descripción neutral]
  key_tensions: [Qué hace interesante este escenario]
  historical_outcome: [Qué sucedió realmente, para discusión post-juego]

# Cumplimiento de Carta
charter_check:
  - uses_base_mechanics: [sí/no]
  - ideologically_neutral_framing: [sí/no]
  - playable_from_multiple_perspectives: [sí/no]
```

---

## Categorías de Escenarios

### /base-game
El/los escenario(s) predeterminados incluidos en el juego base. Deben ser:
- Accesibles para nuevos jugadores
- Representativos de mecánicas centrales
- No atados a un contexto controversial específico

### /historical
Escenarios históricos reales. Se necesita cuidado extra para:
- Enmarcado neutral
- Múltiples perspectivas válidas
- Precisión educativa

### /contemporary
Escenarios modernos. Mayor riesgo de sesgo, requiere:
- Revisión cuidadosa de equilibrio
- Verificaciones explícitas de neutralidad
- Posiblemente variantes regionales

### /hypothetical
Escenarios ficticios o abstractos. Útiles para:
- Explorar mecánicas sin bagaje
- Enseñar conceptos específicos
- Evitar controversia del mundo real

---

## Candidatos para Escenario del Juego Base

1. **"La República"** - Una nación democrática ficticia enfrentando modernización
2. **"Transición"** - Un país moviéndose de un sistema a otro
3. **"Federación"** - Un sistema multi-regional con dinámicas federales
4. **"La Crisis"** - Una nación enfrentando múltiples presiones simultáneas
