# Movilidad estructural y legitimidad de exposición en el Sistema Vectorial SV: formalización de una condición de frontera

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Proyecto:** Sistema Vectorial SV  
**Publicación:** IA eñ ™ — La Biblia de la IA · ISSN 2695-6411  
**Licencia:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)  
**Versión:** 1 · Madrid, 17/03/2026

---

## Resumen

Este trabajo formula una condición de frontera para el Sistema Vectorial SV destinada a resolver un problema que no queda agotado por la semántica estructural ni por la interfaz visual ya publicadas: bajo qué condiciones una trayectoria interna, ya legítimamente constituida, puede adquirir estatuto de exposición externa sin violar los invariantes del sistema. El resultado no constituye una teoría de acción ni un modelo de ejecución física. Su alcance es más austero y, por ello, más exigente: definir una condición necesaria de legitimidad estructural previa a cualquier acoplamiento externo.

La propuesta se formula como un predicado sobre trayectorias finitas y no introduce nuevos valores semánticos ni altera la ontología ternaria del sistema. Se prueban cuatro propiedades mínimas: no trivialidad, dependencia de clausura, sensibilidad a la indeterminación crítica y no composicionalidad fuerte. El trabajo incluye ejemplos formales y un evaluador verificable para grafos finitos dirigidos. Su interés no reside en prometer movilidad física, sino en fijar una frontera mínima entre interior estructural y exteriorización posible.

**Palabras clave:** Sistema Vectorial SV; condición de frontera; legitimidad de exposición; indeterminación estructural; trayectoria; habilitación estructural; semántica ternaria.

---

## Abstract

This work formulates a boundary condition for the SV Vectorial System aimed at resolving a problem not exhausted by the already-published structural semantics or visual interface: under what conditions an internal trajectory, once legitimately constituted, may acquire the status of external exposure without violating the system's invariants. The result does not constitute a theory of action nor a model of physical execution. Its scope is more austere and therefore more demanding: defining a necessary condition of structural legitimacy prior to any external coupling.

The proposal is formulated as a predicate over finite trajectories and introduces no new semantic values nor alters the system's ternary ontology. Four minimal properties are proved: non-triviality, closure dependence, sensitivity to critical indeterminacy, and strong non-compositionality. The work includes formal examples and a verifiable evaluator for finite directed graphs. Its contribution is not to promise physical mobility, but to fix a minimal boundary between structural interior and possible exteriorisation.

**Keywords:** SV Vectorial System; boundary condition; exposure legitimacy; structural indeterminacy; trajectory; structural enablement; ternary semantics.

---

## 1. Introducción

El problema de la movilidad no puede formularse en el Sistema Vectorial SV como un problema directo de ejecución sin romper su jerarquía doctrinal. El sistema, tal como ha sido desarrollado en la semántica estructural y en la interfaz visual, fija con precisión la captura, la admisibilidad, la transducción ternaria, la clausura y la constitución de trayectorias; pero no define por sí mismo una teoría de salida, ni de actuadores, ni de acción física. Por ello, la cuestión correcta no es cómo actúa el sistema, sino cuándo una estructura interna puede exponerse sin dejar de ser semánticamente honesta.

Esta precisión es decisiva. Un sistema puede disponer de estados, de composición y de trayectorias sin que de ello se siga ninguna legitimidad de exteriorización. Si esa transición entre interior y exterior se concede sin criterio, el sistema colapsa en arbitrariedad; si se niega sin análisis, el sistema queda clausurado por exceso. El presente trabajo introduce una solución mínima a ese problema: una **condición estructural de exposición** definida sobre trayectorias ya constituidas.

La tesis del artículo es deliberadamente sobria:

> Existe un predicado estructural sobre trayectorias del SV que permite distinguir entre trayectorias internamente válidas pero no exponibles y trayectorias internamente válidas cuya exposición no contradice, en el sentido mínimo aquí fijado, la semántica del sistema.

El resultado no demuestra movilidad física. Demuestra algo previo y necesario: que puede definirse una frontera formal entre estructura interna y exposición externa sin ampliar el sistema más allá de su ontología ternaria.

---

## 2. Delimitación negativa

Este trabajo no:

1. define una teoría de acción, intención, voluntad o agencia;
2. formaliza actuadores, cinemática, dinámica o control físico;
3. introduce probabilidad, continuidad ni grados semánticos intermedios entre `0`, `1` y `U`;
4. modifica la gramática, la IR ni el validator del lenguaje SV;
5. sustituye ni reabre la semántica estructural ya fijada;
6. pretende competir con marcos completos de robótica o planificación.

Su alcance es estrictamente estructural: fijar una condición de frontera sobre trayectorias ya constituidas.

---

## 3. Marco de partida

Se asume la cadena estructural del SV ya fijada en el corpus \[1–3\]:

```
x ∈ Wⱼ → ϕⱼ → oⱼ → rⱼ → τⱼ → σ → Pⱼ → célula → composición → frame → trayectoria
```

Los términos de esta cadena corresponden a los objetos formales definidos en los documentos del corpus: `x` es el contenido de entrada del dominio; `ϕⱼ` es la función de captura; `oⱼ` la observación resultante; `rⱼ` el resultado de admisibilidad; `τⱼ` la transducción al alfabeto ternario `{0,1,U}`; `σ` la configuración; `Pⱼ` la interfaz paramétrica; y los términos finales la jerarquía compositiva hasta la trayectoria. El presente trabajo comienza en el último término de esa cadena: la **trayectoria**. No reabre la formalización de captura, admisibilidad, transducción o clausura.

Del mismo modo, mantiene el régimen eventivo ya establecido: en SV las transiciones dependen de sucesos pertinentes y no del tiempo como principio constitutivo. El tiempo conserva aquí un papel auxiliar de ordenación o medida, no de fundamento ontológico de la transición.

En esta posición, la pregunta ya no es cómo se constituye una trayectoria, sino qué puede decirse de su posible exteriorización sin recurrir a información ajena a la propia trayectoria.

![Figura 1. Cadena estructural del SV y punto de arranque del presente trabajo. Los nodos en gris representan pasos ya formalizados en el corpus; trayectoria (teal) es el objeto de partida; CSE · H(T) (púrpura) es el objeto introducido aquí.](figuras/fig_01_cadena_sv.svg)

**Figura 1.** Cadena estructural del SV y punto de arranque del presente trabajo. Los nodos en gris representan pasos ya formalizados en el corpus; *trayectoria* es el objeto de partida; *CSE · H(T)* es el objeto introducido en este trabajo.

---

## 4. Estado del arte y posicionamiento

El problema tratado aquí tiene afinidades parciales con varias familias de trabajos externos, pero no coincide con ninguna de ellas.

En **Behavior Trees**, la cuestión central es la organización jerárquica y reactiva del comportamiento, con gran atención a modularidad y ejecución; sin embargo, los BTs modelan estructuras de decisión y comportamiento, no una frontera semántica entre trayectoria interna y exposición externa. La literatura reciente ha señalado la ambigüedad frecuente en la definición y evaluación de propiedades de BTs \[6, 8\], precisamente uno de los riesgos que aquí se intenta evitar mediante un predicado explícito y verificable.

En **Task and Motion Planning (TAMP)** \[7\], el foco está en la articulación entre planificación lógica de alto nivel y planificación de movimiento de bajo nivel. El parentesco con el presente trabajo existe sólo en la separación de planos: aquí también se separa estructura interna de realización externa. Pero el objetivo es muy distinto: TAMP integra lógica y movimiento; este trabajo no integra movimiento, sino que fija una condición previa de legitimidad de exposición.

En **métodos formales para control y síntesis**, la afinidad reside en la exigencia de corrección y en la idea de especificación previa a la ejecución. La distancia es decisiva: aquí no se sintetiza un controlador ni se resuelve un problema de verificación temporal rica; se define una condición mínima de frontera sobre trayectorias ya formadas.

Finalmente, existen analogías superficiales con **guardas**, **precondiciones** o **condiciones de habilitación** en redes de Petri y sistemas de transición. Pero la CSE no modela consumo de recursos, ni dinámica de transición, ni efectos de disparo. Opera en un nivel anterior: no decide cómo transita el sistema, sino si una trayectoria ya constituida puede o no presentarse como exponible.

El posicionamiento correcto del presente trabajo es, por tanto, el de una pieza de frontera: ni semántica general del SV, ni control robótico, ni planificación de movimiento, sino condición estructural de exposición.

![Figura 5. Posicionamiento de la CSE respecto a modelos relacionados.](figuras/fig_05_posicionamiento.svg)

**Figura 5.** Posicionamiento de la CSE respecto a modelos relacionados. El eje horizontal separa bivaluado de ternario; el vertical separa modelos que modelan ejecución de los que no. La CSE ocupa el cuadrante ternario / no-ejecutivo, que ninguno de los modelos previos habitaba.

---

## 5. Problema formal

Sea `T` una trayectoria finita ya constituida en el marco SV. El problema del artículo es definir una condición interna al sistema que permita responder a la pregunta:

> ¿Puede `T` adquirir estatuto de exposición externa sin depender de información no contenida en `T` y sin violar los invariantes estructurales mínimos del sistema?

La respuesta no puede reducirse a la mera validez interna de `T`. Hay trayectorias estructuralmente válidas que, sin embargo, no deben exponerse: por ejemplo, porque dependen de indeterminación crítica, porque carecen de relevancia estructural o porque su supuesta clausura descansa en dependencias no resueltas.

Esto obliga a introducir un predicado adicional, subordinado a la semántica ya fijada, que actúe como condición de frontera.

---

## 6. Definición de la condición de frontera

### 6.1. Objeto formal

Sea `𝒯` el conjunto de trayectorias finitas representadas como grafos dirigidos etiquetados:

```
T = (N, R, v, val)
```

donde:

- `N` es un conjunto finito de nodos;
- `R ⊆ N × N` es un conjunto finito de aristas dirigidas;
- `v ∈ N` es el nodo de exposición;
- `val : N → {0,1,U}` es la asignación ternaria.

### 6.2. Predicado de habilitación

Se define el predicado de habilitación estructural:

```
H : 𝒯 → {0,1}
```

con la convención:

- `H(T) = 1` si `T` es estructuralmente habilitable para exposición;
- `H(T) = 0` si `T` no lo es.

### 6.3. Definición operativa

`H(T) = 1` si y sólo si se satisfacen simultáneamente las seis condiciones siguientes:

**C1 — Coherencia de valores**  
Todo nodo de `N` tiene valor en `{0,1,U}`. Formalmente: `∀n ∈ N, val(n) ∈ {0,1,U}`.

**C2 — Clausura sobre dependencia de `v`**  
Sea `Anc(v)` el conjunto de ancestros de `v`, es decir, de nodos desde los que existe un camino dirigido hasta `v`. Entonces `Anc(v) ⊆ N`. Toda dependencia estructural del punto de exposición está definida dentro del grafo.

**C3 — Trazabilidad no trivial**  
Existe al menos un nodo `n ≠ v` tal que `n →* v`. El punto de exposición no puede quedar legitimado por pura autoidentidad del propio nodo.

**C4 — Ausencia de indeterminación crítica**  
No existe nodo `n` con `val(n) = U` tal que `n →* v`.

**C5 — Admisibilidad**  
No existen nodos con valor ausente o nulo. Formalmente: `∀n ∈ N, val(n) ≠ ∅`.

**C6 — Relevancia estructural mínima**  
Existe al menos una arista `(a,b) ∈ R` tal que `b = v`. La trayectoria no puede considerarse exponible si no existe incidencia estructural efectiva sobre el nodo de exposición.

### 6.4. Lectura

Estas seis condiciones no añaden nuevos valores semánticos ni redefinen la trayectoria. Operan como un filtro de frontera. Su austeridad es deliberada: no pretenden agotar toda posible teoría de exposición, sino fijar un mínimo no trivial y verificable.

![Figura 2. Predicado H como filtro en cascada de seis condiciones. Cualquier fallo en Ci produce H(T) = 0. C4 aparece resaltado por ser la condición específica al alfabeto ternario del SV.](figuras/fig_02_predicado_H.svg)

**Figura 2.** Predicado H como filtro en cascada de seis condiciones. Cualquier fallo en Ci produce H(T) = 0. C4 aparece resaltado en ámbar por ser la condición específica al alfabeto ternario del SV.

---

## 7. Propiedades mínimas

### Proposición 1 — No trivialidad

Existen trayectorias válidas en el sentido de coherencia local que no son habilitables.

**Demostración.**  
Sea `T₃ = ({A}, ∅, A, val(A)=1)`. Se satisfacen C1 y C5, pero falla C6 porque no existe ninguna arista que incida en `v = A`. Por tanto `H(T₃) = 0`. ∎

### Proposición 2 — Sensibilidad a `U`

Si existe un nodo con valor `U` que alcanza el nodo de exposición, entonces la trayectoria no es habilitable.

**Demostración.**  
Es la propia condición C4. Si `∃n` tal que `val(n) = U` y `n →* v`, entonces C4 falla y, por definición, `H(T) = 0`. ∎

### Proposición 3 — Dependencia de clausura

Si el punto de exposición depende de información no contenida en el grafo, la trayectoria no es habilitable.

**Demostración.**  
Si existe un ancestro de `v` que no pertenece a `N`, entonces falla C2. Luego `H(T) = 0`. ∎

### Proposición 4 — No composicionalidad fuerte

La habilitación no está cerrada, en general, bajo composición de trayectorias.

**Justificación.**  
Dos trayectorias `T₁` y `T₂` pueden ser individualmente habilitables y, sin embargo, su composición introducir nuevas dependencias hacia el nodo de exposición o una nueva propagación de `U`, haciendo fallar C2 o C4. Por tanto, de `H(T₁) = H(T₂) = 1` no se sigue en general `H(T₁ ⊕ T₂) = 1`. ∎

Estas proposiciones no agotan la teoría, pero muestran que `H` no es un mero renombrado de validez interna.

![Figura 4. Las cuatro proposiciones del §7 como consecuencias de la tesis central. Prop. 2 en ámbar por depender específicamente de U; Prop. 4 en coral por ser la más contraintuitiva.](figuras/fig_04_proposiciones.svg)

**Figura 4.** Las cuatro proposiciones como consecuencias de la tesis central: H no es trivial, es sensible a U, depende de clausura, y no es composicional.

---

## 8. Ejemplos formales

Los cuatro ejemplos siguientes cubren los casos límite mínimos del predicado `H`. No son ornamentales: fijan el umbral entre interior válido y exposición legítima.

### Ejemplo 1 — Indeterminación crítica directa

```
N   = {A, B, C}
R   = {(A,B), (B,C)}
v   = C
val = {A:1, B:U, C:1}
```

Como `B →* C` y `val(B) = U`, falla **C4**.  
**Resultado:** `H(T₁) = 0`

### Ejemplo 2 — Indeterminación crítica indirecta

```
N   = {D, B, C}
R   = {(D,B), (B,C)}
v   = C
val = {D:U, B:1, C:1}
```

`D` alcanza `C` indirectamente a través de `B`; falla **C4**.  
**Resultado:** `H(T₂) = 0`

### Ejemplo 3 — Vacío estructural

```
N   = {A}
R   = ∅
v   = A
val = {A:1}
```

No existe arista que incida en `v`; falla **C6**.  
**Resultado:** `H(T₃) = 0`

### Ejemplo 4 — Caso mínimo habilitable

```
N   = {A, B}
R   = {(A,B)}
v   = B
val = {A:1, B:1}
```

Se satisfacen C1–C6.  
**Resultado:** `H(T₄) = 1`

![Figura 3. Los cuatro ejemplos formales como grafos dirigidos T = (N, R, v, val). El nodo de exposición v se indica con doble círculo. Los nodos U en ámbar; las aristas que propagan U también. El único caso habilitable (Ejemplo 4) en verde.](figuras/fig_03_ejemplos.svg)

**Figura 3.** Los cuatro ejemplos formales como grafos dirigidos T = (N, R, v, val). El nodo de exposición v se indica con doble círculo. Los nodos con valor U aparecen en ámbar; las aristas que propagan la indeterminación, también. El único caso habilitable (Ejemplo 4) se muestra en verde.

---

## 9. Discusión adversarial

La propuesta debe soportar al menos cuatro objeciones serias.

### 9.1. Objeción de trivialidad

Se podría afirmar que `H` no hace más que volver a nombrar la validez interna de la trayectoria. La Proposición 1 refuta esa lectura: existen trayectorias localmente válidas —coherentes y sin nulos— que no son habilitables porque carecen de relevancia estructural (C6) o trazabilidad (C3). La distinción entre válido e habilitable es sustantiva.

### 9.2. Objeción de reducción binaria

Se podría sostener que `H` es equivalente a una condición binaria ordinaria y que la presencia de `U` no aporta nada que no capture un sistema bivaluado. La Proposición 2 muestra que la posición semántica de `U` es esencial: el sistema no colapsa la indeterminación en falso o verdadero, sino que la trata como causa de no exposición cuando alcanza la frontera. Un predicado bivaluado no puede expresar esta distinción sin pérdida estructural.

### 9.3. Objeción de contaminación ontológica

Se podría acusar a `H` de introducir una nueva capa semántica ajena al SV. Esto no ocurre: `H` no crea nuevos valores ni nuevos estados del sistema; actúa sobre trayectorias ya constituidas, utiliza exclusivamente los objetos y relaciones ya definidos en el corpus, y devuelve una decisión booleana de frontera. No hay ampliación ontológica.

### 9.4. Objeción de equivalencia con modelos de habilitación clásicos

La similitud con guardas o condiciones de disparo en redes de Petri o sistemas de transición es parcial y superficial. `H` no consume recursos, no desencadena transición alguna y no modela dinámica. Opera en un plano distinto: el de la legitimidad de exposición de una trayectoria ya formada, con semántica ternaria explícita y tratamiento propio de la indeterminación.

---

## 10. Relación con el evaluador

El evaluador computacional adjunto no funda el artículo. Lo verifica parcialmente sobre el dominio de grafos finitos dirigidos aquí considerado. Su función es comprobar que la definición operativa de `H` no queda sólo enunciada, sino que puede ser sometida a prueba en ejemplos reproducibles y en casos límite.

La relación correcta es la siguiente:

- el artículo define `H`;
- el evaluador implementa `H` para un dominio finito concreto;
- el dataset proporciona casos falsables.

El evaluador implementa los seis predicados C1–C6 mediante funciones explícitas y verificables. Cualquier lector puede ejecutarlo, añadir casos al dataset y generar contraejemplos. El código, por tanto, acompaña al paper; no lo sustituye.

---

## 11. Conclusión

Se ha definido una condición estructural de frontera para el Sistema Vectorial SV. Su resultado no es una teoría de acción ni una semántica de ejecución, sino una condición necesaria de legitimidad en el paso desde la trayectoria interna hacia una posible exposición externa.

La aportación del artículo es doble. Por una parte, muestra que la mera constitución de trayectoria no basta para justificar exposición. Por otra, demuestra que es posible fijar un predicado mínimo, no trivial y verificable que preserve la austeridad ontológica del sistema.

En este sentido, el trabajo no clausura la movilidad, pero sí establece el requisito mínimo sin el cual cualquier discurso sobre movilidad compatible con el SV sería prematuro o ilegítimo.

---

## Notas sobre el evaluador adjunto

El repositorio adjunto contiene tres archivos:

- `paper_sv_motricidad_pubpub.md` — este documento;
- `../codigo/evaluador.py` — implementación de `H` en Python para grafos finitos dirigidos;
- `../codigo/datos.json` — dataset de casos formales, incluyendo los cuatro ejemplos del artículo y casos límite adicionales.

El evaluador puede ejecutarse directamente con `python3 evaluador.py` desde el directorio `codigo/`. No requiere dependencias externas. Los resultados deben coincidir con los de la sección 8.

---

## Referencias

1. Lloret Egea, J. A. (2026). *Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable* (Release 1). ITVIA.  
   https://www.itvia.online/pub/semantica-auditada-en-el-sistema-vectorial-sv-formalizacion-estructural-basada-en-sucesos-transduccion-ternaria-y-clausura-trazable/release/1

2. Lloret Egea, J. A. (2026). *Formalización de una interfaz visual estructurada en el Sistema Vectorial SV* (Release 1). ITVIA.  
   https://www.itvia.online/pub/formalizacion-de-una-interfaz-visual-estructurada-en-el-sistema-vectorial-sv/release/1

3. Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — IV: transducción al alfabeto ternario e interfaz paramétrica del sistema* (Release 1). ITVIA.  
   https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iv-transduccion-al-alfabeto-ternario-e-interfaz-parametrica-del-sistema/release/1

4. Lloret Egea, J. A. (2026). *Análisis del comportamiento geométrico del polígono del Sistema Vectorial SV: del plano cartesiano a una carta espacial afín auxiliar como vía de razonamiento para situaciones complejas* (Release 2). ITVIA.  
   https://www.itvia.online/pub/analisis-del-comportamiento-geometrico-del-poligono-del-sistema-vectorial-sv-del-plano-cartesiano-a-una-carta-espacial-afin-auxiliar-como-via-de-razonamiento-para-situaciones-complejas/release/2

5. Lloret Egea, J. A. (2026). *Transiciones estructurales y trayectorias de la U en el Sistema Vectorial SV* (Release 2). ITVIA.  
   https://www.itvia.online/pub/transiciones-estructurales-y-trayectorias-de-la-u-en-el-sistema-vectorial-sv/release/2

6. Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith, C. (2022). A survey of behavior trees in robotics and AI. *Robotics and Autonomous Systems*, 154, 104096.  
   https://www.sciencedirect.com/science/article/pii/S0921889022000513

7. Zhao, Z., Cheng, S., Ding, Y., Zhou, Z., Zhang, S., Xu, D., & Zhao, Y. (2024). A survey of optimization-based task and motion planning: From classical to learning approaches. *arXiv:2404.02817*.  
   https://arxiv.org/abs/2404.02817

8. Gugliermo, S., et al. (2024). Evaluating behavior trees. *Robotics and Autonomous Systems*.  
   https://www.sciencedirect.com/science/article/pii/S0921889024000976
