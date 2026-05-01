# Contributing

Gracias por considerar contribuir a Mercadona User Story Toolkit. Este es un proyecto en evolución y la mejor versión sale de uso real en equipos diversos.

## Antes de abrir un PR

1. **Abre un issue primero.** Para bugs reproducibles puedes ir directo a PR. Para cambios de comportamiento o nuevas skills, discute primero — evitamos PRs grandes que no se mergean.

2. **Mantén la filosofía copiloto.** Las skills NO deben inventar datos. Si tu cambio hace que una skill genere métricas, JTBDs o criterios sin evidencia explícita del usuario, no se mergea.

3. **No acoples a herramientas externas.** El toolkit es agnóstico de Notion/Jira/Linear. Si necesitas integración con una herramienta concreta, ponla por fuera (configuración del usuario, MCP, etc.) — no dentro de las skills.

## Cambios bienvenidos

- **Bugs en el flujo** del pipeline o las skills
- **Mejoras en heurísticas** de splitting/priorización con justificación clara
- **Nuevas reglas anti-waterfall** con caso de uso real
- **Soporte para nuevos formatos de PRD** (manteniendo compatibilidad con el actual)
- **Bridges adicionales** (a otras herramientas de planning más allá de GSD)
- **Ejemplos end-to-end** de equipos reales (con permiso)
- **Traducciones** de las skills a otros idiomas

## Cambios que probablemente rechacemos

- Acoplar a una herramienta concreta (Jira, Notion, Linear) en el código de las skills
- Añadir generación autónoma sin checkpoints (la skill decide sin preguntar)
- Plantillas que rellenan datos inventados como placeholder "razonable"
- Cambios que rompen compatibilidad con el contrato actual de skills sin migración

## Estructura del repo

```
.
├── .claude-plugin/        # Manifesto del plugin
├── commands/              # Slash commands del toolkit
├── skills/                # Skills (lógica + references)
│   ├── <skill>/SKILL.md
│   └── <skill>/references/
├── bridge/                # gsd-bridge.py (CLI standalone)
├── examples/              # Walkthroughs end-to-end
├── shared-config.md       # Config compartida por skills
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Tests

Los smoke tests del bridge están en `bridge/tests/` (próximamente). Para skills, validar manualmente con un PRD real antes de PR.

## Comunicación

- Issues: bugs y propuestas
- Discussions: dudas, casos de uso, retroalimentación

Mantenedor: [@josemerca](https://github.com/josemerca) — José Ramón Pérez Agüera
