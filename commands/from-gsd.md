---
name: from-gsd
description: "Genera un PRD sintético a partir de los artefactos de GSD (.planning/) listo para entrar al pipeline MUST"
argument-hint: "[ruta a .planning/, default: ./.planning/]"
---

Ejecuta `/from-gsd` para transformar los artefactos de un proyecto GSD (Get Shit Done) en un PRD sintético compatible con `/prd-quality-guard`. El PRD resultante puede entrar al pipeline en la fase de research → stories.

**Input necesario:** Ruta al directorio `.planning/` de un proyecto GSD. Default: `./.planning/` (directorio actual).

**Proceso:**
1. Validar que existen los artefactos requeridos: `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`
2. Leer también (si existen): `phases/*/SPEC.md`, `phases/*/RESEARCH.md`, `STATE.md`
3. Cargar el SKILL.md de `skills/gsd-to-prd/`
4. Aplicar la matriz de mapeo GSD → PRD (referencia: `mapping-table.md`)
5. Generar fichero `prd-from-gsd.md` en la raíz del proyecto
6. Marcar explícitamente las secciones que GSD no cubre (gaps)
7. Reportar resumen: secciones rellenas + gaps a completar

**Output:** Fichero `prd-from-gsd.md` listo para `/prd-quality-guard`.

**Importante:**
- El PRD generado es **sintético**: refleja lo que GSD captura, NO sustituye discovery
- Si GSD ya tiene `RESEARCH.md` por fase, se referencia como evidencia previa para `/research`
- El comando NO modifica los ficheros GSD — solo lee
- El comando NO inventa datos: secciones sin equivalente en GSD se marcan como `⚠️ GAP`

**Siguiente paso:** `/prd-quality-guard prd-from-gsd.md` → si PASS → `/research source_type=PRD`
