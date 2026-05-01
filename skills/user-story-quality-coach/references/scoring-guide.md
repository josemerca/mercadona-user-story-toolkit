# Guía de Scoring Detallada

## Dimensión 1: JTBD & Problem Context (0-10)

**Pregunta clave:** ¿Hay evidencia cuanti+cuali del problema antes de la solución?

| Score | Criterio |
|-------|----------|
| 9-10 | Formato Job Story perfecto ("Cuando [situación], quiero [capacidad], para [outcome]"). Evidencia cuantitativa (datos, métricas). Evidencia cualitativa (quotes, observaciones). Solución como hipótesis. |
| 7-8 | Formato Job Story correcto. Evidencia sólida (falta cuanti O cuali). Problema claro antes de solución. |
| 5-6 | Problema mencionado pero solution-first. Evidencia débil/anecdótica. No usa formato Job Story. |
| 3-4 | Problema vago o sin evidencia. Solución prescrita sin contexto. Confunde problema usuario con problema negocio. |
| 0-2 | Sin contexto de problema. Pura especificación de solución. Sin evidencia. |

---

## Dimensión 2: User Specificity (0-10)

**Checklist de Wendel (4 preguntas):**
1. ¿Qué experiencia previa tiene este usuario?
2. ¿Qué relación tiene con el producto/empresa?
3. ¿Qué le motiva en esta situación específica?
4. ¿Qué le impide conseguirlo ahora?

| Score | Criterio | Ejemplo |
|-------|----------|---------|
| 9-10 | Responde 4/4 preguntas Wendel. Usuario específico y diferenciado. | "Jefe recurrente que compra 1-2x/semana los mismos ~40 productos" |
| 7-8 | Segmento específico. Responde 3/4 preguntas. | "Jefe que busca descuentos en SPBs" |
| 5-6 | Algo de especificidad pero genérico. | "Usuario experimentado" |
| 3-4 | Rol genérico con contexto mínimo. | "Usuario de la app" |
| 0-2 | Completamente genérico. | "As a user" o "As a jefe" |

---

## Dimensión 3: Behavior Change (0-10)

**Template esperado:**
```
START: [Qué empezarán a hacer] con frecuencia [X]
STOP: [Qué dejarán de hacer]
DIFFERENT: [Qué harán diferente] [% mejora]
Rango: Mínimo / Target / Over-top
```

| Score | Criterio | Ejemplo |
|-------|----------|---------|
| 9-10 | START/STOP/DIFFERENT cuantificado. Rango min/target/over definido. | "Reducir tiempo búsqueda de 8 min a 4 min (50% mejora). Min: -30% / Target: -50% / Over: -70%" |
| 7-8 | Cambio claro con números. Falta rango completo. | "Reducir tiempo búsqueda 50%" |
| 5-6 | Cambio mencionado pero no cuantificado. | "Comprar más rápido" |
| 3-4 | Beneficio vago. | "Mejor experiencia" |
| 0-2 | Beneficio es "tener la feature". Sin cambio de comportamiento. | "Para poder usar filtros" |

---

## Dimensión 4: Zone of Control (0-10)

**Pregunta clave:** ¿El "I want" está en control del equipo?

| Score | Criterio |
|-------|----------|
| 9-10 | 100% en control del equipo. Dependencias identificadas y gestionables. Criterios claros de control vs influencia. |
| 7-8 | Mayormente en control. Dependencias externas menores y conocidas. |
| 5-6 | Dependencia externa significativa pero manejable. Coordinación con otro equipo necesaria. |
| 3-4 | Dependencia crítica de equipo externo o vendor. Deliverable fuera del control directo. |
| 0-2 | Completamente fuera del control del equipo. Depende de factores externos no gestionables. |

---

## Dimensión 5: Time Constraints (0-10)

**Pregunta clave:** ¿Urgencia real con consecuencias, o artificial?

| Score | Criterio | Ejemplo |
|-------|----------|---------|
| 9-10 | Urgencia real con consecuencias claras O sin deadline artificial. "Best before" justificada. | "Antes iOS 18 en Septiembre para evitar fricción usuarios" |
| 7-8 | Deadline justificado con impacto negocio claro. | "Antes de Black Friday" |
| 5-6 | Deadline mencionado, justificación débil. | "Para Q1" |
| 3-4 | Urgencia artificial sin consecuencias reales. | "ASAP" |
| 0-2 | Todo es urgente (red flag si >50% sprint tiene deadlines). Fake urgency. | "Crítico" sin contexto |

---

## Dimensión 6: Survivable Experiment (0-10)

**Pregunta clave:** ¿Qué pasa si estamos equivocados?

| Score | Criterio | Ejemplo |
|-------|----------|---------|
| 9-10 | ≤1 sprint de esfuerzo. Costo si equivocados definido y aceptable. Plan de rollback claro. | "1 sprint dev + 2 semanas test. Si falla: rollback. Costo aceptable vs aprendizaje." |
| 7-8 | 1-2 sprints. Fallo es asequible. Mitigación considerada. | "2 sprints, feature flag para rollback" |
| 5-6 | 2-3 sprints. Costo moderado si falla. | "3 sprints de esfuerzo" |
| 3-4 | 3-6 sprints. Alto costo si equivocados. Riesgoso. | "Requiere migración de datos" |
| 0-2 | >6 sprints. Catastrófico si falla. Sin plan de rollback. | "Reescritura completa del sistema" |

---

## Completitud Operativa (checklist, no scoring)

Estas secciones no puntúan en las 6 dimensiones pero se reportan como **señales de readiness**. Su ausencia no baja el score pero sí genera alertas en el reporte.

### Diseño (Protos/Pantallas)

| Estado | Señal |
|--------|-------|
| ✅ Completo | Links Figma presentes para cada plataforma relevante (mobile, web). Proto y pantallas diferenciados |
| ⚠️ Parcial | Solo una plataforma, o solo proto sin pantallas finales, o link roto |
| ❌ Ausente | Sin sección de diseño, o sección vacía |
| ➖ No aplica | Story puramente backend/infra sin componente visual |

**Qué evaluar:**
- ¿Hay links Figma para mobile Y web (si aplica)?
- ¿Se distingue proto (flujo interactivo) de pantallas (specs para dev)?
- ¿Los links son accesibles (no placeholder)?

### Traducciones

| Estado | Señal |
|--------|-------|
| ✅ Completo | Traducciones definidas (link a sheet o texto inline) |
| ⚠️ WIP | Sección presente pero marcada como "WIP" o incompleta |
| ❌ Ausente | Sin sección de traducciones |
| ➖ No aplica | Story sin textos visibles al usuario |

**Qué evaluar:**
- ¿Hay contenido o solo "WIP"?
- ¿Cubre todos los idiomas necesarios?
- Si la story tiene UI, ¿las traducciones están listas antes de dev?

### Métricas/Analytics

| Estado | Señal |
|--------|-------|
| ✅ Completo | Eventos definidos con propiedades + medición de éxito |
| ⚠️ Parcial | Eventos sin propiedades, o sin medición de éxito |
| ❌ Ausente | Sin sección de métricas |

### Go-to-market

| Estado | Señal |
|--------|-------|
| ✅ Completo | Plan de activación definido (feature flag, comunicación, coordinación) |
| ⚠️ Parcial | Mencionado pero sin plan concreto |
| ❌ Ausente | Sin sección de go-to-market |

---

## Cálculo de Score Global

```
Score Global = Promedio(Dim1, Dim2, Dim3, Dim4, Dim5, Dim6)
```

**Interpretación:**
- 🔴 **0-4 Deficiente:** Requiere reescritura completa
- 🟡 **5-6 Necesita mejora:** Refinamiento necesario antes de desarrollo
- 🟢 **7-8 Aceptable:** Lista para desarrollo con mejoras menores
- ⭐ **9-10 Excelente:** Modelo a seguir para el equipo
