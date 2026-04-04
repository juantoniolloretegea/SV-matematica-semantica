# Matriz de extracción y contraste — capa de sucesos

**Fecha y Versión: V.1 del conjunto**  
**Fecha:** 4 de abril de 2026  
**Versión del conjunto:** V.1 del conjunto  
**Autor del corpus:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA — IA eñ™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Titularidad y autoría:** © Juan Antonio Lloret Egea, 2026. Este conjunto se distribuye con atribución explícita de autoría y bajo la licencia indicada, sin autorización para apropiación de la paternidad intelectual del Sistema Vectorial SV.  

---


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

A esta fecha, esta matriz debe leerse después de la integración material de **VII.6** y antes del siguiente ciclo fuerte de consolidación de interfaces pendientes, de la publicación específica de **células especializadas del Sistema Vectorial SV** y de cualquier intento de cierre prematuro del backend.

Su función inmediata no es forzar traducciones implementativas automáticas, sino conservar trazabilidad sobre cuatro planos distintos:

1. lo ya absorbido doctrinalmente por la familia VII hasta VII.6;
2. lo ya contrastado de forma preliminar con el Lenguaje SV;
3. lo que exige cautela fuerte de arquitectura y no debe cristalizar todavía en IR, validator, runner o backend;
4. y lo que deberá reexaminarse cuando se abran los siguientes carriles de interfaces pendientes y el frente de células especializadas.

Por tanto, esta capa sigue siendo un instrumento de vigilancia, contraste y preparación, no un mandato autónomo de cierre técnico.
