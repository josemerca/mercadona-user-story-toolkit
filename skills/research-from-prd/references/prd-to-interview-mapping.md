# Mapeo PRD → Plan de Research (Observación + Entrevista)

## Principio fundamental

> El PRD te dice QUÉ investigar. Mom Test te dice CÓMO preguntar. Field Study te dice CÓMO observar.
> Nunca traslades directamente un dato del PRD a una pregunta ni busques confirmarlo en observación.
> Siempre transforma.

## Estructura del mapeo PRD

```
┌────────────────────────────────────────────────────────────────┐
│ PRD: EAC define problema → EFC define dirección                │
│ → Mapeo: Farolas/Penumbras EAC → entrevistas sobre problema   │
│ → Mapeo: Hipótesis EFC → validación de solución propuesta     │
│ → Mapeo: Discovery → profundización de hallazgos              │
└────────────────────────────────────────────────────────────────┘
```

**Mapeo clave:** En un PRD, las secciones de Discovery y Explore ya contienen research previo.
El nuevo research debe PROFUNDIZAR lo descubierto, no repetirlo.

---

## Mapeo EAC → Plan de Observación

### Farolas (datos cuantitativos del EAC)

**Uso en observación:** Saber qué MEDIR durante la observación, sin buscar el número exacto.

| Farola del PRD | ❌ Buscar directamente | ✅ Qué observar |
|---|---|---|
| "45 min/pedido urgente vs 30 min obj" | Cronometrar pedidos | Cómo se comporta el picker: ¿busca, duda, cambia prioridad? |
| "8% tasa error selección" | Contar errores | Momentos de duda: ¿cuándo mira dos veces? ¿Qué le confunde? |
| "60% tiempo extra en decidir prioridad" | Medir decisión | Qué hace antes de empezar: ¿mira pantallas, pregunta, lee Post-its? |

**Regla:** Si un comportamiento observado CONTRADICE la Farola del PRD, documentar la discrepancia.

### Penumbras (observaciones cualitativas del EAC)

**Uso en observación:** Áreas donde prestar atención especial. Las Penumbras del PRD son HIPÓTESIS.

| Penumbra del PRD | Qué observar | Señales de confirmación | Señales de refutación |
|---|---|---|---|
| "Pickers usan Post-its como workaround" | Herramientas no oficiales, notas, trucos | Post-its, hojas, pantallazos guardados | Flujo digital limpio sin extras |
| "Coordinadores duplican info en 3 herramientas" | Cuántas herramientas abren, secuencia | Alt-tab frecuente, copy-paste entre ventanas | Una herramienta principal, consultas puntuales |

**Regla:** Si la Penumbra NO se observa, eso es un hallazgo válido e importante.

### Hallazgos Discovery previo

**Uso en observación:** Profundizar hallazgos del Discovery, NO repetir.

| Hallazgo del Discovery | Qué observar (profundización) |
|---|---|
| "Pickers priorizan por cercanía física, no por urgencia" | ¿Siempre? ¿Cuándo cambian de estrategia? ¿Qué desencadena el cambio? |
| "Coordinadores no tienen visibilidad en tiempo real" | ¿Qué miran en su lugar? ¿Cada cuánto? ¿Qué acción toman cuando consiguen la info? |

---

## Mapeo EAC → Preguntas de Entrevista

### Farolas (datos cuantitativos)

**Uso en entrevista:** Contexto interno del entrevistador. NUNCA preguntar directamente por la métrica.

| Farola del PRD | ❌ Pregunta directa (PROHIBIDA) | ✅ Pregunta Mom Test |
|---|---|---|
| "45 min/pedido urgente" | "¿Tardas 45 minutos?" | "Cuéntame cómo fue el último pedido urgente. ¿Cómo te organizaste?" |
| "8% tasa error selección" | "¿Cometes errores al seleccionar?" | "¿Alguna vez te ha pasado que el producto no era el correcto? Cuéntame qué pasó" |
| "60% tiempo en decidir prioridad" | "¿Pasas mucho tiempo decidiendo?" | "Cuando empiezas turno y tienes varios pedidos, ¿cómo decides por cuál empezar?" |

**Regla:** Si el usuario menciona la métrica espontáneamente, profundizar. Si no la menciona, no forzar.

### Penumbras (observaciones cualitativas)

| Penumbra del PRD | Área a explorar | Pregunta de apertura | Probes |
|---|---|---|---|
| "Usan Post-its como workaround" | Herramientas no oficiales | "¿Qué herramientas usas durante tu turno?" | "¿Te has inventado algún truco para ir más rápido?" |
| "Duplican info en 3 herramientas" | Fragmentación de info | "Cuando necesitas saber cómo va el turno, ¿dónde miras?" | "¿Siempre miras ahí? ¿Qué pasa si ese dato no está?" |
| "No tienen visibilidad en tiempo real" | Latencia de información | "¿Cómo te enteras de que algo va mal?" | "La última vez que algo fue mal, ¿cuánto tardaste en enterarte?" |

### Hipótesis de Solución (EFC)

**Uso en entrevista:** NUNCA mencionar la solución propuesta. Explorar el área que la solución intenta cubrir.

| Hipótesis EFC | ❌ Preguntar (PROHIBIDO) | ✅ Explorar el área |
|---|---|---|
| "Vista consolidada de pedidos" | "¿Te gustaría una pantalla con todos los pedidos?" | "¿Cómo te organizas cuando tienes muchos pedidos? ¿Dónde miras?" |
| "Priorización automática" | "¿Querrías que el sistema te dijera por cuál empezar?" | "¿Cómo decides qué hacer primero? ¿Siempre funciona?" |
| "Dashboard tiempo real para coordinadores" | "¿Te sería útil un dashboard?" | "Cuando necesitas saber cómo va el turno, ¿qué haces?" |

**Regla anti-sesgo:** La hipótesis del EFC es tu BRÚJULA, no tu DESTINO. Si el research descubre que
la solución propuesta no ataca el struggle real, documentar y recomendar pivot.

---

## Mapeo Discovery → Profundización

### Hallazgos del Discovery previo → Preguntas de profundización

| Hallazgo Discovery | Tipo | Pregunta de profundización |
|---|---|---|
| "Priorizan por cercanía, no urgencia" | Comportamiento | "Cuéntame cómo decides a qué pasillo ir primero. ¿Siempre es igual?" |
| "Post-its para tracking personal" | Workaround | "He visto que algunos compañeros usan notas. ¿Tú? ¿Para qué?" |
| "Coordinador no interviene hasta que es tarde" | Proceso | "Cuando un turno va complicado, ¿quién se da cuenta primero? ¿Cómo?" |

**Regla:** Si el Discovery previo ya tiene citas directas de usuarios, usarlas como punto de partida
(DESPUÉS de la narrativa libre del entrevistado, no antes).

### Explore (alternativas descartadas) → Preguntas de validación

| Alternativa descartada | Por qué explorar en entrevista |
|---|---|
| "Alertas Slack" → Descartada por "demasiada notificación" | ¿Los usuarios confirman notif. fatigue? ¿O es asunción? |
| "Migrar a MOT" → Descartada por "complejidad técnica" | ¿Los usuarios conocen MOT? ¿Lo usarían? |

---

## Templates de Guión para PRD

### Template A: Guión de Entrevista — PRD Modo Descubrir

```markdown
# Guión de Entrevista: PRD [Nombre]

**Equipo:** [Vertical]
**Hipótesis a explorar:** [Derivada del EAC/EFC del PRD]
**Duración:** 30-35 min
**Perfil usuario:** [Inferido del PRD — quién sufre el problema]

## Briefing interno (NO compartir con usuario)

**Datos del PRD a tener en mente (NO preguntar directamente):**
- Farola 1: [dato] → Explorar área: [tema]
- Farola 2: [dato] → Explorar área: [tema]
- Penumbra clave: "[quote]" → Validar si es real
- Hipótesis EFC: [solución propuesta] → NO mencionar, explorar el área

**Hallazgos Discovery previo a profundizar:**
- [Hallazgo 1] → Profundizar: [aspecto]
- [Hallazgo 2] → Profundizar: [aspecto]

**Criterios de éxito (Bloque 3):** [lista]

---

## Fase 1: Warm-up (3-5 min)

**Apertura:**
> "Hola [nombre], gracias por tu tiempo. Quiero entender cómo es tu día a día
> con [contexto general, SIN mencionar PRD]. No hay respuestas correctas."

**Contexto básico:**
1. [Pregunta sobre su rol/antigüedad]
2. [Pregunta sobre frecuencia de la actividad]

## Fase 2: Su vida / Problema (10-12 min)

**Apertura gold:**
> "Cuéntame cómo fue la última vez que [actividad relacionada con el problema del PRD],
> desde el principio hasta el final."

**Preguntas de profundización:**
1. [Pregunta que explora el problema del EAC sin mencionarlo]
2. [Pregunta sobre lo más frustrante/complicado]
3. [Pregunta derivada de Penumbra]

## Fase 3: Comportamiento actual (8-10 min)

**Preguntas:**
1. [Pregunta sobre herramientas/workarounds]
2. [Pregunta que profundiza hallazgo Discovery 1]
3. [Pregunta que profundiza hallazgo Discovery 2]
4. [Pregunta sobre cómo interactúa con otros actores]

## Fase 4: Deep dive (8-10 min)

**Preguntas de motivaciones JTBD:**
1. [Motivación funcional: qué necesita lograr]
2. [Motivación emocional: cómo se siente]
3. [Motivación social: quién observa/depende]
4. [Desired outcome: cómo sería si fuera perfecto]

## Fase 5: Cierre (3 min)

> "¿Hay algo que no te haya preguntado y crees que debería saber?"
> "¿Conoces a alguien que [perfil] y podría charlar conmigo?"

---

## Notas para el moderador

**Si el usuario menciona espontáneamente:**
- [Farola 1] → Profundizar: "¿Desde cuándo? ¿Cómo era antes?"
- [Penumbra] → Profundizar: "Cuéntame la última vez que pasó"
- [Algo de la hipótesis EFC] → Profundizar sin validar: "¿Y eso cómo te afecta?"

**Si el usuario NO menciona:**
- [Problema del EAC] → Podría ser que NO es un problema real. Documentar ausencia.
- [Hallazgo del Discovery] → ¿Era específico de otros perfiles?

**Señales de alerta:**
- Si confirma TODO el PRD → Revisar leading
- Si no confirma NADA → Revisar si el perfil es correcto
```

### Template B: Guión de Entrevista — PRD Modo Validar

```markdown
# Guión de Validación: PRD [Nombre]

**Equipo:** [Vertical]
**Modo:** Validación de hipótesis EFC con hallazgos Discovery
**Duración:** 25-30 min
**Perfil usuario:** [Del PRD]

## Briefing interno

**Hipótesis a validar (NO mencionar):**
- EFC: [solución propuesta] → Explorar área: [necesidad subyacente]
- Discovery hallazgo 1: [hecho] → ¿Se confirma con este perfil?
- Discovery hallazgo 2: [hecho] → ¿Se confirma?

**Hipótesis nulas (lo que refutaría el PRD):**
- Si nadie menciona [problema del EAC] → Problema no confirmado
- Si el workaround actual funciona bien → Solución menos urgente
- Si el struggle real es diferente → EFC necesita ajuste

---

## Fase 1-5: [Mismo formato que Template A pero con foco en validación]

## Notas para el moderador

**Matriz de validación (completar después):**
| Elemento PRD | ¿Mencionado? | ¿Espontáneo? | ¿Emoción? | ¿Workaround? | Estado |
|---|---|---|---|---|---|
| Problema EAC | Sí/No | Sí/No | Sí/No | Sí/No | ✅/🟡/❌ |
| Farola 1 | Sí/No | Sí/No | — | — | ✅/🟡/❌ |
| Penumbra 1 | Sí/No | Sí/No | Sí/No | — | ✅/🟡/❌ |
| Hipótesis EFC | Sí/No | Sí/No | Sí/No | — | ✅/🟡/❌ |

**Descubrimientos nuevos (no en PRD):**
- [Anotar cualquier insight que emerja y no estaba contemplado]
```

---

## Sección exploratoria obligatoria (ambos modos)

En AMBOS modos, SIEMPRE incluir exploración abierta para descubrir lo NO contemplado:

**Preguntas de exploración abierta:**
- "Aparte de lo que hemos hablado, ¿hay algo más que te complique [actividad]?"
- "¿Qué más te gustaría que fuera diferente?"
- "¿Hay algo que tus compañeros mencionan mucho?"
- "Si pudieras cambiar UNA cosa, ¿cuál sería?"

**Por qué es obligatoria:** El PRD refleja la visión del PM. El research debe dejar espacio
para descubrir lo que el PM no contempló.
