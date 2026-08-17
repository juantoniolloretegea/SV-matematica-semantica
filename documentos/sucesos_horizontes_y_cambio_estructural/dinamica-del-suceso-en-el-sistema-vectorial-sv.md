# Dinámica del Suceso en el Sistema Vectorial SV

**Juan Antonio Lloret Egea**
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® (ITVIA)
ORCID: 0000-0002-6634-3351
Madrid, 17 de agosto de 2026

---

## Resumen

La dinámica del Suceso en el Sistema Vectorial SV reúne objetos ya constituidos en el corpus y resultados desarrollados en este trabajo. La configuración o *frame* y el dato de transición proceden de los fundamentos celulares y de la composición intercelular [1,4]; el suceso admisible se define en VII.1 [6]; y la noción estructural de cadena procede de VII.3 [8]. Estos objetos no se identifican entre sí.

VII.1 define un suceso admisible como e = (H, H′, σ, Rₑ), con Rₑ : Dₑ → X_H′, sometido a seis condiciones de admisibilidad A1–A6 [6]. Entre ellas, A4 exige que exista al menos un observable compatible cuya lectura cambie entre la entrada y la salida. A partir de esa definición, este trabajo formaliza la composición sucesiva de los operadores Rₑ sobre un dominio efectivo común y demuestra que la existencia de la reevaluación compuesta no basta para constituir un nuevo suceso: la cuaterna resultante debe satisfacer de nuevo A1–A6 [6].

Para evitar confundir niveles distintos, se introducen dos nociones adicionales. Se denomina **tramo realizable** a una sucesión de sucesos para la que existe un mismo estado inicial capaz de atravesar todos los dominios sucesivos. Se denomina **cadena realizable** a una cadena en el sentido de VII.3 —composición local, compatibilidad de horizontes, transporte suficiente de observables y lectura acumulativa [8]— que además posee ese testigo común. Un **suceso compuesto**, en cambio, sólo existe cuando la cuaterna asociada al recorrido satisface nuevamente A1–A6 [6]. De este modo, tramo realizable, cadena y suceso compuesto quedan separados.

Sobre esta base se demuestra que la composición por pares no garantiza una realización conjunta y que, sobre recorridos realizados con observables compatibles, la variación total satisface una identidad telescópica. El teorema HNA preserva las posiciones clausuradas dentro de una misma trayectoria canónica *append-only* [13,14], y la bifurcación conserva el prefijo ya constituido sin modificar registros anteriores [13]. Como consecuencia adicional, en las cadenas estrictas de habilitación mediante clausura de posiciones cuyo valor es U, el número de tales posiciones proporciona un rango finito y excluye ciclos.

Los cambios de horizonte no se resuelven por continuidad presumida: VII.4 distingue persistencia, reevaluación y no herencia [9]; VII.5 formaliza el enlace tipado entre regímenes [10]; y VII.6 limita preservación, invariancia y equivalencia a subdominios declarados [11]. La recurrencia estructural permite además que una misma configuración visible aparezca en evaluaciones distintas sin identidad de suceso o activación [15].

U es uno de los tres valores del alfabeto Σ = {0, 1, U} [1–3] y no admite subtipos. Las clasificaciones de resolubilidad, frontera, criticidad o vecindad recaen sobre posiciones cuyo valor es U y dependen del horizonte declarado [13,14]; no modifican U ni amplían el alfabeto.

Las referencias indican la procedencia de las nociones heredadas. Las definiciones de dominio efectivo, reevaluación compuesta, tramo realizable y cadena realizable, así como los resultados de separación entre composición y suceso, falta de realización conjunta por mera composición por pares, telescopía y aciclicidad estricta, se desarrollan en este trabajo.

**Palabras clave:** Sistema Vectorial SV; Suceso; suceso admisible; *frame*; horizonte; U; reevaluación; cadena realizable; HNA; *append-only*.

---

## 1. Base ternaria y celular

El Sistema Vectorial SV utiliza el alfabeto Σ = {0, 1, U} [1–3]. Una célula de base b dispone de n = b² posiciones y una configuración, denominada *frame* en el SV, es S = (s₁, …, sₙ) ∈ Σⁿ. La instancia canónica de primer nivel es SV(9,3), sin que la dinámica general quede restringida a nueve posiciones [1,4].

Los fundamentos fijan el *frame* como configuración celular [1], mientras que VII.1 define el suceso como una cuaterna que actúa sobre configuraciones legibles [6]. Por ello, el *frame* no es el suceso: dos evaluaciones pueden presentar la misma configuración visible sin constituir el mismo suceso ni pertenecer al mismo recorrido. La misma separación reaparece en la recurrencia estructural, donde una configuración visible puede repetirse con activaciones distintas [15].

### 1.1. Unicidad de U y clasificación contextual de las posiciones

El alfabeto Σ contiene exactamente tres valores: 0, 1 y U. U es un único valor de Σ y no admite subtipos.

En [13], la función Γ_H se aplica a una posición i cuyo valor es U y devuelve una de tres categorías: irreducible, fronteriza o resoluble. Las definiciones subsiguientes reúnen los índices de las posiciones en tres conjuntos según el resultado de Γ_H. La clasificación recae, por tanto, sobre la posición respecto del horizonte declarado, no sobre U.

En [14] se emplea después la formulación según la cual una posición pᵢ = U puede tipificarse y aparecen las expresiones «U irreducible», «U fronteriza» y «U resoluble». Este trabajo adopta un refinamiento terminológico de esa formulación: tales expresiones designan posiciones con valor U clasificadas por Γ_H; no constituyen valores distintos, variantes ni clases de U. El alfabeto permanece Σ = {0, 1, U}. El mismo criterio se aplica a la criticidad, la vecindad y cualquier otra propiedad contextual: califican la posición o su situación respecto del horizonte, no a U.

La asignación legítima de U a una posición no expresa probabilidad, espera, transición en curso ni simple cálculo pendiente. Expresa no clausura tras el agotamiento trazable de las vías admisibles disponibles en el dominio y horizonte declarados [2,3,13].

---

## 2. Tipado de los objetos

En el SV se emplean dos nociones de horizonte con funciones distintas. En el álgebra de composición intercelular se define el horizonte de tipos de suceso ℋ(𝒜) = {ε₁, …, εₘ} [4]. Cada εᵢ representa un tipo de suceso declarado para la arquitectura. El dato de transición adopta la forma νₙ = {(εᵢ, τᵢ)}ᵢ∈Iₙ, con τᵢ ∈ Σ; el valor τᵢ indica que consta incidencia, que consta no incidencia o que no existe base suficiente para clausurar la instancia en 0 o 1.

VII.1 define, por otra parte, el horizonte estructural H = (I_H, ≼_H, X_H, 𝒜_H), que determina las posiciones, la relación interna, el espacio de configuraciones legibles y la familia de observables [6].

Por tanto, ℋ(𝒜), H, εᵢ, τᵢ, νₙ, S, e y Rₑ son objetos distintos. En particular, e ≠ ν, e ≠ S y e ≠ ε. El dato ν puede inducir una reevaluación en la arquitectura de [4], pero no se identifica por ello con el suceso admisible e de VII.1.

Las reutilizaciones posteriores de la notación conservan el significado del régimen en que se definen. En [15], por ejemplo, εₖ designa un activador indexado y no el tipo εᵢ del horizonte ℋ(𝒜); los usos posteriores de ν tampoco identifican automáticamente el dato de transición de [4] con el suceso admisible [14,15].

---

## 3. Suceso admisible

VII.1 define el suceso admisible como la cuaterna e = (H, H′, σ, Rₑ), donde Rₑ : Dₑ → X_H′, Dₑ ⊆ X_H y Dₑ ≠ ∅ [6]. La admisibilidad exige:

1. **A1 — soporte bien tipado:** σ ⊆ I_H.
2. **A2 — dominio no vacío y operador bien tipado.**
3. **A3 — legibilidad de la entrada y de la salida.**
4. **A4 — no trivialidad del suceso:** existe un observable compatible F y un punto x ∈ Dₑ tales que F_H′(Rₑ(x)) − F_H(x) ≠ 0.
5. **A5 — control exterior parcial:** existe al menos un control Cₑ = (Jₑ, θₑ), con Jₑ ⊆ I_H ∖ σ y una aplicación parcial θₑ : Jₑ → I_H′, de modo que la región exterior declarada no desaparezca del análisis sin correspondencia formal.
6. **A6 — compatibilidad observacional declarada:** la comparación entre las lecturas F_H y F_H′ sólo puede invocarse cuando la familia observacional ha sido declarada compatible entre los horizontes considerados.

Estas seis condiciones pertenecen a la definición de admisibilidad de VII.1 [6]. En particular, A4 excluye como suceso una transformación que no produzca variación en ningún observable compatible dentro del dominio y alcance declarados [6].

---

## 4. Composición de reevaluaciones

VII.1 asocia a cada suceso admisible eₖ un operador de reevaluación Rₖ con dominio declarado y deja abierta la composición parcial de sucesos [6]. Sean eₖ = (Hₖ₋₁, Hₖ, σₖ, Rₖ), para k = 1, …, m, sucesos admisibles tales que el horizonte de llegada de cada eₖ coincide con el horizonte de partida de eₖ₊₁. Las Definiciones 4.1 y 4.2 formalizan en este trabajo cuándo esa sucesión de operadores puede ejecutarse sobre un mismo estado inicial.

### Definición 4.1. Dominio efectivo

Se denomina D₁…ₘ al conjunto de estados iniciales sobre los que puede ejecutarse toda la sucesión:

D₁…ₘ = {x ∈ D₁ : R₁(x) ∈ D₂, R₂(R₁(x)) ∈ D₃, …, (Rₘ₋₁ ∘ ⋯ ∘ R₁)(x) ∈ Dₘ}.

### Definición 4.2. Reevaluación compuesta

Si D₁…ₘ ≠ ∅, se define R₁…ₘ(x) = (Rₘ ∘ ⋯ ∘ R₁)(x) para todo x ∈ D₁…ₘ.

### Teorema 4.3. Asociatividad de la composición

Sobre el dominio efectivo común, R₃ ∘ (R₂ ∘ R₁) = (R₃ ∘ R₂) ∘ R₁; la misma igualdad vale para cualquier número finito de operadores.

**Demostración.** Es la asociatividad ordinaria de la composición funcional, restringida al dominio donde están definidas todas las aplicaciones sucesivas. (c.q.d.)

La asociatividad pertenece a la composición funcional y no establece la clausura de la clase de sucesos admisibles bajo composición.

---

## 5. Separación entre reevaluación compuesta y suceso admisible

### Teorema 5.1. Separación

La existencia de R₁…ₘ no implica que la cuaterna candidata e₁…ₘ = (H₀, Hₘ, σ₁…ₘ, R₁…ₘ) sea un suceso admisible.

**Demostración.** Considérese SV(9,3) sobre un horizonte H tal que S₀ = (0,0,0,0,0,0,0,0,0) y S₁ = (1,0,0,0,0,0,0,0,0) pertenecen a X_H. Sean D₁ = {S₀}, R₁(S₀) = S₁, D₂ = {S₁} y R₂(S₁) = S₀.

Tómese en ambos sucesos el soporte σ = {1}, el control exterior común Cₑ₁ = Cₑ₂ = (J, id_J), con J = {2, …, 9}, y el observable compatible F ∈ 𝒜_H definido por F(S) = |{i : Sᵢ = 1}|. Entonces Δₑ₁F(S₀) = 1 y Δₑ₂F(S₁) = −1. Cada suceso presenta, por tanto, variación observable no nula y satisface las condiciones de soporte, dominio, legibilidad, control exterior y compatibilidad observacional en el horizonte declarado.

Sin embargo, D₁…₂ = {S₀} y R₁…₂(S₀) = S₀. Como el estado inicial y el final coinciden y el horizonte es el mismo, para todo observable G ∈ 𝒜_H se cumple G(R₁…₂(S₀)) − G(S₀) = 0. La cuaterna candidata no satisface A4, condición constitutiva de VII.1 [6], y no es un suceso admisible. (c.q.d.)

El contraejemplo pertenece a la capa operatoria de VII.1; no se presenta como una trayectoria canónica *append-only*.

### Criterio 5.2. Constitución del compuesto como suceso

Por la definición de suceso admisible de VII.1 [6], una reevaluación compuesta constituye un nuevo suceso si y sólo si la cuaterna correspondiente satisface de nuevo A1–A6. En particular, que R₁…ₘ esté definido no implica que e₁…ₘ sea admisible. Quedan así separadas las dos cuestiones que intervienen en la composición parcial: primero, si la sucesión de operadores está definida sobre algún estado inicial común; segundo, si el resultado reúne nuevamente las condiciones que permiten llamarlo suceso admisible.

### 5.3. Soporte efectivo con índices comunes

Si H₀ = H₁ = ⋯ = Hₘ = H y todas las configuraciones utilizan el mismo conjunto de posiciones I_H, puede definirse como soporte efectivo mínimo

σₘᵢₙ = {i ∈ I_H : existe x ∈ D₁…ₘ tal que la posición i de R₁…ₘ(x) difiere de la posición i de x}.

Esta definición no sustituye el soporte declarado de VII.1. Se aplica cuando las posiciones iniciales y finales son directamente comparables. Si el cambio de horizonte exige transporte para identificarlas, el soporte se determina conforme al régimen correspondiente [9–11].

### Corolario 5.4. Identidad funcional

La identidad funcional es neutral para la composición: R ∘ id = R e id ∘ R = R. Sin embargo, para todo observable compatible F se cumple F(id(x)) − F(x) = 0. En consecuencia, la identidad funcional falla A4 y no constituye por sí sola un suceso admisible en el sentido de VII.1 [6].

---

## 6. Realización y cadena

### Definición 6.1. Tramo realizable

Esta definición es propia del presente trabajo. Una sucesión ordenada (e₁, …, eₘ) es realizable si D₁…ₘ ≠ ∅. Equivale a la existencia de x₀ ∈ D₁ tal que, al definir xₖ = Rₖ(xₖ₋₁), cada xₖ₋₁ pertenece al dominio del operador siguiente.

### Proposición 6.2. La composición por pares no implica realización conjunta

Puede ocurrir que D₁…₂ ≠ ∅ y D₂…₃ ≠ ∅ y, sin embargo, D₁…₃ = ∅.

**Demostración.** Considérense cinco configuraciones legibles a, b, c, d y e. Sean D₁ = {a}, R₁(a) = b; D₂ = {b, c}, R₂(b) = d y R₂(c) = e; y D₃ = {e}. El primer par admite composición mediante a y el segundo mediante c. No obstante, el único recorrido que parte de D₁ es a ↦ b ↦ d, con d ∉ D₃. No existe un testigo común para toda la sucesión. (c.q.d.)

### Definición 6.3. Cadena

VII.3 define una cadena de sucesos admisibles mediante cuatro condiciones: composición local definible, compatibilidad de horizontes, transporte suficiente de observables y criterio explícito de lectura acumulativa [8]. Esas cuatro condiciones pertenecen a VII.3 y no se sustituyen por la mera existencia de D₁…ₘ.

### Definición 6.4. Cadena realizable

La noción de cadena realizable se introduce aquí para añadir a la cadena de VII.3 [8] una condición que VII.3 no expresa por sí sola: la existencia de un testigo común para toda la sucesión. Así, una cadena realizable es una cadena en el sentido de VII.3 que, además, satisface D₁…ₘ ≠ ∅ y permite representar un único recorrido efectivo x₀ ↦ x₁ ↦ ⋯ ↦ xₘ.

Una cadena realizable no constituye necesariamente un único suceso compuesto. Para que la cuaterna asociada al recorrido sea además un suceso compuesto debe satisfacer A1–A6 de VII.1 [6]; en particular, A4 exige que la lectura final de algún observable compatible difiera de su lectura inicial.

---

## 7. Aditividad sobre recorridos realizados

VII.3 exige que una cadena declare un criterio de lectura acumulativa y transporte suficiente de observables [8]. El Teorema 7.1 fija, dentro de ese marco, el caso escalar de una cadena realizable: sea xₖ = Rₖ(xₖ₋₁) y denotemos por Fₖ la lectura compatible del observable en el horizonte Hₖ.

### Teorema 7.1. Identidad telescópica de la variación observable

Fₘ(xₘ) − F₀(x₀) = Σₖ₌₁…ₘ [Fₖ(xₖ) − Fₖ₋₁(xₖ₋₁)].

Equivalentemente, Δ₁…ₘF(x₀) = Σₖ₌₁…ₘ ΔₑₖF(xₖ₋₁).

**Demostración.** Los términos intermedios se cancelan dos a dos. (c.q.d.)

La identidad corresponde al caso escalar de un recorrido realizado. Las formas más generales de acumulación definidas en VII.3 mantienen sus reglas propias de tipado y lectura [8].

---

## 8. Persistencia append-only, HNA y bifurcación

HNA es un teorema ya demostrado en el corpus para una misma trayectoria canónica *append-only* [13,14]. El Teorema 8.1 lo enuncia en la notación empleada en este trabajo.

### Teorema 8.1. Persistencia de una posición clausurada

Sea T = (S₀, ν₀, S₁, ν₁, …) una trayectoria canónica *append-only*. Si una posición p queda clausurada en el paso j con Sⱼ(p) = τ ∈ {0, 1}, entonces Sₖ(p) = τ para todo k > j. Ningún paso posterior de esa trayectoria vuelve a asignar U a p.

La afirmación se refiere a la misma trayectoria canónica. Si cambia la trayectoria o el horizonte y la identificación de posiciones requiere transporte, la correspondencia debe establecerse en el régimen pertinente.

### 8.2. Bifurcación

La semántica de *fork* de [13] permite que dos trayectorias compartan un prefijo ya constituido y diverjan después mediante datos de transición distintos. La bifurcación conserva íntegro el prefijo común y genera trayectorias posteriores distintas sin modificar los registros anteriores.

---

## 9. Precedencia y cadenas estrictas de habilitación

VII.2 define comparabilidad, afectación y precedencia entre sucesos admisibles [7]. Esas relaciones pueden establecerse por pares. Este trabajo añade una condición distinta cuando se afirma una trayectoria efectiva: debe existir un mismo recorrido que realice conjuntamente los pasos considerados. La precedencia relacional de VII.2 y la realizabilidad del recorrido no se identifican.

### Definición 9.1. Número de posiciones con valor U

En una célula finita se define u(S) = |{i : Sᵢ = U}|.

### Teorema 9.2. Aciclicidad de las cadenas estrictas de habilitación por clausura de posiciones con valor U

Como consecuencia de la realizabilidad introducida en §6 y de HNA [13,14], considérese S₀ —e₁→ S₁ —e₂→ ⋯ —eₘ→ Sₘ una cadena realizable dentro de una misma trayectoria canónica *append-only*. Supóngase que cada paso habilita estrictamente al siguiente mediante la clausura de al menos una posición necesaria cuyo valor era U. Entonces u(Sₖ₊₁) < u(Sₖ) para todo k y la cadena no puede contener un ciclo.

**Demostración.** u(S) es un entero no negativo. Cada paso clausura al menos una posición cuyo valor era U. Por el Teorema 8.1, ninguna posición ya clausurada puede recuperar el valor U dentro de esa misma trayectoria canónica. Por tanto, u(S) disminuye estrictamente en cada paso. Un ciclo exigiría recuperar un valor anterior de u, lo que es imposible. (c.q.d.)

### Corolario 9.3. Cota finita

Si la célula tiene n posiciones, m ≤ u(S₀) ≤ n. En SV(9,3), m ≤ 9.

El Teorema 9.2 se refiere exclusivamente a cadenas realizables de habilitación estricta por clausura de U dentro de una misma trayectoria canónica *append-only*.

---

## 10. Cambio de horizonte y recurrencia estructural

Si una reevaluación modifica el conjunto de posiciones, su identificación o la familia de observables, la continuidad entre horizontes no se presume [5,12]. VII.4 distingue persistencia, reevaluación y no herencia [9]; VII.5 formaliza el enlace tipado entre regímenes [10]; y VII.6 restringe la preservación, la invariancia y la equivalencia a los subdominios en los que se han establecido [11].

VII.5 y VII.6 sólo sostienen transporte, preservación o equivalencia sobre dominios y familias expresamente declarados [10,11]. En ausencia de ese transporte, la dinámica no puede identificar por defecto una posición del horizonte de partida con otra del horizonte resultante.

La repetición de un mismo *frame* visible tampoco implica identidad de suceso ni de activación. En el régimen de recurrencia estructural de [15] puede cumplirse v(Sₙ) = v(S₀) con εₙ ≠ ε₀. La distinción entre ambas comparecencias depende de la evaluación o trayectoria a la que pertenecen y, cuando el régimen indexa activaciones, del activador asociado; no del *frame* considerado aisladamente. Esto es compatible con HNA: la persistencia impide que una posición clausurada recupere U dentro de una misma trayectoria canónica, pero no impide que evaluaciones o recorridos estructuralmente distintos presenten la misma configuración visible.

---

## 11. Síntesis estructural

Los resultados anteriores permiten resumir la dinámica general del Suceso en cinco relaciones:

1. **Separación de objetos:** el *frame* y el dato de transición proceden de [1,4], mientras que horizonte estructural, suceso admisible y operador de reevaluación proceden de VII.1 [6]. Estos objetos conservan su identidad matemática propia.
2. **Separación entre operación y suceso:** la composición funcional de los operadores se desarrolla en §§4–5; el compuesto sólo constituye un suceso cuando satisface las seis condiciones A1–A6 de VII.1 [6].
3. **Separación entre composición local y recorrido:** la cadena conserva las cuatro condiciones de VII.3 [8]; la exigencia de un testigo común para afirmar una realización efectiva se introduce en §6, y sobre esa realización se obtiene la identidad telescópica de §7.
4. **Persistencia y bifurcación:** HNA y la semántica de *fork* proceden de [13,14]. A partir de HNA y de la cadena realizable, §9 demuestra la aciclicidad del régimen estricto de habilitación por clausura de U.
5. **Cambio de horizonte:** persistencia, reevaluación y no herencia proceden de VII.4 [9]; el enlace tipado, de VII.5 [10]; la preservación e invariancia local, de VII.6 [11]; y la recurrencia con activadores distintos, de [15].

Estas relaciones no exigen identidad global, composición total, monoide, grupo ni métrica general; tampoco toman el tiempo canónico como primitiva [5,12] ni la probabilidad como fundamento de la clausura [1–3].

---

## 12. Conclusión

La dinámica del Suceso distingue la ejecución de una reevaluación de la constitución de un suceso admisible y separa la composición local de la existencia de un recorrido común. HNA y la bifurcación se reciben de [13,14]; la aciclicidad del régimen estricto de clausura de U se demuestra en §9; y el cambio de horizonte queda sujeto al transporte y a las condiciones de preservación establecidas en VII.4–VII.6 [9–11].

U permanece como un único valor de Σ y las clasificaciones contextuales recaen sobre posiciones, no sobre U. La igualdad de *frames* no determina identidad de suceso ni de activación. La estructura resultante describe la dinámica general del Suceso sin exigir continuidad global, tiempo canónico, probabilidad ni una composición total de sucesos.

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
