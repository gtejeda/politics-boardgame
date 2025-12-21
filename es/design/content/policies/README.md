# Cartas de Política

Este directorio contiene diseños de cartas de política organizados por categoría.

---

## Principios de Diseño de Políticas

> Ref. de Carta: Principio 2 - "Los Intercambios Son Obligatorios"
> Ref. de Carta: Principio 5 - "Las Consecuencias Son Frecuentemente Retardadas"

Cada carta de política debe tener:

1. **Efecto claro:** Qué hace mecánicamente
2. **Intercambio:** Qué presión crea
3. **Camino institucional:** Cómo se implementa
4. **Tiempo:** Efectos inmediatos vs. retardados

---

## Plantilla de Carta de Política

```yaml
name: [Nombre de Política]
category: [económico | social | seguridad | institucional | exterior]
ideological_lean: [izquierda | derecha | neutral]  # Solo para seguimiento de equilibrio, no jugabilidad

# Costos
budget_cost: [número]
political_cost: [número]  # Legitimidad gastada para proponer
institutional_requirement: [mayoría_legislatura | supermayoría | solo_ejecutivo | etc.]

# Efectos Inmediatos
immediate:
  - resource: [nombre_recurso]
    change: [+/- número]

# Efectos Retardados
delayed:
  - resource: [nombre_recurso]
    change: [+/- número]
    delay_rounds: [número]
    condition: [condición de activación opcional]

# Intercambios
tradeoff_pressure:
  - resource: [nombre_recurso]
    effect: [descripción de presión creada]

# Ambientación
description: [Breve descripción neutral]
historical_parallel: [Referencia opcional del mundo real]

# Cumplimiento de Carta
charter_check:
  - has_tradeoff: [sí/no]
  - neutral_framing: [sí/no]
  - institutional_path: [sí/no]
  - delayed_component: [sí/no/na]
```

---

## Categorías

### /economic
Política tributaria, gasto, regulación, comercio, política monetaria

### /social
Bienestar, educación, salud, vivienda, trabajo

### /security
Militar, policía, inteligencia, poderes de emergencia, fronteras

### /institutional
Reforma electoral, cambios judiciales, enmiendas constitucionales

### /foreign
Diplomacia, alianzas, sanciones, acuerdos internacionales

---

## Seguimiento de Equilibrio

Al agregar políticas, actualizar el rastreador de equilibrio:

| Categoría | Inclinación-Izq | Neutral | Inclinación-Der | Total |
|-----------|-----------------|---------|-----------------|-------|
| Económico | | | | |
| Social | | | | |
| Seguridad | | | | |
| Institucional | | | | |
| Exterior | | | | |

Objetivo: Paridad aproximada entre inclinaciones ideológicas dentro de cada categoría.
