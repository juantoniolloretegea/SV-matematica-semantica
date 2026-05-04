# Conjunto laboratorial reproducible — De Bell a Tsirelson sin formalismo de Hilbert en el Sistema Vectorial SV

**Documento canónico vinculado:** [De Bell a Tsirelson sin formalismo de Hilbert: aparato determinista no local del Sistema Vectorial SV con alfabeto ternario, unicidad del correlador angular factual acoplado y derivación estructural de la cota cuántica](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/de-bell-a-tsirelson-sin-formalismo-hilbert)

**Autor:** Juan Antonio Lloret Egea — ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)
**Editor:** IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español, ITVIA) — ISSN 2695-6411
**Licencia:** CC BY-NC-ND 4.0 — Protegida por [CEDRO](https://www.cedro.org/english?lng=en)
**© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.**

---

## Depósito canónico en Zenodo

El presente conjunto laboratorial se publica en Zenodo (CERN Data Centre & InvenioRDM) como software canónico bajo el DOI [`10.5281/zenodo.20020201`](https://doi.org/10.5281/zenodo.20020201).

| Campo | Valor |
|---|---|
| **DOI** | [10.5281/zenodo.20020201](https://doi.org/10.5281/zenodo.20020201) |
| **Registro Zenodo** | [https://zenodo.org/records/20020201](https://zenodo.org/records/20020201) |
| **Versión** | v1 — 2 de mayo de 2026 |
| **Fichero canónico** | `laboratorios.zip` |
| **SHA-256** | `7a34823d351529c152d8744879f2256d38f8a11444fac1535ea28be8a53f8335` |
| **Firma digital** | `laboratorios.zip_signed.csig` (DER PKCS#7 Signed Data — firma desprendida del autor, certificado FNMT-RCM bajo eIDAS) |
| **Sello temporal** | `laboratorios.zip.ots` (OpenTimestamps anclado en la blockchain de Bitcoin) |

La integridad y autenticidad del depósito quedan garantizadas por la conjunción de los tres ficheros publicados conjuntamente en Zenodo. Cualquier modificación del fichero `laboratorios.zip` invalidaría tanto la firma digital como el sello temporal.

**Verificación criptográfica por terceros:**

```bash
# Verificación SHA-256
sha256sum laboratorios.zip
# Debe producir: 7a34823d351529c152d8744879f2256d38f8a11444fac1535ea28be8a53f8335

# Verificación de la firma digital con OpenSSL
openssl smime -verify -binary -inform DER \
    -in laboratorios.zip_signed.csig \
    -content laboratorios.zip \
    -noverify -out /dev/null

# Verificación del sello temporal con cliente OpenTimestamps
ots verify laboratorios.zip.ots --file laboratorios.zip
```

---

## Cláusula de subordinación

El conjunto laboratorial está **subordinado** al documento canónico fijado. Su función exclusiva es **verificar y cotejar** por cómputo determinista los enunciados del documento canónico. No introduce contenido doctrinal nuevo, no extiende, no reescribe y no propone. Si un laboratorio detectara un fallo de cotejo o un error material, lo reporta sin tocar el documento canónico.

---

## Estructura del conjunto

```
laboratorios/
├── CATALOGO-DE-ERRORES.md                    [códigos E-01..E-09]
├── runner.py                                 [runner agregado]
├── LAB-01_saturacion_familia_celulas.py
├── LAB-02_factorizacion_R0.py
├── LAB-03_monotonia_barrido.py
├── LAB-04_equivalencia_cuantica.py
├── LAB-05_unicidad_correlador.py
└── LAB-06_fidelidad_A9.py
```

Total: **8 ficheros** bajo la carpeta raíz `laboratorios/`, comprendiendo el catálogo unificado de errores (códigos E-01 a E-09), el runner agregado y los seis laboratorios canónicos LAB-01 a LAB-06.

## Catálogo de los seis laboratorios canónicos

| ID | Laboratorio | Sección doctrinal | Criterio de aptitud (tolerancia 1e-14 IEEE 754) |
|---|---|---|---|
| 1 | `LAB-01_saturacion_familia_celulas.py` | §11.2 — Teorema 11.2.1 | `\|S_SV(χ_c=1)\| = 2√2` sobre familia SV(b, b²), b ∈ {3, 4, 5, 7, 9, 11} |
| 2 | `LAB-02_factorizacion_R0.py` | §§6.2, 7.3 — Teorema 6.2.1, Lema 7.3.1 | `\|R₀(Q)\| = 260` sobre SV(3, 9), `T(v; Q) ≡ 0 (mod 2)` sobre 𝔽₂, `\|X(v)\| ≤ 2` |
| 3 | `LAB-03_monotonia_barrido.py` | §11.3, §11.1 — Teorema 11.3.1, Corolario 11.1.0.1 | monotonía estricta sobre 10 001 puntos de [0, 1], cruce único S = 2 |
| 4 | `LAB-04_equivalencia_cuantica.py` | §10.2 — Teorema 10.2.1 | `C_SV(δ) = E_QM(α, β) = −cos(α − β)` sobre 1 000 cuádruples |
| 5 | `LAB-05_unicidad_correlador.py` | §10.2 — Teorema 10.2.1 | sólo `C_SV(δ) = −cos δ` satisface A1–A9 entre once candidatos |
| 6 | `LAB-06_fidelidad_A9.py` | §9.4 — Lema 9.4.1 | sólo `k = 1` admitido como representación angular fiel |

## Estructura de salida

Cada laboratorio produce salida humano-legible por consola con la siguiente estructura canónica:

```
========================================================================
LAB-XX — <Título del laboratorio>
========================================================================

Cota / invariante esperado: <valor canónico>
Tolerancia operativa: 1e-14 (IEEE 754)

<tabla de verificación con marcas [OK] / [FALLA] por entrada>

✓ LAB-XX SUPERADO: <enunciado verificado del documento canónico>.
   ó
✗ LAB-XX FALLA: <descripción del fallo y código E-NN aplicable>.
```

El laboratorio retorna **código de salida 0** si todas las entradas verifican el enunciado dentro de la tolerancia operativa, y **código de salida 1** si alguna entrada falla. Bajo política de **no pases silenciosos**, todo fallo numérico se mapea al catálogo unificado E-01 a E-09 documentado en `CATALOGO-DE-ERRORES.md`.

## Aptitud

Un laboratorio es **APTO** si y sólo si:

(i) `código de salida = 0` sobre la entrada canónica del apartado correspondiente;

(ii) todas las verificaciones tabulares marcan `[OK]` dentro de la tolerancia operativa (1e-14 para magnitudes en coma flotante, exacto para cardinales y verificaciones combinatorias).

Un laboratorio es **NO APTO** si `código de salida = 1` sobre la entrada de cierre estructural o si alguna verificación tabular marca `[FALLA]`. El runner agregado emite dictamen global `APTO` si y sólo si los seis laboratorios son individualmente aptos.

## Invocación

### Ejecución de un laboratorio individual

```bash
python LAB-01_saturacion_familia_celulas.py
```

Produce salida humano-legible por consola con la estructura indicada y dictamen `LAB-XX SUPERADO` / `LAB-XX FALLA`.

### Ejecución del runner agregado

```bash
python runner.py
```

Ejecuta los seis laboratorios en orden, captura los resultados y emite informe global de cumplimiento. **Código de salida 0** si los seis laboratorios superan sus verificaciones; **código de salida 1** si al menos uno falla.

## Dependencias

- Biblioteca estándar de Python (versión ≥ 3.10).
- `numpy` (única dependencia externa, requerida por todos los laboratorios para la aritmética del aparato angular).

No requiere ninguna otra dependencia externa.

## Catálogo de errores

Códigos canónicos E-01 a E-09 documentados en [`CATALOGO-DE-ERRORES.md`](./CATALOGO-DE-ERRORES.md):

| Código | Descripción |
|:---:|:---|
| E-01 | Saturación `\|S\| ≠ 2√2` sobre familia de células |
| E-02 | `\|R₀(Q)\| ≠ 260` sobre SV(3, 9) bajo codificación SV (0 ↦ 0, 1 ↦ +1, U ↦ −1) |
| E-03 | `T mod 2 ≠ 0` sobre R₀ |
| E-04 | `\|X(v)\| > 2` sobre v ∈ R₀ |
| E-05 | Monotonía no estricta sobre [χ_min, 1] |
| E-06 | `C_SV(δ) ≠ E_QM(α, β)` sobre cuádruple |
| E-07 | Candidato canónico falla un axioma A1–A9 |
| E-08 | Candidato alternativo cumple A1–A9 espuriamente |
| E-09 | k = 2, 3, … admitido como representación angular fiel |

## Reproducibilidad

Cada laboratorio es **estrictamente determinista**: misma entrada produce misma salida a precisión de máquina IEEE 754 sobre cualquier plataforma compatible. La única invocación de generador pseudoaleatorio (LAB-04, sobre 1 000 cuádruples de bases) está fijada por `np.random.seed(42)` para garantizar reproducibilidad cruzada bit a bit. El conjunto no utiliza muestreo, no depende de probabilidad, no realiza inferencia opaca y no recurre a aprendizaje inductivo. Conforme a las prohibiciones constitutivas P.1, P.2 y P.4 del corpus del Sistema Vectorial SV.

## Cláusula de validez vinculante

Este conjunto laboratorial es vinculante exclusivamente cuando está vinculado al documento canónico. Los laboratorios aislados del documento carecen de valor doctrinal: cualquier interpretación, derivación o aplicación que se haga de ellos sin remisión al cuerpo del documento canónico queda fuera del Sistema Vectorial SV.

## Cláusula de prevalencia

En caso de discrepancia, divergencia, errata, omisión o cualquier incoherencia entre el conjunto laboratorial y el cuerpo del documento canónico, **prevalece el cuerpo del documento canónico**. Los laboratorios son subordinados al texto canónico, no al revés.

## Citación canónica

> Lloret Egea, J. A. (2026). *Canonical laboratories from Bell to Tsirelson without Hilbert-space formalism within the Vectorial System SV*. Zenodo. [https://doi.org/10.5281/zenodo.20020201](https://doi.org/10.5281/zenodo.20020201)

## Aclaración sobre la versión publicada en GitHub

La versión publicada en este repositorio GitHub mantiene los mismos seis laboratorios canónicos depositados en Zenodo, con referencias bibliográficas explícitas al DOI canónico. La versión criptográficamente firmada y sellada es la disponible en Zenodo bajo el DOI [10.5281/zenodo.20020201](https://doi.org/10.5281/zenodo.20020201). Para verificación de integridad y autenticidad por terceros, descárguese el paquete `laboratorios.zip` con sus dos ficheros adjuntos `laboratorios.zip_signed.csig` y `laboratorios.zip.ots` directamente desde el registro Zenodo.
