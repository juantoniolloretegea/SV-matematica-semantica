# Primitivos metrológicos del Sistema Vectorial SV

Este directorio es la **unidad canónica** del paquete metrológico del SV para GitHub y PubPub.

## Ruta canónica

- Ruta relativa: `documentos/adendas/primitivos-metrologicos-sv`
- URL canónica GitHub: <https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/primitivos-metrologicos-sv>
- Colección PubPub: <https://www.itvia.online/nueva-matematica--y-fisica-factual-del-sv>

## Contenido

- `primitivos-metrologicos-sv.md`: documento principal para GitHub.
- `primitivos-metrologicos-sv_pubpub.md`: copia nominal equivalente para PubPub.
- `laboratorios/`: 7 laboratorios auditables.
- `runners/`: runner maestro y runner rápido.
- `core/`: soporte común.
- `web/`: conversor HTML/JavaScript.
- `ERRORES.md`: historial de errores detectados y corregidos.
- `CATALOGO_ERRORES_EJECUCION.md`: catálogo operativo de códigos de salida.
- `reporte_laboratorios_primitivos_metrologicos_sv.json`: informe de ejecución.

## Ejecución local

```bash
python runners/runner_maestro.py
python runners/runner_rapido.py
```
