# Reporte del laboratorio mínimo

Este reporte se genera a partir de `lab_minimo_olfato.py` y ofrece una verificación mínima de consistencia interna del esquema propuesto.

## Resultados

| Caso | Salida del modelo |
|---|---|
| Caso 1. Café recién servido, sin ingestión | admisibilidad olfativa suficiente |
| Caso 2. Sabor a vainilla durante ingestión de crema | admisibilidad olfativa con U |
| Caso 3. Caramelo mentolado | admisibilidad olfativa con U |
| Caso 4. Solución de tastant con componente volátil | admisibilidad olfativa con U |
| Caso 5. Olor ambiental en cocina con humo y picor ocular | admisibilidad olfativa suficiente |

## Regla de prudencia aplicada

Ante mezcla no separable, vía indeterminada o coactivación relevante en contexto no limpio, el modelo conserva `U` antes que cierre fuerte.
