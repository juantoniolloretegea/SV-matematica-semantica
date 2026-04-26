# Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV

© 2026. Todos los derechos reservados. | DOI: [pendiente] | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 26/04/2026 |

---

## Estructura canónica de la publicación

| Pieza | Descripción canónica |
|---|---|
| [`teoria-general-sucesos-generadores-protocampos-unificados-sv.md`](./teoria-general-sucesos-generadores-protocampos-unificados-sv.md) | Documento doctrinal principal V.1 |
| [`imagenes/`](./imagenes/) | Portada canónica de la publicación |
| [`laboratorios/`](./laboratorios/) | Cinco laboratorios canónicos en Python que verifican computacionalmente los teoremas del documento |

---

## Contenido canónico del documento

El documento construye la **fórmula maestra unificada del Sistema Vectorial SV**, denotada 𝔉_SV, y la fija canónicamente como pieza algebraica única que articula los siete sectores primarios coexistentes (eléctrico, magnético, gravitatorio bisectorial, TPA, convergencia ternaria, espectral, topológico), las siete identidades intersectoriales {𝒮_k}, y el morfismo dictamen ternario G**_SV : T_SV → K_3 mediante la compuerta canónica de buena definición Δ_SV.

La fórmula canónica del Sistema Vectorial SV queda fijada en la Definición §K.7 del documento como:

```
𝔉_SV(Φ¹,…,Φ⁷; {𝒮_k}; G**_SV) := ⊕_{j=1}^{7} 𝓤⁽ʲ⁾_SV(Φʲ) ⊕ ⊕_{k=1}^{7} 𝒮_k ⊕ Δ_SV(G**_SV) = 0
```

donde ⊕ es el operador concatenador canónico (conjunción lógica factual) heredado del Glosario tipográfico canónico de Lloret Egea (2026 — luz factual).

---

## Verificación computacional canónica

Los cinco laboratorios canónicos en la carpeta [`laboratorios/`](./laboratorios/) verifican ejecutivamente los teoremas demostrados en el documento. Cada laboratorio es script Python autocontenido, ejecutable con Python ≥ 3.8 sin dependencias externas, trazable sección a sección al cuerpo doctrinal:

- **[Laboratorio 01](./laboratorios/lab_01_banco_numerico.py)** verifica el Teorema §17.1 sobre los diez supuestos del banco con residuos del orden de la precisión de máquina.
- **[Laboratorio 02](./laboratorios/lab_02_falsacion_canonica.py)** verifica el Teorema §C.1 ejecutando los seis criterios F1–F6 con sus controles C1–C6.
- **[Laboratorio 03](./laboratorios/lab_03_absorciones_canonicas.py)** verifica el Teorema §E.1 sobre las 110 celdas de la verificación cruzada de absorciones.
- **[Laboratorio 04](./laboratorios/lab_04_morfismo_dictamen.py)** verifica el Teorema §K.1 y el Corolario §K.1.bis sobre el morfismo dictamen G**_SV.
- **[Laboratorio 05](./laboratorios/lab_05_configuracion_propia.py)** aplica canónicamente la fórmula 𝔉_SV a configuraciones declaradas por el usuario.

El núcleo computacional canónico [`sv_core.py`](./laboratorios/sv_core.py) implementa los siete operadores sectoriales, las siete identidades intersectoriales, el operador concatenador ⊕ con cláusulas C.1 y C.2, la reconstrucción Rec, la admisibilidad Adm, el morfismo dictamen G**_SV = Adm ∘ Rec, la compuerta Δ_SV y la fórmula maestra 𝔉_SV.

Detalles de ejecución y mapa de verificación canónica en [`laboratorios/README.md`](./laboratorios/README.md).

---

## Licencia y advertencia

**Advertencia.** Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra sólo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y estrictamente supeditado al licenciamiento permitido.

**Warning.** This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.
