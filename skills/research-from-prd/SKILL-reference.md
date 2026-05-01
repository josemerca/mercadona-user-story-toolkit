# SKILL-reference.md — research-from-prd

> Reference data for SKILL.md. Loaded on demand.

---

## §1: Las Tres Capas (diagrama + antipatron)

> Reference data for SKILL.md. Loaded on demand.

```
┌────────────────────────────────────────────────────────────────┐
│ PROCESO (los 6 bloques)                                        │
│ → Estructura y rigor del research                              │
│ → Propósito → Plan → Criterios → Análisis →                   │
│   Conclusiones → Next Steps                                    │
├────────────────────────────────────────────────────────────────┤
│ LENTE (JTBD)                                                   │
│ → Qué buscamos: el TRABAJO que el usuario intenta lograr       │
│ → Foco en la TAREA, no en la persona                           │
│ → Las 3 dimensiones: funcional, emocional, social              │
│ → "Las personas no compran productos, contratan soluciones     │
│    para realizar trabajos específicos"                          │
├────────────────────────────────────────────────────────────────┤
│ TÉCNICA (Mom Test + Field Study)                               │
│ → Cómo preguntamos sin sesgar                                  │
│ → Cómo observamos sin interpretar                              │
│ → Hablar de su vida, no del PRD                               │
│ → Observar lo que HACEN, no lo que DICEN                       │
└────────────────────────────────────────────────────────────────┘
```

**Por qué el foco está en el TRABAJO:**

El JTBD no es un paso del research — es la lente que atraviesa TODO. Cada bloque se
formula en términos del trabajo que el usuario intenta lograr:

| Bloque | Sin lente JTBD (mal) | Con lente JTBD (bien) |
|--------|---------------------|----------------------|
| Propósito | "Entender cómo Caty planifica horarios" | "Entender qué TRABAJO intenta lograr Caty cuando planifica horarios y qué fricciones experimenta" |
| Criterios | "¿Qué herramientas usa?" | "¿Cuál es el trigger del trabajo? ¿Qué struggle real tiene? ¿Qué motivaciones la mueven?" |
| Observaciones | "Copia de hace 6 semanas" | "Copia de hace 6 semanas → workaround que señala que la herramienta no sirve el job" |
| Aprendizajes | "MOT actúa como editor" | "El TRABAJO de planificar horarios está mal servido: MOT no cubre el job funcional y obliga a recurrir al PDF" |
| Conclusiones | "Falta integrar datos del PDF" | "JTBD: 'Cuando tengo que planificar la semana, quiero cuadrar horas y recursos rápidamente, para sentirme segura de que todo va a funcionar'" |

**Antipatrón clave:** Confundir funcionalidades con trabajos.
- "Quiero un botón más grande" NO es un JTBD
- "Necesito completar la planificación rápidamente cuando estoy agobiada por el turno de tarde" SÍ lo es

---

## §2: Pipeline 6 Bloques (diagrama completo)

> Reference data for SKILL.md. Loaded on demand.

```
PRD (fichero, URL o pegado)
    │
    ▼
┌─────────────────────────────────────┐
│ /prd-quality-guard                  │  ← Evalúa calidad del PRD
│ Score ≥7 para continuar            │
└──────────────┬──────────────────────┘
               │
               ▼
┌══════════════════════════════════════════════════════════════════┐
║ /research-from-prd  (ESTA SKILL)                               ║
║                                                                  ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ PREPARACIÓN: Análisis del PRD                             │  ║
║  │ Gap Detection PF + PI (input para los 6 bloques)           │  ║
║  │ + Inventario de JTBDs existentes (si PI tiene)             │  ║
║  │ Output: Gap Score + modo research + contexto               │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 1: PROPÓSITO                                        │  ║
║  │ ¿Qué queremos entender y en qué contexto real?             │  ║
║  │ Formulado en términos del TRABAJO del usuario               │  ║
║  │ Checkpoint: ¿Propósito bien delimitado?                     │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 2: PLAN                                              │  ║
║  │ Siempre dual: observación + entrevista                      │  ║
║  │ → Plan de observación (Field Study): qué mirar, dónde      │  ║
║  │ → Guión de entrevista (Mom Test): preguntas, probes         │  ║
║  │ Checkpoint: ¿Plan cubre los criterios?                      │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 3: CRITERIOS DE ÉXITO                               │  ║
║  │ 2-4 preguntas verificables derivadas del propósito          │  ║
║  │ Orientadas a componentes JTBD: trigger, struggle,           │  ║
║  │ motivaciones (funcional, emocional, social)                 │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ [EJECUCIÓN DEL RESEARCH — asistida por la skill]           │  ║
║  │ Guía de observación + Guía de entrevista + Template notas  │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 4: ANÁLISIS                                          │  ║
║  │ Organizado POR criterio de éxito                            │  ║
║  │ 4a. Observaciones clave (hechos, lo que se VIO)             │  ║
║  │ 4b. Aprendizajes (interpretación en clave JTBD)             │  ║
║  │ → JTBDs emergen como síntesis del análisis                  │  ║
║  │ → Fichas JTBD con componentes y evidencia                   │  ║
║  │ Checkpoint: ¿Criterios cubiertos?                           │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 5: CONCLUSIONES                                      │  ║
║  │ Síntesis ejecutiva (2-4 bullets)                            │  ║
║  │ JTBDs descubiertos como pieza central                       │  ║
║  │ NO introduce información nueva                              │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │ BLOQUE 6: NEXT STEPS                                        │  ║
║  │ PROHIBIDO proponer soluciones (Discovery ≠ Explore)         │  ║
║  │ → Si JTBDs con evidencia suficiente: pasar a Explore        │  ║
║  │ → Si gaps en evidencia: más research focalizado             │  ║
║  └───────────────────────┬────────────────────────────────────┘  ║
║                          │                                        ║
║              JTBDs con evidencia real                              ║
║              (confianza alta)                                     ║
╚══════════════════════════╤═══════════════════════════════════════╝
                           │
                           ▼
┌─────────────────────────────────────┐
│ /jtbd-to-stories                    │  ← Solo genera stories
│ (usa JTBDs reales, NO infiere)     │     (skip Paso 0)
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ /user-story-quality-coach           │  ← Validación final
└─────────────────────────────────────┘
```

---

## §3: Migration notes (v0.5→v0.6 y v0.4→v0.5)

> Reference data for SKILL.md. Loaded on demand.

### Cambios v0.6 vs v0.5

| Antes (v0.5) | Ahora (v0.6) |
|---|---|
| (Internamente acoplado a un formato concreto) | **Source-agnostic:** acepta PRDs en cualquier estructura (EAC/EFC, Brief, etc.) |
| Gap detection con taxonomía única | Gap detection adaptable a la estructura del PRD |
| Mapeo entrevistas hardcodeado | Mapeo via `prd-to-interview-mapping.md` (extensible) |
| Preparación asume estructura específica | Preparación detecta automáticamente la estructura del PRD |
| Bloques con referencias a campos concretos | Bloques con referencias genéricas que se adaptan al PRD |

### Cambios v0.5 vs v0.4

| Antes (v0.4) | Ahora (v0.5) |
|---|---|
| Pipeline lineal: Gap Detection → Inventario → Fichas → Entrevistas → Research Gap | Pipeline en 6 bloques: Propósito → Plan → Criterios → Análisis → Conclusiones → Next Steps |
| JTBD como paso aislado (inventario + fichas primero) | JTBD como lente transversal (atraviesa todo el research) |
| Solo diseñaba entrevistas (actitudinal) | Dual: observación conductual + entrevista actitudinal |
| Sin propósito explícito del research | Bloque 1: Propósito formulado en términos del TRABAJO |
| Sin criterios de éxito | Bloque 3: Criterios verificables como METRO del research |
| Análisis sin estructura clara | Bloque 4: Separación obligatoria observaciones vs aprendizajes |
| Sin conclusiones ejecutivas | Bloque 5: Síntesis para "enterarse de la peli" |
| Next steps genéricos | Bloque 6: Regla anti-soluciones (Discovery ≠ Explore) |
| Gap Detection como evaluación final | Criterios de éxito como evaluación primaria |

---

## §4: Bloque 1 output template

> Reference data for SKILL.md. Loaded on demand.

```markdown
## Bloque 1: Propósito del Research

**Propósito:** [1-2 párrafos formulados en términos del TRABAJO]

**Job Performer principal:** [Rol específico]
**Proceso real que aborda:** [Descripción en lenguaje del usuario, no del PRD]
**Foco específico:** [Derivado de los gaps del PRD]
**Delimitación:** [Qué NO investigamos en este research]
```

---

## §5: Bloque 2 output template

> Reference data for SKILL.md. Loaded on demand.

```markdown
## Bloque 2: Plan de Research

### 2a. Plan de observación
[Template de observación completado para este PRD]

### 2b. Guión de entrevista
[Guión completo con fases, preguntas, probes, notas moderador]

### Justificación
[Por qué este método, perfil de reclutamiento, tamaño de muestra]
```

---

## §6: Bloque 3 output template

> Reference data for SKILL.md. Loaded on demand.

```markdown
## Bloque 3: Criterios de Éxito del Research

| # | Criterio | Componente JTBD | Umbral |
|---|----------|-----------------|--------|
| 1 | [Pregunta verificable] | [Componente] | [Mínimo de evidencia] |
| 2 | [Pregunta verificable] | [Componente] | [Mínimo de evidencia] |
| 3 | [Pregunta verificable] | [Componente] | [Mínimo de evidencia] |

**Regla anti-scope-creep:** Este research se limita a estos 3 criterios.
Si durante la ejecución emergen temas interesantes fuera de scope,
documentarlos como "para futuro research" pero NO ampliar el scope actual.
```

---

## §7: Template de notas de campo

> Reference data for SKILL.md. Loaded on demand.

Estructura genérica para notas de campo:

```markdown
# Notas de Research: [PRD] — Sesión [N]

**Fecha:** [YYYY-MM-DD]
**Tipo:** Observación / Entrevista / Ambos
**Participante:** [Rol, antigüedad, contexto]
**Entorno:** [Dónde se realizó]
**Duración:** [N] min

## Observaciones (HECHOS — lo que VI, no lo que creo)

| Momento | Qué hizo | Qué usó | Contexto |
|---------|----------|---------|----------|
| [Hora/Fase] | [Acción concreta] | [Herramienta/recurso] | [Circunstancia] |
| ... | ... | ... | ... |

**Workarounds detectados:**
- [Descripción del workaround] → Posible señal de: [job mal servido]

## Verbatims (QUOTES — lo que DIJO, textual)

> "[Quote literal]" — Contexto: [cuándo y por qué lo dijo]
> "[Quote literal]" — Contexto: [cuándo y por qué lo dijo]

## Mis interpretaciones (SEPARADAS de los hechos)

Esto es lo que YO creo, no lo que el participante dijo/hizo:
- [Interpretación 1]
- [Interpretación 2]

## Cobertura de criterios de éxito

| Criterio | ¿Cubierto en esta sesión? | Evidencia |
|----------|---------------------------|-----------|
| Criterio 1: [nombre] | Sí / Parcial / No | [Referencia a observación/quote] |
| Criterio 2: [nombre] | Sí / Parcial / No | [Referencia] |
| ... | ... | ... |

## Top 3 hallazgos de esta sesión
1. [Lo más importante]
2. [Lo segundo]
3. [Lo tercero]

## Sorpresas (lo que NO esperaba)
- [Qué me sorprendió y por qué]
```

---

## §8: Bloque 5 output template

> Reference data for SKILL.md. Loaded on demand.

```markdown
## Bloque 5: Conclusiones

### Síntesis ejecutiva

1. **[Conclusión principal]** — El trabajo central que descubrimos es [JTBD principal
   en una frase]. Lo más relevante es que [insight clave que cambia la comprensión
   del problema].

2. **[Conclusión sobre JTBDs]** — Descubrimos [N] JTBDs con evidencia de [N] sesiones.
   [Resumen de los JTBDs en 1-2 líneas cada uno].

3. **[Conclusión sobre PRD]** — [Qué del PRD se confirmó y qué no. Qué es NUEVO
   que el PRD no contemplaba].

4. **[Nivel de confianza]** — Los criterios de éxito [se cubrieron todos / se cubrieron
   parcialmente: criterio X no cubierto]. La evidencia es [suficiente para avanzar /
   necesita refuerzo en X área].

### JTBDs descubiertos (resumen)

| # | JTBD | Confianza | Criterios que cubre |
|---|------|-----------|---------------------|
| JTBD-1 | [Título] | Alta/Media/Baja | Criterio 1, 2 |
| JTBD-2 | [Título] | Alta/Media/Baja | Criterio 2, 3 |
```

---

## §9: Bloque 6 output template

> Reference data for SKILL.md. Loaded on demand.

```markdown
## Bloque 6: Next Steps

### Decisión: [Pasar a Explore / Más research]

**Evaluación de criterios:**
| Criterio | Estado | Justificación |
|----------|--------|---------------|
| Criterio 1 | Cubierto | [Por qué] |
| Criterio 2 | Cubierto | [Por qué] |
| Criterio 3 | Parcial | [Qué falta] |

[Si pasar a Explore:]
**JTBDs listos para Explore:**
- JTBD-1: [Título] — Confianza Alta
- JTBD-2: [Título] — Confianza Alta (advertencia: motivación social débil)

**Formato compatible con /jtbd-to-stories:**
[JTBDs en formato estructurado para el siguiente paso del pipeline]

[Si más research:]
**Research adicional necesario:**
- **Criterio [N] no cubierto:** [Qué tipo de evidencia falta]
- **Sesiones recomendadas:** [N] con perfil [X], focalizadas en [tema]
- **Preguntas específicas:** [Lista de preguntas para las sesiones adicionales]
```

---

## §10: Senales de calidad del research

> Reference data for SKILL.md. Loaded on demand.

### Research de alta calidad (discovery reconocible)
- Los 6 bloques están completos y se lee como un documento coherente
- Hay separación clara entre observaciones y aprendizajes
- Los JTBDs tienen las 3 dimensiones con evidencia real (quotes + observaciones)
- Hay hallazgos que NO estaban en el PRD (señal de preguntas abiertas)
- Alguna Penumbra NO se confirmó (señal de que no hubo leading)
- Los workarounds están documentados (señal de observación real)
- Los criterios de éxito se evalúan explícitamente
- Next Steps NO proponen soluciones

### Research de baja calidad
- Falta algún bloque o están mezclados
- No hay separación observaciones/aprendizajes
- Todo coincide exactamente con el PRD (sospecha de sesgo)
- Solo hay entrevistas, no observación (o viceversa)
- Los JTBDs son funcionalidades disfrazadas ("quiero un botón que...")
- No hay quotes literales
- Los criterios de éxito no se mencionan en el análisis
- Next Steps proponen soluciones concretas

---

## §11: Cheatsheet preguntas JTBD + Mom Test

> Reference data for SKILL.md. Loaded on demand.

### Para explorar el TRABAJO (Job)
- "Cuéntame paso a paso cómo haces [proceso], desde que empiezas"
- "¿Qué es lo primero que haces cuando [trigger del flujo]?"
- "¿Qué estabas intentando conseguir?"

### Para descubrir el Trigger
- "¿Qué te hizo empezar [proceso] la última vez?"
- "¿Siempre es por la misma razón o hay varias?"
- "¿Qué estabas haciendo justo antes?"

### Para descubrir Struggles (Penumbras → preguntas)
- "¿Qué es lo más pesado/frustrante de ese proceso?"
- "¿Cuándo fue la última vez que algo salió mal? ¿Qué pasó?"
- "¿Hay algún momento en el que pierdas tiempo o te sientas bloqueado?"

### Para descubrir Desired Outcome
- "¿Cómo sabes que [proceso] salió bien?"
- "Si esto funcionara perfecto, ¿qué cambiaría para ti?"
- "La última vez que salió realmente bien, ¿qué fue diferente?"

### Para descubrir motivaciones emocionales
- "¿Cómo te sientes cuando [situación del PF]?"
- "¿Qué te preocupa cuando haces [proceso]?"
- "Si esto saliera perfecto, ¿cómo sería tu día?"

### Para descubrir motivaciones sociales
- "¿Quién más depende de que hagas esto bien?"
- "¿Cómo se entera tu jefe/equipo de que esto fue bien?"
- "¿Qué pasa si tardas más de lo normal?"

### Para observación (Field Study)
- "He visto que hiciste X, ¿por qué?" (DESPUÉS de observar, no durante)
- "¿Siempre lo haces así o a veces cambia?"
- "¿Ese [post-it/nota/atajo] te lo inventaste tú?"

### Técnicas de moderación
| Situación | Respuesta |
|---|---|
| Cumplido sobre el proceso | "Gracias. Cuéntame la última vez que lo hiciste" |
| Respuesta genérica | "¿Cuándo fue la última vez? ¿Qué pasó exactamente?" |
| Feature request | "¿Qué te permitiría hacer eso? ¿Cómo lo resuelves ahora?" |
| Menciona herramienta | "¿Qué intentas conseguir con eso? ¿Qué pasa si no funciona?" |
| Usa jerga técnica PRD | "¿Cómo le llamas tú a eso?" |

---

## §12: Antipatrones JTBD

> Reference data for SKILL.md. Loaded on demand.

| Antipatrón | Ejemplo | Por qué es incorrecto | Corrección |
|------------|---------|----------------------|------------|
| Funcionalidad disfrazada | "Quiero un botón más grande" | Describe solución, no trabajo | "Necesito completar la acción rápido cuando estoy bajo presión" |
| Tarea sin contexto | "Registrar pedido" | Falta trigger, struggle, motivación | "Cuando llega un pedido urgente, necesito registrarlo rápido para no perder el turno" |
| Persona sin situación | "Como MOT quiero planificar" | Ignora el contexto situacional | "Cuando tengo que cuadrar caudales el lunes a primera hora..." |
| Motivación solo funcional | "Para optimizar tiempos" | Falta emocional y social | Añadir: "Para sentirme segura" + "Para que DT vea que gestiono bien" |
| Job genérico | "Gestionar el proceso" | Demasiado amplio para ser útil | Especificar: "Cuadrar horas del equipo respetando restricciones del convenio" |

---

## §13: Comandos Rapidos

> Reference data for SKILL.md. Loaded on demand.

| Comando | Acción |
|---------|--------|
| `Research completo para el PRD de [X]` | Pipeline completo: Preparación → 6 Bloques |
| `Diseña research para el PRD de [X]` | Preparación + Bloques 1-3 (Propósito + Plan + Criterios) |
| `Detectar gaps en el PRD de [X]` | Solo Preparación (Gap Detection) |
| `Revisa estas preguntas para el PRD de [X]` | Review Mom Test |
| `Analiza estas notas del PRD de [X]` | Bloques 4-6 (Análisis + Conclusiones + Next Steps) |
| `Genera JTBDs del research de [X]` | Bloque 4 → formato compatible con /jtbd-to-stories |

---

## §14: Changelog (v0.2→v0.5)

> Reference data for SKILL.md. Loaded on demand.

### v0.5.0 (28 Feb 2026)
- **Las Tres Capas:** Proceso (6 bloques) + Lente (JTBD) + Técnica (Mom Test + Field Study)
- **Bloque 1: Propósito** — Delimitar qué entender, formulado en clave JTBD (trabajo del usuario)
- **Bloque 2: Plan** — Dualidad conductual + actitudinal: plan de observación (Field Study) + guión de entrevista (Mom Test)
- **Bloque 3: Criterios de éxito** — 2-4 preguntas verificables orientadas a componentes JTBD, con umbral de evidencia
- **Bloque 4: Análisis refactorizado** — Separación obligatoria observaciones (hechos) vs aprendizajes (interpretación). Organizado por criterio de éxito. JTBDs emergen como síntesis del análisis
- **Bloque 5: Conclusiones** — Síntesis ejecutiva (2-4 bullets) con JTBDs descubiertos como pieza central
- **Bloque 6: Next Steps** — Regla anti-soluciones (Discovery ≠ Explore). Árbol de decisión: más research vs pasar a Explore
- **Plan de observación** — Template completo de Field Study con checklist de campo y señales JTBD
- **Template de notas** — Estructura recomendada para notas de campo
- **Guía de observación** — Tabla workarounds → señales JTBD
- **Antipatrones JTBD** — 5 antipatrones comunes con correcciones
- **Quality Gate dual** — Criterios de éxito (primario) + Research Gap Score (secundario)
- **Checkpoints adaptados** — Post-Preparación+Propósito, Post-Plan+Criterios, Post-Análisis
- **Gap Detection del PRD** reubicado como PREPARACIÓN (input para los 6 bloques, no paso central)
- **Inventario de JTBDs** integrado en Preparación (cuando PI tiene JTBDs)
- Se conservan: Mom Test principles, gap detection taxonomías, 2 modos (Descubrir/Validar), regla anti-sesgo

### v0.4.0 (23 Feb 2026)
- Paso 0.5: Inventario de JTBDs
- Fichas Individuales por JTBD
- Checkpoint 1.5: Estructura de JTBDs
- Tabla de verificación de completitud
- Fichas post-research con comparativa pre/post

### v0.3.0 (18 Feb 2026)
- 2 Checkpoints Conversacionales

### v0.2.0 (17 Feb 2026)
- Versión inicial con Gap Detection + 2 modos + Mom Test

---

## §15: Output template de Preparación + Gaps vs Research

> Reference data for SKILL.md. Loaded on demand.

### Tabla: Gaps vs Research (qué resolver con quién)

| Tipo de gap | Resolver con... |
|---|---|
| PRD: GAP-PF-01 a PF-08 (gaps de proceso) | **Stakeholder PF** (dueño de proceso) |
| PRD: GAP-PI-01 a PI-06 (gaps de producto) | **Research con usuarios** + Stakeholder PI |
| PRD: GAP-PRD-01 a PRD-04 (gaps de EAC) | **PM** (dueño del PRD) |
| PRD: GAP-PRD-05 a PRD-08 (gaps de EFC/Scope) | **PM + Research** |
| Gaps críticos (cualquier fuente) | BLOQUEAN el research hasta resolverse |
| Gaps de producto/usuario | SON el foco del research |

### Output template

```markdown
## Análisis de Gaps: [Nombre] (source_type: PRD|PRD)

### Resumen
- **Fuente:** [PRD | PRD]
- **Gap Score:** [N] ([Bajo <=5 / Medio 6-15 / Alto 16-30 / Crítico >30])
- **Gaps Críticos:** [N]
- **Gaps Mayores:** [N]
- **Gaps Menores:** [N]
- **Refinamiento:** [N]
- **Modo research:** Descubrir / Validar

### Inventario de JTBDs existentes (si PI tiene)
| # | JTBD | Job Performer | Ubicación |
|---|------|---------------|-----------|
| JTBD-1 | [título] | [performer] | [sección] |
| ... | ... | ... | ... |

### Gaps detectados
[Tabla con gap, severidad, impacto, pregunta para stakeholder]

### Recomendación
[Qué gaps resolver con stakeholder ANTES del research vs cuáles investigar CON research]
```

---

## §16: Antipatrones del Propósito

> Reference data for SKILL.md. Loaded on demand.

| Antipatrón | Ejemplo malo | Corrección |
|------------|-------------|------------|
| Demasiado amplio | "Entender la experiencia de tienda" | "Entender qué trabajo intenta lograr la MOT cuando planifica horarios" |
| Centrado en solución | "Validar si la nueva herramienta ayuda" | "Descubrir qué fricciones tiene al planificar horarios (antes de pensar en soluciones)" |
| Sin Job Performer | "Entender el proceso de reposición" | "Entender qué trabajo intenta lograr el reponedor cuando repone producto fresco" |
| Terminología PRD | "Evaluar el PRD de Control Colmena" | "Entender qué trabajo intenta lograr el responsable de AutoStore cuando monitoriza la operación" |

---

## §17: Template completo del plan de observación (Field Study)

> Reference data for SKILL.md. Loaded on demand.

```markdown
### Plan de Observación: [Nombre del PRD/PRD]

**Entorno:** [Dónde observar — tienda, almacén, oficina, etc.]
**Duración:** [N] min
**Rol observado:** [Job Performer]

#### Qué observar (checklist de campo)

**Proceso:**
- [ ] ¿Cómo empieza la tarea? ¿Qué trigger lo activa?
- [ ] ¿Qué pasos sigue? ¿En qué orden?
- [ ] ¿Dónde se detiene o duda?
- [ ] ¿Cuánto tiempo dedica a cada paso?

**Herramientas y entorno:**
- [ ] ¿Qué herramientas/pantallas usa?
- [ ] ¿Alterna entre ellas? ¿Con qué frecuencia?
- [ ] ¿Usa papel, post-its, anotaciones propias?

**Workarounds (señal de job mal servido):**
- [ ] ¿Hace algo "a mano" que podría estar automatizado?
- [ ] ¿Copia datos de un sitio a otro?
- [ ] ¿Tiene "trucos" personales para facilitar el trabajo?
- [ ] ¿Pide ayuda a alguien? ¿A quién y para qué?

**Interrupciones y contexto:**
- [ ] ¿Le interrumpen? ¿Quién y por qué?
- [ ] ¿Qué pasa cuando le interrumpen? ¿Puede retomar?
- [ ] ¿El entorno afecta (ruido, espacio, presión de tiempo)?

**Emociones visibles:**
- [ ] ¿Muestra frustración, prisa, concentración, estrés?
- [ ] ¿En qué momento del proceso cambia su estado?

#### Reglas de la observación
1. **No intervenir** — Solo observar y anotar
2. **No interpretar en el momento** — Anotar HECHOS, no conclusiones
3. **Preguntar después** — "He visto que hiciste X, ¿por qué?"
4. **Separar columnas** — Izquierda: lo que vi. Derecha: lo que creo que significa (DESPUÉS)
```

---

## §18: Mapeo PRD->Preguntas y justificación del método

> Reference data for SKILL.md. Loaded on demand.

### Mapeo PRD → Preguntas (reglas)

| Elemento PRD | Se convierte en... | PROHIBIDO |
|---|---|---|
| Farolas (métricas) | Contexto interno del entrevistador | Preguntar la métrica directamente |
| Penumbras (quotes) | Áreas de exploración profunda | Confirmar el quote |
| Flujo actual | Base para narrativa del usuario | Sugerir los pasos |
| Líneas Rojas | Constraints a validar indirectamente | Mencionar la restricción |
| Gaps PI | Preguntas específicas de descubrimiento | Preguntar si el gap existe |

### Justificación del método (template)

```markdown
### Justificación del método

**¿Por qué observación + entrevista?**
[Explicación de por qué ambos son necesarios para este PRD específico.
Qué esperamos descubrir con cada uno que el otro no podría capturar.]

**Perfil de reclutamiento:**
[Quién necesitamos observar/entrevistar, con qué criterios de selección]

**Tamaño de muestra recomendado:**
[N observaciones + N entrevistas, con justificación]
```

---

## §19: Ejemplo de criterios de éxito (PRD Horarios) y reglas

> Reference data for SKILL.md. Loaded on demand.

### Ejemplo para un PRD de Horarios

```markdown
**Criterio 1: ¿Cuál es el trigger real que activa el trabajo de planificar horarios?**
- Componente JTBD: Trigger
- Cómo verificar: >=3 MOTs describen qué les hace empezar la planificación
- Umbral: Patrón consistente en >=3 de N observaciones/entrevistas

**Criterio 2: ¿Qué struggle experimenta al intentar cuadrar caudales con restricciones?**
- Componente JTBD: Struggle
- Cómo verificar: Observar workarounds activos + quotes con emoción
- Umbral: >=2 workarounds observados + >=3 mentions espontáneas

**Criterio 3: ¿Qué motivaciones emocionales y sociales hay detrás del trabajo?**
- Componente JTBD: Motivación emocional + social
- Cómo verificar: Quotes literales que capturen cómo se SIENTEN y quién OBSERVA
- Umbral: >=2 quotes emocionales + >=1 quote social con contexto real
```

### Reglas de los criterios

| Regla | Descripción |
|-------|-------------|
| **CR-1** | Máximo 4 criterios — foco, no exhaustividad |
| **CR-2** | Cada criterio mapea a >=1 componente JTBD |
| **CR-3** | Cada criterio tiene umbral de evidencia claro |
| **CR-4** | Los criterios son verificables: se puede decir "cubierto" o "no cubierto" con datos |
| **CR-5** | Anti-scope-creep: "Eso de pues ya que estoy pregunto por... no suele ser buena idea" |

---

## §20: Tabla completa de señales observación->JTBD

> Reference data for SKILL.md. Loaded on demand.

| Lo que observas | Lo que significa (en clave JTBD) |
|----------------|----------------------------------|
| Copia datos a mano de una pantalla a otra | La herramienta no sirve el job de integrar información |
| Tiene post-its con instrucciones | El proceso no es autoexplicativo — job de "saber qué hacer" mal servido |
| Pide ayuda a un compañero | Job demasiado complejo para una persona — posible job social |
| Mira el reloj constantemente | Presión temporal — trigger y motivación emocional |
| Alterna entre 3+ herramientas | Fragmentación — el job de "tener visión completa" está mal servido |
| Repite una acción varias veces | Incertidumbre — no sabe si el resultado es correcto |
| Suspira o muestra frustración | Struggle real con evidencia emocional |

---

## §21: Templates Bloque 4 (observaciones, aprendizajes, fichas JTBD, validación cruzada)

> Reference data for SKILL.md. Loaded on demand.

### 4a. Observaciones clave (HECHOS) — por criterio

```markdown
### Criterio [N]: [Pregunta del criterio]

#### Observaciones (lo que vimos/escuchamos — HECHOS)

**De observación de campo:**
- [Hecho 1] — Sesión [N], [participante]
- [Hecho 2] — Sesión [N], [participante]

**De entrevistas (quotes literales):**
> "[Quote]" — [Participante], Sesión [N]
> "[Quote]" — [Participante], Sesión [N]

**Datos cuantitativos:**
- [N] de [M] participantes [comportamiento/mención]
- Frecuencia observada: [dato]
```

### 4b. Aprendizajes (INTERPRETACIONES en clave JTBD) — por criterio

```markdown
#### Aprendizajes (lo que creemos que significan los hechos)

**En clave JTBD:**
- [Interpretación 1] — Basado en: [referencia a observaciones]
- [Interpretación 2] — Basado en: [referencia a observaciones]

**Componentes JTBD que emergen:**
- Trigger: [lo que descubrimos] — Evidencia: [referencia]
- Struggle: [lo que descubrimos] — Evidencia: [referencia]
- Motivación [tipo]: [lo que descubrimos] — Evidencia: [referencia]

**¿Criterio cubierto?** Sí / Parcial / No
- Justificación: [por qué sí/no, con referencia al umbral]
```

### 4c. Ficha JTBD descubierto

```markdown
---
### JTBD-[N]: [Título descriptivo]

**Confianza:** Alta / Media / Baja
**Basado en:** [N] observaciones + [N] entrevistas
**Criterios que cubre:** [Lista de criterios del Bloque 3]

#### Formulación JTBD
Cuando [trigger real descubierto],
quiero [motivación funcional observada],
para [desired outcome expresado por usuarios].

#### Componentes con evidencia

| Componente | Descubierto | Evidencia | Fuente |
|------------|-------------|-----------|--------|
| Job Performer | [Rol específico real] | "[quote/observación]" | Sesión [N] |
| Trigger | [Situación concreta] | "[quote/observación]" | Sesión [N] |
| Struggle | [Fricción real con workaround] | "[quote/observación]" | Sesión [N] |
| Desired Outcome | [En palabras del usuario] | "[quote]" | Sesión [N] |
| Motivación Funcional | [Tarea práctica] | "[quote/comportamiento]" | Sesión [N] |
| Motivación Emocional | [Cómo quieren sentirse] | "[quote]" | Sesión [N] |
| Motivación Social | [Cómo quieren ser percibidos] | "[quote/observación]" | Sesión [N] |

#### Fuerza de la evidencia
- Mencionado por [N]/[M] participantes
- Workarounds observados: [Sí/No — descripción]
- Emoción al describirlo: [Sí/No — contexto]
- Ejemplos con fechas/detalles: [Sí/No]
---
```

### Validación cruzada con PRD

```markdown
### Validación cruzada PRD

| Elemento PRD | Fuente | Estado | Evidencia real |
|---|---|---|---|
| Farola: "[métrica]" | PF | Confirmado/Refutado/Parcial | "[dato de research]" |
| Penumbra: "[quote]" | PF | Confirmado/Refutado/Parcial | "[quote real]" |
| Línea Roja: "[restricción]" | PF | Confirmado/Refutado/Parcial | "[evidencia]" |
| JTBD PI: "[job]" | PI | Confirmado/Refutado/Parcial | "[evidencia]" |

### Hallazgos nuevos (no en PRD)
| Hallazgo | Tipo | Frecuencia | Impacto |
|---|---|---|---|
| [Problema nuevo] | Struggle | N/M | Alto/Medio/Bajo |
```

---

## §22: Templates completos de Checkpoints Conversacionales

> Reference data for SKILL.md. Loaded on demand.

### CHECKPOINT Post-Preparación + Bloque 1

```
"He analizado el PRD de [nombre] y definido el propósito del research.

Gap Score: [N] ([Nivel])
- Gaps principales: [lista breve]
- Modo research: [Descubrir/Validar]

Propósito del research:
[Propósito del Bloque 1 en 2-3 líneas]

¿Estamos alineados en lo que queremos entender?
¿Procedo a diseñar el plan de observación + entrevista?"
```

### CHECKPOINT Post-Plan (Bloques 2 y 3)

```
"He diseñado el plan de research:

Plan:
- Observación: [N] min en [entorno], foco en [qué observar]
- Entrevista: [N] min, modo [Descubrir/Validar], [N] fases
- Perfil: [resumen en 1 línea]
- Muestra recomendada: [N] sesiones

Criterios de éxito (lo que mide si el research fue suficiente):
1. [Criterio 1 en 1 línea]
2. [Criterio 2 en 1 línea]
3. [Criterio 3 en 1 línea]

¿Quieres:
a) Que publique el plan completo
b) Revisarlo conmigo primero (muestro preguntas clave)
c) Ajustar algo antes"
```

### CHECKPOINT Post-Análisis (Bloque 4)

```
"He analizado la evidencia del research de [nombre].

Cobertura de criterios:
- Criterio 1: [Cubierto/Parcial/No cubierto] [nombre del criterio]
- Criterio 2: [Cubierto/Parcial/No cubierto] [nombre del criterio]
- Criterio 3: [Cubierto/Parcial/No cubierto] [nombre del criterio]

JTBDs descubiertos: [N]
[Resumen de 1 línea por JTBD]

¿Los criterios de éxito se han cubierto?
¿Procedo a escribir conclusiones y next steps?"
```
