# Dinámica del Suceso en el Sistema Vectorial SV

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0). Esta licencia se aplica exclusivamente a esta versión |Madrid, 17 de agosto de 2026

---

## Resumen

La dinámica del Suceso en el Sistema Vectorial SV distingue entre configuración, dato de transición, reevaluación, suceso admisible y cadena. Sobre la base ternaria y celular del SV, una configuración o *frame* S ∈ Σⁿ, con Σ = {0, 1, U}, no constituye por sí misma un suceso; tampoco toda transformación ejecutable adquiere la condición de suceso admisible.

Sea

e = (H, H′, σ, Rₑ)

un suceso admisible, con Rₑ : Dₑ → X_H′, sometido a las condiciones A1–A6 de VII.1. Para una sucesión de sucesos cuyos horizontes consecutivos coinciden conforme al tipado declarado se define un dominio efectivo común y una reevaluación compuesta R[1:m]. La composición funcional es asociativa sobre ese dominio, pero la existencia de R[1:m] no basta para constituir un nuevo suceso: la cuaterna resultante debe satisfacer de nuevo A1–A6, incluida la condición A4 de variación observable no nula.

Esta separación permite distinguir el tramo realizable por composición, la cadena de sucesos de VII.3 y el suceso compuesto. Se demuestra que la componibilidad por pares no garantiza una realización conjunta y que, sobre recorridos realizados con observables compatibles, la variación total satisface una identidad telescópica. El teorema HNA preserva las posiciones clausuradas dentro de una misma trayectoria canónica *append-only*. En las cadenas estrictas de habilitación mediante clausura de posiciones cuyo valor es U, el número de tales posiciones proporciona un rango finito y excluye ciclos. La bifurcación conserva el prefijo ya constituido y permite trayectorias posteriores distintas sin alteración retrospectiva.

Cuando cambia el horizonte, el transporte, la persistencia, la reevaluación, la no herencia y la preservación parcial se rigen por los resultados establecidos para los regímenes heterogéneos. La continuidad y la equivalencia global no se presumen.

La U es única y no admite tipado. Las clasificaciones de resolubilidad, frontera, criticidad o vecindad califican la situación de una posición respecto de un horizonte; no producen especies distintas de U. La estructura descrita no exige identidad global, composición total, monoide, grupo ni métrica general; tampoco toma el tiempo canónico o la probabilidad como primitivas.

**Palabras clave:** Sistema Vectorial SV; Suceso; suceso admisible; *frame*; horizonte; U; reevaluación; cadena realizable; HNA; *append-only*.

---

## 1. Base ternaria y celular

El Sistema Vectorial SV utiliza el alfabeto [1–3]

Σ = {0, 1, U}.

Una célula de base b dispone de

n = b²

posiciones. Una configuración, denominada *frame* en el SV, es

S = (s₁, …, sₙ) ∈ Σⁿ.

La instancia canónica de primer nivel es SV(9,3), sin que la dinámica general quede restringida a nueve posiciones [1,4].

El *frame* representa una configuración celular; no es un suceso. Por ello,

S(a) = S(b)

no implica identidad de los sucesos ni de los recorridos asociados a ambas configuraciones. Esta distinción resulta asimismo necesaria en la recurrencia estructural, donde puede repetirse una configuración visible sin repetirse el suceso [15].

### 1.1. U única y no tipada

La U conserva un único estatuto dentro de Σ. No existen subtipos de U.

Si una posición p satisface

S(p) = U,

su situación puede clasificarse respecto de un horizonte declarado —por ejemplo, como resoluble, fronteriza o irreducible según la clasificación de [13]— sin alterar el valor de la posición:

S(p) = U.

Las nociones de criticidad, vecindad u otras propiedades contextuales se aplican igualmente a la posición o a su situación en el horizonte, no a U.

Una U genuina tampoco equivale a probabilidad, transición en curso, promedio, error ni cálculo pendiente. Expresa no clausura tras el agotamiento trazable de las vías admisibles disponibles en el dominio y horizonte declarados [2,3,13].

---

## 2. Tipado de los objetos

El corpus contiene dos objetos distintos denominados horizonte.

En el álgebra de composición intercelular aparece el horizonte de tipos de suceso [4]:

ℋ(𝒜) = {ε₁, …, εₘ}.

Cada εᵢ representa un tipo de suceso declarado para la arquitectura. El dato de transición adopta la forma

νₙ = {(εᵢ, τᵢ)}ᵢ∈Iₙ ,    τᵢ ∈ Σ,

donde τᵢ registra el valor ternario de la instancia: consta incidencia, consta no incidencia o la instancia no puede clausurarse suficientemente.

VII.1 define, por otra parte, el horizonte estructural [6]:

H = (I_H, ≼_H, X_H, 𝒜_H),

que determina las posiciones, la relación interna, el espacio de configuraciones legibles y la familia de observables.

Son, por tanto, objetos distintos:

ℋ(𝒜),   H,   εᵢ,   τᵢ,   νₙ,   S,   e,   Rₑ.

En particular,

e ≠ ν,    e ≠ S,    e ≠ ε.

Los usos de ε o ν en regímenes especializados conservan el significado definido en esos regímenes y no identifican los objetos anteriores [14,15].

---

## 3. Suceso admisible

VII.1 define el suceso admisible como la cuaterna [6]

e = (H, H′, σ, Rₑ),

donde

Rₑ : Dₑ → X_H′,    Dₑ ⊆ X_H,    Dₑ ≠ ∅.

La admisibilidad exige las condiciones siguientes:

1. **A1 — soporte bien tipado**

   σ ⊆ I_H;

2. **A2 — dominio no vacío y operador bien tipado;**

3. **A3 — legibilidad de la entrada y de la salida;**

4. **A4 — no trivialidad del suceso:** existe un observable compatible F y un punto x ∈ Dₑ tales que

   Δₑ F(x) = F[H′](Rₑ(x)) − F[H](x) ≠ 0;

5. **A5 — control exterior parcial;**

6. **A6 — compatibilidad observacional declarada.**

A4 es una condición constitutiva. Una transformación que no produzca variación en ningún observable compatible dentro del dominio y del alcance declarados no constituye un suceso admisible.

---

## 4. Composición de reevaluaciones

Sean

eₖ = (Hₖ₋₁, Hₖ, σₖ, Rₖ),    k = 1, …, m,

sucesos admisibles tales que el horizonte de llegada de cada eₖ coincide con el horizonte de partida de eₖ₊₁.

### Definición 4.1. Dominio efectivo

Se define

D[1:m] = { x ∈ D₁ : R₁(x) ∈ D₂, R₂(R₁(x)) ∈ D₃, …, Rₘ₋₁⋯R₁(x) ∈ Dₘ }.

### Definición 4.2. Reevaluación compuesta

Si

D[1:m] ≠ ∅,

se define

R[1:m] = Rₘ ∘ ⋯ ∘ R₁, restringida a D[1:m].

La condición D[1:m] ≠ ∅ garantiza la existencia de al menos un estado inicial sobre el que puede ejecutarse toda la sucesión de reevaluaciones.

### Teorema 4.3. Asociatividad de la composición

Sobre el dominio efectivo común,

R₃ ∘ (R₂ ∘ R₁) = (R₃ ∘ R₂) ∘ R₁.

La misma igualdad vale para cualquier número finito de operadores.

**Demostración.** Es la asociatividad ordinaria de la composición funcional, restringida al dominio donde están definidas todas las aplicaciones sucesivas. ∎

Esta igualdad pertenece a la composición funcional y no establece la clausura de la clase de sucesos admisibles bajo composición.

---

## 5. Separación entre reevaluación compuesta y suceso admisible

### Teorema 5.1. Separación

La existencia de R[1:m] no implica que la cuaterna candidata

e[1:m] = (H₀, Hₘ, σ[1:m], R[1:m])

sea un suceso admisible.

**Demostración.** Considérese SV(9,3) sobre un horizonte H tal que

S₀ = (0,0,0,0,0,0,0,0,0),
S₁ = (1,0,0,0,0,0,0,0,0)

pertenecen a X_H. Sean

D₁ = {S₀},    R₁(S₀) = S₁,

y

D₂ = {S₁},    R₂(S₁) = S₀.

Tómese en ambos sucesos el soporte

σ = {1},

el control exterior común

Cₑ₁ = Cₑ₂ = (J, id_J),    J = {2, …, 9},

y el observable compatible F ∈ 𝒜_H,

F(S) = |{ i : Sᵢ = 1 }|.

Se obtiene

Δₑ₁ F(S₀) = 1,
Δₑ₂ F(S₁) = −1.

Así, cada suceso presenta variación observable no nula y satisface las condiciones de soporte, dominio, legibilidad, control exterior y compatibilidad observacional en el horizonte declarado. Sin embargo,

D[1:2] = {S₀},
R[1:2](S₀) = S₀.

Como el estado inicial y el final coinciden y el horizonte es el mismo, para todo observable G ∈ 𝒜_H se cumple

G(R[1:2](S₀)) − G(S₀) = 0.

La cuaterna candidata no satisface A4 y, por tanto, no es un suceso admisible. ∎

### Criterio 5.2. Constitución del compuesto como suceso

Una reevaluación compuesta constituye un nuevo suceso si y sólo si la cuaterna correspondiente satisface de nuevo A1–A6.

En particular,

R[1:m] definido  ⇏  e[1:m] admisible.

La composición parcial exige, por tanto, dos comprobaciones independientes: la existencia de la reevaluación compuesta y la admisibilidad de la cuaterna resultante.

### 5.3. Soporte efectivo con índices comunes

Si

H₀ = H₁ = ⋯ = Hₘ = H

y todas las configuraciones utilizan el mismo conjunto de posiciones I_H, el soporte efectivo mínimo puede definirse como

{ i ∈ I_H : existe x ∈ D[1:m] tal que la posición i de R[1:m](x) difiere de xᵢ }.

Esta definición no sustituye el soporte declarado de VII.1. Se aplica cuando las posiciones iniciales y finales son directamente comparables. Si el cambio de horizonte exige transporte para identificarlas, el soporte se determina conforme al régimen correspondiente [9–11].

### Corolario 5.4. Identidad funcional

La identidad funcional es neutral para la composición:

R ∘ id = R,
id ∘ R = R.

Sin embargo,

Δid F(x) = 0

para todo observable compatible. En consecuencia, la identidad funcional no constituye por sí sola un suceso admisible.

---

## 6. Realizabilidad y cadena

### Definición 6.1. Tramo realizable

Una sucesión ordenada

(e₁, …, eₘ)

es realizable si

D[1:m] ≠ ∅.

Equivale a la existencia de un x₀ ∈ D₁ tal que, al definir

xₖ = Rₖ(xₖ₋₁),

cada xₖ₋₁ pertenece al dominio del operador siguiente.

### Proposición 6.2. La componibilidad por pares no implica realización conjunta

Puede ocurrir

D[1:2] ≠ ∅,    D[2:3] ≠ ∅,

y, sin embargo,

D[1:3] = ∅.

**Demostración.** Sean

D₁ = {a},    R₁(a) = b,

D₂ = {b, c},    R₂(b) = d,    R₂(c) = e,

y

D₃ = {e}.

El primer par es componible mediante a, y el segundo, mediante c. No obstante, el único recorrido que parte de D₁ es

a ↦ b ↦ d,

con d ∉ D₃. No existe, por tanto, un testigo común para toda la sucesión. ∎

### Definición 6.3. Cadena

VII.3 define una cadena de sucesos admisibles mediante cuatro condiciones: composición local definible, compatibilidad de horizontes, transporte suficiente de observables y criterio explícito de lectura acumulativa [8].

### Definición 6.4. Cadena realizable

Una cadena realizable es una cadena en el sentido de VII.3 que, además, satisface

D[1:m] ≠ ∅.

La condición anterior aporta el testigo común necesario para representar un recorrido efectivo:

x₀ ↦ x₁ ↦ ⋯ ↦ xₘ.

Una cadena realizable no constituye necesariamente un único suceso compuesto. Para que la cuaterna asociada al recorrido sea un suceso admisible debe satisfacer A1–A6; en particular, A4 exige que exista un observable compatible F y un estado inicial x₀ ∈ D[1:m] tales que

F[Hₘ](xₘ) − F[H₀](x₀) ≠ 0.

---

## 7. Aditividad sobre recorridos realizados

Sea una cadena realizable con

xₖ = Rₖ(xₖ₋₁)

y una familia de observables compatibles F[H₀], …, F[Hₘ] a lo largo del recorrido.

### Teorema 7.1. Identidad telescópica de la variación observable

F[Hₘ](xₘ) − F[H₀](x₀)
= Σₖ₌₁…ₘ [ F[Hₖ](xₖ) − F[Hₖ₋₁](xₖ₋₁) ].

Equivalentemente,

Δ[1:m] F(x₀) = Σₖ₌₁…ₘ Δₑₖ F(xₖ₋₁).

**Demostración.** Los términos intermedios se cancelan dos a dos. ∎

La identidad anterior corresponde al caso escalar de un recorrido realizado. Las formas más generales de acumulación definidas en VII.3 mantienen sus reglas propias de tipado y lectura [8].

---

## 8. Persistencia *append-only*, HNA y bifurcación

El teorema HNA se aplica a una misma trayectoria canónica *append-only* [13,14].

### Teorema 8.1. Persistencia de una posición clausurada

Sea

T = (S₀, ν₀, S₁, ν₁, …)

una trayectoria canónica *append-only*. Si una posición p queda clausurada en el paso j,

Sⱼ(p) = τ ∈ {0, 1},

entonces, para todo paso posterior de esa misma trayectoria,

Sₖ(p) = τ,    k > j.

Ningún paso posterior de esa trayectoria vuelve a asignar U a p.

La afirmación se refiere a la misma trayectoria canónica. Si cambia la trayectoria o el horizonte y la identificación de posiciones requiere transporte, la correspondencia debe establecerse en el régimen pertinente.

### 8.2. Bifurcación

Dos trayectorias pueden compartir un prefijo ya constituido y divergir después mediante datos de transición distintos [13]. La bifurcación conserva íntegro el prefijo común y genera trayectorias posteriores distintas sin modificar los registros anteriores.

---

## 9. Precedencia y cadenas estrictas de habilitación

VII.2 define comparabilidad, afectación y precedencia entre sucesos admisibles [7]. En una trayectoria efectiva, las relaciones establecidas por pares deben acompañarse de una realización conjunta.

### Definición 9.1. Número de posiciones con valor U

En una célula finita se define

u(S) = |{ i : Sᵢ = U }|.

### Teorema 9.2. Aciclicidad de las cadenas estrictas de habilitación por clausura de posiciones con valor U

Sea

S₀ —e₁→ S₁ —e₂→ ⋯ —eₘ→ Sₘ

una cadena realizable dentro de una misma trayectoria canónica *append-only*. Supóngase que cada paso habilita estrictamente al siguiente mediante la clausura de al menos una posición necesaria cuyo valor era U.

Entonces

u(Sₖ₊₁) < u(Sₖ)

para todo k, y la cadena no puede contener un ciclo.

**Demostración.** u(S) es un entero no negativo. Cada paso clausura al menos una posición cuyo valor era U. Por el Teorema 8.1 (HNA), ninguna posición ya clausurada puede recuperar el valor U dentro de esa misma trayectoria canónica. Por tanto, u(S) disminuye estrictamente en cada paso. Un ciclo exigiría recuperar un valor anterior de u, lo que es imposible. ∎

### Corolario 9.3. Cota finita

Si la célula tiene n posiciones,

m ≤ u(S₀) ≤ n.

En SV(9,3),

m ≤ 9.

---

## 10. Cambio de horizonte y recurrencia estructural

Si una reevaluación modifica el conjunto de posiciones, su identificación o la familia de observables, la continuidad entre horizontes no se presume [5,12]. VII.4 distingue persistencia, reevaluación y no herencia [9]; VII.5 formaliza el enlace tipado entre regímenes [10]; y VII.6 restringe la preservación, la invariancia y la equivalencia a los subdominios en los que se han establecido [11].

El transporte entre horizontes debe quedar declarado en el régimen correspondiente. Si no se declara un transporte, no se establece identidad entre posiciones pertenecientes a horizontes distintos.

La repetición de un mismo *frame* visible tampoco implica identidad de suceso. Los resultados sobre recurrencia estructural admiten configuraciones iguales asociadas a activaciones o evaluaciones distintas [15]:

S(a) = S(b)  ⇏  e(a) = e(b).

Esto es compatible con HNA: la persistencia impide que una posición clausurada recupere U dentro de una misma trayectoria canónica, pero no impide que recorridos estructuralmente distintos presenten la misma configuración visible.

---

## 11. Estructura de la dinámica del Suceso

Los resultados anteriores establecen las separaciones

frame  ≠  dato de transición  ≠  reevaluación  ≠  suceso admisible  ≠  cadena,

así como

R[1:m] definido  ⇏  e[1:m] admisible

y

componibilidad por pares  ⇏  realización conjunta.

La dinámica general se apoya en:

1. la base celular ternaria S ∈ Σⁿ;
2. la distinción entre tipo de suceso, valor ternario de instancia, dato de transición, *frame*, horizonte estructural, suceso admisible y operador de reevaluación;
3. el suceso admisible e = (H, H′, σ, Rₑ), sujeto a A1–A6;
4. la composición parcial de reevaluaciones sobre su dominio efectivo;
5. la comprobación independiente de la admisibilidad del compuesto;
6. las condiciones de cadena de VII.3 y la existencia de un testigo común cuando se afirma un recorrido efectivo;
7. la aditividad telescópica de observables compatibles sobre recorridos realizados;
8. HNA y la persistencia *append-only* dentro de una misma trayectoria canónica;
9. la bifurcación sin alteración retrospectiva;
10. el transporte declarado cuando cambia el horizonte.

Esta estructura no exige identidad global, composición total, monoide, grupo ni métrica general; tampoco toma el tiempo canónico como primitiva [5,12] ni la probabilidad como fundamento de la clausura [1–3].

---

## 12. Conclusión

La dinámica del Suceso distingue entre la ejecución de una reevaluación y la constitución de un suceso admisible. La composición funcional de los operadores es parcial y asociativa sobre su dominio efectivo; la cuaterna resultante sólo pertenece a la clase de sucesos admisibles cuando satisface A1–A6.

La distinción entre tramo realizable, cadena y suceso compuesto separa la componibilidad local de la existencia de un recorrido común. HNA preserva las posiciones clausuradas dentro de una trayectoria canónica *append-only*, y la bifurcación permite trayectorias posteriores distintas sin modificar el prefijo compartido. En las cadenas estrictas de habilitación mediante clausura de posiciones cuyo valor era U, la función u(S) excluye ciclos y proporciona una cota finita.

La U permanece única y no tipada. La igualdad entre *frames* no determina identidad de suceso. Los cambios de horizonte exigen el transporte que corresponda al régimen declarado, sin presuponer continuidad ni equivalencia global.

Con estas relaciones queda descrita la dinámica general del Suceso en el Sistema Vectorial SV.

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
