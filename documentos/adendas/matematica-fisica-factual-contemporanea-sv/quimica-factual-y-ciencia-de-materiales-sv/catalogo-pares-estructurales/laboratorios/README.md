# Laboratorios — Catálogo de Pares Estructurales SV (CPS-SV)

**Publicación:** Catálogo de Pares Estructurales SV (CPS-SV)  
**Autor:** Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351  
**ISSN:** 2695-6411 | CC BY-NC-ND 4.0

## Estructura

```
laboratorios/
├── datos/
│   ├── tabla_global_sv443.csv   — Tabla Global SV: 443 elementos, 9 columnas (entrada)
│   └── catalogo_pares_sv443.csv — CPS-SV completo: 97.903 pares (salida)
├── descargar-laboratorios/      — ZIP firmado y estampillado (pendiente)
├── resultados/
│   └── verificacion_cps_sv.json — Resultado de verificación (APTO, 0 errores)
├── src/
│   └── sv_cps.py                — Módulo Python: función D(A,B), carga, invariantes
├── CATALOGO-DE-ERRORES.md
├── README.md                    — Este archivo
└── runner.py                    — Runner maestro: genera y verifica el CPS-SV
```

## Ejecución

```bash
python3 runner.py
python3 runner.py --tabla2 datos/tabla_global_sv443.csv --salida datos/catalogo_pares_sv443.csv
```

**Requisitos:** Python 3.8+, biblioteca estándar exclusivamente. Sin dependencias externas.

## Resultado canónico (09/05/2026)

```
Estado:        APTO
APTO-M:        9.515
APTO-C:       37.580
APTO-I:        5.075
NO-APTO:      45.733
APTO total:   52.170
Pares totales: 97.903
Errores:           0
```

## Advertencia

Datos estructurales SV. No son mediciones empíricas. Uso comercial prohibido sin autorización. CEDRO.
