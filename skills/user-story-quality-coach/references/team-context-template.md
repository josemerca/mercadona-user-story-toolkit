# Template de Contexto por Equipo

Usar este template para crear `references/teams/{team-key}.md`. El contexto de equipo es **opcional pero recomendado**: ayuda a la skill a detectar Fake Stories (con usuarios inválidos para tu dominio) y a sugerir métricas relevantes.

---

```markdown
# Contexto: {Nombre Equipo}

**Issue tracker key:** {KEY}
**Dominio:** {Cliente final / Interno / Mixto}
**Última actualización:** YYYY-MM-DD

## Usuarios específicos válidos

### Usuarios primarios
| Usuario | Descripción | Contexto típico |
|---------|-------------|-----------------|
| [Nombre rol] | [Descripción breve] | [Cuándo interactúa] |

### Usuarios secundarios
| Usuario | Descripción | Contexto típico |
|---------|-------------|-----------------|
| [Nombre rol] | [Descripción breve] | [Cuándo interactúa] |

### ⚠️ Usuarios de alto riesgo (verificar Fake Story)
- [Rol interno que puede ser beneficiario real vs proxy]

## Métricas relevantes

### Métricas de producto (analytics)
| Evento / KPI | Descripción | Uso típico |
|--------------|-------------|------------|
| [evento_name] | [Qué mide] | [Cuándo usar] |

### Métricas de negocio
| Métrica | Fuente | Descripción |
|---------|--------|-------------|
| [Métrica] | [Sistema] | [Qué contiene] |

## Contexto técnico

### Experimentos
- **Plataforma:** [GrowthBook / LaunchDarkly / etc.]
- **Naming convention:** `{team}_{feature}_{variant}`

### Feature flags
- **Formato:** `{patron_naming}`
- **Ejemplos:** [ejemplos relevantes]

### Integraciones
- [Sistema 1]: [cómo se integra]
- [Sistema 2]: [cómo se integra]

## Antipatrones comunes del equipo

| Antipatrón | Frecuencia | Ejemplo típico | Cómo corregir |
|------------|------------|----------------|---------------|
| [Antipatrón] | Alta/Media/Baja | "[Ejemplo]" | [Recomendación] |

## Ejemplos de buenas stories del equipo

### Ejemplo 1: {STORY-KEY}
```
[Story completa en formato JTBD]
```
**Por qué es buena:** [Explicación]

## Contexto de negocio

### Objetivos actuales
- [Objetivo 1]
- [Objetivo 2]

### Restricciones conocidas
- [Restricción 1]
- [Restricción 2]

## Fuentes de información

- **Documentación:** [URL espacio del equipo]
- **Comunicación:** [Canales relevantes]
```

---

## Proceso para crear contexto de equipo

1. **Buscar en tu issue tracker** stories recientes del equipo
2. **Identificar usuarios** de stories recientes
   - Extraer roles mencionados en "As a..."
   - Clasificar en primarios/secundarios/riesgo
3. **Buscar documentación** del equipo (wiki, Notion, Confluence)
   - Objetivos / OKRs
   - Métricas clave
   - Contexto técnico
4. **Identificar antipatrones** analizando stories pasadas
   - Patrones que se repiten
   - Errores comunes
5. **Seleccionar ejemplos** de buenas stories como referencia

---

## Mantenimiento

- **Frecuencia:** Revisar trimestralmente o cuando cambien objetivos
- **Trigger:** Actualizar cuando se detecten nuevos usuarios o antipatrones
- **Responsable:** Quien solicite análisis del equipo
