# gsd-bridge

CLI standalone que mantiene consistencia entre los artefactos de [GSD (Get Shit Done)](https://github.com/...) — `.planning/PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `phases/N/SPEC.md` — y el trabajo ejecutado por [Superpowers](https://github.com/...) (o cualquier otro flujo de implementación).

## Por qué existe

Cuando GSD planea pero Superpowers ejecuta, los artefactos de GSD no se actualizan automáticamente. Resultado: `STATE.md` desactualizado, `ROADMAP.md` muestra la fase como "Not started" cuando en realidad está hecha, y `VERIFICATION.md` nunca se genera. El bridge cierra ese gap.

## Instalación

Sin dependencias externas (solo Python 3.9+):

```bash
# Opción 1: copiar al PATH
cp gsd-bridge.py /usr/local/bin/gsd-bridge
chmod +x /usr/local/bin/gsd-bridge

# Opción 2: alias
alias gsd-bridge="python3 /ruta/a/gsd-bridge.py"
```

## Uso

### Auto-sync desde git

Lee el último `last-sync-sha` de `STATE.md`, examina los commits desde ahí, extrae los REQ-IDs mencionados (formato `[A-Z]{2,8}-\d{1,4}`, p. ej. `AUTH-01`, `FOUND-12`) y los marca como done en los `PLAN.md` correspondientes.

```bash
gsd-bridge sync
gsd-bridge sync --planning ./mi-proyecto/.planning/
gsd-bridge sync --dry-run    # ve qué pasaría sin escribir nada
gsd-bridge sync --quiet      # silencia output (útil en hooks)
```

Si todos los REQ-IDs de una fase están done, la fase se cierra automáticamente:
- `ROADMAP.md` → checkbox marcado, tabla de progreso actualizada
- `phases/N/VERIFICATION.md` → se genera con la lista completa de REQs
- `STATE.md` → se anexa el sync con timestamp y SHA

### Marcar manualmente

Si los commits no referencian REQ-IDs (caso típico cuando el ejecutor olvidó incluirlos), puedes marcarlos a mano:

```bash
gsd-bridge mark-done AUTH-01 AUTH-02 PROF-03
```

### Registrar amendments

Cuando la implementación divergió del `SPEC.md` original (decisiones tomadas durante el desarrollo que cambiaron el diseño), regístralo en `SPEC-AMENDMENTS.md` en lugar de reescribir `SPEC.md` (preserva el trail):

```bash
gsd-bridge amend "El endpoint /config se renombró a /settings por consistencia con el resto de la API"
gsd-bridge amend "Se descartó WebSocket por complejidad — fallback a polling cada 5s" --phase 2
```

### Status

Muestra divergencia entre la realidad de los commits y el estado de los artefactos:

```bash
gsd-bridge status
```

Salida ejemplo:

```
GSD Bridge Status — 2026-05-01 12:34

Last sync sha:    e05994b5...
Current sha:      8f2a91e7...
Commits pending:  3
REQs in pending commits: AUTH-04, PROF-01

Phases:
  01-foundation: 4/4 done
  02-profiles: 1/4 done
  03-features: 0/3 done
```

## Integración con Claude Code (hook automático)

Para que Claude Code ejecute `gsd-bridge sync` automáticamente al final de cada conversación, añade este hook a tu `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "test -d $(pwd)/.planning && python3 /ruta/a/gsd-bridge.py sync --quiet || true",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

El hook es no-op si no hay `.planning/` en el directorio (con `test -d ... && ... || true`).

## Convenciones

### Formato de REQ-ID

El bridge busca el patrón `[A-Z]{2,8}-\d{1,4}` en commits y PLAN.md. Convención GSD estándar:

- 2-8 letras mayúsculas que identifican la categoría
- Guion
- 1-4 dígitos

Ejemplos válidos: `AUTH-01`, `PROF-12`, `CHECKOUT-3`, `SR-9`
Ejemplos no válidos: `auth-01` (minúsculas), `A-01` (1 letra), `AUTH-12345` (5 dígitos)

### Mensajes de commit

Para que el sync detecte completitud automáticamente, incluye el REQ-ID en el commit:

```
✓ feat: implement AUTH-01 user signup
✓ fix: resolve PROF-03 avatar upload bug
✗ feat: add login        # sin REQ-ID, no se detecta
```

Si olvidas el REQ-ID, usa `mark-done` después.

### Estructura de fases

El bridge espera fases en `.planning/phases/NN-name/` (ej. `01-foundation/`, `02-profiles/`). Cada fase puede tener uno o varios `*PLAN.md`.

## Limitaciones conocidas

1. **No detecta tests pasando, solo presencia de REQ-ID en commit.** Para verificación real de aceptación, ejecutar tests manualmente o usar la skill `verification-before-completion` de Superpowers antes de cerrar fase.

2. **No mergea ramas.** Si trabajas en feature branch sin mergear a main, los commits no aparecen en `HEAD` hasta merge.

3. **No sabe distinguir reverts.** Un commit que reverta `AUTH-01` lo seguiría marcando como done.

4. **No traduce locale.** Si tu PLAN.md está en inglés, se actualiza en inglés; idem español.

5. **Asume que el REQ-ID en el commit corresponde al PLAN.md activo.** Si tienes el mismo REQ-ID en múltiples PLAN.md (no recomendado), todos se marcan.

## Filosofía

- **Read-mostly** sobre `.planning/`: solo escribe en `STATE.md`, `PLAN.md`, `ROADMAP.md`, `VERIFICATION.md` y `SPEC-AMENDMENTS.md`.
- **Nunca reescribe `SPEC.md`** — preserva el trail con `SPEC-AMENDMENTS.md`.
- **Idempotente:** ejecutar dos veces no duplica entradas.
- **Honesto:** si no puede determinar el estado, lo reporta como "unknown" en lugar de adivinar.

## Licencia

MIT.
