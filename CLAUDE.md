# CLAUDE.md

Instrucciones para trabajar con este repositorio. Este toolkit es un **plugin de Claude Code** (skills + slash commands en Markdown + scripts Python auxiliares). No es código de aplicación; es contenido prompt-engineered con el que se cargan agentes.

## Estructura

```
.claude-plugin/plugin.json   # Manifesto del plugin (incluye `version`)
commands/                    # Slash commands (.md)
skills/<skill>/SKILL.md      # Skills + references/
bridge/                      # gsd-bridge.py (CLI standalone) + tests
scripts/                     # Scripts auxiliares de las skills
shared-config.md             # Config compartida
examples/                    # Walkthroughs end-to-end
```

## Versionado y releases

El versionado sigue **SemVer** sobre el campo `version` de `.claude-plugin/plugin.json`. Los tags `vX.Y.Z` y las GitHub Releases los crea automáticamente la CI (`.github/workflows/release.yml`) cuando detecta un cambio en `plugin.json` al mergear a `main`.

**Regla obligatoria:** cualquier cambio que se mergee a `main` debe ir acompañado de un bump de `version` en `.claude-plugin/plugin.json`. Si no se bumpea, no hay release.

### Cómo decidir el bump

Aplicar SemVer al **contrato del plugin** (lo que un usuario invoca o consume), no al código interno:

- **PATCH** (`x.y.Z`) — corrección sin cambio de comportamiento observable:
  - Typos, mejoras de redacción en SKILL.md o commands/
  - Bug fixes en scripts/ o bridge/ que dejan los mismos inputs/outputs
  - Refactor interno de un script
  - Documentación (`README.md`, `CONTRIBUTING.md`, `examples/`)

- **MINOR** (`x.Y.0`) — funcionalidad aditiva, retrocompatible:
  - Nueva skill o nuevo command
  - Nuevo flag opcional en un command existente
  - Nueva heurística aditiva en una skill (no cambia las existentes)
  - Nuevo bridge / nuevo formato de PRD soportado
  - Nuevo script en `scripts/` invocado por skills

- **MAJOR** (`X.0.0`) — cambio incompatible para usuarios existentes:
  - Renombrar o eliminar una skill o un command
  - Cambiar inputs/outputs requeridos de una skill (rompe pipelines existentes)
  - Cambios estructurales en `plugin.json` o `shared-config.md` que requieran migración
  - Eliminar un flag, hacer obligatorio un flag antes opcional
  - Cambio de comportamiento por defecto que altere outputs en escenarios existentes

Ante la duda entre dos niveles, sube al más alto. Las MAJOR se justifican en el cuerpo del PR con la nota de migración.

### Instrucción al agente (bump automático)

Cuando implementes cualquier cambio en este repo, **bumpea tú mismo** `.claude-plugin/plugin.json` → `version` antes de cerrar el PR. No esperes a que el usuario lo pida. Procedimiento:

1. Lee la `version` actual de `.claude-plugin/plugin.json`.
2. Clasifica el cambio aplicado contra los criterios PATCH/MINOR/MAJOR de arriba. Si el PR contiene varios cambios de distinto nivel, gana el más alto.
3. Calcula la nueva versión:
   - PATCH → `x.y.Z+1`
   - MINOR → `x.Y+1.0`
   - MAJOR → `X+1.0.0`
4. Edita `.claude-plugin/plugin.json` con la nueva versión.
5. Inclúyelo en el mismo commit / PR que el cambio funcional. En la descripción del PR indica explícitamente: tipo de bump (PATCH/MINOR/MAJOR), versión anterior → nueva, y la justificación de una línea contra los criterios.
6. Si el cambio es **solo documentación fuera del contrato del plugin** (`README.md`, `CONTRIBUTING.md`, este `CLAUDE.md`, `.github/`, `examples/` sin alterar comandos), **no bumpees** — no hay release que publicar.

Antes de cerrar, comprueba que `plugin.json` está en el commit. Si falta, el PR no genera release.

### Flujo de release

1. Implementar el cambio en una rama.
2. Bumpear `.claude-plugin/plugin.json` → `version` según el criterio de arriba (mismo PR que el cambio).
3. Mergear a `main`.
4. La CI (`ubuntu-latest`):
   - Lee `version` de `plugin.json`.
   - Si el tag `v<version>` no existe, lo crea y publica una GitHub Release con notas auto-generadas desde los commits.
   - Si ya existe, no hace nada (idempotente — útil si el merge no tocó la versión por accidente).
5. La CI también es disparable manualmente vía `workflow_dispatch` con la versión actual del manifest.

**No crear tags `vX.Y.Z` a mano.** Los gestiona la CI.

## Convenciones técnicas

- **Skills/commands son contenido, no código.** Antes de añadir lógica, considerar si encaja como heurística en una skill existente.
- **Sin acoplamiento a herramientas externas** (Jira, Notion, Linear) en skills. Las integraciones viven fuera del plugin (MCP, scripts del usuario).
- **Sin generación inventada.** Las skills no rellenan métricas, JTBDs ni criterios sin evidencia explícita del usuario. Esto es invariante del producto, no preferencia estética.
- **Scripts deterministas en Python.** Cálculos repetibles (scoring, splitting) viven en `scripts/` y `bridge/`, no embebidos en prompts.

## Tests

- `bridge/tests/` — smoke tests del CLI standalone.
- Skills/commands se validan manualmente con un PRD real antes de PR. No hay test runner automático para los prompts.
