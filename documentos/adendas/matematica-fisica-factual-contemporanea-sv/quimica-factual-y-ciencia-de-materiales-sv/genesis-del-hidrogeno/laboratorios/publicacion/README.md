# Laboratorio reproducible de la publicación principal

Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026

Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.

Warning. This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

## DOI y depósito canónico

- DOI del laboratorio canónico, versión depositada: `10.5281/zenodo.20058612`.
- DOI del conjunto de versiones del laboratorio canónico: `10.5281/zenodo.20058611`.
- DOI de la publicación principal asociada: `10.17613/qq4q9-sd847`.

Este laboratorio forma parte del fichero canónico `laboratorios.zip`.

| Fichero canónico | Función | SHA-256 |
|---|---|---|
| `laboratorios.zip` | ZIP que contiene este laboratorio y el laboratorio del anexo técnico | `6f34ede5a57714128e67451c9aa031a68c5c6c062de04b14a707035214caf642` |
| `laboratorios.zip.ots` | Sello OpenTimestamps del ZIP de laboratorios | `64474fbd6b7b942ca4a5a4dd92b8fa49c515452bbc6f64f7bd99041a1b7432fe` |
| `laboratorios.zip_signed.csig` | Firma criptográfica del ZIP de laboratorios | `7f179505f5badeed1b0002202c200ae574ff356c02172d0e631016bff7030853` |

## Ejecución

```bash
python runner.py
python runner_bis.py
python runner_publicacion_integral.py
```

## Alcance

El laboratorio verifica de forma reproducible:

1. regeneración formal de los 118 elementos conocidos del dominio periódico;
2. dictamen conservador `U` para candidatos no verificados por encima de Z=118;
3. formación molecular con agua como caso canónico;
4. formación atmosférica con atmósfera terrestre como caso canónico;
5. fallo explícito de una atmósfera no retenida;
6. verificación integrada de publicación y anexo técnico mediante `runner_publicacion_integral.py`.

## Salida esperada

```text
elementos_regenerados: 118/118
banco_demostrativo: 12/12
tests_tabla_bis: 7/7
banco_negativo: 10/10
extension_24: 24/24
extension_48: 48/48
estado: APTO
```
