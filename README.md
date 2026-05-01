# Mercadona User Story Toolkit

Pipeline de **definición de producto** para Claude Code: convierte un PRD (o un proyecto GSD) en user stories validadas y priorizadas, listas para que tu equipo de ingeniería las implemente.

> Forjado en producción en [Mercadona Tech](https://www.mercadona.es), generalizado para cualquier equipo. Parte de la serie [Gemba](https://www.gemba.es) sobre desarrollo de productos con agentes.

---

## ¿Qué hace?

Toma un documento de producto (PRD, output de GSD, o nada) y produce **user stories que aprobarías sin reescribir**: con JTBD, criterios de aceptación falsables, scoring de calidad y orden de entrega anti-waterfall.

```
PRD / GSD / vacío
    │
    ▼
[ Quality gate ] → [ Research design ] → [ Análisis ] →
    │
    ▼
[ Stories con JTBD ] → [ Validación ] → [ Splitting ] → [ Priorización ]
    │
    ▼
Stories listas para implementación
```

Cubre el "antes" del código. Para el "durante" del código (implementación), se integra con [Superpowers](https://github.com/...) vía el bridge incluido (`bridge/gsd-bridge.py`).

---

## ¿Para quién?

- **PMs** que quieren stories con criterios falsables, no "user wants better UX"
- **Equipos de producto** que pasaron de Notion + Jira a un flujo asistido por agentes
- **Equipos pequeños** sin PM dedicado que quieren un proceso ligero pero riguroso
- **Equipos que ya usan GSD para planning** y quieren cerrar el bucle hasta stories ejecutables

**No es para ti** si:
- Crees que las stories son una pérdida de tiempo y prefieres especificar todo en código
- Buscas un generador automático que rellene métricas inventadas (esta skill *se niega* a hacerlo)
- Tu producto es un experimento de fin de semana — overkill

---

## Instalación

### Como plugin de Claude Code (recomendado)

```bash
# Clonar
git clone https://github.com/josemerca/mercadona-user-story-toolkit ~/.claude/plugins/mercadona-user-story-toolkit

# Activar en ~/.claude/settings.json
{
  "enabledPlugins": {
    "mercadona-user-story-toolkit": true
  }
}
```

### Bridge GSD↔Superpowers (opcional)

Si usas GSD para planning + Superpowers para ejecución:

```bash
# Copiar el script al PATH
cp bridge/gsd-bridge.py /usr/local/bin/gsd-bridge
chmod +x /usr/local/bin/gsd-bridge

# Hook automático (opcional): añadir bloque a ~/.claude/settings.json
# Ver bridge/sample-hook.json
```

---

## Uso rápido

### Tienes un PRD

```
/prd-quality-guard mi-prd.md     # Quality gate (≥7 → PASS)
/research                         # Diseñar entrevistas Mom Test
# ... realizas las entrevistas ...
/analyze-research                 # Generar JTBDs con evidencia
/stories                          # Convertir JTBDs → user stories
/validate-stories                 # Scoring 6D + antipatrones
/split-stories                    # Splits incrementales si son grandes
/prioritize                       # Batches anti-waterfall
```

### Tienes un proyecto GSD

```
/from-gsd .planning/              # Genera prd-from-gsd.md
# ... completas GAPs marcados ...
/prd-quality-guard prd-from-gsd.md
# ... resto del pipeline igual que arriba ...
```

### No tienes nada

```
/build-story                      # Guía conversacional
/validate-stories
/split-stories
/prioritize
```

---

## Ejemplo end-to-end

Ver [`examples/searchmo-facets/`](examples/searchmo-facets/): walkthrough completo del feature "filtro por facetas en búsqueda" implementado con GSD → toolkit → Superpowers.

---

## Filosofía

**Modo copiloto, no piloto automático.**

Las skills NO inventan datos. Si falta información, te lo dicen y te preguntan. Si tu PRD no tiene métricas, no fabricarán números — el placeholder `[⚠️ Pendiente: definir con PM/Data]` aparece y te recomienda qué tipo de métrica sería útil.

Esto es deliberado. La razón está en [el primer artículo de la serie](https://www.gemba.es/p/el-ai-mercadona-user-story-framework): si la skill rellena por ti, dejas de pensar — y las stories sin pensamiento no soportan ejecución.

---

## Skills incluidas

| Skill | Rol |
|-------|-----|
| `prd-quality-guard` | Quality gate del PRD antes de research |
| `gsd-to-prd` | Mapear artefactos GSD → PRD sintético |
| `research-from-prd` | Gap detection + diseño de entrevistas Mom Test |
| `user-story-builder` | Crear stories desde cero (sin PRD) |
| `jtbd-to-stories` | Generar stories estructuradas desde JTBDs |
| `user-story-quality-coach` | Validar stories con scoring 6D + antipatrones |
| `story-splitting` | Detectar stories grandes y proponer splits |
| `story-prioritization` | Priorización con 5 lentes + grafo de dependencias |

---

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md). Reportes de bugs y PRs son bienvenidos.

---

## Licencia

MIT — ver [LICENSE](LICENSE).

---

## Créditos

Diseñado y mantenido por [José Ramón Pérez Agüera](https://www.linkedin.com/in/joseaguera/), CPTO en [Mercadona Tech](https://www.mercadona.es). Forjado en producción durante 2025-2026; generalizado y open-sourced en mayo 2026.

Inspiración: [Mom Test](http://momtestbook.com/) (Rob Fitzpatrick), [INVEST](https://en.wikipedia.org/wiki/INVEST_(mnemonic)), [Jobs-to-be-Done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) (Christensen et al.), [Get Shit Done](https://github.com/...), [Superpowers](https://github.com/...).
