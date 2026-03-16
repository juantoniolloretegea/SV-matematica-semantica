.
<!-- PubPub import: usar este archivo junto con las imágenes `figura_1_R2.png` y `figura_2_R3.png` en la misma carpeta o en el mismo paquete ZIP. -->
<!-- Header superior sugerido: IA eñ ™ - (La Biblia de la IA - The Bible of AI ™ ISSN 2695-6411) • Sistema Vectorial SV: matemática y semántica -->

# Análisis del comportamiento geométrico del polígono del Sistema Vectorial SV: del plano cartesiano a una carta espacial afín auxiliar como vía de razonamiento para situaciones complejas

## Levantamiento geométrico, métricas discretas y criterio de validez relativa en la célula ternaria SV

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Institución:** Instituto tecnológico virtual de la Inteligencia Artificial para el español ™ (ITVIA)  
**Versión:** 1.0.0  
**Lugar y fecha:** Madrid, 16/03/2026  
**Estado:** Texto técnico de investigación

---

## Resumen

Este trabajo estudia si la elevación auxiliar del polígono ternario del Sistema Vectorial SV desde la carta polar plana habitual a una carta espacial en R³ puede utilizarse como vía de razonamiento matemático para situaciones complejas sin alterar la ontología canónica del sistema. La hipótesis de partida es estricta: la célula SV sigue siendo un objeto ternario exacto, U no se convierte en magnitud continua ni en infinito, y la tercera coordenada se introduce únicamente como recurso de carta para separar geométricamente el régimen de no determinación actual respecto del plano de determinación. Sobre esa base se formalizan dos aplicaciones: Phi_2, que representa la célula en el plano polar, y Phi_3, que la eleva a una carta espacial auxiliar con altura finita h. A continuación se definen cinco magnitudes discretas explotables —L₂, L₃, ΔL, Cz, E_rho y Ez— y se distinguen con precisión sus alcances. Se demuestra de forma exacta que Ez(v,h)=k(v)·h², donde k(v) es el número de transiciones verticales del polígono elevado, lo que asegura invarianza exacta de rango para Ez frente a variaciones de h. Para ΔL se obtiene un resultado más prudente: monotonicidad y estabilidad empírica en la batería ensayada, sin elevar esa observación a teorema universal. El programa incorpora además dos criterios de falsación: la no discriminación entre configuraciones semánticamente distintas y la mera redundancia respecto de la información ya disponible en R². El caso de estudio v=(1,1,1,1,1,1,1,0,U), con n=9=3², muestra que la carta elevada no resuelve por sí sola la semántica del sistema, pero sí hace visible y medible una diferencia geométrica que en el plano aparece comprimida. La conclusión es afirmativa y matizada: la elevación a R³ no debe promoverse a ontología nueva, pero sí merece consolidarse como técnica matemática auxiliar de laboratorio dentro del marco ternario vigente.

**Palabras clave:** Sistema Vectorial SV; célula ternaria; polígono polar; levantamiento geométrico; carta auxiliar; R²; R³; U; no determinación actual; geometría discreta

## 1. Introducción

El Sistema Vectorial SV trabaja, en su nivel canónico, con una célula exacta formada por parámetros ternarios y con una representación polar cerrada cuya finalidad no es ornamental, sino epistémica y auditiva. La imagen poligonal permite que el razonamiento humano y el razonamiento algorítmico recorran una misma figura visible y estable. Esta decisión de diseño es una de las piezas más características del sistema: la representación no sustituye a la semántica, pero la hace verificable.

Dentro de ese marco, el signo U expresa no determinación actual. No representa un número, no es una probabilidad parcial y no puede tratarse como un valor continuo situado entre 0 y 1. Sin embargo, cuando la célula se dibuja en la carta polar plana, U comparte el mismo plano geométrico que los estados determinados. Esa coexistencia es útil para la visualización general, pero puede comprimir diferencias estructurales cuya lectura interesa cuando el problema es complejo.

La cuestión que aquí se aborda es, por tanto, concreta: si ciertas configuraciones ternarias que en la carta polar plana se muestran geométricamente comprimidas admiten una representación auxiliar en R³ que las haga más legibles sin alterar el estatuto semántico del sistema. La comparación es análoga, en espíritu matemático, a los cambios de variable o de carta que permiten tratar en un dominio auxiliar fenómenos que, en su dominio inmediato, no se separan con claridad suficiente.

La tesis defendida en este artículo es la siguiente: la elevación geométrica a R³ es legítima como técnica auxiliar de laboratorio siempre que se mantengan cuatro cautelas. Primero, separación estricta entre objeto semántico y carta geométrica. Segundo, análisis explícito de la dependencia respecto del parámetro de elevación h. Tercero, fijación de criterios de falsación que permitan descartar la técnica si no añade valor real. Cuarto, rechazo expreso de cualquier relectura ontológica de U a partir de la tercera coordenada.

## 2. Marco doctrinal y matemático de partida

La célula exacta del Sistema Vectorial SV se define como 𝒮ₙ = {0,1,U}ⁿ, con la restricción arquitectónica n=b² y b≥3 [1]. Esta forma cuadrática no es decorativa: garantiza una organización angular regular y una lectura por capas estable. En el ejemplo de laboratorio utilizado en este trabajo se toma n=9=3², es decir, la forma (9,3) en el sentido preciso de nueve parámetros obtenidos como b² con base b=3.

El marco canónico distingue entre plano exacto y plano auxiliar [1]. En el plano exacto, la célula es un objeto semántico discreto. En el plano auxiliar, esa célula puede codificarse para fines geométricos, algebraicos o computacionales, siempre que dicha codificación no se confunda con la ontología primaria del sistema. Esta distinción es crucial para la legitimidad del presente trabajo, porque la coordenada espacial adicional no se atribuye a U como rasgo esencial, sino a la imagen Phi_3(U) como recurso de carta.

El documento canónico sobre la U precisa, además, que U nace como garantía formal de honestidad cognoscitiva: U significa “no lo sé” en sentido estricto, no duda psicológica, no estadística, no minería de datos y no promedio entre 0 y 1 [2]. A su vez, la pieza histórica sobre la frontera 0-1 deja fijado que la convención semántica canónica vigente 0/1/U no se modifica [3]. El presente artículo se mueve deliberadamente dentro de ese cierre: no propone un cuarto valor ni reabre la terna, sino que explora una carta auxiliar compatible con la doctrina vigente.

En ese contexto, la palabra “afín” se usa aquí en sentido geométrico y no doctrinal. La carta elevada no pretende introducir un nuevo origen semántico, sino trabajar sobre un espacio euclídeo tridimensional en el que la información angular del polígono se conserva y se añade una coordenada vertical finita de laboratorio.

## 3. Formulación geométrica del problema

Sea v=(v₁,…,vₙ) una célula ternaria exacta. Para cada parámetro Pᵢ se define el ángulo theta_i = 2π(i−1)/n. La carta polar plana Phi_2 se construye mediante una codificación radial auxiliar ρ sobre {0,U,1}. En este trabajo se adopta la convención de laboratorio rho(0)=1, rho(U)=2 y rho(1)=3. No se trata de una equivalencia ontológica, sino de una codificación visible que separa los tres signos sin convertirlos en magnitudes con el mismo estatuto.

La representación plana queda definida por la aplicación

Phi_2(Pᵢ=s) = (rho(s)·cos theta_i, rho(s)·sin theta_i).

La carta espacial auxiliar Phi_3 conserva la parte angular y radial de Phi_2, y añade una coordenada z(s) tal que z(0)=0, z(1)=0 y z(U)=h, con h>0. Por tanto,

Phi_3(Pᵢ=s) = (rho(s)·cos theta_i, rho(s)·sin theta_i, z(s)).

La interpretación correcta de esta construcción es la siguiente: el sistema no dice que U “valga h”, ni que U posea una cantidad de incertidumbre medible por z. Lo que se afirma es solo que, dentro de esta carta auxiliar, la no determinación actual sale del plano de determinación y puede estudiarse mediante efectos geométricos cuantificables. La elevación, en consecuencia, es un cambio de dominio de la representación, no un cambio de la ontología del sistema.

## 4. Magnitudes cuantitativas explotables

La utilidad de la elevación a R³ no puede quedar reducida a una impresión visual. Si la carta elevada ha de merecer un lugar estable en el laboratorio matemático del SV, debe producir magnitudes con lectura clara y con una relación explícita con el comportamiento del polígono. En esta investigación se consideran las siguientes.

Longitud plana: L₂ = Σ‖pᵢ₊₁−pᵢ‖. Mide el contorno del polígono en R².

Longitud espacial: L₃ = Σ‖qᵢ₊₁−qᵢ‖. Mide el contorno del polígono levantado en R³.

Exceso de elevación: ΔL = L₃ − L₂. Mide el sobrecoste geométrico introducido por la salida del plano.

Defecto global de coplanaridad: Cz = √[(1/n) Σ zᵢ²]. Resume cuánto se separa globalmente la figura respecto del plano z=0.

Energía radial discreta: E_rho = Σ(rho_i₊₁ − rho_i)². Mide la brusquedad radial entre estados consecutivos.

Energía vertical discreta: Ez = Σ(zᵢ₊₁ − zᵢ)². Mide la intensidad de las entradas y salidas del régimen U.

En prosa, estas magnitudes distinguen dos fenómenos que conviene no mezclar. Por un lado, la variación radial entre signos dentro de la misma carta plana. Por otro, el coste geométrico añadido cuando la no determinación actual abandona el plano. Si ambas familias de magnitudes terminaran diciendo exactamente lo mismo, la carta elevada carecería de justificación. Si, por el contrario, la parte vertical discrimina configuraciones que el plano comprime, entonces la técnica aporta una información nueva y útil.

## 5. Dependencia respecto de h y criterio de validez relativa

El parámetro de elevación h es una convención de carta y, por ello, cualquier explotación matemática seria debe analizar hasta qué punto condiciona las magnitudes construidas sobre Phi_3. El objetivo no es encontrar un valor “verdadero” de h —tal cosa no existe en el marco—, sino distinguir qué resultados son invariantes de rango y cuáles dependen de la elección concreta de la carta.

Para Ez el resultado es exacto. Sea k(v) el número de aristas del polígono elevado que conectan un vértice con z=0 y un vértice con z=h. Entonces

Ez(v,h) = k(v)·h².

La consecuencia es inmediata: para dos vectores v_A y v_B con k(v_A) ≠ k(v_B), se tiene Ez(v_A,h)/Ez(v_B,h)=k(v_A)/k(v_B) para todo h>0. El orden relativo de Ez depende solo del entero estructural k(v). El factor h² escala los valores absolutos, pero no cambia el rango comparativo. Este resultado sí puede presentarse como exacto y cerrado.

El caso de ΔL es más prudente. Cada arista que cruza el plano contribuye con δL(i,h)=√(d_xy(i)²+h²)−d_xy(i), donde d_xy(i) es la longitud plana de la arista correspondiente. Esta función es estrictamente creciente y convexa en h. De ahí se deduce que, para un vector fijo con al menos un U, ΔL crece con h. Lo que no se deduce automáticamente es que el orden relativo entre vectores distintos sea universalmente invariante, porque ese orden depende también de la geometría plana concreta de las aristas que cruzan el plano. Por ello, en este artículo se formula una afirmación restringida: la estabilidad de rango de ΔL queda tratada como resultado empírico de laboratorio, no como teorema general.

Sobre esa base, el programa adopta dos criterios de falsación. F1: si ΔL y Ez no discriminan entre configuraciones semánticamente distintas —por ejemplo, distinta densidad o distinta posición de U—, la carta elevada debe descartarse como herramienta clasificatoria. F2: si las magnitudes elevadas son monótonamente equivalentes a información ya computable en R² y no añaden estructura nueva, la elevación deja de tener valor matemático autónomo. Estos criterios son importantes porque convierten la hipótesis en programa de investigación y no en simple descripción gráfica.

## 6. Caso de estudio: la célula SV(9,3) v = (1,1,1,1,1,1,1,0,U)

El caso de estudio se toma sobre la célula de nueve parámetros v=(1,1,1,1,1,1,1,0,U). La elección no es arbitraria. Se evita el caso completamente determinado, se introduce un 0 y una U en posiciones contiguas, y se obliga a comparar, dentro del mismo ciclo angular, una caída a determinación baja seguida de una salida al régimen de no determinación actual.

En la carta polar plana, el vector produce una corona casi saturada por siete valores 1, una muesca profunda en P8=0 y un retorno parcial en P9=U. La figura es ya inteligible, pero la diferencia de régimen entre 0 y U permanece comprimida dentro de una misma familia radial. En la carta espacial auxiliar, en cambio, P9 deja de funcionar como simple radio intermedio y aparece como una salida finita de la coplanaridad. La información angular se conserva; lo que cambia es la legibilidad geométrica del signo U.

Para hacer comparables los números del ejemplo, se toma h=2,2 como valor de trabajo visual. Esta elección no pretende fijar una convención canónica, sino ofrecer una carta legible para el caso concreto.

![Figura 1. Carta polar plana auxiliar en R² para la célula de estudio.](figura_1_R2.png)

*Figura 1. Carta polar plana auxiliar en R² para la célula de estudio.*

![Figura 2. Carta espacial elevada en R³ para la célula de estudio.](figura_2_R3.png)

*Figura 2. Carta espacial elevada en R³ para la célula de estudio.*

**Tabla 1. Magnitudes geométricas del caso de estudio para h = 2,2.**

| Magnitud | Valor | Lectura |
|---|---:|---|
| L₂ | 17,980 | Longitud del contorno plano. |
| L₃ | 20,181 | Longitud del contorno elevado. |
| ΔL | 2,201 | Sobrecoste geométrico debido a la elevación. |
| Cz | 0,733 | Defecto global de coplanaridad. |
| E_rho | 6,000 | Brusquedad radial discreta. |
| Ez | 9,680 | Intensidad de las transiciones verticales. |

**Tabla 2. Sensibilidad del caso de estudio respecto del parámetro de elevación h.**

| h | ΔL(v,h) | Cz(v,h) | Ez(v,h) |
|---:|---:|---:|---:|
| 0,5 | 0,150 | 0,167 | 0,500 |
| 1,0 | 0,563 | 0,333 | 2,000 |
| 2,0 | 1,888 | 0,667 | 8,000 |
| 2,2 | 2,201 | 0,733 | 9,680 |
| 5,0 | 7,215 | 1,667 | 50,000 |
| 10,0 | 16,942 | 3,333 | 200,000 |

## 7. Discusión y alcance del resultado

La contribución principal del análisis no es haber “resuelto” la semántica del sistema en R³. El resultado más valioso es otro: haber mostrado que la elevación auxiliar permite distinguir con claridad dos planos conceptuales que, en R², pueden aparecer visualmente mezclados. El primero es el plano de la determinación: 0 y 1 permanecen en z=0. El segundo es el plano de la no determinación actual: U sale del plano no porque sea más grave ni más verdadero, sino porque la carta auxiliar necesita un grado de libertad adicional para representar su diferencia estructural.

Desde un punto de vista matemático, la técnica es fértil por tres razones. Primero, produce al menos una magnitud exacta de rango comparativo independiente de h: Ez. Segundo, ofrece un conjunto de indicadores discretos que pueden ponerse a prueba sobre familias de vectores: ΔL, Cz y E_rho. Tercero, conecta de forma natural con la idea clásica de cambio de dominio para hacer visible lo que la carta inicial comprime.

Desde un punto de vista doctrinal, la operación sigue siendo legítima porque no reescribe la terna, no convierte U en magnitud continua y no desplaza la célula exacta fuera de su estatuto canónico. El objeto sigue siendo ternario; la carta elevada es auxiliar.

Con todo, conviene subrayar un límite. La técnica no debe presentarse como resultado universalmente cerrado mientras la estabilidad comparativa de ΔL no haya sido validada sobre baterías más amplias y mientras F1 y F2 no se hayan ejecutado con amplitud suficiente. El programa queda, por tanto, abierto en su extensión, pero cerrado en su legitimidad mínima.

## Conclusión

El análisis permite afirmar, con base suficiente, que el levantamiento geométrico del polígono ternario del Sistema Vectorial SV desde la carta polar plana a una carta espacial auxiliar en R³ constituye una técnica matemática legítima y útil para el laboratorio del sistema. No se trata de una reforma ontológica ni de una vía para cuantificar U, sino de un procedimiento de representación que, sin alterar la semántica canónica 0/1/U, hace visible y medible una diferencia estructural que en el plano puede quedar comprimida. El resultado fuerte del estudio es exacto para Ez: su orden relativo entre vectores depende solo del número estructural de transiciones verticales y no del valor concreto de h. El resultado prudente afecta a ΔL: su monotonicidad está justificada y su estabilidad comparativa ha sido observada en la batería ensayada, pero no debe elevarse todavía a invariancia universal. Esta asimetría no debilita el programa; al contrario, lo vuelve científicamente más honesto. Por ello, el veredicto final del presente trabajo es afirmativo y preciso: la representación elevada debe incorporarse como técnica auxiliar de razonamiento y análisis geométrico dentro del marco ternario vigente, con continuidad investigadora, criterios de falsación explícitos y sin promoción indebida a rango doctrinal superior. El polígono SV sigue siendo el mismo objeto; lo que cambia es la calidad de la carta con la que ciertos casos complejos se dejan pensar.

## Referencias

[1] Lloret Egea, Juan Antonio. Fundamentos algebraico-semánticos del Sistema Vectorial SV. Instituto tecnológico virtual de la Inteligencia Artificial para el español ™ (ITVIA), versión 1.0.0, Madrid, 09/03/2026. Disponible en: https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv

[2] Lloret Egea, Juan Antonio. Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV. Instituto tecnológico virtual de la Inteligencia Artificial para el español ™ (ITVIA), versión 1.0.0, Madrid, 14/03/2026. Disponible en: https://www.itvia.online/pub/origen-doctrinal-definicion-y-alcance-de-la-u-en-el-sistema-vectorial-sv

[3] Lloret Egea, Juan Antonio. Desde la terna (0, 1, U) hasta la nueva frontera (0, 1, U, 0-1). Instituto tecnológico virtual de la Inteligencia Artificial para el español ™ (ITVIA), versión 1.0.0, Madrid, 14/03/2026. Disponible en: https://www.itvia.online/pub/desde-la-terna-0-1-u-hasta-la-nueva-frontera-0-1-u-0-1

[4] OpenStax. Calculus Volume 2. Sección 7.1, Parametric Equations. Rice University, 2016.

[5] OpenStax. Calculus Volume 3. Sección 1.3, Polar Coordinates. Rice University, 2016.

[6] Bobenko, Alexander I.; Suris, Yuri B. Discrete Differential Geometry: Integrable Structure. Graduate Studies in Mathematics, vol. 98. American Mathematical Society, 2008.
