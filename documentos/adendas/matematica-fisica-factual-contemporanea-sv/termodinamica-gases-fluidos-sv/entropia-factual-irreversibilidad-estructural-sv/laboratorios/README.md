# Laboratorios canónicos de entropía factual e irreversibilidad estructural en el Sistema Vectorial SV

© 2026. Todos los derechos reservados. Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)  
IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411  
Licencia CC BY-NC-ND 4.0 | Madrid, 23/04/2026

## Publicación principal

**Factual entropy and structural irreversibility in the Sistema Vectorial SV: pre-ternary dispersion, transport law along the foundational chain and asymmetric conservation of factual content**

DOI Commons/KCWorks de la publicación principal:  
https://doi.org/10.17613/vh6ak-6em43

Colección canónica:  
https://doi.org/10.17613/r4dwa-d9b30

Fuente material canónica en GitHub:  
https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/termodinamica-gases-fluidos-sv/entropia-factual-irreversibilidad-estructural-sv

## Objeto del paquete

Este paquete conserva los laboratorios reproducibles asociados a la publicación sobre entropía factual e irreversibilidad estructural en el Sistema Vectorial SV. Los laboratorios implementan, en forma ejecutable, el cálculo de la dispersión preternaria, el transporte por la cadena fundacional, la monotonía de la entropía factual, la violación retroactiva simulada y tres ejemplos canónicos de dictamen.

## Estructura

| Elemento | Descripción |
|---|---|
| `sv_core.py` | Primitivas compartidas de dispersión preternaria, transporte estratificado y entropía factual SV. |
| `lab_04_4_verificacion_preternaria.py` | Verificación numérica de H_pre sobre tres posiciones. |
| `lab_11_recorrido_consistencia.py` | Recorrido de consistencia sobre SV(3,9). |
| `lab_11_10_violacion_simulada.py` | Contraste adversarial de reescritura retroactiva. |
| `lab_ejemplo_A_cierre_determinado.py` | Ejemplo A: cierre determinado. |
| `lab_ejemplo_B_residual_en_U.py` | Ejemplo B: residual en U. |
| `lab_ejemplo_C_clase_emergente.py` | Ejemplo C: clase emergente. |
| `tests/test_monotonia.py` | Suite de trece tests de monotonía y consistencia. |
| `run_all.py` | Ejecutor reproducible principal. |
| `runner.py` | Ejecutor equivalente para uso directo. |
| `CATALOGO_ERRORES.md` | Catálogo doctrinal de grietas detectadas y corregidas. |
| `catalogo_errores.json` | Catálogo JSON derivado para trazabilidad computacional. |
| `MANIFEST.json` | Manifiesto material del paquete. |
| `SHA256SUMS.txt` | Huellas SHA-256 de todos los archivos. |
| `EXECUTION_REPORT.txt` | Informe breve de ejecución. |
| `EXECUTION_LOG_FULL.txt` | Registro completo de ejecución. |
| `CITATION.cff` | Metadatos de citación. |
| `ZENODO_UPLOAD_FIELDS.md` | Campos recomendados para depósito Zenodo. |

## Cómo reproducir

Desde esta carpeta:

```bash
python run_all.py
```

o bien:

```bash
python runner.py
```

## Resultado verificado

- Laboratorios visibles superados: 6/6.
- Tests de monotonía superados: 13/13.
- Verificaciones operativas totales: 19/19.
- Sintaxis Python verificada.
- Sin dependencias externas; sólo biblioteca estándar Python 3.8+.
- Paquete sin `__pycache__` ni bytecode.

## Depósito reproducible preservado

Los laboratorios de esta carpeta están preservados en Zenodo como suplemento computacional reproducible de la publicación principal.

DOI de versión:
https://doi.org/10.5281/zenodo.19897700

DOI conceptual de todas las versiones:
https://doi.org/10.5281/zenodo.19897699

Registro Zenodo:
https://zenodo.org/records/19897700

## Licencia

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).
