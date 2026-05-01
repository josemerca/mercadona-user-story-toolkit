# De Evidencia de Research a JTBDs Estructurados

## Principio fundamental

> "Saber que sabemos lo que no sabíamos y por qué podemos decir que lo sabemos."
>
> Las observaciones son HECHOS. Los aprendizajes son INTERPRETACIONES.
> Mezclarlos es el error más común y más peligroso del research.

---

## Las dos columnas del análisis

```
┌────────────────────────────┐    ┌────────────────────────────┐
│ OBSERVACIONES              │    │ APRENDIZAJES               │
│ (Lo que vimos/escuchamos)  │    │ (Lo que creemos que         │
│                            │    │  significan los hechos)     │
├────────────────────────────┤    ├────────────────────────────┤
│ • Hechos de campo          │    │ • Interpretaciones JTBD    │
│ • Comportamientos          │ →  │ • Qué trabajo emerge       │
│ • Quotes literales         │    │ • Qué struggle real tiene  │
│ • Datos cuantitativos      │    │ • Qué motivaciones lo      │
│ • Workarounds observados   │    │   mueven                   │
│                            │    │                            │
│ VERIFICABLE: otro          │    │ DEBATIBLE: requiere        │
│ investigador vería lo      │    │ interpretación en clave    │
│ mismo                      │    │ JTBD                       │
└────────────────────────────┘    └────────────────────────────┘
```

**Test de separación:** ¿Otro investigador que estuviera en la sesión diría lo mismo?
- **Sí** → Es una observación (hecho)
- **Depende** → Es un aprendizaje (interpretación)

---

## Proceso de análisis: 5 pasos

### Paso 1: Procesamiento inmediato (mismo día de cada sesión)

Después de cada sesión (observación o entrevista), capturar en la plantilla de notas:

1. **Top 3 hallazgos** — Lo más importante que aprendiste
2. **Sorpresas** — Qué no esperabas (especialmente vs PRD)
3. **Quotes gold** — Frases textuales que capturan insights
4. **Workarounds observados** — Qué hace para resolver problemas (señal de job mal servido)
5. **Cobertura de criterios** — ¿Qué criterio de éxito (Bloque 3) cubrió esta sesión?
6. **Validación PRD** — ¿Qué del PF se confirmó? ¿Qué no?

### Paso 2: Filtrado de Bad Data

Para cada dato extraído, clasificar:

| Clasificación | Criterio | Acción |
|---|---|---|
| ✅ **Hecho observado** | Comportamiento visto directamente en campo | Usar como observación |
| ✅ **Quote gold** | Frase literal que captura insight emocional/situacional | Usar como observación |
| ✅ **Comportamiento narrado** | Acción pasada específica con detalles y fechas | Usar como observación |
| ⚠️ **Dato débil** | Genérico pero con potencial (anclar en siguiente sesión) | Marcar para follow-up |
| ❌ **Cumplido** | "Me parece bien", "No me quejo" | Descartar |
| ❌ **Fluff** | "Siempre...", "Normalmente...", "Lo haría..." | Descartar |
| ❌ **Feature request** | "Deberíais hacer..." | Guardar la motivación, descartar la solución |

### Paso 3: Organización por criterio de éxito

**Este es el paso clave de v0.5.** Toda la evidencia se organiza según los criterios
definidos en el Bloque 3, no por sesión ni por JTBD.

Para cada criterio de éxito:

```markdown
### Criterio [N]: [Pregunta verificable del Bloque 3]

#### Observaciones (HECHOS)

**De observación de campo:**
- [Sesión N, Participante X]: [Hecho observado]
- [Sesión N, Participante Y]: [Hecho observado]

**De entrevistas (quotes):**
> "[Quote literal]" — Participante X, Sesión N, contexto: [cuándo/por qué lo dijo]
> "[Quote literal]" — Participante Y, Sesión N, contexto: [cuándo/por qué lo dijo]

**Datos cuantitativos:**
- [N] de [M] participantes [describieron este comportamiento / mencionaron este tema]
- Frecuencia observada: [dato]

**Workarounds relacionados:**
- [Descripción del workaround] — Observado en Sesión [N]
  → Señal de: [qué job está mal servido]

#### Aprendizajes (INTERPRETACIONES en clave JTBD)

**Qué creemos que significan los hechos:**
- [Interpretación 1] — Basado en: [referencia a observaciones específicas arriba]
- [Interpretación 2] — Basado en: [referencia a observaciones específicas arriba]

**Componentes JTBD que emergen de este criterio:**
- [Componente JTBD]: [Lo descubierto] — Evidencia: [referencia a observación]

**¿Criterio cubierto?** ✅ Sí / 🟡 Parcial / ❌ No
- Justificación: [por qué, con referencia al umbral definido en Bloque 3]
- Si parcial/no: [qué tipo de evidencia falta]
```

### Paso 4: Identificación de patrones entre criterios

Después de analizar cada criterio por separado:

- **Convergencias:** ¿Hay observaciones que cubren varios criterios? → Señal de JTBD fuerte
- **Repeticiones:** ¿Qué dicen/hacen ≥3 participantes? → Patrón confirmado
- **Contradicciones:** ¿Dónde hay desacuerdo entre lo observado y lo dicho? → Insight potente
- **Contradicciones con PRD:** ¿Qué del PF NO se confirma? → Hallazgo valioso
- **Extremos:** ¿Quién tiene el problema más agudo? → Power user del JTBD
- **Ausencias:** ¿Qué del PRD NADIE menciona ni hace? → Posible falso problema

### Paso 5: Síntesis en JTBDs

Los JTBDs EMERGEN como síntesis del análisis por criterios. No se imponen desde el principio.

---

## Framework: De Patrones a JTBDs

### Cómo emerge un JTBD del análisis

```
Criterio 1: ¿Cuál es el trigger? ──────────┐
  Observaciones: 5/8 participantes           │
  describen el mismo evento                  │
                                             ├──→ JTBD: "Cuando [trigger],
Criterio 2: ¿Qué struggle tiene? ──────────┤     quiero [motivación funcional],
  Observaciones: 3 workarounds activos       │     para [desired outcome]"
  + quotes con emoción                       │
                                             │     Componentes: Trigger ✅,
Criterio 3: ¿Qué motivaciones? ────────────┘     Struggle ✅, Motivaciones ✅
  Observaciones: quotes emocionales                Confianza: 🟢 Alta
  + contexto social observado
```

### Estructura JTBD compatible con jtbd-to-stories

```markdown
### JTBD [N]: [Título descriptivo]

**Confianza:** 🟢 Alta / 🟡 Media / 🔴 Baja
**Basado en:** [N] observaciones + [N] entrevistas
**Criterios que cubre:** [Lista de criterios del Bloque 3]

#### Formulación JTBD
Cuando [trigger real descubierto en el research],
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
- Mencionado/observado por [N]/[M] participantes
- Workarounds observados: [Sí/No — descripción]
- Emoción al describirlo: [Sí/No — contexto]
- Ejemplos con fechas/detalles: [Sí/No]
- Triangulación observación-entrevista: [Coincide / Discrepa — detalle]

#### Wendel Checklist (datos reales)
1. **Experiencia previa:** [dato real de las sesiones]
2. **Relación con producto:** [dato real]
3. **Motivación situacional:** [dato real]
4. **Impedimento actual:** [dato real]
```

---

## Cruce PRD: Validación cruzada

### Template de validación

| Elemento PRD | Fuente | Estado | Evidencia real |
|---|---|---|---|
| Farola: "[métrica]" | PF | ✅/❌/🟡 | "[dato de research]" |
| Penumbra: "[quote]" | PF | ✅/❌/🟡 | "[quote/observación real]" |
| Línea Roja: "[restricción]" | PF | ✅/❌/🟡 | "[evidencia]" |
| Job Performer: "[rol]" | PI | ✅/❌/🟡 | "[perfil real observado]" |
| JTBD existente: "[job]" | PI | ✅/❌/🟡 | "[evidencia]" |

### Significado de estados

- ✅ **Confirmado:** ≥3 participantes validan con comportamiento observado o ejemplos específicos
- 🟡 **Parcial:** 1-2 participantes validan, o la observación contradice parcialmente lo dicho
- ❌ **No confirmado:** Ningún participante lo menciona/muestra, o evidencia lo contradice

### Hallazgos nuevos (no en PRD)

| Hallazgo | Tipo | Frecuencia | Impacto | Criterio relacionado |
|---|---|---|---|---|
| [Problema nuevo] | Struggle | N/M participantes | Alto/Medio/Bajo | Criterio [N] |
| [Motivación nueva] | Emocional | N/M participantes | Alto/Medio/Bajo | Criterio [N] |
| [Comportamiento inesperado] | Proceso | N/M participantes | Alto/Medio/Bajo | Criterio [N] |

---

## Bloque 5: Conclusiones (síntesis ejecutiva)

### Estructura

Las conclusiones NO introducen información nueva. Solo consolidan el Bloque 4.

```markdown
## Conclusiones

### Síntesis ejecutiva

1. **[Conclusión principal]** — El trabajo central que descubrimos es [JTBD
   principal en una frase]. Lo más relevante es [insight clave].

2. **[Conclusión sobre JTBDs]** — Descubrimos [N] JTBDs con evidencia de
   [N] sesiones. [Resumen 1-2 líneas cada uno].

3. **[Conclusión sobre PRD]** — [Qué se confirmó, qué no, qué es NUEVO].

4. **[Nivel de confianza]** — Los criterios de éxito [estado]. La evidencia
   es [suficiente / necesita refuerzo en X].

### JTBDs descubiertos (resumen)

| # | JTBD | Confianza | Criterios que cubre |
|---|------|-----------|---------------------|
| 1 | [Título] | 🟢/🟡/🔴 | Criterio 1, 2 |
| 2 | [Título] | 🟢/🟡/🔴 | Criterio 2, 3 |
```

### Reglas

| Regla | Descripción |
|-------|-------------|
| **CON-1** | NO introduce información nueva |
| **CON-2** | 2-4 bullets máximo |
| **CON-3** | JTBDs descubiertos son pieza central |
| **CON-4** | Mencionar qué del PRD se confirmó y qué no |
| **CON-5** | Tono: informar, no recomendar |

---

## Template: Reporte de Research Completo (6 Bloques)

```markdown
# Research: PRD [Nombre del PRD]

## Bloque 1: Propósito
[Propósito formulado en términos del TRABAJO]

## Bloque 2: Plan
### Metodología
- **Observación:** [N] sesiones de [N] min en [entorno]
- **Entrevistas:** [N] sesiones de [N] min, modo [Descubrir/Validar]
- **Participantes:** [N] [perfil], criterios: [selección]
- **Período:** [fechas]
- **PRD de referencia:** [nombre, URL Notion]

## Bloque 3: Criterios de Éxito
| # | Criterio | Componente JTBD | Umbral |
|---|----------|-----------------|--------|
| 1 | [Pregunta] | [Componente] | [Mínimo evidencia] |
| 2 | ... | ... | ... |

## Bloque 4: Análisis

### Criterio 1: [Pregunta]
#### Observaciones (hechos)
[Observaciones organizadas]
#### Aprendizajes (interpretaciones JTBD)
[Interpretaciones con referencia a observaciones]
**¿Criterio cubierto?** [✅/🟡/❌]

### Criterio 2: [Pregunta]
[Mismo formato...]

### JTBDs Descubiertos
[Fichas JTBD con componentes y evidencia]

### Validación cruzada PRD
[Tabla de validación Farolas, Penumbras, etc.]

### Hallazgos nuevos (no en PRD)
[Tabla de hallazgos]

## Bloque 5: Conclusiones
[Síntesis ejecutiva 2-4 bullets]
[Tabla resumen JTBDs]

## Bloque 6: Next Steps
**Decisión:** [Pasar a Explore / Más research]
[Evaluación de criterios]
[JTBDs listos / Research adicional necesario]

## Anexo: Quotes destacados
> "[Quote 1]" — Participante X, [contexto]
> "[Quote 2]" — Participante Y, [contexto]
```

---

## Criterios de calidad del análisis

### Checklist antes de reportar

- [ ] **Separación obligatoria:** Observaciones y aprendizajes están en columnas/secciones separadas
- [ ] **Organizado por criterio:** El análisis sigue los criterios del Bloque 3, no por sesión
- [ ] **Basado en hechos:** Cada aprendizaje tiene referencia a observación/quote específica
- [ ] **Sin cherry-picking:** Incluyo evidencia contradictoria
- [ ] **Quotes literales:** Uso palabras exactas, no paráfrasis
- [ ] **Tamaño muestra claro:** Indico cuántos participantes dijeron/hicieron qué (N/M)
- [ ] **Cruce PRD completo:** Todas las Farolas y Penumbras evaluadas
- [ ] **Triangulación:** Contrasto lo observado con lo dicho cuando hay discrepancia
- [ ] **Criterios evaluados:** Cada criterio tiene estado explícito (✅/🟡/❌)
- [ ] **3 motivaciones:** Cada JTBD tiene funcional, emocional y social con evidencia
- [ ] **Workarounds documentados:** Los que se observaron y los que se mencionaron
- [ ] **Limitaciones reconocidas:** Sesgos o gaps en los datos

### Señales de buen análisis

✅ "5 de 8 participantes hicieron/dijeron espontáneamente [comportamiento]"
✅ "Observamos que [hecho]. En entrevista, [participante] explicó: '[quote]'"
✅ "La Penumbra '[quote PF]' se confirma en observación pero con matiz: [detalle]"
✅ "Descubrimos un struggle no documentado en el PRD: [hallazgo] — observado en [N] sesiones"
✅ "Lo que dicen y lo que hacen no coincide: dicen X pero observamos Y → [interpretación]"
✅ "La Farola de 8 min no se confirma: observamos 12-15 min en 4 de 5 sesiones"

### Señales de mal análisis

❌ "Los usuarios quieren X" (sin especificar cuántos ni evidencia)
❌ "Claramente el problema es Y" (sin quotes ni observaciones)
❌ "Confirmamos todo lo que dice el PRD" (sospechoso — posible sesgo)
❌ Observaciones y aprendizajes mezclados en el mismo párrafo
❌ Análisis organizado por sesión en vez de por criterio
❌ Solo entrevistas sin observación (o viceversa) sin justificación
❌ Conclusiones que coinciden exactamente con el PRD (¿preguntaste/observaste bien?)
