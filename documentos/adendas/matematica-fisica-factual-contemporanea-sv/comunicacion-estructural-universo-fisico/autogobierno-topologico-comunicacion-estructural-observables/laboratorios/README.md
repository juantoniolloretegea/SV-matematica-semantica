# Laboratorios — Autogobierno topológico y comunicación estructural de observables

![Portada — Autogobierno topológico y comunicación estructural de observables](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/imagenes/portada.png)

Este directorio contiene los nueve laboratorios reproducibles asociados a la publicación **Autogobierno topológico y comunicación estructural de observables en el Universo físico realizado**.

Los laboratorios verifican consistencia formal. No sustituyen validación física externa. Ningún laboratorio convierte `U` en valor numérico, usa probabilidad como criterio de verdad ni cierra favorablemente por ausencia de contradicción.

## Tabla resumen de laboratorios

| Familia | Laboratorio | Qué verifica | Ejecución |
|---|---|---|---|
| Comparador | L.1. Comparador con realimentación | Ruptura de equipotencialidad y comparador global sin agente externo. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L1_comparador_realimentacion/runner.py) |
| Convergencia y U | L.2. Convergencia asintótica gobernada | No clausura a reposo absoluto y conservación de `U`. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L2_convergencia_asintotica_U/runner.py) |
| Régimen ciclo-distancial | L.3. Topología sin transmisión | Separación entre latencia física y propiedad topológica no propagativa. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L3_regimen_ciclo_distancial/runner.py) |
| Tránsito por dominios | L.4. Ley general del tránsito | Cierre de tránsito sólo con residual nulo en restricciones locales. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L4_transito_dominios/runner.py) |
| Gobierno de observables | L.5. Fórmula universal de observables | Admisión, no admisión o `U` sin cierre impropio. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L5_gobierno_observables/runner.py) |
| Transductores | L.6. Familia `𝓖★TrU(D)` | Legitimidad del transductor por especialización tipada. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L6_transductores/runner.py) |
| Canal y diccionario | L.7. `Diag_AB^⊥` | Consolidación sólo con canal, diccionario, retorno y residual. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L7_canal_diccionario_diag/runner.py) |
| Predominancia | L.8. Compatible y lesiva | Distinción estructural entre asimetría gobernada y captura lesiva. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L8_predominancia/runner.py) |
| Matriz integrada | L.9. Integración completa | Integración sin tiempo rector, sintiencia, transmisión al unísono ni probabilidad fundante. | [runner.py](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables/laboratorios/L9_matriz_integrada/runner.py) |

## Estructura de salida

Cada `runner.py` imprime los campos:

```text
LAB_ID
OBJETO
ENTRADAS
RESTRICCIONES
SALIDA_ESPERADA
SALIDA_OBTENIDA
RESIDUAL
CONDICION_ACEPTACION
RESULTADO
```

## Convención ternaria

Los residuales cierran en `0`: `R=0` significa cierre, `R=1` significa contradicción material o no admisión, y `R=U` conserva indeterminación honesta. Los predicados positivos de consolidación cierran en `1`: `Id_trans^SV=1`, `Canal_AB^Γ=1` o `Diag_AB^⊥=1` significan admisión positiva del predicado.

## Ejecución

Ejecutar todos los laboratorios desde este directorio:

```bash
python run_all.py
```

Ejecutar un laboratorio concreto:

```bash
python L1_comparador_realimentacion/runner.py
```

Las salidas obtenidas por `run_all.py` se escriben en `salidas_obtenidas/`.

---

**Advertencia.** Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física y la Química, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.

***Warning.** This publication is protected by CEDRO. Its application in the field of Physics and Chemistry, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.*

| Url canónica: https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/autogobierno-topologico-comunicacion-estructural-observables |

