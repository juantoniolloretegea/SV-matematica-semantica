# Dinámica del Suceso - Sistema Vectorial SV

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados.  
ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0). Esta licencia se aplica exclusivamente a esta versión. | Madrid, 17/08/2026.

**DOI:** 10.21428/39829d0b.8ea18396  
**URL canónica:** https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/sucesos_horizontes_y_cambio_estructural/dinamica-del-suceso-sistema-vectorial-sv/dinamica-del-suceso-sistema-vectorial-sv.md

---

## Resumen

La Matemática del Suceso en el Sistema Vectorial SV ha establecido la configuración celular, el dato de transición, el horizonte de tipos, el suceso admisible, las relaciones entre sucesos, las cadenas, la persistencia *append-only*, la bifurcación y el cambio de horizonte [1,4,6–15]. Sin quedar determinada en una sola formulación general la relación entre esos elementos ni, en particular, la diferencia entre una transformación ejecutable, un recorrido realizable y un suceso admisible.

Este trabajo establece esa relación. A partir del suceso admisible de VII.1, e = (H, H′, σ, Rₑ), sometido a las condiciones A1–A6 [6], precisa el dominio común sobre el que puede ejecutarse una sucesión de reevaluaciones y define su reevaluación compuesta. Se demuestra que la existencia de esa composición funcional no basta para constituir un nuevo suceso: la cuaterna resultante debe satisfacer nuevamente A1–A6, incluida A4, que exige una variación observable no nula [6]. Un contraejemplo explícito en SV(9,3) muestra que dos sucesos admisibles pueden cancelarse y producir una reevaluación compuesta que ya no sea un suceso admisible.

El trabajo introduce además el **tramo realizable**, que exige un mismo estado inicial capaz de atravesar todos los dominios sucesivos, y la **cadena realizable**, que añade ese requisito a las condiciones de cadena establecidas en VII.3 [8]. Se demuestra que la composición por pares no garantiza una realización conjunta y que, sobre una cadena realizable con lecturas observacionales compatibles, la variación total satisface una identidad telescópica.

HNA preserva las posiciones clausuradas dentro de una misma trayectoria *append-only* [13,14]. Sobre ese resultado se demuestra que toda cadena estricta de habilitación que clausure al menos una posición con valor U en cada paso posee un rango entero estrictamente decreciente y, por tanto, no puede formar ciclos. La bifurcación conserva el prefijo ya constituido [13].

Los cambios de horizonte quedan sujetos a persistencia, reevaluación, no herencia, transporte declarado y preservación local [9–12]; no se presume continuidad ni equivalencia global. La recurrencia estructural permite, además, que una configuración visible vuelva a aparecer con una activación distinta [15], por lo que la identidad del *frame* no determina la identidad del suceso ni de la activación.

U sigue siendo uno de los tres valores de Σ = {0, 1, U} [1–3] y no admite subtipos. Las clasificaciones irreducible, fronteriza y resoluble definidas en [13], así como otras propiedades contextuales, califican posiciones cuyo valor es U respecto del horizonte declarado; no modifican U ni amplían el alfabeto.

El resultado es una dinámica general en la que configuración, dato de transición, reevaluación, suceso admisible, realización y cadena quedan formalmente relacionados sin exigir identidad global, composición total, monoide, grupo, métrica general, tiempo ni probabilidad como primitivas.

**Palabras clave:** Sistema Vectorial SV; Suceso; suceso admisible; *frame*; horizonte; U; reevaluación; cadena realizable; HNA; *append-only*.

---

## 1. Base ternaria y celular

El Sistema Vectorial SV utiliza el alfabeto Σ = {0, 1, U} [1–3]. Una célula de base b dispone de n = b² posiciones. Una configuración, denominada *frame* en el SV, es S = (s₁, …, sₙ) ∈ Σⁿ. La instancia canónica de primer nivel es SV(9,3), sin que la dinámica general quede restringida a nueve posiciones [1,4].

Los fundamentos definen el *frame* como configuración celular [1], mientras que VII.1 define el suceso admisible mediante un horizonte de partida, un horizonte resultante, un soporte y un operador de reevaluación [6]. Por ello, una configuración no es un suceso. Dos evaluaciones pueden presentar el mismo *frame* visible sin constituir el mismo suceso ni pertenecer al mismo recorrido; la recurrencia estructural confirma esta separación al admitir configuraciones iguales con activaciones distintas [15].

### 1.1. Unicidad de U y clasificación contextual de las posiciones

El alfabeto Σ contiene exactamente tres valores: 0, 1 y U. U es un único valor de Σ y no admite subtipos.

La función Γ_H clasifica cada posición cuyo valor es U respecto del horizonte declarado como irreducible, fronteriza o resoluble [13]. Las tres clases resultantes son conjuntos de posiciones; no son clases de U. El valor de cada una de esas posiciones continúa siendo U.

En [14] aparecen también las expresiones «U irreducible», «U fronteriza» y «U resoluble». Conforme a la definición formal de Γ_H de [13], esas expresiones se entienden aquí como abreviaturas de «posición con valor U clasificada como irreducible, fronteriza o resoluble». El alfabeto permanece Σ = {0, 1, U}. La criticidad, la vecindad y cualquier otra propiedad contextual se predican igualmente de la posición o de su situación respecto del horizonte, no de U.

La asignación legítima de U a una posición no expresa probabilidad, espera, transición en curso ni simple cálculo pendiente. Expresa no clausura después del agotamiento trazable de las vías admisibles disponibles en el dominio y horizonte declarados [2,3,13].

---

## 2. Tipado de los objetos

El SV emplea dos nociones de horizonte con funciones distintas.

En el álgebra de composición intercelular se define el horizonte de tipos de suceso ℋ(𝒜) = {ε₁, …, εₘ} [4]. Cada εᵢ representa un tipo de suceso declarado para la arquitectura. El dato de transición se escribe νₙ = {(εᵢ, τᵢ)}ᵢ∈Iₙ, con τᵢ ∈ Σ. El valor τᵢ registra si consta incidencia, consta no incidencia o no existe base suficiente para clausurar la instancia en 0 o 1 [4].

VII.1 define, por otra parte, el horizonte estructural H = (Iₕ, ≼ₕ, Xₕ, 𝒜ₕ), que determina las posiciones disponibles, la relación interna declarada, el espacio de configuraciones legibles y la familia de observables [6].

Por tanto, ℋ(𝒜), H, εᵢ, τᵢ, νₙ, S, e y Rₑ son objetos distintos. En particular, el dato de transición ν puede inducir una reevaluación en la arquitectura de [4], pero no se identifica con el suceso admisible e de VII.1 [6].

La notación debe conservar el significado del régimen en que fue definida. Así, εᵢ es un tipo de suceso en [4], mientras que en el régimen de recurrencia de [15] εₖ designa un activador indexado. La coincidencia de letra no identifica ambos objetos. Del mismo modo, los usos posteriores de ν no convierten el dato de transición de [4] en el suceso admisible de VII.1 [14,15].

---

## 3. Suceso admisible

VII.1 define un suceso admisible como la cuaterna e = (H, H′, σ, Rₑ), donde Rₑ : Dₑ → Xₕ′, Dₑ ⊆ Xₕ y Dₑ ≠ ∅ [6]. Su admisibilidad exige seis condiciones:

1. **A1 — soporte bien tipado:** σ ⊆ Iₕ.
2. **A2 — dominio de reevaluación no vacío:** Dₑ ⊆ Xₕ, Dₑ ≠ ∅ y Rₑ está bien tipado hacia Xₕ′.
3. **A3 — legibilidad antes y después:** para todo x ∈ Dₑ, tanto x como Rₑ(x) son configuraciones legibles en sus respectivos horizontes.
4. **A4 — no trivialidad efectiva:** existe al menos un observable compatible F y un x ∈ Dₑ tales que Fₕ′(Rₑ(x)) − Fₕ(x) ≠ 0.
5. **A5 — control exterior parcial:** existe un dato Cₑ = (Jₑ, θₑ), con Jₑ ⊆ Iₕ ∖ σ y θₑ : Jₑ → Iₕ′, que conserva una correspondencia formal para la región exterior declarada.
6. **A6 — compatibilidad observacional declarada:** la comparación entre Fₕ y Fₕ′ sólo puede invocarse dentro de una clase de horizontes para la que esa familia observacional haya sido declarada compatible.

Estas condiciones pertenecen a VII.1 [6]. A4 será decisiva para la composición: una transformación netamente trivial desde el punto de vista de todos los observables compatibles no constituye un suceso admisible.

---

## 4. Composición de reevaluaciones

VII.1 deja abierta la composición parcial de sucesos admisibles [6]. Para tratarla es necesario separar dos preguntas: si los operadores pueden ejecutarse sucesivamente sobre un mismo estado inicial y, en caso afirmativo, si el resultado vuelve a satisfacer las condiciones que definen un suceso.

Sean eₖ = (Hₖ₋₁, Hₖ, σₖ, Rₖ), para k = 1, …, m, sucesos admisibles cuyos horizontes consecutivos coinciden conforme al tipado declarado.

### Definición 4.1. Dominio efectivo

Se denomina D₁…ₘ al conjunto de estados iniciales sobre los que puede ejecutarse toda la sucesión:

D₁…ₘ = { x ∈ D₁ : R₁(x) ∈ D₂, R₂(R₁(x)) ∈ D₃, …, (Rₘ₋₁ ∘ ⋯ ∘ R₁)(x) ∈ Dₘ }.

### Definición 4.2. Reevaluación compuesta

Si D₁…ₘ ≠ ∅, se define R₁…ₘ(x) = (Rₘ ∘ ⋯ ∘ R₁)(x) para todo x ∈ D₁…ₘ.

### Teorema 4.3. Asociatividad de la composición funcional

Sobre el dominio efectivo común, R₃ ∘ (R₂ ∘ R₁) = (R₃ ∘ R₂) ∘ R₁. La misma igualdad vale para cualquier número finito de operadores.

**Demostración.** Es la asociatividad ordinaria de la composición de funciones, restringida al dominio en el que están definidas todas las aplicaciones sucesivas. ∎

La asociatividad anterior es una propiedad de los operadores Rₖ. No implica que la clase de sucesos admisibles sea estable respecto de la composición.

---

## 5. Separación entre reevaluación compuesta y suceso admisible

### Teorema 5.1. La composición funcional no basta para constituir un suceso

La existencia de R₁…ₘ no implica que una cuaterna candidata e₁…ₘ = (H₀, Hₘ, σ₁…ₘ, R₁…ₘ) sea un suceso admisible.

**Demostración.** Considérese SV(9,3) sobre un mismo horizonte H que contenga las configuraciones S₀ = (0,0,0,0,0,0,0,0,0) y S₁ = (1,0,0,0,0,0,0,0,0). Sean D₁ = {S₀}, R₁(S₀) = S₁, D₂ = {S₁} y R₂(S₁) = S₀.

En ambos sucesos tómese σ = {1}, J = {2, …, 9} y el control exterior C = (J, id(J)). Sea F ∈ 𝒜ₕ el observable F(S) = |{i : Sᵢ = 1}|. Entonces F(S₁) − F(S₀) = 1 y F(S₀) − F(S₁) = −1. Los dos pasos poseen dominio no vacío, entrada y salida legibles, soporte declarado, control exterior y variación observable no nula. Como el horizonte de partida y el de llegada son el mismo H, la comparación pertenece a la misma familia observacional. Con estos datos, ambos pasos satisfacen A1–A6 de VII.1 [6].

Sin embargo, D₁…₂ = {S₀} y R₁…₂(S₀) = S₀. Para todo observable compatible G ∈ 𝒜ₕ se cumple G(R₁…₂(S₀)) − G(S₀) = 0. La cuaterna compuesta falla A4 y no es un suceso admisible. ∎

El contraejemplo pertenece al régimen general de operadores de VII.1. No se presenta como una trayectoria *append-only* y, por tanto, no contradice HNA.

### Criterio 5.2. Constitución del compuesto como suceso

Por la definición de VII.1 [6], una reevaluación compuesta constituye un nuevo suceso si y sólo si la cuaterna resultante satisface A1–A6. La composición parcial exige así dos verificaciones independientes:

1. D₁…ₘ ≠ ∅, para que exista la reevaluación compuesta.
2. A1–A6 para la cuaterna resultante, para que esa reevaluación constituya un suceso admisible.

La primera condición no implica la segunda.

### 5.3. Soporte efectivo con índices comunes

Si H₀ = H₁ = ⋯ = Hₘ = H y todas las configuraciones utilizan el mismo conjunto de posiciones Iₕ, puede definirse el soporte efectivo mínimo

σₘᵢₙ = { i ∈ Iₕ : existe x ∈ D₁…ₘ tal que la posición i de R₁…ₘ(x) difiere de la posición i de x }.

Este soporte efectivo no sustituye el soporte declarado de VII.1 [6]. Sólo se aplica cuando las posiciones iniciales y finales son directamente comparables. Si el cambio de horizonte exige transporte para identificarlas, la comparación debe realizarse mediante el régimen de transporte correspondiente [9–11].

### Corolario 5.4. Identidad funcional

La identidad funcional es neutral para la composición: R ∘ id = R e id ∘ R = R. Sin embargo, F(id(x)) − F(x) = 0 para todo observable compatible F. Por A4 [6], la identidad funcional no constituye por sí sola un suceso admisible.

---

## 6. Realización y cadena

### Definición 6.1. Tramo realizable

Se denomina tramo realizable a una sucesión ordenada (e₁, …, eₘ) para la que D₁…ₘ ≠ ∅. Equivale a la existencia de un estado inicial x₀ ∈ D₁ tal que, al definir xₖ = Rₖ(xₖ₋₁), cada xₖ₋₁ pertenece al dominio del operador siguiente.

Esta definición añade una exigencia que no se deduce de la composición por pares: un mismo estado inicial debe poder recorrer toda la sucesión.

### Proposición 6.2. La composición por pares no implica realización conjunta

Puede ocurrir que D₁…₂ ≠ ∅ y D₂…₃ ≠ ∅ y, sin embargo, D₁…₃ = ∅, incluso cuando e₁, e₂ y e₃ son sucesos admisibles.

**Demostración.** Considérese un horizonte H de SV(9,3) que contenga las configuraciones a = (0,0,0,0,0,0,0,0,0), b = (1,0,0,0,0,0,0,0,0), c = (0,1,0,0,0,0,0,0,0), d = (1,1,0,0,0,0,0,0,0) y e = (0,0,1,0,0,0,0,0,0). Sea F(S) = |{i : Sᵢ = 1}| un observable de 𝒜ₕ.

Defínanse D₁ = {a}, R₁(a) = b y σ₁ = {1}; D₂ = {b,c}, R₂(b) = d, R₂(c) = e y σ₂ = {2,3}; D₃ = {e}, R₃(e) = a y σ₃ = {3}. Para cada suceso declárese como control exterior la identidad sobre el complemento de su soporte. Todos los estados son legibles en H, los dominios son no vacíos y F presenta variación no nula al menos en a → b, b → d y e → a; al mantenerse el mismo horizonte, la compatibilidad observacional está declarada. Los tres pasos satisfacen A1–A6 [6].

El par (e₁, e₂) es realizable mediante a, porque a → b → d. El par (e₂, e₃) es realizable mediante c, porque c → e y e ∈ D₃. Sin embargo, el único recorrido que parte de D₁ es a → b → d, con d ∉ D₃. Por tanto, D₁…₃ = ∅. ∎

### Definición 6.3. Cadena

VII.3 establece que una sucesión de sucesos admisibles sólo constituye una cadena legítima cuando satisface, entre otras condiciones, composición local definible, compatibilidad de horizontes, transporte suficiente de observables y un criterio explícito de lectura acumulativa [8]. La mera existencia de sucesos consecutivos no basta.

### Definición 6.4. Cadena realizable

Se denomina cadena realizable a una cadena en el sentido de VII.3 [8] para la que, además, existe un testigo común de todo el recorrido.

En el régimen directamente tipado de §4, esta condición es D₁…ₘ ≠ ∅. Si la cadena de VII.3 enlaza horizontes compatibles mediante un transporte declarado, el testigo común debe conservarse a través de ese transporte. En ambos casos, la realizabilidad exige un único recorrido x₀ → x₁ → ⋯ → xₘ.

Una cadena realizable no constituye necesariamente un único suceso compuesto. Para que la cuaterna asociada al recorrido sea además un suceso admisible debe satisfacer A1–A6 de VII.1 [6]; en particular, A4 exige que algún observable compatible presente una variación neta no nula entre el estado inicial y el final.

---

## 7. Variación acumulada sobre recorridos realizados

VII.3 exige que una cadena declare un criterio de lectura acumulativa y un transporte suficiente de observables [8]. En el caso escalar de una cadena realizable, sea xₖ = Rₖ(xₖ₋₁) y denótese por Fₖ la lectura compatible del observable en el horizonte Hₖ.

### Teorema 7.1. Identidad telescópica

Fₘ(xₘ) − F₀(x₀) = Σₖ₌₁…ₘ [ Fₖ(xₖ) − Fₖ₋₁(xₖ₋₁) ].

Equivalentemente, Δ₁…ₘ F(x₀) = Σₖ₌₁…ₘ Δₑₖ F(xₖ₋₁).

**Demostración.** Los términos intermedios se cancelan dos a dos. ∎

La identidad anterior describe el caso escalar de un recorrido efectivamente realizado. Las formas más generales de acumulación de VII.3 conservan sus propias reglas de tipado y lectura [8].

---

## 8. Persistencia *append-only*, HNA y bifurcación

HNA es un teorema ya demostrado para una misma trayectoria *append-only* [13,14]. En la notación utilizada aquí puede expresarse del modo siguiente.

### Teorema 8.1. Persistencia de una posición clausurada

Sea T = (S₀, ν₀, S₁, ν₁, …) una trayectoria *append-only*. Si una posición p queda clausurada en el paso j con Sⱼ(p) = τ ∈ {0, 1}, entonces Sₖ(p) = τ para todo k > j. Ningún paso posterior de esa misma trayectoria vuelve a asignar U a p [13,14].

La afirmación se limita a la misma trayectoria. Si cambia la trayectoria o si cambia el horizonte de manera que la identificación de posiciones requiera transporte, la correspondencia debe justificarse en el régimen correspondiente [9–11].

### 8.2. Bifurcación

La bifurcación definida en [13] permite que dos trayectorias compartan un prefijo ya constituido y diverjan después mediante datos de transición distintos. El prefijo común se conserva: la trayectoria nueva no modifica retrospectivamente la anterior.

---

## 9. Precedencia y cadenas estrictas de habilitación

VII.2 define comparabilidad, afectación y precedencia entre sucesos admisibles [7]. Esas relaciones tienen alcance relacional y pueden establecerse por pares. La realizabilidad definida en §6 responde a otra pregunta: si existe un mismo recorrido que ejecute conjuntamente los pasos considerados. Precedencia y realizabilidad no se identifican.

### Definición 9.1. Número de posiciones con valor U

En una célula finita se define u(S) = |{i : Sᵢ = U}|.

### Teorema 9.2. Aciclicidad de las cadenas estrictas de habilitación por clausura de U

Sea S₀ —e₁→ S₁ —e₂→ ⋯ —eₘ→ Sₘ una cadena realizable dentro de una misma trayectoria *append-only*. Supóngase que cada paso clausura al menos una posición necesaria cuyo valor era U y que esa clausura habilita estrictamente el paso siguiente. Entonces u(Sₖ₊₁) < u(Sₖ) para todo k y la cadena no puede contener un ciclo.

**Demostración.** u(S) es un entero no negativo. Cada paso elimina al menos una posición del conjunto de posiciones cuyo valor es U. Por HNA, ninguna posición ya clausurada puede volver a U dentro de la misma trayectoria [13,14]. Por tanto, u(S) disminuye estrictamente en cada paso. Un ciclo exigiría recuperar un valor anterior de u, lo que es imposible. ∎

### Corolario 9.3. Cota finita

Si la célula tiene n posiciones, m ≤ u(S₀) ≤ n. En SV(9,3), m ≤ 9.

El Teorema 9.2 no afirma aciclicidad global de toda relación de precedencia de VII.2. Su alcance se limita a cadenas realizables de habilitación estricta por clausura de U dentro de una misma trayectoria *append-only*.

---

## 10. Cambio de horizonte y recurrencia estructural

El cambio de horizonte no autoriza a presumir continuidad. VII.4 distingue persistencia, reevaluación y no herencia [9]. VII.5 introduce un dato de enlace que declara el dominio enlazable, el transporte parcial y la herencia aceptable entre regímenes [10]. VII.6 limita la preservación, la invariancia y la equivalencia a subdominios expresamente declarados [11]. El tratamiento del suceso local y del suceso envolvente refuerza la necesidad de declarar el horizonte en el que se realiza cada comparación [12].

En consecuencia, una posición del horizonte de partida no se identifica por defecto con una posición del horizonte resultante. Esa identificación sólo puede afirmarse cuando existe el transporte correspondiente [10,11].

La repetición de un mismo *frame* visible tampoco implica identidad de suceso ni de activación. En la notación del régimen de recurrencia estructural de [15] puede cumplirse v(Sₙ) = v(S₀) con εₙ ≠ ε₀. La igualdad de la configuración visible no determina, por sí sola, la evaluación, la trayectoria ni el activador asociados. Esta posibilidad es compatible con HNA: una posición clausurada no se reabre dentro de la misma trayectoria, pero evaluaciones o recorridos distintos pueden presentar la misma configuración visible [13–15].

---

## 11. Síntesis de la dinámica general

Los resultados anteriores permiten establecer cinco relaciones principales:

1. **Separación de objetos.** El *frame* y el dato de transición se definen en [1,4]; el horizonte estructural, el suceso admisible y el operador de reevaluación, en VII.1 [6]. La dinámica exige conservar esas diferencias.
2. **Separación entre composición y suceso.** Las Definiciones 4.1 y 4.2 precisan cuándo existe una reevaluación compuesta; el Teorema 5.1 demuestra que esa existencia no basta para constituir un suceso. La admisibilidad del compuesto vuelve a depender de A1–A6 [6].
3. **Separación entre composición local y recorrido.** VII.3 establece las condiciones de cadena [8]. El tramo realizable y la cadena realizable añaden la existencia de un testigo común. La Proposición 6.2 demuestra que la composición por pares no garantiza ese testigo.
4. **Persistencia, bifurcación y aciclicidad restringida.** HNA y la bifurcación proceden de [13,14]. Sobre HNA y la realizabilidad, el Teorema 9.2 demuestra la aciclicidad del régimen estricto de habilitación por clausura de U.
5. **Cambio de horizonte e identidad.** El tránsito entre horizontes queda sometido a las condiciones de persistencia, enlace, transporte y preservación de [9–12]. La recurrencia de [15] demuestra que la igualdad de *frames* no determina identidad de activación.

Estas relaciones no exigen identidad global, composición total, monoide, grupo ni métrica general. Tampoco toman el tiempo como primitiva [5,12] ni la probabilidad como fundamento de la clausura [1–3].

---

## 12. Conclusión

La dinámica general del Suceso exige distinguir tres niveles que no pueden reducirse entre sí: la ejecución de reevaluaciones, la realización de un recorrido y la constitución de un suceso admisible. La composición funcional puede existir sin que exista un suceso compuesto; la composición por pares puede existir sin un recorrido conjunto; y una cadena realizable puede no satisfacer la no trivialidad necesaria para constituirse como un único suceso.

HNA preserva las posiciones clausuradas en una misma trayectoria *append-only* [13,14]. En el régimen estricto definido en §9, esa persistencia permite construir el rango u(S) y demostrar que las cadenas de habilitación por clausura de U son finitas y acíclicas. Los cambios de horizonte requieren transporte y preservación declarados [9–12], mientras que la recurrencia estructural impide identificar una configuración visible con un suceso o una activación determinados [15].

U permanece como un único valor de Σ. Las clasificaciones contextuales recaen sobre posiciones cuyo valor es U, no sobre U misma [13,14]. Con estas condiciones queda establecida una dinámica del Suceso suficiente para relacionar composición, realización, persistencia, bifurcación y cambio de horizonte sin introducir estructuras más fuertes de las necesarias.

---

## Referencias

[1] Lloret Egea, J. A. (2026). *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. DOI: 10.21428/39829d0b.b0cf9a13.

[2] Lloret Egea, J. A. (2026). *Origen de fundamentos, definición y alcance de la U en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.f433065f.

[3] Lloret Egea, J. A. (2026). *Transiciones estructurales y trayectorias de la U en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.10e10f96.

[4] Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta*. DOI: 10.21428/39829d0b.bb86c65d.

[5] Lloret Egea, J. A. (2026). *Documento VII.0 — Hacia una geometría eventivo-espacial sin tiempo canónico: horizonte declarado, sucesos y reevaluación situacional en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.89e77c19.

[6] Lloret Egea, J. A. (2026). *Teoría rigurosa del suceso admisible en el Sistema Vectorial SV. Documento VII.1*. DOI: 10.21428/39829d0b.1608c18c.

[7] Lloret Egea, J. A. (2026). *VII.2 — Precedencia, compatibilidad y afectación entre sucesos admisibles en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.1f58d8a2.

[8] Lloret Egea, J. A. (2026). *VII.3 — Cadenas, acumulación y regímenes de paso entre sucesos admisibles en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.6326ca96.

[9] Lloret Egea, J. A. (2026). *VII.4 — Respuesta estructural, umbral, transición de régimen y preparación de células especializadas en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.300a3099.

[10] Lloret Egea, J. A. (2026). *VII.5 — Enlace formal entre acumulaciones sucesivas en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.55f0e22d.

[11] Lloret Egea, J. A. (2026). *Equivalencia parcial, preservación e invariancia local entre regímenes en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.9d3f0a9d.

[12] Lloret Egea, J. A. (2026). *Suceso local, suceso envolvente y reevaluación situacional en horizonte declarado en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.09daf43b.

[13] Lloret Egea, J. A. (2026). *Convergencia ternaria y gobierno determinista de trayectorias en el Sistema Vectorial SV: tipología de la indeterminación, HNA como teorema y fundamentos de la célula NLP*. DOI: 10.21428/39829d0b.802bed57.

[14] Lloret Egea, J. A. (2026). *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador*. DOI: 10.21428/39829d0b.67195860.

[15] Lloret Egea, J. A. (2026). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. DOI: 10.21428/39829d0b.2b3c9808.
