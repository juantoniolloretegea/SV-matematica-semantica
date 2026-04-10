# LAB-EM-01 — Modos cíclicos factuales del campo electromagnético

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Lugar y fecha:** Madrid, 10/04/2026

---

**Fichero:** `laboratorios/LAB-EM-01.md`
**JSON congelado:** `laboratorios/json_congelados/lab-em-01.json`
**Runner de referencia:** `laboratorios/runners/runner_maestro_emf.py`
**Caso director:** ED-EM-01
**Dictamen local:** APTO
**Fecha de ejecución:** 2026-04-10T20:17:40Z

## Entrada factual

Estado inicial: `[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`.

## Salida modal

Media factual: `0.111111111111`.
Coeficientes α: `[0.170232098471, 0.038588483926, -0.111111111111, -0.208820582397]`.
Coeficientes β: `[0.142841691041, 0.218846167336, 0.19245008973, 0.076004476295]`.
Módulos M: `[0.222222222222, 0.222222222222, 0.222222222222, 0.222222222222]`.
Reconstrucción exacta (K=4): `[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`.
Error máximo de reconstrucción: `0.0`.
Tolerancia: `1e-12`.

## Criterio de paso

`error_maximo_reconstruccion < tolerancia` → `True`.

## Custodia

Fichero: `laboratorios/json_congelados/lab-em-01.json`
Huella MD5 autosellada: `fcd9a75c27ab0ba9f58aa81e90b956fd`.

> Protocolo de verificación: eliminar el campo `md5` del JSON, serializar con
> `json.dumps(d, ensure_ascii=False, indent=2)` y calcular `md5(texto.encode('utf-8'))`.
> El resultado debe coincidir con el valor del campo `md5`.
