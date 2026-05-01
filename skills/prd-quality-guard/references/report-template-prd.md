# Template: Reporte PRD Quality Check

## Instrucciones
Este template define la estructura del reporte que genera la skill.
El reporte se crea como página de Notion.

---

## Estructura del Reporte

```markdown
# 🔍 PRD Quality Check

**PRD:** {Nombre del PRD}
**Equipo:** {Vertical}
**Fecha evaluación:** {YYYY-MM-DD}

---

## 📦 Inventario de Secciones PRD

### EAC (Estado Actual Conocido)
| Sección | Estado | Observación |
|---------|--------|-------------|
| Problema | ✅/⚠️/❌ | {Detalle} |
| Farolas | ✅/⚠️/❌ | {Detalle} |
| Penumbras | ✅/⚠️/❌ | {Detalle} |
| Próximos pasos | ✅/⚠️/❌ | {Detalle} |

### EFC (Estado Futuro Conocido)
| Sección | Estado | Observación |
|---------|--------|-------------|
| Hipótesis Solución | ✅/⚠️/❌ | {Detalle} |
| Aspectos financieros | ✅/⚠️/❌ | {Detalle} |
| Métricas | ✅/⚠️/❌ | {Detalle} |
| Dimensionamiento | ✅/⚠️/❌ | {Detalle} |

### Discovery + Scope
| Sección | Estado | Observación |
|---------|--------|-------------|
| Discovery | ✅/⚠️/❌ | {Detalle} |
| Explore | ✅/⚠️/❌ | {Detalle} |
| Funcionalidades | ✅/⚠️/❌ | {Detalle} |
| Flujos usuario | ✅/⚠️/❌ | {Detalle} |
| Exclusiones | ✅/⚠️/❌ | {Detalle} |
| FAQs | ✅/⚠️/❌ | {Detalle} |

**Resumen:** {N}/14 secciones completas ({%})

---

## 📊 Scorecard

| Dimensión | Score | Estado |
|-----------|-------|--------|
| D1: Completitud EAC | X.X/10 | 🔴/🟡/🟢/⭐ |
| D2: Claridad EFC + Métricas | X.X/10 | 🔴/🟡/🟢/⭐ |
| D3: Rigor Discovery + Scope | X.X/10 | 🔴/🟡/🟢/⭐ |
| **Score Global** | **X.X/10** | **🔴/🟡/🟢/⭐** |

### Gate Decision: {✅ PASS / ⚠️ CONDICIONAL / ❌ FAIL}

{Explicación breve de la decisión}

---

## ✅ Fortalezas (Top 3)

1. **{Título}:** {Descripción con evidencia del PRD}
2. **{Título}:** {Descripción con evidencia del PRD}
3. **{Título}:** {Descripción con evidencia del PRD}

---

## 🚨 Antipatrones Detectados

{Si se detectaron antipatrones AP-PRD-1 a AP-PRD-5}

| # | Antipatrón | Texto encontrado | Impacto | Recomendación |
|---|------------|------------------|---------|---------------|
| 1 | AP-PRD-{N}: {Nombre} | "{texto literal}" | {Dim afectada} | {Cómo corregir} |

{Si no se detectaron: "No se detectaron antipatrones. ✅"}

---

## 📋 Análisis por Dimensión

### D1: Completitud EAC ({score}/10)

**Problema:** {Evaluación — ¿claro, concreto, cuantificado?}
**Farolas:** {Evaluación — cuántas, calidad, con baseline/fuente}
**Penumbras:** {Evaluación — cuántas, calidad, con citas/procedencia}
**Contexto temporal:** {¿Explica por qué ahora?}
**Impacto cuantificado:** {¿En €, usuarios, operaciones?}
**Próximos pasos:** {¿Claros y accionables?}

### D2: Claridad EFC + Métricas ({score}/10)

**Hipótesis Solución:** {Evaluación — ¿formulada correctamente? ¿Basada en EAC?}
**Métricas:** {Evaluación — cuántas, formato baseline→target→plazo}
**Aspectos financieros:** {Evaluación — ¿números concretos? ¿ROI?}
**Dimensionamiento:** {Evaluación — ¿realista? ¿Fases?}
**Criterios de éxito:** {¿Medibles? ¿Go/no-go?}

### D3: Rigor Discovery + Scope ({score}/10)

**Discovery:** {Evaluación — metodología, hallazgos, cómo informan solución}
**Explore:** {Evaluación — ¿alternativas? ¿Criterios de evaluación?}
**Funcionalidades:** {Evaluación — ¿priorizadas? ¿Vinculadas a problemas?}
**Flujos usuario:** {Evaluación — ¿documentados? ¿Con actores?}
**Exclusiones:** {Evaluación — ¿explícitas? ¿Justificadas?}
**FAQs:** {Evaluación — ¿anticipatorias? ¿Técnicas + negocio?}

---

## 🎯 Recomendaciones

### 🚨 Críticas (resolver antes de pasar a research)
1. {Acción concreta con ejemplo}

### 🟡 Importantes (mejorar esta semana)
1. {Acción concreta con ejemplo}

### ⚪ Mejora continua
1. {Acción concreta con ejemplo}

---

## ➡️ Siguiente Paso

{Depende del gate:}
{PASS → "Ejecutar: Research para el PRD de {nombre}. Usar /research con source_type=PRD"}
{CONDICIONAL → "Resolver recomendaciones críticas y volver a evaluar"}
{FAIL → "Completar secciones faltantes del PRD y volver a evaluar"}

{Si hay secciones vacías, SIEMPRE incluir:}
{🚨 "IMPORTANTE: Completar las secciones vacías del PRD antes de proceder"}
```

---

## Reglas de Generación

1. **SIEMPRE** incluir evidencia literal del PRD (quotes)
2. **SIEMPRE** dar recomendaciones accionables (no genéricas)
3. **SIEMPRE** incluir inventario de secciones como primera sección del reporte
4. **NUNCA** sugerir que una sección vacía "no es necesaria"
5. **SIEMPRE** generar como markdown (no como documento ofimático)
6. Si el PRD tiene Discovery débil (D3 < 5), **SIEMPRE** recomendar más Discovery antes de research
7. Si el PRD viene de otro formato (GSD output, Brief, etc.), indicar qué secciones se trasladaron correctamente y cuáles necesitan completarse
8. Las recomendaciones deben ayudar al PM a mejorar su PRD, no a diseñar la solución
