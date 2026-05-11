# Laboratorios reproducibles SV-BH9

![Portada de la publicación](../imagenes/portada_agujero_negro_clausura_no_transmisibilidad.png)

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Derechos:** © 2026. Todos los derechos reservados.  
**Licencia:** CC BY-NC-ND 4.0  
**Fecha:** Madrid, 10/05/2026

## Objeto

Estos laboratorios verifican el banco SV-BH9 de la publicación [El agujero negro como cierre interno sin resto exterior formulable](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/agujero-negro-clausura-no-transmisibilidad.md).

No hay pases silenciosos: cada caso declara entrada, cálculo, resultado esperado, resultado obtenido y estado. Los errores adversariales esperados cuentan como APTO sólo si se detectan con el código previsto.


## Registro vinculado

Los laboratorios quedan vinculados al registro de preservación de la publicación principal. El registro histórico de la carpeta contenedora está disponible en [Internet Archive](https://web.archive.org/web/20260511122405/https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad); el registro histórico del texto principal está disponible en [Internet Archive](https://web.archive.org/web/20260511122924/https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/agujero-negro-clausura-no-transmisibilidad.md); el detalle de firma, estampillado de tiempo y hashes se recoge en [../registros/README.md](../registros/README.md).

## Ejecución

python runner.py

## Componentes

| Componente | Función |
|---|---|
| [datos/sv_bh9_banco.json](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/datos/sv_bh9_banco.json) | Banco de entrada con células, fórmulas externas, casos adversariales y metadatos de autoría. |
| [src/sv_core.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/sv_core.py) | Núcleo de DΣ, T(n), conteos, formas equivalentes de 𝔅Hₛᵥ y postfrontera. |
| [src/bh_physics.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/bh_physics.py) | Cálculos externos: Schwarzschild, Kerr, termodinámica y singularidad geométrica. |
| [src/absorption.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/absorption.py) | Clasificación de absorción, absorción parcial y rechazo como fundamento. |
| [src/validators.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/validators.py) | Validadores sin pase silencioso y generación de trazas. |
| [catalogo_errores.md](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/catalogo_errores.md) | Catálogo de errores de laboratorio. |
| [salidas](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/salidas) | Resultados JSON, traza CSV y resumen reproducible. |

## Estado esperado

El estado global esperado es APTO, con todos los errores adversariales detectados.
