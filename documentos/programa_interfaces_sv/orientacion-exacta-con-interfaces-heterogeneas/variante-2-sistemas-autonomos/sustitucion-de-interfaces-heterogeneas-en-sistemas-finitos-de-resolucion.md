
# Sustitución de interfaces heterogéneas en sistemas finitos de resolución: constitución del episodio y preservación exacta de los perfiles de terminales alcanzables

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0). Esta licencia se aplica exclusivamente a esta versión | Madrid, 13/08/2026

***PREPRINT*** **- NO REVISADO POR PARES**

## Resumen

Los sistemas finitos pueden recibir información pertinente para la resolución a través de realizaciones heterogéneas de interfaz. La admisibilidad local de las salidas individuales de una interfaz no garantiza que los testigos disponibles constituyan conjuntamente una instancia del problema de resolución declarado; además, sustituir una realización por otra puede alterar el comportamiento global incluso cuando la sustitución parezca localmente compatible. Estudiamos ambas cuestiones para mecanismos finitos de resolución con guardas. Un contrato de resolución especifica los papeles requeridos, las transiciones con guardas y dos clases terminales designadas. Las realizaciones de interfaz producen testigos tipados posteriores a la transducción; un episodio sólo queda constituido cuando al menos una asignación completa por papeles, formada por testigos localmente admisibles, satisface asimismo las restricciones estructurales conjuntas declaradas, y ambas comprobaciones son independientes de los resultados del mecanismo de resolución. Para cada papel, una equivalencia contextual indexada por el mecanismo de resolución identifica los valores indistinguibles para toda guarda y todo predicado terminal pertinente en cualquier contexto de los restantes papeles. Tres condiciones suficientes formuladas en el nivel de los testigos —equivalencia contextual local, preservación de las asignaciones constitutivas y completitud de los vectores de clases locales realizados— implican entonces la igualdad de los conjuntos realizados de vectores de clases y de firmas globales de resolución, el isomorfismo canónico de los mecanismos cociente semánticos y la preservación exacta del perfil de terminales alcanzables. Ocho escenarios adversariales finitos aíslan las hipótesis, mientras que una familia canónica de escalado reduce exactamente 4ᵏ asignaciones constitutivas a 2ᵏ firmas semánticas. Por construcción, las condiciones son suficientes, no necesarias.

**Palabras clave:** interfaces heterogéneas; sistemas de estados finitos; sustitución de componentes; equivalencia contextual; verificación composicional; sistemas formales.

## 1. Introducción

Los mecanismos finitos de decisión y resolución pueden depender de información suministrada mediante interfaces heterogéneas. Un papel requerido puede quedar instanciado por un sensor, una base de datos, una transformación de software, un modelo aprendido o una composición declarada de varias fuentes. Esta heterogeneidad plantea dos cuestiones formales distintas. Primera: ¿constituyen conjuntamente las salidas disponibles de las interfaces la estructura de entrada exigida por el problema de resolución declarado? Segunda: cuando una realización de interfaz se sustituye por otra, ¿qué condiciones bastan para preservar exactamente el comportamiento terminal alcanzable del mecanismo de resolución?

Estas preguntas deben mantenerse separadas. Un testigo puede ser localmente admisible y, sin embargo, resultar estructuralmente incompatible con los testigos disponibles para otros papeles. A la inversa, varios testigos localmente admisibles para un mismo papel pueden discrepar y, aun así, participar cada uno en una asignación conjunta legítima. Resolver esa discrepancia antes de instanciar el mecanismo de resolución puede eliminar una rama que la semántica declarada exige conservar. La sustitución introduce otra dificultad: exigir igualdad entre valores brutos suele ser más fuerte de lo necesario, mientras que la coincidencia en un único contexto observado suele ser demasiado débil. El criterio pertinente es si la sustitución conserva todas las distinciones que el mecanismo de resolución declarado puede observar.

Separamos, por ello, la frontera de interfaz de la semántica de resolución. En todo el artículo, denominamos **mecanismo de resolución** al mecanismo finito con guardas que se instancia únicamente después de constituir el episodio. El objeto primitivo de interfaz es un **testigo posterior a la transducción**: un valor tipado acompañado de los metadatos necesarios para evaluar su procedencia declarada, referencia, unidades e integridad. Para cada papel requerido, un verificador local evalúa un testigo individual sin consultar los valores suministrados para otros papeles, las guardas del mecanismo, los estados terminales, resultados preferidos ni el perfil final de terminales alcanzables. La compatibilidad estructural conjunta se evalúa por separado y queda sometida al mismo requisito de independencia respecto del resultado. Un episodio de resolución sólo queda constituido si existe al menos una asignación completa por papeles, conjuntamente compatible y formada por testigos localmente admisibles. Se conservan todas esas asignaciones, incluidas las que inducen comportamientos terminales distintos.

Una vez constituido el episodio, la semántica del mecanismo de resolución determina qué diferencias entre valores de testigo son relevantes. Para cada papel pertinente para la resolución definimos una equivalencia contextual a partir de la familia completa de guardas y predicados terminales del mecanismo declarado. Dos valores son equivalentes cuando sustituir uno por otro conserva todos esos predicados en cualquier contexto de los restantes papeles. Estas clases definidas por papel se elevan a vectores de clases locales y, mediante un lema de elevación de lo local a lo global, a firmas globales completas de resolución. Un cociente semántico conserva entonces una rama del mecanismo por cada firma global distinta, en lugar de una rama por cada asignación constitutiva bruta.

El teorema de sustitución se formula en el nivel de los testigos. Sean una realización de referencia y una realización sustitutiva que instancian el mismo contrato de resolución. Se exige que una aplicación que preserve los papeles, desde los testigos activos de la realización sustitutiva hacia testigos de referencia, satisfaga tres condiciones: equivalencia contextual de los valores asociados, preservación de las asignaciones constitutivas y completitud de los vectores de clases locales realizados por el sistema de referencia. En conjunto, estas condiciones implican la igualdad de los conjuntos realizados de vectores de clases locales y de los conjuntos de firmas globales. Los correspondientes mecanismos cociente semánticos son, por tanto, canónicamente isomorfos, y sus perfiles exactos de terminales alcanzables coinciden. Las condiciones se formulan deliberadamente como suficientes y no como necesarias: una sustitución puede preservar el perfil final aunque el certificado aquí propuesto no resulte aplicable.

La construcción no propone una nueva teoría general de la sustitución de componentes, la equivalencia contextual, la abstracción o la realizabilidad de contratos. Cada una de esas materias posee una literatura consolidada. La aportación reside en la conexión entre capas: los testigos heterogéneos tipados y la constitución del episodio, independiente de la resolución, quedan enlazados mediante un certificado comprobable en el nivel de los testigos con la preservación exacta de un mecanismo finito de resolución. El certificado se evalúa en la frontera de interfaz; la equivalencia global de los mecanismos es una conclusión, no una hipótesis.

El artículo realiza cuatro aportaciones. En primer lugar, define la constitución del episodio sobre testigos tipados posteriores a la transducción y separa la admisibilidad individual, la compatibilidad estructural conjunta y la semántica de resolución. En segundo lugar, define una equivalencia contextual por papel e indexada por el mecanismo de resolución a partir de la semántica declarada de guardas y terminales, y demuestra un resultado de elevación de lo local a lo global. En tercer lugar, establece condiciones suficientes, formuladas en el nivel de los testigos, bajo las cuales la sustitución de interfaces heterogéneas preserva el mecanismo cociente semántico y el perfil exacto de terminales alcanzables. En cuarto lugar, presenta ocho escenarios adversariales finitos y una familia canónica de escalado que examinan la independencia, el alcance y las consecuencias computacionales de la construcción.

## 2. Estado del arte y delimitación

### 2.1. Sustitución de interfaces y refinamiento composicional

La sustitución sensible a la interfaz es un problema establecido. Los autómatas de interfaz (*interface automata*) proporcionan una base formal para la compatibilidad y el refinamiento de interfaces de componentes [1]. Formulaciones algebraicas posteriores desarrollan relaciones de refinamiento concebidas expresamente para preservar la sustitución de componentes e incluyen operaciones como composición paralela, ocultación, conjunción, disyunción y cociente [2]. Las teorías de supuesto–garantía (*assume–guarantee*) sustentan, de manera análoga, el razonamiento composicional sobre modelos y contratos de componentes de entrada y salida [3]. Los trabajos sobre autómatas de interacción de componentes establecen precondiciones explícitas bajo las cuales sustituir un componente preserva la equivalencia del sistema actualizado [4].

El presente resultado no reivindica, por tanto, novedad para la sustitución conservadora de componentes como tal. Su aplicación de sustitución actúa en una frontera informativa anterior: relaciona testigos tipados producidos por realizaciones heterogéneas de interfaz antes de que se instancie el mecanismo finito de resolución. El objetivo de preservación queda fijado explícitamente como el conjunto exacto de clases terminales designadas que son alcanzables en ese mecanismo. El teorema establece condiciones suficientes en el nivel de los testigos que se elevan desde la capa previa a la resolución hasta la preservación del mecanismo global.

### 2.2. Realizabilidad, particiones semánticas y preservación fuerte

La realizabilidad de contratos pregunta si un contrato admite una implementación que satisfaga sus supuestos y garantías, y se han desarrollado métodos formales de comprobación de realizabilidad para lenguajes de contratos enriquecidos con teorías [5]. La constitución del episodio aborda un objeto más restringido. No sintetiza ni certifica una implementación completa. Pregunta, en cambio, si los testigos tipados disponibles en ese momento contienen al menos una asignación completa por papeles que satisfaga las comprobaciones locales y estructurales conjuntas declaradas bajo un contrato finito de resolución fijo. El fracaso de esta prueba se produce antes de instanciar el mecanismo representado por dicho contrato.

Las clases de equivalencia inducidas por predicados también están bien establecidas. Huang, Krafczyk y Peleska construyen clases de equivalencia sobre valoraciones de máquinas simbólicas de estados finitos a partir de guardas, expresiones de salida y proposiciones atómicas para pruebas exhaustivas basadas en modelos y orientadas a propiedades [6]. La relación empleada aquí ocupa otra posición y cumple otra finalidad. Se define por separado para cada papel pertinente para la resolución y se cuantifica sobre todos los contextos de los restantes papeles, porque la operación que se certifica es la sustitución de testigos tipados individuales. Las clases obtenidas por papel se elevan después a firmas completas del mecanismo de resolución.

La preservación exacta bajo abstracción cuenta asimismo con una base teórica amplia. Los resultados de preservación fuerte caracterizan abstracciones en las que los modelos concretos y abstractos satisfacen las mismas fórmulas de un lenguaje de especificación elegido, y relacionan la preservación con simulación, bisimulación y completitud en interpretación abstracta [7]. El cociente semántico definido más adelante no se presenta, por ello, como una nueva teoría general de abstracción. Elimina ramas duplicadas del mecanismo cuando poseen idéntica semántica declarada de guardas y terminales. La cuestión tratada aquí es si puede certificarse que un cambio efectuado antes, en la capa de testigos heterogéneos, deja inalterado ese cociente.

Para examinar esta frontera se realizó una búsqueda bibliográfica dirigida mediante combinaciones de términos relativas a sustitución y refinamiento de interfaces y componentes, realizabilidad de contratos, equivalencia inducida por predicados y guardas, sistemas cociente y preservación fuerte. Las construcciones más próximas localizadas están representadas por los trabajos citados. En la bibliografía examinada no se identificó un marco que parta de testigos tipados posteriores a la transducción, defina la constitución del episodio con independencia de los resultados del mecanismo de resolución y establezca condiciones suficientes en el nivel de los testigos que impliquen la preservación exacta del mecanismo finito resultante. Esta afirmación informa del resultado de la búsqueda bibliográfica; no pretende demostrar una inexistencia lógica exhaustiva.

### 2.3. Difusión previa y filiación conceptual

Preprints anteriores del autor, publicados en español, documentaron ideas precursoras sobre transducción tipada, interfaces estructuradas, soporte observacional, admisibilidad intermodal y una cadena más amplia de orientación dominio–interfaz [8–12]. Forman parte de la filiación conceptual y documental del presente trabajo, pero las definiciones y demostraciones que siguen son autocontenidas. En particular, la matriz de 22 de junio de 2026 [12] no contiene el predicado de constitución del episodio, la equivalencia contextual indexada por el mecanismo de resolución ni el teorema de sustitución que se demuestra aquí.

Un preprint independiente publicado el 8 de agosto de 2026 desarrolla perfiles exactos de clausura alcanzable, morfismos que cubren la resolución y complejidad de revisión para sistemas finitos de resolución [13]. El presente artículo utiliza únicamente el conjunto elemental de terminales alcanzables necesario para su resultado de preservación y demuestra de forma autocontenida la invariancia requerida. El preprint en español del presente trabajo científico se cita en [14]. Se declara como difusión previa de este mismo trabajo, no como aportación científica independiente de la que dependa el artículo.

## 3. Marco matemático

### 3.1. Contratos finitos de resolución

Sea

Θ = (D, q, 𝔾).  (1)

Θ es un **contrato finito de resolución** para un dominio de aplicación D y una consulta declarada q. Su esquema de resolución con guardas es

𝔾 = (X, 𝒜, E, x★, {gₑ}ₑ∈E, {tᵥ,ₓ}ᵥ∈{0,1},ₓ∈X).  (2)

Aquí, X es un conjunto finito de estados, 𝒜 es un alfabeto finito de acciones, E ⊆ X × 𝒜 × X es una relación estructural de transición y x★ es el estado inicial. Cada gₑ es una guarda booleana. Para v ∈ {0,1}, el predicado tᵥ,ₓ determina si el estado x pertenece a la clase terminal Tᵥ después de la valoración.

Se supone que el esquema está en **forma normal con guardas**: X, 𝒜 y E no dependen de la valoración, y toda elección dependiente de la valoración que afecte a la disponibilidad de una transición o a la pertenencia a cualquiera de las clases terminales está representada mediante una guarda o un predicado terminal. Por consiguiente, los destinos o las acciones que dependan de parámetros deben expandirse en alternativas estructurales con guardas.

Sea X° el conjunto de estados alcanzables desde x★ en el grafo dirigido subyacente cuando cada guarda se sustituye por el predicado constantemente verdadero. Sea E° el conjunto de aristas estructurales cuyo origen pertenece a X°. Para cualquier guarda o predicado terminal f, sea supp(f) su soporte declarado de parámetros. Definimos el soporte estructural conservador

PΘ^(str) = ⋃ₑ∈E° supp(gₑ) ∪ ⋃ₓ∈X°, v∈{0,1} supp(tᵥ,ₓ).  (3)

No se afirma que (3) sea mínimo. Un análisis estático más fuerte puede reducir este soporte; todos los resultados que siguen son relativos al contrato declarado Θ.

Para cada p ∈ PΘ^(str), sea 𝒱ₚ un dominio finito de valores. Toda guarda y todo predicado terminal son funciones totales sobre su producto finito declarado:

gₑ : ∏ₚ∈supp(gₑ) 𝒱ₚ → {0,1},  (4)

tᵥ,ₓ : ∏ₚ∈supp(tᵥ,ₓ) 𝒱ₚ → {0,1}.  (5)

La totalidad garantiza que toda valoración híbrida utilizada en la construcción de la equivalencia contextual esté definida.

### 3.2. Testigos tipados y constitución del episodio

Sea W una familia finita de **testigos posteriores a la transducción**. Un testigo es

w = (papel(w), val(w), μ(w)),  (6)

donde papel(w) ∈ PΘ^(str), val(w) pertenece al dominio finito 𝒱 correspondiente a papel(w), y μ(w) contiene los metadatos estructurales exigidos por el contrato, como tipo, referencia, unidad, dominio, procedencia e información declarada de integridad. El testigo es la salida de la interfaz o de la cadena de transducción declarada en la frontera pertinente para el contrato. Puede proceder de una sola fuente o de una transformación declarada en la que intervengan varias fuentes. La teoría no identifica un testigo con una lectura bruta de sensor ni con una tecnología física concreta. Para cada papel p, escribimos

W(p) = {w ∈ W : papel(w) = p}.  (7)

Para cada papel p, un verificador local

Vₚ : W(p) → {0,1}  (8)

comprueba únicamente la admisibilidad individual de los testigos asignados a p. Puede examinar el tipo, la pertenencia al dominio de valores, la referencia, la procedencia y la integridad de la cadena declarada de adquisición o transducción. Es independiente de la semántica del mecanismo de resolución: no puede consultar los valores de otros testigos, las guardas ni los predicados terminales introducidos más adelante, la pertenencia a clases terminales, una clase terminal preferida ni el perfil final de terminales alcanzables.

La compatibilidad estructural conjunta se representa mediante

J(b) = J̃(μ ∘ b).  (9)

La proyección de metadatos μ excluye la información derivada del mecanismo de resolución. En particular, no contiene etiquetas de clases semánticas locales, valores de guardas, valores terminales, un perfil terminal esperado ni campos calculados a partir de esas cantidades. Por tanto, (9) no puede actuar como selector encubierto de resultados del mecanismo de resolución.

Una **asignación constitutiva** es una aplicación

b : PΘ^(str) → W  (10)

que selecciona un testigo para cada papel requerido y satisface, para todo p,

papel(b(p)) = p,  Vₚ(b(p)) = 1,  (11)

junto con J(b) = 1. Sea ℬΘ(W) el conjunto de todas las asignaciones constitutivas. Definimos

ConstitΘ(W) = 1 ⇔ ℬΘ(W) ≠ ∅.  (12)

Decimos que el episodio de resolución **está constituido bajo Θ** cuando se cumple (12).

Esta afirmación es relativa al contrato. Si ConstitΘ(W) = 0, la familia de testigos disponible no instancia el mecanismo de resolución especificado por Θ. De ello no se sigue que ningún contrato alternativo pueda definir, sobre la misma información subyacente, un episodio constituido distinto.

Un certificado de constitución ζ consta de una asignación constitutiva candidata y de la información necesaria para evaluar las correspondientes comprobaciones locales y de compatibilidad conjunta. Si cada Vₚ y J̃ son decidibles, entonces

ConstitΘ(W) = 1 ⇔ ∃ζ : VerificaConstitΘ(ζ) = 1.  (13)

El fracaso de este verificador es un fracaso previo a la resolución. No se le asigna una clase terminal ni se trata como una propiedad de un mecanismo de resolución ya instanciado.

Cada b ∈ ℬΘ(W) induce una valoración completa

ν_b(p) = val(b(p)).  (14)

Dos asignaciones constitutivas admisibles pueden discrepar. Esa discrepancia se conserva en lugar de resolverse en la capa de constitución.

### 3.3. Equivalencia contextual indexada por el mecanismo de resolución

Sea

ℱΘ = {gₑ : e ∈ E°} ∪ {tᵥ,ₓ : v ∈ {0,1}, x ∈ X°}.  (15)

Para p ∈ PΘ^(str) y a ∈ 𝒱ₚ, definimos la firma contextual por papel

κₚ^Θ(a) = ( f(η[p ↦ a]) ) para todo f ∈ ℱΘ con p ∈ supp(f) y toda η ∈ ∏q∈supp(f)∖{p} 𝒱q.  (16)

Así, κₚ^Θ(a) registra cómo evalúa cada predicado del mecanismo de resolución que depende de p cuando se fija p = a, en todos los contextos posibles de los restantes argumentos de ese predicado.

Definimos

a ≡ₚ^Θ b ⇔ κₚ^Θ(a) = κₚ^Θ(b).  (17)

La relación ≡ₚ^Θ es una relación de equivalencia determinada por la semántica declarada del mecanismo de resolución. Sea

rₚ^Θ : 𝒱ₚ → 𝒱ₚ / ≡ₚ^Θ  (18)

la aplicación cociente.

Para una valoración completa ν, definimos la firma global de resolución

ρΘ(ν) = ((gₑ(ν))ₑ∈E°, (t₀,ₓ(ν))ₓ∈X°, (t₁,ₓ(ν))ₓ∈X°).  (19)

Para una asignación constitutiva b, definimos su vector de clases locales

λΘ(b) = (rₚ^Θ(ν_b(p)))ₚ∈PΘ^(str),  (20)

y los conjuntos realizados

ΛΘ(W) = {λΘ(b) : b ∈ ℬΘ(W)},  (21)

𝒮Θ(W) = {ρΘ(ν_b) : b ∈ ℬΘ(W)}.  (22)

**Lema 1. Preservación de la semántica de resolución de lo local a lo global.** Si dos valoraciones completas ν y ν′ satisfacen

rₚ^Θ(ν(p)) = rₚ^Θ(ν′(p)) para todo p ∈ PΘ^(str),  (23)

entonces

ρΘ(ν) = ρΘ(ν′).  (24)

**Demostración.** Enumeremos PΘ^(str) = {p₁, …, pₖ} y construyamos valoraciones híbridas ν⁽⁰⁾ = ν, …, ν⁽ᵏ⁾ = ν′ sustituyendo una coordenada cada vez. En el paso i, la condición (17) establece que sustituir ν(pᵢ) por ν′(pᵢ) preserva todo f ∈ ℱΘ que dependa de pᵢ, en cualquier contexto de los restantes argumentos de f. Los predicados que no dependen de pᵢ permanecen trivialmente inalterados, y la totalidad garantiza que cada contexto híbrido esté definido. Por tanto, f(ν⁽ⁱ⁻¹⁾) = f(ν⁽ⁱ⁾) para todo f ∈ ℱΘ. Al encadenar las k sustituciones se obtiene la igualdad de todos los componentes de (19). **□**

No se necesita la recíproca, y ésta puede no cumplirse: vectores distintos de clases locales pueden inducir la misma firma global.

### 3.4. Mecanismo finito de resolución y cociente semántico

Una asignación constitutiva b instancia

ℛΘ[b] = (X, 𝒜, →_b, x★, T₀^b, T₁^b),  (25)

donde, para (x, a, y) = e ∈ E,

x —a→_b y ⇔ gₑ(ν_b) = 1,  (26)

y

Tᵥ^b = {x ∈ X : tᵥ,ₓ(ν_b) = 1}.  (27)

Todas las asignaciones constitutivas se conservan en un único mecanismo finito de resolución introduciendo una raíz común x̂★ y una rama independiente por asignación. Definimos

X̂_W = {x̂★} ∪ (X × ℬΘ(W)),  (28)

Â_W = 𝒜 ⊔ {ι_b : b ∈ ℬΘ(W)}.  (29)

Para todo b ∈ ℬΘ(W),

x̂★ —ι_b→ (x★, b),  (30)

y

(x, b) —a→ (y, b) ⇔ x —a→_b y.  (31)

Los conjuntos terminales son

T̂ᵥ = {(x, b) : x ∈ Tᵥ^b}.  (32)

Denotamos este sistema por 𝒪Θ[W].

Para cualquier mecanismo finito de resolución ℛ, definimos su perfil exacto de terminales alcanzables en el estado x mediante

Cℛ(x) = {v ∈ {0,1} : Reachℛ(x) ∩ Tᵥ ≠ ∅}.  (33)

Este es el conjunto exacto de clases terminales designadas alcanzables desde x; puede ser vacío, unitario o igual a {0,1}. En el marco independiente del autor sobre no clausura finita [13], el mismo conjunto recibe el nombre de **perfil exacto de clausura alcanzable**. Ningún resultado posterior depende de terminología ni de semántica adicional de aquel marco.

Varias asignaciones constitutivas pueden inducir la misma firma global ρΘ. Definimos el mecanismo cociente semántico por

X̂_W★ = {x̂★} ∪ (X × 𝒮Θ(W)),  (34)

Â_W★ = 𝒜 ⊔ {ι_s : s ∈ 𝒮Θ(W)}.  (35)

Para una firma s = ρΘ(ν), denotamos por sₑ su componente asociado a la guarda gₑ y por sᵥ,ₓ su componente asociado al predicado terminal tᵥ,ₓ. Para todo s ∈ 𝒮Θ(W),

x̂★ —ι_s→ (x★, s).  (36)

Para e = (x, a, y) ∈ E°,

(x, s) —a→ (y, s) ⇔ sₑ = 1.  (37)

Finalmente,

T̂ᵥ★ = {(x, s) : x ∈ X°, sᵥ,ₓ = 1}.  (38)

Denotamos este cociente por 𝒪Θ★[W].

**Lema 2. Invariancia del perfil de terminales bajo el cociente semántico.**

C𝒪Θ[W](x̂★) = C𝒪Θ★[W](x̂★).  (39)

**Demostración.** Las asignaciones constitutivas que poseen la misma firma global inducen las mismas transiciones estructurales habilitadas y las mismas pertenencias terminales y, por tanto, el mismo perfil de rama. El cociente conserva una rama por cada firma distinta. Eliminar ramas duplicadas no puede añadir ni eliminar una clase terminal alcanzable desde la raíz común. **□**

### 3.5. Sustitución de interfaces heterogéneas que preserva el perfil

Definimos el conjunto de testigos activos

W_act = {w ∈ W : ∃b ∈ ℬΘ(W), ∃p, b(p) = w},  (40)

y W_act(p) = W_act ∩ W(p). Sólo son activos los testigos que aparecen en al menos una asignación constitutiva.

Sea W la realización de referencia y W′ una realización sustitutiva del mismo contrato Θ, con ambos episodios constituidos. Una sustitución tipada consta de aplicaciones

mₚ : W′_act(p) → W(p)  (41)

para todo p ∈ PΘ^(str). La dirección de (41) es deliberada: cada testigo activo producido por la realización sustitutiva se empareja con un testigo de referencia del mismo papel respecto del cual se comprueba la preservación. Para b′ ∈ ℬΘ(W′), definimos la asignación transformada por

(m ∘ b′)(p) = mₚ(b′(p)).  (42)

Se imponen tres condiciones suficientes.

**C2 — Equivalencia contextual local.**

val(w′) ≡ₚ^Θ val(mₚ(w′)) para todo w′ ∈ W′_act(p).  (43)

**C3 — Preservación de las asignaciones constitutivas.**

b′ ∈ ℬΘ(W′) ⇒ m ∘ b′ ∈ ℬΘ(W).  (44)

**C4λ — Completitud de los vectores de clases locales realizados.**

Para todo λ ∈ ΛΘ(W), existe b′ ∈ ℬΘ(W′) tal que λΘ(b′) = λ.  (45)

Estas condiciones son conservadoras y suficientes. No se afirma que caractericen todas las sustituciones que preservan (33).

**Lema 3. Igualdad de los conjuntos realizados de vectores de clases locales.** Bajo C2 y C3,

ΛΘ(W′) ⊆ ΛΘ(W).  (46)

Si además se cumple C4λ, entonces

ΛΘ(W′) = ΛΘ(W).  (47)

**Demostración.** Tomemos cualquier b′ ∈ ℬΘ(W′). Por C3, m ∘ b′ ∈ ℬΘ(W). Por C2, cada coordenada de b′ pertenece a la misma clase contextual que la coordenada correspondiente de m ∘ b′. Por ello, λΘ(b′) = λΘ(m ∘ b′) ∈ ΛΘ(W), lo que demuestra (46). La condición C4λ aporta la inclusión recíproca. **□**

**Lema 4. La igualdad de vectores de clases locales implica la igualdad de firmas globales.** Si se cumple (47), entonces

𝒮Θ(W′) = 𝒮Θ(W).  (48)

**Demostración.** Tomemos una firma inducida por algún b′ ∈ ℬΘ(W′). La igualdad de los conjuntos realizados de vectores de clases locales proporciona b ∈ ℬΘ(W) con λΘ(b′) = λΘ(b). El Lema 1 da entonces ρΘ(ν_b′) = ρΘ(ν_b). Así se obtiene una de las inclusiones entre los conjuntos de firmas; la inclusión recíproca se obtiene de forma simétrica. **□**

**Teorema 1. Condiciones en el nivel de los testigos para la preservación exacta del perfil de terminales.** Sean W y W′ realizaciones constituidas de interfaces heterogéneas del mismo contrato finito de resolución Θ. Si una sustitución tipada (41) satisface C2, C3 y C4λ, entonces

𝒮Θ(W′) = 𝒮Θ(W),  (49)

los mecanismos cociente semánticos son canónicamente isomorfos,

𝒪Θ★[W′] ≅ 𝒪Θ★[W],  (50)

y

C𝒪Θ[W′](x̂★) = C𝒪Θ[W](x̂★).  (51)

**Demostración.** Los lemas anteriores proporcionan la igualdad de los conjuntos realizados de firmas globales. Ambos mecanismos cociente se construyen sobre el mismo conjunto estructural de estados y contienen una rama por cada firma realizada. Identificar las dos raíces comunes y llevar cada estado (x, s) a su homólogo con el mismo par (x, s) define una biyección canónica. Esta biyección preserva y refleja cada selección inicial de rama, cada transición interna habilitada y cada pertenencia terminal; por tanto, es un isomorfismo de los dos mecanismos finitos de resolución. En consecuencia, una clase terminal es alcanzable desde la raíz de uno de los mecanismos cociente si y sólo si la clase correspondiente es alcanzable desde la raíz del otro. El Lema 2 traslada esta igualdad a los mecanismos no cocientados y demuestra (51). **□**

La condición C4λ sólo cuantifica sobre vectores de clases contextuales locales. No cuantifica sobre firmas globales, mecanismos de resolución completos, resultados terminales ni sobre el perfil final. El puente desde los vectores de clases locales hasta el conjunto de firmas globales lo proporcionan los Lemas 1 y 4.

### 3.6. Límites del certificado y obstrucción por indistinguibilidad

El incumplimiento de C2–C4λ no demuestra que haya cambiado el perfil terminal. Dos realizaciones pueden tener conjuntos de firmas globales distintos y, sin embargo, alcanzar exactamente las mismas clases terminales designadas:

𝒮Θ(W′) ≠ 𝒮Θ(W) y, aun así, C𝒪Θ[W′](x̂★) = C𝒪Θ[W](x̂★).  (52)

El teorema proporciona, por ello, un certificado suficiente y verificable, no una caracterización necesaria.

Sea

Ω_D,Θ^con = {ω : ConstitΘ(W(ω)) = 1}.  (53)

Para cada ω ∈ Ω_D,Θ^con, escribimos

C(ω) = C𝒪Θ[W(ω)](x̂★).  (54)

**Proposición 1. Obstrucción por indistinguibilidad.** Sea π_S : Ω_D,Θ^con → Y_S la representación de toda la información puesta a disposición por una familia de interfaces S. Si existen ω₁, ω₂ ∈ Ω_D,Θ^con tales que

π_S(ω₁) = π_S(ω₂),  C(ω₁) ≠ C(ω₂),  (55)

entonces ninguna función determinista F : Y_S → 𝒫({0,1}) puede recuperar el perfil exacto de terminales para ambos estados.

**Demostración.** La función F recibe la misma entrada para ω₁ y ω₂ y, por tanto, debe devolver la misma salida, mientras que los perfiles terminales correctos son distintos. **□**

### 3.7. Alcance computacional

Todos los dominios de valores y mecanismos de resolución considerados aquí son finitos. La construcción exhaustiva de las equivalencias contextuales por papel tiene un coste de evaluación, en el peor caso, acotado por

O( Σₚ∈PΘ^(str) |𝒱ₚ|² · Σ_{f∈ℱΘ, p∈supp(f)} [∏q∈supp(f)∖{p} |𝒱q|] · c_f ).  (56)

donde c_f es el coste de evaluar f. El coste puede, por tanto, crecer exponencialmente con la aridad del soporte de los predicados. El teorema no presupone un comprobador barato de equivalencia. Para lenguajes restringidos de predicados pueden emplearse, en cambio, procedimientos simbólicos basados en SAT o SMT.

## 4. Evaluación finita reproducible

La evaluación persigue dos fines. El primero es adversarial: los escenarios separan las funciones de las hipótesis del teorema y ponen a prueba distinciones semánticas que, de otro modo, podrían confundirse. El segundo es estructural: la familia de escalado muestra cómo el cociente inducido por la semántica declarada del mecanismo de resolución puede eliminar grandes multiplicidades de asignaciones constitutivas brutas sin modificar el perfil exacto de terminales. Todos los ejemplos son finitos y pueden comprobarse exhaustivamente. El verificador determinista suplementario implementa los contratos finitos, la verificación local de testigos, la compatibilidad estructural conjunta, la enumeración de asignaciones constitutivas, la equivalencia contextual, las firmas locales y globales, los mecanismos de resolución brutos y cocientados, los perfiles exactos de alcanzabilidad y las condiciones C2–C4λ.

### 4.1. Mecanismo común de resolución

Siete escenarios utilizan el conjunto común de estados

X = {x★, a, b, c, d, t₀, t₁},  (57)

con p ∈ {0,1,2,3} y q, r ∈ {0,1}. Las aristas con guardas son

x★ → a ⇔ r = 1,   x★ → b ⇔ q = 1,  (58)

a → c ⇔ q = 1,   b → c ⇔ r = 1,  (59)

c → t₀ ⇔ p ∈ {0,2},   c → t₁ ⇔ p = 1,  (60)

c → d ⇔ p = 3,   d → t₀ incondicionalmente.  (61)

Las clases terminales son T₀ = {t₀} y T₁ = {t₁}. Con q = r = 1,

p ∈ {0,2,3} ⇒ C = {0},   p = 1 ⇒ C = {1}.  (62)

Sin embargo,

0 ≡ₚ^Θ 2,   0 ≢ₚ^Θ 1,   0 ≢ₚ^Θ 3,  (63)

porque p = 0 y p = 3 inducen valores distintos de las guardas: el primero habilita c → t₀, mientras que el segundo habilita c → d. Ambas ramas alcanzan finalmente t₀, pero la equivalencia contextual registra la semántica declarada de guardas y terminales, no sólo la alcanzabilidad terminal. El escenario F2 utiliza la guarda acoplada g(p, q) = [p + q > 5] para distinguir la equivalencia contextual de la coincidencia puntual.

### 4.2. Serie adversarial finita

| ID | Objeto de la prueba | Construcción | Referencia | Sustitución |
|---|---|---|---:|---:|
| F1 | Independencia de C2 | W realiza p = 0; W′ realiza p = 0,1. La aplicación tipada lleva ambos valores de la sustitución al testigo de referencia con p = 0. Se cumplen C3 y C4λ; C2 falla en 1 ↦ 0. | {0} | {0,1} |
| F2 | Equivalencia contextual frente a coincidencia puntual | Guarda g = [p + q > 5]. Referencia p = 2, sustitución p = 3, con q = 3,4 admisibles. Los dos valores de p coinciden cuando q = 4, pero discrepan cuando q = 3. | {0,1} | {1} |
| F3 | Independencia de C3 | La referencia W tiene un testigo válido con p = 0 y un testigo localmente admisible con p = 1 cuyo valor para el mecanismo coincide con el de su homólogo sustitutivo, pero cuyos metadatos de episodio son incompatibles. W′ posee p = 0,1 válidos. Se cumplen C2 y C4λ, pero la imagen de la asignación p = 1 no es constitutiva. | {0} | {0,1} |
| F4 | Independencia de C4λ | W realiza las clases locales de p = 0 y p = 1; W′ conserva sólo la clase p = 0. C2 y C3 se cumplen para todo testigo activo que permanece. | {0,1} | {0} |
| F5 | Por qué la aplicación se restringe a W′_act | Se añade un testigo localmente admisible que no puede intervenir en ninguna asignación constitutiva porque sus metadatos incumplen J. Exigirle una imagen de sustitución haría fracasar el certificado aunque no cambie ninguna rama del mecanismo. | {0} | {0} |
| F6 | Por qué el objeto primitivo es el testigo posterior a la transducción | Dos cadenas de transducción independientemente admisibles producen testigos distintos para el mismo papel, con valores 0 y 1. Fusionarlos prematuramente elimina una rama constitutiva legítima. | {0,1} | {0,1} |
| F7 | Sustitución sin igualdad de valores brutos | La interfaz de referencia produce p = 0 y la sustitutiva produce p = 2. Los valores brutos son distintos, pero 0 ≡ₚ^Θ 2; se cumplen C3 y C4λ. | {0} | {0} |
| F8 | La suficiencia no implica necesidad | La realización de referencia usa p = 0 y la arista directa c → t₀; la sustitutiva usa p = 3 y la trayectoria c → d → t₀. Las clases locales y las firmas difieren, pero los perfiles de terminales alcanzables coinciden. | {0} | {0} |

Los escenarios establecen hechos distintos, en lugar de repetir una única ablación. F1 muestra que C2 no es redundante respecto del tipado de papeles, la preservación de asignaciones y la completitud de vectores de clases locales. F2 descarta la condición más débil en la que C2 se comprueba únicamente en el contexto observado en ese momento. Como la sustitución debe seguir siendo semánticamente intercambiable en cualquier contexto en el que el mecanismo declarado pueda situar el valor de ese papel, la coincidencia puntual en un solo contexto es insuficiente.

F3 aísla C3. La igualdad de los valores pertinentes para el mecanismo de resolución no repara una asignación estructuralmente inadmisible: la procedencia, la referencia u otra restricción declarada de metadatos puede impedir que los testigos transformados formen un episodio legítimo. F4 aísla C4λ. Las condiciones C2 y C3 impiden que la sustitución introduzca clases semánticas locales ausentes de la realización de referencia, pero no impiden que pierda una clase de referencia. La completitud aporta precisamente esa cobertura recíproca.

F5 muestra por qué los testigos inactivos quedan fuera de la obligación de sustitución. Un testigo que no puede participar en ninguna asignación constitutiva no aporta ninguna rama al mecanismo de resolución. F6 muestra por qué el objeto primitivo de interfaz se sitúa después de la transducción declarada y no en el nivel de las fuentes brutas: varias fuentes heterogéneas pueden alimentar un mismo testigo, y transducciones admisibles distintas pueden producir testigos contradictorios que deben permanecer separados hasta que el mecanismo de resolución los evalúe. F7 confirma que el teorema no exige identidad física ni igualdad de valores brutos. F8 marca la frontera opuesta: el incumplimiento de las condiciones suficientes no implica que haya cambiado el perfil de terminales alcanzables.

### 4.3. Familia canónica de escalado

Para separar la multiplicidad representacional de la semántica del mecanismo de resolución, considérese un sistema con k papeles, cada uno con dominio de valores {0,1,2,3}, y predicados que distinguen únicamente la paridad en cada papel. Entonces

{0,2} y {1,3}  (64)

son las dos clases contextuales de cada papel. Si cada valor bruto se representa de forma independiente, el número de asignaciones constitutivas es 4ᵏ, mientras que el número de vectores de clases locales es 2ᵏ. Una familia de guardas que exponga cada bit de paridad produce una firma global por cada vector de clases locales. La tabla siguiente recoge los recuentos exactos.

| k | Asignaciones brutas 4ᵏ | Firmas 2ᵏ | Reducción |
|---:|---:|---:|---:|
| 2 | 16 | 4 | 4× |
| 3 | 64 | 8 | 8× |
| 4 | 256 | 16 | 16× |
| 5 | 1.024 | 32 | 32× |
| 6 | 4.096 | 64 | 64× |
| 7 | 16.384 | 128 | 128× |
| 8 | 65.536 | 256 | 256× |

Se trata de recuentos combinatorios exactos, no de mediciones de tiempo de ejecución. Cuantifican la reducción obtenida cuando múltiples asignaciones constitutivas son indistinguibles para toda guarda y todo predicado terminal declarados. Por el Lema 2, esta reducción deja inalterado el perfil de terminales alcanzables.

## 5. Discusión

### 5.1. La constitución es distinta de la resolución

La expresión (12) separa tres situaciones lógicamente diferentes. En primer lugar, una salida individual de interfaz puede incumplir su verificador local; ese testigo no puede sostener el papel que se le ha asignado. En segundo lugar, todos los testigos disponibles pueden ser individualmente admisibles y, sin embargo, no existir ningún conjunto completo por papeles que satisfaga las restricciones estructurales conjuntas; en ese caso, el episodio no está constituido bajo Θ. En tercer lugar, un mecanismo de resolución constituido puede presentar un perfil de terminales alcanzables vacío, unitario o con dos clases. Sólo este tercer caso es una propiedad de un mecanismo ya instanciado.

Esta distinción evita un error de categoría. No poder instanciar el problema de resolución declarado no constituye un resultado terminal negativo. A la inversa, constituir correctamente el episodio no implica una clase terminal única; sólo establece que el mecanismo finito de resolución declarado ha quedado instanciado a partir de evidencia de interfaz admisible.

### 5.2. La discrepancia admisible se conserva

La factorización de (9) y la independencia de los verificadores locales respecto de la semántica de resolución son restricciones deliberadas. Impiden que la capa de constitución filtre testigos por el resultado que inducirían en el mecanismo. Si dos testigos individualmente admisibles discrepan, pero cada uno participa en una asignación constitutiva válida, ambas asignaciones permanecen en ℬΘ(W) y, por tanto, ambas ramas permanecen en 𝒪Θ[W]. Es el mecanismo de resolución, y no la capa de admisión de interfaces, el que determina la consecuencia de esa discrepancia.

Esta separación adquiere especial importancia cuando las interfaces son heterogéneas. Un mismo papel puede estar sustentado por cadenas de adquisición o transformación distintas, con implementaciones físicas, procedencias de datos o codificaciones numéricas diferentes. El teorema no exige que esas realizaciones sean idénticas. Exige preservar la clase contextual pertinente para el mecanismo de resolución, junto con la preservación y la cobertura de la estructura constitutiva.

### 5.3. Relación con las teorías establecidas de sustitución y preservación

El teorema es deliberadamente más restringido que los resultados generales sobre sustitución. Los autómatas de interfaz, el razonamiento de supuesto–garantía y los marcos de sustitución de componentes ya proporcionan tratamientos amplios de la sustitución segura de componentes [1–4]. Del mismo modo, los cocientes semánticos y la preservación fuerte cuentan con teorías generales que no se reproducen aquí [7]. La construcción presente fija una frontera informativa concreta: la sustitución se expresa sobre testigos tipados que preceden a un mecanismo finito de resolución, y el certificado debe poder comprobarse sin presuponer la equivalencia global del mecanismo que precisamente pretende establecer.

Esta ubicación explica también el papel de C4λ. La condición no exige directamente la igualdad de firmas globales. Exige, en cambio, que la sustitución realice todos los vectores de clases locales presentes en la realización de referencia. Combinada con C2 y C3, produce la igualdad de los conjuntos realizados de vectores de clases locales; el Lema 1 eleva después esa igualdad a las firmas globales. El teorema proporciona así un certificado suficiente que conecta una capa de testigos previa a la resolución con un invariante global exacto.

El resultado no debe interpretarse como una caracterización necesaria. F8 aporta un contraejemplo finito: dos realizaciones pueden diferir en sus clases locales y en su estructura de transición y, aun así, alcanzar la misma clase terminal. El fracaso del certificado significa únicamente que la vía suficiente aquí propuesta no ha establecido la preservación. No constituye evidencia de que la sustitución haya modificado el resultado.

### 5.4. Aplicabilidad más allá de una tecnología concreta de interfaz

Nada en la matemática exige que un testigo proceda de un sensor físico determinista. Puede producirlo hardware de medida, un servicio de software, una base de datos, una transformación basada en reglas o un modelo aprendido, siempre que la aplicación aporte las comprobaciones declaradas de admisibilidad local y de metadatos. El teorema no valida esas comprobaciones específicas del dominio. Sólo restringe su función formal y establece qué se sigue cuando se satisfacen.

La misma distinción se aplica a la incertidumbre. Pueden emplearse procedimientos estadísticos o probabilísticos en una etapa previa para producir un testigo candidato. La constitución finita y la semántica de resolución estudiadas aquí siguen condicionadas a los valores declarados de los testigos resultantes y a sus reglas de verificación. El teorema no requiere ningún modelo de probabilidad, ni se afirma que la incertidumbre probabilística pueda reducirse siempre a los dominios finitos aquí supuestos.

## 6. Limitaciones

El marco es finito. Las dinámicas continuas, los dominios de valores no acotados o las semánticas de guardas parcialmente definidas requieren una abstracción finita o una teoría distinta. El soporte estructural de (3) es conservador y puede exigir testigos para ramas estructuralmente alcanzables que un análisis estático más fuerte demostrase irrelevantes. En consecuencia, ConstitΘ(W) = 0 es una afirmación relativa al contrato declarado, no un teorema de imposibilidad sobre todas las formulaciones alternativas del problema.

La corrección, específica del dominio, de los verificadores locales, del modelo de metadatos y de la relación de compatibilidad conjunta se considera en términos extensionales. El marco restringe qué información pueden consultar estos mecanismos para impedir que codifiquen de forma encubierta el resultado deseado de la resolución, pero no demuestra que una regla concreta de calibración, procedencia, conversión de unidades, un registro de base de datos o un criterio de validación de un modelo aprendido sean científicamente correctos. Esos juicios siguen siendo obligaciones externas del dominio de aplicación.

La construcción de equivalencia contextual puede ser costosa. La expresión (56) muestra un crecimiento exponencial, en el peor caso, con la aridad del soporte de los predicados. Los métodos simbólicos pueden reducir el coste para lenguajes de predicados adecuados, pero aquí no se formula ninguna afirmación de tiempo polinómico.

Por último, C2, C3 y C4λ son condiciones suficientes, pero no necesarias, para la igualdad del perfil de terminales alcanzables. El teorema ofrece, por tanto, una vía conservadora de certificación, no una clasificación completa de todas las sustituciones que preservan el perfil. La evaluación es formal y computacional: comprueba exhaustivamente los escenarios finitos y la familia de escalado, pero no sustituye a la validación empírica específica del dominio de una tecnología concreta de interfaz.

## 7. Conclusión

Este trabajo ha desarrollado un marco para sistemas finitos que separa la constitución del episodio de la ejecución del mecanismo de resolución bajo interfaces heterogéneas. Un contrato finito de resolución determina los papeles y el soporte estructural pertinentes para su semántica de guardas y terminales. Los testigos tipados posteriores a la transducción se verifican localmente sin acceso a los resultados de resolución, y las selecciones completas por papeles que son conjuntamente compatibles forman asignaciones constitutivas. La discrepancia legítima puede así permanecer explícita en lugar de quedar eliminada por una regla previa de fusión.

La equivalencia contextual indexada por el mecanismo de resolución identifica, para cada papel, los valores finitos que la semántica declarada de guardas y terminales no puede distinguir en ningún contexto de los restantes papeles. El lema de elevación de lo local a lo global lleva la igualdad de las clases definidas por papel a la igualdad de firmas completas del mecanismo de resolución. Sobre esa base, C2, C3 y C4λ proporcionan un certificado suficiente en el nivel de los testigos para la sustitución de interfaces heterogéneas: implican la igualdad de los conjuntos realizados de vectores de clases locales, la igualdad de los conjuntos de firmas globales, el isomorfismo canónico de los mecanismos cociente semánticos y la preservación exacta del perfil de terminales alcanzables.

La serie adversarial delimita el alcance del certificado. La equivalencia contextual local, la preservación de asignaciones constitutivas y la completitud de vectores de clases locales protegen frente a modos de fallo distintos; los testigos inactivos no necesitan ser transformados; la igualdad de valores brutos no es necesaria; y el fracaso del certificado no implica un cambio en el perfil terminal. La familia de escalado muestra además que el cociente semántico puede eliminar grandes multiplicidades de asignaciones constitutivas brutas mientras preserva exactamente el comportamiento terminal. El resultado es una conexión finita y comprobable entre realizaciones heterogéneas de interfaz y un invariante global del mecanismo de resolución, no una nueva teoría general de sustitución de componentes o de abstracción.

## Disponibilidad de datos

En este estudio no se generaron ni analizaron datos.

## Disponibilidad del código

Se ha enviado a Code Ocean, para su publicación y archivo, un verificador determinista en Python que reproduce los ocho escenarios adversariales finitos y la familia canónica de escalado (DOI provisional: https://doi.org/10.24433/CO.5971538.v2). Las demostraciones matemáticas del presente trabajo son autocontenidas y no dependen del verificador.

## Financiación

Este trabajo no recibió financiación externa.

## Declaración de intereses

El autor declara que no existen intereses contrapuestos que deban declararse.

## Declaración sobre el uso de inteligencia artificial generativa

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para la localización de bibliografía, la comprobación adversarial de la coherencia, la estructuración del manuscrito, la asistencia en la formalización matemática y la composición tipográfica, así como para la revisión lingüística del inglés. Grok 4.5 (xAI; interacción de 8 de agosto de 2026) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias sobre presentación y posicionamiento. Todas las salidas de las herramientas de IA se trataron como material no autoritativo de apoyo a la investigación. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume la responsabilidad íntegra del presente trabajo.

## Nota biográfica

Juan Antonio Lloret Egea es ingeniero en Electrónica y Automática y miembro del Institute of Electrical and Electronics Engineers (IEEE). Dirige *La Biblia de la IA – The Bible of AI* y *The Bible of AI Open Science* (BAIOS), es miembro de Apply AI Alliance y miembro asociado de CEDRO. Su trayectoria profesional comprende la docencia en informática y telecomunicaciones, la dirección de medios de comunicación y la edición. Cofundó en 1997 el periódico *El Noroeste*, que dirigió entre 2005 y 2008, y cofundó y dirigió Ediciones Gollarín hasta 2008. Fue profesor de Informática y Telecomunicaciones en la Consejería de Educación de Madrid y actualmente está jubilado. ORCID: 0000-0002-6634-3351.

## Referencias

1. L. de Alfaro y T. A. Henzinger, “Interface automata”, en *Proceedings of the 8th European Software Engineering Conference Held Jointly with the 9th ACM SIGSOFT International Symposium on Foundations of Software Engineering (ESEC/FSE)*, 2001, pp. 109–120. https://doi.org/10.1145/503209.503226

2. C. Chilton, B. Jonsson y M. Kwiatkowska, “An algebraic theory of interface automata”, *Theoretical Computer Science*, vol. 549, pp. 146–174, 2014. https://doi.org/10.1016/j.tcs.2014.07.018

3. C. Chilton, B. Jonsson y M. Kwiatkowska, “Compositional assume–guarantee reasoning for input/output component theories”, *Science of Computer Programming*, vol. 91, parte A, pp. 115–137, 2014. https://doi.org/10.1016/j.scico.2013.12.010

4. I. Černá, P. Vařeková y B. Zimmerova, “Component substitutability via equivalencies of component-interaction automata”, *Electronic Notes in Theoretical Computer Science*, vol. 182, pp. 39–55, 2007. https://doi.org/10.1016/j.entcs.2006.09.030

5. A. Gacek, A. Katis, M. W. Whalen, J. Backes y D. Cofer, “Towards realizability checking of contracts using theories”, en *NASA Formal Methods: 7th International Symposium, NFM 2015*, Lecture Notes in Computer Science, vol. 9058, 2015, pp. 173–187. https://doi.org/10.1007/978-3-319-17524-9_13

6. W.-l. Huang, N. Krafczyk y J. Peleska, “Exhaustive property oriented model-based testing with symbolic finite state machines”, *Science of Computer Programming*, vol. 231, art. 103005, 2024. https://doi.org/10.1016/j.scico.2023.103005

7. F. Ranzato y F. Tapparo, “Generalized strong preservation by abstract interpretation”, *Journal of Logic and Computation*, vol. 17, n.º 1, pp. 157–197, 2007. https://doi.org/10.1093/logcom/exl035

8. J. A. Lloret Egea, “Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable”, preprint, 17 de marzo de 2026. https://doi.org/10.21428/39829d0b.f471b07c

9. J. A. Lloret Egea, “Formalización de una interfaz visual estructurada en el Sistema Vectorial SV”, preprint, 17 de marzo de 2026. https://doi.org/10.21428/39829d0b.b96fee32

10. J. A. Lloret Egea, “Primera forma legítima del frente de corpus observacional tipado del Sistema Vectorial SV”, preprint, 20 de marzo de 2026. https://doi.org/10.21428/39829d0b.d8304be4

11. J. A. Lloret Egea, “Modelo formal de admisibilidad olfativa e indeterminación intermodal en el Sistema Vectorial SV”, preprint, 21 de marzo de 2026. https://doi.org/10.21428/39829d0b.51507a08

12. J. A. Lloret Egea, “Orientación universal y geográfica, potencial del suceso e interfaz de dominio desde el universo y los seres biológicos: humanoide”, preprint, 22 de junio de 2026. https://doi.org/10.21428/39829d0b.5e15cabb

13. J. A. Lloret Egea, “Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity”, preprint, 8 de agosto de 2026. https://doi.org/10.21428/39829d0b.f0892864

14. J. A. Lloret Egea, “Sustitución de interfaces heterogéneas en sistemas finitos de resolución: constitución del episodio y preservación exacta de los perfiles de terminales alcanzables”, preprint, 13 de agosto de 2026. https://doi.org/10.21428/39829d0b.e5347310
