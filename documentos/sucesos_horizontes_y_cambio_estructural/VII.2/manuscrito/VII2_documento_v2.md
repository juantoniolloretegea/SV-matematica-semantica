# VII.2 — Precedencia, compatibilidad y afectación entre sucesos admisibles en el Sistema Vectorial SV

**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Serie doctrinal:** Sistema Vectorial SV
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
**Publicación:** IA eñ™ – La Biblia de la IA™
**ISSN:** 2695-6411
**Fecha:** Madrid, 23 de marzo de 2026
**Pertenece a la colección:** <a href="https://www.itvia.online/sucesos-horizontes-y-cambio-estructural--una-aproximacion-algebraica-desde-el-sistema-vectorial-sv" target="_blank" rel="noopener noreferrer">Sucesos, horizontes y cambio estructural — Una aproximación algebraica desde el Sistema Vectorial SV</a>
**Licencia:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC-BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
**URL:** https://www.itvia.online/pub/vii2--precedencia-compatibilidad-y-afectacion-entre-sucesos-admisibles-en-el-sistema-vectorial-sv

![Figura 0. Mapa de nociones relacionales de VII.2.](figura_00_portada.svg)

*Figura 0. Mapa de nociones relacionales de VII.2.*

Figura 0. Las tres nociones se construyen en cadena —comparabilidad → afectación → precedencia— y desembocan en la Proposición 7.5: la precedencia es acíclica sobre Σⁿ = {0,1,U}ⁿ. La célula canónica (9,3) actúa como instancia verificable en todo el documento.

---

## Resumen

El Sistema Vectorial SV opera sobre células de la forma $(n, b)$ con $n = b^2$, cuyo espacio de estados es $\Sigma^n$ donde $\Sigma = \{0, 1, U\}$ es el alfabeto ternario canónico. Un *frame* es una configuración $S \in \Sigma^n$: un vector de $n$ componentes, cada una con valor $0$, $1$ o $U$. Sobre ese objeto concreto, los documentos anteriores de la serie VII han fijado el horizonte como cuádrupla, el suceso admisible como cuaterna y la composición como semigrupoid parcial.

El presente documento aborda el problema siguiente: dada una familia de sucesos admisibles sobre frames del SV, ¿qué estructura relacional mínima puede imponerse entre ellos sin reintroducir tiempo fuerte, sin invadir la teoría completa de cadenas y sin abandonar el suelo ternario? La respuesta se construye en cuatro capas: **comparabilidad legítima**, **afectación estratificada**, **precedencia estructural** y **compatibilidad derivada**. Cada noción se define en el nivel general $(n, b)$ con $n = b^2$ y se instancia canónicamente sobre la célula $(9, 3)$ —nueve componentes sobre la terna $\{0, 1, U\}$— que actúa como ejemplo singular verificable a lo largo del documento.

El resultado central es la **acíclicidad de la precedencia** (Proposición 7.5): en toda familia finita de sucesos admisibles sobre el SV, la relación de precedencia estructural no contiene ciclos. Esa propiedad, demostrada desde la terna y el *frame*, es la condición necesaria para que el documento VII.3 pueda definir después cadenas admisibles de sucesos sin circularidad.

**Palabras clave:** Sistema Vectorial SV; alfabeto ternario; *frame*; célula $(n,b)$; suceso admisible; horizonte; comparabilidad; afectación; precedencia; admisibilidad estructural.

---

## 0. Estatuto, alcance y criterio de lectura

Este documento ocupa una posición intermedia deliberadamente restringida en la serie VII. No redefine el suceso admisible fijado en VII.1 ni desarrolla todavía una teoría cerrada de cadenas, acumulación eventiva, límites o geometría reconstructiva. Su función es más precisa: introducir la **estructura relacional mínima** entre sucesos admisibles del SV, partiendo del objeto que el SV tiene como suelo propio —la célula ternaria $(n, b)$ con $n = b^2$— y sin perder ese contacto en ningún momento.

Toda afirmación pertenece a una de tres clases:

- Definición o proposición cerrada en esta pieza.
- Resultado justificado solo bajo hipótesis explícitas.
- Problema abierto reconocido como tal.

No existe cuarta clase oculta.

---

## 1. El suelo propio del SV: terna, frame y célula (n, b)

### 1.1. El alfabeto ternario y la célula

El Sistema Vectorial SV parte de un suelo semántico explícito: cada posición de una célula puede estar en uno de tres estados, y esa ternidad no es una convención sino una decisión arquitectónica. El alfabeto que la recoge es

$$\Sigma = \{0,\, 1,\, U\},$$

donde $0$ designa ausencia o no cumplimiento estructural, $1$ presencia o cumplimiento estructural, y $U$ indeterminación honesta: no es probabilidad, ni error, ni término medio. U designa una forma positiva de no sobrecerrar lo que todavía no puede resolverse sin violencia sobre el fenómeno o sobre la arquitectura que lo recibe.

Para cualquier base $b \geq 1$, la célula $(n, b)$ tiene $n = b^2$ componentes. El espacio de estados de esa célula es

$$X_{(n,b)} = \Sigma^n = \{0,\, 1,\, U\}^n.$$

El dominio activo de índices es $I_{(n,b)} = \{1, \ldots, n\}$. Cada índice $i \in I_{(n,b)}$ designa una posición de la célula que puede tomar valor en $\Sigma$.

### 1.2. La instancia canónica: célula (9, 3)

A lo largo de este documento se utiliza como instancia canónica y verificable la célula $(9, 3)$:

$$n = 9,\quad b = 3,\quad \Sigma^9 = \{0,\,1,\,U\}^9.$$

Un *frame* de esta célula es un vector de nueve componentes, cada una en $\{0, 1, U\}$. Las posiciones se designan como P1, P2, …, P9 siguiendo la estructura del polígono SV. Cada vez que se enuncia una definición o proposición en el nivel general $(n, b)$, se acompaña de su instanciación explícita en $(9, 3)$. La doble lectura garantiza que las nociones formales mantienen contacto directo con el objeto propio del SV.

### 1.3. El frame como unidad de análisis

Un *frame* es una configuración $S \in \Sigma^n$, es decir, una asignación de valor $\{0, 1, U\}$ a cada una de las $n$ posiciones de la célula. El *frame* es la unidad mínima de estado del SV. Una trayectoria es una sucesión de *frames*

$$T = (S_1, \nu_1, S_2, \nu_2, \ldots, S_N)$$

donde cada $\nu_k$ recoge la comparecencia de dato o interacción asociada al paso entre *frames* consecutivos.

Un suceso admisible —en el sentido de VII.1— es una cuaterna que describe cómo un *frame* puede ser reevaluado legítimamente en un horizonte declarado. VII.2 trata la cuestión de cuándo dos sucesos admisibles pueden ser comparados, cuándo uno afecta al otro y cuándo uno es condición necesaria del otro, todo ello operando sobre el espacio de *frames* $\Sigma^n$.

---

## 2. El horizonte canónico del SV y los antecedentes de la serie VII

### 2.1. Horizonte canónico para una célula (n, b)

En el plano general del SV, el horizonte canónico asociado a una célula $(n, b)$ es la cuádrupla

$$H_{(n,b)} = \bigl(I_{(n,b)},\; \preceq_{(n,b)},\; X_{(n,b)},\; \mathcal{A}_{(n,b)}\bigr),$$

donde: $I_{(n,b)} = \{1, \ldots, n\}$ es el dominio activo de índices de la célula; $\preceq_{(n,b)}$ es la relación interna de precedencia, admisibilidad o dependencia entre posiciones, inducida por la estructura del polígono SV; $X_{(n,b)} = \Sigma^n$ es el espacio de *frames*; $\mathcal{A}_{(n,b)}$ es la álgebra de observables: al menos las funciones $F : \Sigma^n \to \mathbb{Z}$, incluyendo los conteos de posiciones en cada valor de $\Sigma$.

**Instancia canónica (9, 3):**

$$H_{(9,3)} = \bigl(\{1,\ldots,9\},\; \preceq_{(9,3)},\; \{0,1,U\}^9,\; \mathcal{A}_{(9,3)}\bigr).$$

El dominio activo $I_{(9,3)} = \{P1, \ldots, P9\}$ son las nueve posiciones del polígono. Los observables naturales incluyen, por ejemplo, $F_U(S) = |\{i : S_i = U\}|$ (número de posiciones en régimen U) y $F_1(S) = |\{i : S_i = 1\}|$ (número de posiciones determinadas a 1).

### 2.2. Suceso admisible sobre el suelo ternario

Un suceso admisible sobre la célula $(n, b)$ es una cuaterna

$$e = (H,\, H',\, \sigma,\, R_e),$$

donde $H$ y $H'$ son horizontes de la célula (posiblemente distintos bajo sucesos envolventes), $\sigma \subseteq I_{(n,b)}$ es el **soporte declarado** —el subconjunto de posiciones que cambian de valor bajo la reevaluación— y $R_e : D_e \to X_{H'}$ con $D_e \subseteq X_H$ es el **operador de reevaluación**.

**Instancia canónica (9, 3):** Un suceso admisible sobre la célula $(9, 3)$ tiene soporte $\sigma \subseteq \{P1, \ldots, P9\}$. Por ejemplo, un suceso que transforma el valor de P3 de U a 1 y el valor de P8 de 0 a U tiene soporte $\sigma = \{P3, P8\}$. La reevaluación $R_e$ modifica exactamente esas dos posiciones en el *frame*; las restantes siete permanecen invariantes.

### 2.3. Conexión con el conteo de cruces $k(\tau)$

La dinámica de U en el SV está formalizada por el conteo de cruces estructurales

$$k(\tau) = \sum_{i=0}^{m-1} \varepsilon_i,$$

donde $\varepsilon_i = 1$ cuando el paso $S_i \to S_{i+1}$ cruza la frontera entre el régimen U y el plano de determinación $\{0,1\}$, y $\varepsilon_i = 0$ en caso contrario. La identidad $Ez(\tau, h) = h^2 k(\tau)$ establece que esta magnitud discreta es el antecedente formal del conteo eventivo.

En términos de sucesos admisibles: un suceso $e$ con soporte $\sigma$ que cambia posiciones de U a $\{0,1\}$ o viceversa contribuye a $k(\tau)$. La conexión precisa entre sucesos admisibles y cruces U-determinación es el puente que este documento abre y que el documento VII.3 deberá desarrollar.

### 2.4. Antecedente inmediato: el álgebra de composición de sucesos

El artículo *Álgebra de composición de sucesos admisibles* (Lloret Egea, 2026f) establece que la composición $e_2 \circ e_1$ de dos sucesos con horizonte intermedio coincidente es un suceso admisible (Proposición 4.3), que la estructura resultante es un semigrupoid parcial con neutros locales (Proposición 6.2), y que la acumulación eventiva $\mathcal{A}(\gamma; F, x_0)$ es aditiva respecto a la concatenación de cadenas (Proposición 7.2).

*(Nota editorial: este artículo es antecedente fundacional de VII.2 pero no tiene aún asignación dentro de la numeración VII.x de la serie. Hasta que se le asigne posición, el lector de la serie debe consultarlo directamente a través de la referencia bibliográfica (2026f).)*

VII.2 toma esos resultados como punto de partida y extiende la gramática hacia relaciones entre sucesos que no requieren horizontes encadenables: dos sucesos sobre la misma célula pueden ser comparables, afectarse o ser compatibles sin que ninguno sea antecedente directo del otro en una cadena.

---

## 3. Estado del arte y posición propia del SV

### 3.1. Estructuras de eventos y configuraciones

Las estructuras de eventos de Nielsen, Plotkin y Winskel (1981) formalizan causalidad, concurrencia e incompatibilidad sobre eventos abstractos. La extensión de van Glabbeek y Plotkin (2009) introduce *configuration structures* y clarifica distintas nociones de precedencia y conflicto. La proximidad con VII.2 es real: ambas tradiciones rechazan la secuencialidad temporal global y trabajan con relaciones parciales entre eventos.

La diferencia es de suelo: las estructuras de eventos parten de eventos abstractos sin especificar en qué espacio de estados operan. El SV parte de *frames* $S \in \Sigma^n$ con valores en $\{0, 1, U\}$, horizontes que declaran jurisdicción sobre subconjuntos de posiciones, y un régimen de indeterminación U con dinámica propia. La precedencia en VII.2 no es solo dependencia causal; es condición necesaria de admisibilidad sobre el espacio ternario.

### 3.2. Redes de Petri y estructura monoidal

Meseguer y Montanari (1990) demostraron que las redes de Petri admiten estructura monoidal, conectando con la aproximación del artículo de composición. Las redes de Petri trabajan con plazas, transiciones y marcas; no tematizan la admisibilidad dependiente del régimen U ni la variación de horizonte bajo sucesos envolventes sobre el espacio ternario.

### 3.3. Estructuras inhibidoras

La distinción entre afectación débil y fuerte tiene analogía con *enabling* y *disabling* en estructuras inhibidoras. En el SV esa distinción se ancla en el espacio ternario: la afectación débil altera evaluaciones de observables sin cambiar el conjunto de posiciones en U; la afectación fuerte altera el dominio de admisibilidad, lo que puede incluir cambios en qué posiciones están en régimen U.

### 3.4. Posición propia del SV

| Tradición vecina | Qué formaliza bien | Qué falta para el SV |
|---|---|---|
| Estructuras de eventos | causalidad, concurrencia, conflicto | espacio de estados ternario; régimen U; horizonte como jurisdicción |
| Redes de Petri / monoidal | composición de transiciones, marcaje | admisibilidad dependiente de U |
| Estructuras inhibidoras | habilitación e inhibición | admisibilidad tipada por horizonte ternario |
| Sistemas de transición | estados, pasos, refinamientos | soporte sobre posiciones de $\Sigma^n$; reevaluación entre horizontes |

---

## 4. Universo de trabajo

Sea $b \geq 1$ y $n = b^2$. Sea

$$\mathcal{E}_{(n,b)} = \bigl\{e = (H,\, H',\, \sigma,\, R_e) \;\big|\; \sigma \subseteq I_{(n,b)},\; R_e : D_e \to X_{H'},\; \text{A1–A6}\bigr\}$$

la familia de sucesos admisibles sobre la célula $(n, b)$ en el sentido de VII.1. Cuando el contexto es claro, se escribe simplemente $\mathcal{E}$. El presente documento impone sobre $\mathcal{E}$ una capa mínima de relaciones legítimas, siempre interpretadas sobre el espacio de *frames* $\Sigma^n$.

**Instancia (9, 3):** $\mathcal{E}_{(9,3)}$ es la familia de todos los sucesos admisibles sobre la célula de nueve posiciones con valores en $\{0, 1, U\}$. Un elemento típico tiene soporte $\sigma \subseteq \{P1, \ldots, P9\}$ y reevaluación $R_e : D_e \to \{0,1,U\}^9$.

---

## 5. Comparabilidad legítima

**Definición 5.1. Dato de transporte de observables para un par.** Sean $e, f \in \mathcal{E}$. Un dato de transporte parcial de observables para el par $(e, f)$ es una cuaterna

$$(J_{e,f},\; \Theta_{e,f},\; \mathcal{F}_e,\; \mathcal{F}_f),$$

donde: $J_{e,f} \subseteq I_{(n,b)}$ es un dominio común de referencia no vacío de posiciones de la célula; $\Theta_{e,f} : \mathcal{F}_e \to \mathcal{F}_f$ es una aplicación parcial entre familias de observables relevantes de $e$ y $f$, con codominio en el mismo escalar $\mathbb{K} = \mathbb{R}$ o $\mathbb{K} = \mathbb{Z}$; para todo $F_e \in \mathcal{F}_e$ y su imagen $\Theta_{e,f}(F_e) = F_f \in \mathcal{F}_f$, la expresión $\Delta_e F_e(x) - \Delta_f F_f(y)$ es un escalar bien definido en $\mathbb{K}$ para $x \in D_e$, $y \in D_f$.

**Instancia (9, 3):** Sea $e$ un suceso con soporte $\sigma(e) = \{P3, P8\}$ y sea $f$ un suceso con soporte $\sigma(f) = \{P6, P7\}$. Un dato de transporte natural toma $J_{e,f} = \{P1, P2, P4, P5, P9\}$ (posiciones no afectadas por ninguno de los dos), con $\Theta_{e,f}$ la identidad sobre los observables que solo dependen de esas posiciones. La condición (3) se verifica porque ambas diferencias eventivas son escalares en $\mathbb{Z}$ al evaluarse sobre las mismas posiciones no alteradas.

**Definición 5.2. Comparabilidad legítima.** Diremos que $e \bowtie f$ —o que son **comparables**— si existe al menos un dato de transporte parcial de observables para el par $(e, f)$.

**Observación 5.3.** La comparabilidad no es simétrica por defecto: la existencia de transporte de $e$ a $f$ no garantiza transporte de $f$ a $e$. Se declara como problema abierto cuándo la comparabilidad es simétrica en familias de horizontes con álgebras compatibles (§12, problema 1).

![Figura 1. Comparabilidad legítima entre dos sucesos admisibles.](figura_01_comparabilidad.svg)

*Figura 1. Comparabilidad legítima entre dos sucesos admisibles.*

Figura 1. Dos sucesos son comparables cuando existe un dato de transporte entre sus observables sobre un dominio común de posiciones. En la célula (9,3) con σ(e) = {P3,P8} y σ(f) = {P6,P7}, ese dominio son las cinco posiciones no afectadas. La comparabilidad no es universal (Proposición 5.4) ni necesariamente simétrica (Observación 5.3).

**Proposición 5.4. No universalidad de la comparabilidad.** No todo par $(e, f) \in \mathcal{E} \times \mathcal{E}$ es comparable.

*Prueba.* Considérese sobre la célula $(n, b)$ un suceso $e$ cuya álgebra de observables $\mathcal{A}_{H_e}$ está definida sobre $\mathbb{K} = \mathbb{R}$ y un suceso $f$ cuya álgebra $\mathcal{A}_{H_f}$ solo contiene observables con valores en un conjunto $\Omega$ sin estructura de orden compatible con $\mathbb{R}$. La condición (3) de la Definición 5.1 exige que $\Delta_e F_e(x) - \Delta_f F_f(y)$ sea un escalar en $\mathbb{K}$. Si no existe $\Theta_{e,f}$ que produzca diferencias eventivas en el mismo cuerpo escalar, el par no es comparable.

**Instancia (9, 3):** Si $e$ opera sobre posiciones donde todos los valores son $\{0, 1\}$ y $f$ opera sobre posiciones enteramente en U sin observable numérico definido, no existe transporte entre sus álgebras de observables. El par no es comparable. ∎

**Adversarial interna 5.5.**
*Objeción.* El dato de transporte es demasiado abstracto si $\Theta_{e,f}$ no queda mejor especificado.
*Respuesta.* La condición (3) impide que $\Theta_{e,f}$ funcione como etiqueta verbal: exige que produzca diferencias eventivas comparables en el mismo escalar. La instancia $(9, 3)$ muestra que en el caso natural del SV —observables que cuentan posiciones en cada valor de $\Sigma$— el transporte existe de forma concreta. La unicidad y las propiedades de preservación de estructura de $\Theta_{e,f}$ quedan abiertas (§12).

---

## 6. Afectación estratificada

**Definición 6.1. Afectación débil.** Sean $e, f \in \mathcal{E}$ con $e \bowtie f$. Diremos que $e$ afecta débilmente a $f$, notado $e \rightsquigarrow_w f$, si la aplicación de $R_e$ modifica la evaluación de al menos un observable $F_f \in \mathcal{F}_f$ sin alterar el dominio $D_f$ ni la condición de admisibilidad de $f$.

Formalmente: existe $x \in D_e$ y $y \in D_f$ tal que $\Delta_e F_e(x) \neq 0$ y $F_f(R_e(y)) \neq F_f(y)$, pero $D_f^{\text{post-}e} = D_f$.

**Instancia (9, 3):** Sea $e$ un suceso que cambia P3 de U a 1. Si $f$ tiene un observable $F_f = F_1$ que cuenta posiciones en valor 1, entonces $F_1$ aumenta en 1 tras la reevaluación de $e$. Si el dominio de admisibilidad de $f$ depende solo de que P6 y P7 tengan valores determinados, y esos no cambian, entonces $D_f$ permanece intacto: $e \rightsquigarrow_w f$.

**Definición 6.2. Afectación fuerte.** Diremos que $e$ afecta fuertemente a $f$, notado $e \rightsquigarrow_s f$, si la aplicación de $R_e$ altera el dominio de admisibilidad de $f$:

$$D_f^{\text{post-}e} \subsetneq D_f \quad \text{o} \quad D_f^{\text{post-}e} = \varnothing.$$

**Instancia (9, 3):** Sea $f$ un suceso cuyo dominio de admisibilidad exige que P5 tenga valor 1: $D_f = \{S \in \Sigma^9 : S_{P5} = 1\}$. Si $e$ es un suceso que cambia P5 de 1 a U, entonces $D_f^{\text{post-}e} = \varnothing$: ningún *frame* resultante de $R_e$ pertenece a $D_f$. La reevaluación de $e$ destruye la aplicabilidad de $f$. Entonces $e \rightsquigarrow_s f$.

**Observación 6.3. La distinción es estructural, no cuantitativa.** Un suceso que cambia una sola posición puede ser fuerte si esa posición es condición de admisibilidad de otro suceso. Un suceso que cambia seis posiciones puede ser débil si ninguna de ellas afecta la admisibilidad del suceso comparado. En la célula $(9, 3)$, esto es verificable caso a caso sobre el soporte $\sigma$.

![Figura 2. Afectación débil y afectación fuerte.](figura_02_afectacion.svg)

*Figura 2. Afectación débil y afectación fuerte.*

Figura 2. La distinción entre los dos tipos de afectación no es de grado sino de naturaleza. La afectación débil (columna izquierda, fondo claro) modifica cómo se evalúan los observables de f, pero el dominio $D_f$ permanece intacto: f sigue siendo admisible. La afectación fuerte (columna derecha, borde reforzado) destruye o restringe $D_f$: tras la reevaluación de e, hay *frames* que f ya no puede procesar. En la célula (9,3): cambiar P3 de U a 1 es débil si $D_f$ depende de P5 intacto; cambiar P5 de 1 a U es fuerte si $D_f$ exige P5=1, porque ese dominio queda vacío. La Proposición 6.5 establece que la afectación fuerte implica la débil, pero no al revés. La Proposición 6.4 establece que la afectación fuerte no es simétrica.

**Proposición 6.4. No simetría de la afectación fuerte.** La relación $\rightsquigarrow_s$ no es simétrica.

*Prueba.* Sea $e = (H, H', \sigma_e, R_e)$ con $\sigma_e = \{P5\}$ tal que $R_e$ cambia P5 de 1 a U, destruyendo $D_f$ como en la Instancia de la Definición 6.2. Sea $f = (H', H'', \sigma_f, R_f)$ con $\sigma_f = \{P6, P7\}$, cuyo operador $R_f$ actúa sobre posiciones disjuntas de $\sigma_e$ y no modifica ninguna condición de admisibilidad de $e$. Entonces $D_e^{\text{post-}f} = D_e$: la aplicación de $f$ no altera el dominio de $e$. Luego $e \rightsquigarrow_s f$ pero $f \not\rightsquigarrow_s e$. ∎

**Proposición 6.5. Afectación fuerte implica afectación débil bajo comparabilidad.** Si $e \rightsquigarrow_s f$ y $e \bowtie f$, entonces $e \rightsquigarrow_w f$.

*Prueba.* Si $R_e$ altera $D_f$, modifica la región sobre la que $R_f$ es aplicable. Esa modificación implica un cambio en la evaluabilidad de al menos un observable $F_f$ definido sobre la parte de $D_f$ que queda restringida. Por la condición (3) del dato de transporte, esa variación es detectable como diferencia eventiva en $\mathbb{K}$. Luego $e \rightsquigarrow_w f$.

**Instancia (9, 3):** Si $e$ destruye $D_f$ al cambiar P5, el observable $F_f$ que evaluaba configuraciones con P5 = 1 ya no puede evaluarse sobre las configuraciones resultantes de $R_e$. Esa pérdida de evaluabilidad es precisamente la variación que caracteriza la afectación débil. ∎

**Adversarial interna 6.6.**
*Objeción.* La relación de afectación podría inflar en un símbolo casos demasiado distintos.
*Respuesta.* La estratificación débil/fuerte es la respuesta directa. En el SV, la distinción tiene interpretación concreta sobre el espacio ternario: la afectación débil afecta la lectura de observables; la fuerte afecta qué *frames* son válidos como dominio de otro suceso. Las Proposiciones 6.4 y 6.5 establecen relaciones no triviales entre ambos niveles.

---

## 7. Precedencia estructural

**Definición 7.1. Precedencia estructural.** Sean $e, f \in \mathcal{E}$. Diremos que $e$ precede estructuralmente a $f$, notado $e \prec f$, si se cumplen simultáneamente:

1. $e \bowtie f$ (comparabilidad);
2. $e \rightsquigarrow_s f$ (afectación fuerte, entendida en el sentido de que la reevaluación de $e$ condiciona la existencia del dominio de $f$);
3. La reevaluación inducida por $e$ es condición necesaria de admisibilidad para $f$:

$$D_f^{\text{pre-}e} = \varnothing \quad \text{y} \quad D_f^{\text{post-}e} \neq \varnothing.$$

La condición (3) distingue precedencia de mera afectación fuerte: no basta que $e$ restrinja $D_f$; se requiere que sin la reevaluación de $e$, $f$ no tenga ningún *frame* admisible en absoluto, y que después de $e$ los haya.

**Instancia (9, 3):** Sea $f$ un suceso que requiere que P3 tenga valor 1 para ser admisible. Si en el *frame* actual P3 tiene valor U, entonces $D_f^{\text{pre-}e} = \varnothing$: $f$ no es admisible. Sea $e$ un suceso con soporte $\{P3\}$ que cambia P3 de U a 1. Tras la reevaluación de $e$, $D_f^{\text{post-}e} \neq \varnothing$: $f$ se vuelve admisible. Entonces $e \prec f$. La precedencia de $e$ sobre $f$ está determinada por la dinámica de U sobre la posición P3.

**Observación 7.2. Precedencia no es tiempo; es dinámica de U.** La precedencia no expresa "antes" y "después" en sentido cronológico. Expresa una dependencia estructural sobre el espacio ternario: $f$ no puede comparecer mientras ciertas posiciones estén en U. La reevaluación de $e$ que resuelve esas U hacia $\{0,1\}$ es lo que habilita $f$. No hay reloj global; hay dinámica de U.

En la célula $(9, 3)$, la precedencia $e \prec f$ se reduce a verificar: ¿existe algún *frame* $S \in \Sigma^9$ donde $f$ sea admisible antes de aplicar $R_e$? Si no existe, y después de $R_e$ sí existe, entonces $e \prec f$.

![Figura 3. Precedencia estructural y aciclicidad.](figura_03_precedencia.svg)

*Figura 3. Precedencia estructural y aciclicidad.*

Figura 3. La precedencia exige tres condiciones: comparabilidad, afectación fuerte, y que sin e el suceso f sea imposible. En la célula (9,3): P3 en U bloquea f; e resuelve P3 a 1 y habilita f. La Proposición 7.5 garantiza que ninguna cadena de precedencias puede cerrarse en ciclo: cada eslabón resuelve una U, y cerrar el ciclo contradiría A2. Sin reloj; solo terna.

**Proposición 7.3. Precedencia implica afectación fuerte, pero no recíprocamente.** $e \prec f$ implica $e \rightsquigarrow_s f$. La implicación no se invierte.

*Prueba.* La dirección directa es inmediata por la condición (2) de la Def. 7.1. Para la no inversión: sea $e \rightsquigarrow_s f$ con $D_f^{\text{post-}e} \subsetneq D_f$ pero $D_f^{\text{pre-}e} \neq \varnothing$. Entonces $f$ era admisible antes de $e$: la condición (3) de la Def. 7.1 falla. Luego $e \rightsquigarrow_s f$ pero $e \not\prec f$.

**Instancia (9, 3):** Si $e$ cambia P5 de 1 a U y $D_f$ requiere $P5 \in \{0,1\}$, entonces $D_f^{\text{post-}e}$ queda restringido pero no vacío si hay otros *frames* con P5 = 0 en $D_f$. En ese caso $e \rightsquigarrow_s f$ pero $e \not\prec f$ porque $f$ tenía *frames* admisibles antes de $e$. ∎

**Proposición 7.4. Irreflexividad.** Para todo $e \in \mathcal{E}$, $e \not\prec e$.

*Prueba.* La condición (3) de la Def. 7.1 exigiría $D_e^{\text{pre-}e} = \varnothing$: que $e$ no sea admisible antes de su propia reevaluación. Pero por A2 de VII.1, $D_e \neq \varnothing$ es condición de admisibilidad de $e$ como dato de partida. Contradicción.

**Instancia (9, 3):** Un suceso sobre P3 existe porque hay al menos un *frame* donde P3 tiene el valor que $R_e$ puede transformar. Ese *frame* pertenece a $D_e$. Luego $D_e^{\text{pre-}e} = D_e \neq \varnothing$ y la condición de precedencia reflexiva falla. ∎

**Proposición 7.5. Acíclicidad en familias finitas** *(resultado central).* En toda familia finita $\{e_1, \ldots, e_n\} \subset \mathcal{E}$, la relación de precedencia estructural $\prec$ no contiene ciclos.

*Prueba.* Supóngase un ciclo $e_1 \prec e_2 \prec \ldots \prec e_k \prec e_1$. Por la condición (3) de la Def. 7.1 aplicada al primer paso: $D_{e_2}^{\text{pre-}e_1} = \varnothing$, es decir, $e_2$ no es admisible en ningún *frame* antes de la reevaluación de $e_1$. Por el último paso del ciclo: $D_{e_1}^{\text{pre-}e_k} = \varnothing$, es decir, $e_1$ no es admisible en ningún *frame* antes de la reevaluación de $e_k$. Encadenando: $e_1$ requiere $e_k$, que requiere $e_{k-1}$, …, que requiere $e_1$. Pero $e_1$ tiene $D_{e_1} \neq \varnothing$ por A2. Contradicción con la Proposición 7.4. ∎

**Instancia (9, 3):** Ningún ciclo de sucesos admisibles sobre las nueve posiciones puede formarse bajo precedencia estructural, porque cada eslabón del ciclo exigiría que el anterior resuelva ciertas U, y el último eslabón exigiría que el primero no tuviera *frames* admisibles, contradiciendo A2.

Esta proposición es el resultado central del documento: garantiza que VII.3 puede definir cadenas admisibles de sucesos sobre el SV sin circularidad, apoyándose en la dinámica de U como mecanismo de habilitación.

**Observación 7.7. Hipótesis implícita de la Proposición 7.5: monotonicidad de la habilitación por U.**
La prueba por contradicción presupone que ningún suceso en la cadena $e_1 \prec e_2 \prec \ldots \prec e_k$ puede *reintroducir* U en las posiciones que hacen admisible a $e_1$. Si un suceso posterior de la cadena revirtiera la resolución de U realizada por $e_1$ —devolviendo a U posiciones que $e_1$ necesita tener determinadas para existir como suceso—, el último paso del ciclo no contradiría A2. Esta condición de *monotonicidad de la habilitación* no está enunciada como axioma en VII.1 ni en este documento. La acíclicidad es sólida bajo ella; su falta de declaración explícita es el problema abierto más urgente de cara a VII.3. Se añade formalmente al §12 (problema 6).

**Adversarial interna 7.6.**
*Objeción.* Podría estarse reintroduciendo tiempo fuerte con otro nombre.
*Respuesta.* La precedencia no depende de ningún índice temporal externo. Depende de si $D_f^{\text{pre-}e} = \varnothing$ sobre el espacio de *frames* $\Sigma^n$. Esa condición es verificable posición a posición en la célula sin ninguna referencia a tiempo. La dinámica de U que habilita sucesos es una propiedad del espacio ternario, no de un reloj.

**Observación 7.8. Lectura correcta de la condición (2) en presencia de la condición (3).**
La condición (2) de la Def. 7.1 exige $e \rightsquigarrow_s f$, cuya definición (Def. 6.2) describe un suceso que *restringe o destruye* un dominio preexistente. La condición (3) establece que $D_f^{\text{pre-}e} = \varnothing$: ese dominio era ya vacío antes de $e$. La lectura correcta es que la condición (2) en el contexto de la precedencia no describe restricción de un dominio existente, sino la condición necesaria de que la reevaluación de $e$ sea lo que *crea* el dominio de $f$ donde antes no existía. Las condiciones (2) y (3) juntas establecen que $e$ transita el estado de $f$ de no-admisible a admisible, lo que es el caso límite de la afectación fuerte en dirección constructiva. Esta lectura no contradice la Def. 6.2; la especializa.

---

## 8. Compatibilidad como noción derivada

**Definición 8.1. Compatibilidad.** Sean $e, f \in \mathcal{E}$. Diremos que son **compatibles**, notado $e \parallel f$, si:

1. $e \bowtie f$;
2. $e \not\rightsquigarrow_s f$ y $f \not\rightsquigarrow_s e$;
3. existe un dato de transporte $(J_{e,f}, \Theta_{e,f}, \mathcal{F}_e, \mathcal{F}_f)$ bajo el cual $\Theta_{e,f}(F_e)(y) = F_f(y)$ para todo $y \in D_f$ en el dominio común $J_{e,f}$.

La condición (3) exige coevaluabilidad estable: no basta ausencia de conflicto, se requiere coexistencia positiva y legible.

**Instancia (9, 3):** Sea $e$ con soporte $\{P1, P2\}$ y $f$ con soporte $\{P7, P8\}$. Sus soportes son disjuntos. Ninguno altera el dominio de admisibilidad del otro. El dato de transporte toma $J_{e,f} = \{P3, P4, P5, P6, P9\}$ con $\Theta_{e,f}$ la identidad. Los observables que solo dependen de esas posiciones son coevaluables establemente. Entonces $e \parallel f$.

**Proposición 8.2. Soportes disjuntos implican compatibilidad.** Si $\sigma(e) \cap \sigma(f) = \varnothing$ y $e \bowtie f$, entonces $e \parallel f$.

*Prueba.* Si los soportes son disjuntos sobre $I_{(n,b)}$, la reevaluación de $e$ no modifica las posiciones sobre las que opera $R_f$, y viceversa. Por A1 de VII.1, cada soporte está bien tipado. La afectación fuerte es nula en ambas direcciones: $D_f^{\text{post-}e} = D_f$ y $D_e^{\text{post-}f} = D_e$. La coevaluabilidad estable se obtiene con $J_{e,f} = I_{(n,b)} \setminus (\sigma(e) \cup \sigma(f))$ y $\Theta_{e,f}$ la identidad restringida.

**Instancia (9, 3):** Con $\sigma(e) \cup \sigma(f) \subseteq \{P1,\ldots,P9\}$ y soportes disjuntos, al menos $9 - |\sigma(e)| - |\sigma(f)|$ posiciones forman el dominio común. Para soportes de tamaño 2 cada uno, $J_{e,f}$ tiene al menos 5 posiciones. ∎

**Adversarial interna 8.3.**
*Objeción.* La compatibilidad está definida negativamente como ausencia de afectación fuerte.
*Respuesta.* La condición (3) es positiva: exige coevaluabilidad estable. La Proposición 8.2 muestra que hay una clase no vacía de pares compatibles —aquellos con soportes disjuntos— lo que impide que la definición sea vacua.

---

## 9. Relación con la composición de sucesos

La composición secuencial, estudiada en el artículo de composición (Lloret Egea, 2026f), exige que el horizonte resultante de un suceso coincida con el horizonte de partida del siguiente. Ese es el caso más estricto de relación entre sucesos: la cadena. VII.2 trabaja el caso más general: dos sucesos que operan sobre la misma célula sin estar encadenados pueden ser comparables, afectarse mutuamente o ser compatibles. Esas relaciones —comparabilidad, afectación, precedencia, compatibilidad— describen la estructura interna de familias de sucesos concurrentes sobre el mismo espacio de *frames*.

---

## 10. Resumen de resultados cerrados

| Resultado | Tipo | Contenido |
|---|---|---|
| Proposición 5.4 | No trivial | No todo par de sucesos es comparable |
| Proposición 6.4 | No trivial | La afectación fuerte no es simétrica |
| Proposición 6.5 | No trivial | Afectación fuerte implica débil bajo comparabilidad |
| Proposición 7.3 | No trivial | Precedencia implica afectación fuerte; no recíprocamente |
| Proposición 7.4 | Cerrada | La precedencia es irreflexiva |
| Proposición 7.5 | Central | La precedencia es acíclica en familias finitas |
| Proposición 8.2 | Cerrada | Soportes disjuntos implican compatibilidad |

---

## 11. Delimitación negativa

Este documento no establece: teoría completa de cadenas ordenadas por precedencia (reservada a VII.3); acumulación eventiva sobre cadenas con precedencia (reservada a VII.3); conexión métrica entre $k(\tau)$ y número de sucesos admisibles en régimen general (problema abierto); geometría reconstructiva ni física cerrada; modificación de gramática, IR, *validator*, *runner* o backend. (<a href="https://juantoniolloretegea.github.io/SV-lenguaje-de-computacion/" target="_blank" rel="noopener noreferrer">Ver documentación relacionada</a>.)

---

## 12. Problemas abiertos reconocidos

**1. Simetría de la comparabilidad.** Condiciones sobre $\mathcal{A}_{H_e}$ y $\mathcal{A}_{H_f}$ bajo las cuales $e \bowtie f$ implica $f \bowtie e$.

**2. Unicidad del dato de transporte.** Condiciones bajo las cuales $(J_{e,f}, \Theta_{e,f})$ es canónico para un par dado sobre la célula $(n, b)$.

**3. Precedencia en familias infinitas.** La Proposición 7.5 cubre familias finitas; la extensión requiere buena fundación de $\prec$ sobre $\mathcal{E}_{(n,b)}$.

**4. Compatibilidad y composición paralela.** Si $e \parallel f$ sobre la misma célula, ¿existe una forma de composición paralela que preserve el soporte disjunto?

**5. Puente entre precedencia y conteo $k(\tau)$.** La Proposición 7.5 garantiza acíclicidad; la conexión precisa entre $e \prec f$ y el incremento de $k(\tau)$ bajo cadenas de sucesos que resuelven U queda abierta para VII.3.

**6. Monotonicidad de la habilitación (hipótesis implícita de Prop. 7.5).** La prueba de acíclicidad presupone que ningún suceso en una cadena de precedencia puede reintroducir U en las posiciones que hacen admisible al primer suceso de la cadena. Esta condición debe elevarse a axioma explícito antes de que VII.3 construya cadenas sobre ella, o bien la Proposición 7.5 debe reformularse como condicional bajo esa hipótesis declarada.

---

## 13. Conclusión

VII.2 establece la gramática relacional del Sistema Vectorial SV desde su suelo propio: la célula $(n, b)$ con $n = b^2$, el espacio de *frames* $\Sigma^n = \{0,1,U\}^n$ y el régimen de indeterminación U con su dinámica de cruces.

Las cuatro nociones —comparabilidad legítima, afectación estratificada, precedencia estructural y compatibilidad derivada— se definen sobre el espacio ternario y se instancian en cada caso sobre la célula $(9, 3)$, que actúa como verificación directa sobre nueve posiciones concretas.

El resultado central —acíclicidad de la precedencia (Proposición 7.5)— se demuestra desde A2 y la dinámica de U: ningún ciclo de sucesos admisibles puede formarse porque cada eslabón exigiría que el anterior resuelva U sobre ciertas posiciones, y el cierre del ciclo exigiría que el primero no tuviera *frames* admisibles, lo que contradice A2. Sin reloj. Sin tiempo fuerte. Solo terna.

La Observación 7.7 declara explícitamente la hipótesis de monotonicidad de habilitación que subyace a esa prueba, convirtiéndola en el problema abierto más urgente para VII.3.

Con este suelo, VII.3 puede definir cadenas admisibles ordenadas por precedencia estructural sobre el SV y desarrollar la acumulación eventiva sobre el espacio ternario, sujeto a la formalización de la monotonicidad en §12, problema 6.

---

## Bibliografía

### Referencias internas del Sistema Vectorial SV

Lloret Egea, J. A. (2026-NOTA). *Suceso local, suceso envolvente y reevaluación situacional en horizonte declarado en el Sistema Vectorial SV*. Nota de precisión algebraico-semántica, v2. ITVIA, Madrid, 22 de marzo de 2026. ISSN 2695-6411.

Lloret Egea, J. A. (2026a). *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. ITVIA, ISSN 2695-6411.

Lloret Egea, J. A. (2026b). *Álgebra de composición intercelular del marco SV — VI. Análisis discreto, representaciones y herramientas de secuencias del sistema*. ITVIA, Madrid.

Lloret Egea, J. A. (2026c). *Transiciones estructurales y trayectorias de la U en el Sistema Vectorial SV*. Release 2. ITVIA, Madrid.

Lloret Egea, J. A. (2026d). *Documento VII.0 — Hacia una geometría eventivo-espacial sin tiempo canónico*. ITVIA, Madrid.

Lloret Egea, J. A. (2026e). *Teoría rigurosa del suceso admisible* (VII.1). ITVIA, Madrid.

Lloret Egea, J. A. (2026f). *Álgebra de composición de sucesos admisibles en el Sistema Vectorial SV*. ITVIA, Madrid. *(Antecedente fundacional de VII.2; posición en la serie VII pendiente de asignación.)*

### Referencias externas

Abramsky, S., & Jung, A. (1994). Domain theory. In *Handbook of Logic in Computer Science*, Vol. 3. Oxford University Press.

Meseguer, J., & Montanari, U. (1990). Petri nets are monoids. *Information and Computation*, 88(2), 105–155. DOI: 10.1016/0890-5401(90)90013-8.

Nielsen, M., Plotkin, G., & Winskel, G. (1981). Petri nets, event structures and domains, Part I. *Theoretical Computer Science*, 13(1), 85–108. DOI: 10.1016/0304-3975(81)90112-2.

Petri, C. A. (1962). *Kommunikation mit Automaten*. Universität Bonn.

van Glabbeek, R. J., & Plotkin, G. D. (2009). Configuration structures, event structures and Petri nets. *Theoretical Computer Science*, 410, 4111–4159. DOI: 10.1016/j.tcs.2009.06.014.

Winskel, G. (1987). Event structures. In *Advances in Petri Nets 1986*, LNCS 255. Springer. DOI: 10.1007/3-540-17906-2_31.
