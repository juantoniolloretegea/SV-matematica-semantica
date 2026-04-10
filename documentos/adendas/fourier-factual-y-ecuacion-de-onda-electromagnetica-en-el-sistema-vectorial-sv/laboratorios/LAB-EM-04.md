# LAB-EM-04 — Residual de borde factual

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Lugar y fecha:** Madrid, 10/04/2026

---

**Fichero:** `laboratorios/LAB-EM-04.md`
**JSON congelado:** `laboratorios/json_congelados/lab-em-04.json`
**Runner de referencia:** `laboratorios/runners/runner_maestro_emf.py`
**Caso director:** ED-EM-01
**Dictamen local:** APTO
**Fecha de ejecución:** 2026-04-10T20:17:40Z

## Conjunto de borde

Posiciones (1-indexadas): `[1, 2, 3]`.

## Indicadores de truncación y borde

### K_0

- borde máximo: `0.888888888889`
- borde cuadrático: `0.814814814815`
- residuo total cuadrático: `0.888888888889`
- concentración de borde: `0.916666666667`
- sobreoscilación: `0.0`
- suboscilación: `0.0`
- reconstrucción truncada: `[0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111]`

### K_1

- borde máximo: `0.666666666667`
- borde cuadrático: `0.6027524476`
- residuo total cuadrático: `0.666666666667`
- concentración de borde: `0.9041286714`
- sobreoscilación: `0.0`
- suboscilación: `0.0`
- reconstrucción truncada: `[0.281343209582, 0.333333333333, 0.281343209582, 0.149699595037, 0.0, -0.097709471286, -0.097709471286, 0.0, 0.149699595037]`

### K_2

- borde máximo: `0.444444444444`
- borde cuadrático: `0.402243441219`
- residuo total cuadrático: `0.444444444444`
- concentración de borde: `0.905047742743`
- sobreoscilación: `0.0`
- suboscilación: `0.0`
- reconstrucción truncada: `[0.319931693508, 0.555555555556, 0.319931693508, -0.05912098736, -0.111111111111, 0.072522627185, 0.072522627185, -0.111111111111, -0.05912098736]`

### K_3

- borde máximo: `0.222222222222`
- borde cuadrático: `0.136594787315`
- residuo total cuadrático: `0.222222222222`
- concentración de borde: `0.614676542915`
- sobreoscilación: `0.0`
- suboscilación: `0.0`
- reconstrucción truncada: `[0.208820582397, 0.777777777778, 0.208820582397, -0.170232098471, 0.111111111111, -0.038588483926, -0.038588483926, 0.111111111111, -0.170232098471]`

## Criterios de paso

- Todos los valores finitos: `True`.
- Borde máximo decreciente con K: `True`.
- Concentraciones en [0, 1]: `True`.
- Dictamen: `True`.

## Custodia

Fichero: `laboratorios/json_congelados/lab-em-04.json`
Huella MD5 autosellada: `e1045b501a9a03e6ddd1bf8ed27718f0`.

> Protocolo de verificación: eliminar el campo `md5` del JSON, serializar con
> `json.dumps(d, ensure_ascii=False, indent=2)` y calcular `md5(texto.encode('utf-8'))`.
> El resultado debe coincidir con el valor del campo `md5`.
