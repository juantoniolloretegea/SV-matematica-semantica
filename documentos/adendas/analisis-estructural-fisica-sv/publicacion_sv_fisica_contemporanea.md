# Medición, reconstrucción e incertidumbre estructural en la física contemporánea sin probabilidad ni tiempo soberano: un marco analítico basado en sucesos y trayectorias con laboratorios ejecutables

## Measurement, Reconstruction and Structural Uncertainty in Contemporary Physics Without Probability or Sovereign Time: An Event- and Trajectory-Based Analytical Framework with Executable Laboratories

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Lugar y fecha:** Madrid, 2026

---

## Resumen

Este trabajo presenta un marco analítico operativo para el estudio de problemas característicos de la física experimental contemporánea —medición, reconstrucción e incertidumbre estructural— sin recurrir a la probabilidad ni al tiempo como primitivas soberanas. En su lugar, los procesos físicos se describen mediante sucesos y trayectorias factuales ordenadas, residuales estructurales, fronteras explícitas de clausura y criterios conservadores de dictamen.

El interés del enfoque aparece en situaciones distintas y reconocibles para el investigador. En metrología, permite separar una calibración estructuralmente válida de otra que depende de una reducción previa que ha destruido información relevante. En reconstrucción electromagnética, permite distinguir entre una reconstrucción completa, una truncación con pérdida controlada y un borde irreductible que obliga a mantener abierta la clausura. En análisis multidetector, permite diferenciar entre coincidencia suficiente, conflicto parcial de lecturas y discrepancia estructural no resoluble sin introducir cierres artificiales. En física de partículas, permite tratar la identificación ambigua de entidades físicas y la coexistencia de hipótesis compatibles sin convertirlas de forma prematura en una decisión única. En la frontera cuántica, permite formalizar la no clausura, la dependencia del orden de medición y los límites de observabilidad sin degradarlos a mera insuficiencia instrumental.

El objetivo del marco no es sustituir las teorías físicas vigentes, sino ofrecer una capa analítica adicional allí donde la reconstrucción es incompleta, aparecen residuales persistentes, existe desacuerdo entre lecturas o la clausura no puede justificarse con rigor suficiente. Sobre un núcleo algebraico mínimo se construye una arquitectura operativa que incluye herramientas de análisis, laboratorios reproducibles, una implementación local verificable y una guía de uso orientada al investigador. Se presentan desarrollos en metrología factual, reconstrucción electromagnética, análisis multidetector, tratamiento estructural de la ambigüedad y no clausura con reapertura trazable cuando el cierre no resulta legítimo.

El artículo se acompaña de un conjunto reproducible de trabajo. En él, texto, interfaz web, datasets, laboratorios, runner y pruebas mínimas quedan reunidos en un mismo bloque ejecutable. El alcance corresponde a una validación estructural y laboratorial controlada, con distinta madurez según dominios, y establece una base para reejecuciones posteriores sobre contextos experimentales más amplios.

## Abstract

This work presents an operational analytical framework for the study of characteristic problems in contemporary experimental physics—measurement, reconstruction and structural uncertainty—without relying on probability or time as foundational primitives. Instead, physical processes are described through ordered factual events and trajectories, structural residuals, explicit closure boundaries and conservative decision criteria.

The relevance of the approach becomes apparent in a range of situations familiar to experimental researchers. In metrology, it separates a structurally valid calibration from one that depends on prior reduction steps that destroy relevant information. In electromagnetic reconstruction, it distinguishes between complete reconstruction, controlled truncation loss and irreducible boundary effects that prevent legitimate closure. In multi-detector analysis, it distinguishes between sufficient coincidence, partial detector conflict and structurally unresolved discrepancy without forcing artificial closure. In particle physics, it addresses ambiguous identification and the coexistence of compatible hypotheses without prematurely collapsing them into a single decision. At the quantum boundary, it formalizes non-closure, measurement-order dependence and observability limits without reducing them to mere instrumental insufficiency.

The framework does not aim to replace established physical theories, but to provide an additional analytical layer where reconstruction is incomplete, residual structure persists, readings disagree or closure cannot be rigorously justified. A minimal algebraic core supports an operational architecture that includes analytical tools, reproducible laboratories, a verifiable local implementation and a practical guide for researchers. Developments are presented in factual metrology, electromagnetic reconstruction, multi-detector analysis, ambiguity-sensitive evaluation and traceable reopening when closure is not legitimate.

The article is accompanied by a reproducible working set in which text, web interface, datasets, laboratories, runner and minimal tests are gathered in a single executable block. Its scope corresponds to structural and controlled laboratory validation, with different maturity levels across domains, and establishes a basis for later re-execution in broader experimental settings.

## 1. Introducción

La práctica experimental en física contemporánea se enfrenta de forma recurrente a situaciones en las que la medición no conduce de manera inmediata a una clausura legítima del fenómeno observado. Un detector puede registrar una señal compatible con varias interpretaciones físicas y no ofrecer base suficiente para decidir entre ellas. Una reconstrucción modal puede reproducir con precisión la mayor parte de una señal y conservar, sin embargo, un borde irreductible que impide declarar cierre completo. Dos instrumentos pueden coincidir sólo parcialmente ante un mismo suceso y dejar abierto si se trata de concordancia suficiente o de conflicto estructural. Una cadena de calibración puede producir un resultado aparentemente correcto, aunque una reducción previa haya eliminado parte de la información necesaria para sostenerlo con rigor. En física de partículas, un conjunto de observables puede seguir siendo compatible con más de una identidad física; en el dominio cuántico, el orden de medición y el límite de observabilidad pueden impedir que la no clausura sea tratada como un simple déficit instrumental (BIPM, 2019; JCGM, 2008; Jackson, 1999; Griffiths, 2017; Griffiths, 2008; Olive et al., 2020; Dirac, 1981; von Neumann, 1955; Sakurai & Napolitano, 2017).

Los procedimientos habituales responden a estas dificultades mediante inferencia probabilística, ajuste estadístico, criterios de optimización o clasificación por verosimilitud. Tales procedimientos han mostrado una utilidad práctica indiscutible y forman parte del instrumental ordinario de la física actual. Sin embargo, su eficacia no elimina una cuestión más básica: hay situaciones en las que el resultado obtenido depende en parte de la forma de cálculo adoptada y no sólo de la estructura del fenómeno. Cuando esto ocurre, conviene separar dos planos: la utilidad operativa del procedimiento y la legitimidad estructural de la clausura que produce (JCGM, 2008; Taylor, 1997; Oppenheim & Schafer, 2010).

Este trabajo se sitúa en ese segundo plano. Su punto de partida es que existen contextos en los que la no clausura no es un accidente provisional ni una mera carencia de datos, sino una propiedad estructural del problema. Si dos lecturas ofrecen coincidencia parcial pero no plenamente consistente, la respuesta científicamente más rigurosa puede no ser una decisión forzada, sino la conservación explícita de esa indeterminación. Si una reconstrucción truncada conserva un residual persistente en el borde, el resultado correcto puede no ser una aproximación cerrada, sino el reconocimiento formal de un límite de representación. Si dos tipos de entidad física siguen siendo compatibles con el mismo conjunto de observables, el sistema debe poder expresar esa ambigüedad sin degradarla a una heurística de conveniencia.

Con este propósito se propone un marco analítico que describe procesos físicos mediante sucesos y trayectorias factuales ordenadas, sin recurrir a la probabilidad ni al tiempo como primitivas soberanas. La idea central es sencilla en su formulación y exigente en sus consecuencias: un proceso puede analizarse como una sucesión explícita de estados y transformaciones, de modo que cada paso conserve trazabilidad, cada discrepancia quede registrada como residual estructural y cada intento de clausura dependa de una frontera declarada, no de una presión de completitud. En este marco, la pregunta decisiva deja de ser “qué resultado produce el procedimiento” y pasa a ser “si la estructura disponible autoriza realmente ese resultado”.

La propuesta se apoya en cuatro nociones principales. La primera es la trayectoria factual, que ordena el proceso sin convertir el tiempo en fundamento. La segunda es el residual estructural, que permite medir discrepancias sin reducirlas a error estadístico ni a ruido indiferenciado. La tercera es la frontera de clausura, que establece bajo qué condiciones una trayectoria puede considerarse suficientemente determinada. La cuarta es un dictamen conservador, capaz de distinguir entre clausura legítima, no clausura y reapertura necesaria. Un sistema analítico científicamente útil no debe limitarse a decidir; debe saber cuándo no puede decidir sin violentar la estructura del problema.

Este artículo no pretende sustituir las teorías físicas vigentes ni presentar una teoría total de la física. Su objetivo es más preciso: ofrecer una capa analítica adicional allí donde los procedimientos habituales producen clausuras cuya legitimidad estructural no es evidente, o allí donde la indeterminación debe ser preservada en lugar de disuelta. Por ello, el marco se desarrolla junto con herramientas de análisis, laboratorios reproducibles, una implementación local y procedimientos de uso orientados a reejecución. La intención no es proponer una doctrina abstracta, sino construir un instrumento de trabajo sometible a verificación material.

## 2. Estatuto, alcance y conjunto reproducible

El presente texto tiene rango de documento analítico aplicado. No funda una teoría física nueva ni desplaza la autoridad de la física establecida. Tampoco se presenta como sustituto de los formalismos numéricos, probabilísticos o temporales que dominan la práctica experimental contemporánea. Su función es más restringida y más exigente: introducir una capa adicional de evaluación estructural allí donde la clausura del análisis no puede darse por legítima sólo por el hecho de que exista un resultado computable.

El trabajo debe leerse junto con el conjunto reproducible que lo acompaña. Ese conjunto no es decorativo ni externo a la argumentación; contiene la materialización mínima de lo que aquí se afirma. Su organización operativa se articula, al menos, en los siguientes planos:

| Componente | Función material |
|---|---|
| [`publicacion_sv_fisica_contemporanea.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/publicacion_sv_fisica_contemporanea.md) | texto base para publicación y revisión editorial |
| [`analisis-estructural-fisica-sv/`](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/) | entrada pública y navegación pública del conjunto |
| [metrología](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/metrologia.html), [electromagnetismo](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/electromagnetismo.html), [multidetector](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/multidetector.html), [partículas](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/particulas.html) y [no clausura](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/no-clausura.html) | acceso navegable a los dominios y trazabilidad del conjunto |
| [`entorno_local/README_local.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/README_local.md) | runner, núcleo Python, datasets, laboratorios y pruebas mínimas |
| [`implementacion/implementacion-local.html`](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/implementacion/implementacion-local.html) | contrato operativo resumido para reejecución |
| [`errores/catalogo-ffsv.html`](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/errores/catalogo-ffsv.html) | catálogo de errores publicado del entorno local |
| [`tests/plan-verificacion.html`](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/tests/plan-verificacion.html) | plan mínimo de verificación material |

El conjunto es autocontenido en sentido operativo, no en sentido ontológico. Esto significa que el lector dispone, en un mismo bloque, del texto, de la interfaz de exploración, de los datasets, de los laboratorios, del runner y de pruebas mínimas suficientes para reejecutar los casos controlados. No significa que el marco quede validado de una vez y para siempre sobre todos los contextos experimentales posibles.

Su alcance actual corresponde a validación estructural y laboratorial controlada. Los dominios no presentan el mismo grado de madurez. La metrología factual y el núcleo transversal de trayectoria, residual, frontera y dictamen son los sectores más cerrados del paquete. Los dominios electromagnético, multidetector, de ambigüedad en física de partículas y de no clausura representan, en esta versión, validaciones estructurales controladas mediante casos discretizados y no herramientas generales de resolución física.

## 3. Núcleo analítico mínimo

### 3.1. Sucesos y trayectorias

#### 3.1.1. Formulación física conocida

En física, la descripción de la evolución de un sistema se expresa de forma habitual mediante una parametrización temporal. En su forma más general, un estado físico se escribe como:

$$
x(t)
$$

y su dinámica se establece a través de ecuaciones diferenciales del tipo:

$$
\frac{d x(t)}{dt} = F(x(t), t)
$$

En el caso de sistemas ondulatorios, esta dependencia adopta formas como la ecuación de onda:

$$
\frac{\partial^2 \psi}{\partial t^2} = c^2 \nabla^2 \psi
$$

En análisis experimental, esta estructura se traduce en series temporales de señal, reconstrucciones dependientes del tiempo, sincronización entre detectores y correlaciones temporales entre eventos (Arnold, 1989; Oppenheim & Schafer, 2010).

#### 3.1.2. Límite estructural de la formulación

Esta formulación presenta limitaciones en contextos experimentales concretos. Existen situaciones en las que el tiempo no es accesible como variable directa, sino sólo como reconstrucción derivada de los propios datos. Además, la parametrización temporal puede ocultar la estructura real de la transición entre estados. Dos procesos con la misma dependencia temporal pueden corresponder a secuencias físicas distintas si los estados intermedios no son equivalentes. Cuando la reconstrucción es incompleta, la continuidad temporal no garantiza por sí sola la legitimidad de la trayectoria.

#### 3.1.3. Reformulación en el marco propuesto

Para evitar esta dependencia, se introduce una descripción basada en **sucesos** y **trayectorias factuales**:

$$
T = (S_0, \varepsilon_0, S_1, \varepsilon_1, \dots, S_n)
$$

donde:
- $S_i$ representa un estado físico accesible o reconstruido;
- $\varepsilon_i$ representa un suceso o transformación explícita entre estados.

El orden de la trayectoria no se apoya en una variable temporal continua, sino en la relación estructural entre estados y sucesos.

### 3.2. Residual estructural

En física experimental, la discrepancia entre un estado observado y su reconstrucción se expresa habitualmente mediante magnitudes de error o desviación. El marco propuesto reformula esa discrepancia como **residual estructural**, no como error a minimizar. Dado un paso de trayectoria:

$$
S_i \xrightarrow{\varepsilon_i} S_{i+1}
$$

se define un residual:

$$
R(S_i, S_{i+1})
$$

que no se reduce a una magnitud escalar única, sino que se interpreta como una estructura de diferencia entre estados. Este residual puede contener componentes debidas a truncación, borde, incompatibilidades entre representaciones o información no capturada por el modelo aplicado.

### 3.3. Frontera de clausura

La clausura no se determina por un umbral implícito, sino por una **frontera de clausura explícita**. Dada una trayectoria:

$$
T = (S_0, \varepsilon_0, \dots, S_n)
$$

se define una función de frontera:

$$
F(T)
$$

que evalúa si la trayectoria puede considerarse cerrada en términos estructurales. En la implementación reproducible incluida en este conjunto, la frontera se calcula a partir de la clasificación ternaria derivada de los residuales entre estados consecutivos. Las transformaciones y el horizonte declarado se conservan en la traza del análisis y sirven para contextualizar y reproducir el caso, pero no alteran todavía el operador efectivo de frontera en esta versión.

### 3.4. Sensibilidad factual y jacobiano estructural

Las herramientas diferenciales conocidas se amplían aquí a una sensibilidad definida sobre trayectorias y no únicamente sobre funciones. Dada una trayectoria:

$$
T = (S_0, \varepsilon_0, \dots, S_n)
$$

se considera una perturbación:

$$
\delta T
$$

que puede afectar a los estados, a las transformaciones o a las condiciones de contorno. El marco general admite esas tres vías. En la implementación reproducible actual, el **jacobiano estructural** se realiza sobre los estados numéricos de la trayectoria mediante perturbaciones explícitas de magnitud declarada. Para cada estado numérico $S_i$, se evalúa si una perturbación $\varepsilon$ produce un cambio en el dictamen global. Los estados de tipo $U$ no son perturbables. El resultado es un registro de los estados sensibles y de la variación de dictamen asociada a cada perturbación. Esta implementación se recoge en el módulo `core/jacobian.py` del entorno local.

### 3.5. Clasificación local y dictamen global

Se introduce una distinción explícita entre **clasificación local** y **dictamen global**.

En la implementación reproducible de esta versión, cada transición entre estados consecutivos se evalúa mediante una clasificación ternaria derivada del residual estructural:

$$
C \in \{0, 1, U\}
$$

donde:
- $1$ indica validez estructural;
- $0$ indica no validez estructural;
- $U$ indica que la información disponible no permite decidir.

A partir de la clasificación local y del análisis de la trayectoria completa, se emite un dictamen global:

$$
D(T) \in \{\text{APTO}, \text{INDETERMINADO}, \text{NO APTO}\}
$$

### 3.6. Reapertura factual y trazabilidad

La revisión de un resultado se formaliza como **reapertura factual** de la trayectoria, no como sustitución. Dada una trayectoria:

$$
T = (S_0, \varepsilon_0, \dots, S_n)
$$

la incorporación de nueva información o la modificación de condiciones da lugar a una extensión:

$$
T \longrightarrow T'
$$

donde $T'$ contiene a $T$ como subestructura:

$$
T \subseteq T'
$$

La reapertura no corrige un suceso ya fijado ni lo sustituye; añade nuevos sucesos soberanos a la trayectoria y conserva íntegra la trazabilidad de los anteriores.

## 4. Herramientas desarrolladas

### 4.1. Herramienta metrológica factual

La herramienta metrológica factual no trata la medición como una operación instantánea, sino como una **trayectoria de medición y transformación**. Se parte de una estructura del tipo:

$$
T = (S_0, \varepsilon_0, S_1, \varepsilon_1, \dots, S_n)
$$

La herramienta se organiza sobre cinco elementos: equivalencia metrológica factual, trayectoria de transformación, residual estructural, frontera de validación y dictamen global. La comparación estructural de estados se realiza sobre representaciones normalizadas a una unidad base común. Esto garantiza que una conversión metrológicamente correcta —cuyo residual en la unidad base es cero— produce dictamen APTO, mientras que una reducción con pérdida de información produce residual positivo y dictamen NO APTO. El trasfondo metrológico clásico de esta exigencia, aunque aquí se reformule fuera del régimen probabilístico, sigue siendo reconocible en la disciplina de unidades y en la expresión rigurosa de la incertidumbre de medida (BIPM, 2019; JCGM, 2008; Taylor, 1997).

### 4.2. Herramienta de trayectorias, residualidad, frontera y dictamen

Esta herramienta constituye el **núcleo instrumental transversal** del sistema. Trata el análisis como un objeto estructurado completo. Se define una trayectoria factual y sobre ella se aplican de forma integrada cuatro operadores: trayectoria, residual estructural, frontera de clausura y dictamen global. En la versión reproducible aquí presentada, ese núcleo trabaja sobre secuencias finitas de estados y clasifica la clausura a partir de residuales consecutivos; no resuelve todavía, por sí solo, compatibilidades más ricas entre transformaciones ni horizontes de dominio. Su función es responder no sólo a “qué resultado aparece”, sino a “qué estructura mínima sostiene ese resultado y autoriza su aceptación”.

### 4.3. Herramienta electromagnética factual

La herramienta electromagnética factual reformula la reconstrucción de campos y señales en términos de trayectorias de estados del campo, sucesos de transformación, residuales estructurales, fronteras de clausura y dictamen global. En el paquete reproducible, esta herramienta queda representada por casos controlados de reconstrucción completa, truncación, borde y conflicto estructural, y no por un solver electromagnético general. El trasfondo físico del dominio se apoya en la teoría electromagnética y en la reconstrucción modal clásica (Jackson, 1999; Griffiths, 2017; Bracewell, 2000).

### 4.4. Herramienta de coincidencia multidetector

La herramienta de coincidencia multidetector aborda escenarios en los que varias lecturas deben evaluarse conjuntamente sin forzar una clausura por mera proximidad aparente. En el marco general, cada detector puede describirse mediante una trayectoria propia y la coincidencia debe decidirse por compatibilidad estructural y no sólo por correlación numérica. En el paquete reproducible actual, esta idea se implementa mediante casos discretizados predeclarados —coincidencia completa, coincidencia parcial, correlación aparente, conflicto estructural y no clausura— y no como un motor general de fusión de detectores.

### 4.5. Herramienta de análisis bajo ambigüedad (física de partículas)

El conjunto de hipótesis físicas se trata como un **conjunto finito de trayectorias compatibles o incompatibles**, no como alternativas que deban colapsar necesariamente en una única decisión. En la versión reproducible, la herramienta evalúa casos controlados de identificación unívoca, ambigüedad estructural, hipótesis dominante con alternativa residual abierta, conflicto e irreductibilidad. La ambigüedad no se elimina por principio; se declara y se conserva cuando la estructura disponible no autoriza cierre único (Griffiths, 2008; Olive et al., 2020; Thomson, 2013).

### 4.6. Herramienta de no clausura y frontera cuántica

En la física cuántica existen situaciones en las que la no clausura no es un defecto del análisis, sino una propiedad estructural del sistema. La herramienta trata estos casos como **no clausura estructural**, representada mediante $U$ y reflejada en el dictamen global como **INDETERMINADO** cuando la estructura no permite una clausura legítima. En el paquete reproducible, esto se ensaya mediante casos mínimos de orden de medición, límite de observabilidad, no clausura irreductible, clausura forzada y reapertura factual. No se presenta como teoría cuántica cerrada ni como sustitución de la formulación estándar (Dirac, 1981; von Neumann, 1955; Heisenberg, 1958; Sakurai & Napolitano, 2017).

## 5. Laboratorios ejecutables

### 5.1. Marco y función de los laboratorios

El presente bloque somete las herramientas desarrolladas a **validación estructural controlada** mediante laboratorios reproducibles. Su función no consiste en sustituir la validación experimental completa en entornos físicos abiertos, sino en verificar, bajo condiciones explícitas, que el marco propuesto conserva trazabilidad, distingue entre clausura legítima y clausura forzada, trata correctamente el residual, preserva la no clausura cuando es necesaria y permite reapertura sin reescritura.

### 5.2. Laboratorios metrológicos

Los laboratorios metrológicos verifican que el sistema distingue entre equivalencia metrológica estructural y reducción con pérdida de información. Se implementan y verifican los cinco casos siguientes, con el dictamen esperado en cada uno: equivalencia ideal (APTO), reducción con pérdida estructural (NO APTO), compensación aparente con paso indeterminado (INDETERMINADO), incompatibilidad dimensional (NO APTO) y no clausura metrológica (INDETERMINADO). Cada caso fija estados, transformación y dictamen esperado; el laboratorio verifica que el sistema produce exactamente ese dictamen.

### 5.3. Laboratorios electromagnéticos

Este conjunto somete la herramienta electromagnética factual a validación estructural controlada. Se implementan cinco casos verificados: reconstrucción completa (APTO), truncación controlada con pérdida modal (NO APTO), residual de borde con clausura abierta (INDETERMINADO), conflicto estructural entre campo medido y reconstruido (NO APTO) y no clausura electromagnética (INDETERMINADO).

### 5.4. Laboratorios de coincidencia multidetector

Estos laboratorios validan la herramienta de coincidencia multidetector en escenarios de lectura distribuida. Se implementan cinco casos: coincidencia completa entre tres detectores (APTO), coincidencia parcial con tercer detector indeterminado (INDETERMINADO), correlación aparente en la que dos detectores coinciden pero el tercero los contradice y revela que la coincidencia no es estructural (NO APTO), conflicto estructural entre detectores (NO APTO) y no clausura multidetector (INDETERMINADO).

### 5.5. Laboratorios de ambigüedad en física de partículas

Se implementan cinco casos de identificación y ambigüedad: identificación unívoca (APTO), ambigüedad estructural con dos hipótesis compatibles (INDETERMINADO), hipótesis dominante con alternativa residual abierta (INDETERMINADO), conflicto entre hipótesis mutuamente incompatibles (NO APTO) y no clausura bajo ambigüedad irreductible (INDETERMINADO). El sistema preserva la coexistencia de hipótesis compatibles y no colapsa prematuramente la indeterminación.

### 5.6. Laboratorios de no clausura

Este conjunto cierra el bloque laboratorial con cinco casos: determinación parcial con estado irresuelto (INDETERMINADO), dependencia del orden de medición (INDETERMINADO), no clausura irreductible constitutiva del fenómeno (INDETERMINADO), clausura forzada sobre estados incompatibles (NO APTO) y reapertura factual con nueva información. Este último caso emplea explícitamente el operador de reapertura: extiende la trayectoria sin reescribir el pasado y preserva la trazabilidad íntegra de los sucesos anteriores.

## 6. Guía práctica para el investigador

La guía traduce el marco desarrollado a un uso operativo directo. El investigador debe:
1. definir estados iniciales;
2. declarar transformaciones;
3. fijar el horizonte de análisis;
4. construir la trayectoria;
5. evaluar el residual;
6. clasificar localmente;
7. evaluar la frontera;
8. emitir dictamen;
9. reabrir si procede.

El sistema no debe interpretarse como mecanismo de decisión automática, sino como estructura, trazabilidad y criterio de legitimidad.

## 7. Implementación local y arquitectura operativa

La implementación materializa el sistema de forma autónoma y reproducible. Se organiza en cinco módulos principales:
1. constructor de trayectorias;
2. evaluador de residuales;
3. evaluador de frontera;
4. clasificador y dictaminador;
5. gestor de reapertura y trazabilidad.

Se fija un contrato mínimo de entrada y salida, un runner reproducible y un catálogo de errores `FFSV-*`. La entrada admite un caso directo con `states`, `transforms` y `horizon`, así como el sobre JSON exportado desde la web con claves `input` y `result`. En el contrato JSON validado, `horizon.domain` es obligatorio. Los archivos `*_casos.json` reúnen baterías de casos; los `*_minimo.json`, casos unitarios. En esta versión, el runner emite de forma directa `FFSV-001`, `FFSV-002`, `FFSV-004`, `FFSV-005` y `FFSV-006`; `FFSV-003` queda reservado para compuertas superiores de evaluación de frontera. `transforms` y `horizon` se conservan en la traza y en la reejecución, pero el operador efectivo de frontera sigue calculándose a partir de la clasificación de residuales entre estados consecutivos. La implementación no optimiza, no ajusta, no decide por probabilidad y no elimina el residual.

## 8. Evaluación externa, límites y alcance

Desde una perspectiva externa, el sistema aporta una evaluación estructural explícita del análisis físico, separada de su formulación numérica o probabilística. Los elementos de mayor madurez son el núcleo analítico mínimo, la herramienta transversal, la herramienta metrológica y su validación en laboratorios controlados. Otros dominios —electromagnetismo, coincidencia multidetector, ambigüedad en física de partículas y no clausura— presentan mayor dependencia del contexto y requieren integración más amplia con datos experimentales y contrastes externos.

El sistema no sustituye modelos físicos, no es un método predictivo y no resuelve por sí mismo la indeterminación estructural. Su función es evaluar la legitimidad del cierre o de la no clausura sobre trayectorias y casos declarados.

## 9. Conclusiones

El presente trabajo ha desarrollado un marco analítico orientado a evaluar la **legitimidad estructural de determinados resultados en física contemporánea**, sin recurrir a probabilidad ni a tiempo como principios soberanos.

Se ha establecido un núcleo analítico mínimo basado en trayectorias de estados, sucesos no reescribibles, residual estructural, frontera de clausura explícita, clasificación ternaria y dictamen global. A partir de este núcleo se han desarrollado herramientas operativas y laboratorios controlados que muestran que el sistema no fuerza cierres indebidos, conserva el residual, mantiene la indeterminación cuando es necesaria y distingue entre validez, conflicto y apertura.

La aportación principal del trabajo puede resumirse así: introducir una evaluación estructural explícita del análisis físico, separada de la mera obtención de un resultado numérico o probabilístico. Esto permite distinguir entre resultado y legitimidad, identificar límites reales del sistema y evitar decisiones no justificadas por la estructura disponible.

El conjunto no debe leerse como cierre total de los dominios que explora. Debe leerse como una base operativa verificable, ya capaz de sostener casos controlados y reejecución material, sobre la que podrán exigirse contrastes posteriores de mayor dureza experimental.

## 10. Función material de los laboratorios y trazabilidad pública

Los laboratorios no actúan aquí como ejemplos ornamentales, sino como piezas de contraste material del marco. Cada uno fija un dominio de validación controlada, una implementación local concreta y un conjunto de casos declarados. Para facilitar la inspección pública, se indica en cada caso la página navegable del laboratorio, el fichero de implementación y el dataset principal de casos.

### 10.1. Laboratorio metrológico factual

Este laboratorio verifica que el marco distingue entre equivalencia metrológica estructural, pérdida de información por reducción, compensación aparente, incompatibilidad dimensional y no clausura metrológica. Su función es comprobar que la disciplina de unidades y el residual estructural producen un dictamen conservador sin introducir cierre espurio.

- Página navegable: [laboratorios/metrologia.html](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/metrologia.html)
- Implementación local: [`entorno_local/labs/metrologia_lab.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/labs/metrologia_lab.py)
- Dataset principal: [`entorno_local/datasets/metrologia_casos.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/datasets/metrologia_casos.json)

### 10.2. Laboratorio electromagnético factual

Este laboratorio ensaya reconstrucción completa, truncación con pérdida modal, residual de borde, conflicto estructural entre campo medido y reconstruido y no clausura electromagnética. Su función no es resolver electromagnetismo general, sino verificar que el marco conserva el residual y no blanquea cierres allí donde la reconstrucción queda estructuralmente abierta.

- Página navegable: [laboratorios/electromagnetismo.html](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/electromagnetismo.html)
- Implementación local: [`entorno_local/labs/electromagnetismo_lab.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/labs/electromagnetismo_lab.py)
- Dataset principal: [`entorno_local/datasets/electromagnetismo_casos.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/datasets/electromagnetismo_casos.json)

### 10.3. Laboratorio de coincidencia multidetector

Este laboratorio contrasta coincidencia completa, coincidencia parcial, correlación aparente, conflicto estructural y no clausura entre detectores. Su función es verificar que la proximidad entre lecturas no se confunda automáticamente con coincidencia estructural suficiente.

- Página navegable: [laboratorios/multidetector.html](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/multidetector.html)
- Implementación local: [`entorno_local/labs/multidetector_lab.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/labs/multidetector_lab.py)
- Dataset principal: [`entorno_local/datasets/multidetector_casos.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/datasets/multidetector_casos.json)

### 10.4. Laboratorio de ambigüedad en física de partículas

Este laboratorio verifica identificación unívoca, ambigüedad estructural, hipótesis dominante con alternativa residual, conflicto entre hipótesis incompatibles y no clausura bajo ambigüedad irreductible. Su función es preservar la coexistencia de trayectorias compatibles cuando la estructura observacional no autoriza colapso prematuro.

- Página navegable: [laboratorios/particulas.html](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/particulas.html)
- Implementación local: [`entorno_local/labs/particulas_lab.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/labs/particulas_lab.py)
- Dataset principal: [`entorno_local/datasets/particulas_casos.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/datasets/particulas_casos.json)

### 10.5. Laboratorio de no clausura y reapertura factual

Este laboratorio verifica determinación parcial con estado irresuelto, dependencia del orden de medición, no clausura irreductible, clausura forzada sobre estados incompatibles y reapertura factual con nueva información. Su función específica es comprobar que el operador de reapertura extiende la trayectoria sin reescribir el pasado y preserva la trazabilidad material de los sucesos previos.

- Página navegable: [laboratorios/no-clausura.html](https://juantoniolloretegea.github.io/SV-matematica-semantica/analisis-estructural-fisica-sv/laboratorios/no-clausura.html)
- Implementación local: [`entorno_local/labs/no_clausura_lab.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/labs/no_clausura_lab.py)
- Dataset principal: [`entorno_local/datasets/no_clausura_casos.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/analisis-estructural-fisica-sv/entorno_local/datasets/no_clausura_casos.json)

## 11. Bibliografía (formato APA 7)

Arnold, V. I. (1989). *Mathematical methods of classical mechanics* (2nd ed.). Springer.

BIPM. (2019). *The international system of units (SI)* (9th ed.). Bureau International des Poids et Mesures.

Born, M., & Wolf, E. (1999). *Principles of optics* (7th ed.). Cambridge University Press.

Bracewell, R. N. (2000). *The Fourier transform and its applications* (3rd ed.). McGraw-Hill.

Dirac, P. A. M. (1981). *The principles of quantum mechanics* (4th ed.). Oxford University Press.

Griffiths, D. (2008). *Introduction to elementary particles* (2nd ed.). Wiley-VCH.

Griffiths, D. J. (2017). *Introduction to electrodynamics* (4th ed.). Cambridge University Press.

Heisenberg, W. (1958). *Physics and philosophy: The revolution in modern science*. Harper & Row.

Jackson, J. D. (1999). *Classical electrodynamics* (3rd ed.). Wiley.

JCGM. (2008). *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*.

Lang, S. (2002). *Algebra* (revised 3rd ed.). Springer.

Lloret Egea, J. A. (2026). *Conjunto matemático de orden, directriz y cambio factual en el Sistema Vectorial SV*. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA).

Lloret Egea, J. A. (2026). *Sucesos, horizontes y cambio estructural: Una aproximación algebraica desde el Sistema Vectorial SV*. ITVIA.

Lloret Egea, J. A. (2026). *Nueva matemática y física factual del Sistema Vectorial SV*. ITVIA.

Mallat, S. (2009). *A wavelet tour of signal processing* (3rd ed.). Academic Press.

Olive, K. A., et al. (Particle Data Group). (2020). Review of particle physics. *Progress of Theoretical and Experimental Physics*, 2020(8), 083C01.

Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-time signal processing* (3rd ed.). Prentice Hall.

Rudin, W. (1976). *Principles of mathematical analysis* (3rd ed.). McGraw-Hill.

Sakurai, J. J., & Napolitano, J. (2017). *Modern quantum mechanics* (2nd ed.). Cambridge University Press.

Simon, H. A. (1996). *The sciences of the artificial* (3rd ed.). MIT Press.

Taylor, J. R. (1997). *An introduction to error analysis* (2nd ed.). University Science Books.

Thomson, M. (2013). *Modern particle physics*. Cambridge University Press.

von Neumann, J. (1955). *Mathematical foundations of quantum mechanics*. Princeton University Press.

## 12. Palabras clave

medición estructural; trayectoria factual; residual estructural; frontera de clausura; indeterminación estructural; análisis sin probabilidad; física contemporánea; reconstrucción de señal; coincidencia multidetector; ambigüedad en física de partículas; no clausura.
