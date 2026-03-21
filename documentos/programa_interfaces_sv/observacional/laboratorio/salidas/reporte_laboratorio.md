# Laboratorio mínimo del frente de corpus observacional tipado

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA  
**Publicación:** IA en™ – La Biblia de la IA™  
**ISSN:** 2695-6411  
**Colección:** Programa de interfaces del Sistema Vectorial SV  
**Lugar y fecha:** Madrid, 20 de marzo de 2026

Este laboratorio no integra nada en el SV. Solo demuestra el principio conservador del patrón inaugural.

## Núcleo axiomático ensayado

1. Sin observación suficiente, no hay cierre favorable.
2. Sin garantía suficiente, no hay cierre favorable.
3. La indeterminación material relevante preserva `U`.
4. El fallo fuerte de captura o admisibilidad produce inadmisibilidad.

| Caso | Salida | Decisión | Fundamento |
|---|---|---|---|
| Caso A — Entrega favorable | 1 | paso | Observación suficiente y garantía válida: la compuerta autoriza la entrega. |
| Caso B — Salida en U | U | suspensión | La garantía no puede avalar honestamente la entrega; no se fabrica certeza. |
| Caso C — Inadmisibilidad | inadmisibilidad | bloqueo | Fallo de captura: no procede entrega semántica. |

## Casos de entrada

### Caso A — Entrega favorable
- Observación: captura=True, admisibilidad=ok, sigma_local=1.
- Nota observacional: Unidad observacional correctamente capturada y ternarizada.
- Garantía: avala_entrega=True, suficiencia=suficiente.
- Nota de garantía: La cadena observacional y la trazabilidad son bastante sólidas.

### Caso B — Salida en U
- Observación: captura=True, admisibilidad=degradado, sigma_local=1.
- Nota observacional: Existe observación, pero un punto material no queda blindado.
- Garantía: avala_entrega=False, suficiencia=deficiente.
- Nota de garantía: La garantía no puede avalar honestamente la entrega.

### Caso C — Inadmisibilidad
- Observación: captura=False, admisibilidad=fallido, sigma_local=U.
- Nota observacional: La captura falla y la cadena se corta.
- Garantía: avala_entrega=False, suficiencia=rota.
- Nota de garantía: No existe base suficiente para garantizar nada.

