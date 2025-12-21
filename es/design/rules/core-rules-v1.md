# Reglas Centrales v1.0 - Borrador de Diseño Inicial

> **Nota de Diseño:** Este es un primer borrador con opiniones claras. Cada decisión es intencional pero negociable. Los ítems marcados con [DISCUTIR] están particularmente abiertos a cambios.

---

## Resumen del Juego

**Jugadores:** 3-5 (óptimo: 4)
**Tiempo:** 90-120 minutos
**Modo:** Semi-cooperativo con victoria individual

Los jugadores son **líderes de facción** dentro de una sola nación democrática. Comparten la responsabilidad de gobernar pero compiten por influencia y legado. Si la nación colapsa, todos pierden. Entre los supervivientes, el jugador cuyas dimensiones de legado puntúen más alto gana.

---

## Qué Representan los Jugadores

Cada jugador lidera una **Facción Política** - una coalición de intereses, ideología y seguidores. Las facciones no son estrictamente "izquierda" o "derecha" pero tienen **inclinaciones iniciales** que dan bonificaciones menores a ciertos tipos de políticas.

### Las 5 Facciones

| Facción | Inclinación Inicial | Bonificación |
|---------|---------------------|--------------|
| **Los Progresistas** | Reforma social | +1 Legitimidad al aprobar políticas Sociales |
| **Los Conservadores** | Enfoque en estabilidad | +1 Estabilidad al bloquear cambios rápidos |
| **Los Liberales** | Mercado y libertad | +1 Crecimiento al aprobar desregulación Económica |
| **Los Nacionalistas** | Seguridad y soberanía | +1 Estabilidad al aprobar políticas de Seguridad |
| **Los Populistas** | Anti-establishment | +1 Legitimidad al oponerse a políticas institucionales |

[DISCUTIR] ¿Son las facciones nombradas demasiado obvias? Alternativa: Colores abstractos sin identidad preestablecida.

---

## Recursos

Cinco recursos nacionales rastreados en un tablero central. Todos los jugadores los comparten - la nación tiene éxito o fracasa juntos.

| Recurso | Rango | Comienza En | Umbral de Colapso |
|---------|-------|-------------|-------------------|
| **Presupuesto** | -10 a +20 | 8 | ≤0 por 2 rondas consecutivas |
| **Legitimidad** | 0 a 20 | 10 | ≤2 |
| **Estabilidad** | 0 a 20 | 10 | ≤2 |
| **Crecimiento** | -5 a +15 | 5 | ≤-3 por 2 rondas consecutivas |
| **Libertad** | 0 a 20 | 10 | ≤3 (activa Bloqueo Autoritario) |

### Interacciones de Recursos (Tensiones Incorporadas)

Estos ajustes automáticos ocurren durante la fase de Consecuencias:

- **Crecimiento > 10:** Presupuesto +1 (ingresos fiscales)
- **Crecimiento < 0:** Presupuesto -1, Estabilidad -1 (efectos de recesión)
- **Estabilidad < 5:** Legitimidad -1 (el público pierde fe)
- **Libertad < 5:** Legitimidad -1 (la represión genera resentimiento)
- **Legitimidad < 5:** Todos los costos de políticas +1 (resistencia al gobierno)
- **Presupuesto < 0:** No se pueden aprobar políticas que cuesten Presupuesto (austeridad)

---

## Influencia (Recurso Individual)

Cada jugador tiene **Influencia** personal (0-15, comienza en 5). Esto representa el capital político de tu facción.

**Ganar Influencia:**
- +1 cuando una política que patrocinaste se aprueba
- +2 cuando predices exitosamente el resultado de una crisis
- +1 cuando estás en el lado ganador de un voto disputado

**Gastar Influencia:**
- 1 Influencia: Agregar +1 a cualquier voto en el que participes
- 2 Influencia: Patrocinar una política de tu mano (requerido para proponer)
- 3 Influencia: Forzar una política a votación (saltar deliberación)
- 5 Influencia: Vetar una política después de que se apruebe (una vez por partida)

---

## Instituciones

Seis instituciones restringen lo que los jugadores pueden hacer. Cada una tiene una calificación de **Fuerza** (1-5, comienza en 3).

### Legislatura
- Todas las políticas deben pasar aquí por voto mayoritario
- **Efecto de fuerza:** Mayor = más votos necesarios (Fuerza 3 = mayoría simple, Fuerza 5 = supermayoría)
- Los jugadores votan con su peso de Influencia (base 1 + Influencia gastada)

### Poder Judicial
- Revisa políticas que afectan Libertad o categorías Institucionales
- **Efecto de fuerza:** Mayor = más probable que bloquee políticas inconstitucionales
- Tirar 1d6: Política bloqueada si tirada ≤ Fuerza Judicial Y la política reduce Libertad

### Ejecutivo
- Implementa políticas aprobadas
- **Efecto de fuerza:** Mayor = mejor implementación (efecto completo). Menor = efecto reducido o retardado
- Tirar 1d6: Implementación completa si tirada ≤ Fuerza Ejecutiva, de lo contrario 50% del efecto

### Mercados
- Generan Crecimiento automáticamente pero resisten el control
- **Efecto de fuerza:** Mayor = más estable pero menos dinámico. Menor = volátil pero con picos más altos
- Cada ronda: Tirar 1d6. Si ≤ Fuerza de Mercado: Crecimiento +1. Si > Fuerza de Mercado: Crecimiento +1d3-2 (rango -1 a +1)

### Opinión Pública
- Rastreada como un medidor separado (Aprobación: 0-10, comienza en 5)
- **Efecto de fuerza:** Mayor = más presión electoral, efectos de políticas sobre Legitimidad amplificados
- Si Aprobación < 3: La facción gobernante pierde 1 Influencia por ronda

### Sociedad Civil
- Intereses organizados que responden a políticas
- **Efecto de fuerza:** Mayor = respuesta más activa a políticas
- Cuando una política se aprueba: Si Fuerza de Sociedad Civil ≥ 4 Y la política es controversial, activar evento de Reacción

[DISCUTIR] ¿Son 6 instituciones demasiadas para rastrear? Se podrían fusionar algunas.

---

## Estructura de Turno

Cada ronda de juego representa aproximadamente 1 año de gobierno. Jugar 8-12 rondas (escala con número de jugadores).

### Fase 1: Eventos (Simultáneo)

1. Robar 1 carta de Evento por jugador (ej., 4 jugadores = 4 eventos)
2. Revelar todos los eventos simultáneamente
3. Los eventos con tiempo "Inmediato" se resuelven ahora
4. Los eventos con tiempo "Pendiente" se colocan en la línea de tiempo

### Fase 2: Deliberación (5 minutos máximo)

1. Los jugadores discuten la situación abiertamente
2. Negocian apoyo, hacen tratos, forman coaliciones temporales
3. Sin compromisos vinculantes - los tratos pueden romperse
4. Cada jugador selecciona 1 carta de Política de su mano para potencialmente patrocinar

### Fase 3: Acciones de Política (En sentido horario desde el Primer Jugador)

Cada jugador en orden de turno:

1. **Patrocinar** (opcional): Pagar 2 Influencia para poner tu Política seleccionada a votación
2. **Votar**: Todos los jugadores votan Sí/No/Abstención sobre la política patrocinada
   - Sí = +1 voto (puede gastar Influencia para más)
   - No = -1 voto (puede gastar Influencia para más)
   - Abstención = 0
3. **Resolver**: Si Sí > No, la política se aprueba. Si hay empate, la política falla.
4. Repetir para la política patrocinada del siguiente jugador

Máximo 1 política patrocinada por jugador por ronda. Máximo 3 políticas pueden aprobarse por ronda (las demás se apartan).

### Fase 4: Implementación

Para cada política aprobada:

1. Verificar Poder Judicial (si aplica): Tirar vs. Fuerza Judicial
2. Verificar Ejecutivo: Tirar vs. Fuerza Ejecutiva para calidad de implementación
3. Aplicar efectos inmediatos (modificados por tirada de implementación)
4. Colocar marcadores de efectos retardados en la línea de tiempo

### Fase 5: Consecuencias

1. **Efectos Retardados**: Resolver cualquier efecto programado para esta ronda
2. **Bucles de Retroalimentación**: Verificar y aplicar interacciones de recursos
3. **Decaimiento/Crecimiento Institucional**: Ajustar fuerzas institucionales basado en eventos de la ronda
4. **Fase de Mercado**: Tirar para Crecimiento generado por Mercado
5. **Actualización de Aprobación**: Ajustar Opinión Pública basado en cambios de recursos

### Fase 6: Refresco

1. Robar 2 cartas de Política, descartar hasta tener 5
2. Pasar el marcador de Primer Jugador en sentido horario
3. Verificar condiciones de colapso
4. Si Ronda 8+: Verificar activador de final de juego

---

## Votación en Detalle

Cuando se patrocina una política:

1. El patrocinador declara la política y sus efectos
2. 30 segundos para negociación final
3. Revelación simultánea de votos (usar fichas ocultas o dedos)
4. Contar votos: Cada jugador = 1 voto base + cualquier Influencia gastada
5. Los empates fallan. La mayoría aprueba.

**Sistema de Látigo** [DISCUTIR]: Antes de la revelación de votos, un jugador puede gastar 2 Influencia para convertirse en Látigo. El Látigo vota último y abiertamente, viendo todos los demás votos primero.

---

## Sistema de Efectos Retardados

Muchas políticas tienen efectos que se activan 2-4 rondas después. Rastrear usando un **Tablero de Línea de Tiempo**:

```
Ronda:   Actual | +1 | +2 | +3 | +4 | +5
Efectos:   --   | A  | B,C|  D |    | E
```

Al colocar un efecto retardado:
1. Poner una ficha numerada en la línea de tiempo
2. Registrar el efecto en la hoja de seguimiento
3. Cuando llega la ronda, el efecto se activa automáticamente

Los jugadores pueden ver qué viene pero no siempre recordar los efectos exactos (simula la complejidad de las políticas).

---

## Bucles de Retroalimentación (Automáticos)

Estos se activan durante la fase de Consecuencias cuando se cumplen las condiciones:

### Ciclo Económico
- **Auge**: Si Crecimiento ≥ 8 por 2 rondas consecutivas → Presupuesto +2, pero Estabilidad -1 (desigualdad)
- **Crisis**: Si Crecimiento ≤ 0 por 2 rondas consecutivas → Presupuesto -2, Legitimidad -1

### Espiral de Legitimidad
- **Mandato**: Si Legitimidad ≥ 15 → Toda implementación de política +1
- **Crisis de Fe**: Si Legitimidad ≤ 5 → Todos los costos de política +1 Influencia

### Tensión Estabilidad-Libertad
- **Estado de Seguridad**: Si Estabilidad > 15 Y Libertad < 8 → Libertad -1 por ronda (erosión automática)
- **Disturbios**: Si Estabilidad < 5 → Robar 1 evento de Crisis extra

### Acumulación de Desigualdad (Rastreada Separadamente)
- **Contador de Desigualdad**: Comienza en 0, máximo 10
- Ciertas políticas suman a Desigualdad (marcado en las cartas)
- Si Desigualdad ≥ 7 Y Legitimidad < 10 → Estabilidad -2 (disturbios)
- Si Desigualdad ≥ 10 → Activar evento de Revolución

### Erosión Institucional
- Cada vez que se elude el Poder Judicial: Fuerza Judicial -1
- Cada vez que el Ejecutivo actúa sin Legislatura: Fuerza Legislatura -1
- Si cualquier Fuerza Institucional ≤ 1: Esa institución deja de funcionar

---

## Condiciones de Victoria

### Derrota Colectiva (Todos Pierden)
Si CUALQUIER condición de colapso se activa, el juego termina inmediatamente y todos los jugadores pierden:

- **Colapso Fiscal**: Presupuesto ≤ 0 por 2 rondas consecutivas
- **Crisis de Legitimidad**: Legitimidad ≤ 2
- **Quiebre Sistémico**: Estabilidad ≤ 2
- **Bloqueo Autoritario**: Libertad ≤ 3 Y cualquier política de Seguridad aprobada esta ronda
- **Revolución**: Desigualdad ≥ 10 Y Estabilidad ≤ 5

### Victoria Individual (Entre Supervivientes)

Si la nación sobrevive hasta el final (Ronda 8-12 basado en número de jugadores), los jugadores puntúan:

**Puntuación de Legado:**

Antes del juego, cada jugador elige secretamente 2 prioridades de Legado de:

| Legado | Puntuación |
|--------|------------|
| **Prosperidad** | 1 punto por Crecimiento sobre 5, 1 punto por Presupuesto sobre 10 |
| **Igualdad** | 3 puntos si Desigualdad ≤ 3, -2 puntos si Desigualdad ≥ 7 |
| **Libertad** | 1 punto por Libertad sobre 10 |
| **Orden** | 1 punto por Estabilidad sobre 10 |
| **Instituciones** | 1 punto por Institución en Fuerza 4+ |
| **Influencia** | 1 punto por cada 3 Influencia restante |

**Puntos de Bonificación:**
- +3 por más políticas aprobadas
- +2 por predecir la calificación final de Aprobación (dentro de 1)
- +2 por nunca romper un trato

El total más alto gana. Los empates van al mayor Influencia restante.

---

## Cartas de Política

Cada carta de política contiene:

```
┌─────────────────────────────────┐
│ [CATEGORÍA]           [COSTO]    │
│                                 │
│ NOMBRE DE POLÍTICA               │
│                                 │
│ Inmediato: [Efecto]             │
│ Retardado (Xr): [Efecto]        │
│                                 │
│ Intercambio: [Efecto negativo]  │
│                                 │
│ Requiere: [Camino institucional]│
│ ───────────────────────────     │
│ [Inclinación ideológica: I/C/D]  [#ID]   │
└─────────────────────────────────┘
```

**Costo**: Influencia para patrocinar (usualmente 2) + cualquier costo de Presupuesto
**Requiere**: Qué instituciones deben aprobar (todas las políticas necesitan Legislatura; algunas necesitan revisión Judicial)

---

## Cartas de Evento

```
┌─────────────────────────────────┐
│ [SEVERIDAD]          [CATEGORÍA] │
│                                 │
│ NOMBRE DEL EVENTO                │
│                                 │
│ [Texto narrativo]               │
│                                 │
│ Efecto: [Qué sucede]            │
│                                 │
│ Opciones de Respuesta:          │
│ A) [Elección]: [Consecuencia]   │
│ B) [Elección]: [Consecuencia]   │
│ C) Ignorar: [Consecuencia]      │
│                                 │
│ ───────────────────────────     │
│ [Tiempo: Inmediato/Pendiente +X]│
└─────────────────────────────────┘
```

**Severidad**: Menor (efectos pequeños), Moderado (significativo), Mayor (significativo), Crisis (cambia el juego)
**Respuesta**: Los jugadores votan qué respuesta tomar (o respuestas de facción individual donde se indique)

---

## Lista de Componentes (Prototipo)

- 1 Tablero Central (pistas de Recursos, Fuerzas institucionales, Línea de tiempo)
- 5 tableros de Facción (pista de Influencia, selección de Legado)
- 60 cartas de Política (12 por categoría)
- 40 cartas de Evento
- 5 conjuntos de fichas de votación (Sí/No/Abstención por jugador)
- Marcadores de recursos (cubos o fichas)
- Fichas de Influencia (suministro personal por jugador)
- Marcadores de efecto retardado (numerados 1-10)
- 2 dados de seis caras
- Marcador de Primer Jugador
- Block de hojas de seguimiento

---

## Registro de Decisiones de Diseño

| Decisión | Opción Elegida | Justificación | Alternativas Consideradas |
|----------|----------------|---------------|--------------------------|
| Número de jugadores | 3-5 | Suficientes para votos significativos, no muy caótico | Variante 2 jugadores, modo fiesta 6+ |
| Rol del jugador | Líderes de facción | Permite competencia dentro de gobierno compartido | Gobierno único, partidos puros |
| Modo de juego | Semi-cooperativo | Crea tensión: deben cooperar para sobrevivir, competir para ganar | Co-op puro, competitivo puro |
| Votación | Mayoría con Influencia | Simple pero permite gasto de capital político | Elección ordenada, unanimidad |
| Instituciones | 6 con calificaciones de Fuerza | Cada una restringe diferente | Menos instituciones, on/off binario |
| Efectos retardados | Tablero de línea de tiempo | Visual, rastreable, crea anticipación | Efectos ocultos, basado en dados |
| Victoria | Prioridades de legado | Múltiples estrategias válidas, elegidas secretamente | Puntuación única, específica de facción |

---

## Preguntas Abiertas en Este Diseño

1. [DISCUTIR] ¿Son 90-120 minutos demasiado para el público objetivo?
2. [DISCUTIR] ¿Son las 5 facciones nombradas demasiado políticamente cargadas?
3. [DISCUTIR] ¿Es la mecánica de revisión Judicial (tirada de dados) demasiado aleatoria?
4. [DISCUTIR] ¿Deberían los tratos ser vinculantes o siempre rompibles?
5. [DISCUTIR] ¿Se rastrea bien la Desigualdad o está demasiado oculta?
6. [DISCUTIR] ¿Son 6 instituciones demasiado complejas para la primera prueba de juego?

---

*Versión 1.0 - Borrador Inicial*
*Listo para discusión e iteración*
