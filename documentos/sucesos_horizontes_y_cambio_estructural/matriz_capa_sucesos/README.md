# Matriz de extracción y contraste — capa de sucesos

Este módulo no constituye una gramática ni una extensión del Lenguaje SV.
Su función es doble:

1. extraer de los documentos VII.x necesidades estructurales reales;
2. formular dichas necesidades de forma controlada para su contraste posterior con el Lenguaje SV.

La matriz madre recoge únicamente lo que está explícita o implícitamente exigido por los documentos.
La matriz espejo está destinada a responder, desde el Lenguaje SV, si dichas necesidades:

- están cubiertas;
- están cubiertas parcialmente;
- requieren vigilancia;
- o no proceden todavía.

Este módulo no autoriza por sí mismo cambios en:

- gramática,
- IR,
- validator,
- runner,
- o backend.

Toda traslación a implementación deberá someterse a validación formal independiente.

## Nota de gobierno de lectura

La matriz espejo no debe leerse como inventario genérico de carencias del Lenguaje SV, sino como instrumento de contraste disciplinado entre:

- necesidades estructurales nacidas de la familia VII; y
- el estado materialmente constatado del Lenguaje SV a la fecha.

Por ello:

- `NO_CUBIERTO` no equivale automáticamente a backlog técnico;
- `NO_PROCEDE_AUN` designa reserva doctrinal, no simple pendiente de implementación;
- y `SOLO_VIGILANCIA` obliga a evitar endurecimientos prematuros del Lenguaje SV.

## Estado actual de esta capa

<<<<<<< HEAD
A esta fecha, esta matriz debe leerse después de la integración material de **VII.4** y antes de la apertura formal del frente específico de **células especializadas del Sistema Vectorial SV** y del siguiente ciclo fuerte de contraste con el Lenguaje SV.

Su función inmediata no es forzar traducciones implementativas automáticas, sino conservar trazabilidad sobre tres planos distintos:

1. lo ya absorbido doctrinalmente por la familia VII hasta VII.4;
2. lo ya contrastado de forma preliminar con el Lenguaje SV;
3. y lo que todavía deberá reexaminarse cuando se abra el siguiente tramo doctrinal relativo a células especializadas.
=======
A esta fecha, esta matriz debe leerse **después de la integración material de VII.3** y **antes de la delimitación fuerte de VII.4**.

Su función inmediata no es forzar traducciones implementativas automáticas, sino conservar trazabilidad sobre tres planos distintos:

1. lo ya absorbido doctrinalmente por la familia VII;
2. lo ya contrastado de forma preliminar con el Lenguaje SV;
3. y lo que todavía deberá reexaminarse cuando se abra el siguiente tramo doctrinal.
>>>>>>> 4160509cf588eb39a2d62774d505f233c8d42f12

Por tanto, esta capa sigue siendo un instrumento de vigilancia, contraste y preparación, no un mandato autónomo de cierre técnico.
