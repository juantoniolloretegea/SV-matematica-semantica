# Laboratorios — Elementos químicos del Sistema Vectorial SV (SV-443)

[![Tabla periódica estructural SV — análisis preliminar de elementos químicos, materiales y aleaciones de nueva generación (k=119–443, índices SV 1–325)](imagenes/Tabla%20periodica.svg)](imagenes/Tabla%20periodica.svg)

---

**DOI laboratorio:** [10.5281/zenodo.20084771](https://doi.org/10.5281/zenodo.20084771) — Zenodo  
**DOI publicación:** [10.17613/8ryyb-g9h48](https://doi.org/10.17613/8ryyb-g9h48) — Humanities Commons (HCOMMONS)

**Integridad criptográfica:**  
| Archivo | Tipo | Descripción |
|---|---|---|
| `laboratorios.zip.csig` | Firma criptográfica | Autoría e integridad del laboratorio |
| `laboratorios.zip.ots` | Sellado de tiempo | OpenTimestamps — blockchain |
| `Preliminary_Analysis_[...].pdf.ots` | Sellado de tiempo | OpenTimestamps sobre la publicación |

---



© 2026. Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | ISSN 2695-6411 | CC BY-NC-ND 4.0 | Madrid, 08/05/2026

---

## Estructura

```
laboratorios/
├── runner.py                 ← ejecutar: python3 runner.py
├── CATALOGO-DE-ERRORES.md    ← catálogo exhaustivo de códigos de error
├── README.md                 ← este archivo
├── resultados/               ← resultados de ejecución (auto-generados)
│   └── .gitkeep
└── src/
    └── sv_443.py             ← módulo de verificación
```

## Ejecución

```bash
cd laboratorios
python3 runner.py
```

El CSV se busca en `../../elementos_sv_443.csv`. Para pasar una ruta distinta:

```bash
python3 runner.py /ruta/a/elementos_sv_443.csv
```

## Resultado esperado (APTO)

```json
{
  "elementos_esperados": 443,
  "columnas_esperadas": 33,
  "errores_totales": 0,
  "errores_formula": 0,
  "errores_rango": 0,
  "errores_texto": 0,
  "errores_otros": 0,
  "elementos_verificados": "443/443",
  "estado": "APTO"
}
```

## Política de errores

Ningún error pasa silenciosamente. Cada comprobación tiene su código específico (SV-443-*). En caso de fallo, el campo `detalle_errores` lista absolutamente todos los errores encontrados, con código, elemento afectado y valor observado frente al esperado. El catálogo completo está en `CATALOGO-DE-ERRORES.md`.
