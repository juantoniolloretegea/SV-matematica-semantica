# Laboratorios — Teoría general factual de la luz en el Sistema Vectorial SV

**Versión del paquete:** v1.0.0  
**Documento asociado:** *General factual theory of light in the Sistema Vectorial SV*  
**DOI documental Commons/KCWorks:** https://doi.org/10.17613/1z7c0-mqb40  
**Colección:** Contemporary Factual Mathematics and Physics of the SV  
**DOI canónico de colección:** https://doi.org/10.17613/r4dwa-d9b30  
**Sede material canónica:**  
https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/optica-factual-sv/teoria-general-factual-de-la-luz-en-el-sistema-vectorial-sv

Este directorio contiene veintidós laboratorios Python reproducibles, núcleo computacional, catálogo de errores, casos canónicos, runner estricto y ejecutor directo complementario. El paquete se prepara para depósito técnico en Zenodo, firma con AutoFirma, prueba OpenTimestamps e inserción en GitHub.

## Ejecución recomendada

```bash
python runner.py
```

Ejecución directa complementaria:

```bash
python run_all.py
```

## Estado material de esta versión

- 22/22 laboratorios ejecutados materialmente con resultado PASADO.
- 182 códigos `LUZ-` únicos en el catálogo canónico.
- Sin errores de sintaxis.
- Sin `except:` genérico ni `except Exception` detectado.
- JSON de configuración, catálogo y casos canónicos validados.
- Hashes SHA-256 incluidos.
- Informe de ejecución incluido en `EXECUTION_REPORT.txt`.

---

# Laboratorios — Régimen luminoso factual SV

Contrapartida ejecutable del documento
[`teoria-general-factual-luz-sv.md`](../teoria-general-factual-luz-sv.md).
Veintidós laboratorios Python verifican numérica y estructuralmente cada
teorema del documento, con catálogo de errores explícito (182 códigos LUZ
únicos) y runner sin pases silenciosos.

## Política de rigor

1. **Códigos únicos**: cada fallo estructural se reporta con un código del
   catálogo [`catalogo_errores.json`](catalogo_errores.json). Dos fallos
   estructuralmente distintos nunca comparten código; el mismo fallo nunca
   tiene dos códigos.
2. **Sin `except` genéricos**: los laboratorios capturan únicamente `SVError`
   y lo re-lanzan con su código. Ninguna excepción se ignora silenciosamente.
3. **Fail-fast**: el runner detiene la ejecución en el primer laboratorio que
   falla y reporta el código.
4. **Exit 0 sólo si los 22 pasan**: si cualquier laboratorio escribe `FALLO`
   en stdout o termina con `returncode != 0`, el runner termina con `exit(1)`.
5. **Determinismo**: semilla aleatoria 33 fijada globalmente; ejecuciones
   sucesivas producen salidas idénticas bit a bit en los valores verificados.
6. **Tolerancia estricta**: 1e-9 absoluto en identidades canónicas,
   5% relativo en comparaciones con valor heredado clásico.

## Ejecución completa

```bash
python3 runner.py
```

Salida esperada (síntesis):

```
RUNNER COMPLETADO — 22/22 laboratorios pasados en ~9 segundos.
Ningún código de error activado sobre 182 códigos canónicos.
El régimen luminoso factual SV queda verificado ejecutablemente.
```

## Índice de laboratorios

| # | Archivo | Teorema | Tema | Códigos principales |
|---|---|---|---|---|
| 01 | [`lab_01_vacio_factual.py`](lab_01_vacio_factual.py) | 2.1 + §2.6 | Vacío factual preternario y costura terminológica (a)(b)(c) | `LUZ-VAC-001..004` |
| 02 | [`lab_02_activacion_pi3h.py`](lab_02_activacion_pi3h.py) | Lemas 5.5, 7.3 | Activación Π<sub>3</sub><sup>H</sup> con no-retorno y honestidad | `LUZ-ACT-001..005` |
| 03 | [`lab_03_energia_cuanto.py`](lab_03_energia_cuanto.py) | 3.1, 3.2, 3.3 | Energía factual y cuanto canónico h<sub>SV</sub> | `LUZ-CUA-001..005`, `LUZ-ENG-001..003` |
| 04 | [`lab_04_ruptura_epsilon_cero.py`](lab_04_ruptura_epsilon_cero.py) | 3bis.1 | Ruptura de conservación y suceso cero ε<sub>0</sub> | `LUZ-EPS-001..004` |
| 05 | [`lab_05_materia_tpa.py`](lab_05_materia_tpa.py) | 15.1 | Materia factual rendida a aparato TPA | `LUZ-MAT-001..004`, `LUZ-TPA-001..003` |
| 06 | [`lab_06_gravedad_factor_phi.py`](lab_06_gravedad_factor_phi.py) | 14.1 | Gravedad como factor Φ y deformación de umbrales | `LUZ-GRA-001..005` |
| 07 | [`lab_07_siete_campos.py`](lab_07_siete_campos.py) | 6.1 | Siete campos factuales coexistentes | `LUZ-CAM-001..007` |
| 08 | [`lab_08_quince_proyecciones.py`](lab_08_quince_proyecciones.py) | 7.1 | Quince proyecciones canónicas P1–P15 | `LUZ-P1-001` a `LUZ-P6-001`, `LUZ-PRO-001..005` |
| 09 | [`lab_09_algoritmo_a1_a5.py`](lab_09_algoritmo_a1_a5.py) | §7.3bis | Algoritmo canónico A1–A5 de búsqueda proyectiva | `LUZ-A15-001..005` |
| 10 | [`lab_10_cuarenta_y_cuatro_operadores.py`](lab_10_cuarenta_y_cuatro_operadores.py) | §8 | Conjunto canónico de 44 operadores (24+12+8) | `LUZ-OPE-001..005` |
| 11 | [`lab_11_ecuacion_unica.py`](lab_11_ecuacion_unica.py) | 9.1 | Ecuación única L<sub>SV</sub> = 0 con 15 sumandos e 13 invariantes | `LUZ-LSV-001..008`, `LUZ-INV-001..013` |
| 12 | [`lab_12_propiedades_algebraicas.py`](lab_12_propiedades_algebraicas.py) | 10.1–10.5 | Homogeneidad, aditividad, covariancia, estabilidad | `LUZ-ALG-001..008` |
| 13 | [`lab_13_reduccion_maxwell.py`](lab_13_reduccion_maxwell.py) | 11.1 | Reducción a Maxwell factual con diccionario íntegro | `LUZ-MAX-001..004` |
| 14 | [`lab_14_emergencia_planck.py`](lab_14_emergencia_planck.py) | 12.1 | Emergencia factual de Planck E = h·ν | `LUZ-PLA-001..004` |
| 15 | [`lab_15_disolucion_dualidad.py`](lab_15_disolucion_dualidad.py) | 13.1 | Disolución proyectiva de la dualidad | `LUZ-DUA-001..004` |
| 16 | [`lab_16_falsacion_seis_criterios.py`](lab_16_falsacion_seis_criterios.py) | 17.1 | Falsación con seis criterios F.1–F.6 | `LUZ-FAL-001..008` |
| 17 | [`lab_17_celula_sv3_9.py`](lab_17_celula_sv3_9.py) | §18 | Recorrido de consistencia sobre célula SV(3, 9) | `LUZ-CEL-001..005` |
| 18 | [`lab_18_diecisiete_bancos.py`](lab_18_diecisiete_bancos.py) | §19 | Diecisiete bancos visibles B-LUZ-01 a B-LUZ-17 | `LUZ-BNC-001..005` |
| 19 | [`lab_19_transductor_nlp.py`](lab_19_transductor_nlp.py) | §8 A.23 | Transductor lingüístico 𝓘<sub>NLP</sub> sobre paquete observacional | `LUZ-NLP-001..003` |
| 20 | [`lab_20_coherencia_polarizacion_correlacion.py`](lab_20_coherencia_polarizacion_correlacion.py) | §8 B.6/B.7/B.16 + A.6.1 | Coherencia, polarización y correlación estructural | `LUZ-COH-001..003`, `LUZ-POL-001..003`, `LUZ-COR-001..003` |
| 21 | [`lab_21_transmutacion_clases.py`](lab_21_transmutacion_clases.py) | A.7.1 | Transmutación luminosa y clases emergentes χ<sub>α</sub> | `LUZ-TRS-001..003` |
| 22 | [`lab_22_antesala_unificado.py`](lab_22_antesala_unificado.py) | A.5.1, 22.1 | Antesala del régimen unificado U<sup>unif</sup><sub>SV</sub> sobre 7 sectores | `LUZ-UNF-001..003` |

## Infraestructura

| Archivo | Función |
|---|---|
| [`sv_core.py`](sv_core.py) | Núcleo operatorio: clase `SVError`, `CasoFibra`, construcción de acumulados, 15 sumandos de L<sub>SV</sub>, 15 proyecciones P1–P15, identidades O1/O2/O3, diccionario Maxwell de 18 entradas, constantes CODATA. |
| [`catalogo_errores.json`](catalogo_errores.json) | 182 códigos únicos organizados en 43 prefijos (ver tabla abajo). |
| [`runner_config.json`](runner_config.json) | Orden declarado de los 22 laboratorios y políticas de ejecución (tolerancia 1e-9, semilla 33, timeout 180s). |
| [`runner.py`](runner.py) | Ejecutor maestro: carga catálogo, verifica unicidad de códigos, ejecuta laboratorios secuencialmente, detiene al primer fallo, detecta pases silenciosos. |
| [`datos/casos_canonicos.json`](datos/casos_canonicos.json) | Tres casos canónicos: A simétrico SV(3,4), B asimétrico SV(3,6), C canónica SV(3,9) con datum estructural completo. |

## Prefijos del catálogo de errores

Los 182 códigos están organizados en 43 prefijos estructurales. Cada prefijo
corresponde a un dominio conceptual distinto del régimen luminoso:

### Prefijos de teoremas canónicos

| Prefijo | Dominio |
|---|---|
| `LUZ-VAC` | Vacío factual preternario (§2) |
| `LUZ-ACT` | Activación Π<sub>3</sub><sup>H</sup> (§5, Lemas 5.5/7.3) |
| `LUZ-CUA` | Cuanto factual h<sub>SV</sub> (§3, Teorema 3.1) |
| `LUZ-ENG` | Energía factual (§3, Teoremas 3.2/3.3) |
| `LUZ-EPS` | Suceso cero ε<sub>0</sub> y ruptura de conservación (§3bis) |
| `LUZ-MAT` | Materia factual (§4) |
| `LUZ-TPA` | Aparato TPA aplicado (2026h, Teorema 15.1) |
| `LUZ-GRA` | Gravedad y factor Φ (§5, Teorema 14.1) |
| `LUZ-CAM` | Siete campos factuales (§6, Teorema 6.1) |
| `LUZ-FIB` | Objeto fibroso factual Φ<sup>L</sup><sub>SV</sub> (§7) |
| `LUZ-PRO` | Proyecciones canónicas y unidad proyectiva (§7.3, Teorema 7.1) |
| `LUZ-A15` | Algoritmo canónico A1–A5 de búsqueda proyectiva (§7.3bis) |
| `LUZ-P1..P6` | Proyecciones individuales P1–P6 (§7.3) |
| `LUZ-OPE` | Conjunto canónico de 44 operadores (§8) |
| `LUZ-LSV` | Operador maestro L<sub>SV</sub> y 15 sumandos (§9, Teorema 9.1) |
| `LUZ-INV` | Trece invariantes I1–I13 (§9) |
| `LUZ-ALG` | Propiedades algebraicas (§10, Teoremas 10.1–10.5) |
| `LUZ-MAX` | Reducción a Maxwell factual (§11, Teorema 11.1) |
| `LUZ-PLA` | Emergencia de Planck (§12, Teorema 12.1) |
| `LUZ-DUA` | Disolución de la dualidad (§13, Teorema 13.1) |
| `LUZ-UNI` | Unicidad canónica interna (§16, Teorema 16.1) |
| `LUZ-FAL` | Seis criterios de falsación (§17, Teorema 17.1 y Proposición 17.1) |
| `LUZ-CEL` | Célula canónica SV(3, 9) (§18) |
| `LUZ-BNC` | Diecisiete bancos visibles (§19) |
| `LUZ-LAB` | Arquitectura laboratorial (§20) |
| `LUZ-UNF` | Antesala del régimen unificado (§22, Teorema A.5.1) |
| `LUZ-APP` | Apéndice final y glosario |
| `LUZ-TRS` | Transmutación luminosa (Teorema A.7.1) |
| `LUZ-COH` | Coherencia estructural (B.7) |
| `LUZ-POL` | Polarización y residual polar (B.6) |
| `LUZ-COR` | Correlación estructural entre fibras (B.16, Teorema A.6.1) |
| `LUZ-NLP` | Transductor NLP 𝓘<sub>NLP</sub> (A.23) |
| `LUZ-CHI` | Alfabeto ternario Σ = {0, 1, U} y configuración χ |
| `LUZ-DIM` | Consistencia dimensional y calibración metrológica |
| `LUZ-PAR` | Par polar (α, β) preternario y protocampo primordial |
| `LUZ-PRN` | Prohibiciones P.1–P.6 del corpus |
| `LUZ-CFG` | Configuración y carga de catálogo/casos |
| `LUZ-IO` | Entrada/salida y parsing |
