© 2026. Todos los derechos reservados.

Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.

Warning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

# Resultado del runner maestro del bloque electromagnético factual

- Bancos positivos superados: 21/21
- Casos negativos detectados correctamente: 15/15

## Bancos positivos

| Banco | Descripción | Observado | Esperado | Dictamen |
|---|---|---|---|---|
| BANCO_01 | Gauss eléctrica factual (forma integral) | `0.05000000000000002` | `0.05` | Pasa |
| BANCO_02 | Gauss magnética factual (forma integral) | `0.0` | `0.0` | Pasa |
| BANCO_03 | Faraday factual (forma integral) | `0.27` | `0.27` | Pasa |
| BANCO_04 | Ampère–Maxwell factual (forma integral) | `0.39` | `0.39` | Pasa |
| BANCO_05 | Balance electromagnético factual | `0.2` | `0.2` | Pasa |
| BANCO_06 | Conservación factual de la carga | `0.0` | `0.0` | Pasa |
| BANCO_07 | Condición de contorno: componente normal de D | `0.0` | `0.0` | Pasa |
| BANCO_08 | Condición de contorno: componente normal de B | `0.0` | `0.0` | Pasa |
| BANCO_09 | Condición de contorno: componente tangencial de E | `[0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0]` | Pasa |
| BANCO_10 | Condición de contorno: componente tangencial de H | `[0.0, -0.040000000000000036, 0.0]` | `[0.0, -0.04, 0.0]` | Pasa |
| BANCO_11 | Criterio absoluto de frontera factual: determinante del jacobiano | `0.0` | `0.0` | Pasa |
| BANCO_12 | Criterio absoluto de frontera factual: activación de frontera | `True` | `True` | Pasa |
| BANCO_13 | Operador exacto de reconfiguración factual | `0.09999999999999999` | `0.1` | Pasa |
| BANCO_14 | Relación constitutiva eléctrica factual | `3.0` | `3.0` | Pasa |
| BANCO_15 | Relación constitutiva magnética factual | `0.4` | `0.4` | Pasa |
| BANCO_16 | Relación constitutiva de conducción factual | `2.0999999999999996` | `2.1` | Pasa |
| BANCO_17 | Forma maestra operatoria factual | `[0.0, 0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0, 0.0]` | Pasa |
| BANCO_18 | Forma maestra integral factual | `[1.3877787807814457e-17, 0.0, 0.0, 0.0]` | `[0.0, 0.0, 0.0, 0.0]` | Pasa |
| BANCO_19 | Ecuación única factual electromagnética | `{'M': True, 'K': True, 'F': True}` | `{'M': True, 'K': True, 'F': True}` | Pasa |
| BANCO_20 | Cosido dimensional soberano | `{'gauss_electrica': True, 'faraday': True, 'ampere_maxwell': True, 'balance': True, 'onda': True}` | `{'gauss_electrica': True, 'faraday': True, 'ampere_maxwell': True, 'balance': True, 'onda': True}` | Pasa |
| BANCO_21 | Identidad de onda factual | `0.0` | `0.0` | Pasa |

## Casos negativos

| Caso | Error esperado | Error observado | Dictamen |
|---|---|---|---|
| NEG_GAUSS_ELECTRICA | `MAXWELL001` | `MAXWELL001` | Pasa |
| NEG_GAUSS_MAGNETICA | `MAXWELL002` | `MAXWELL002` | Pasa |
| NEG_FARADAY | `MAXWELL003` | `MAXWELL003` | Pasa |
| NEG_AMPERE | `MAXWELL004` | `MAXWELL004` | Pasa |
| NEG_BALANCE | `MAXWELL005` | `MAXWELL005` | Pasa |
| NEG_CARGA | `MAXWELL006` | `MAXWELL006` | Pasa |
| NEG_CONTORNO_D | `MAXWELL007` | `MAXWELL007` | Pasa |
| NEG_CONTORNO_B | `MAXWELL008` | `MAXWELL008` | Pasa |
| NEG_CONTORNO_E | `MAXWELL016` | `MAXWELL016` | Pasa |
| NEG_CONTORNO_H | `MAXWELL017` | `MAXWELL017` | Pasa |
| NEG_FRONTERA | `MAXWELL009` | `MAXWELL009` | Pasa |
| NEG_RECONFIGURACION | `MAXWELL010` | `MAXWELL010` | Pasa |
| NEG_CONSTITUTIVA | `MAXWELL011` | `MAXWELL011` | Pasa |
| NEG_METROLOGIA | `MAXWELL012` | `MAXWELL012` | Pasa |
| NEG_ONDA | `MAXWELL018` | `MAXWELL018` | Pasa |
