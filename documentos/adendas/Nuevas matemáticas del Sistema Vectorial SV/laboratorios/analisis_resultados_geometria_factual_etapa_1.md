# Análisis de resultados del laboratorio geométrico factual — Etapa 1

## Alcance

Este análisis acompaña a `lab_03_geometrico.py` y a `salida_geometrico.json`.
Su función es dejar trazabilidad legible de los cinco casos mínimos G1–G5.

## Casos mínimos verificados

- **G1** — dos unidades con frontera interna cancelable.
- **G2** — tres unidades con orientación mixta.
- **G3** — frontera total insuficiente.
- **G4** — campo factual insuficiente.
- **G5** — ciclo factual mínimo.

## Lectura técnica

El caso G1 verifica cancelación interna y balance estructural.
El caso G2 verifica agregación de divergencias sobre orientación mixta.
El caso G3 preserva la frontera explícita como condición de legitimidad.
El caso G4 preserva la no ejecución favorable ante campo factual insuficiente.
El caso G5 verifica circulación factual mínima sin degradación de U.

## Dictamen

El laboratorio geométrico se considera **APTO** como soporte mínimo reproducible del bloque geométrico factual.
