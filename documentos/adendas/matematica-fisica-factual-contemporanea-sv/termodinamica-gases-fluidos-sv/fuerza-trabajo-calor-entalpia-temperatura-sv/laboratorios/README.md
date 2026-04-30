# Laboratorios canónicos de termodinámica factual SV

© 2026. Todos los derechos reservados. Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)  
IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411  
Licencia CC BY-NC-ND 4.0 | Madrid, 30/04/2026

## Publicación principal

**Force, Work, Heat, Enthalpy, Temperature, Principles and Foundations of Thermodynamics, and the Correlation Among Them in the SV**

Título español de referencia:  
**Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV**

DOI de la publicación principal:  
https://doi.org/10.17613/ptw68-d1r57

DOI de la colección canónica:  
https://doi.org/10.17613/r4dwa-d9b30

## Depósito reproducible preservado

Los laboratorios de esta carpeta están preservados en Zenodo como suplemento computacional reproducible de la publicación principal.

DOI de versión:  
https://doi.org/10.5281/zenodo.19900023

DOI conceptual de todas las versiones:  
https://doi.org/10.5281/zenodo.19900022

Registro Zenodo:  
https://zenodo.org/records/19900023

## Objeto del paquete

Este paquete conserva los laboratorios reproducibles asociados al dominio termodinámico factual del Sistema Vectorial SV. Los laboratorios verifican, en forma ejecutable, la fórmula factual única absoluta del dominio termodinámico y sus proyecciones sobre fuerza, trabajo, calor, entalpía y temperatura.

El conjunto ejecuta doce laboratorios Python autocontenidos, con catálogo de errores explícito, tres casos canónicos en `datos/casos_canonicos.json`, runner maestro, verificación de unicidad de códigos y política de no admisión de pases silenciosos.

## Estructura

| Elemento | Descripción |
|---|---|
| `datos/casos_canonicos.json` | Tres casos canónicos: A simétrico SV(3,4), B asimétrico SV(3,5), C heterogéneo SV(3,6). |
| `sv_core.py` | Núcleo operatorio del dominio termodinámico factual. |
| `lab_01_balance_canonico.py` | Balance canónico. |
| `lab_02_irreversibilidad.py` | Irreversibilidad factual. |
| `lab_03_tres_formas_cruzadas.py` | Equivalencia de tres formas algebraicas. |
| `lab_04_vector_director.py` | Vector director y ortogonalidad. |
| `lab_05_identidad_termometrica.py` | Identidad termométrica. |
| `lab_06_absorcion_limite_clasica.py` | Absorción del límite clásico. |
| `lab_07_fuerza_helmholtz_factual.py` | Fuerza canónica y descomposición tipo Helmholtz factual. |
| `lab_08_unicidad_generador.py` | Unicidad del generador. |
| `lab_09_exhaustividad_tres_clases.py` | Exhaustividad de las tres clases estructurales. |
| `lab_10_consistencia_dimensional.py` | Consistencia dimensional. |
| `lab_11_celula_canonica_sv3_9.py` | Célula canónica SV(3,9). |
| `lab_12_adversarial_rivales.py` | Exclusividad frente a seis clases de rivales. |
| `catalogo_errores.json` | Catálogo de códigos de error únicos. |
| `runner_config.json` | Orden declarado de ejecución. |
| `runner.py` | Ejecutor maestro. |
| `run_all.py` | Ejecutor complementario directo. |
| `MANIFEST.json` | Manifiesto material del paquete. |
| `SHA256SUMS.txt` | Huellas SHA-256 de los archivos. |
| `EXECUTION_REPORT.txt` | Informe breve de ejecución. |
| `EXECUTION_LOG_FULL.txt` | Registro completo de ejecución. |
| `CITATION.cff` | Metadatos de citación. |

## Cómo reproducir

Desde esta carpeta:

```bash
python runner.py
```

o bien:

```bash
python run_all.py
```

## Resultado verificado

Estado del paquete:

- Laboratorios superados: 12/12.
- Sintaxis Python verificada.
- JSON validados.
- Catálogo de errores: 120 códigos únicos.
- Orden de `runner_config.json` compatible con los archivos `lab_*.py`.
- Paquete sin `__pycache__` ni bytecode.

## Dependencias

```text
numpy
```

## Licencia

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).
