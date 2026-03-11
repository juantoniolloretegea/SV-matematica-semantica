# Especificaciones formales del Sistema Vectorial SV

**Estado:** Estructura reservada — contenido pendiente de migración

---

## Función en el repositorio

Este directorio albergará las especificaciones formales verificables del Sistema Vectorial SV: definiciones que puedan validarse automáticamente, contratos de datos y suites de conformidad cruzada.

## Estructura prevista

```
especificaciones/
├── nucleo/          ← Definiciones formales: célula, umbral T(n), convención semántica
├── conformidad/     ← Tests de conformidad cruzada entre implementaciones (C8)
└── esquemas/        ← Contratos YAML/JSON Schema para estructuras de datos SV
```

## Relación con SVperitus-dataset

La carpeta `especificaciones/` existe actualmente en el repositorio SVperitus-dataset. El contenido migrará progresivamente a este repositorio como hogar canónico, manteniendo presencia en SVperitus como espejo o puntero según proceda.

## Nota de honestidad

Esta carpeta existe para reservar la estructura correcta desde el nacimiento del repositorio. No contiene todavía artefactos verificables. No se presenta como material consolidado.

---

*ISSN 2695-6411 · CC BY-NC-ND 4.0*
