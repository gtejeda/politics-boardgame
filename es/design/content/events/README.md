# Cartas de Evento

Este directorio contiene diseños de cartas de evento que introducen presiones externas e incertidumbre.

---

## Principios de Diseño de Eventos

> Ref. de Carta: Principio 4 - "La Información Es Imperfecta pero No Arbitraria"

Los eventos crean incertidumbre pero deben:
1. Ser explicables (los jugadores entienden por qué esto podría suceder)
2. Crear presión sin determinar resultados
3. Ofrecer opciones de respuesta, no solo imponer efectos
4. Reflejar causas sistémicas, no caos aleatorio

---

## Plantilla de Carta de Evento

```yaml
name: [Nombre del Evento]
category: [económico | social | político | internacional | natural]
severity: [menor | moderado | mayor | crisis]

# Condiciones de Activación (por qué este evento tiene sentido ahora)
trigger_logic:
  - condition: [Qué estado hace esto plausible]
  - probability_modifier: [Qué aumenta/disminuye probabilidad]

# Efectos del Evento
immediate_pressure:
  - resource: [nombre_recurso]
    effect: [descripción]

# Opciones de Respuesta
responses:
  - name: [Respuesta A]
    cost: [recursos requeridos]
    effect: [resultado inmediato]
    delayed_effect: [consecuencias futuras]

  - name: [Respuesta B]
    cost: [recursos requeridos]
    effect: [resultado inmediato]
    delayed_effect: [consecuencias futuras]

# Si no hay respuesta / respuesta insuficiente
default_outcome:
  - effect: [Qué sucede si los jugadores no pueden o no responden]

# Ambientación
description: [Descripción neutral de lo que está sucediendo]
historical_parallels: [Ejemplos opcionales del mundo real]

# Cumplimiento de Carta
charter_check:
  - explainable_randomness: [sí/no]
  - offers_choice: [sí/no]
  - neutral_framing: [sí/no]
```

---

## Categorías

### /economic
Caídas de mercado, interrupciones comerciales, choques de recursos, cambios tecnológicos

### /social
Movimientos públicos, cambios demográficos, cambios culturales, salud pública

### /political
Escándalos, sorpresas electorales, cambios de coalición, desafíos institucionales

### /international
Guerras, tratados, sanciones, crisis globales, migración

### /natural
Desastres, eventos climáticos, pandemias, descubrimientos de recursos

---

## Composición del Mazo de Eventos

El mazo de eventos debe componerse para:
- Evitar largos tramos de eventos del mismo tipo
- Escalar severidad apropiadamente (más menores, menos crisis)
- Incluir algunos ciclos predecibles (elecciones, fechas límite de presupuesto)
- Permitir períodos "tranquilos" donde los jugadores impulsan la acción

Proporción sugerida:
- Menor: 40%
- Moderado: 35%
- Mayor: 20%
- Crisis: 5%
