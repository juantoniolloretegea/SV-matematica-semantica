# Fourier factual y ecuación de onda electromagnética en el Sistema Vectorial SV: desarrollo cíclico, transformada modal y propagación sobre ciclo y trayectoria poligonal

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Lugar y fecha:** Madrid, 10/04/2026


## Breviario inicial de terminología, siglas y unidades del documento

| Término | Definición |
|---|---|
| **Ciclo de Suceso** | Recurrencia estructural del polígono o de la trayectoria factual; no equivale a tiempo clásico. |
| **Medidor factual de ciclo** | Instrumento de normalización factual apoyado en el Ciclo de Suceso. |
| **Trayectoria poligonal de activación** | Soporte discreto donde el SV describe activaciones, recorridos y acumulaciones factuales. |
| **Electromagnetismo factual del SV** | Primer dominio físico director del bloque de física factual del SV. |
| **Modo cíclico factual** | Componente modal propia del SV sobre ciclo factual y trayectoria poligonal. |
| **Transformada modal factual** | Operador que lleva una configuración factual del dominio poligonal al dominio modal factual. |
| **Balance factual modal** | Identidad de correspondencia entre dominio factual y dominio modal. |
| **Residual de borde factual** | Residuo reconstructivo concentrado en una transición abrupta, una frontera o una detonación factual. |
| **ED-EM-01** | Ejemplo director del documento: pulso electromagnético factual localizado sobre `SV(3,9)`, en vacío factual, propagándose sobre ciclo y trayectoria poligonal. |
| **UE_MFC** | Unidad Elemental del Medidor Factual de Ciclo. |
| **UFE** | Unidad Factual de Extensión. |
| **UFM** | Unidad Factual de Masa. |
| **UFC** | Unidad Factual de Corriente. |

**Diccionario dimensional mínimo:**

$$
[T]=\mathrm{UE\_MFC},\qquad [L]=\mathrm{UFE},\qquad [M]=\mathrm{UFM},\qquad [I]=\mathrm{UFC}.
$$

$$
[v_{\mathrm{SV}}]=\mathrm{UFE}\cdot\mathrm{UE\_MFC}^{-1},\qquad
[E_{\mathrm{SV}}]=\mathrm{UFM}\cdot\mathrm{UFE}\cdot\mathrm{UFC}^{-1}\cdot\mathrm{UE\_MFC}^{-3},\qquad
[B_{\mathrm{SV}}]=\mathrm{UFM}\cdot\mathrm{UFC}^{-1}\cdot\mathrm{UE\_MFC}^{-2}.
$$


## Resumen

Este documento construye, dentro del Sistema Vectorial SV, una formulación cíclico-modal factual del electromagnetismo sobre célula canónica, ciclo factual, medición factual y trayectoria poligonal. Su objeto es preciso: sostener una **ecuación factual de onda electromagnética en vacío factual** sin introducir tiempo soberano y sin ceder la dirección semántica a formalismos externos. El dominio director es el **electromagnetismo factual del Sistema Vectorial SV**; el soporte no temporal lo forman el **Ciclo de Suceso** y el **Medidor factual de ciclo**; y la base metrológica mínima descansa en **UE_MFC**, **UFE**, **UFM** y **UFC**.

Todo el recorrido se cose sobre el ejemplo director **ED-EM-01**.

---

## Introducción

El presente documento no pretende clausurar una física factual general del Sistema Vectorial SV. Su estatuto es más estricto: responder, con rigor, a una exigencia interna del corpus. Si el electromagnetismo factual del SV ha de tratar propagación, contorno, residualidad y sensibilidad estructural, entonces necesita un aparato propio de modos, transformada, balance y reconstrucción factual.

El suelo del documento es doble. Por un lado, los **Fundamentos algebraico-semánticos del Sistema Vectorial SV** fijan la célula canónica, el polígono representativo y la dualidad entre plano exacto y plano auxiliar. Por otro, **Primitivos metrológicos del Sistema Vectorial SV** permite hablar del campo electromagnético factual con unidades y dimensiones propias del sistema. Entre ambos planos, el **Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV** fija la compuerta decisiva: la evolución no se apoyará en tiempo soberano, sino en **Ciclo de Suceso** y **Medidor factual de ciclo**.

Toda esta arquitectura se recorre sobre un único caso director: **ED-EM-01**, un pulso electromagnético factual localizado sobre la célula canónica `SV(3,9)`, en vacío factual, propagándose sobre ciclo y trayectoria poligonal.

---

## Principios y variables canónicas del Sistema Vectorial SV

### Principio 1. Primacía del suceso

En el Sistema Vectorial SV, la unidad soberana de descripción no es el tiempo, sino el **suceso**. Una variable de medición, por importante que sea en la práctica, no adquiere por ello estatuto doctrinal primario. La evolución legítima del dominio no se funda, por tanto, en una variable temporal soberana, sino en la sucesión factual de sucesos, trayectorias, recurrencias estructurales y medición factual subordinada.

### Principio 2. Inmutabilidad del suceso

Un suceso ya fijado en la trayectoria no puede ser reescrito retroactivamente por otro suceso posterior. Si una configuración reaparece, no corrige el suceso anterior ni lo sustituye; comparece como un nuevo suceso de la trayectoria. Esta disciplina protege al sistema frente a retroproyecciones ilegítimas, clausuras espurias y narrativas donde una variable instrumental termina absorbiendo la estructura del dominio.

### Principio 3. El tiempo no es variable canónica del SV

El Sistema Vectorial SV rechaza el tiempo como **primitiva doctrinal soberana**. Esto no significa que toda medición temporal funcional sea ilegítima; significa que no puede elevarse a fundamento constitutivo del sistema. Por eso el documento admite la **UE_MFC** como unidad factual de medición compatible y, al mismo tiempo, niega que tal magnitud se convierta en principio ontológico director. El **Ciclo de Suceso** expresa recurrencia estructural; el **Medidor factual de ciclo** ordena y normaliza esa recurrencia; ninguno de los dos autoriza a reintroducir tiempo soberano bajo otro nombre.

### Principio 4. U como indeterminación honesta

El símbolo `U` no designa ambigüedad complaciente ni licencia de cierre arbitrario. Designa **indeterminación honesta**. Allí donde no hay base suficiente para concluir, el SV no fuerza una respuesta. Esta compuerta protege al sistema frente a soluciones aparentes, cierres prematuros y reescrituras narrativas no justificadas.

### Ejemplo doctrinal 1. La paradoja del abuelo

**1. Enunciado clásico de la paradoja**

La formulación habitual es ésta:

Un nieto viaja al pasado y mata a su abuelo antes de que este tenga descendencia.
Si el abuelo muere antes de engendrar la línea familiar, el nieto no nacería.
Pero si el nieto no nace, no puede viajar al pasado para matar al abuelo.
Luego el sistema entra en contradicción.

En el lenguaje de la lógica clásica de narrativas temporales, la paradoja aparece porque se permite simultáneamente:

- que un estado futuro **modifique causalmente** un estado pasado ya fijado;
- y que ese mismo pasado siga funcionando como condición de existencia del futuro que lo ha modificado.

Dicho de otro modo: el sistema se muerde a sí mismo porque concede al tiempo un poder ontológico que permite **retroescritura**.

**2. Traducción mínima al régimen SV**

En el SV no se formula esto en términos de "pasado" y "futuro" como soberanías. Debe traducirse al lenguaje correcto: sucesos, trayectoria factual, inmutabilidad, compatibilidad estructural y, si procede, $U$.

Definamos una trayectoria mínima:

$$
S_{1} \rightarrow S_{2} \rightarrow S_{3} \rightarrow S_{4}
$$

donde $S_{1}$ es la existencia del abuelo, $S_{2}$ la generación de la línea familiar, $S_{3}$ el nacimiento del nieto y $S_{4}$ la acción del nieto contra el abuelo.

En la paradoja clásica, $S_{4}$ pretende actuar **sobre** $S_{1}$ como si pudiera **reescribirlo**. Ésa es exactamente la operación que el SV prohíbe.

**3. Principio canónico que desarma la paradoja**

> **Un suceso soberano es inmutable. Ningún suceso posterior puede modificar retroactivamente un suceso ya fijado en la trayectoria.**

Por tanto, si $S_{1}$ ya ha sido fijado como suceso soberano de la trayectoria, entonces ningún $S_{n}$ con $n > 1$ puede convertirlo en "no ocurrido". La operación

$$
S_{4} \Rightarrow \neg S_{1}
$$

es **ilegal en el SV**: no es paradójica, sino estructuralmente inválida.

El SV no "resuelve" la paradoja por una pirueta. La **disuelve** por prohibición estructural.

**4. Formulación rigurosa del fallo**

La paradoja del abuelo exige simultáneamente:

1. $S_{1}$ ocurrió.
2. $S_{4}$ hace que $S_{1}$ no haya ocurrido.

Es decir: $S_{1} \land (S_{4} \Rightarrow \neg S_{1})$, lo que obliga al sistema a tolerar que un suceso posterior altere el estatuto de verdad de un suceso anterior ya fijado. El SV responde que $S_{4}$ sólo puede producir un nuevo suceso:

$$
S_{4} \Rightarrow S_{5}
$$

donde $S_{5}$ es un **nuevo suceso**, no una anulación retroactiva de $S_{1}$.

**5. Las tres respuestas posibles del SV**

**Caso A — Imposibilidad estructural.** Si la trayectoria intentada hace depender la existencia de un suceso de la anulación de sus propias condiciones ya fijadas, el dictamen es NO APTO. La trayectoria es estructuralmente incompatible.

**Caso B — Nuevo ramo factual.** $S_{4}$ no modifica $S_{1}$; sólo puede generar un nuevo suceso compatible:

$$
S_{1} \rightarrow S_{2} \rightarrow S_{3} \rightarrow S_{4} \rightarrow S_{5}
$$

Lo posterior sucede; no reescribe.

**Caso C — Indeterminación honesta $U$.** Si no hay base suficiente para clasificar el tipo exacto de interacción entre $S_{4}$ y la trayectoria previa, el SV no fuerza un cierre. El símbolo $U$ comparece: no hay base para afirmar retroescritura, cancelación ni imposibilidad concreta.

**6. El punto donde la paradoja clásica colapsa**

La paradoja sólo funciona si se aceptan tres licencias: que el tiempo es una variable ontológicamente soberana, que la trayectoria puede ser retroescrita y que un efecto puede destruir la condición ya fijada de su propia aparición. El SV niega las tres. La paradoja **no llega a nacer plenamente** dentro del sistema.

**7. Test formal mínimo — SV-TEMP-01**

| Elemento | Contenido |
|---|---|
| Trayectoria | $S_1$: existencia del abuelo · $S_2$: generación de la línea familiar · $S_3$: nacimiento del nieto · $S_4$: acción del nieto contra el abuelo |
| Pretensión clásica | $S_{4} \Rightarrow \neg S_{1}$ |
| Regla 1 — Inmutabilidad | $S_{1}$ ya fijado $\Rightarrow$ no reescribible |
| Regla 2 — No retroclausura | $S_{4} \not\Rightarrow$ anulación de la trayectoria previa |
| Salida válida | $S_{4} \Rightarrow S_{5}$ o bien $S_{4} \Rightarrow U$ |
| Dictamen | La paradoja no es una contradicción del SV; es una trayectoria inválida o mal planteada bajo el régimen del suceso soberano. |

### Ejemplo doctrinal 2. Medición no equivale a ontología

Una magnitud medible puede ser indispensable para operar y, sin embargo, no merecer rango constitutivo. Una regla mide una longitud sin crearla; un reloj mide una duración sin fundar por ello la ontología del dominio. Del mismo modo, el **Medidor factual de ciclo** normaliza la recurrencia factual, pero no funda la estructura del sistema. Esta distinción es decisiva para el presente documento: la ecuación factual de onda electromagnética emplea medición factual y metrología explícita, pero no se deja gobernar por tiempo soberano.

### Función de esta sección en el documento

La presente sección no sustituye a la Introducción ni al apartado I. Su función es fijar, antes de la arquitectura formal del documento, el régimen canónico de lectura bajo el cual deben entenderse sus variables, sus operadores y sus ejemplos. Con ello, el lector recibe desde el principio una compuerta doctrinal nítida: el documento no traslada sin más una teoría previa al SV; obliga a reexpresar lo que toma bajo un régimen más estricto de suceso, trayectoria, recurrencia estructural, medición factual subordinada e indeterminación honesta.

---

## I. Estatuto, alcance y cautelas

El documento es una documento especializado, subordinada y verificable dentro del Sistema Vectorial SV. Su alcance queda restringido al **electromagnetismo factual del Sistema Vectorial SV** como dominio director. Quedan fuera del cuerpo demostrativo gravedad discreta, ondas gravitacionales, sector de Higgs, frontera cuántica y toda teoría de campo unificado.

La delimitación negativa del documento es fuerte: no introduce tiempo soberano, probabilidad, minería de datos, inferencia opaca, heurística no declarada ni clausura espuria de `U`. Toda analogía con Fourier, Parseval, Gibbs o la ecuación de onda clásica es comparativa y externa, nunca soberana. En particular, el presente documento establece con evidencia laboratorial el residual de borde factual; la sobreoscilación factual fuerte queda, cuando proceda, como régimen parcial o candidato de trabajo y no como cierre más amplio ya demostrado en todos los casos del estudio.

---

## II. Primitivos metrológicos, semántica dimensional y mapeo factual electromagnético del SV

La ecuación factual de onda electromagnética exige una disciplina metrológica explícita. Para este frente bastan cuatro primitivos: **UE_MFC**, **UFE**, **UFM** y **UFC**. La delimitación negativa constitutiva debe preservarse: adoptar una constante ancla para fijar una unidad factual no importa, por ello sólo, la teoría física de origen como verdad constitutiva del SV.

La codificación visible del polígono y la metrización factual tampoco deben confundirse: los radios auxiliares pertenecen al plano visible; las magnitudes expresadas en **UE_MFC**, **UFE**, **UFM** y **UFC** pertenecen al plano metrológico del sistema.

---

## III. Suelo matemático mínimo: célula canónica, polígono, módulo y ángulo

Sobre la célula canónica `SV(3,9)` se adopta la codificación visible canónica

$$
\rho(0)=1,\qquad \rho(1)=2,\qquad \rho(U)=3,
$$

con vértices

$$
V_i(v)=\left(\rho(v_i)\cos\theta_i,\rho(v_i)\sin\theta_i\right),\qquad
\theta_i=\frac{2\pi(i-1)}{9}.
$$

La masa radial visible queda definida por

$$
\mu_\rho(v):=\sum_{i=1}^{9}\rho(v_i)=9+N_1(v)+2N_U(v),\qquad 9\le \mu_\rho(v)\le 27.
$$

Esta magnitud estratifica el espacio visible, pero no recompone por si sola la geometría del contorno ni la clase fuerte del sistema. Los ángulos canónicos fijan el orden cíclico del soporte y preparan el paso a los modos cíclicos factuales.

---

## IV. Electromagnetismo factual del Sistema Vectorial SV como dominio director

Las ecuaciones de Maxwell no se introducen aquí como verdad constitutiva del Sistema Vectorial SV. Su presencia en este documento tiene estatuto de referencia física externa de contraste y de reorganización factual interna, sin desplazamiento de la autoridad doctrinal del sistema ni absorción acrítica del formalismo clásico.

El electromagnetismo factual del Sistema Vectorial SV es el dominio director del documento porque el corpus ya lo había señalado como primer ámbito físico de máxima exigencia. El problema obliga a tratar propagación, contorno, conservación de carga, residualidad y sensibilidad estructural. Por ello, el documento exige operadores propios de cambio, circulación, acumulación, residualidad y clausura factual.

El laboratorio director correspondiente queda fijado: **Maxwell factual sintético**. ED-EM-01 debe leerse desde aquí como un pulso electromagnético factual mínimo cuya evolución sobre ciclo y trayectoria poligonal obliga al sistema a tratar propagación y residualidad con aparato propio.

---

## V. Ciclo de Suceso y Medidor factual de ciclo como soporte no temporal

El **Ciclo de Suceso** no introduce periodicidad temporal externa, sino recurrencia estructural del polígono y del régimen del suceso. El **Medidor factual de ciclo** actúa como instrumento de normalización factual apoyado en el ciclo.

La regla rectora del documento es esta:


> **el Medidor factual de ciclo no sustituye al Ciclo de Suceso; se apoya en el.**


En consecuencia, la evolución de ED-EM-01 no se describe por un parámetro temporal externo, sino como sucesión de configuraciones factuales ordenadas sobre tramos compatibles del ciclo y comparadas bajo el medidor factual de ciclo.

---

## VI. Modos cíclicos factuales del campo electromagnético

Sea $X=\{X_i\}_{i=1}^{9}$ un observable factual escalar leído sobre el ciclo canónico de `SV(3,9)`. Definimos, para cada orden cíclico $m$,

$$
A_m[X]=\sum_{i=1}^{9}X_i\cos(m\theta_i),\qquad
B_m[X]=\sum_{i=1}^{9}X_i\sin(m\theta_i),
$$

y el modo cíclico factual de orden $m$ por

$$
\mathcal M_m[X]:=\left(A_m[X],B_m[X]\right),\qquad
M_m[X]:=\sqrt{A_m[X]^2+B_m[X]^2}.
$$

El orden cero viene dado por

$$
\overline X:=\frac{1}{9}\sum_{i=1}^{9}X_i.
$$

El primer modo capta sesgo factual; el segundo, axialidad factual; los modos superiores, estructura cíclica fina. Para una idealización puntual de ED-EM-01,

$$
E_i^{(0)}=E_\ast\,\delta_{i,j_0},
$$

se obtiene $M_m[E^{(0)}]=|E_\ast|$ para todo orden disponible: la localización factual extrema exige distribución modal extensa.

---

## VII. Desarrollo cíclico factual y transformada modal electromagnética

Definimos los coeficientes modales factuales normalizados

$$
\alpha_m[X]:=\frac{2}{9}\sum_{i=1}^{9}X_i\cos(m\theta_i),\qquad
\beta_m[X]:=\frac{2}{9}\sum_{i=1}^{9}X_i\sin(m\theta_i),\qquad m=1,2,3,4.
$$

Entonces el desarrollo cíclico factual de $X$ es

$$
X_i=\overline X+\sum_{m=1}^{4}\left(\alpha_m[X]\cos(m\theta_i)+\beta_m[X]\sin(m\theta_i)\right),\qquad i=1,\dots,9.
$$

La **transformada modal factual** se define por

$$
\mathcal T_{\mathrm{mf}}[X]:=\left(\overline X,\alpha_1[X],\beta_1[X],\alpha_2[X],\beta_2[X],\alpha_3[X],\beta_3[X],\alpha_4[X],\beta_4[X]\right).
$$

La transformada es invertible sobre la célula canónica. Para la reconstrucción truncada de orden $K$, definimos

$$
X_i^{[K]}:=\overline X+\sum_{m=1}^{K}\left(\alpha_m[X]\cos(m\theta_i)+\beta_m[X]\sin(m\theta_i)\right),
$$

y el residual modal factual puntual

$$
R_i^{[K]}[X]:=X_i-X_i^{[K]}.
$$

---

## VIII. Análisis armónico factual del SV

La **textura modal factual** de un observable $X$ queda dada por

$$
\left(|\overline X|,\,M_1[X],\,M_2[X],\,M_3[X],\,M_4[X]\right).
$$

El contenido radial cuantifica, el contenido angular ordena y el contenido modal estructura. Sobre esta base se introduce una clasificación por dominancia modal: fondo dominante, dominancia de primer orden, dominancia axial, dominancia armónica alta y mezcla modal.

Se definen también los índices

$$
D_m[X]:=\frac{M_m[X]}{|\overline X|+M_1[X]+M_2[X]+M_3[X]+M_4[X]},\qquad m=1,\dots,4,
$$

y

$$
C_{12}[X]:=\frac{M_1[X]+M_2[X]}{|\overline X|+M_1[X]+M_2[X]+M_3[X]+M_4[X]}.
$$

En ED-EM-01, la localización factual inicial produce una **mezcla modal extensa**, con presencia significativa de armónicos altos.

---

## IX. Balance factual modal: identidad SV de tipo Parseval

Definimos el **contenido cuadrático factual** de un observable $X$ por

$$
\mathcal Q[X]:=\sum_{i=1}^{9}X_i^2.
$$

Entonces se verifica la identidad de balance factual modal:

$$
\boxed{
\mathcal Q[X]=9\,\overline X^{\,2}+\frac{9}{2}\sum_{m=1}^{4}\left(\alpha_m[X]^2+\beta_m[X]^2\right)=9\,\overline X^{\,2}+\frac{9}{2}\sum_{m=1}^{4}M_m[X]^2.
}
$$

Para la reconstrucción truncada de orden $K$, definimos

$$
\mathcal Q^{[K]}[X]:=9\,\overline X^{\,2}+\frac{9}{2}\sum_{m=1}^{K}M_m[X]^2,
$$

y el residual modal cuadrático factual

$$
\mathcal R_{\mathrm{mod}}^{[K]}[X]:=\mathcal Q[X]-\mathcal Q^{[K]}[X]=\frac{9}{2}\sum_{m=K+1}^{4}M_m[X]^2.
$$

Para la idealización inicial de ED-EM-01, la identidad se verifica exactamente.

---

## X. Residual de borde factual y régimen preliminar de sobreoscilación

Definimos el residuo factual puntual de truncación por

$$
\Delta_i^{[K]}[X]:=X_i-X_i^{[K]}.
$$

Si $B\subset\{1,\dots,9\}$ designa el conjunto de posiciones que forman el borde factual considerado, introducimos

$$
\mathcal B^{[K]}[X;B]:=\max_{i\in B}|\Delta_i^{[K]}[X]|,
$$

$$
\mathcal Q_B^{[K]}[X]:=\sum_{i\in B}\left(\Delta_i^{[K]}[X]\right)^2,
$$

$$
\mathcal C_B^{[K]}[X]:=\frac{\mathcal Q_B^{[K]}[X]}{\sum_{i=1}^{9}\left(\Delta_i^{[K]}[X]\right)^2}.
$$

Diremos que existe **sobreoscilación factual** cuando la reconstrucción truncada desborda el rango factual inmediato de la transición original. En el ejemplo director ED-EM-01, el documento verifica de forma material el residual de borde factual y su concentración local; la sobreoscilación factual fuerte se mantiene en esta versión como régimen preliminar de comparación externa y no como cierre universal del caso director.

---

## XI. Ecuación factual de onda electromagnética en vacío factual

La evolución no se parametriza por $t$, sino por una abscisa factual de ciclo medido $\xi$, con dimensión

$$
[\xi]=\mathrm{UE\_MFC}.
$$

Para el caso director **ED-EM-01** y para la suite laboratorial asociada, el documento fija de forma canónica y explícita:

$$
\Delta \ell := 1\,\mathrm{UFE},
\qquad
c_{\mathrm{SV}} := 1\,\mathrm{UFE}\cdot \mathrm{UE\_MFC}^{-1}.
$$

Estas elecciones tienen estatuto operativo y laboratorial. No se presentan como cierre universal de la escala propagativa del SV, sino como normalización factual mínima del caso canónico, suficiente para la ejecución, la trazabilidad y la comparación de resultados dentro del presente documento.

Sobre la trayectoria poligonal canónica, definimos el operador factual de curvatura propagativa mínima

$$
(\Delta_{\Gamma}X)_i:=X_{i+1}-2X_i+X_{i-1},\qquad i=1,\dots,9,
$$

con cierre cíclico $X_{10}=X_1$ y $X_0=X_9$. En la dirección del ciclo medido, tomamos la segunda diferencia factual

$$
(\delta_{\xi}^2 X)_i(\xi):=X_i(\xi+\Delta \xi)-2X_i(\xi)+X_i(\xi-\Delta \xi).
$$

La **ecuación factual de onda electromagnética en vacío factual** se formula asi:

$$
\boxed{
\frac{(\delta_{\xi}^2 X)_i(\xi)}{(\Delta \xi)^2}=c_{\mathrm{SV}}^{\,2}\frac{(\Delta_{\Gamma}X)_i(\xi)}{(\Delta \ell)^2}
}\qquad i=1,\dots,9.
$$

Para lecturas escalarizadas del campo eléctrico factual y del campo magnético factual:

$$
\frac{(\delta_{\xi}^2 E)_i}{(\Delta \xi)^2}=c_{\mathrm{SV}}^{\,2}\frac{(\Delta_{\Gamma}E)_i}{(\Delta \ell)^2},
\qquad
\frac{(\delta_{\xi}^2 B)_i}{(\Delta \xi)^2}=c_{\mathrm{SV}}^{\,2}\frac{(\Delta_{\Gamma}B)_i}{(\Delta \ell)^2}.
$$

Cada orden modal satisface una ecuación desacoplada

$$
\frac{\delta_{\xi}^2 a_m}{(\Delta \xi)^2}+\Omega_m^2 a_m=0,\qquad
\frac{\delta_{\xi}^2 b_m}{(\Delta \xi)^2}+\Omega_m^2 b_m=0,
$$

con

$$
\Omega_m^2=\frac{4c_{\mathrm{SV}}^{\,2}}{(\Delta \ell)^2}\sin^2\!\left(\frac{\pi m}{9}\right).
$$

La propagación de ED-EM-01 puede leerse como evolución factual sobre la trayectoria y como evolución desacoplada de sus componentes modales.

**Condición inicial canónica del caso director.** Para la ejecución de ED-EM-01 se declaran explícitamente las dos condiciones iniciales que el esquema de segundo orden requiere:

$$
a_m(\xi=0) = \alpha_m^{(0)},\qquad
\frac{\delta_{\xi} a_m}{\Delta\xi}\bigg|_{\xi=0} = 0
\quad (\text{velocidad factual inicial nula}).
$$

La velocidad factual inicial nula se impone mediante el **arranque frío**: se toma $a_m(-\Delta\xi) := a_m(0)$, lo que en el primer paso produce

$$
a_m(\Delta\xi) = a_m(0)\,\left(1 - (\Delta\xi)^2\,\Omega_m^2\right).
$$

Esta condición no equivale a la condición general del problema de propagación; es la condición específica del caso director ED-EM-01, suficiente para la ejecución, la trazabilidad y la comparación de resultados dentro del presente documento.

---

## XII. Extensión controlada a medio homogéneo e isótropo

El documento deja abierta una **extensión controlada** a un **medio homogéneo e isótropo**, sin romper el dominio electromagnético factual, el soporte no temporal ni la metrización propia del SV. La deformación mínima consiste en sustituir $c_{\mathrm{SV}}$ por una velocidad factual efectiva del medio $v_{\mathrm{med}}$, con dimensión

$$
[v_{\mathrm{med}}]=\mathrm{UFE}\cdot\mathrm{UE\_MFC}^{-1}.
$$

La ecuación pasa a ser

$$
\boxed{
\frac{(\delta_{\xi}^2 X)_i(\xi)}{(\Delta \xi)^2}=v_{\mathrm{med}}^{\,2}\frac{(\Delta_{\Gamma}X)_i(\xi)}{(\Delta \ell)^2}
}\qquad i=1,\dots,9.
$$

La base modal no cambia; sólo cambia la escala propagativa modal:

$$
\Omega_{m,\mathrm{med}}^{2}=\frac{4v_{\mathrm{med}}^{\,2}}{(\Delta \ell)^2}\sin^2\!\left(\frac{\pi m}{9}\right).
$$

No se introducen aquí medios no homogéneos, anisótropos, pérdidas factuales ni condiciones de contorno materiales generales.

---

## XIII. Laboratorios mínimos reproducibles, runners, catálogo de errores y pseudocódigo doctrinal

La publicación debe ir acompañada de una **suite mínima reproducible**:

| ID | Titulo | Fichero MD | JSON congelado |
|---|---|---|---|
| LAB-EM-01 | Modos cíclicos factuales del campo electromagnético | `laboratorios/LAB-EM-01.md` | `laboratorios/json_congelados/lab-em-01.json` |
| LAB-EM-02 | Desarrollo cíclico factual y transformada modal electromagnética | `laboratorios/LAB-EM-02.md` | `laboratorios/json_congelados/lab-em-02.json` |
| LAB-EM-03 | Balance factual modal | `laboratorios/LAB-EM-03.md` | `laboratorios/json_congelados/lab-em-03.json` |
| LAB-EM-04 | Residual de borde factual | `laboratorios/LAB-EM-04.md` | `laboratorios/json_congelados/lab-em-04.json` |
| LAB-EM-05 | Ecuación factual de onda electromagnética | `laboratorios/LAB-EM-05.md` | `laboratorios/json_congelados/lab-em-05.json` |

Deben declararse al menos tres runners:

| Fichero | Función |
|---|---|
| `laboratorios/runners/runner_maestro_emf.py` | Suite completa LAB-EM-01 a LAB-EM-05 en régimen fail-fast |
| `laboratorios/runners/runner_rapido_emf.py` | Verificación rápida de propagación (2 pasos) |
| `laboratorios/runners/runner_ed_em_01.py` | Ejecución completa del caso director ED-EM-01 |
| `laboratorios/runners/sv_emf_core.py` | Librería central: transformada modal, propagación, freeze_json |

Entradas mínimas:

- identificador del caso factual;
- dominio: vacío factual o medio homogéneo e isótropo;
- trayectoria poligonal compatible;
- observable factual de entrada `E_SV` o `B_SV`, o residual asociado;
- parámetros del ciclo factual y del medidor factual de ciclo;
- parámetros materiales, sólo cuando proceda;
- perturbaciones declaradas, si las hubiera.

Salidas obligatorias:

- coeficientes modales factuales;
- reconstrucción exacta o truncada;
- contenido cuadrático factual y balance modal;
- residual puntual y residual de borde;
- evolución propagativa factual;
- dictamen local;
- custodia factual;
- huella de integridad;
- fichero JSON congelado.

Catálogo mínimo de errores:

- **EMF-001** — Trayectoria factual no compatible.
- **EMF-002** — Observable sin homogeneidad dimensional.
- **EMF-003** — Parámetro material no declarado.
- **EMF-004** — Transformada modal factual no invertible en ejecución.
- **EMF-005** — Balance factual modal inconsistente.
- **EMF-006** — Residual de borde factual fuera de régimen esperado.
- **EMF-007** — Propagación factual no estable bajo el runner.
- **EMF-008** — Excepción no controlada en laboratorio.
- **EMF-009** — Salida JSON no congelada o huella ausente.
- **EMF-010** — Dictamen local ausente o estado inválido.

Pseudocódigo doctrinal maestro:

```text
PROCEDIMIENTO GOBERNAR_ED_EM_01

ENTRA:
    caso := ED-EM-01
    dominio := VACIO_FACTUAL
    trayectoria := TRAYECTORIA_POLIGONAL_CANONICA_SV_3_9
    observable := CAMPO_ELECTROMAGNETICO_FACTUAL_INICIAL
    escala_ciclo := UE_MFC
    escala_extension := UFE
    parámetros_materiales := NULO

DECLARA:
    exigir COMPATIBILIDAD_DE_TRAYECTORIA
    exigir HOMOGENEIDAD_DIMENSIONAL
    exigir CUSTODIA_DE_ENTRADA

EJECUTA:
    1. LEER_CONFIGURACION_FACTUAL(caso, trayectoria, observable)
    2. MEDIR_EN_CICLO_FACTUAL(escala_ciclo)
    3. PROYECTAR_A_MODOS_CICLICOS_FACTUALES(observable)
    4. RECONSTRUIR_EN_REGIMEN_COMPLETO
    5. CALCULAR_BALANCE_FACTUAL_MODAL
    6. TRUNCAR_A_ORDEN_DECLARADO
    7. MEDIR_RESIDUAL_DE_BORDE_FACTUAL
    8. PROPAGAR_EN_REGIMEN_DE_ONDA_FACTUAL
    9. COMPARAR_ESTADO_INICIAL_Y_ESTADO_PROPAGADO
   10. EMITIR_DICTAMEN_LOCAL
   11. CONGELAR_SALIDA_JSON
   12. SELLAR_HUELLA_DE_INTEGRIDAD

NO_TOLERA:
    trayectoria_incompatible
    observable_sin_dimension
    importacion_fallida
    excepcion_no_controlada
    salida_no_congelada
    passed_false

SALE:
    transformada_modal_factual
    balance_factual_modal
    residual_de_borde_factual
    estado_propagado
    dictamen_local
    huella_de_integridad
FIN
```

Pseudocódigo del runner maestro:

```text
PROCEDIMIENTO RUNNER_MAESTRO_EMF

DECLARA:
    suite := [LAB-EM-01, LAB-EM-02, LAB-EM-03, LAB-EM-04, LAB-EM-05]
    invariantes_obligatorios :=
        [autoria_presente,
         trayectorias_compatibles,
         dimensiones_homogéneas,
         salidas_congeladas,
         huellas_validas]

PARA cada laboratorio EN suite HACER:
    EJECUTAR(laboratorio)
    SI FALLA(laboratorio) ENTONCES
        REGISTRAR_ERROR
        CORTAR_EN_REGIMEN_FAIL_FAST
    FIN_SI
    VERIFICAR(invariantes_obligatorios)
    SI ALGUN_INVARIANTE_NO_PASA ENTONCES
        REGISTRAR_ERROR
        CORTAR_EN_REGIMEN_FAIL_FAST
    FIN_SI
FIN_PARA

EMITIR_REPORTE_GLOBAL_JSON
EMITIR_DICTAMEN_FINAL
SELLAR_HUELLAS_DE_INTEGRIDAD

FIN
```

La publicación debe ofrecer una implementación de referencia en Python, pero sin depender semánticamente de Python para expresarse.

---

## XIV. Apertura prudente hacia una formulación SV del problema de campo unificado

Este apartado **no forma parte del objeto demostrativo** del documento. No introduce una teoría de campo unificado del Sistema Vectorial SV ni una nueva física general del sistema. Sólo deja planteada, con prudencia extrema, una posibilidad futura: examinar si el aparato ya consolidado del documento permite expresar o reordenar semánticamente el problema clásico de la unificación electromagnetismo-gravedad dentro del léxico del SV.

Una futura línea sobre campo unificado en clave SV no podrá introducir tiempo soberano, ni importar sin control relatividad, mecánica cuántica, teoría gauge o geometría diferencial como si fueran verdad constitutiva del sistema, ni presentar analogías estructurales como equivalencias físicas demostradas.

---

## XV. Discusión, límites y cuestiones abiertas

Quedan establecidos cinco resultados principales:

1. el **electromagnetismo factual del Sistema Vectorial SV** queda fijado como dominio director legítimo de la publicación;
2. la construcción entera del documento queda anclada en un régimen no temporal, gobernado por el **Ciclo de Suceso** y el **Medidor factual de ciclo**, y en una metrización factual explícita basada en **UE_MFC**, **UFE**, **UFM** y **UFC**;
3. la célula canónica `SV(3,9)` y su desarrollo cíclico factual bastan para construir un aparato modal interno del SV;
4. queda establecida una **identidad de balance factual modal** de tipo Parseval, internamente formulada y verificada sobre ED-EM-01;
5. queda fijada una **ecuación factual de onda electromagnética en vacío factual**, con extensión controlada a medio homogéneo e isótropo.

No queda demostrada todavía una teoría factual completa de Maxwell. Tampoco queda cerrada una teoría general del análisis armónico factual del SV más allá de la célula canónica y de su trayectoria poligonal mínima. El residual de borde factual queda formulado y cuantificado, pero no agotado en todos sus regímenes posibles. Permanece abierta, además, la integración laboratorial completa del documento bajo la suite prevista. Permanece abierta asimismo la generalización no canónica de $c_{\mathrm{SV}}$ y de $\Delta \ell$ más allá de la normalización operativa fijada para **ED-EM-01**; en el presente documento ambos quedan establecidos de manera explícita sólo para el caso canónico y para su infraestructura de ejecución reproducible.

**Nota sobre el contenido cuadrático en la propagación factual.** En LAB-EM-05 se observa que el contenido cuadrático $\mathcal{Q}[X](\xi) = \sum_i X_i(\xi)^2$ varía de forma no monótona entre pasos de ciclo. Esta variación es matemáticamente esperada y no constituye inestabilidad. El esquema leapfrog discreto no conserva $\mathcal{Q}$, sino una energía escalonada discreta distinta: para cada modo, $E_m^{(n)} = \frac{1}{2}(a_m^{(n+1)} - a_m^{(n)})^2/(\Delta\xi)^2 + \frac{\Omega_m^2}{2}\,a_m^{(n)}\,a_m^{(n+1)}$. Esta es la cantidad que permanece acotada cuando el número de Courant cumple $\Delta\xi\,\Omega_m \le 2$. En ED-EM-01, el número de Courant canónico es $\approx 0{,}985$, estrictamente inferior a 2, lo que garantiza la estabilidad del esquema.

Dictamen global:


> **El documento cierra con solidez una primera teoría cíclico-modal factual del campo electromagnético sobre la célula canónica del SV, pero no clausura todavía una teoría electromagnética factual completa del sistema.**


---

## XVI. Conclusión

El presente documento ha desarrollado, dentro del Sistema Vectorial SV, una formulación cíclico-modal factual del electromagnetismo sobre la célula canónica, el ciclo factual, la medición factual y la trayectoria poligonal de activación. Ha construido un aparato modal factual completo sobre `SV(3,9)`, metrización explícita mediante **UE_MFC**, **UFE**, **UFM** y **UFC**, una identidad de balance factual modal, un residual de borde factual y una primera ecuación factual de onda electromagnética en vacío factual, con extensión controlada a medio homogéneo e isótropo.

El resultado principal del documento puede fijarse asi:


> **El Sistema Vectorial SV dispone ya, sobre la célula canónica y bajo régimen factual no temporal, de una primera teoría cíclico-modal factual del electromagnetismo capaz de sostener una ecuación factual de onda electromagnética en vacío factual, sin abandonar su gramática doctrinal ni su metrología propia.**


Y, con igual necesidad, debe añadirse la cláusula complementaria:


> **Este cierre no equivale todavía a una teoría electromagnética factual completa del SV, sino al establecimiento riguroso de su núcleo inicial más fértil, reproducible y doctrinalmente legítimo.**


---

## Fourier factual y ecuación de onda electromagnética en el Sistema Vectorial SV: reflexiones finales

El presente documento no debe leerse como un mero traslado de la ecuación de onda o del sistema metrológico moderno al Sistema Vectorial SV mediante un cambio de símbolos o de nombres. Si su operación se redujera a eso, su alcance sería trivial. Su pretensión es otra y más precisa: obligar a que toda formulación acogida por el sistema sea reinterpretada bajo el régimen del **suceso**, de la **trayectoria**, de la **recurrencia estructural**, de la **medición factual subordinada** y de la **indeterminación honesta**.

Esta exigencia tiene una consecuencia doctrinal de primer orden: el SV rechaza el tiempo como primitiva soberana. No niega por ello la utilidad funcional de ciertas magnitudes de medición temporal; niega que una variable de medición o de parametrización pueda convertirse, sin más, en fundamento constitutivo del dominio. En el SV, la unidad soberana no es el tiempo, sino el suceso. Un suceso ya fijado es inmutable: no se corrige retroactivamente ni se deja reescribir por otro posterior. Si una configuración reaparece, comparece como un nuevo suceso de la trayectoria. Esta disciplina impide que el sistema se apoye en retroproyecciones, reindexaciones o clausuras ontológicas no justificadas.

La prueba doctrinal más clara de esta exigencia es el test de la llamada paradoja del abuelo. Cuando una narrativa temporal permite que un estado posterior destruya la condición de posibilidad que lo hizo comparecer, lo que aparece no es una profundidad teórica superior, sino una fragilidad de fundamento: una variable instrumental ha sido elevada a principio soberano y termina reescribiendo la trayectoria que debía limitarse a medir. El SV bloquea esa operación de manera estructural. Lo posterior puede suceder; no puede reescribir soberanamente lo ya sucedido. Y, donde no hay base suficiente para decidir, el sistema no inventa una clausura elegante: responde con $U$, esto es, con indeterminación honesta.

Bajo esta luz, el alcance real del documento se hace más nítido. Fourier factual, la transformada modal factual, el balance factual modal, el residual de borde factual y la ecuación factual de onda electromagnética no se proponen como rebautizo triunfalista de matemáticas conocidas, sino como intento de someter formulaciones ya poderosas a un régimen más estricto de lectura. El SV no proclama aquí una superioridad empírica demostrada sobre la física moderna. Lo que si hace es imponer una compuerta: toda formulación que entre en su dominio debe hacerse responsable de sus sucesos, de su trayectoria, de su soporte metrológico y de sus zonas de no-clausura.

Si esta exigencia resulta fecunda, el documento habrá conseguido algo suficiente y serio: no inventar una física nueva por decreto, sino ofrecer un marco en el que ciertas formulaciones físicas puedan ser reconsideradas bajo una disciplina más sobria respecto de sus variables, sus cierres y sus contradicciones aparentes. Esa es, en este punto, la fuerza real del Sistema Vectorial SV y también el límite que honestamente se le reconoce.

---

## Glosario consolidado de terminología, acrónimos, magnitudes y unidades factuales

### A. Léxico doctrinal del SV

**Cambio factual.** Cambio tratado dentro del aparato formal del SV, con régimen explícito de compatibilidad.

**Ciclo de Suceso.** Recurrencia estructural del polígono o del régimen del suceso.

**Clausura factual.** Cierre o dictamen de un dominio bajo las reglas expresas del sistema.

**Detonación.** Cambio local o frontera cuya intensidad estructural altera el régimen de lectura o de reconstrucción.

**Directriz.** Dirección o gobierno estructural del cambio factual en sentido fuerte del aparato del SV.

**Frontera factual.** Régimen explícito de cierre y comparación de un dominio o una trayectoria.

**Residual factual.** Diferencia estructural no absorbida por una formulación, reconstrucción o clausura.

**Trayectoria poligonal de activación.** Soporte discreto estructurado donde se distribuyen activaciones, recorridos y acumulaciones factuales.

### B. Léxico cíclico-modal del documento

**Análisis armónico factual.** Lectura estructural del reparto modal de un observable factual sobre la célula canónica y su trayectoria.

**Balance factual modal.** Identidad de correspondencia entre el dominio factual y el dominio modal del observable.

**Desarrollo cíclico factual.** Expansión finita exacta del observable sobre los órdenes cíclicos del soporte canónico.

**Dominancia modal.** Régimen en el que un orden modal prevalece estructuralmente sobre el resto.

**Ecuación factual de onda electromagnética.** Ecuación de propagación del documento formulada sobre ciclo medido y trayectoria poligonal.

**Modo cíclico factual.** Componente modal propia del SV sobre el ciclo canónico, leída sin tiempo soberano.

**Residual de borde factual.** Residuo reconstructivo concentrado en una transición abrupta, frontera o detonación factual.

**Transformada modal factual.** Operador que lleva el observable del dominio factual al dominio modal cíclico.

### C. Acrónimos y abreviaturas

**ED-EM-01.** Ejemplo director del documento: pulso electromagnético factual localizado sobre `SV(3,9)` en vacío factual.

**UE_MFC.** Unidad Elemental del Medidor Factual de Ciclo.

**UFE.** Unidad Factual de Extensión.

**UFM.** Unidad Factual de Masa.

**UFC.** Unidad Factual de Corriente.

**UFT.** Unidad Factual de Temperatura.

**UFCE.** Unidad Factual de Cantidad de Entidad.

### D. Magnitudes y dimensiones

$$
[T]=\mathrm{UE\_MFC},\qquad [L]=\mathrm{UFE},\qquad [M]=\mathrm{UFM},\qquad [I]=\mathrm{UFC}.
$$

$$
[v_{\mathrm{SV}}]=\mathrm{UFE}\cdot \mathrm{UE\_MFC}^{-1}.
$$

$$
[E_{\mathrm{SV}}]=\mathrm{UFM}\cdot \mathrm{UFE}\cdot \mathrm{UFC}^{-1}\cdot \mathrm{UE\_MFC}^{-3}.
$$

$$
[B_{\mathrm{SV}}]=\mathrm{UFM}\cdot \mathrm{UFC}^{-1}\cdot \mathrm{UE\_MFC}^{-2}.
$$

### E. Correspondencias externas controladas

**Modo cíclico factual** se corresponde externamente, de forma controlada, con un modo de Fourier discreta.

**Balance factual modal** es comparable externamente con una identidad de tipo Parseval.

**Residual de borde factual** designa el residuo reconstructivo concentrado en una transición abrupta, una frontera o una detonación factual. En esta versión del documento, su comparación externa con el fenómeno de Gibbs debe leerse como correspondencia parcial y preliminar, no como identidad fuerte ya demostrada.

**Ecuación factual de onda electromagnética** mantiene correspondencia externa con una ecuación de onda clásica discreta, sin depender doctrinalmente de ella.

---

## Laboratorios

Suite mínima reproducible que acompaña al documento. Cada laboratorio tiene su propio fichero Markdown, su JSON congelado con huella MD5 autosellada y se ejecuta desde el runner Python de referencia.

### [LAB-EM-01 — Modos cíclicos factuales del campo electromagnético](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-01.md)

Calcula y verifica los coeficientes modales del campo escalarizado sobre `SV(3,9)`. Comprueba que todos los módulos $M_m$ son iguales para un pulso delta y que la reconstrucción exacta tiene error $< 10^{-12}$.

Fichero: [`LAB-EM-01.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-01.md) · JSON: [`lab-em-01.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/json_congelados/lab-em-01.json)

### [LAB-EM-02 — Desarrollo cíclico factual y transformada modal electromagnética](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-02.md)

Construye la transformada modal completa y las reconstrucciones truncadas $K = 0, 1, 2, 3, 4$. Verifica que los residuos cuadráticos decrecen monótonamente con $K$ y que la reconstrucción exacta ($K=4$) tiene error $< 10^{-12}$.

Fichero: [`LAB-EM-02.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-02.md) · JSON: [`lab-em-02.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/json_congelados/lab-em-02.json)

### [LAB-EM-03 — Balance factual modal](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-03.md)

Verifica la identidad de balance factual modal (tipo Parseval). Diferencia absoluta entre ambos lados igual a cero.

Fichero: [`LAB-EM-03.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-03.md) · JSON: [`lab-em-03.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/json_congelados/lab-em-03.json)

### [LAB-EM-04 — Residual de borde factual](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-04.md)

Calcula el residual de borde factual para $K = 0, 1, 2, 3$ sobre el conjunto de borde $\{1, 2, 3\}$. Verifica convergencia del borde máximo con $K$ y concentración de borde en $[0,1]$.

Fichero: [`LAB-EM-04.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-04.md) · JSON: [`lab-em-04.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/json_congelados/lab-em-04.json)

### [LAB-EM-05 — Ecuación factual de onda electromagnética](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-05.md)

Propaga el pulso ED-EM-01 durante 6 pasos de ciclo factual mediante el esquema leapfrog. Condición inicial: velocidad factual nula. Verifica estabilidad (número de Courant < 2).

Fichero: [`LAB-EM-05.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/LAB-EM-05.md) · JSON: [`lab-em-05.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/json_congelados/lab-em-05.json)

### Runner maestro

[`runner_maestro_emf.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios/runners/runner_maestro_emf.py) — ejecuta la suite completa en régimen fail-fast y produce el reporte global con huellas MD5 autoselladas.

## Bibliografía

Cooley, J. W., & Tukey, J. W. (1965). An algorithm for the machine calculation of complex Fourier series. *Mathematics of Computation, 19*(90), 297–301.

Einstein, A. (1950). *The meaning of relativity* (5th ed.). Princeton University Press.

Fourier, J. (1822/2009). *The analytical theory of heat*. Cambridge University Press.

Gibbs, J. W. (1899). Fourier's series. *Nature, 59*, 606.

Jackson, J. D. (1999). *Classical electrodynamics* (3rd ed.). Wiley.

Kreyszig, E. (2011). *Advanced engineering mathematics* (10th ed.). Wiley.

Lloret Egea, J. A. (2026a). *Fundamentos algebraico-semánticos del Sistema Vectorial SV* [Documento de trabajo del corpus SV].

Lloret Egea, J. A. (2026b). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV* [Documento rector en fase de publicación].

Lloret Egea, J. A. (2026c). *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador* [Documento de trabajo del corpus SV].

Lloret Egea, J. A. (2026d). *Primitivos metrológicos del Sistema Vectorial SV* [Documento de trabajo del corpus SV].

Maxwell, J. C. (1873). *A treatise on electricity and magnetism* (Vols. 1–2). Clarendon Press.

Oppenheim, A. V., Schafer, R. W., & Buck, J. R. (1999). *Discrete-time signal processing* (2nd ed.). Prentice Hall.

Parseval, M.-A. (1806). Memoire sur les series et sur l'integration complete d'une equation aux differences partielles lineaires. *Memoires presentes a l'Institut des Sciences, Lettres et Arts, par divers savants, et lus dans ses assemblees*, *1*, 638–648.

Strang, G. (1993). The discrete cosine transform. *SIAM Review, 41*(1), 135–147.

Trefethen, L. N. (2000). *Spectral methods in MATLAB*. SIAM.

Yee, K. S. (1966). Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media. *IEEE Transactions on Antennas and Propagation, 14*(3), 302–307).
