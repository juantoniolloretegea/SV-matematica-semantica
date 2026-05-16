# Laboratorios reproducibles — Proyecciones biológicas de la fibra

![Portada — Proyecciones biológicas de la fibra](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/imagenes/portada.png?raw=1)
**© 2026. Todos los derechos reservados.** Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 16/05/2026.

## Estatuto

Este directorio materializa los bancos y laboratorios declarados en la publicación. La ejecución es local, determinista, sin internet, sin aprendizaje, sin probabilidad y sin inferencia opaca. El paquete no diagnostica pacientes reales, no sustituye el acto médico y no formula recomendaciones terapéuticas.

## Estructura

| Ruta | Función |
|---|---|
| [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/runner.py) | ejecución global de 11 bancos, 54 laboratorios y 48 errores |
| [runner_diagnostico.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/runner_diagnostico.py) | ejecución del lote clínico-biológico semilla |
| [src/io_utils.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/src/io_utils.py) | lectura y escritura CSV/JSON |
| [src/validators.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/src/validators.py) | validadores de bancos, errores, U y salida |
| [datos/registro_bancos.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/datos/registro_bancos.csv) | inventario de bancos B01–B11 |
| [datos/catalogo_laboratorios.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/datos/catalogo_laboratorios.csv) | inventario de LAB-01–LAB-54 |
| [datos/catalogo_errores.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/datos/catalogo_errores.csv) | catálogo E-01–E-48 |
| [datos/clinico_biologico](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/datos/clinico_biologico) | tablas canónicas del Anexo I |
| [salidas](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas) | salidas obtenidas y manifiesto |

## Ejecución

```bash
python runner.py
python runner_diagnostico.py
```

## Salidas esperadas

| Salida | Condición |
|---|---|
| PASS global | 11/11 bancos, 54/54 laboratorios, 48/48 errores detectados |
| U conservada | toda entrada diseñada como U permanece U |
| 0 pases silenciosos | todo fallo debe quedar tipado |
| PASS diagnóstico | 6 casos, 16 negativos, 4 refutaciones con error cero acotado y 2 U legítimos |

## Ficheros de salida

| Fichero | Función |
|---|---|
| [salidas/laboratorios_obtenidos.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/laboratorios_obtenidos.csv) | salida de cada laboratorio |
| [salidas/errores_detectados.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/errores_detectados.csv) | detección de E-01–E-48 |
| [salidas/salida_obtenida_global.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/salida_obtenida_global.csv) | SG-01–SG-04 |
| [salidas/resumen_global.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/resumen_global.csv) | resumen material del lote |
| [salidas/salida_obtenida_diagnostico.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/salida_obtenida_diagnostico.csv) | salida de los casos clínico-biológicos |
| [salidas/resumen_diagnostico.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/resumen_diagnostico.csv) | resumen del lote clínico-biológico |
| [salidas/manifiesto_sha256.txt](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/biologia-molecular-y-medicina/proyecciones-biologicas-de-la-fibra/laboratorios/salidas/manifiesto_sha256.txt) | hashes de los ficheros de laboratorio |
