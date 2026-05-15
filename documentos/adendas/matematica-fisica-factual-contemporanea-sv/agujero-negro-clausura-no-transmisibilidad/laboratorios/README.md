# Laboratorios reproducibles SV-BH9

![Portada de la publicación](../imagenes/portada_agujero_negro_clausura_no_transmisibilidad.png)

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Derechos:** © 2026. Todos los derechos reservados.  
**Licencia:** CC BY-NC-ND 4.0  
**Fecha:** Madrid, 10/05/2026  
**DOI editorial PubPub/Crossref:** [10.21428/39829d0b.b757ccc4](https://doi.org/10.21428/39829d0b.b757ccc4)  
**Release editorial PubPub:** [Release 1](https://www.itvia.online/pub/el-agujero-negro-como-cierre-interno-sin-resto-exterior-formulable/release/1)  
**Colección editorial:** [El Universo](https://www.itvia.online/el-universo)  
**DOI de la colección El Universo:** [10.21428/39829d0b.26484bfd](https://doi.org/10.21428/39829d0b.26484bfd)  
**DOI Zenodo de preservación:** [10.5281/zenodo.20155687](https://doi.org/10.5281/zenodo.20155687)  
**DOI Zenodo de todas las versiones:** [10.5281/zenodo.20155686](https://doi.org/10.5281/zenodo.20155686)

---

## Objeto

Estos laboratorios verifican el banco SV-BH9 de la publicación [El agujero negro como cierre interno sin resto exterior formulable](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/agujero-negro-clausura-no-transmisibilidad.md).

No hay pases silenciosos: cada caso declara entrada, cálculo, resultado esperado, resultado obtenido y estado. Los errores adversariales esperados cuentan como APTO sólo si se detectan con el código previsto.

---

## Registro vinculado

Los laboratorios quedan vinculados al registro editorial y al registro de preservación de la publicación principal. La lectura editorial pública vive en PubPub/Crossref, el paquete técnico de preservación vive en Zenodo, y la sede canónica técnica del laboratorio vive en GitHub.

DOI editorial PubPub/Crossref de la publicación:

[10.21428/39829d0b.b757ccc4](https://doi.org/10.21428/39829d0b.b757ccc4)

Release editorial PubPub:

[https://www.itvia.online/pub/el-agujero-negro-como-cierre-interno-sin-resto-exterior-formulable/release/1](https://www.itvia.online/pub/el-agujero-negro-como-cierre-interno-sin-resto-exterior-formulable/release/1)

Colección editorial El Universo:

[https://www.itvia.online/el-universo](https://www.itvia.online/el-universo)

DOI de la colección El Universo:

[10.21428/39829d0b.26484bfd](https://doi.org/10.21428/39829d0b.26484bfd)

DOI Zenodo de preservación:

[10.5281/zenodo.20155687](https://doi.org/10.5281/zenodo.20155687)

DOI Zenodo de todas las versiones:

[10.5281/zenodo.20155686](https://doi.org/10.5281/zenodo.20155686)

Registro histórico de la carpeta contenedora:

[Internet Archive](https://web.archive.org/web/20260511122405/https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad)

Registro histórico del texto principal:

[Internet Archive](https://web.archive.org/web/20260511122924/https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/agujero-negro-clausura-no-transmisibilidad.md)

Registro detallado de preservación, firma, estampillado y hashes:

[../registros/README.md](../registros/README.md)

---

## Ejecución

La ejecución completa se realiza desde esta carpeta con:

```bash
python runner.py
```

La batería de tests se ejecuta con:

```bash
python -m pytest -q
```

---

## Componentes materiales del laboratorio

- [datos/sv_bh9_banco.json](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/datos/sv_bh9_banco.json): banco de entrada con células, fórmulas externas, casos adversariales y metadatos de autoría.
- [src/sv_core.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/sv_core.py): núcleo de DΣ, T(n), conteos, formas equivalentes de BHₛᵥ y postfrontera.
- [src/bh_physics.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/bh_physics.py): cálculos externos de Schwarzschild, Kerr, termodinámica y singularidad geométrica.
- [src/absorption.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/absorption.py): clasificación de absorción, absorción parcial y rechazo como fundamento.
- [src/validators.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/validators.py): validadores sin pase silencioso y generación de trazas.
- [src/autoria.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/src/autoria.py): metadatos de autoría y publicación.
- [catalogo_errores.md](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/catalogo_errores.md): catálogo de errores de laboratorio.
- [salidas](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/salidas): resultados JSON, traza CSV y resumen reproducible.

---

## Salidas reproducibles

La ejecución del laboratorio genera o conserva las salidas siguientes:

- [salidas/sv_bh9_resultados.json](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/salidas/sv_bh9_resultados.json)
- [salidas/sv_bh9_traza.csv](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/salidas/sv_bh9_traza.csv)
- [salidas/sv_bh9_resumen.md](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/agujero-negro-clausura-no-transmisibilidad/laboratorios/salidas/sv_bh9_resumen.md)

---

## Estado esperado

La salida global esperada es APTO: 54 casos totales, 54 aptos, 0 fallidos y 15 errores adversariales detectados. La batería `pytest` asociada al paquete debe devolver 6 tests superados.

Un validador no puede devolver APTO por ausencia de datos. Debe distinguir entre APTO, NO_APTO y dato ausente; cualquier ausencia material de dato exigido impide el cierre global hasta que el alcance quede declarado o el dato sea incorporado.
