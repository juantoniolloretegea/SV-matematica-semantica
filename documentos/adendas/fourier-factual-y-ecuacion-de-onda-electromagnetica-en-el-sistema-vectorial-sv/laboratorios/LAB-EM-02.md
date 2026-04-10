# LAB-EM-02 — Desarrollo cíclico factual y transformada modal electromagnética

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Lugar y fecha:** Madrid, 10/04/2026

---

**Fichero:** `laboratorios/LAB-EM-02.md`
**JSON congelado:** `laboratorios/json_congelados/lab-em-02.json`
**Runner de referencia:** `laboratorios/runners/runner_maestro_emf.py`
**Caso director:** ED-EM-01
**Dictamen local:** APTO
**Fecha de ejecución:** 2026-04-10T20:17:40Z

## Transformada modal factual

Media factual: `0.111111111111`.
α: `[0.170232098471, 0.038588483926, -0.111111111111, -0.208820582397]`.
β: `[0.142841691041, 0.218846167336, 0.19245008973, 0.076004476295]`.
Módulos: `[0.222222222222, 0.222222222222, 0.222222222222, 0.222222222222]`.

## Reconstrucciones truncadas

- `K_0`: `[0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111, 0.111111111111]`
- `K_1`: `[0.281343209582, 0.333333333333, 0.281343209582, 0.149699595037, 0.0, -0.097709471286, -0.097709471286, 0.0, 0.149699595037]`
- `K_2`: `[0.319931693508, 0.555555555556, 0.319931693508, -0.05912098736, -0.111111111111, 0.072522627185, 0.072522627185, -0.111111111111, -0.05912098736]`
- `K_3`: `[0.208820582397, 0.777777777778, 0.208820582397, -0.170232098471, 0.111111111111, -0.038588483926, -0.038588483926, 0.111111111111, -0.170232098471]`
- `K_4`: `[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`

## Criterios de paso

- Error máximo K=4: `0.0` (tolerancia: `1e-12`) → `True`.
- Todos los valores finitos: `True`.
- Residuos cuadráticos decrecientes con K: `True`.
- Dictamen: `True`.

## Custodia

Fichero: `laboratorios/json_congelados/lab-em-02.json`
Huella MD5 autosellada: `5c8d171047bfaa996d08f7726b9cce0c`.

> Protocolo de verificación: eliminar el campo `md5` del JSON, serializar con
> `json.dumps(d, ensure_ascii=False, indent=2)` y calcular `md5(texto.encode('utf-8'))`.
> El resultado debe coincidir con el valor del campo `md5`.
