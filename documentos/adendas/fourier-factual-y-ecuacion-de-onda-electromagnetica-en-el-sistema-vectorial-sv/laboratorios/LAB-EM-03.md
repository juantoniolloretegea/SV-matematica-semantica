# LAB-EM-03 — Balance factual modal

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Lugar y fecha:** Madrid, 10/04/2026

---

**Fichero:** `laboratorios/LAB-EM-03.md`
**JSON congelado:** `laboratorios/json_congelados/lab-em-03.json`
**Runner de referencia:** `laboratorios/runners/runner_maestro_emf.py`
**Caso director:** ED-EM-01
**Dictamen local:** APTO
**Fecha de ejecución:** 2026-04-10T20:17:40Z

## Verificación del balance factual modal

Contenido cuadrático factual Q[X]: `1.0`.
Lado derecho del balance (fórmula Parseval): `1.0`.
Diferencia absoluta: `0.0`.
Tolerancia: `1e-12`.

## Criterio de paso

`|Q[X] - RHS| < tolerancia` → `True`.

## Custodia

Fichero: `laboratorios/json_congelados/lab-em-03.json`
Huella MD5 autosellada: `6300fbb99e0cd526e69da42480a700a1`.

> Protocolo de verificación: eliminar el campo `md5` del JSON, serializar con
> `json.dumps(d, ensure_ascii=False, indent=2)` y calcular `md5(texto.encode('utf-8'))`.
> El resultado debe coincidir con el valor del campo `md5`.
