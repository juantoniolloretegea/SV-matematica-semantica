# Conjunto laboratorial reproducible — Teoría del TODO y de la NADA en el Sistema Vectorial SV

**Documento canónico vinculado:** [Teoría del TODO y de la NADA en el Sistema Vectorial SV](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv)

**Autor:** Juan Antonio Lloret Egea — ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)
**Editor:** IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español, ITVIA) — ISSN 2695-6411
**Licencia:** CC BY-NC-ND 4.0 — Protegida por [CEDRO](https://www.cedro.org/english?lng=en)
**© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.**

---

## Cláusula de subordinación

El conjunto laboratorial está **subordinado** al documento canónico fijado. Su función exclusiva es **verificar y cotejar** por cómputo determinista los enunciados del documento canónico. No introduce contenido doctrinal nuevo, no extiende, no reescribe y no propone. Si un laboratorio detectara un fallo de cotejo o un error material, lo reporta sin tocar el documento canónico.

---

## Estructura del conjunto

```
laboratorios/
├── README.md                                 [este archivo]
├── runner.py                                 [runner agregado]
├── catalogo_errores.md                       [códigos E1..E7]
├── sv_lib.py                                 [biblioteca compartida]
├── lab01_alfabeto_y_celula.py
├── lab02_suceso_admisible.py
├── lab03_distancia_factual_fibrosa.py
├── lab04_agotamiento_K3n.py
├── lab05_frontera_mu_lambda.py
├── lab06_componentes_ciclo_q.py
├── lab07_normalizacion_zeta.py
├── lab08_verificador_ternario_fuerte.py
├── lab09_absorcion_canonica.py
├── lab10_ley_canonica_rectora.py
├── lab11_mapa_absorcion.py
├── lab12_banco_diez_supuestos.py
├── lab13_tabla_cruzada_once_absorciones.py
├── lab14_cinco_interpretaciones.py
└── lab15_validador_total.py
```

## Catálogo de los quince laboratorios canónicos

| ID | Laboratorio | Sección doctrinal | Criterio de aptitud (E7 = 0) |
|---|---|---|---|
| 1 | `lab01_alfabeto_y_celula.py` | §2.1 | enumeración exhaustiva de K₃ⁿ |
| 2 | `lab02_suceso_admisible.py` | §2.4 | A1-A6 todas verdaderas |
| 3 | `lab03_distancia_factual_fibrosa.py` | §§2.7-2.8, 8 | coherencia telescópica con monotonía |
| 4 | `lab04_agotamiento_K3n.py` | §9 | Im(v) △ K₃ⁿ = ∅ |
| 5 | `lab05_frontera_mu_lambda.py` | §10 | (μ, λ) = (0, 0) simultáneo |
| 6 | `lab06_componentes_ciclo_q.py` | §12 | cinco componentes a 0 |
| 7 | `lab07_normalizacion_zeta.py` | §13.1 | tres ramas correctas |
| 8 | `lab08_verificador_ternario_fuerte.py` | §§13.3-13.5 | 27 entradas con cardinal canónico (1, 19, 7) |
| 9 | `lab09_absorcion_canonica.py` | §14 | Δᵀᴼᴰᴼ_D = 0 sobre dominios admisibles |
| 10 | `lab10_ley_canonica_rectora.py` | §15 | 𝓔★_TODO,SV = 0 sobre entrada de cierre |
| 11 | `lab11_mapa_absorcion.py` | §18 | 𝔘ᵘⁿⁱᶠ_SV = 0 ⟺ 14 componentes nulos |
| 12 | `lab12_banco_diez_supuestos.py` | §20 | 10 supuestos del banco con dictamen 0 |
| 13 | `lab13_tabla_cruzada_once_absorciones.py` | §21 | 110 celdas con Δʳᵉˢ = 0,00 |
| 14 | `lab14_cinco_interpretaciones.py` | §22 | 5 veredictos con prelación 1 ≻ U ≻ 0 |
| 15 | `lab15_validador_total.py` | §§18-23 | seis subverificadores nulos |

## Estructura tipada de salida

Por el §24.2 del documento canónico, cada laboratorio produce salida tipada `SV_TODO_NADA_RESULT`:

```python
SV_TODO_NADA_RESULT = {
    "lab_id":     str,
    "section":    str,
    "verdict":    { 0, 1, U },
    "components": [ x_1, x_2, ..., x_m ],   # cada x_i ∈ {0,1,U}
    "trace":      [ ... ],
    "passes_E7":  bool,
}
```

## Aptitud

Por el §24.2 del documento canónico, un laboratorio es **APTO** si y sólo si:

(i) `verdict = 0` sobre la entrada del apartado correspondiente;

(ii) `passes_E7 = True`, donde el código E7 verifica nulidad estricta sobre todos los componentes declarados en la sección de origen.

Un laboratorio es **NO APTO** si `verdict ∈ { 1, U }` sobre la entrada de cierre estructural o si `passes_E7 = False`.

## Invocación

### Ejecución de un laboratorio individual

```bash
python lab01_alfabeto_y_celula.py
```

Produce salida humano-legible por consola con la estructura `SV_TODO_NADA_RESULT` y dictamen APTO / NO APTO.

### Ejecución del runner agregado

```bash
python runner.py
```

Ejecuta los quince laboratorios en orden, imprime tabla resumen y reporta el dictamen global. Salida en formato JSON adicional con `--json`:

```bash
python runner.py --json
```

## Dependencias

Únicamente la biblioteca estándar de Python (versión ≥ 3.10). El módulo `sv_lib.py` es código hermano del propio repositorio canónico, no dependencia externa.

## Catálogo de errores

Códigos canónicos E1-E7 documentados en [`catalogo_errores.md`](./catalogo_errores.md).

## Reproducibilidad

Cada laboratorio es determinista: misma entrada produce misma salida. No utiliza generadores aleatorios, no realiza muestreo, no depende de probabilidad ni de inferencia. Conforme a las prohibiciones constitutivas P.1, P.2 y P.4 del corpus.

## Cláusula de validez vinculante

Este conjunto laboratorial es vinculante exclusivamente cuando está vinculado al documento canónico. Los laboratorios aislados del documento carecen de valor doctrinal: cualquier interpretación, derivación o aplicación que se haga de ellos sin remisión al cuerpo del documento canónico queda fuera del Sistema Vectorial SV.

## Cláusula de prevalencia

En caso de discrepancia, divergencia, errata, omisión o cualquier incoherencia entre el conjunto laboratorial y el cuerpo del documento canónico, **prevalece el cuerpo del documento canónico**. Los laboratorios son subordinados al texto canónico, no al revés.
