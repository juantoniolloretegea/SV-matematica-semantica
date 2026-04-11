# Entorno local

Este entorno permite reejecutar el núcleo analítico, los casos por dominio y los laboratorios incluidos en el conjunto.

## Componentes

- `runner/`
- `core/`
- `labs/`
- `datasets/`
- `tests/`
- `schemas/`
- `scripts/`
- `examples/`

## Relación con el conjunto

El entorno local se coordina con:

- la [publicación científica](../publicacion/publicacion.html),
- los [dominios del Sistema Vectorial SV](../dominios/index.html),
- la [guía práctica del investigador](../guia/guia-practica.html),
- la [implementación local en web](../implementacion/implementacion-local.html),
- y el [plan de verificación](../tests/plan-verificacion.html).

## Regla principal

La web permite una exploración inmediata. El entorno local repite el análisis con datasets, laboratorios y ejecución por lotes.

## Contrato de entrada

Se admiten dos formatos JSON:

1. objeto directo con `states`, `transforms` y `horizon`;
2. sobre exportado desde la web con claves `input` y `result`.

En la validación del contrato JSON, `horizon.domain` es obligatorio. El runner tipa errores de entrada con `FFSV-001`, `FFSV-002`, `FFSV-004`, `FFSV-005` y `FFSV-006`.

Los archivos `*_casos.json` contienen listas de casos. Los archivos `*_minimo.json` y `examples/ejemplo_manual.json` contienen un único caso.

## Uso mínimo

```bash
python runner/sv_runner.py
python scripts/run_all_examples.py
pytest
```

## Ejecución verificada

Este entorno puede ejecutarse directamente desde `runner/`, `scripts/`, `labs/` y `tests/` sin instalación adicional, porque cada punto de entrada resuelve de forma explícita la raíz de `entorno_local/`.
