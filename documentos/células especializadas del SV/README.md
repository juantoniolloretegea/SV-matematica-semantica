# Células especializadas del Sistema Vectorial SV — Laboratorio de referencia

Repositorio: `SV-matematica-semantica`
Ruta: `documentos/celulas_especializadas_sv/`
Estatuto: implementación de referencia subordinada al documento marco

## Contenido

- `laboratorio_celulas_especializadas_marco.py` — implementación ejecutable de las
  tres operaciones del anexo técnico del documento marco (§10).
- `README.md` — este archivo.

## Documento de referencia

Juan Antonio Lloret Egea. *Células especializadas del Sistema Vectorial SV:
estatuto, perfil funcional mínimo y familias iniciales.*
ITVIA, IA eñ™ — La Biblia de la IA™, ISSN 2695-6411, Madrid, 2026.
Disponible en: https://www.itvia.online

## Operaciones implementadas

1. `evaluar_admisibilidad` — contrasta las seis condiciones del perfil
   funcional mínimo (§4), incluyendo la referenciación explícita al aparato
   de la familia VII cuando éste comparece (§4.5-bis).
2. `clasificar_familia` — determina si la célula es especialización de dominio
   o de interfaz según los criterios de §5.0.
3. `merece_tratamiento_formal_especifico` — decide si la célula candidata
   satisface las condiciones de §8 para recibir tratamiento formal propio.

## Casos incluidos

- **Caso positivo:** célula de vigilancia y seguridad estructural. Clasificada
  como especialización de dominio; admisible; merece tratamiento formal
  específico.
- **Caso negativo:** célula de interlocución funcional condicionada. Clasificada
  como especialización de interfaz; falla admisibilidad por ausencia de
  referencias explícitas al aparato VII y perfil no estabilizado. Ilustra
  el estatuto de §5.4.

## Límite declarado

La condición `perfil_estable` no puede verificarse computacionalmente.
El laboratorio la hace visible como límite en lugar de ocultarla (véase §10.4
del documento marco y la Figura 3 del documento).

## Estatuto

Esta implementación es subordinada y demostrativa. No constituye
especificación técnica cerrada del Lenguaje SV, semántica operacional
completa ni contrato de integración con runner o backend.

## Ejecución
```bash
python laboratorio_celulas_especializadas_marco.py
```

## Autor

Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial
para el Español™ (ITVIA)

Implementación ejecutable del anexo técnico del documento marco sobre
células especializadas. Incluye evaluar_admisibilidad, clasificar_familia
y merece_tratamiento_formal_especifico con caso positivo (vigilancia/
seguridad) y caso negativo (interlocución condicionada, fallo en VII).
Estatuto: subordinado y demostrativo. No especificación técnica del
Lenguaje SV.
