# LAB-EM-05 — Ecuación factual de onda electromagnética

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Lugar y fecha:** Madrid, 10/04/2026

---

**Fichero:** `laboratorios/LAB-EM-05.md`
**JSON congelado:** `laboratorios/json_congelados/lab-em-05.json`
**Runner de referencia:** `laboratorios/runners/runner_maestro_emf.py`
**Caso director:** ED-EM-01
**Dictamen local:** APTO
**Fecha de ejecución:** 2026-04-10T20:17:40Z

## Condición inicial canónica

Velocidad factual inicial nula: `da_m/dξ|_{ξ=0} = 0`.
Impuesta mediante arranque frío: `a_m(−Δξ) := a_m(0)`.

## Parámetros de propagación

| Parámetro | Valor | Unidad |
|---|---|---|
| Δξ | `0.5` | UE_MFC |
| Δℓ | `1.0` | UFE |
| c_SV | `1.0` | UFE·UE_MFC⁻¹ |
| Courant_max | `0.984807753012` | — (< 2.0 → ESTABLE) |

λ_m = `[-0.467911113762, -1.652703644666, -3.0, -3.879385241572]`
Ω_m² = `[0.467911113762, 1.652703644666, 3.0, 3.879385241572]`

## Nota sobre el contenido cuadrático

El contenido cuadrático `∑X_i²` **no es** la cantidad conservada del esquema leapfrog.
Su variación entre pasos es esperada y no indica inestabilidad.
La cantidad conservada es la energía escalonada discreta del esquema.

## Estados propagados

### Paso 0

- ξ = `0.0` UE_MFC
- estado = `[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
- contenido cuadrático = `1.0`
- máximo en posición (1-indexada) = `2`
- valor máximo = `1.0`

### Paso 1

- ξ = `0.5` UE_MFC
- estado = `[0.25, 0.5, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
- contenido cuadrático = `0.375`
- máximo en posición (1-indexada) = `2`
- valor máximo = `0.5`

### Paso 2

- ξ = `1.0` UE_MFC
- estado = `[0.5, -0.125, 0.5, 0.0625, 0.0, 0.0, 0.0, 0.0, 0.0625]`
- contenido cuadrático = `0.5234375`
- máximo en posición (1-indexada) = `1`
- valor máximo = `0.5`

### Paso 3

- ξ = `1.5` UE_MFC
- estado = `[0.484375, -0.4375, 0.484375, 0.21875, 0.015625, 0.0, 0.0, 0.015625, 0.21875]`
- contenido cuadrático = `0.7568359375`
- máximo en posición (1-indexada) = `1`
- valor máximo = `0.484375`

### Paso 4

- ξ = `2.0` UE_MFC
- estado = `[0.171875, -0.2890625, 0.171875, 0.390625, 0.078125, 0.00390625, 0.00390625, 0.078125, 0.390625]`
- contenido cuadrático = `0.460052490234`
- máximo en posición (1-indexada) = `4`
- valor máximo = `0.390625`

### Paso 5

- ξ = `2.5` UE_MFC
- estado = `[-0.201171875, 0.08984375, -0.201171875, 0.4296875, 0.2001953125, 0.0263671875, 0.0263671875, 0.2001953125, 0.4296875]`
- contenido cuadrático = `0.539821624756`
- máximo en posición (1-indexada) = `9`
- valor máximo = `0.4296875`

### Paso 6

- ξ = `3.0` UE_MFC
- estado = `[-0.34375, 0.3232421875, -0.34375, 0.253662109375, 0.336181640625, 0.09228515625, 0.09228515625, 0.336181640625, 0.253662109375]`
- contenido cuadrático = `0.71257185936`
- máximo en posición (1-indexada) = `5`
- valor máximo = `0.336181640625`

## Criterios de paso

- Número de Courant estable (< 2.0): `True`.
- Todos los valores finitos: `True`.
- Contenido cuadrático acotado y no negativo en todos los pasos: `True`.
- Dictamen: `True`.

## Custodia

Fichero: `laboratorios/json_congelados/lab-em-05.json`
Huella MD5 autosellada: `f2265946c538805805d6cf6bbcf1d48b`.

> Protocolo de verificación: eliminar el campo `md5` del JSON, serializar con
> `json.dumps(d, ensure_ascii=False, indent=2)` y calcular `md5(texto.encode('utf-8'))`.
> El resultado debe coincidir con el valor del campo `md5`.
