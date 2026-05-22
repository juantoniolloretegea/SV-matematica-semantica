# Laboratorios — Campo, energía, masa, gravedad, G y Λ

![Portada de Campo y energía, génesis de la masa y definición física de la gravedad](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/imagenes/portada.png)

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)  
**Institución:** [Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ — ITVIA](https://www.itvia.online/)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** [2695-6411](https://portal.issn.org/resource/ISSN/2695-6411)  
**Licencia:** [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)  
**Fecha:** Madrid, 22/05/2026  
**Carpeta canónica:** [SV-matematica-semantica/.../laboratorios](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios)  
**DOI de la publicación:** [10.21428/39829d0b.41afec0f](https://doi.org/10.21428/39829d0b.41afec0f)  
**Adscrita a la colección:** [10.21428/39829d0b.26484bfd](https://doi.org/10.21428/39829d0b.26484bfd)  
**URL canónica de publicación:** [IA eñ™ — release/1](https://www.itvia.online/pub/campo-y-energia-genesis-de-la-masa-y-definicion-fisica-de-la-gravedad-gravitacion-universal-constante-cosmologica-y-dominio-observable/release/1)  
**Preservación independiente (Internet Archive):** [snapshot de la carpeta 2026-05-22 20:47:11 UTC](https://web.archive.org/web/20260522204711/https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad)

## Cómo citar

Lloret Egea, J. A. (2026). *Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable*. IA eñ™ — La Biblia de la IA™. ISSN 2695-6411. DOI: [10.21428/39829d0b.41afec0f](https://doi.org/10.21428/39829d0b.41afec0f). Colección DOI: [10.21428/39829d0b.26484bfd](https://doi.org/10.21428/39829d0b.26484bfd).

Estos laboratorios verifican los bancos inyectados en el apartado XIV de la publicación. No crean doctrina ni sustituyen la argumentación física: comprueban entradas, unidades, operaciones, retornos, residuales y dictámenes. El paquete conserva la separación entre G y Λ, impide la conversión de `Λ_obs[B]` en magnitud constitutiva, y exige que `Λ_SV,ret[B]` opere como tupla auditada con banco, unidad, incertidumbre, residual y dictamen.

## Ejecución

Requisito: Python 3.8 o superior, sin dependencias externas.

```text
python runner.py
```

El runner ejecuta todos los laboratorios, escribe `salida_obtenida.txt` y comprueba su coincidencia exacta con `salida_esperada.txt`. Cualquier discrepancia, salida no tabulada, negativo aceptado, banco incompleto o excepción produce fallo.

## Ficheros principales

| Fichero | Función |
|---|---|
| [`runner.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/runner.py) | Ejecuta todos los laboratorios y bloquea el pase silencioso. |
| [`sv_lab_core.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/sv_lab_core.py) | Núcleo común de constantes, cálculos, bancos, dictámenes y verificaciones. |
| [`salida_esperada.txt`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/salida_esperada.txt) | Salida textual que debe reproducirse. |
| [`salida_obtenida.txt`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/salida_obtenida.txt) | Salida generada por la ejecución material. |
| [`catalogo_errores.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/catalogo_errores.csv) | Códigos de error por dominio, distancia, G, Λ, masa, campo, estadística, tiempo, banco y pase silencioso. |
| [`MANIFIESTO_SHA256.txt`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/MANIFIESTO_SHA256.txt) | Manifiesto de integridad SHA-256 del paquete de laboratorios. |

## Bancos de datos

| Fichero | Función |
|---|---|
| [`datos/constantes.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/constantes.csv) | Constantes y magnitudes de entrada: c, G, T<sub>obs</sub>, Mpc, bancos cosmológicos y magnitudes astronómicas. |
| [`datos/banco_positivo.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/banco_positivo.csv) | Casos positivos y de absorción parcial. |
| [`datos/banco_negativo.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/banco_negativo.csv) | Casos negativos que deben ser rechazados. |
| [`datos/banco_transduccion.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/banco_transduccion.csv) | Transducciones ciencia contemporánea ↔ Sistema Vectorial SV, con unidad, residual y retorno. |
| [`datos/bancos_observacionales_lambda.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/bancos_observacionales_lambda.csv) | Bancos observacionales de Λ, incluido `B_Planck18-baseΛCDM`, `B_Planck18+BAO` y `B_DESI-DR2`. |
| [`datos/banco_lambda_adversarial.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos/banco_lambda_adversarial.csv) | Casos adversariales específicos de Λ, banco B, `Λ_obs[B]` y `Λ_SV,ret[B]`. |

## Laboratorios

| ID | Fichero | Comprobación |
|---|---|---|
| LAB-01 | [`LAB-01_campo_energia.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-01_campo_energia.py) | Campo y energía se articulan por dominio; rechazo de sinonimia universal. |
| LAB-02 | [`LAB-02_masa_frontera.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-02_masa_frontera.py) | La masa exige frontera, residual, retorno y traza. |
| LAB-03 | [`LAB-03_hidrogeno_persistencia.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-03_hidrogeno_persistencia.py) | Hidrógeno como caso canónico conocido, no mínimo universal. |
| LAB-04 | [`LAB-04_campo_gravitatorio.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-04_campo_gravitatorio.py) | Campo gravitatorio con fuente, dominio, acción y retorno. |
| LAB-05 | [`LAB-05_atraccion_local.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-05_atraccion_local.py) | Cálculo local Tierra–Luna y Sol–Tierra. |
| LAB-06 | [`LAB-06_distancias_tipadas.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-06_distancias_tipadas.py) | Separación entre r local, D<sub>L</sub>, D<sub>A</sub>, D<sub>M</sub> y distancia factual. |
| LAB-07 | [`LAB-07_constante_G.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-07_constante_G.py) | G como coeficiente metrológico de retorno local. |
| LAB-08 | [`LAB-08_lambda_puro.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-08_lambda_puro.py) | `Λ_SV,puro = 3/(c²T_obs²)`. |
| LAB-09 | [`LAB-09_lambda_retorno_banco_declarado.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-09_lambda_retorno_banco_declarado.py) | `Λ_obs[B]` y `Λ_SV,ret[B]` sólo con banco, unidad, incertidumbre, residual y dictamen. |
| LAB-10 | [`LAB-10_separacion_G_Lambda.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-10_separacion_G_Lambda.py) | Separación dimensional y física entre G y Λ. |
| LAB-11 | [`LAB-11_vacio_lambda.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-11_vacio_lambda.py) | Rechazo de proyección directa vacío desnudo → Λ física. |
| LAB-12 | [`LAB-12_energia_oscura_dinamica.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-12_energia_oscura_dinamica.py) | Tensión observacional sin cierre mecanístico final. |
| LAB-13 | [`LAB-13_transduccion_bidireccional.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-13_transduccion_bidireccional.py) | Ida y vuelta ciencia contemporánea ↔ SV con unidad y residual. |
| LAB-14 | [`LAB-14_matriz_absorcion.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-14_matriz_absorcion.py) | Dictamen por uso y dominio, no por nombre. |
| LAB-15 | [`LAB-15_banco_negativo_integral.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-15_banco_negativo_integral.py) | Rechazo de todos los negativos críticos. |
| LAB-16 | [`LAB-16_salida_global.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/LAB-16_salida_global.py) | Coincidencia entre salida esperada y salida obtenida. |

## Política de cierre

Un resultado sólo es APTO si todos los positivos retornan unidad correcta, todos los negativos son detectados, todas las transducciones conservan dominio o rechazo explícito, y la salida obtenida coincide con la salida esperada. La incertidumbre experimental no se confunde con error de plano: el fallo se activa por dominio mal declarado, unidad incompatible, banco ausente, residual oculto, retorno incompleto o pase silencioso.

© 2026 Juan Antonio Lloret Egea. Licencia CC BY-NC-ND 4.0.
