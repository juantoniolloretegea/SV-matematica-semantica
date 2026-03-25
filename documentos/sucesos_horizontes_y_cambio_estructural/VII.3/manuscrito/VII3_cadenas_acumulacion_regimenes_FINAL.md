---
title: "VII.3 — Cadenas, acumulación y regímenes de paso entre sucesos admisibles en el Sistema Vectorial SV"
author: "Juan Antonio Lloret Egea"
orcid: "0000-0002-6634-3351"
series: "Sistema Vectorial SV"
publisher: "Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)"
publication: "IA eñ™ – La Biblia de la IA™"
issn: "2695-6411"
date: "2026-03-25"
keywords:
  - Sistema Vectorial SV
  - célula SV(9,3)
  - cadenas de sucesos
  - acumulación eventiva
  - regímenes de paso
  - horizonte declarado
  - admisibilidad estructural
---

# VII.3 — Cadenas, acumulación y regímenes de paso entre sucesos admisibles en el Sistema Vectorial SV

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Serie doctrinal:** Sistema Vectorial SV  
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ – La Biblia de la IA™  
**ISSN:** 2695-6411  
**Madrid, 25 de marzo de 2026**

---

## Membresía editorial

Este documento pertenece a la serie:

**Sucesos, horizontes y cambio estructural — Una aproximación algebraica desde el Sistema Vectorial SV**

y constituye el tercer documento del frente VII, tras VII.1 (*El suceso admisible como objeto formal*) y VII.2 (*Gramática relacional mínima entre sucesos admisibles*). El acompañamiento experimental asociado se encuentra en:

`manuscrito/` · `figuras/` · `laboratorio_python_vii3/`

El laboratorio Python que acompaña a este documento acompaña, verifica e ilustra los ejemplos formales, pero no sustituye al manuscrito ni tiene rango doctrinal soberano sobre el Lenguaje SV.

---

## Dedicatoria

<img src="./figuras/descartes.jpg" alt="René Descartes" width="110" align="left" style="margin-right:18px;margin-bottom:8px;border:2px solid #2d6a9f;" />

A René Descartes, que en 1637 tuvo la audacia de proponer que todo problema difícil debe dividirse en partes tan pequeñas como sea necesario para resolverlo, y que esa división no es una rendición ante la complejidad sino su única forma de gobierno. Sin ese principio —sin la convicción de que lo oscuro se vuelve tratable cuando se le impone una partición rigurosa— el Sistema Vectorial SV no habría encontrado jamás su arquitectura de célula. La célula SV(9,3) no es otra cosa que el método cartesiano aplicado al espacio de lectura: nueve posiciones, tres grupos, un horizonte declarado; no porque la realidad tenga esa forma, sino porque esa forma hace la realidad pensable. Descartes no creó el mundo por partes; creó la disciplina de mirarlo por partes, y esa disciplina es la que aquí se hereda.

<br clear="left"/>

*Crédito imagen: retrato de Frans Hals (ca. 1649–1700), dominio público. Reproducción con diagramas del Discours de la méthode. Fuente: [Store norske leksikon](https://lille.snl.no/Ren%C3%A9_Descartes).*

---

<img src="./figuras/cajal.jpg" alt="Santiago Ramón y Cajal" width="110" align="left" style="margin-right:18px;margin-bottom:8px;border:2px solid #2d6a9f;" />

A Santiago Ramón y Cajal, español, Premio Nobel de Medicina de 1906, que demostró al mundo —contra la teoría reticular dominante— que el sistema nervioso no es una red continua e indistinta sino una comunidad de unidades discretas, cada una con su propia integridad, sus propios polos, su propia dirección de señal. Cajal vio en la célula nerviosa no un nudo de una malla sino un objeto: con entrada, con salida, con función propia y límites propios. Lo que él hizo con el microscopio y la tinción de Golgi sobre el tejido biológico, este trabajo intenta hacerlo con el álgebra sobre el espacio de sucesos: declarar que hay unidades, que esas unidades tienen estructura interna, que esa estructura no se disuelve en el conjunto y que es precisamente su discreción lo que hace posible el análisis. La célula SV no toma prestado el nombre de Cajal por metáfora; lo toma por deuda conceptual directa.

<br clear="left"/>

*Crédito imagen: fotografía de autor desconocido (ca. 1899), dominio público. Fuente: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Santiago-Ramon-y-Cajal-(cropped).jpg).*

---

Ambos, separados por dos siglos y por sus disciplinas, comparten una misma convicción que este trabajo hace suya sin reservas: que para entender cualquier sistema complejo hay que encontrar primero su unidad mínima legítima, describirla con exactitud, y negarse a disolverla antes de haberla comprendido. El Sistema Vectorial SV no existiría sin esa doble herencia. Que conste.

![Figura 0. Deuda intelectual fundacional — René Descartes y Santiago Ramón y Cajal](./figuras/figura_00_dedicatoria_descartes_cajal.svg){#fig-00}

*Figura 0. La doble herencia fundacional del Sistema Vectorial SV: el método cartesiano de partición rigurosa (izquierda) y la doctrina cajaliana de la unidad discreta (derecha), unidos en la arquitectura de la célula SV(9,3).*

---

## Resumen

Si VII.1 fijó el suceso admisible como objeto formal y VII.2 introdujo la gramática relacional mínima entre sucesos, VII.3 debe abordar el primer problema propiamente secuencial del frente: **cuándo una familia ordenada de sucesos merece el nombre de cadena**, bajo qué condiciones puede admitirse una **acumulación eventiva** y cómo distinguir **regímenes de paso** sin recaer ni en cronología fuerte ni en una suma verbal de eventos heterogéneos. El documento no introduce todavía una teoría general de límites, ni una métrica universal, ni una reconstrucción geométrica completa. Su finalidad es más estricta: impedir que la noción de acumulación quede suspendida entre intuiciones narrativas, metáforas cuantitativas y cierres prematuros. El texto queda anclado desde su apertura al Sistema Vectorial SV, a la célula SV(9,3) como ejemplo mínimo recurrente, al balance ya alcanzado por VII.0–VII.2 y a la prueba de estrés realizada sobre el Lenguaje SV. Desde ese punto de apoyo, VII.3 delimita lo que puede afirmarse ya, lo que sólo puede vigilarse y lo que debe reservarse para VII.4.

**Palabras clave:** Sistema Vectorial SV; célula SV(9,3); cadenas de sucesos; acumulación eventiva; regímenes de paso; horizonte declarado; admisibilidad estructural.

---

## 0. Estatuto, alcance y adversariales de legitimidad

### 0.1. Qué hace este documento

VII.3 introduce el **primer nivel formal de secuencialidad no trivial** de la familia VII. Su tarea no consiste en volver a definir el suceso admisible ni en repetir la gramática relacional mínima ya abierta por VII.2, sino en fijar tres piezas nuevas y mutuamente dependientes:

1. **cadena de sucesos admisibles**;
2. **acumulación eventiva**;
3. **regímenes de paso** entre estados de lectura acumulativa.

El documento trabaja en un régimen austero y explícito. Sólo introduce aquello que resulta necesario para que el frente VII no deje huérfana la secuencialidad del SV.

### 0.2. Qué no hace este documento

VII.3 **no** establece todavía:

- una teoría general de límites;
- una convergencia numérica universal;
- una métrica cerrada de acumulación;
- una reconstrucción geométrica global de cadenas;
- una traslación automática al Lenguaje SV;
- ni una especificación implementativa de backend, runner o IR.

Tampoco convierte la matriz de contraste de la familia VII en autoridad soberana. La carpeta de matriz fue abierta justamente para disciplinar el contraste con el Lenguaje SV, no para colonizarlo ni endurecerlo por vía lateral.

### 0.3. Adversariales que el documento debe superar

La legitimidad de VII.3 depende de superar, al menos, estas adversariales:

**A1. Inflación doctrinal.** Llamar teoría de cadenas a una suma de intuiciones secuenciales sin control tipado.  
**A2. Debilidad narrativa.** Llamar acumulación a cualquier enumeración verbal de sucesos.  
**A3. Temporalismo encubierto.** Reintroducir por la puerta de atrás una cronología fuerte bajo nombres aparentemente nuevos.  
**A4. Desanclaje respecto del SV.** Redactar un texto abstracto sobre eventos que podría pertenecer a cualquier sistema de transición y no al Sistema Vectorial SV.  
**A5. Endurecimiento prematuro del Lenguaje SV.** Exigir como capa operativa del lenguaje lo que todavía sólo comparece como exigencia doctrinal o como reserva estructural.

### 0.4. Criterio positivo de legitimidad

VII.3 sólo será legítimo si cumple simultáneamente cuatro condiciones:

1. queda cosido al SV desde la primera línea hasta la última;
2. usa la célula **SV(9,3)** como apoyo ejemplificativo real siempre que no quede postiza;
3. incorpora la prueba de estrés al Lenguaje SV sin leerla ni como absolución plena ni como condena genérica;
4. deja preparado el terreno para VII.4 sin fingir que ya lo ha cerrado.

---

## 1. Posición de VII.3 en la familia VII y en el Sistema Vectorial SV

La familia VII quedó abierta cuando la modificación efectiva dejó de leerse como función soberana del mero transcurso y pasó a depender de la comparecencia de **sucesos admisibles en horizonte declarado**. El README de la familia fijó expresamente que el paso correcto tras VII.0–VII.2 era **consolidar la extracción matricial nacida de esos documentos, contrastarla con el Lenguaje SV y sólo después abrir el siguiente documento de la serie**. Ese orden ya ha sido cumplido y queda reflejado en el corpus de este documento.

VII.3 hereda así tres planos ya estabilizados:

- **de VII.0**, la no soberanía modificativa del tiempo y la exigencia de horizonte declarado;
- **de VII.1**, el suceso admisible como objeto formal tipado;
- **de VII.2**, la gramática relacional mínima: comparabilidad legítima, afectación, precedencia estructural y compatibilidad derivada.

La pregunta propia de VII.3 ya no es: *¿qué es un suceso?* ni sólo *¿cómo se relacionan dos sucesos?* La pregunta es otra:

> **¿cuándo una familia ordenada de sucesos puede ser leída como cadena legítima y bajo qué condiciones esa cadena admite una magnitud acumulativa formalmente tratable dentro del SV?**

La respuesta no puede proceder de intuiciones generales sobre "paso del tiempo". Debe proceder del propio sustrato del SV:

- espacio ternario $\Sigma=\{0,1,U\}$;
- célula $(n,b)$, con especial atención aquí a **SV(9,3)**;
- horizonte declarado;
- soporte;
- reevaluación;
- transporte de observables;
- y lectura estructural de la modificación.

---

## 2. Resultado de la prueba de estrés al Lenguaje SV

### 2.1. Qué ha resistido bien

La prueba de estrés al Lenguaje SV no ha mostrado un lenguaje vacío ni ciego frente a la familia VII. Ha mostrado, más bien, un lenguaje con **base real** para hospedar parte del frente de sucesos:

- existencia de horizonte formal y referencias de horizonte;
- estructuras de trayectoria y transición;
- especificaciones de admisibilidad;
- y vigilancia arquitectónica explícita sobre frentes futuros.

Por tanto, sería falso presentar el Lenguaje SV como si no supiera nada de horizontes, trayectorias o admisibilidad.

### 2.2. Qué no ha quedado cubierto todavía

La misma prueba de estrés ha mostrado, sin embargo, que siguen abiertos huecos reales:

- distinción operativa entre **suceso local** y **suceso envolvente**;
- formalización explícita de **afectación débil** y **afectación fuerte**;
- noción propia de **precedencia estructural entre sucesos**;
- **compatibilidad derivada** como relación operativa;
- y una pieza particularmente fértil: la **respuesta estructural a suceso de horizonte** (véase [Figura 4](#fig-04)).

VII.3 debe escribirse desde ese balance. No debe fingir que el Lenguaje SV ya lo contiene todo, pero tampoco debe tratarlo como terreno virgen. Su papel aquí es más sobrio: **delimitar con precisión lo que puede exigirse doctrinalmente sin invadir todavía integración de lenguaje**.

### 2.3. Regla de relación con el Lenguaje SV

La crítica al Lenguaje SV en este documento no adopta forma polémica. Adopta forma diagnóstica:

- **ya cubierto o casi cubierto**: horizonte formal mínimo, trayectoria, transición, admisibilidad;
- **vigilado pero no cerrado**: cadenas, acumulaciones, reservas frente a endurecimiento prematuro;
- **no cubierto todavía**: local/envolvente, afectación estratificada, precedencia entre sucesos, respuesta estructural a horizonte.

Ese balance es el que legitima VII.3 y, al mismo tiempo, le impone modestia.

---

## 3. Antecedentes internos: VII.1 y VII.2

### 3.1. Herencia de VII.1

VII.1 fijó el suceso admisible como objeto formal. VII.3 hereda de allí una convicción decisiva: el cambio no puede quedar absorbido por el mero transcurso, sino que debe comparecer como **suceso admisible** dentro de un **horizonte declarado**. En esta nueva fase no se altera ese núcleo; se le añade una pregunta secuencial.

### 3.2. Herencia de VII.2

VII.2 definió la estructura relacional mínima entre sucesos admisibles. Sin comparabilidad legítima, afectación y precedencia, cualquier secuencia sería una yuxtaposición arbitraria. VII.3 empieza exactamente donde VII.2 debe detenerse:

- una vez posible la relación por pares,
- la cuestión pasa a ser **cómo se encadenan más de dos sucesos**
- y **qué puede acumularse legítimamente a través de ese encadenamiento**.

### 3.3. Primera formulación ya anclada a SV(9,3)

En **SV(9,3)**, donde la célula dispone de nueve posiciones distribuidas en tres grupos estructurales de lectura, no basta observar que entre dos estados aparece un cambio. Para que una secuencia de modificaciones parciales sobre esos nueve parámetros pueda leerse como cadena, hace falta algo más que sucesión cronológica:

- compatibilidad de horizonte entre los pasos;
- un criterio común de observables relevantes;
- y una regla de lectura que no destruya la posibilidad de acumulación en el tercer o cuarto paso.

Ese ejemplo mínimo anticipa ya el problema central.

---

## 4. Ubicación comparativa y restricción metodológica

La literatura matemática y computacional conoce múltiples herramientas para pensar secuencias, acumulaciones y cambios de régimen: sistemas de transición, estructuras de eventos, teorías de concurrencia, iteración de operadores, sumas parciales, recursión y límite. VII.3 puede dialogar con ese trasfondo, pero no se le superpone sin resto. El SV introduce aquí restricciones que modifican el problema:

1. no trabaja sólo con "estados" y "pasos", sino con **horizontes, soportes y reevaluaciones**;
2. no trata la acumulación como un hecho automático;
3. no presupone una continuidad fuerte previa;
4. y no autoriza a ocultar bajo causalidad genérica lo que en el SV exige **transporte de observables y legibilidad de régimen**.

Por ello, VII.3 adopta una regla de método: **usar sólo el instrumental mínimo necesario para no dejar huérfana la secuencialidad del SV**, sin sobreimportar modelos ajenos ni clausurar todavía una teoría completa de paso asintótico.

---

## 5. Cadenas de sucesos admisibles

### 5.1. Definición

Sea una familia ordenada de sucesos admisibles

$$
\mathbf e=(e_1,e_2,\dots,e_n,\dots).
$$

Diremos que $\mathbf e$ constituye una **cadena de sucesos admisibles** si para todo par consecutivo $e_i,e_{i+1}$ se cumplen simultáneamente:

1. la composición local $e_{i+1}\circ e_i$ es definible en el sentido restrictivo heredado de VII.2;
2. el horizonte resultante de $e_i$ es compatible con el horizonte de partida de $e_{i+1}$;
3. existe transporte suficiente de observables relevantes entre los pasos consecutivos;
4. la cadena conserva un criterio explícito de lectura acumulativa.

La definición es deliberadamente austera: VII.3 no exige todavía propiedades globales de completitud ni una teoría cerrada de cadenas infinitas. La [Figura 1](#fig-01) ilustra los cuatro criterios sobre la célula SV(9,3).

![Figura 1. Cadena de sucesos admisibles — los cuatro criterios C1–C4 sobre SV(9,3)](./figuras/figura_01_cadena_admisible.svg){#fig-01}

*Figura 1. Cadena de sucesos admisibles. Arriba: cadena legítima $(e_1,e_2,e_3)$ con los cuatro criterios satisfechos. Abajo: contraejemplo de ruptura por observable ajena no transportable. Célula SV(9,3), espacio ternario $\Sigma=\{0,1,U\}$.*

### 5.2. Observación estructural

Una colección de composiciones locales puede existir y, sin embargo, **no** definir ninguna cadena útil. El cuarto criterio —persistencia de una lectura acumulativa explícita— impide precisamente esa degradación. Aquí empieza ya la diferencia entre una mera sucesión de sucesos y una cadena en sentido propio.

### 5.3. Ejemplo mínimo en SV(9,3)

Considérese una célula **SV(9,3)** con vector de lectura inicial

$$
x^{(0)}=(0,0,U,\;0,0,0,\;U,0,0).
$$

Supóngase una sucesión de tres sucesos admisibles:

- $e_1$: reevaluación local del parámetro 3, que pasa de $U$ a $0$;
- $e_2$: modificación localizada del parámetro 7, que pasa de $U$ a $1$;
- $e_3$: reevaluación del parámetro 3 condicionada por el mismo horizonte declarado y por observables aún transportables.

La secuencia $(e_1,e_2,e_3)$ **no** merece llamarse cadena sólo porque tenga tres pasos. Merece ese nombre únicamente si:

- el horizonte del segundo paso no invalida ilegítimamente el primero;
- los observables que sostienen la reevaluación del tercer paso siguen siendo comparables;
- y existe una lectura común que permita tratar el conjunto como proceso estructural y no como mera lista de incidencias.

En cambio, si $e_3$ exigiera un horizonte ajeno o una observable no transportable desde $e_2$, la cadena se rompería aunque hubiera tres sucesos cronológicamente ordenados.

### 5.4. Primera adversarial interna

**Objeción.** Todo esto podría reducirse a una iteración cualquiera de composiciones locales.  
**Respuesta.** No. Una iteración local puede existir sin generar cadena si carece de criterio acumulativo, de compatibilidad de horizonte o de transporte suficiente de observables. La cadena exige más que mera composibilidad puntual.

---

## 6. Acumulación eventiva

### 6.1. Problema

Una vez fijada una cadena, la pregunta siguiente es si puede asociarse a ella una magnitud acumulativa legítima. VII.3 responde negativamente a toda identificación automática entre "más sucesos" y "más acumulación".

### 6.2. Definición restringida

Sea $\mathbf e=(e_1,\dots,e_n)$ una cadena finita. Diremos que existe una **acumulación eventiva local** si puede definirse una familia de magnitudes

$$
A_n(\mathbf e)
$$

tal que:

1. $A_1$ depende de una observable relevante o de una diferencia eventiva inicial;
2. $A_{n+1}$ se obtiene por una regla de actualización bien tipada a partir de $A_n$ y del nuevo suceso $e_{n+1}$;
3. la regla de actualización conserva el régimen de lectura explicitado para la cadena.

En esta fase, $A_n$ no se identifica todavía con una suma numérica universal. Puede ser magnitud escalar, vectorial o dato acumulativo abstracto, siempre que quede bien tipado y sea legible dentro del régimen adoptado. La [Figura 2](#fig-02) muestra la recursión formal sobre los Ejemplos I y II.

![Figura 2. Acumulación eventiva — recursión A_n con ejemplo legítimo e ilegítimo](./figuras/figura_02_acumulacion_eventiva.svg){#fig-02}

*Figura 2. Acumulación eventiva. Izquierda: recursión $A_1\to A_2\to A_3$ sobre cadena legítima de SV(9,3). Derecha: pseudoacumulación ilegítima por observable ajena en $e_3$ (criterio C3 incumplido, $\Phi$ indefinida).*

### 6.3. Ejemplo legítimo en SV(9,3)

Retomemos la célula **SV(9,3)** anterior y consideremos que los sucesos $e_1,e_2,e_3$ afectan a una observable relevante $F$ que mide, no el mero número de cambios, sino una magnitud estructural de reevaluación sobre parámetros comparables.

Defínase:

$$
A_1=\Delta_{e_1}F,\qquad A_{n+1}=A_n+\Phi(e_{n+1},A_n),
$$

donde $\Phi$ es una regla bien tipada de actualización.

Entonces:

- si $\Phi$ conserva el mismo criterio de lectura en los tres pasos, existe **acumulación eventiva local**;
- si, en cambio, el tercer paso exige una observable ajena al régimen previo o altera ilegítimamente el horizonte, la acumulación deja de ser legítima bajo esa regla.

El ejemplo muestra que la acumulación no depende sólo del número de sucesos ni del conteo de posiciones modificadas en la célula $(9,3)$, sino de la persistencia de una **gramática de actualización**.

### 6.4. Pseudoacumulación ilegítima

Será ilegítima toda pseudoacumulación en la que:

- falte transporte común de observables;
- cambie el régimen de lectura sin control;
- se sumen magnitudes heterogéneas sin regla formal de actualización;
- o se pretenda llamar acumulación a un simple recuento narrativo de incidencias.

### 6.5. Segunda adversarial interna

**Objeción.** La acumulación propuesta sigue siendo abstracta y podría esconder una suma verbal.  
**Respuesta.** La objeción sólo prospera si se renuncia a exigir regla de actualización bien tipada. VII.3 define acumulación por **recursión formal sobre cadena legítima**, no por suma retórica de acontecimientos.

---

## 7. Regímenes de paso

### 7.1. Motivación

Una vez admitida una acumulación local, surge una pregunta nueva: **qué tipos de comportamiento puede exhibir esa acumulación a medida que la cadena crece**. VII.3 no introduce todavía una teoría completa de convergencia, pero sí necesita un vocabulario mínimo de regímenes de paso. La [Figura 3](#fig-03) presenta la tipología.

![Figura 3. Tipología mínima de regímenes de paso en SV(9,3)](./figuras/figura_03_regimenes_de_paso.svg){#fig-03}

*Figura 3. Regímenes de paso: finito (acumulación local, sin cuestión asintótica), estable (criterio de lectura persistente, $\Phi$ legible en todos los pasos) y singular (ruptura por cambio de horizonte o pérdida de transporte de observables).*

### 7.2. Tipología mínima

Se distinguen tres regímenes iniciales.

#### Régimen finito
La cadena es corta o está acotada por diseño, y la acumulación sólo necesita sentido local.

#### Régimen estable
La cadena puede prolongarse manteniendo un criterio de lectura suficientemente persistente como para seguir actualizando $A_n$ sin pérdida de tipado.

#### Régimen singular
El crecimiento de la cadena provoca pérdida de transporte, ruptura del criterio de lectura o cambio de horizonte no absorbible por la regla de actualización.

### 7.3. Ejemplo comparativo en SV(9,3)

En una célula **SV(9,3)** puede darse, por ejemplo, este comportamiento:

- en un primer tramo, varios sucesos locales sobre parámetros comparables mantienen misma familia de observables y mismo horizonte declarado: **régimen estable**;
- un suceso posterior introduce una reevaluación envolvente que altera el conjunto de observables o cambia de horizonte sin traducción legítima: **paso a régimen singular**.

El problema ya no es "cuántos sucesos hay", sino **si la regla de actualización sigue siendo legible**.

### 7.4. Sentido preciso del término "estable"

En este documento, "estable" **no significa convergencia numérica clásica**. Significa persistencia del criterio de lectura y de la regla de actualización. La convergencia en sentido fuerte, si llega a abrirse, deberá ser tratada en otra fase de la serie.

### 7.5. Tercera adversarial interna

**Objeción.** El término "régimen estable" sigue sonando demasiado fuerte si no se prueba límite.  
**Respuesta.** La objeción es pertinente si se importa al documento una semántica clásica del límite que aquí no ha sido introducida. En VII.3, estabilidad significa únicamente **persistencia legible del régimen**, no convergencia ya clausurada.

---

## 8. Cuatro ejemplos estructurales que ponen a prueba VII.3 y la familia previa

### 8.1. Ejemplo I — cadena legítima finita en SV(9,3)

Sea el vector inicial

$$
x^{(0)}=(0,U,0,\;0,0,0,\;U,0,0).
$$

Definimos tres sucesos admisibles:

- $e_1$: reevaluación del parámetro 2, $U\to 0$;
- $e_2$: reevaluación del parámetro 7, $U\to 1$;
- $e_3$: ajuste local del parámetro 7, manteniendo mismo horizonte y misma familia de observables.

Si la comparabilidad heredada de VII.2 se conserva y la regla de actualización sobre una magnitud $A_n$ permanece bien tipada, la familia $(e_1,e_2,e_3)$ constituye **cadena legítima** y admite **acumulación local**. El laboratorio Python (sección 11) reproduce este ejemplo con salida verificable.

### 8.2. Ejemplo II — pseudoacumulación ilegítima

Sea ahora una sucesión de tres sucesos sobre una célula SV(9,3) en la que:

- $e_1$ y $e_2$ se apoyan en observables de conectividad;
- $e_3$ exige súbitamente una observable ajena de otro régimen sin traducción formal.

Aunque el recuento de pasos sea el mismo que en el ejemplo anterior, aquí no existe una acumulación eventiva legítima. La cadena queda rota por heterogeneidad no absorbida (criterio C3 incumplido; véase [Figura 2](#fig-02)).

### 8.3. Ejemplo III — paso de régimen estable a régimen singular

Sea una cadena inicialmente legítima de cuatro sucesos sobre SV(9,3), con actualización acumulativa bien tipada en los tres primeros pasos. Supóngase que el cuarto introduce un cambio de horizonte declarado que modifica el criterio de lectura de los observables relevantes.

Entonces:

- los tres primeros pasos pueden haber operado en **régimen estable**;
- el cuarto fuerza un **paso a régimen singular** (criterio C2 incumplido: $H_{\text{out}}(e_3)\neq H_{\text{in}}(e_4)$);
- y la acumulación deja de ser legítima bajo la misma regla.

El ejemplo muestra que VII.3 no organiza meramente "series temporales", sino condiciones de continuidad estructural de lectura.

### 8.4. Ejemplo IV — respuesta estructural a suceso de horizonte

La prueba de estrés al Lenguaje SV ha dejado visible un hueco fértil: **la respuesta estructural a suceso de horizonte**. Considérese una célula SV(9,3) en la que una cadena de sucesos locales opera establemente hasta que un suceso nuevo altera el horizonte declarado sin destruir por completo la legibilidad del sistema (véase [Figura 4](#fig-04)).

El punto crítico ya no es sólo si hay cadena o acumulación, sino **qué tipo de respuesta estructural puede considerarse legítima**. Se delimitan cuatro respuestas posibles:

- **R1.** ¿se prolonga la cadena bajo nueva regla $\Phi'$?
- **R2.** ¿se abre una nueva cadena independiente bajo $H'$?
- **R3.** ¿se detiene la acumulación previa y queda congelada?
- **R4.** ¿o se exige una reevaluación envolvente que todavía no ha sido formalizada?

Este cuarto ejemplo no queda cerrado en VII.3; queda **delimitado** como una de las aperturas más fértiles hacia VII.4.

![Figura 4. Respuesta estructural a suceso de horizonte — apertura hacia VII.4](./figuras/figura_04_respuesta_horizonte.svg){#fig-04}

*Figura 4. Respuesta estructural a suceso de horizonte $e^*$ (H→H′) sobre SV(9,3). Las cuatro respuestas posibles (R1–R4). La respuesta R4 —reevaluación envolvente— no es formalizable en VII.3 y queda reservada para VII.4.*

---

## 9. Proposiciones mínimas

### Proposición 1. No toda sucesión de sucesos admisibles es una cadena legítima
**Razón.** Puede faltar composibilidad local (C1), compatibilidad de horizonte (C2) o criterio común de lectura acumulativa (C4).

### Proposición 2. No toda cadena admite acumulación eventiva
**Razón.** La existencia de una cadena no garantiza una regla de actualización $\Phi$ bien tipada para una magnitud acumulativa.

### Proposición 3. Un régimen estable no implica convergencia clásica
**Razón.** La estabilidad aquí se refiere a persistencia del criterio de lectura, no a cierre numérico por límite.

### Proposición 4. La acumulación eventiva es dependiente del régimen
**Razón.** Un mismo esquema de actualización puede ser legítimo en régimen finito y dejar de serlo al entrar en régimen singular.

### Proposición 5. La respuesta estructural a suceso de horizonte no puede reducirse a mero paso cronológico
**Razón.** Lo decisivo no es el orden temporal del suceso, sino su capacidad para alterar el horizonte, la comparabilidad y la legitimidad de la regla de actualización $\Phi$.

---

## 10. Delimitación negativa reforzada

Este documento no establece todavía:

- teoría completa de cadenas infinitas;
- convergencia o divergencia general;
- métrica universal de acumulación;
- reconstrucción geométrica a partir de cadenas;
- traducción computacional al backend o al IR;
- ni catálogo completo de respuestas estructurales a suceso de horizonte.

Su función es preparatoria y estructural. Fija el vocabulario mínimo para que el paso a una teoría posterior de regímenes, límites o reconstrucciones no nazca confundiendo:

- **sucesión** con **cadena**;
- **suma** con **acumulación**;
- **estabilidad** con **convergencia**;
- o **cambio de horizonte** con **simple transcurso**.

---

## 11. Laboratorio mínimo reproducible en Python

### 11.1. Juicio de necesidad

A la fecha de esta redacción no existe todavía un laboratorio ya consolidado y publicado específicamente para VII.3. Sin embargo, **sí procede** abrir un laboratorio mínimo en Python, porque aquí no sería un postizo: permitiría comprobar de forma controlada justamente aquello que VII.3 introduce por primera vez:

- legitimidad o ilegitimidad de cadenas finitas (criterios C1–C4);
- posibilidad o imposibilidad de acumulación eventiva;
- paso entre régimen estable y régimen singular;
- y primeros ensayos sobre respuesta estructural a suceso de horizonte.

### 11.2. Alcance legítimo del laboratorio

El laboratorio no pretende:

- reconstrucción geométrica completa;
- integración con backend soberano;
- ni validación lingüística final del Lenguaje SV.

Sí permite al lector experimentar, con ejemplos de **SV(9,3)**, al menos con estas cuatro operaciones:

1. declarar una célula inicial con vector ternario en $\Sigma^9=\{0,1,U\}^9$;
2. introducir una familia finita de sucesos admisibles tipados;
3. verificar si la familia constituye cadena legítima (criterios C1–C4);
4. aplicar una regla de actualización $\Phi$ y detectar si el régimen permanece estable o entra en singularidad.

### 11.3. Forma y salida

El laboratorio nace como **módulo mínimo reproducible** (`laboratorio_vii3.py`). Su salida para cada ejemplo es:

- tabla de cadena con soporte $\sigma(e_i)$, horizonte y observable;
- la magnitud acumulativa $A_n$ en cada paso;
- y la clasificación del régimen de paso (FINITO / ESTABLE / SINGULAR).

Los cuatro ejemplos de la sección 8 quedan cubiertos con salida verificable en consola. El laboratorio acompaña, verifica e ilustra; no sustituye ni al manuscrito ni al Lenguaje SV.

---

## 12. Conclusión

VII.3 introduce el primer nivel formal de secuencialidad no trivial del Sistema Vectorial SV. Frente a la tentación de identificar toda sucesión de sucesos con una cadena y toda cadena con una acumulación, el documento impone tres filtros: **composibilidad**, **persistencia de lectura** y **regla de actualización bien tipada**. Al hacerlo, no sólo consolida lo heredado de VII.1 y VII.2, sino que incorpora ya el balance de la prueba de estrés al Lenguaje SV: el lenguaje dispone de base suficiente para hospedar el frente, pero no ha cerrado aún sus huecos más fértiles.

El resultado no es una teoría general de límites, ni una métrica universal, ni una implementación de lenguaje. Es algo más austero y más necesario: una disciplina mínima para que el SV pueda hablar legítimamente de cadenas, acumulación y regímenes de paso sin recaer ni en temporalismo fuerte ni en acumulación verbal.

Y precisamente por eso VII.3 debe entregar ya la continuidad a VII.4. Si VII.3 ha fijado cuándo una cadena existe, cuándo una acumulación es legítima y cuándo un régimen se vuelve singular, VII.4 deberá afrontar con mayor precisión el problema todavía abierto de la **respuesta estructural prolongada**, de la **reevaluación bajo cambio de horizonte** y de la **continuidad o ruptura del transporte estructural** a través de familias más largas y más tensas de sucesos admisibles.

---

## Bibliografía

**Referencias de la serie doctrinal:**

- Lloret Egea, J. A. *VII.0 — El tiempo no modifica por sí mismo: sucesos, horizontes y cambio estructural en el Sistema Vectorial SV*. ITVIA / IA eñ™, Madrid, 2026. ISSN: 2695-6411.
- Lloret Egea, J. A. *VII.1 — El suceso admisible como objeto formal del Sistema Vectorial SV*. ITVIA / IA eñ™, Madrid, 2026. ISSN: 2695-6411.
- Lloret Egea, J. A. *VII.2 — Gramática relacional mínima entre sucesos admisibles en el Sistema Vectorial SV*. ITVIA / IA eñ™, Madrid, 2026. ISSN: 2695-6411.

**Referencias de contraste:**

- Abramsky, S., & Jung, A. *Domain Theory*. In: *Handbook of Logic in Computer Science*, Vol. 3. Oxford University Press, 1994.
- Aczel, P. *Non-Well-Founded Sets*. CSLI Lecture Notes, 1988.
- Nielsen, M., Plotkin, G., & Winskel, G. "Petri Nets, Event Structures and Domains." *Theoretical Computer Science*, 13(1), 85–108, 1981.
- Petri, C. A. *Kommunikation mit Automaten*. Universität Bonn, 1962.
- Winskel, G. "Event Structures." In: *Advances in Petri Nets 1986*, Lecture Notes in Computer Science 255. Springer, 1987.

---

*Créditos fotográficos de la dedicatoria:*  
*René Descartes — retrato de Frans Hals (ca. 1649), dominio público. Fuente: [Store norske leksikon](https://lille.snl.no/Ren%C3%A9_Descartes).*  
*Santiago Ramón y Cajal — fotografía de autor desconocido (ca. 1899), dominio público. Fuente: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Santiago-Ramon-y-Cajal-(cropped).jpg).*
