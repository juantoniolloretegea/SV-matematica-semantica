# Catálogo de errores de ejecución — EMF

## Familia EMF

- **EMF-001** — Trayectoria factual no compatible.
- **EMF-002** — Observable sin homogeneidad dimensional.
- **EMF-003** — Parámetro material no declarado.
- **EMF-004** — Transformada modal factual no invertible en ejecución.
- **EMF-005** — Balance factual modal inconsistente.
- **EMF-006** — Residual de borde factual fuera de régimen esperado.
- **EMF-007** — Propagación factual no estable bajo el runner.
- **EMF-008** — Excepción no controlada en laboratorio.
- **EMF-009** — Salida JSON no congelada o huella ausente.
- **EMF-010** — Dictamen local ausente o estado inválido.

## Régimen de no tolerancia

El runner maestro opera en régimen **fail-fast**. Si aparece cualquiera de las familias anteriores o si un laboratorio devuelve `passed = false`, la suite se interrumpe y el dictamen global pasa a `NO_APTO`.
