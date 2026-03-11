# Álgebra de composición intercelular del marco SV

## I. Transmisión en serie por parámetro puente

### Célula acoplable, parámetro puente, grafo dirigido y composición trazable

**Autor:** Juan Antonio Lloret Egea
**Versión:** 1
**Lugar y fecha:** Madrid, 11/03/2026
**Estado:** Documento doctrinal cerrado
**URL canónica:** https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv/release/4

---

## 1. Objeto y alcance

El presente documento es la primera pieza de una teoría de composición intercelular del Sistema Vectorial SV. Formaliza un patrón compositivo concreto — la transmisión en serie por parámetro puente — con grado alto de cierre. Su objeto no es sustituir ni reformular el aparato fundacional establecido en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV*, sino extenderlo con precisión en una dirección concreta: la transmisión formal de resultados entre células mediante el operador de sustitución σ_{k,φ}.

La tesis central del documento es la siguiente:

> El marco SV admite no solo células aisladas, sino también sistemas dirigidos de células acopladas, en los que la salida global tipada de una célula puede transportarse a una célula sucesora como parámetro puente, mediante una álgebra explícita de transmisión intercelular, sin pérdida de trazabilidad, sin duplicación de evaluación y sin cesión de soberanía normativa a sistemas opacos.

El alcance se delimita con rigor. Este documento formaliza lo que hoy puede sostenerse con definición y demostración, y abre como programa de investigación lo que aún no está cerrado. La distinción entre ambos planos se mantiene con disciplina a lo largo de todo el texto.

Quedan expresamente fuera de este documento: los demás patrones compositivos del marco SV (compuerta jerárquica, supervisión meta del sistema, composición multinivel, etc.), que serán objeto de otros documentos complementarios; la discusión de implementaciones concretas por lenguaje; la validación clínica de ningún dominio particular; la formalización completa de capas de supervisión meta; y toda forma de delegación de la decisión normativa en inteligencia artificial, estadística o minería de datos.

---

## 2. Relación con el corpus doctrinal vigente

### 2.1. Subordinación a los Fundamentos

Este documento es doctrina derivada de segundo nivel. La autoridad normativa suprema del Sistema Vectorial SV reside en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV* (Release 3). Todo lo que aquí se establece debe ser coherente con dicho documento. En caso de discrepancia, prevalecen los *Fundamentos*.

Los puntos de apoyo específicos en los *Fundamentos* son:

- §7.2: la célula composable como cuádruple Cᵢ = (vᵢ, Ωᵢ, κᵢ, ρᵢ).
- §7.3: la función de evaluación χᵢ : Cᵢ → Ωᵢ, factorizada a través del vector interno y del motor normativo.
- §7.4: la tesis central de que no existe una única operación binaria universal para toda composición.
- §7.5: la familia ℱ_SV = { max, min, ⊗_gate, σ_{k,φ}, ▷, Γ, Comp }.
- §7.8: el operador de sustitución σ_{k,φ} como forma de composición en serie.
- §7.10: la función de criticidad Γ como operador de enriquecimiento.
- §7.12: el principio de cierre, que establece que la gramática de composición puede ampliarse pero no reducirse indebidamente.
- §9: los invariantes constitutivos, en particular la primacía decisional humana y la exclusión de la probabilidad opaca.

### 2.2. Coherencia con la Guía práctica y la Declaración de Autoridad

La *Guía práctica del conocimiento profundo y la crítica de la razón pura* establece las reglas inamovibles del proyecto (R1–R9), la subordinación de la IA al marco, y la curva de adopción como parámetro real del sistema. La *Declaración de Autoridad Normativa Suprema* formaliza la jerarquía. Este documento no crea un nuevo soberano normativo; crea una nueva capa compositiva subordinada al marco existente.

### 2.3. Tabla de notación y estatutos

Para evitar colisiones entre la notación de los *Fundamentos* y la que este documento introduce, se fija la siguiente tabla de correspondencia. Los símbolos heredados no se modifican. Los símbolos nuevos se introducen como extensión subordinada.

**Símbolos heredados de los Fundamentos (axiomas, intocables):**

| Símbolo | Significado | Referencia |
|---------|------------|------------|
| Σ = {0, 1, U} | Alfabeto ternario | §2 |
| 𝒮ₙ = Σⁿ | Célula exacta | §3.1 |
| n = b², b ≥ 3 | Restricción arquitectónica | §3.1 |
| T(n) = ⌊7n/9⌋ | Umbral canónico | §5.2 |
| Cᵢ = (vᵢ, Ωᵢ, κᵢ, ρᵢ) | Célula composable canónica | §7.2 |
| χᵢ : Cᵢ → Ωᵢ | Función de evaluación | §7.3 |
| σ_{k,φ} | Operador de sustitución | §7.8 |
| ▷ | Supervisión meta / veto | §7.9 |
| Γ(v) = Nᵤ(v) − min(δ₀, δ₁) | Función de criticidad | §7.10 |

**Símbolos introducidos en este documento (definiciones, subordinadas):**

| Símbolo | Significado | Estatuto |
|---------|------------|----------|
| Kᵢ | Codominio tipado de clases globales (equivalente operativo de Ωᵢ) | Definición |
| Ĉᵢ = (Cᵢ, Bᵢ) | Célula acoplable (extensión compositiva) | Definición |
| Bᵢ ⊆ {1, …, nᵢ} | Conjunto de posiciones declaradas como parámetro puente | Definición |
| φⱼ→ᵢ⁽ᵏ⁾ : Kⱼ → Σ | Conector de transmisión | Definición |
| 𝒢 = (V, E, Φ) | Grafo de células acopladas | Definición |
| xᵢ⁽⁰⁾ | Estado base de la célula (antes de transmisión) | Definición |
| x̃ᵢ | Estado actualizado (tras transmisiones) | Definición |
| Cᵢ[x̃ᵢ] | Célula Cᵢ con vector actualizado x̃ᵢ | Definición |
| yᵢ = χᵢ(Cᵢ[x̃ᵢ]) | Evaluación final sobre célula con vector actualizado | Definición |
| ΔΓₖ(Cᵢ) | Criticidad condicionada al puente k | Proposición demostrada |
| Ψ_{i,k} : Σ × Σʳ → Σ | Operador de conflicto (solo régimen general) | Definición |

**Nota sobre Kᵢ y Ωᵢ.** Los *Fundamentos* (§7.2) definen Ωᵢ como codominio de salida de la célula composable. Este documento introduce Kᵢ como notación operativa para el mismo concepto, a fin de liberar la letra Ω de cualquier colisión con otros usos. La equivalencia es puramente notacional: Kᵢ ≡ Ωᵢ en sentido formal. No se modifica la semántica.

**Nota sobre χᵢ y la evaluación del vector actualizado.** Los *Fundamentos* (§7.3) definen χᵢ : Cᵢ → Ωᵢ como función de evaluación sobre la célula composable. En este documento, la transmisión produce un vector actualizado x̃ᵢ que difiere del vector original vᵢ. Para expresar la evaluación de la célula con ese vector actualizado sin romper el dominio de χᵢ, se emplea la notación Cᵢ[x̃ᵢ], que designa la célula Cᵢ con su vector interno sustituido por x̃ᵢ. La evaluación final se escribe entonces yᵢ = χᵢ(Cᵢ[x̃ᵢ]) ∈ Kᵢ. Esta mediación preserva la definición fundacional: χᵢ sigue evaluando la célula, no directamente un vector.

---

## 3. De la célula aislada a la célula acoplable

### 3.1. Límite de la célula aislada

Una célula SV exacta 𝒮ₙ = {0, 1, U}ⁿ con su motor normativo y su función de evaluación χ constituye una unidad completa de análisis. Recibe parámetros, los evalúa, produce una clasificación determinista y, cuando procede, enriquece la indeterminación mediante Γ.

Sin embargo, una arquitectura real rara vez se agota en una sola célula. Cuando dos o más células operan sobre aspectos distintos de una misma situación — por ejemplo, la adecuación de una profilaxis y el riesgo residual de un paciente — surge la necesidad de que el resultado de una célula informe a otra. Esa necesidad no puede resolverse duplicando parámetros ni fusionando células en una supercélula inmanejable. Exige una teoría formal de transmisión.

### 3.2. Qué significa acoplar células

Acoplar dos células no significa mezclarlas. Significa establecer un canal formal, tipado y trazable por el cual la salida de una célula entra en otra como dato, no como autoridad. La célula receptora conserva su estructura, sus parámetros locales, su motor normativo propio y su autonomía de evaluación. Lo que recibe es un valor ternario heredado — derivado de una evaluación externa — que actualiza una posición específica de su vector.

La diferencia con la fusión es decisiva. En una fusión, dos células se disuelven en una tercera mayor. En un acoplamiento, cada célula permanece intacta; lo que se añade es una conexión formal entre ellas.

### 3.3. Célula acoplable: extensión compositiva

La célula composable canónica queda definida en los *Fundamentos* (§7.2) como el cuádruple Cᵢ = (vᵢ, Ωᵢ, κᵢ, ρᵢ). Este documento no modifica esa definición. Lo que añade es una extensión compositiva que permite declarar qué posiciones del vector están destinadas a recibir transmisión externa.

**Definición 1.** La **célula acoplable** es el par

> Ĉᵢ = (Cᵢ, Bᵢ)

donde Cᵢ es la célula composable canónica y Bᵢ ⊆ {1, …, nᵢ} es el conjunto de posiciones declaradas como **parámetros puente**. Las posiciones que no pertenecen a Bᵢ son parámetros locales ordinarios.

La extensión es conservadora: si Bᵢ = ∅, la célula acoplable se reduce a la célula composable canónica y el sistema se comporta como si no hubiera transmisión. Toda célula composable es automáticamente acoplable con conjunto de puentes vacío.

---

## 4. Transmisión intercelular tipada

### 4.1. Salida global tipada

Toda célula composable Cᵢ posee una función de evaluación χᵢ : Cᵢ → Ωᵢ, donde Ωᵢ es el codominio de salida definido en los *Fundamentos* (§7.2). A efectos de la transmisión intercelular, este documento emplea la notación operativa Kᵢ para referirse al mismo conjunto.

Sea Kᵢ el conjunto tipado de clases globales admisibles de la célula Cᵢ. En las familias de módulos clínicos tratadas hasta ahora, Kᵢ = {APTO, NO_APTO, INDETERMINADO}. Otras familias de dominio podrían definir conjuntos de clases distintos, siempre que sean finitos, explícitos y semánticamente documentados.

La salida χᵢ(Cᵢ) ∈ Kᵢ es lo que este documento denomina **salida global tipada**. Es tipada porque pertenece a un conjunto finito, explícito y semánticamente definido. No es un número real, no es una probabilidad, no es una estimación: es una sentencia determinista del motor normativo.

### 4.2. Conector de transmisión

**Definición 2.** Sean Ĉⱼ y Ĉᵢ dos células acoplables. Sea k ∈ Bᵢ una posición declarada como parámetro puente en la célula receptora. Un **conector de transmisión** de Cⱼ a Cᵢ en la posición k es una aplicación

> φⱼ→ᵢ⁽ᵏ⁾ : Kⱼ → Σ

que transforma la salida global tipada de la célula transmisora en un valor ternario apto para ocupar la posición k del vector de la célula receptora.

El conector no es universal ni canónico por sí mismo. Su definición depende de la semántica formal del parámetro puente receptor y debe estar explícitamente documentada. El conector φ(APTO) = 0, φ(NO_APTO) = 1, φ(INDETERMINADO) = U es válido para casos donde la presencia de una condición favorable se codifica como 0 y su ausencia como 1, pero no debe elevarse a ley general del marco. Otros parámetros con polaridad distinta podrían requerir conectores distintos.

### 4.3. Tríada del flujo de evaluación

Para formalizar con nitidez la separación entre transmisión y evaluación, se introduce la siguiente tríada:

**Estado base.** El estado local de la célula Cᵢ antes de recibir ninguna transmisión es

> xᵢ⁽⁰⁾ ∈ Σⁿⁱ

Este estado refleja únicamente la configuración local de parámetros del dominio propio de la célula, antes de recibir transmisión.

**Estado actualizado.** Tras aplicar las transmisiones entrantes (y, en el régimen general, resolver conflictos), se obtiene

> x̃ᵢ ∈ Σⁿⁱ

El estado actualizado difiere del estado base solo en las posiciones correspondientes a parámetros puente que hayan recibido transmisión.

**Evaluación final.** La célula se evalúa sobre su estado actualizado:

> yᵢ = χᵢ(Cᵢ[x̃ᵢ]) ∈ Kᵢ

Esta separación garantiza tres propiedades: la transmisión intercelular es una fase distinta de la evaluación intrínseca; la evaluación local sigue siendo exacta y determinista; y la trazabilidad del proceso puede reconstruirse paso a paso.

### 4.4. Operación de transmisión

**Definición 3.** La **transmisión intercelular** de Cⱼ a Cᵢ en la posición k mediante el conector φⱼ→ᵢ⁽ᵏ⁾ es la operación que produce el estado actualizado x̃ᵢ a partir del estado base xᵢ⁽⁰⁾ sustituyendo su componente k-ésima:

> x̃ᵢ[k] = φⱼ→ᵢ⁽ᵏ⁾( χⱼ(Cⱼ) )
> x̃ᵢ[l] = xᵢ⁽⁰⁾[l]  para todo l ≠ k

Esta operación es una instancia del operador de sustitución σ_{k,φ} definido en los *Fundamentos* (§7.8). La presente formalización no crea un operador nuevo; concreta y extiende uno ya existente. La definición anterior describe una transmisión elemental (una sola arista del grafo). Los estados actualizados con múltiples transmisiones se obtienen por iteración de esta operación en régimen simple, o por sustitución acompañada de Ψ_{i,k} en régimen general cuando exista concurrencia sobre un mismo puente.

---

## 5. Parámetro puente

### 5.1. Definición

**Definición 4.** Sea Ĉᵢ = (Cᵢ, Bᵢ) una célula acoplable y k ∈ Bᵢ. El parámetro Pₖ de Cᵢ se denomina **parámetro puente**. Su valor en el estado actualizado no proviene de una evaluación local del dominio de Cᵢ, sino de la salida global tipada de una célula transmisora transformada por un conector φ.

La distinción entre parámetros locales y parámetros puente es estructural, no accidental. Debe quedar declarada en la especificación de la célula acoplable antes de que se ejecute ninguna transmisión.

### 5.2. Comportamiento ante indeterminación de la transmisora

**Proposición 1 — Coherencia epistémica de la transmisión.** Si la célula transmisora Cⱼ produce una salida χⱼ(Cⱼ) = INDETERMINADO y el conector φ traduce INDETERMINADO a U, entonces el parámetro puente queda en estado U. Esto es coherente con la semántica epistémica de U en el marco SV: el sistema no finge saber lo que la célula transmisora no ha podido determinar.

**Consecuencia para Γ.** El valor U en el parámetro puente entra en el cómputo de la función de criticidad Γ de la célula receptora exactamente igual que cualquier otro U local. Esto permite que Γ cuantifique el impacto de la indeterminación propagada con la misma herramienta que cuantifica la indeterminación propia. Las causas del U son distintas (local o heredado); el tratamiento algebraico es idéntico. Esta es una consecuencia directa del estatuto epistémico de U definido en los *Fundamentos* (§6): U no distingue causas, solo registra el estado de no determinación actual.

---

## 6. Grafo de células y condiciones de buena formación

### 6.1. Definición del grafo

**Definición 5.** Un **sistema de células acopladas** del Sistema Vectorial SV se representa como un grafo dirigido

> 𝒢 = (V, E, Φ)

donde:

- V = {Ĉ₁, Ĉ₂, …, Ĉₘ} es un conjunto finito de células acoplables.
- E ⊆ V × V × ℕ es un conjunto de aristas dirigidas, donde cada arista e = (Ĉⱼ, Ĉᵢ, k) indica que la célula Cⱼ transmite su salida global al parámetro k de la célula Cᵢ, con k ∈ Bᵢ.
- Φ = {φₑ}ₑ∈E es la familia de conectores, uno por cada arista, con φₑ : Kⱼ → Σ.

### 6.2. Dos regímenes de buena formación

Este documento define dos regímenes de buena formación, con condiciones progresivas. El régimen simple es estrictamente más restrictivo que el general; todo sistema bien formado en régimen simple lo es también en régimen general, pero no a la inversa.

#### Régimen simple (RS)

Un grafo 𝒢 está **bien formado en régimen simple** si satisface las siguientes condiciones:

**RS1 — Unicidad de destino.** Para cada par (Ĉᵢ, k), existe a lo sumo una arista en E con destino (·, Ĉᵢ, k). Es decir, cada parámetro puente recibe a lo sumo una transmisión.

**RS2 — Compatibilidad de codominio.** Para cada arista (Ĉⱼ, Ĉᵢ, k), el conector φₑ está definido sobre Kⱼ y produce valores en Σ.

**RS3 — Aciclicidad.** Existe un orden topológico de V tal que toda célula se evalúa después de todas las células de las que recibe transmisión. Esto equivale a exigir que 𝒢, proyectado sobre V, sea un grafo dirigido acíclico (DAG).

**RS4 — Completitud local.** Toda célula Cᵢ ∈ V posee su propio motor normativo, su propio umbral T(nᵢ) y su propia función de evaluación χᵢ, independientemente de las transmisiones que reciba.

El régimen simple es el implementado y verificado en el repositorio del proyecto. Es la clase más restringida de sistemas bien formados y la que admite las proposiciones más fuertes.

#### Régimen general (RG)

Un grafo 𝒢 está **bien formado en régimen general** si satisface las condiciones RS2, RS3 y RS4, y además:

**RG1 — Resolución de concurrencia.** Si para un par (Ĉᵢ, k) existen varias aristas en E con destino (·, Ĉᵢ, k), el grafo debe incluir un operador de conflicto Ψ_{i,k} y una regla formal de prioridad. En ausencia de ambos, el sistema no se considera bien formado.

El régimen general relaja la condición RS1 (unicidad de destino) pero exige en su lugar un mecanismo formal de resolución. La sección 8 de este documento define las familias de operadores de conflicto actualmente identificadas.

### 6.3. Profundidad del sistema

**Definición 6.** La **profundidad** de un grafo de células 𝒢 es la longitud del camino dirigido más largo en 𝒢. Un sistema de profundidad 0 no tiene transmisiones. Un sistema de profundidad 1 tiene transmisiones directas sin cadena. Un sistema de profundidad d > 1 tiene cadenas de transmisión de al menos d eslabones.

La profundidad importa porque cada eslabón de la cadena propaga, potencialmente, un U. En una cadena de profundidad d, la indeterminación de la primera célula puede propagarse a todas las siguientes. La función Γ cuantifica este efecto en cada eslabón, pero la acumulación a lo largo de la cadena es un fenómeno que merece atención formal y que este documento deja abierto como línea de investigación.

---

## 7. Topologías permitidas

Este documento estudia cuatro topologías de acoplamiento. Las tres primeras son casos particulares de la cuarta, que las engloba.

### 7.1. Cadena serial

La cadena serial es una secuencia de células en la que cada una transmite su salida a la siguiente:

> C₁ → C₂ → C₃ → … → Cₘ

Formalmente, E = {(Ĉⱼ, Ĉⱼ₊₁, kⱼ) : j = 1, …, m−1} donde kⱼ es el parámetro puente de Ĉⱼ₊₁ que recibe la salida de Cⱼ.

La cadena serial tiene profundidad m−1, satisface RS1 de forma trivial (cada puente recibe una sola transmisión) y su orden topológico coincide con el orden de la cadena. Es la topología del caso interno del proyecto.

### 7.2. Herencia selectiva

En la herencia selectiva, una célula Ĉᵢ recibe transmisión de una o varias células predecesoras, cada una a un parámetro puente distinto:

> Ĉ₁ → Ĉ₄ (al parámetro k₁)
> Ĉ₂ → Ĉ₄ (al parámetro k₂)
> Ĉ₃ (sin transmisión a Ĉ₄)

con k₁ ≠ k₂. En régimen simple, cada parámetro puente sigue recibiendo una sola transmisión (RS1 se cumple). La herencia selectiva se caracteriza porque existen células que podrían transmitir pero no lo hacen: el diseñador del sistema elige qué conexiones son semánticamente relevantes.

### 7.3. Fusión paralela

En la fusión paralela, dos o más células que se evalúan de forma independiente transmiten cada una a una célula integradora:

> Ĉ₁ → Ĉₘ (al parámetro k₁)
> Ĉ₂ → Ĉₘ (al parámetro k₂)
> …
> Ĉᵣ → Ĉₘ (al parámetro kᵣ)

con k₁, k₂, …, kᵣ todos distintos (en régimen simple). La fusión paralela tiene profundidad 1 y es la forma natural de integrar evaluaciones de dominios independientes. A diferencia de la dominancia homogénea (max/min definida en los *Fundamentos* §7.6), aquí no se comparan salidas sobre una escala ordinal común: cada salida se inyecta como parámetro puente distinto en una célula que posee su propia lógica de evaluación.

### 7.4. DAG general

Las tres topologías anteriores son casos particulares de un grafo dirigido acíclico general. El DAG permite combinaciones arbitrarias de cadenas, herencias selectivas y fusiones, siempre que se mantenga la aciclicidad exigida por RS3 y heredada también por el régimen general.

**Sobre los ciclos.** Este documento no admite ciclos en el grafo de células. Un ciclo implicaría que la evaluación de una célula depende, directa o indirectamente, de su propia salida, lo que destruiría la determinación del sistema. La investigación futura podrá explorar formulaciones con retroalimentación temporal, pero esa extensión requiere una teoría de estados que este documento no aborda.

---

## 8. Conflicto y prioridad

### 8.1. Planteamiento del problema

En el régimen simple, cada parámetro puente recibe a lo sumo una transmisión y el problema de conflicto no se presenta. En el régimen general, si varias transmisiones concurren sobre el mismo parámetro puente k de una célula Ĉᵢ, se necesita un mecanismo formal de resolución.

Este documento no impone una ley universal de resolución. Impone un requisito: si hay concurrencia, el operador de conflicto y la regla de prioridad deben existir, estar formalmente declarados y ser deterministas. En ausencia de cualquiera de los tres, el sistema no se considera bien formado.

### 8.2. Operador de conflicto

**Definición 7.** Sea k ∈ Bᵢ un parámetro puente de la célula Ĉᵢ que recibe transmisiones de r células distintas. Sea a₀ = xᵢ⁽⁰⁾[k] el valor local del parámetro antes de la transmisión, y sean a₁, …, aᵣ los valores propuestos por las r transmisiones concurrentes. El **operador de conflicto** es una aplicación

> Ψ_{i,k} : Σ × Σʳ → Σ

que determina el valor final del parámetro k en el estado actualizado:

> x̃ᵢ[k] = Ψ_{i,k}(a₀, a₁, …, aᵣ)

El operador Ψ recibe el valor local como primer argumento distinto para que el diseñador pueda establecer políticas de prioridad entre lo local y lo heredado.

### 8.3. Tres familias iniciales de operadores

Este documento identifica tres familias de operadores de conflicto. No prescribe cuál debe adoptarse en general: la elección depende del dominio, de la arquitectura y de la decisión documentada del diseñador humano.

**a) Consenso conservador.** El desacuerdo no puede producir falsa certeza:

> Ψ^cons(a₀, a₁, …, aᵣ) = a₁ si a₁ = a₂ = … = aᵣ; U en cualquier otra situación.

Bajo este operador, la discrepancia colapsa en U. Es la familia más prudente y la más coherente con el estatuto epistémico de U en el marco SV: si las fuentes no coinciden, el sistema reconoce que no sabe. En Ψ^cons, el valor local a₀ no participa en el consenso; el operador resuelve únicamente la concurrencia entre señales heredadas (a₁, …, aᵣ). La relación entre el valor local y las señales heredadas queda remitida al régimen de prioridad adoptado o a la familia Ψ^loc.

**b) Precedencia declarada.** Sea π un orden total sobre las señales entrantes:

> Ψ^π(a₀, a₁, …, aᵣ) = a_{j*}

donde a_{j*} es la señal con prioridad máxima según π. El orden π debe estar formalmente declarado antes de la ejecución del sistema, no aprendido ni inferido.

**c) Soberanía local condicionada.** El valor local solo cede si está en estado indeterminado:

> Ψ^loc(a₀, a₁, …, aᵣ) = a₀ si a₀ ∈ {0, 1}; Ψ^cons(U, a₁, …, aᵣ) si a₀ = U.

Este operador protege la autonomía local: un valor ya determinado localmente no puede ser derogado por transmisiones externas. Solo cuando el valor local es U se consultan las señales heredadas, y aun entonces se aplica el criterio conservador.

### 8.4. Regímenes de prioridad

Además de la resolución puntual por operador, el diseñador del sistema debe documentar el régimen de prioridad aplicable:

**Prioridad local.** Lo heredado no puede derogar lo ya determinado localmente, salvo declaración expresa. Es el régimen implícito del operador Ψ^loc.

**Prioridad heredada.** Determinadas transmisiones tienen supremacía formal sobre ciertos parámetros del receptor. El diseñador debe documentar qué aristas y qué parámetros operan bajo esta prioridad.

**Prioridad condicionada por tipo.** La prioridad depende del tipo de parámetro puente y del rol estructural de la célula emisora. Es la forma más flexible pero también la que exige más documentación.

Este documento plantea el problema y clasifica las soluciones. No impone una ley universal de prioridad. La elección pertenece al diseñador del sistema y debe quedar registrada como parte de la especificación del grafo.

---

## 9. Propiedades formales de la transmisión

### 9.1. Proposición 2 — Preservación de la dimensión

La transmisión intercelular no altera la dimensión de la célula receptora. Si Cᵢ es una célula SV(nᵢ, bᵢ), después de la transmisión sigue siendo SV(nᵢ, bᵢ). Solo cambia el valor de una o varias componentes de su vector.

**Demostración.** La operación sustituye xᵢ⁽⁰⁾[k] por un elemento de Σ, que es el mismo conjunto del que proviene xᵢ⁽⁰⁾[k] por definición. La longitud del vector no cambia. El espacio 𝒮ₙᵢ = Σⁿⁱ es el mismo antes y después. ∎

### 9.2. Proposición 3 — Preservación de la clasificación determinista

La transmisión no altera la regla de clasificación de la célula receptora. Después de la sustitución, la célula receptora se clasifica con el mismo umbral T(nᵢ) = ⌊7nᵢ/9⌋ y las mismas reglas de conteo.

**Demostración.** La regla de clasificación depende de los conteos N₀, N₁ y Nᵤ sobre el vector completo y del umbral T(nᵢ). La sustitución de una o varias componentes modifica esos conteos pero la regla misma no cambia. ∎

### 9.3. Proposición 4 — No reentrada en la evaluación emisora

La transmisión no reabre ni modifica la evaluación de la célula transmisora. Sea Yⱼ = χⱼ(Cⱼ) la salida global de Cⱼ calculada antes de la transmisión. Después de la transmisión, Yⱼ permanece inalterada. La célula receptora utiliza φ(Yⱼ), no recalcula χⱼ.

**Demostración.** La operación de transmisión toma Yⱼ como dato de entrada de φ. No invoca χⱼ ni accede al vector vⱼ. La evaluación de Cⱼ es un hecho consumado antes de que la transmisión se ejecute. ∎

### 9.4. Proposición 5 — Clausura ternaria

Si todas las transmisiones son formalmente válidas y todos los conectores φ toman valores en Σ, entonces todo estado actualizado x̃ᵢ pertenece a Σⁿⁱ.

**Demostración.** Cada componente de x̃ᵢ es o bien el valor original xᵢ⁽⁰⁾[l] ∈ Σ (si l no es puente o no recibe transmisión), o bien φₑ(Yⱼ) ∈ Σ (por definición del conector). En ambos casos, la componente pertenece a Σ. ∎

### 9.5. Proposición 6 — Evaluación global determinista (régimen simple)

Si 𝒢 = (V, E, Φ) es un grafo bien formado en régimen simple (satisface RS1–RS4), entonces existe un procedimiento determinista que evalúa todas las células del sistema y produce, para cada una, una clasificación en Kᵢ.

**Demostración.** Por RS3, existe un orden topológico τ = (Ĉ_π(1), Ĉ_π(2), …, Ĉ_π(m)) tal que si (Ĉⱼ, Ĉᵢ, k) ∈ E, entonces Ĉⱼ precede a Ĉᵢ en τ. Se evalúan las células en ese orden. Cuando se evalúa Ĉ_π(r), todas las células que le transmiten ya han sido evaluadas y su salida global está determinada. Por RS4, Ĉ_π(r) posee motor propio. Por RS1, cada parámetro puente tiene valor único (una sola transmisión). Luego el estado actualizado x̃_π(r) está determinado. Luego la evaluación y_π(r) = χ_π(r)(C_π(r)[x̃_π(r)]) es determinista. Por inducción sobre r, la evaluación de todo el sistema es determinista. ∎

### 9.6. Proposición 7 — Evaluación global determinista (régimen general)

Si 𝒢 = (V, E, Φ) es un grafo bien formado en régimen general (satisface RS2, RS3, RS4 y RG1), y todos los operadores de conflicto Ψ_{i,k} son deterministas, entonces existe un procedimiento determinista que evalúa todas las células del sistema.

**Demostración.** Análoga a la de la Proposición 6. La diferencia es que, en los parámetros puente con concurrencia, el valor de x̃ᵢ[k] se determina por Ψ_{i,k} en lugar de por una transmisión única. Si Ψ_{i,k} es determinista y todas sus entradas están disponibles (por el orden topológico), el resultado es determinista. ∎

### 9.7. Proposición 8 — Conservadurismo del consenso

Bajo el operador Ψ^cons, ningún desacuerdo puede aumentar la certeza; solo puede preservarla o llevarla a U.

**Demostración.** Por definición, Ψ^cons produce un valor distinto de U solo si todas las señales entrantes coinciden. En caso de discrepancia, el resultado es U. Por tanto, si al menos una señal difiere de las demás, el resultado no es 0 ni 1: es U. La certeza nunca se fabrica a partir de la discrepancia. ∎

---

## 10. Criticidad de la indeterminación en composición

### 10.1. Γ en presencia de parámetros puente

La función de criticidad Γ(v) = Nᵤ(v) − min(δ₀(v), δ₁(v)), definida en los *Fundamentos* (§7.10), se aplica a la célula receptora sobre su estado actualizado x̃ᵢ sin modificación alguna. El valor U en un parámetro puente entra en el conteo de Nᵤ exactamente igual que un U local.

La interpretación del U propagado es distinta de la del U local: un U local indica que falta información sobre el parámetro evaluado; un U en parámetro puente indica que la célula transmisora no pudo determinar su resultado. Las causas son distintas; el tratamiento algebraico es idéntico.

### 10.2. Criticidad condicionada al puente

**Definición 8.** Sea Ĉᵢ una célula receptora con un parámetro puente en la posición k que recibe transmisión de Cⱼ. Si χⱼ(Cⱼ) = INDETERMINADO (y el conector traduce esto a U), puede definirse la **criticidad condicionada al puente** como:

> ΔΓₖ(Cᵢ) = | Γ(x̃ᵢ | x̃ᵢ[k] ← 0) − Γ(x̃ᵢ | x̃ᵢ[k] ← 1) |

Esta cantidad mide cuánto cambia la criticidad de la célula receptora en función de cómo se resuelva la célula transmisora. Si ΔΓₖ es grande, conviene resolver la célula transmisora antes de abordar las indeterminaciones locales de la receptora. Si ΔΓₖ = 0, la resolución de la transmisora no afecta a la criticidad de la receptora.

### 10.3. Proposición 9 — Acotación de ΔΓₖ

Para cualquier célula Cᵢ y cualquier parámetro puente k cuyo valor actual es U, se cumple:

> ΔΓₖ(Cᵢ) ∈ {0, 1}

**Demostración.** Sea v el estado actualizado x̃ᵢ con v[k] = U. Sean m = Nᵤ(v), n₀ = N₀(v), n₁ = N₁(v), y T = T(nᵢ). Definimos δ₀ = T − n₀ y δ₁ = T − n₁.

Considérese la sustitución v|_{k←0}: el conteo queda m' = m − 1, n₀' = n₀ + 1, n₁' = n₁. Luego δ₀' = δ₀ − 1, δ₁' = δ₁, y Γ(v|_{k←0}) = (m − 1) − min(δ₀ − 1, δ₁).

Considérese la sustitución v|_{k←1}: el conteo queda m'' = m − 1, n₀'' = n₀, n₁'' = n₁ + 1. Luego δ₀'' = δ₀, δ₁'' = δ₁ − 1, y Γ(v|_{k←1}) = (m − 1) − min(δ₀, δ₁ − 1).

La diferencia es:

> ΔΓₖ = | min(δ₀, δ₁ − 1) − min(δ₀ − 1, δ₁) |

Se analizan tres casos exhaustivos:

**Caso 1: δ₀ < δ₁.** Entonces min(δ₀, δ₁ − 1) = δ₀ (pues δ₀ < δ₁ implica δ₀ ≤ δ₁ − 1) y min(δ₀ − 1, δ₁) = δ₀ − 1. Luego ΔΓₖ = |δ₀ − (δ₀ − 1)| = 1.

**Caso 2: δ₀ > δ₁.** Entonces min(δ₀, δ₁ − 1) = δ₁ − 1 y min(δ₀ − 1, δ₁) = δ₁. Luego ΔΓₖ = |(δ₁ − 1) − δ₁| = 1.

**Caso 3: δ₀ = δ₁.** Entonces min(δ₀, δ₁ − 1) = δ₁ − 1 = δ₀ − 1 y min(δ₀ − 1, δ₁) = δ₀ − 1 = δ₁ − 1. Luego ΔΓₖ = 0.

En todos los casos, ΔΓₖ ∈ {0, 1}. ∎

**Consecuencia.** La resolución de una sola célula transmisora nunca puede alterar drásticamente la criticidad de la receptora. Si la receptora tiene muchas U propias, la contribución del puente es relativamente menor. Si la receptora está en situación fronteriza (δ₀ = δ₁), la resolución del puente no cambia la criticidad en absoluto. Este resultado refuerza la autonomía local: el puente informa, no domina.

---

## 11. Principios doctrinales de la transmisión intercelular

Los principios siguientes se derivan de los invariantes constitutivos del marco SV (§9 de los *Fundamentos*) y de las propiedades formales demostradas en las secciones anteriores.

**P1 — Transmisión tipada.** Solo se transmite una salida global formalmente tipada (elemento de Kⱼ), nunca un valor numérico opaco, una probabilidad ni un resultado parcial no formalizado. La transmisión es discreta, finita y semánticamente definida.

**P2 — Parámetro puente explícito.** Toda transmisión debe entrar en un parámetro puente nominalmente declarado en el conjunto Bᵢ de la célula receptora. Los parámetros no declarados como puente no pueden recibir transmisión.

**P3 — No duplicación.** La célula receptora no recuenta, repite ni reabre la evaluación interna de la célula transmisora. Utiliza su salida como dato consumado. La Proposición 4 garantiza esta propiedad.

**P4 — Autonomía local.** La célula receptora conserva su estructura (nᵢ, bᵢ), su motor normativo, su umbral T(nᵢ) y su función de evaluación χᵢ. La transmisión modifica el valor de una o varias componentes de su vector, no su arquitectura. Las Proposiciones 2 y 3 garantizan esta propiedad.

**P5 — Trazabilidad.** Toda transmisión debe poder responder a tres preguntas: ¿de qué célula proviene?, ¿con qué conector se tradujo?, ¿a qué parámetro de la receptora afectó? Esto es una extensión directa de la trazabilidad de U exigida en los *Fundamentos* (§6.4).

**P6 — Composición exacta.** La resolución de todo sistema de células acopladas se rige por álgebra explícita. Las Proposiciones 6 y 7 demuestran que, dado un grafo bien formado en cualquiera de los dos regímenes, la evaluación global es determinista. No interviene ningún mecanismo probabilístico, heurístico ni opaco.

**P7 — Soberanía humana.** La inteligencia artificial puede asistir en la exploración de topologías, la visualización de grafos, la verificación de conformidad y la estimación de Γ en espacios grandes. No puede decidir qué conectores se definen, qué topologías se permiten, qué operador de conflicto se adopta ni qué prioridad tiene una señal heredada sobre una local. Esas decisiones pertenecen al diseñador humano del sistema y deben quedar documentadas.

---

## 12. Caso interno del proyecto: inmunología

### 12.1. Composición IMMUNO-1 → IMMUNO-2

El repositorio SVperitus-dataset contiene una instancia verificada que opera en régimen simple:

- **Célula transmisora:** IMMUNO-1, SV(25,5), T(25) = 19. Evalúa la profilaxis antiinfecciosa.
- **Célula receptora:** IMMUNO-2, SV(25,5), T(25) = 19. Evalúa el riesgo infeccioso en inmunosupresión farmacológica.
- **Parámetro puente:** P25 de IMMUNO-2 (k = 25, con B₂ = {25}).
- **Conector:** φ(APTO) = 0, φ(NO_APTO) = 1, φ(INDETERMINADO) = U. Este conector es coherente con la semántica del parámetro receptor, donde 0 indica profilaxis adecuada y 1 indica profilaxis inadecuada o ausente.

El grafo es 𝒢 = ({IMMUNO-1, IMMUNO-2}, {(IMMUNO-1, IMMUNO-2, 25)}, {φ}). Se emplean aquí las denominaciones abreviadas IMMUNO-1 e IMMUNO-2 en lugar de la notación formal Ĉ₁, Ĉ₂ para facilitar la lectura del caso concreto. Es un DAG de profundidad 1. Satisface RS1–RS4. La Proposición 6 garantiza la evaluación determinista.

Esta composición constituye un caso interno en desarrollo que muestra la viabilidad del patrón compositivo. No constituye una clausura clínica definitiva del módulo de riesgo infeccioso. La especificación de IMMUNO-2 está en estado de borrador. La formalización de este documento es independiente de esa validación: describe qué ocurre mecánicamente cuando se acoplan dos células, no si la decisión de acoplarlas es clínicamente correcta.

### 12.2. Compatibilidad con supervisión meta

El sistema de células acopladas descrito en este documento es compatible con capas de supervisión meta ya definidas en el corpus doctrinal (operador ▷ de los *Fundamentos* §7.9). La supervisión meta no utiliza el mecanismo de transmisión por parámetro puente: emite un veredicto de integridad que habilita, anula o condiciona los resultados de las células de dominio. Su formalización completa pertenece a otro documento.

### 12.3. Enriquecimiento por Γ

Cuando IMMUNO-1 produce INDETERMINADO, el parámetro P25 de IMMUNO-2 recibe U. La función Γ se calcula sobre el estado actualizado de IMMUNO-2. La criticidad condicionada ΔΓ₂₅ cuantifica si conviene resolver IMMUNO-1 antes de abordar las U propias de IMMUNO-2. Por la Proposición 9, ΔΓ₂₅ ∈ {0, 1}.

---

## 13. Límites actuales del modelo

Este documento se compromete a documentar con honestidad lo que aún no puede cerrar.

**L1 — Elección del operador de conflicto.** Se han identificado tres familias de operadores (§8.3), pero este documento no prescribe cuál debe adoptarse en general. La elección es problema abierto subordinado al dominio y a la decisión del diseñador humano.

**L2 — Prioridad local versus heredada.** Se han clasificado tres regímenes de prioridad (§8.4), pero no se ha establecido una regla universal. Algebraicamente, un U heredado tiene el mismo peso que un U local (el conteo no distingue origen). Semánticamente, puede que no. La extensión a pesos diferenciados por origen del valor es compatible con la formalización presente, pero no se desarrolla aquí.

**L3 — Profundidad y degradación.** En cadenas largas (profundidad d >> 1), la propagación de U puede reducir la capacidad discriminante de las células posteriores. Este documento no define un umbral máximo de profundidad ni una métrica formal de degradación. La definición de esa métrica dentro de la gramática SV es línea de investigación abierta.

**L4 — Ciclos.** Se prohíben. La formalización de retroalimentación temporal — donde la salida de una célula en el instante t alimenta a otra en el instante t+1 — es una extensión natural pero requiere una teoría de estados que este documento no aborda.

**L5 — Validación empírica.** El caso IMMUNO-1 → IMMUNO-2 es un caso interno en desarrollo. La composición funciona algebraicamente y está verificada por implementación, pero la validación clínica de la dependencia entre profilaxis y riesgo infeccioso no está resuelta. La formalización de este documento es independiente de esa validación.

---

## 14. Líneas futuras

### 14.1. Teoría formal de conflicto

Formalizar las propiedades axiomáticas que todo operador Ψ debe satisfacer. Estudiar si existen otras familias además de las tres identificadas. Determinar si alguna familia es universalmente preferible o si la elección es siempre dependiente del dominio.

### 14.2. Pesos por origen

Extensión de Γ para distinguir entre U locales y U propagados. Formalmente viable; requiere redefinición de μ como función de dos argumentos (margen local y margen heredado). Los pesos deben ser explícitos, normativos y declarados, jamás aprendidos.

### 14.3. Composición temporal

Secuencias de evaluaciones del mismo sistema en instantes distintos. El grafo permanece fijo; los vectores cambian. Puede modelarse como una familia {𝒢ₜ}_{t∈T} con el mismo grafo y distintas evaluaciones.

### 14.4. Reticulado de células

Cuando el número de células crece, la estructura del conjunto V puede admitir un orden parcial natural que refleje relaciones de subordinación, especialización o generalización entre dominios. Este reticulado no está definido en el presente documento.

### 14.5. Escalabilidad computacional

Para sistemas con muchas células y transmisiones densas, la evaluación secuencial sigue siendo exacta pero puede requerir optimización. La inteligencia artificial puede asistir en la planificación del orden de evaluación (cuando hay múltiples órdenes topológicos válidos), pero no en la evaluación misma.

---

## 15. Alcance de este documento y gramática general de composición

La transmisión en serie por parámetro puente constituye el primer patrón compositivo del marco SV formalizado en este documento con grado alto de cierre. Los *Fundamentos* contemplan una familia más amplia de operadores compositivos, entre los que se incluyen compuerta jerárquica, supervisión meta y composición multinivel, etc. Algunos de esos patrones ya aparecen en dominios internos del proyecto, pero su formalización con el mismo nivel de rigor que la serie no se desarrolla aquí.

La gramática general de composición intercelular, incluida la determinación previa de la relación semántica entre células como condición de licitud operatoria, será objeto de desarrollos complementarios sucesivos. El siguiente se centrará en la **Gramática general de composición**, mientras que otras extensiones del marco podrán abordar, en piezas posteriores, planos adicionales de estructuración, dinámica o evolución del sistema.

---

## 16. Conclusión doctrinal

El Sistema Vectorial SV, tras este desarrollo, queda formalmente extendido desde la célula aislada hasta el sistema de células acopladas por transmisión en serie. La extensión no modifica los invariantes constitutivos del marco. Lo que se añade es una capa compositiva que permite a las células transmitirse resultados tipados entre sí a través de parámetros puente, bajo un grafo dirigido acíclico con conectores explícitos.

La formalización distingue dos regímenes de buena formación. El régimen simple admite las proposiciones más fuertes y es el implementado en el proyecto. El régimen general exige un operador de conflicto y una regla de prioridad formalmente declarados.

Las nueve proposiciones demostradas en este documento garantizan que la transmisión preserva la dimensión, la clasificación determinista, la no reentrada en la evaluación emisora, la clausura ternaria, la existencia de evaluación global determinista en ambos regímenes, el conservadurismo del consenso y la acotación de la criticidad condicionada. Los siete principios doctrinales formalizan las reglas que todo sistema acoplado por serie debe respetar.

Este documento es la primera pieza de una teoría compositiva más amplia. La composición en serie es uno de varios patrones lícitos del marco SV. Los demás patrones quedan reservados al documento complementario correspondiente.

El conjunto resultante para el patrón seriado — la célula SV que transmite, la célula SV que recibe, el conector que traduce, el grafo que organiza y el operador de conflicto que resuelve — es más expresivo que cualquier célula individual. Su resolución se rige por composición algebraica exacta. No interviene la estadística. No interviene la minería de datos. No interviene la inteligencia artificial como autoridad. El ser humano diseña la topología, define los conectores, establece las prioridades, elige los operadores de conflicto y gobierna el sistema. El álgebra garantiza que sus decisiones se ejecutan de forma determinista, trazable y auditable.

Ésa es la extensión que este documento fija. Lo que la humanidad haga con ella es, como siempre, su responsabilidad.

---

## Referencias

[R1] Juan Antonio Lloret Egea. *Fundamentos algebraico-semánticos del Sistema Vectorial SV.* v1.0.0, Release 3. ITVIA, 2026.
https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

[R2] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

[R3] Juan Antonio Lloret Egea. *Compilador doctrinal y célula meta SV(9,3)-IA.* Release 5. ITVIA, 2026.
https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/5

[R4] Juan Antonio Lloret Egea. *SVperitus–IMMUNO-1: módulo demostrador de profilaxis infecciosa y vacunación.* Release 5. ITVIA, 2026.
https://www.itvia.online/pub/de-svcustos-el-marco-de-intrusion-hasta-svperitus-immuno-1--profilaxis-infecciosa-y-vacunacion--sv255/release/5

---

*Documento doctrinal del proyecto SVperitus. ISSN 2695-6411.*
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
