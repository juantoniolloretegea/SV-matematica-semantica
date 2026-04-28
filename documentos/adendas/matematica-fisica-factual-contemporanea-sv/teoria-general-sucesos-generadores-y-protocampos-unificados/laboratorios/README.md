# Laboratorios canónicos — Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV

Este directorio contiene los **cinco laboratorios canónicos** que verifican computacionalmente las afirmaciones del documento **V.1** de la publicación *«Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV»* (Lloret Egea, 2026).

Los cinco laboratorios son **scripts Python autocontenidos** y **trazables sección a sección** al documento canónico V.1. Cada uno verifica un teorema canónico específico mediante ejecución reproducible.


---

## Identificación del depósito reproducible

- **Título del laboratorio:** Laboratorios canónicos de la Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV
- **DOI del laboratorio reproducible:** https://doi.org/10.5281/zenodo.19863166
- **DOI de la publicación principal:** https://doi.org/10.17613/177nb-v2465
- **Relación documental:** este paquete es material computacional suplementario de la publicación principal en Commons/KCWorks.
- **Repositorio vivo en GitHub:** https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-general-sucesos-generadores-y-protocampos-unificados/laboratorios
- **Versión del paquete:** V.1 / 1.0.0
- **Fecha:** 2026-04-26


---

## Estructura del directorio

```
laboratorios_sucesos_generadores_protocampos_sv_v1/
├── README.md                            Este archivo
├── CITATION.cff                         Metadatos de citación del laboratorio
├── LICENSE.txt                          Licencia y advertencia jurídica
├── MANIFEST.json                        Manifiesto técnico del paquete
├── SHA256SUMS.txt                       Hashes SHA-256 de integridad
├── ZENODO_UPLOAD_FIELDS.md              Campos recomendados para Zenodo
├── run_all.py                           Ejecución secuencial de los cinco laboratorios
├── sv_core.py                           Núcleo computacional canónico del SV
├── lab_01_banco_numerico.py             Banco numérico de los diez supuestos §17
├── lab_02_falsacion_canonica.py         Banco de falsación operativa F1–F6 §C
├── lab_03_absorciones_canonicas.py      Verificación cruzada de absorciones §E
├── lab_04_morfismo_dictamen.py          Morfismo dictamen ternario G**_SV §K
└── lab_05_configuracion_propia.py       Configuración propia del usuario
```

---

## Requisitos

- Python ≥ 3.8
- No requiere bibliotecas externas (sólo módulos estándar `math` y `dataclasses`)

---

## Ejecución

Cada laboratorio se ejecuta independientemente desde la carpeta:

```bash
cd laboratorios/

python3 lab_01_banco_numerico.py
python3 lab_02_falsacion_canonica.py
python3 lab_03_absorciones_canonicas.py
python3 lab_04_morfismo_dictamen.py
python3 lab_05_configuracion_propia.py

# Ejecución completa secuencial
python3 run_all.py
```

---

## Mapa canónico de verificación

| Laboratorio | Teorema verificado | Sección de V.1 | Esperado |
|---|---|---|---|
| Lab 01 | Teorema §17.1 — Cumplimiento del banco numérico | §17 | 10/10 supuestos anulan, residuos ≤ 1e-16 |
| Lab 02 | Teorema §C.1 — Compatibilidad canonicidad-falsabilidad | §C | 6/6 controles canónicamente verificados |
| Lab 03 | Teorema §E.1 — Coincidencia cruzada de absorciones | §E | 110/110 celdas anulan canónicamente |
| Lab 04 | Teorema §K.1 + Corolario §K.1.bis — Morfismo dictamen | §K | Tabla §K.8 reproducida; 10/10 dictámenes |
| Lab 05 | Aplicación canónica de 𝔉_SV a configuración propia | §K.7 | Operativo para terceros |

---

## Núcleo computacional `sv_core.py`

El módulo `sv_core.py` implementa canónicamente:

- Operadores canónicos básicos `Div_SV`, `Rot_SV` (Definición §11.2 de V.1)
- Operador concatenador `⊕` con cláusulas C.1 y C.2 (Definición §11.1)
- Siete operadores sectoriales `𝓤⁽¹⁾_SV` a `𝓤⁽⁷⁾_SV` (Definiciones §11.2–§11.8)
- Siete identidades intersectoriales `𝒮_1` a `𝒮_7` (Tabla §12)
- Reconstrucción canónica `Rec` (Definición §K.3)
- Admisibilidad canónica `Adm` con disjunción exhaustiva (Definición §K.4)
- Morfismo dictamen `G**_SV = Adm ∘ Rec` (Definición §K.5)
- Compuerta canónica de buena definición `Δ_SV` (Definición §K.6)
- Fórmula maestra unificada `𝔉_SV` (Definición §K.7)

Cada función referencia explícitamente la sección de V.1 que la sostiene canónicamente. Ningún operador se introduce sin trazabilidad al corpus con DOI.

---

## Disciplina canónica del operador `⊕`

El operador concatenador `⊕` del Sistema Vectorial SV es **conjunción lógica factual**, NO suma aritmética. Implementación: `oplus_anula(*valores)` evalúa la propiedad de anulación canónica conjunta sin sumar los valores. La función `suma_absoluta` se usa exclusivamente para reportar el residuo consolidado por suma de valores absolutos `Σ|x_i|`, conforme al §17.13 de V.1.

---

## Reproducibilidad

Los cinco laboratorios producen salida tabulada determinista. Cualquier revisor académico puede:

1. Clonar el repositorio.
2. Ejecutar los cinco scripts.
3. Verificar que los residuos numéricos son del orden de la precisión de máquina (≈ 1e-16) sobre los diez supuestos del banco §17.
4. Verificar que las 110 celdas de la Tabla §E.1 anulan canónicamente.
5. Verificar que la Tabla §K.8 se reproduce exactamente.
6. Aplicar la fórmula sobre configuraciones propias mediante el Lab 05.

Esto cumple operativamente el criterio P.4 del corpus (no inferencia opaca) al máximo nivel posible.

---

## Trazabilidad por DOI

Cada laboratorio invoca operadores cuya canonización está cerrada en publicaciones del corpus con DOI explícito. La carpeta `laboratorios/` no re-axiomatiza ningún cierre canónico; opera por invocación trazable de las publicaciones de origen, conforme a la disciplina P.5.

---

## Licencia y autoría

© 2026. Todos los derechos reservados.
Juan Antonio Lloret Egea — ORCID: 0000-0002-6634-3351
ITVIA — Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia CC BY-NC-ND 4.0
DOI del laboratorio: https://doi.org/10.5281/zenodo.19863166
DOI de la publicación principal: https://doi.org/10.17613/177nb-v2465
Madrid, 26/04/2026

**Advertencia.** Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada.

**Warning.** This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated.
