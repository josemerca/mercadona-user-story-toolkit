# User Story Builder - Referencia

Material de referencia complementario al flujo principal en `SKILL.md`.

---

## S1 Antipatrones a Evitar

| Antipatron | Senal | Correccion |
|------------|-------|------------|
| "As a user..." | Usuario generico | Especificar con Wendel |
| No Behavior Change | Beneficio = "tener la feature" | Definir START/STOP/DIFFERENT |
| Fake Story | Beneficiario real es el equipo | Reformular para usuario final |
| Solution as Need | "Quiero un boton que..." | Profundizar con "por que?" |

---

## S2 Sistema de Scoring (6 Dimensiones)

**Compatible con `/user-story-quality-coach` y `/jtbd-to-stories`**

Cada story generada debe evaluarse en estas 6 dimensiones (0-10):

| Dim | Nombre | Pregunta Clave | Fuente en Builder |
|-----|--------|----------------|-------------------|
| 1 | **JTBD & Problem Context** | Hay evidencia cuanti+cuali? | Fase 1 + Evidencia |
| 2 | **User Specificity** | Responde Wendel 4/4? | Fase 3 |
| 3 | **Behavior Change** | Que haran DIFERENTE? | Fase 5 |
| 4 | **Zone of Control** | El equipo controla? | Fase 2 (detectar scope) |
| 5 | **Time Constraints** | Urgencia real? | Fase 1 (contexto) |
| 6 | **Survivable Experiment** | Que pasa si falla? | Fase 5 (rangos) |

### Interpretacion

| Score | Estado | Accion |
|-------|--------|--------|
| 0-4 | Requiere reescritura | Volver a fase correspondiente |
| 5-6 | Necesita refinamiento | Iterar antes de finalizar |
| 7-8 | Lista para desarrollo | Proceder con confianza |
| 9-10 | Modelo a seguir | Usar como referencia |

**Score Global = Promedio(Dim1...Dim6)**

### Reglas de Penalizacion

- **Dim 2 <= 5** si no hay Wendel Checklist 4/4
- **Dim 3 <= 5** si no hay START/STOP/DIFFERENT con rangos
- **Dim 1 <= 7** si solo hay evidencia cualitativa (sin cuantitativa)

---

## S3 Integracion con Otras Skills

### Flujo Recomendado

```
+-------------------------------------------------------------+
|  Tienes JTBDs validados con research?                       |
|         |                                                   |
|    SI   |   NO                                              |
|    v    |   v                                               |
| /jtbd-to-stories      /user-story-builder (ESTA SKILL)     |
| (genera desde JTBDs)  (guia conversacional desde cero)     |
|         |                   |                               |
|         +--------+----------+                               |
|                  v                                          |
|         STORY GENERADA                                      |
|                  |                                          |
|                  v                                          |
|         /user-story-quality-coach                           |
|         (validar y puntuar)                                 |
+-------------------------------------------------------------+
```

### Cuando Derivar a Otras Skills

| Situacion | Skill Recomendada |
|-----------|-------------------|
| "Tengo JTBDs validados de research" | -> `/jtbd-to-stories` |
| "Analiza estas stories del sprint" | -> `/user-story-quality-coach` |
| "Evalua el backlog del equipo" | -> `/user-story-quality-coach` |
| "Genera stories desde un PRD" | -> `/prd-quality-guard` -> `/research` -> `/stories` |

---

## S4 Referencias

- **Template completo:** Ver `references/story-template.md`
- **Guia JTBD detallada:** Ver `references/jtbd-guide.md`
- **Ejemplos de stories excelentes:** Ver `references/examples.md`
- **Scoring de calidad:** Ver `references/quality-checklist.md`
- **Configuracion compartida:** Ver `../shared-config.md`

### Skills Relacionadas

| Skill | Proposito | Integracion |
|-------|-----------|-------------|
| `/jtbd-to-stories` | Convertir JTBDs en stories | Usa mismo template JTBD |
| `/user-story-quality-coach` | Evaluar stories existentes | Usa mismo scoring 6 dimensiones |

---

## S5 Comandos Rapidos

| Comando | Accion |
|---------|--------|
| `Ayudame a escribir una user story` | Iniciar flujo completo |
| `Tengo esta idea: [descripcion]` | Analizar y guiar desde Fase 1 |
| `Reescribe esta story: [texto]` | Mejorar story existente |
| `Que le falta a esta story?` | Validar contra checklist |
