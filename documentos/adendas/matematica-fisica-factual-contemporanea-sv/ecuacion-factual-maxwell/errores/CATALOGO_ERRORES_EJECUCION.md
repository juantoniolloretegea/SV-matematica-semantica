© 2026. Todos los derechos reservados. 

Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.

Warning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

# Catálogo canónico de errores de ejecución

| Código | Disparo | Significado | Acción correctiva |
|---|---|---|---|
| MAXWELL001 | Desajuste en Gauss eléctrica factual | El flujo factual del desplazamiento no coincide con la carga encerrada | Revisar `gauss_electrica.boundary_D`, `rho` y `volume` |
| MAXWELL002 | Desajuste en Gauss magnética factual | La suma orientada del flujo magnético no es nula | Revisar `gauss_magnetica.boundary_B` |
| MAXWELL003 | Desajuste en Faraday factual | La circulación factual de E no coincide con la variación factual de B | Revisar `faraday.gamma_E`, `dnu_B` y `area` |
| MAXWELL004 | Desajuste en Ampère–Maxwell factual | La circulación factual de H no coincide con la suma de corriente y derivada de D | Revisar `ampere_maxwell.gamma_H`, `J`, `dnu_D` y `area` |
| MAXWELL005 | Desajuste en balance electromagnético factual | La potencia factual disipada no coincide con la identidad Poynting–SV | Revisar `balance` |
| MAXWELL006 | Desajuste en conservación factual de la carga | La suma `∂_ν ρ + Div(J)` no se anula | Revisar `carga` |
| MAXWELL007 | Desajuste en el contorno normal de D | El salto normal de D no coincide con la carga superficial | Revisar `contorno_D` |
| MAXWELL008 | Desajuste en el contorno normal de B | La continuidad normal de B se ha roto | Revisar `contorno_B` |
| MAXWELL009 | Desajuste en el criterio absoluto de frontera | El determinante del jacobiano y el estado de frontera no coinciden | Revisar `frontera.jacobian` y `frontera.frontier_active` |
| MAXWELL010 | Desajuste en el operador exacto de reconfiguración | El valor de `𝓡^f_SV` no coincide con `1_{{det=0}}·Λ·B_reg` | Revisar `reconfiguracion` |
| MAXWELL011 | Desajuste constitutivo factual | Alguna de las tres relaciones constitutivas no se satisface | Revisar `constitutivas` |
| MAXWELL012 | Desajuste metrológico soberano | El cosido dimensional del bloque se ha roto | Revisar `metrologia.dimensions` |
| MAXWELL013 | Desajuste en la forma maestra operatoria | El vector `𝕄_SV` no se anula | Revisar `operatorial` |
| MAXWELL014 | Desajuste en la forma maestra integral | El vector `𝕀_SV` no se anula | Revisar bancos integrales 1–4 |
| MAXWELL015 | Desajuste en la ecuación única factual | No se anulan simultáneamente `𝕄_SV`, `𝕂_SV` y `𝔽_SV` | Revisar bancos 11–20 |
| MAXWELL016 | Desajuste en el contorno tangencial de E | La continuidad tangencial de E se ha roto | Revisar `contorno_E` |
| MAXWELL017 | Desajuste en el contorno tangencial de H | El salto tangencial de H no coincide con `J_s` | Revisar `contorno_H` |
| MAXWELL018 | Desajuste en la identidad de onda factual | La identidad `Rot∘Rot(E) + εμ∂²_νE = 0` no se cumple | Revisar `onda` |
| MAXWELL900 | Archivo de datos no encontrado | Falta un JSON obligatorio | Restaurar la ruta del archivo |
| MAXWELL901 | JSON inválido | El archivo de datos no se puede parsear | Corregir sintaxis JSON |
| MAXWELL920 | Número incorrecto de bancos | El runner no produjo los bancos positivos exigidos | Revisar implementación del módulo |
| MAXWELL921 | Falla positiva no detectada | Existe un banco positivo fallido | Revisar el banco concreto y su salida |
| MAXWELL922 | Ataque negativo no detectado | Un caso negativo pasó, se omitió o devolvió código incorrecto | Revisar mutación y control de error |
| MAXWELL930 | Estructura de datos incompleta | Falta una sección obligatoria del laboratorio | Restaurar la clave ausente |
| MAXWELL931 | Tipo de dato inválido | Un valor esperado como número o dimensión no tiene el tipo correcto | Corregir el dato afectado |
| MAXWELL932 | Vector incompatible | Un vector o secuencia no tiene la longitud requerida | Corregir cardinalidad y orden |
| MAXWELL933 | Matriz incompatible | La matriz del jacobiano no es 3x3 | Restaurar la forma canónica 3x3 |
| MAXWELL934 | Booleano inválido | El estado de frontera no es booleano | Corregir `frontier_active` |
| MAXWELL935 | Mutación negativa inválida | Un ataque negativo referencia una ruta inexistente o mal formada | Corregir la ruta de mutación |
