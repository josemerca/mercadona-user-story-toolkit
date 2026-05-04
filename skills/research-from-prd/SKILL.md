---
name: research-from-prd
description: |
  Diseña y ejecuta user research estructurado en 6 bloques (Propósito -> Plan -> Criterios ->
  Análisis -> Conclusiones -> Next Steps) usando JTBD como lente y Mom Test + Field Study
  como técnicas. Pieza central del pipeline: después de prd-quality-guard, antes de jtbd-to-stories.
  SIEMPRE se ejecuta (modo Discover o Validate).

  Acepta un PRD como fuente de entrada (problema, solución, métricas, scope).

  TRIGGERS: diseñar research, preparar entrevistas, guión de entrevista,
  validar JTBDs con usuarios, analizar notas de entrevistas, Mom Test,
  detectar gaps, "discovery para PRD", "research para el PRD de..."

  INTEGRACIÓN: Input: contenido del PRD (paste, fichero, URL). Output: JTBDs
  compatibles con /jtbd-to-stories.
version: 1.0.0
---

# Research from PRD — Discovery en 6 Bloques

Pieza central del pipeline →Stories. Asiste al usuario en estructurar el research como un proceso de descubrimiento riguroso: 6 bloques que garantizan que pasamos del problema a JTBDs con evidencia real, sin saltar pasos ni inventar conclusiones.

> **Modo copiloto:** Esta skill diseña y propone planes de research, pero NO sustituye el research real. Las conclusiones se basan en evidencia recogida por el usuario, NUNCA inventada. Si el usuario no ha hecho entrevistas, el output son planes y guías de entrevista — no JTBDs inventados. Ver shared-config.md §Filosofía del Plugin.

## Las Tres Capas

Tres capas: **Proceso** (6 bloques) + **Lente** (JTBD: foco en el TRABAJO, 3 dimensiones F/E/S) + **Técnica** (Mom Test + Field Study). El JTBD no es un paso — es la lente que atraviesa TODO.

> Ver SKILL-reference.md §1 para diagrama completo, tabla comparativa por bloque y antipatrón clave.

## Pipeline: 6 Bloques del Discovery

Flujo: prd-quality-guard → **Preparación** → B1 Propósito → B2 Plan → B3 Criterios → [Ejecución] → B4 Análisis → B5 Conclusiones → B6 Next Steps → jtbd-to-stories → quality-coach.

> Ver SKILL-reference.md §2 para diagrama completo del pipeline.

---

## PREPARACIÓN: Análisis del PRD

**Cuándo ejecutar:** SIEMPRE, como primer paso antes de los 6 bloques.

### Proceso

1. Obtener el PRD (fichero local, URL o pegado por el usuario)
2. Leer `references/gap-detection-prd.md`
3. Analizar EAC con GAP-PRD-01 a PRD-04 + EFC/Scope con GAP-PRD-05 a PRD-08
4. Calcular Gap Score: `(Críticos × 10) + (Mayores × 5) + (Menores × 2) + (Refinamiento × 1)`. **Cálculo determinista:** `python3 scripts/gap_score.py --criticos=<N> --mayores=<N> --menores=<N> --refinamiento=<N>`
5. Inventariar JTBDs existentes (si los hay en el Discovery del PRD)
6. Determinar modo:
   - **Descubrir** (Discovery del PRD ausente o flojo)
   - **Validar** (Discovery+EAC completos, hay hipótesis a contrastar)

### Reutilización de evidencia previa

Si el PRD viene de `/from-gsd` y el proyecto GSD tiene `phases/N/RESEARCH.md`, esa evidencia se incorpora al inventario. Pasar al comando `--evidence-from=.planning/phases/N/RESEARCH.md` para evitar duplicar entrevistas ya hechas.

### Regla: Gaps vs Research

Gaps de proceso/contexto (EAC del PRD) → resolver con stakeholder/PM. Gaps de producto/usuario (EFC y Discovery del PRD) → SON el foco del research. Gaps críticos BLOQUEAN hasta resolverse.

> Ver SKILL-reference.md §15 para output template de Preparación y tabla completa de gaps vs resolución.

---

## BLOQUE 1: Propósito

**Objetivo:** Definir qué queremos entender y en qué contexto real. Delimitar el problema.

**Regla:** El propósito SIEMPRE se formula en términos del TRABAJO que el usuario intenta lograr.

### Proceso

1. Leer el PRD completo (EAC + EFC + Discovery)
2. Identificar contexto real: ¿qué proceso del mundo real aborda?
3. Formular: "Entender qué TRABAJO intenta lograr [Job Performer] cuando [proceso], qué fricciones experimenta, y qué motivaciones (F/E/S) lo mueven. En particular, [foco de los gaps]."

Elementos: Job Performer (de EAC) + Proceso real (de EAC) + Foco (gaps) + Delimitación (de Exclusiones del PRD).

Output: Propósito (1-2 párrafos) + Job Performer + Proceso + Foco + Delimitación.

> Ver SKILL-reference.md §16 para antipatrones del propósito. §4 para template completo.

---

## BLOQUE 2: Plan

**Objetivo:** Diseñar plan dual: observación conductual (lo que HACEN) + entrevista actitudinal (lo que PIENSAN).

**Referencia:** `references/prd-to-interview-mapping.md`

### 2a. Plan de observación conductual (Field Study)

Observación valida si lo que el usuario DICE coincide con lo que HACE. Workarounds = señal más fuerte de job mal servido.

Elementos: Qué observar (comportamientos, workarounds) | Dónde (entorno real) | Cómo registrar (hechos vs interpretaciones) | Duración (30-60 min silenciosa).

> Ver SKILL-reference.md §17 para template completo del plan de observación con checklist de campo.

### 2b. Guión de entrevista actitudinal (Mom Test)

**Referencia:** `references/mom-test-principles.md`

**Modo Descubrir** (Discovery vacío/parcial): Warm-up (3-5min) → Su vida/JTBD (10-12min) → Comportamiento actual (8-10min) → Deep dive gaps (8-10min) → Cierre (3min).

**Modo Validar** (Discovery con JTBDs): Warm-up (3min) → Su vida (8-10min) → Validación JTBD (8-10min) → Exploración abierta (5-8min) → Cierre (3min).

> Regla anti-sesgo (Modo Validar): El guión NUNCA debe mencionar, sugerir ni insinuar los JTBDs del Discovery. Si un JTBD NO se confirma, es un hallazgo VALIOSO.

> Ver SKILL-reference.md §18 para mapeo PRD→Preguntas y justificación del método.

Output: Plan de observación + Guión de entrevista + Justificación (método, perfil, muestra).

> Ver SKILL-reference.md §5 para template completo.

---

## BLOQUE 3: Criterios de Éxito

**Objetivo:** Convertir el propósito en 2-4 preguntas verificables como METRO del research.

**Regla:** Criterios orientados a componentes JTBD (trigger, struggle, desired outcome, motivaciones F/E/S).

### Proceso

1. Leer propósito (B1) y gaps (Preparación)
2. Formular 2-4 preguntas verificables que cubran componentes JTBD clave
3. Cada criterio responde "Sí, sabemos porque [evidencia]" o "No, falta [evidencia]"

Estructura: Criterio [N]: [Pregunta] + Componente JTBD + Cómo verificar + Umbral mínimo. Reglas: CR-1 Max 4 | CR-2 Mapea a JTBD | CR-3 Umbral claro | CR-4 Verificable | CR-5 Anti-scope-creep.

Output: Tabla criterios + regla anti-scope-creep.

> Ver SKILL-reference.md §19 para ejemplos y reglas. §6 para template.

---

## Ejecución asistida del Research

La skill asiste durante la ejecución proporcionando guías para observación y entrevistas.

**Guía de observación:** Workarounds = señal más fuerte de job mal servido. Copiar datos a mano = herramienta no sirve el job. Post-its = proceso no autoexplicativo. Pide ayuda = job complejo/social. Alterna 3+ herramientas = fragmentación.

> Ver SKILL-reference.md §20 para tabla completa de señales observación→JTBD.

**Guía de entrevista (Mom Test):** 1) Habla de su vida, no del producto. 2) Pregunta por específicos del pasado. 3) Habla menos, escucha más. Referencia: `references/mom-test-principles.md`.

> Ver SKILL-reference.md §7 para template completo de notas de campo.

---

## BLOQUE 4: Análisis

**Objetivo:** Procesar evidencia separando hechos de interpretaciones, por criterio de éxito. JTBDs emergen como SÍNTESIS del análisis.

**Referencia:** `references/analysis-to-jtbd.md`

### Regla de separación obligatoria

> Observaciones = HECHOS recogidos en campo. Aprendizajes = INTERPRETACIONES en clave JTBD. Mezclarlos es el error más común y más peligroso del research.

### Proceso

1. Consolidar notas de todas las sesiones
2. Filtrar bad data (cumplidos, fluff, promesas futuras)
3. Para cada criterio del B3: observaciones clave (hechos) + aprendizajes (interpretaciones JTBD)
4. Sintetizar inventario de JTBDs descubiertos con fichas de evidencia
5. Validación cruzada con el PRD (¿qué se confirma? ¿qué se contradice? ¿qué emerge nuevo?)

> Ver SKILL-reference.md §21 para templates de observaciones, aprendizajes, fichas JTBD y validación cruzada.

Output: Análisis por criterio + Evaluación cobertura + Inventario JTBDs con fichas + Validación cruzada con PRD.

---

## BLOQUE 5: Conclusiones

**Objetivo:** Síntesis ejecutiva — alguien que no estuvo "se entera de la peli" en 2 minutos.

Reglas: CON-1 NO info nueva | CON-2 Max 2-4 bullets | CON-3 JTBDs = pieza central | CON-4 Qué del PRD se confirmó/no | CON-5 Tono informar, no recomendar.

Output: Síntesis ejecutiva (4 bullets: conclusión principal, JTBDs, validación PRD, confianza) + tabla resumen JTBDs.

> Ver SKILL-reference.md §8 para template completo.

---

## BLOQUE 6: Next Steps

**Objetivo:** Decidir qué hacer después. Dos caminos: más research o pasar a Explore.

> **PROHIBIDO proponer soluciones.** Discovery descubre PROBLEMA. Explore diseña SOLUCIÓN.

### Árbol de decisión

```
¿Todos los criterios cubiertos?
  SI → ¿Todos JTBDs confianza alta? → SI: Pasar a Explore
                                    → NO: Explore con advertencias
  NO → Más research focalizado en criterios no cubiertos
```

Output: Decisión + evaluación criterios + JTBDs listos o research adicional necesario.

> Ver SKILL-reference.md §9 para template completo.

---

## Quality Gate: Evaluación del Research

**Primaria (criterios B3):** 100% = entregar | 75%+ = advertencias | 50-74% = más research | <50% = bloquear.
**Secundaria:** Research Gap Score (`references/gap-detection-research.md`) — cobertura 7 componentes, calidad evidencia, cruce con PRD.
**3 dimensiones:** Cada JTBD necesita F/E/S con evidencia; si "Inferida" en todos → más research.

---

## Checkpoints Conversacionales

> La skill no ejecuta todo de golpe. Pausa en momentos clave para compartir avances y permitir redirigir.

**CHECKPOINT Post-Preparación + B1:** Comunicar Gap Score, gaps principales, modo research, propósito. Preguntar: "¿Estamos alineados? ¿Procedo al plan?"

**CHECKPOINT Post-Plan (B2 y B3):** Comunicar plan (observación + entrevista), perfil, muestra, criterios de éxito. Preguntar: "¿Publico completo, revisamos, o ajustamos?"

**CHECKPOINT Post-Análisis (B4):** Comunicar cobertura criterios, JTBDs descubiertos. Preguntar: "¿Criterios cubiertos? ¿Procedo a conclusiones?"

> Ver SKILL-reference.md §22 para templates completos de los 3 checkpoints.

---

## Workflow: Revisar preguntas de research

**Input:** Preguntas + PRD de contexto.
**Proceso:** Leer `references/mom-test-principles.md`, evaluar cada pregunta contra Mom Test + contexto del PRD. Detectar: leading, pide opinión, futuro, cerrada, lenguaje del PRD, sesgo confirmación. Proponer alternativas.
**Output:** Tabla (original | problema | alternativa) + cobertura criterios.

## Workflow: Analizar notas de entrevistas/observaciones

**Input:** Notas de campo + PRD.
**Ref:** `references/analysis-to-jtbd.md`.
**Proceso:** 1) Por sesión: separar hechos/interpretaciones, filtrar bad data, extraer quotes, identificar workarounds. 2) Organizar por criterio B3. 3) Cruzar con PRD (Farolas, Penumbras, problemas nuevos). 4) Sintetizar JTBDs. 5) Quality Gate.
**Output:** Bloque 4 completo.

---

## Cómo obtener el PRD

Fichero local, URL pública, o pegado directo en el chat. La skill no asume ninguna herramienta concreta de almacenamiento.

---

## Referencia rápida

> Ver SKILL-reference.md: §10 señales calidad | §11 cheatsheet JTBD+Mom Test | §12 antipatrones | §13 comandos | §14 changelog

## Referencias

- `references/gap-detection-prd.md` — Gaps del PRD
- `references/gap-detection-research.md` — Gaps de evidencia research
- `references/prd-to-interview-mapping.md` — Mapeo PRD → preguntas
- `references/mom-test-principles.md` — Mom Test + moderación
- `references/analysis-to-jtbd.md` — Observaciones → JTBDs

---

## Reglas Estrictas

1. **NUNCA** generar JTBDs ni conclusiones sin evidencia real de entrevistas/observación. Si el usuario no ha hecho research, el output son planes y guías, no JTBDs inventados.
2. **SIEMPRE** separar HECHOS (observaciones de campo) de INTERPRETACIONES (aprendizajes en clave JTBD). Mezclarlos es el error más peligroso del research.
3. **En modo Validar:** el guión de entrevista **NUNCA** debe mencionar, sugerir ni insinuar los JTBDs del Discovery. Si un JTBD no se confirma, eso es un hallazgo valioso.
4. **PROHIBIDO** proponer soluciones en B6 Next Steps. Discovery descubre PROBLEMA; Explore diseña SOLUCIÓN.
5. **SIEMPRE** filtrar bad data: cumplidos, fluff y promesas futuras se descartan antes del análisis.
6. **SIEMPRE** delegar el Gap Score a `scripts/gap_score.py`, no calcularlo en el LLM.
