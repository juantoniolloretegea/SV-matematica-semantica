# Laboratorios locales

Este directorio contiene los laboratorios locales mínimos del bloque y su correspondencia con:

- páginas HTML en `../../laboratorios/`,
- datasets en `../datasets/`,
- tests en `../tests/`,
- y ejecución mediante `../runner/sv_runner.py`.

## Correspondencia básica

- `metrologia_lab.py` ↔ `../../laboratorios/metrologia.html` ↔ `datasets/metrologia_minimo.json`
- `electromagnetismo_lab.py` ↔ `../../laboratorios/electromagnetismo.html` ↔ `datasets/electromagnetismo_minimo.json`
- `multidetector_lab.py` ↔ `../../laboratorios/multidetector.html` ↔ `datasets/multidetector_minimo.json`
- `particulas_lab.py` ↔ `../../laboratorios/particulas.html` ↔ `datasets/particulas_minimo.json`
- `no_clausura_lab.py` ↔ `../../laboratorios/no-clausura.html` ↔ `datasets/no_clausura_minimo.json`

## Criterio de lectura

Cada laboratorio debe poder:
1. cargar un dataset real del dominio,
2. ejecutar `run_sv_analysis(...)`,
3. comparar el dictamen esperado con el obtenido,
4. y conservar una traza suficiente del caso ejecutado.

## Referencias complementarias

- [Plan de verificación](../../tests/plan-verificacion.html)
- [Implementación local](../../implementacion/implementacion-local.html)
- [Dominios del SV](../../dominios/index.html)
