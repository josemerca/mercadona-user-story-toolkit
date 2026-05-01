# Checklist de Calidad de User Stories

## Validación Rápida (7 criterios obligatorios)

| # | Criterio | ✓ | Red Flag si falta |
|---|----------|---|-------------------|
| 1 | Usuario específico | ☐ | "As a user", "Como cliente" |
| 2 | Wendel Checklist (4/4) | ☐ | Falta contexto del usuario |
| 3 | Job real (no solución) | ☐ | "Quiero un botón que..." |
| 4 | 3 dimensiones motivación | ☐ | Solo tarea funcional |
| 5 | Behavior change cuantificado | ☐ | "Para tener la feature" |
| 6 | Rangos min-target-over | ☐ | Sin criterios de éxito |
| 7 | Sin antipatrones críticos | ☐ | Fake Story, Solution as Need |

**Regla:** Si faltan ≥2 criterios, la story NO está lista para desarrollo.

---

## Scoring por Dimensiones (0-10)

### Dimensión 1: JTBD & Problem Context

| Score | Criterio |
|-------|----------|
| 9-10 | Formato Job Story perfecto + evidencia cuanti + cuali + solución como hipótesis |
| 7-8 | Formato correcto + evidencia sólida (falta cuanti O cuali) |
| 5-6 | Problema mencionado pero solution-first + evidencia débil |
| 3-4 | Problema vago o sin evidencia + solución prescrita |
| 0-2 | Sin contexto de problema, pura especificación |

### Dimensión 2: User Specificity

| Score | Criterio | Ejemplo |
|-------|----------|---------|
| 9-10 | 4/4 Wendel + usuario diferenciado | "Jefe recurrente que compra ~40 productos fijos" |
| 7-8 | 3/4 Wendel + segmento específico | "Jefe cazador de ofertas" |
| 5-6 | Algo de especificidad | "Usuario experimentado" |
| 3-4 | Rol genérico con contexto mínimo | "Usuario de la app" |
| 0-2 | Completamente genérico | "As a user" |

### Dimensión 3: Behavior Change

| Score | Criterio |
|-------|----------|
| 9-10 | START/STOP/DIFFERENT cuantificado + rango min/target/over |
| 7-8 | Cambio claro con números, falta rango completo |
| 5-6 | Cambio mencionado pero no cuantificado |
| 3-4 | Beneficio vago |
| 0-2 | Beneficio = "tener la feature" |

### Dimensión 4: Zone of Control

| Score | Criterio |
|-------|----------|
| 9-10 | 100% en control del equipo + dependencias gestionables |
| 7-8 | Mayormente en control + dependencias menores |
| 5-6 | Dependencia externa significativa pero manejable |
| 3-4 | Dependencia crítica de equipo externo |
| 0-2 | Completamente fuera de control |

### Dimensión 5: Time Constraints

| Score | Criterio |
|-------|----------|
| 9-10 | Urgencia real con consecuencias claras O sin deadline artificial |
| 7-8 | Deadline justificado con impacto negocio |
| 5-6 | Deadline mencionado, justificación débil |
| 3-4 | Urgencia artificial sin consecuencias |
| 0-2 | Todo es urgente (fake urgency) |

### Dimensión 6: Survivable Experiment

| Score | Criterio |
|-------|----------|
| 9-10 | ≤1 sprint + costo aceptable si falla + rollback claro |
| 7-8 | 1-2 sprints + fallo asequible |
| 5-6 | 2-3 sprints + costo moderado |
| 3-4 | 3-6 sprints + alto costo si falla |
| 0-2 | >6 sprints + catastrófico si falla |

---

## Antipatrones a Detectar

### 1. "As a user..." (Usuario Genérico)
**Señal:** "Como usuario", "Como cliente", "Como jefe" sin especificar
**Impacto:** User Specificity ≤4
**Corrección:** Aplicar Wendel Checklist

### 2. No Behavior Change
**Señal:** Beneficio es "poder usar la feature", "tener acceso a..."
**Impacto:** Behavior Change ≤2
**Corrección:** Definir START/STOP/DIFFERENT con métricas

### 3. Fake Story
**Señal:** Beneficiario real es el equipo, no el usuario final
**Ejemplo:** "Como Product Manager quiero dashboards para trackear métricas"
**Test:** ¿El usuario final se beneficia directamente?
**Corrección:** Reformular para usuario final

### 4. Solution as Need
**Señal:** "Quiero un botón", "Necesito un carrusel", "Quiero filtros"
**Impacto:** JTBD ≤4
**Corrección:** Profundizar con "¿Por qué?" hasta encontrar el job

### 5. Deliverable Outside Control
**Señal:** Dependencia crítica de otro equipo o vendor
**Impacto:** Zone of Control ≤3
**Corrección:** Redefinir alcance o identificar coordinación

### 6. Everything is Urgent
**Señal:** >50% de stories con deadline, uso de "ASAP", "Crítico"
**Impacto:** Time Constraints ≤2
**Corrección:** Priorizar y justificar urgencia real

### 7. Division by Technical Layers
**Señal:** Stories separadas para frontend/backend/BD
**Ejemplo:** "Story 1: API de filtros", "Story 2: UI de filtros"
**Corrección:** Combinar en slice vertical con valor usuario

---

## Cálculo de Score Global

```
Score Global = (D1 + D2 + D3 + D4 + D5 + D6) / 6
```

### Interpretación

| Score | Categoría | Acción |
|-------|-----------|--------|
| 9-10 ⭐ | Excelente | Modelo para el equipo |
| 7-8 🟢 | Aceptable | Lista para desarrollo con mejoras menores |
| 5-6 🟡 | Necesita mejora | Refinamiento antes de desarrollo |
| 0-4 🔴 | Deficiente | Requiere reescritura completa |

---

## Definition of Ready

Una story está **Ready** cuando cumple:

- [ ] Usuario específico identificado (≥3/4 Wendel)
- [ ] Problema documentado con evidencia (cuanti O cuali mínimo)
- [ ] Behavior change definido (START/STOP/DIFFERENT)
- [ ] Métrica de éxito cuantificada con rango min/target
- [ ] Dependencias identificadas y en control del equipo
- [ ] Tamaño ≤2 sprints (experimento supervivable)
- [ ] Sin antipatrones críticos (Fake Story, As a user)
- [ ] Criterios de aceptación en formato Given-When-Then
