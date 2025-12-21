# Estructura de Turno

> Este documento describe la estructura propuesta de turno/ronda. Todos los elementos son provisionales pendientes de pruebas de juego.

---

## Objetivos de Diseño para la Estructura de Turno

1. **Realismo institucional:** Las acciones fluyen a través de canales apropiados
2. **Elecciones significativas:** Cada fase ofrece decisiones reales
3. **Interacción de jugadores:** Oportunidades para negociación/conflicto
4. **Ritmo:** Equilibrio entre acción y resolución de consecuencias

---

## Estructura de Ronda Propuesta

### Fase 1: Evento/Situación
**Propósito:** Introducir presiones externas y nueva información

- Robar carta(s) de evento
- Revelar efectos retardados de rondas anteriores
- Actualizar información pública

**Agencia del jugador:** Reaccionar, no actuar

---

### Fase 2: Deliberación
**Propósito:** Planificación y negociación

- Los jugadores discuten, negocian, forman coaliciones
- Revisar acciones disponibles y costos
- Sin compromisos vinculantes (se permite hablar sin compromiso)

**Agencia del jugador:** Comunicación completa, sin mecánicas

---

### Fase 3: Acción de Política
**Propósito:** Decisiones centrales del juego

- Los jugadores seleccionan y juegan cartas de política
- Votación/resolución legislativa
- Gasto de recursos

**Agencia del jugador:** Fase de decisión principal

---

### Fase 4: Implementación
**Propósito:** Resolver qué sucede realmente

- Implementación ejecutiva (puede modificar resultados)
- Revisión judicial (puede bloquear/modificar)
- Los efectos inmediatos se resuelven

**Agencia del jugador:** Limitada - mayormente resolución

---

### Fase 5: Consecuencias
**Propósito:** Retroalimentación del sistema

- Ajustes de recursos
- Los temporizadores de efectos retardados avanzan
- Los bucles de retroalimentación se activan
- Verificaciones de condiciones de victoria/derrota

**Agencia del jugador:** Observación, aprendizaje

---

### Fase 6: Ciclo
**Propósito:** Preparar para la próxima ronda

- Robar nuevas cartas
- Refrescar recursos/habilidades agotadas
- Avanzar marcador de ronda

---

## Estructuras Alternativas a Considerar

### Selección de Acción Simultánea
Todos los jugadores eligen acciones secretamente, luego revelan juntos.
- Pro: Más rápido, reduce parálisis de análisis
- Contra: Menos negociación, más difícil modelar proceso legislativo

### Basado en Iniciativa
El orden de turno determinado por un recurso o puja.
- Pro: Otra palanca estratégica
- Contra: Puede aventajar ciertas estrategias

### Fases Asimétricas
Diferentes tipos de jugadores tienen diferentes estructuras de fase.
- Pro: Modela diferentes actores políticos
- Contra: Complejidad, dificultad de equilibrio

---

## Mecanismos de Tiempo para Efectos Retardados

### Fichas de Temporizador
Los efectos tienen fichas de cuenta regresiva; remover una por ronda hasta activarse.

### Sistema de Cola
Los efectos entran en una cola y se resuelven en orden cuando llegan al frente.

### Activadores de Umbral
Los efectos permanecen dormidos hasta que un recurso/condición cruza un umbral.

---

## Preguntas Abiertas

- [ ] ¿Cuánto debería durar un juego? (rondas, tiempo real)
- [ ] ¿Debería haber "eras" distintas dentro de un juego?
- [ ] ¿Cómo manejamos eliminación de jugadores vs. juego continuado?
- [ ] ¿Cuál es el número correcto de decisiones por ronda?
