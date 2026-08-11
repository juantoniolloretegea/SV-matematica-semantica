# Certificados de clausura entre dominios para modelos físicos acoplados: desajuste entre transductores, conversión entre clases de medida e insuficiencia del balance escalar terminal

**Juan Antonio Lloret Egea**  
juanantoniolloretegea@ieee.org  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español, Madrid, España  
11 de agosto de 2026

## Resumen

Los modelos físicos acoplados pueden reproducir correctamente el balance escalar final y, sin embargo, representar de forma incorrecta el modo en que una magnitud física se transfiere entre dominios. Formulamos un certificado de clausura basado en teoría de la medida para este tipo de composiciones. A cada dominio se le asigna un espacio de medidas de Radon finitas con signo, junto con un transductor físico de referencia y un transductor del modelo. Su comparación conduce a una recurrencia residual exacta que separa el error heredado, el desajuste entre transductores y el defecto local o interfacial. Respecto de una medida de referencia prescrita, la descomposición de Lebesgue resuelve el residuo en componentes absolutamente continua y singular. Demostramos que, cuando un transductor físico genera una componente singular a partir de una entrada regular, pero la clase admisible de modelos no puede representar esa conversión, la distancia en variación total a la clase de modelos contiene un error irreducible de magnitud igual a la de la componente singular ausente, además de cualquier error residual de aproximación regular. A lo largo de cadenas de transductores positivos que conservan la masa, las omisiones locales positivas se acumulan exactamente. Demostramos asimismo que la anulación del balance escalar terminal no implica la clausura del residuo con signo. Un banco de prueba basado en el cambio de fase del agua ilustra la diferencia: omitir una contribución latente de 40,65 kJ mol⁻¹ produce un error irreducible de la misma magnitud, mientras que redistribuir esa energía a través del canal regular puede hacer exacto el balance energético terminal y dejar, no obstante, un residuo de variación total de 81,30 kJ mol⁻¹. La cadena se indexa únicamente por el orden de transferencia; los resultados no requieren ni el tiempo ni la probabilidad como primitivas.

**Palabras clave:** física matemática; modelos acoplados; medidas de Radon; desajuste entre transductores; interfaces singulares; certificados de clausura; variación total.

## I. Introducción

Los modelos físicos modernos suelen ser modulares. Una magnitud puede representarse en un dominio constitutivo, transferirse a través de una interfaz, convertirse en otra representación física y, finalmente, expresarse mediante un observable escalar o un balance. Los módulos pueden ser correctos por separado y no serlo su composición. Esta distinción es conocida en diversos marcos consolidados: la descomposición de operadores separa los efectos de discretización y transferencia; los sistemas hiperbólicos acoplados pueden requerir términos fuente singulares en las interfaces; las leyes de balance con valores en medidas admiten fuentes concentradas en conjuntos de menor dimensión; las teorías de deformaciones estructuradas distinguen contribuciones volumétricas e interfaciales; y los métodos de cosimulación cuantifican residuos de acoplamiento entre simuladores que, por lo demás, son independientes [7, 8, 3–6, 10].

La cuestión que se aborda aquí es más precisa: ¿cuándo una composición especificada de modelos físicos está clausurada como composición, en lugar de limitarse a producir un resultado escalar final correcto? Una prepublicación anterior del presente autor formuló esta cuestión física en términos de identidades específicas de dominio, fronteras, canales, residuos y aplicaciones de retorno, y presentó cálculos explícitos con agua que muestran que una frontera de fase puede dominar la energía necesaria para completar una transferencia [1]. El presente trabajo no exige que el lector adopte aquel marco más amplio. En su lugar, extrae un problema matemático autocontenido y desarrolla un certificado basado en teoría de la medida que puede comprobarse de forma independiente.

Son esenciales tres distinciones. En primer lugar, puede heredarse un residuo preexistente de un dominio anterior. En segundo lugar, el transductor físico asociado a una transferencia entre dominios puede diferir del transductor empleado por el modelo. En tercer lugar, la propia transferencia puede incorporar una fuente o una contribución de frontera que el modelo omite. Estos mecanismos son algebraicamente distintos y no deben reducirse a un único error terminal.

Una segunda distinción concierne a la clase de medida. Respecto de una medida de referencia declarada, un incremento físico puede poseer una parte absolutamente continua y una parte singular. Una contribución singular no constituye automáticamente una «interfaz»; esa interpretación exige identificar físicamente su soporte. Sin embargo, cuando una frontera de fase, una carga superficial, una fuente impulsiva u otra contribución física localizada se representa mediante una medida singular, una clase de modelos restringida a salidas absolutamente continuas no puede reproducirla únicamente mediante una mejora de su resolución interior.

La contribución de este trabajo es un certificado de clausura entre dominios construido a partir de estos elementos clásicos, y no un nuevo teorema estructural sobre espacios de medidas o retículos de Banach. Derivamos una identidad residual exacta, de un paso y de n pasos, para transductores acoplados de medidas. A continuación demostramos un teorema de obstrucción irreducible por conversión entre clases: para una entrada regular, si el transductor físico genera una componente singular de salida mientras que la clase admisible de salidas del modelo es regular, la distancia en variación total a esa clase se descompone exactamente en la norma de la componente singular más el mejor error de aproximación regular. Demostramos una ley exacta de acumulación para omisiones positivas bajo transductores positivos que conservan la masa, así como un resultado de persistencia para residuos singulares sometidos después a transferencias fieles a las bandas. Por último, demostramos que el balance escalar terminal no constituye un certificado de clausura para residuos con signo.

La distinción se ilustra mediante dos bancos de prueba basados en los datos de referencia del agua de la Ref. [1]. En el banco de prueba de cambio de fase, el calor latente se representa como un incremento singular etiquetado en la temperatura externa de la frontera de fase. En el segundo, los volúmenes del líquido y del vapor se tratan como un problema puro de desajuste entre transductores sobre un dominio de magnitudes de un solo punto. Los ejemplos no introducen una nueva termodinámica; proporcionan realizaciones físicas transparentes de las obstrucciones matemáticas.

El marco no requiere una variable temporal. El índice de una cadena de dominios es ordinal: registra el orden de las transferencias prescritas. Si una teoría externa concreta introduce después tiempo, frecuencia, probabilidad o variables estadísticas de estado, estas pueden incorporarse como datos de ese dominio sin convertirse en primitivas de la construcción de clausura.

## II. Espacios de medidas y transferencias prescritas entre dominios

Sea Xᵢ un espacio de Hausdorff localmente compacto que describe el soporte utilizado en el i-ésimo dominio físico, con σ-álgebra de Borel ℬᵢ. Sea mᵢ una medida de Radon positiva, finita y fija de referencia sobre Xᵢ. Denotamos por

𝓜ᵢ := 𝓜(Xᵢ).  (1)

el retículo de Banach de las medidas de Radon finitas con signo sobre Xᵢ, dotado de la norma de variación total

‖η‖TV := |η|(Xᵢ).  (2)

La medida de referencia mᵢ forma parte de la especificación del dominio. Cambiarla puede modificar qué contribución se denomina regular o singular; por tanto, ese cambio no se considera una modificación meramente notacional.

Por el teorema de descomposición de Lebesgue, toda η ∈ 𝓜ᵢ admite una descomposición única [2]

η = ηᵢᵃ + ηᵢˢ,   ηᵢᵃ ≪ mᵢ,   ηᵢˢ ⟂ mᵢ.  (3)

Escribimos

𝒜ᵢ := {η ∈ 𝓜ᵢ : η ≪ mᵢ},   𝒮ᵢ := {η ∈ 𝓜ᵢ : η ⟂ mᵢ}.  (4)

y denotamos por Pᵢᵃ y Pᵢˢ las proyecciones de banda asociadas. Así,

𝓜ᵢ = 𝒜ᵢ ⊕ 𝒮ᵢ.  (5)

Si α ∈ 𝒜ᵢ y σ ∈ 𝒮ᵢ, entonces α ⟂ σ y

‖α + σ‖TV = ‖α‖TV + ‖σ‖TV.  (6)

La descomposición de la ecuación (5) pertenece a la teoría clásica de la medida. El papel que se le asigna a continuación es el de componente de un certificado de clausura para la composición de modelos entre dominios; no se reivindica ningún nuevo teorema estructural sobre espacios de medidas.

**Definición 1 (Transferencia prescrita entre dominios).** Una transferencia prescrita de Dᵢ₋₁ a Dᵢ es una aplicación afín

μᵢ = Kᵢ μᵢ₋₁ + bᵢ,  (7)

donde Kᵢ: 𝓜ᵢ₋₁ → 𝓜ᵢ es lineal y acotado, y bᵢ ∈ 𝓜ᵢ es una contribución local prescrita. La transferencia correspondiente del modelo es

νᵢ = K̂ᵢ νᵢ₋₁ + b̂ᵢ.  (8)

No se afirma que todas las aplicaciones constitutivas físicas sean lineales. Los resultados presentes se aplican a un transductor lineal especificado de medidas o a una familia dependiente del estado una vez fijados sus parámetros externos.

El término bᵢ es deliberadamente más amplio que el de término interfacial. Según el problema físico, puede representar una fuente interfacial, una contribución debida a un cambio de fase, una carga impuesta, una inyección u otra contribución localizada en la transferencia y no heredada de la medida entrante.

**Definición 2 (Residuo de clausura).** El residuo en el dominio Dᵢ es

Δᵢ := μᵢ − νᵢ ∈ 𝓜ᵢ.  (9)

Definimos además el defecto de transducción evaluado sobre el estado del modelo y el defecto de fuente local mediante

Θᵢ := (Kᵢ − K̂ᵢ)νᵢ₋₁,  (10)  
εᵢ := bᵢ − b̂ᵢ.  (11)

Las denominaciones «físico» y «del modelo» no implican que Kᵢ sea conocido a partir de primeros principios. Indican únicamente que Kᵢ es el transductor cuyo contenido físico se somete a prueba, mientras que K̂ᵢ es el transductor realmente utilizado por la composición objeto de auditoría.

## III. Identidades residuales exactas

**Lema 1 (Identidad residual de un paso).** Para toda transferencia prescrita en las ecuaciones (7) y (8),

**Δᵢ = KᵢΔᵢ₋₁ + Θᵢ + εᵢ.**  (12)

**Demostración.** Usando μᵢ₋₁ = νᵢ₋₁ + Δᵢ₋₁,

Δᵢ = Kᵢμᵢ₋₁ + bᵢ − K̂ᵢνᵢ₋₁ − b̂ᵢ = KᵢΔᵢ₋₁ + (Kᵢ − K̂ᵢ)νᵢ₋₁ + bᵢ − b̂ᵢ.  (13)–(14)

que es la ecuación (12). (c.q.d.)

La ecuación (12) separa tres contribuciones que pueden resultar indistinguibles en una salida escalar terminal: el defecto heredado KᵢΔᵢ₋₁, el desajuste entre transductores Θᵢ y el defecto local o interfacial εᵢ.

Para k ≤ n, definimos

Kₙ:ₖ := KₙKₙ₋₁⋯Kₖ,  (15)

con Kₙ:ₙ₊₁ igual a la identidad sobre 𝓜ₙ como convención para el producto vacío. Esta identidad se introduce exclusivamente para uniformar las fórmulas de propagación; no representa un transductor físico adicional desde Dₙ hacia un dominio ulterior.

**Teorema 1 (Identidad de propagación ordinal).** Para una cadena de n transferencias prescritas,

**Δₙ = Kₙ:₁Δ₀ + Σₖ₌₁ⁿ Kₙ:ₖ₊₁(Θₖ + εₖ).**  (16)

**Demostración.** El caso n = 1 es el lema 1. Si la ecuación (16) es válida para n, al sustituirla en la ecuación (12) para n + 1 se obtiene, en una sola expresión,

Δₙ₊₁ = Kₙ₊₁:₁Δ₀ + Σₖ₌₁ⁿ Kₙ₊₁:ₖ₊₁(Θₖ + εₖ) + (Θₙ₊₁ + εₙ₊₁).  (17)–(18)

que es la fórmula requerida. (c.q.d.)

Las recurrencias generadas por desajustes de operadores y errores de transferencia están bien establecidas en análisis numérico y en estudios de especificación incorrecta de modelos [8, 9, 14]. Por ello, la ecuación (16) no se presenta por sí sola como una reivindicación de novedad. Aquí proporciona la identidad de propagación necesaria para los resultados sobre clases de medida que siguen.

## IV. Conversión entre clases de medida y error irreducible del modelo

Para un transductor especificado Kᵢ, definimos sus cuatro bloques respecto de las bandas:

𝕂ᵢ = [[PᵢᵃKᵢPᵢ₋₁ᵃ, PᵢᵃKᵢPᵢ₋₁ˢ], [PᵢˢKᵢPᵢ₋₁ᵃ, PᵢˢKᵢPᵢ₋₁ˢ]].  (19)

Los bloques no diagonales cuantifican la conversión entre las clases regular y singular seleccionadas por las medidas de referencia declaradas. Denotamos

Cᵢ^{a→s} := PᵢˢKᵢPᵢ₋₁ᵃ,   Cᵢ^{s→a} := PᵢᵃKᵢPᵢ₋₁ˢ.  (20)

Los operadores que preservan bandas y los que las preservan aproximadamente cuentan con una literatura operatoria consolidada [12, 13]. Utilizamos la descomposición en bandas no para redefinir esas clases, sino para identificar una clase física de salida que el modelo no representa.

Fijemos una entrada regular ν ∈ 𝒜ᵢ₋₁ y sea y := Kᵢν. Para el teorema 2, sea ∅ ≠ ℜᵢ(ν) ⊆ 𝒜ᵢ un *conjunto admisible de salidas exclusivamente regulares*: toda salida del modelo admitida para esa entrada fija pertenece a la banda absolutamente continua. Se emplea deliberadamente un conjunto de salidas, en lugar de una clase de operadores, para no exigir que los modelos admisibles posean una parametrización global determinada. Si el modelo admite una componente singular sometida a restricciones independientes, el certificado pertinente es el resultado de dos clases del teorema 3.

**Teorema 2 (Obstrucción irreducible por conversión entre clases).** Sea ν ∈ 𝒜ᵢ₋₁ y sea ∅ ≠ ℜᵢ(ν) ⊆ 𝒜ᵢ un conjunto que contenga toda salida admisible del modelo para esa entrada. Entonces

**distTV(Kᵢν, ℜᵢ(ν)) = ‖Cᵢ^{a→s}ν‖TV + distTV(PᵢᵃKᵢν, ℜᵢ(ν)).**  (21)

En consecuencia,

**distTV(Kᵢν, ℜᵢ(ν)) ≥ ‖Cᵢ^{a→s}ν‖TV.**  (22)

Si PᵢᵃKᵢν pertenece a la clausura de ℜᵢ(ν) en la norma de variación total, entonces

**distTV(Kᵢν, ℜᵢ(ν)) = ‖Cᵢ^{a→s}ν‖TV.**  (23)

**Demostración.** Como ν es regular,

Kᵢν = PᵢᵃKᵢν + Cᵢ^{a→s}ν.  (24)

Para cualquier r ∈ ℜᵢ(ν) ⊆ 𝒜ᵢ, la diferencia PᵢᵃKᵢν − r es absolutamente continua respecto de mᵢ, mientras que Cᵢ^{a→s}ν es singular. Por tanto, la ecuación (6) da

‖Kᵢν − r‖TV = ‖PᵢᵃKᵢν − r‖TV + ‖Cᵢ^{a→s}ν‖TV.  (25)

El término singular es independiente de r, de modo que infᵣ[c + f(r)] = c + infᵣ f(r), con c = ‖Cᵢ^{a→s}ν‖TV. Al tomar el ínfimo sobre r se obtiene la ecuación (21); no se requiere que ℜᵢ(ν) sea convexo o cerrado, ni que el ínfimo se alcance. Las restantes afirmaciones se siguen inmediatamente. (c.q.d.)

El teorema 2 proporciona el primer certificado de clausura no trivial. Distingue una aproximación deficiente *dentro* de la clase regular de la incapacidad de la clase de modelos para representar una salida singular físicamente requerida. Esta última impone una cota mínima de error distinta de cero incluso cuando la componente regular puede aproximarse con precisión arbitraria.

Existe un enunciado simétrico para una entrada singular cuando la clase admisible de salidas se restringe a 𝒮ᵢ, sustituyendo Cᵢ^{a→s} por Cᵢ^{s→a}.

El mismo mecanismo se aplica a una medida física general y a clases admisibles separadas.

**Teorema 3 (Descomposición exacta del mejor error de composición).** Sea μ = μᵃ + μˢ ∈ 𝓜ᵢ, sean ∅ ≠ 𝔄 ⊆ 𝒜ᵢ y ∅ ≠ 𝔖 ⊆ 𝒮ᵢ. Definimos su suma de Minkowski mediante 𝔄 + 𝔖 := {a + s : a ∈ 𝔄, s ∈ 𝔖}. Entonces

**distTV(μ, 𝔄 + 𝔖) = distTV(μᵃ, 𝔄) + distTV(μˢ, 𝔖).**  (26)

**Demostración.** Para todo a ∈ 𝔄 y s ∈ 𝔖,

(μᵃ − a) ⟂ (μˢ − s),  (27)

de modo que

‖μ − a − s‖TV = ‖μᵃ − a‖TV + ‖μˢ − s‖TV.  (28)

Las variables a y s son independientes; por consiguiente, el ínfimo de la suma es la suma de los dos ínfimos. (c.q.d.)

La ecuación (26) motiva un certificado de clausura con dos componentes:

𝔠ᵢ(μ; 𝔄, 𝔖) := (distTV(μᵃ, 𝔄), distTV(μˢ, 𝔖)).  (29)

Puede seguir informándose una norma escalar, pero la ecuación (29) impide que los defectos regular y singular queden ocultos dentro de un agregado indiferenciado.

## V. Omisiones positivas y persistencia a lo largo de una cadena de dominios

Los términos residuales Θᵢ + εᵢ no tienen por qué ser positivos. El desajuste entre transductores puede generar un error con signo. Existe, sin embargo, un caso particular de especial importancia: aquel en el que el modelo se limita a omitir una contribución física no negativa.

**Definición 3 (Transductor positivo y conservador de masa).** Un operador lineal acotado K: 𝓜(X) → 𝓜(Y) es positivo y conserva la masa si

η ≥ 0 ⇒ Kη ≥ 0,   (Kη)(Y) = η(X).  (30)

Para medidas positivas, esto implica ‖Kη‖TV = ‖η‖TV.

**Teorema 4 (Acumulación exacta de omisiones positivas).** Supóngase Δ₀ = 0. Sea

dₖ := Θₖ + εₖ ≥ 0  (31)

para k = 1,…,n, y supóngase que todo Kᵢ es positivo y conserva la masa. Entonces

Δₙ = Σₖ₌₁ⁿ Kₙ:ₖ₊₁ dₖ ≥ 0  (32)

y

**‖Δₙ‖TV = Σₖ₌₁ⁿ ‖dₖ‖TV.**  (33)

En particular,

**Δₙ = 0 ⇔ dₖ = 0 para todo k.**  (34)

**Demostración.** La ecuación (32) se sigue de la ecuación (16) y de la positividad. La norma de variación total de una medida positiva coincide con su masa total. Toda composición Kₙ:ₖ₊₁ es positiva y conserva la masa; por tanto,

‖Δₙ‖TV = Δₙ(Xₙ) = Σₖ₌₁ⁿ (Kₙ:ₖ₊₁dₖ)(Xₙ) = Σₖ₌₁ⁿ dₖ(Xₖ) = Σₖ₌₁ⁿ ‖dₖ‖TV.  (35)–(37)

La ecuación (34) se sigue de que todos los sumandos son no negativos. (c.q.d.)

**Corolario 1 (Omisión homogénea).** Si ‖dₖ‖TV = e para todo k, entonces

‖Δₙ‖TV = ne.  (38)

Si la misma transferencia se replica sobre N cantidades declaradas iguales, la proporcionalidad lineal da Nne.

Este resultado proporciona hipótesis explícitas bajo las cuales la acumulación lineal de contenido físico omitido es exacta. No se aplica a un desajuste arbitrario del modelo con signo, caso en el que pueden producirse cancelaciones.

Para describir la persistencia de una omisión singular utilizamos una clase más restrictiva de transductores posteriores.

**Definición 4 (Transductor fiel a las bandas).** Un transductor Kᵢ es fiel a las bandas respecto del par (mᵢ₋₁, mᵢ) si

Kᵢ𝒜ᵢ₋₁ ⊆ 𝒜ᵢ,   Kᵢ𝒮ᵢ₋₁ ⊆ 𝒮ᵢ.  (39)

Es isométrico sobre la banda singular si

‖Kᵢσ‖TV = ‖σ‖TV para todo σ ∈ 𝒮ᵢ₋₁.  (40)

**Teorema 5 (Persistencia de un residuo singular no corregido).** Sea exactamente

ηₖ := PₖˢΔₖ ∈ 𝒮ₖ  (41)

la componente singular del residuo en Dₖ. Supóngase que, para j = k + 1,…,n, los transductores Kⱼ son fieles a las bandas e isométricos sobre la banda singular, y que todo defecto inyectado posteriormente dⱼ := Θⱼ + εⱼ es regular, es decir, Pⱼˢdⱼ = 0. Entonces

PₙˢΔₙ = Kₙ:ₖ₊₁^{ss} ηₖ,  (42)

donde Kⱼ^{ss} := PⱼˢKⱼPⱼ₋₁ˢ, y

**‖PₙˢΔₙ‖TV = ‖ηₖ‖TV.**  (43)

En consecuencia, las correcciones restringidas a bandas regulares posteriores no pueden cancelar el residuo singular transportado.

**Demostración.** Proyectemos la ecuación (12) sobre la banda singular. La fidelidad a las bandas da PⱼˢKⱼPⱼ₋₁ᵃ = 0, mientras que la hipótesis Pⱼˢdⱼ = 0 elimina toda inyección singular posterior. Por tanto,

PⱼˢΔⱼ = Kⱼ^{ss}Pⱼ₋₁ˢΔⱼ₋₁  (44)

para j = k + 1,…,n. La iteración demuestra la ecuación (42), y la aplicación sucesiva de la isometría sobre la banda singular demuestra la ecuación (43). Una corrección posterior perteneciente a 𝒜ⱼ sigue siendo regular bajo transductores posteriores fieles a las bandas y, por ello, no puede cancelar la componente singular. (c.q.d.)

El teorema 5 es deliberadamente condicional. Los transductores físicos pueden convertir legítimamente la clase de medida; cuando lo hacen, los bloques no diagonales de la ecuación (19) deben conservarse en lugar de anularse por definición. Los bancos de prueba con agua de la sección VII no invocan fidelidad a las bandas ni isometría singular: el banco de prueba de cambio de fase utiliza el conjunto admisible de salidas exclusivamente regulares del teorema 2, mientras que el banco de prueba de volumen aísla el término de desajuste entre transductores Θᵢ de la ecuación (12).

## VI. Insuficiencia del balance escalar terminal

Un diagnóstico habitual consiste en considerar el total escalar del residuo. Definimos

Bᵢ(η) := η(Xᵢ).  (45)

Para residuos positivos, Bᵢ(η) = 0 implica η = 0. Para residuos con signo, la implicación falla.

**Proposición 1 (El balance escalar terminal no es un certificado de clausura).** Existen Δ ≠ 0, con Δ ∈ 𝓜ᵢ, tales que

Bᵢ(Δ) = 0.  (46)

Más concretamente, si

Δ = Δᵃ + Δˢ,   Δᵃ(Xᵢ) = −Δˢ(Xᵢ) ≠ 0,  (47)

entonces

Bᵢ(Δ) = 0  (48)

mientras que

**‖Δ‖TV = ‖Δᵃ‖TV + ‖Δˢ‖TV > 0.**  (49)

**Demostración.** La ecuación (48) se sigue de la ecuación (47). Las componentes son mutuamente singulares por construcción, por lo que la ecuación (49) se sigue de la ecuación (6). (c.q.d.)

Así, un escalar terminal correcto puede coexistir con un residuo no nulo resuelto por clases. El balance escalar aplica un espacio residual de dimensión infinita sobre un único número y, por tanto, descarta información.

## VII. Bancos de prueba físicos basados en el agua

Los resultados matemáticos pueden ilustrarse mediante un sistema físico familiar sin introducir nuevas constantes termodinámicas. El banco numérico que sigue utiliza los valores comunicados anteriormente en la Ref. [1]. NIST proporciona de manera independiente datos de referencia estándar sobre termoquímica del agua y cambios de fase, incluida la región de ebullición normal utilizada para identificar la frontera de fase externa [15].

### A. Calor latente como contribución singular irreducible

Consideremos un mol de agua calentado aproximadamente a presión constante desde 25 °C hasta la región de ebullición normal y, a continuación, vaporizado. Representamos este recorrido declarado mediante una medida de incremento etiquetada por la coordenada externa de temperatura

I = [298,15; 373,15] K  (50)

y la medida de referencia m = dT. Para un valor ilustrativo constante de la capacidad calorífica

Cₚ = 75,3 J mol⁻¹ K⁻¹,  (51)

la contribución sensible es

μᵃ = Cₚ dT,  (52)

con total

μᵃ(I) = 5,6475 kJ mol⁻¹.  (53)

Sea la contribución latente

μˢ = Lδ_Tb,   L = 40,65 kJ mol⁻¹.  (54)

La medida de incremento del recorrido idealizado es, por tanto,

μ = Cₚ dT + Lδ_Tb.  (55)

El átomo situado en T_b registra el incremento latente en la frontera de fase a lo largo de este recorrido prescrito; no afirma que la entalpía de equilibrio bifásico sea una función ordinaria univaluada de la temperatura en T_b. La temperatura actúa únicamente como coordenada externa utilizada para parametrizar este banco de prueba; ninguno de los resultados de clausura la requiere como variable primitiva.

Definamos la clase admisible de salidas exclusivamente regulares por

ℜ_reg(I) := {f(T)dT : f ∈ L¹(I)}.  (56)

El teorema 2 da

**distTV(μ, ℜ_reg(I)) = L = 40,65 kJ mol⁻¹,**  (57)

porque la parte regular CₚdT es admisible por sí misma. Ningún refinamiento de una representación exclusivamente regular puede eliminar la cota mínima de error singular mientras la clase de modelos excluya la contribución de Dirac.

El banco de prueba completo da

Q_tot = 5,6475 + 40,65 = 46,2975 kJ mol⁻¹,  (58)

por lo que la contribución omitida del cambio de fase es

40,65 / 46,2975 = 0,8780171716…  (59)

o, aproximadamente, el 87,80 % de la transferencia energética completa declarada.

Impongamos ahora de manera artificial el balance escalar terminal, manteniéndonos en la clase de medida incorrecta. Sea r ∈ L¹(I) tal que

∫_I r(T)dT = L  (60)

y definamos

μ̂ = (Cₚ + r(T))dT.  (61)

Entonces

μ̂(I) = μ(I),  (62)

de modo que el balance energético terminal es exacto. Sin embargo,

Δ = μ − μ̂ = Lδ_Tb − r(T)dT.  (63)

Como ambos términos son mutuamente singulares,

‖Δ‖TV = L + ∫_I |r(T)|dT.  (64)

Por la ecuación (60),

∫_I |r(T)|dT ≥ L,  (65)

con igualdad siempre que r ≥ 0 casi por doquier. Por tanto,

**μ(I) = μ̂(I), pero ‖μ − μ̂‖TV ≥ 2L = 81,30 kJ mol⁻¹.**  (66)

Este es un caso de balance escalar terminal en un banco de prueba físico: preservar el total energético final mediante la redistribución del calor latente en el canal regular no preserva la descomposición física a través de la frontera de fase.

El enunciado no constituye una crítica de los métodos de entalpía que regularizan explícitamente una transición de fase y demuestran convergencia en una topología elegida. Tales métodos declaran un problema de aproximación distinto. La ecuación (66) se refiere a la clausura exacta respecto de la representación regular/singular prescrita.

### B. Banco de prueba de desajuste puro entre transductores

La misma prepublicación comparó también el volumen molar del líquido con un contraste de vapor de gas ideal. Esto puede representarse mediante un dominio degenerado de un solo punto, para el cual 𝓜({*}) ≃ ℝ. En las condiciones de referencia declaradas, sea el transductor verdadero de contraste el que aplica la cantidad de sustancia n al volumen de gas ideal, mientras que el transductor desajustado conserva el volumen molar del líquido.

Los volúmenes molares de referencia son

v_liq = 0,018068636684 L mol⁻¹,  (67)  
v_vap = 30,619706 L mol⁻¹.  (68)

Definamos K(n) = v_vap n y K̂(n) = v_liq n. Sin término fuente adicional, el desajuste entre los coeficientes de los operadores es

**|v_vap − v_liq| = 30,601637363316 L mol⁻¹.**  (69)

Para la entrada especificada n = 1 mol, esto corresponde a un residuo de salida de 30,601637363316 L. Respecto de la salida del contraste de gas ideal, el valor líquido conservado por el transductor subestima aproximadamente en

99,9409902 %.  (70)

La comparación con el gas ideal no se presenta como un modelo exacto del vapor de agua real. Su finalidad es mostrar que el dominio y el transductor deben especificarse de manera coherente. Este segundo banco de prueba aísla Θᵢ del defecto singular de fuente εᵢ del ejemplo de cambio de fase.

## VIII. Relación con marcos matemáticos y computacionales consolidados

La presente construcción se apoya deliberadamente en matemáticas consolidadas. Por ello, la reivindicación de novedad se restringe al certificado de clausura combinado y no a sus ingredientes.

Chen, Ziemer y Torres desarrollaron rigurosamente leyes de balance con valores en medidas y trazas normales para campos cuya divergencia es una medida [3]. En el problema de acoplamiento de las ecuaciones de Euler de Ambroso *et al.* aparece explícitamente un acoplamiento interfacial con una fuente de Dirac que modeliza una pérdida de presión prescrita [4]. Estos trabajos establecen que las medidas singulares son objetos físicos naturales y no un artificio introducido para el ejemplo del agua.

Las energías volumétricas e interfaciales son clásicas en la teoría de deformaciones estructuradas. Choksi y Fonseca proporcionaron una representación integral que separa densidades de energía volumétrica e interfacial [5], y la teoría reciente de deformaciones estructuradas con valores en medidas amplía este marco a componentes difusas y singulares de medida [6]. En consecuencia, no se reivindica aquí novedad alguna por la existencia de contribuciones físicas volumétricas y singulares separadas.

La teoría *a posteriori* para la descomposición de operadores separa desde hace tiempo los efectos de discretización de los componentes, los errores de transferencia y los efectos de acoplamiento [7–9]. Del mismo modo, los residuos energéticos en interfaces de cosimulación cuantifican el error de acoplamiento entre simuladores [10, 11]. Estos enfoques suelen estar ligados a la aproximación numérica o a la cosimulación dependiente del tiempo, mientras que la construcción presente comprueba la clausura sobre una sucesión ordinal de dominios físicos antes de introducir cualquier esquema de avance temporal.

El desajuste de operadores constituye también un ámbito consolidado y amplio. Con una notación particularmente próxima, González *et al.* estudian el filtrado no lineal bajo especificación incorrecta del modelo mediante operadores predictivos verdaderos K_t y operadores perturbados K̂_t, y obtienen una propagación del error controlada por contracción y por la discrepancia acumulada del modelo [14]. Esa prepublicación fue presentada el 13 de julio de 2026, después de la prepublicación física del 27 de mayo que motivó el presente trabajo; no obstante, la recurrencia explícita de operadores desarrollada aquí es trabajo nuevo y no se retrotrae a la prepublicación anterior. Ambos trabajos abordan problemas distintos: el artículo sobre filtrado es probabilístico y está indexado por el tiempo; el presente artículo formula un certificado de clausura no probabilístico sobre una cadena ordinal de dominios físicos.

Por último, la estabilidad de los operadores que preservan bandas y de los que preservan disjunción forma parte de la teoría establecida de retículos de Banach [12, 13]. No se reivindica una nueva teoría de operadores que preservan bandas. El uso que se hace aquí es más restringido: las bandas de Lebesgue proporcionan una descomposición físicamente interpretable en la que una clase admisible de modelos puede excluir una clase de salida requerida, y la variación total proporciona entonces un error irreducible exacto.

La contribución combinada consta de cuatro partes: (i) una descomposición exacta del residuo en error heredado, desajuste entre transductores y defecto de fuente local; (ii) un certificado de conversión entre clases regular y singular con una cota mínima irreducible del error en variación total; (iii) propagación ordinal con acumulación exacta de omisiones positivas; y (iv) una demostración de que el balance escalar terminal puede ser exacto aun cuando la composición del modelo no clausure.

## IX. Métodos: búsqueda bibliográfica y verificación de las afirmaciones

Antes de fijar las principales afirmaciones de este trabajo se realizó una búsqueda bibliográfica dirigida y una evaluación de novedad. La búsqueda combinó buscadores académicos públicos en la web, arXiv, literatura primaria alojada por las editoriales y repositorios de código fuente cuando los detalles de implementación podían ser relevantes. Los términos de búsqueda se ampliaron iterativamente desde los objetos matemáticos exactos utilizados aquí hacia sus antecedentes consolidados más próximos, entre ellos: leyes de balance con valores en medidas; fuentes singulares e interfaciales; descomposiciones volumen-superficie; operadores que preservan bandas y disjunción; desajuste de operadores y de modelos; errores de acoplamiento y transferencia; residuos de cosimulación; y propagación de discrepancias a través de dominios acoplados. Cuando los artículos pertinentes identificaban antecedentes fundamentales, se siguieron retrospectivamente sus referencias.

La búsqueda identificó una teoría previa sustancial para cada uno de los ingredientes individuales, que se cita expresamente. En particular, el presente artículo no reivindica novedad para las leyes de balance con medidas de Radon, la descomposición de Lebesgue, las fuentes singulares de interfaz, la descomposición de energía volumen-superficie, los operadores que preservan bandas ni la propagación genérica del desajuste entre operadores. Dentro de la bibliografía identificada mediante esta búsqueda, no se encontró una formulación anterior que combine esos ingredientes en el certificado específico de clausura entre dominios desarrollado aquí: separación simultánea del residuo heredado, el desajuste entre transductores y el defecto local o interfacial; descomposición por clases de medida regular y singular; una cota mínima irreducible de error por conversión entre clases; propagación ordinal del residuo resultante sin adoptar el tiempo como primitiva; y demostración de que un balance escalar terminal exacto no tiene por qué implicar la clausura de la composición física. La reivindicación de novedad se restringe a esta construcción combinada y a los resultados demostrados para ella.

La revisión bibliográfica y las pruebas formales de resistencia siguieron un procedimiento deliberadamente conservador: se eliminaron las afirmaciones candidatas siempre que una construcción publicada las subsumiera o cuando sus hipótesis fallaran en el modelo físico examinado.

## X. Alcance y limitaciones

El alcance del marco se limita deliberadamente.

En primer lugar, los transductores Kᵢ son operadores lineales acotados sobre espacios de medidas finitas con signo. Las relaciones constitutivas no lineales solo pueden representarse una vez fijados los parámetros externos que definen una transferencia concreta, o mediante una familia de operadores dependiente del estado. Extender el certificado de clausura a aplicaciones genuinamente no lineales sin perder la identidad exacta de distancia entre clases constituye un problema distinto.

En segundo lugar, «regular» y «singular» se entienden siempre respecto de una medida de referencia declarada mᵢ. La singularidad respecto de mᵢ no identifica por sí sola una interfaz. La interpretación física de una componente singular debe proceder de la especificación del dominio. A la inversa, una contribución de interfaz con significado físico puede regularizarse deliberadamente en un método numérico; ese método debe juzgarse en la topología y la clase de aproximación que declara, no frente a una representación singular exacta que no fue concebido para preservar.

En tercer lugar, la acumulación exacta del teorema 4 requiere omisiones positivas y transductores positivos que conserven la masa. Los errores de transducción con signo pueden cancelarse en totales escalares y pueden contraerse o amplificarse bajo aplicaciones posteriores. La afirmación general es la ecuación (16), no la ecuación (33).

En cuarto lugar, los ejemplos con agua son bancos de prueba, no una nueva ecuación de estado. El valor de la capacidad calorífica se mantiene constante únicamente para reproducir de forma transparente el valor de referencia 5,6475 kJ mol⁻¹ a lo largo de 75 K. El ejemplo del volumen de vapor se formula expresamente como contraste de gas ideal. Ninguna de estas aproximaciones se utiliza para inferir nuevas propiedades del agua.

Por último, el marco no es probabilístico. Las medidas con signo se utilizan como portadoras matemáticas de incrementos y defectos físicos. Un dominio externo puede emplear una medida de probabilidad cuando corresponda, pero ninguno de los teoremas de este artículo exige probabilidad. Del mismo modo, el índice de dominio i no es una coordenada temporal.

## XI. Conclusión

Un modelo físico acoplado puede ser localmente correcto y satisfacer su balance escalar terminal y, sin embargo, estar compuesto de forma incorrecta. La discrepancia puede proceder de tres fuentes distintas: un residuo heredado, un transductor desajustado o una contribución local ausente. Cuando los incrementos físicos se representan mediante medidas de Radon con signo, la descomposición regular/singular proporciona un segundo diagnóstico: una clase de modelos restringida a una clase de medida no puede reproducir una componente físicamente requerida de la otra clase sin modificar su representación admisible.

El resultado central es la identidad de conversión entre clases de la ecuación (21). Esta identifica una cota mínima exacta del error en variación total asociada a una clase de medida ausente y separa esa contribución del error ordinario de aproximación dentro de la clase. En cadenas de dominios con transductores positivos que conservan la masa, las omisiones locales positivas se acumulan exactamente, ecuación (33), y bajo transferencias posteriores fieles a las bandas persiste un residuo singular no corregido. El balance escalar terminal es una condición más débil: los defectos regular y singular con signo pueden cancelarse en el total y seguir siendo no nulos en variación.

El banco de prueba del cambio de fase del agua concreta esta distinción. La omisión de la contribución latente deja un error irreducible exacto de 40,65 kJ mol⁻¹ respecto de modelos exclusivamente regulares. La redistribución de esa misma energía mediante el canal regular hace exacto el total energético final, pero deja al menos 81,30 kJ mol⁻¹ de residuo en variación total. Por tanto, un número final correcto no certifica por sí solo una composición física correcta.

En consecuencia, la contribución consiste en un marco diagnóstico para modelos físicos modulares, no en una nueva teoría de la descomposición de Lebesgue ni de los operadores que preservan bandas. El procedimiento es: especificar los dominios, los transductores, los términos fuente y las medidas de referencia; calcular el residuo mediante la ecuación (12); resolverlo por clase de medida; y determinar si la clausura terminal aparente supera este certificado más exigente.

## Agradecimientos

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para la localización bibliográfica, la comprobación adversarial de coherencia, la estructuración del manuscrito, la asistencia en la formalización matemática y la composición tipográfica, y la edición en lengua inglesa. Grok 4.5 (xAI; interacción del 8 de agosto de 2026) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias sobre presentación y enfoque. DeepSeek-R1 (DeepSeek AI) contribuyó a la revisión adversarial y a la comprobación de coherencia formal del manuscrito. Todas las salidas de IA se trataron como materiales auxiliares de investigación sin carácter de autoridad científica. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume la plena responsabilidad del manuscrito presentado.

## Declaraciones del autor

### Conflicto de intereses

El autor declara no tener conflictos de intereses.

### Aprobación ética

No fue necesaria aprobación ética, ya que este estudio no incluyó participantes humanos ni animales.

### Contribuciones del autor

Juan Antonio Lloret Egea: conceptualización; análisis formal; investigación; metodología; administración del proyecto; validación; redacción del borrador original; revisión y edición del manuscrito.

## Disponibilidad de los datos

No se generaron nuevos conjuntos de datos. Todos los valores numéricos empleados en los cálculos de los bancos de prueba figuran en el artículo y se atribuyen a las fuentes citadas.

## Referencias

1. J. A. Lloret Egea, «El origen material ordinario del universo observable y la relación entre física contemporánea y Sistema Vectorial SV en el tránsito por dominios: errores de plano, contraste entre aparatos y continuidad H–He de la materia ordinaria», prepublicación, 27 de mayo de 2026, doi:10.21428/39829d0b.90fce13d.

2. G. B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed. (Wiley, New York, 1999).

3. G.-Q. Chen, W. P. Ziemer y M. Torres, «Gauss–Green theorem for weakly differentiable vector fields, sets of finite perimeter, and balance laws», *Commun. Pure Appl. Math.* **62**, 242–304 (2009), doi:10.1002/cpa.20262.

4. A. Ambroso, C. Chalons, F. Coquel y T. Galié, «Interface model coupling via prescribed local flux balance», *ESAIM Math. Model. Numer. Anal.* **48**, 895–918 (2014), doi:10.1051/m2an/2013125.

5. R. Choksi e I. Fonseca, «Bulk and interfacial energy densities for structured deformations of continua», *Arch. Rational Mech. Anal.* **138**, 37–103 (1997), doi:10.1007/s002050050036.

6. S. Krömer, M. Kružík, M. Morandotti y E. Zappale, «Measure-valued structured deformations», *J. Nonlinear Sci.* **34**, 100 (2024), doi:10.1007/s00332-024-10076-w.

7. D. Estep, S. Tavener y T. Wildey, «A posteriori analysis and improved accuracy for an operator decomposition solution of a conjugate heat transfer problem», *SIAM J. Numer. Anal.* **46**, 2068–2089 (2008), doi:10.1137/060678737.

8. V. Carey, D. Estep y S. Tavener, «A posteriori analysis and adaptive error control for multiscale operator decomposition solution of elliptic systems I: Triangular systems», *SIAM J. Numer. Anal.* **47**, 740–761 (2009), doi:10.1137/070689917.

9. D. Estep, V. Ginting, D. Ropp, J. N. Shadid y S. Tavener, «An a posteriori–a priori analysis of multiscale operator splitting», *SIAM J. Numer. Anal.* **46**, 1116–1146 (2008), doi:10.1137/07068237X.

10. S. S. Sadjina y E. Pedersen, «Energy conservation and coupling error reduction in non-iterative co-simulations», arXiv:1606.05168 (2016), doi:10.48550/arXiv.1606.05168.

11. S. S. Sadjina, L. T. Kyllingstad, E. Pedersen y S. Skjong, «Energy conservation and power bonds in co-simulations: Non-iterative adaptive step size control and error estimation», arXiv:1602.06434 (2016), doi:10.48550/arXiv.1602.06434.

12. T. Oikhberg y P. Tradacete, «Almost band preservers», *Positivity* **21**, 1393–1423 (2017), doi:10.1007/s11117-017-0475-z.

13. T. Oikhberg y P. Tradacete, «Almost disjointness preservers», *Can. J. Math.* **69**, 650–686 (2017), doi:10.4153/CJM-2016-020-x.

14. F. González, Ö. D. Akyildiz, D. Crisan y J. Míguez, «An operator-theoretic analysis of nonlinear filtering under model misspecification», arXiv:2607.11378 (presentado el 13 de julio de 2026), doi:10.48550/arXiv.2607.11378.

15. National Institute of Standards and Technology, «Water», *NIST Chemistry WebBook*, Standard Reference Database 69 (consultado el 11 de agosto de 2026), https://webbook.nist.gov/chemistry/.
