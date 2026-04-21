© 2026. Todos los derechos reservados. 

Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026 | Advertencia: Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y supeditado estrictamente al licenciamiento permitido.

Warning: This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author’s copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

# Ecuación factual Maxwell — infraestructura laboratorial reforzada

Ruta relativa canónica de destino:

`documentos/adendas/matematica-fisica-factual-contemporanea-sv/ecuacion-factual-maxwell`

Este conjunto aporta la infraestructura laboratorial autocontenida del documento **Reducción estructural absoluta de Maxwell en el Sistema Vectorial SV y ecuación única de la física factual electromagnética**. Su función es reejecutar, con trazabilidad, sin pases silenciosos y con falsación obligatoria, el recorrido visible de consistencia reforzado del bloque electromagnético factual sobre la célula SV(3,9), los bancos metrológicos, la ecuación única y los ataques negativos canónicos.

## Contenido

- `laboratorios/datos/caso_control_svtresnueve.json`: caso positivo de control con veintiún bancos de verificación.
- `laboratorios/datos/casos_negativos.json`: quince ataques negativos obligatorios con sus códigos de error esperados.
- `laboratorios/modulo/verificador_maxwell_sv.py`: núcleo de verificación, validación estructural y escritura de resultados.
- `runners/runner_maestro.py`: reejecución completa de bancos positivos y ataques negativos.
- `runners/runner_rapido.py`: comprobación resumida del núcleo crítico del laboratorio.
- `errores/CATALOGO_ERRORES_EJECUCION.md`: catálogo canónico de errores de ejecución.
- `errores/catalogo_errores_ejecucion.csv`: versión tabular del catálogo.
- `errores/ERRORES.md`: historial local de incidencias detectadas y corregidas.
- `tests/PLAN_VERIFICACION.md`: contrato material de verificación.
- `laboratorios/resultados/`: salidas reproducibles generadas por los runners.

## Criterio de dictamen

El conjunto sólo se considera **APTO** si concurren simultáneamente estas condiciones:

1. se verifican exactamente los veintiún bancos positivos exigidos;
2. todos los bancos positivos pasan sin discrepancia numérica, vectorial ni dimensional;
3. los quince ataques negativos fallan de la forma esperada y quedan detectados por su código canónico;
4. ningún runner produce pase silencioso, omisión de banco, mutación no aplicada o sustitución tácita de un fallo por aproximación no declarada.
