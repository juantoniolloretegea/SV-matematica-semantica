# Laboratorios — Dominio termodinámico factual SV

Contrapartida ejecutable del documento
[`formula_factual_unica_absoluta_termodinamica_sv.md`](../formula_factual_unica_absoluta_termodinamica_sv.md).
Doce laboratorios Python verifican numérica y estructuralmente cada teorema del
documento, con catálogo de errores explícito y runner sin pases silenciosos.

## Política de rigor

1. **Códigos únicos**: cada fallo estructural se reporta con un código del
   catálogo [`catalogo_errores.json`](catalogo_errores.json). Dos fallos
   estructuralmente distintos nunca comparten código; el mismo fallo nunca tiene
   dos códigos.
2. **Sin `except` genéricos**: los laboratorios capturan únicamente `SVError` y
   lo re-lanzan con su código. Ninguna excepción se ignora silenciosamente.
3. **Fail-fast**: el runner detiene la ejecución en el primer laboratorio que
   falla y reporta el código.
4. **Exit 0 sólo si los 12 pasan**: si cualquier laboratorio escribe `FALLO` en
   stdout o termina con `returncode != 0`, el runner termina con `exit(1)`.
5. **Determinismo**: semillas aleatorias fijadas; ejecuciones sucesivas producen
   salidas idénticas bit a bit en los valores verificados.

## Ejecución completa

```bash
python3 runner.py
```

Salida esperada (síntesis):

```
RUNNER COMPLETADO — 12/12 laboratorios pasados en ~5 segundos.
Ningún código de error activado.
```

## Índice de laboratorios

| # | Archivo | Teorema | Tema | Códigos principales |
|---|---|---|---|---|
| 01 | [`lab_01_balance_canonico.py`](lab_01_balance_canonico.py) | 8.1 | Balance canónico 𝔇𝒜 = 𝒲+𝒬+𝒰 | `BAL-001..005` |
| 02 | [`lab_02_irreversibilidad.py`](lab_02_irreversibilidad.py) | 8.2 | Irreversibilidad factual 𝔇𝓗 ≥ 0 | `IRR-001..003`, `H-001..003` |
| 03 | [`lab_03_tres_formas_cruzadas.py`](lab_03_tres_formas_cruzadas.py) | 15.5 | Tres formas cruzadas (90/90 coincidencias) | `W-005..006`, `Q-005..006`, `U-005..006`, `L-002..003`, `A-003`, `F-005..006` |
| 04 | [`lab_04_vector_director.py`](lab_04_vector_director.py) | 15.4 | Vector director y ortogonalidad u⃗·𝖦 = 0 | `ORT-001..004`, `GEN-001..004` |
| 05 | [`lab_05_identidad_termometrica.py`](lab_05_identidad_termometrica.py) | 10.4 | Identidad termométrica Θ·𝔇𝓗 = 𝔇𝒬 | `T-001..007` |
| 06 | [`lab_06_absorcion_limite_clasica.py`](lab_06_absorcion_limite_clasica.py) | §10 | Absorción del límite clásico dU = δW+δQ | `BAL-005`, `T-003`, `U-008` |
| 07 | [`lab_07_fuerza_helmholtz_factual.py`](lab_07_fuerza_helmholtz_factual.py) | §6.5 | Fuerza canónica −∇φ + ⋆d𝒜^vec + 𝒥·ê | `F-001..008` |
| 08 | [`lab_08_unicidad_generador.py`](lab_08_unicidad_generador.py) | 5.1.b | Unicidad del generador 𝖦_SV | `GEN-001..004` |
| 09 | [`lab_09_exhaustividad_tres_clases.py`](lab_09_exhaustividad_tres_clases.py) | 15.8 | Exhaustividad de las tres clases | `EXH-001..002` |
| 10 | [`lab_10_consistencia_dimensional.py`](lab_10_consistencia_dimensional.py) | §9 | Consistencia dimensional del pilar | `DIM-001..003`, `MET-001..002`, `P5-001` |
| 11 | [`lab_11_celula_canonica_sv3_9.py`](lab_11_celula_canonica_sv3_9.py) | 11.1 | Consistencia sobre célula canónica SV(3, 9) | `CEL-001..003`, `BAL-002` |
| 12 | [`lab_12_adversarial_rivales.py`](lab_12_adversarial_rivales.py) | 16.3 | Exclusividad frente a 6 rivales por C1-C7 | `EXC-001..003` |

## Infraestructura

| Archivo | Función |
|---|---|
| [`sv_core.py`](sv_core.py) | Núcleo operatorio: clase `SVError`, `CasoCanonico`, construcción del fibrado, tres formas, vector director, producto con 𝖦_SV. |
| [`catalogo_errores.json`](catalogo_errores.json) | 120 códigos únicos organizados por prefijo (W, Q, U, F, T, L, A, H, J, R, B, BAL, IRR, ORT, GEN, PAR, EXH, EXC, DIM, TRA, CHI, CEL, APP, PRN, MET, P1-P6, LAB, CFG, IO). |
| [`runner_config.json`](runner_config.json) | Orden declarado de los 12 laboratorios y políticas de ejecución. |
| [`runner.py`](runner.py) | Ejecutor maestro: carga catálogo, verifica unicidad de códigos, ejecuta laboratorios secuencialmente, detiene al primer fallo. |
| [`datos/casos_canonicos.json`](datos/casos_canonicos.json) | Tres casos canónicos (A simétrico SV(3,4), B asimétrico SV(3,5), C heterogéneo SV(3,6)) con θ completo. |

## Prefijos del catálogo de errores

Prefijos **por sumando** de la ecuación absoluta:

| Prefijo | Dominio |
|---|---|
| `W` | canal trabajo factual |
| `Q` | canal calor factual |
| `U` | canal no-clausura proyectada |
| `F` | fuerza factual y descomposición canónica |
| `T` | temperatura factual Θ |
| `L` | entalpía factual Λ |
| `A` | contenido factual total 𝒜 |
| `H` | entropía factual 𝓗 |
| `J` | jacobiano factual 𝒥 |
| `R` | residual factual ℛ |
| `B` | frontera factual ℬ |

Prefijos **estructurales**: `BAL`, `IRR`, `ORT`, `GEN`, `PAR`, `EXH`, `EXC`,
`DIM`, `TRA`, `CHI`, `CEL`, `APP`, `PRN`, `MET`.

Prefijos de **prohibiciones canónicas** del §2: `P1` (tiempo soberano), `P2`
(probabilidad fundante), `P3` (estadística sustituta), `P4` (coordenada externa),
`P5` (constantes ajenas), `P6` (cuarto polo ternario).

Prefijos de **ejecución**: `LAB`, `CFG`, `IO`.

## Autocontención

Los laboratorios asumen sólo que el intérprete Python tiene acceso a `numpy`.
Todas las rutas son relativas a la propia carpeta `laboratorios/`. La ejecución
no depende del directorio de trabajo ni del entorno exterior: `python3 runner.py`
desde cualquier shell produce los mismos resultados.
