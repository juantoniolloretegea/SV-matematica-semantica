# Elementos químicos del Sistema Vectorial SV

[![Portada — Tabla periódica estructural SV (elementos k=119–443, índices SV 1–325)](imagenes/portada_elementos_sv_443.svg)](imagenes/portada_elementos_sv_443.svg)

---

**DOI publicación:** [10.17613/8ryyb-g9h48](https://doi.org/10.17613/8ryyb-g9h48) — Humanities Commons (HCOMMONS)  
**DOI laboratorio:** [10.5281/zenodo.20084771](https://doi.org/10.5281/zenodo.20084771) — Zenodo

**Integridad criptográfica:**  
| Archivo | Tipo | Descripción |
|---|---|---|
| `Preliminary_Analysis_[...].pdf` | Publicación | Documento firmado digitalmente |
| `Preliminary_Analysis_[...].pdf.ots` | Sellado de tiempo | OpenTimestamps — blockchain |
| `laboratorios.zip` | Laboratorio | Archivo verificable reproducible |
| `laboratorios.zip.csig` | Firma criptográfica | Autoría e integridad del laboratorio |
| `laboratorios.zip.ots` | Sellado de tiempo | OpenTimestamps — blockchain |

---



© 2026. Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0 | Madrid, 08/05/2026

---

Catálogo completo de los 443 elementos químicos del Sistema Vectorial SV: familias tipológicas, generación prequímica, criterios de transición y propiedades estructurales.

## Estructura

```
elementos-materiales-nueva-generacion/
├── elementos-materiales-nueva-generacion.md   ← publicación principal
├── PDF/                                        ← versión PDF (próximamente)
├── imagenes/                                   ← figuras de la publicación
├── laboratorios/                               ← verificación reproducible
│   ├── runner.py
│   ├── src/sv_443.py
│   ├── CATALOGO-DE-ERRORES.md
│   └── resultados/
└── README.md                                   ← este archivo
```

## Ejecución del laboratorio

```bash
cd laboratorios
python3 runner.py
```

Resultado esperado: `443/443 elementos, estado APTO`.
