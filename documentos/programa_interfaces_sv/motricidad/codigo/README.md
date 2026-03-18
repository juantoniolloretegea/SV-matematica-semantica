# Código del carril de motricidad del Sistema Vectorial SV

Este directorio contiene el evaluador mínimo y el dataset de casos del carril de motricidad.

## Contenido

- `evaluador.py`  
  Implementación en Python del predicado de habilitación estructural `H` sobre grafos finitos dirigidos.

- `datos.json`  
  Dataset de casos formales, incluyendo los cuatro ejemplos del artículo.

## Uso

Desde este directorio:

```bash
python3 evaluador.py
```

No requiere dependencias externas.

## Resultado esperado

La salida del evaluador debe ser:

```text
T1 no_habilitable
T2 no_habilitable
T3 no_habilitable
T4 habilitable
```

## Criterio

Este bloque acompaña al paper y verifica parcialmente sus ejemplos formales. No constituye una teoría de acción ni un modelo de ejecución física.
