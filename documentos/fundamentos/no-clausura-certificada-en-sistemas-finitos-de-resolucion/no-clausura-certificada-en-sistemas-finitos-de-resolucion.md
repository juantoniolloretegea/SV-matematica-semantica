# No clausura certificada en sistemas finitos de resolución: certificados operativos, morfismos conservativos y complejidad de revisión

**Juan Antonio Lloret Egea**
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), España
ORCID: 0000-0002-6634-3351

**PREPRINT - NO REVISADO POR PARES**
Versión española previa a revisión editorial y por pares. 8 de agosto de 2026.

## Resumen

Los formalismos trivalentes pueden confundir una resolución aún no concluida con un resultado no binario ya completado. Estudiamos sistemas finitos de resolución en los que ambos estados quedan separados mediante certificados explícitos. Para cada coordenada, un grafo finito etiquetado dispone de clases terminales binarias. Un certificado exacto de alcanzabilidad demuestra que un conjunto propuesto coincide precisamente con el subgrafo alcanzable; su perfil de clausura produce un conjunto unitario binario o un perfil no unitario certificado. Demostramos la preservación y la reflexión de los perfiles de clausura bajo morfismos de recubrimiento de resolución con levantamiento de caminos. Los estados completados con soporte forman entonces sistemas deterministas de revisión. Una equivalencia de tipo Nerode proporciona la memoria mínima exacta de revisión, y las fronteras de soporte de un paso son exactas bajo un criterio de congruencia derecha y separación futura. Demostramos además que los cambios conservativos de los resolvedores certificados subyacentes, cuando son compatibles con los incrementos de revisión, inducen un isomorfismo entre los cocientes mínimos de revisión alcanzables: los perfiles de clausura presentes y la memoria mínima de revisión futura son conjuntamente invariantes. La multiplicidad oculta de revisión se cuantifica después, sin hipótesis de independencia, a partir de las fibras de la aplicación de marco visible y, cuando la memoria de frontera es exacta, directamente a partir de la diversidad de fronteras. Como especialización se recupera una fórmula de producto independiente. El Sistema Vectorial (SV) se trata únicamente como una realización motivadora; su regla adicional de autorización humana para los registros soberanos de `U` queda fuera de los teoremas finitos generales.

**Palabras clave:** no clausura certificada; sistemas finitos de resolución; marcos ternarios; certificados de prueba; morfismos conservativos; equivalencia de Nerode; sistemas de revisión; historiales de solo adición

# Introducción

Introducir un tercer valor es matemáticamente barato y semánticamente costoso de justificar. En lógicas trivalentes y formalismos de verificación puede representar información parcial, una observación finita inconclusa, abstracción, inconsistencia o la imposibilidad de obtener un resultado binario. Todos estos usos son legítimos, pero responden a preguntas distintas. En particular, `“todavía no se ha producido una respuesta binaria”` no distingue entre trabajo inacabado y una conclusión ya completada según la cual el aparato de resolución admitido no sustenta una clausura binaria única.

La distinción importa siempre que se pretenda que el tercer valor sea auditable. Si un resolvedor puede emitir un tercer valor ante el primer caso difícil, la no clausura se vuelve indistinguible del esfuerzo incompleto. Si se le obliga a emitir `0` o `1` pese a que persistan alternativas admisibles no resueltas, la clausura se fabrica. El régimen estudiado aquí impone una secuencia más fuerte: `representación suficiente → resolución admitida completa → veredicto certificado.` El alfabeto visible sigue siendo `Σ = {0, 1, U}.` En la semántica finita general, la etiqueta `U` denota un episodio completado cuyo perfil de clausura certificado no es unitario. El trabajo pendiente es un estado del proceso de resolución, no un cuarto valor del marco completado. En la realización SV, específicamente, un perfil no unitario verificado es necesario pero no suficiente para un registro soberano de `U`: la autorización humana constituye una condición adicional de instancia.

La construcción se origina en las matemáticas ternarias y basadas en sucesos del Sistema Vectorial (SV), cuyos primeros preprints introdujeron células ternarias exactas, la no determinación actual `U`, horizontes de sucesos e historiales de reevaluación de solo adición [1, 2, 3]. El presente trabajo extrae únicamente el núcleo finito necesario y lo generaliza más allá de la familia de células cuadradas siempre que dicha estructura no desempeña ninguna función a nivel de teorema.

Las literaturas próximas ya proporcionan terceros valores para modelos parciales y observaciones finitas [7, 8, 9], condiciones que registran progreso de verificación incompleto [10], objetos de prueba comprobables de forma independiente [11], formalismos de soporte y revisión [12, 13], ocurrencias de sucesos [14] y minimización de Nerode [18]. En consecuencia, no se reivindica novedad por la mera ternariedad, la procedencia, el levantamiento de caminos o la minimización de máquinas de estados.

La contribución consiste, en cambio, en acoplar cuatro capas que pueden comprobarse de forma independiente.

Primero, la representación se selecciona con relación a una pregunta declarada. No se presume que un marco mayor resuelva más por el mero hecho de contener más coordenadas. La familia de células cuadradas `SV(b², b)` se conserva como especialización canónica, con `SV(9, 3)` como miembro fundacional, pero los teoremas operativos se formulan para conjuntos arbitrarios de parámetros finitos.

Segundo, la resolución se modeliza como un sistema dirigido finito. En lugar de definir el “agotamiento” mediante prosa, proporcionamos un certificado cuya verificación finita demuestra que un conjunto propuesto coincide exactamente con el espacio de resolución alcanzable. De este modo se obtiene una certificación simétrica de `0`, `1` y `U`.

Tercero, el cambio conservativo se formula mediante un morfismo con levantamiento de caminos. El teorema resultante preserva y refleja el perfil de clausura alcanzable; tales morfismos también se componen. Más importante aún, cuando los cambios conservativos de resolvedores locales conmutan con los incrementos de revisión admisibles, preservan y reflejan la equivalencia respecto de todos los futuros e inducen un isomorfismo entre los cocientes mínimos de revisión alcanzables.

Cuarto, la revisión se analiza sobre todos los incrementos futuros admisibles. Un cociente de tipo Nerode proporciona la memoria determinista mínima necesaria para preservar los marcos visibles futuros. Las fronteras de soporte de un paso son suficientes cuando su núcleo constituye una congruencia derecha estable y son mínimas cuando descriptores distintos son separables en el futuro. Esto produce una descomposición exacta por fibras de la memoria oculta de revisión sin hipótesis de independencia; la expresión producto anterior pasa a ser una especialización para coordenadas realizables de manera independiente.

Los principales resultados son, por tanto:

1.  un teorema de adecuación operativa para certificados exactos de alcanzabilidad finita, con coste lineal explícito de verificación para grafos explícitos;

2.  preservación, reflexión, composición y transporte de alcanzabilidad certificada mediante morfismos de recubrimiento de resolución;

3.  un teorema de invariancia que muestra que los cambios conservativos de resolvedor compatibles con la revisión inducen el mismo cociente mínimo de revisión alcanzable;

4.  un criterio bajo el cual las fronteras de soporte de un paso realizan ese cociente, incluido un certificado suficiente de minimalidad enteramente local, junto con una fórmula exacta por fibras/fronteras para la multiplicidad oculta de revisión; y

5.  una especialización de producto independiente que proporciona `∏_i(2 + r_i)` bajo realizabilidad completa del producto.

Estos resultados poseen interés independiente más allá de la instancia motivadora SV. En particular, identifican cuándo los cambios conservativos compatibles con la revisión de los resolvedores certificados subyacentes dejan invariantes tanto los perfiles de clausura presentes como el cociente mínimo de revisión respecto de todos los futuros, y descomponen la memoria determinista oculta de revisión por fibras del marco visible sin presuponer independencia entre coordenadas.

La capa de sucesos de solo adición se utiliza después como disciplina de registro: una reevaluación posterior se representa mediante un nuevo suceso, no mediante mutación del anterior. Una condición adicional de instancia SV reserva a actos autorizados por un humano tanto la constitución de un registro soberano de `U` a partir de un perfil no unitario certificado por máquina como cualquier conversión posterior de ese `U` registrado en un registro binario soberano. Estas condiciones de autoridad se mantienen separadas de los teoremas matemáticos generales.

# Dominios declarados y representaciones finitas suficientes

## Dominio declarado

Un dominio declarado `D` fija la ambición matemática de una evaluación. Tratamos `D` como primitivo y exigimos que determine, cuando sea necesario, un espacio factual `Ω_D`, una aplicación objetivo `Q_D : Ω_D → Z_D,` una familia de esquemas finitos de parámetros admisibles, las reglas que instancian sistemas de resolución a partir de estados de información, una clase `Δ_D` de incrementos externos admisibles y el criterio por el cual un estado terminal binario cuenta como clausura legítima.

La dirección de dependencia es importante: el dominio determina qué resulta pertinente. Un caso difícil no autoriza por sí mismo una ampliación retrospectiva de la pregunta ni de sus reglas de admisibilidad.

Un cambio en la información disponible bajo las mismas reglas se escribe `I ↦ I′`. Por el contrario, un cambio de la pregunta objetivo, de la familia de métodos admisibles, de la regla de clausura o de la política de representación es una revisión del dominio, escrita `D ⇝ D′.` Los teoremas de dominio fijo que siguen no identifican tácitamente estas dos operaciones.

## Suficiencia de un esquema finito de parámetros

Sea `P` un conjunto finito ordenado de parámetros y sea `π_(D, P) : Ω_D → {0, 1}^P` su firma binaria completamente resuelta. Esta aplicación es un dispositivo idealizado para comprobar suficiencia descriptiva; no es el marco ternario operativo producido con información limitada.

**Definición 2.1** (suficiencia del dominio). El esquema de parámetros `P` es suficiente para `D` cuando `π_(D, P)(ω) = π_(D, P)(ω′) ⇒ Q_D(ω) = Q_D(ω′)` para todo `ω, ω′ ∈ Ω_D`. Equivalentemente, existe `q_(D, P)` tal que `Q_D = q_(D, P) ∘ π_(D, P).`

El término suficiente se utiliza únicamente en este sentido de factorización y no guarda relación con la suficiencia estadística.

Supóngase que el dominio declara una familia ordenada de esquemas admisibles `𝔓_D` dotada de un preorden de refinamiento `≼_D`. Un esquema `P_D^⋆` es minimal suficiente dentro de la familia declarada cuando es suficiente y ningún esquema admisible estrictamente menor es suficiente. Un esquema mínimo suficiente en sentido global es una condición más fuerte: debe satisfacer `P_D^⋆≼_DP` para todo `P` suficiente. No se presupone en general ni la existencia ni la unicidad de un esquema minimal o mínimo suficiente; los resultados que se refieren a uno de ellos se aplican únicamente cuando la familia declarada ha proporcionado el objeto requerido.

## Especialización de células cuadradas SV

La arquitectura SV originaria utiliza el alfabeto ternario `Σ = {0, 1, U}` y una familia canónica escrita `SV(b², b), b ≥ 3,` cuyos marcos contienen `b²` coordenadas ordenadas [1]. La palabra vectorial se refiere a esta tupla ordenada; no se presupone estructura de espacio vectorial sobre un cuerpo.

Para un dominio cuyos esquemas admitidos sean precisamente estas células canónicas, defínase `b_D^⋆ := min {b ≥ 3 : P_(D, b) es suficiente para D}.` Entonces la célula canónica mínima suficiente es `SV((b_D^⋆)², b_D^⋆)`. El miembro fundacional es `SV(9, 3)`.

El criterio es de economía, no de compresión máxima. Un problema cuya descripción intrínseca utilice únicamente tres distinciones puede aun así asignarse a `SV(9, 3)` porque ese es el mínimo de la familia canónica. Una vez que un esquema canónico es suficiente para el par fijo `(D, Q_D)`, no puede justificarse un esquema mayor alegando que el esquema suficiente más pequeño perdió una distinción necesaria para determinar `Q_D`. Una célula mayor puede seguir eligiéndose por razones operativas, de interoperabilidad, redundancia o dominios futuros, pero esas razones son distintas de la suficiencia descriptiva para el objetivo inalterado.

**Proposición 2.2** (el refinamiento factorizado no añade información al nivel de la pregunta). Sean `P≼_DP′` y una reducción `ρ : {0, 1}^P′ → {0, 1}^P` tales que `π_(D, P) = ρ ∘ π_(D, P′).` Si `P` es suficiente para `D`, entonces `Q_D` factoriza a través de `ρ ∘ π_(D, P′)`. Por tanto, las distinciones eliminadas por `ρ` no pueden alterar `Q_D`.

Demostración. Como `P` es suficiente, `Q_D = q_(D, P) ∘ π_(D, P)`. Sustituyendo, `Q_D = q_(D, P) ∘ ρ ∘ π_(D, P′).` (c.q.d.)

La Proposición 2.2 es deliberadamente elemental. Su función es excluir un error de categoría antes de estudiar la no clausura: capacidad representacional y relevancia resolutiva no son la misma magnitud.

# Episodios finitos de resolución y certificados exactos

## Sistemas locales de resolución

Fijemos un dominio `D`, un estado de información `I` y una coordenada `i` de un esquema suficiente de parámetros. El trabajo de resolución admitido para esa coordenada se representa mediante un sistema dirigido finito etiquetado `ℛ = (X, 𝒜, →,x_*, T₀, T₁).` Aquí `X` es un conjunto finito de estados, `𝒜` es un alfabeto finito de acciones, `x_*` es el estado inicial de resolución y `→ ⊆ X × 𝒜 × X` es la relación interna de resolución. Los conjuntos `T₀, T₁ ⊆ X` son clases terminales de clausura disjuntas. Un estado de `T_v` significa que se han satisfecho las reglas de legitimidad del dominio para la clausura binaria `v`; el grafo puede codificar cálculos, búsquedas de demostraciones, mediciones, comparaciones u otros procedimientos admitidos antes de alcanzar tal estado.

El sistema finito puede ser el grafo literal de resolución o un cociente operativo finito cuya corrección esté suministrada por el dominio. No se afirma que los espacios de búsqueda infinitos admitan el certificado concreto desarrollado a continuación; las generalizaciones simbólicas quedan fuera del presente teorema.

Para `x ∈ X`, sea `Reach_ℛ(x)` el conjunto de estados alcanzables mediante un camino interno finito, incluido el propio `x`. Definimos el perfil de clausura alcanzable `C_ℛ(x) := {v ∈ {0, 1} : Reach_ℛ(x) ∩ T_v ≠ ∅}.` El veredicto semántico completado es `val_ℛ(x) = 0 si C_ℛ(x)={0}; 1 si C_ℛ(x)={1}; U si |C_ℛ(x)|≠1.` Las dos fuentes del valor visible `U` –ninguna clausura binaria alcanzable y más de una clausura binaria alcanzable– se mantienen deliberadamente sin separar en el alfabeto visible. Su procedencia permanece disponible en el certificado y puede presentar comportamientos futuros de revisión distintos.

La ecuación (1) es semántica, todavía no operativa. Un resolvedor no debe limitarse a afirmar que conoce el conjunto alcanzable completo. Exigimos, por ello, un certificado comprobable.

## Certificados exactos de alcanzabilidad

**Definición 3.1** (certificado exacto de alcanzabilidad). Un certificado exacto de alcanzabilidad para `(ℛ, x_*)` es una terna `χ = (R, d, p),` donde `R ⊆ X`, `d : R → ℕ` y, para todo `y ∈ R ∖ {x_*}`, `p(y) = (z_y, a_y) ∈ R × 𝒜,` que satisface:

1.  `x_* ∈ R` y `d(x_*) = 0`;

2.  para todo `y ≠ x_*` de `R`, `z_y -[a_y]→ y` y `d(z_y) < d(y)`;

3.  `R` está cerrado por sucesores: si `y ∈ R` y `y -[a]→ z`, entonces `z ∈ R`.

El verificador `Ver_ℛ(x_*, χ)` acepta exactamente cuando se cumplen estas condiciones finitas.

Los datos de padre y rango demuestran que todo elemento de `R` es realmente alcanzable. El cierre por sucesores demuestra que no se ha omitido ningún sucesor alcanzable.

**Proposición 3.2** (tamaño y coste de verificación). Supóngase que el sistema finito de transición se almacena explícitamente mediante listas de adyacencia, que la pertenencia a `R` está marcada y que cada registro de padre `p(y)` apunta a una entrada de transición real. Sea `E(R) := {(x, a, z) ∈ → : x ∈ R}.` Entonces los datos auxiliares del certificado `(d, p)` tienen tamaño `O(|R|)`, y las condiciones 1–3 de la Definición 3.1 pueden comprobarse en tiempo `O(|R| + |E(R)|).` Por tanto, el certificado es un objeto de auditoría, no una compresión asintótica de la alcanzabilidad finita explícita.

Demostración. Las comprobaciones del estado inicial y del rango son constantes o lineales en `|R|`. Cada estado no inicial aporta un registro de padre, que se comprueba una sola vez. El cierre por sucesores se verifica recorriendo cada transición cuyo origen pertenece a `R` y comprobando si su destino está marcado como miembro de `R`. No se requiere ningún otro recorrido del grafo. (c.q.d.)

``` text
x* (d=0)
├─[a1]→ a (d=1) ─[a3]→ ((t0, d=2)) ∈ T0
│          └─[a5, transición adicional]→ b (d=1)
└─[a2]→ b (d=1) ─[a4]→ ((t1, d=2)) ∈ T1

Aristas [a1]-[a4]: aristas de padre certificadas.
La transición [a5] también debe quedar cubierta por el cierre por sucesores.
```

**Figura 1.** Certificado exacto de alcanzabilidad ilustrativo. Las aristas de padre y los rangos decrecientes atestiguan la alcanzabilidad de todo miembro de R; el cierre por sucesores comprueba además cada transición saliente, incluida la arista no parental a → b. Los círculos dobles indican clases terminales binarias.

**Lema 3.3** (exactitud de un certificado aceptado). Si `Ver_ℛ(x_*, χ) = 1` para `χ = (R, d, p)`, entonces `R = Reach_ℛ(x_*).`

Demostración. Para `R ⊆ Reach_ℛ(x_*)`, ordénense los estados por rango. El estado inicial es alcanzable. Para cualquier `y ≠ x_*`, la aplicación reiterada de su padre disminuye estrictamente el rango no negativo y, por tanto, termina en `x_*`; concatenando las aristas de padre certificadas se obtiene un camino desde `x_*` hasta `y`.

Para la inclusión inversa, sea `x_* = x₀ → x₁ → ⋯ → x_k` un camino finito cualquiera. Como `x₀ ∈ R` y `R` está cerrado por sucesores, la inducción da `x_j ∈ R` para todo `j`. Por consiguiente, todo estado alcanzable pertenece a `R`. (c.q.d.)

**Teorema 3.4** (adecuación operativa de la certificación finita). Para todo sistema local finito de resolución `(ℛ, x_*)`:

1.  todo certificado exacto de alcanzabilidad aceptado determina exactamente el perfil semántico de clausura;

2.  existe al menos un certificado exacto de alcanzabilidad aceptado; y

3.  si el resolvedor operativo emite `σ ∈ Σ` únicamente después de verificar un certificado y calcular `σ` a partir del conjunto certificado mediante (1), entonces los veredictos operativos y semánticos completados coinciden.

Demostración. La parte 1 se sigue del Lema 3.3: el conjunto `R` del verificador coincide con el verdadero conjunto alcanzable, de modo que `{v : R ∩ T_v ≠ ∅} = C_ℛ(x_*).` Para la parte 2, tómese `R = Reach_ℛ(x_*)`. Como `X` es finito, elíjase para cada `y ∈ R` un camino más corto desde `x_*` hasta `y`; sea `d(y)` su longitud y regístrese en `p(y)` la arista final de uno de esos caminos. Se cumplen entonces las condiciones 1–2 de la Definición 3.1. El cierre por sucesores se sigue de la definición de alcanzabilidad. Por tanto, el certificado es aceptado. La parte 3 resulta de aplicar la misma aplicación determinista (1) al mismo perfil de clausura. (c.q.d.)

**Corolario 3.5** (el trabajo pendiente no es un episodio completado de no clausura certificada). Bajo el régimen de certificado exacto de este trabajo, no se emite ningún veredicto completado antes de aceptar un certificado exacto –u otro sistema de certificación demostrado capaz de establecer el mismo perfil exacto de clausura alcanzable con la misma garantía de completitud–. Por tanto, detener prematuramente la búsqueda no constituye un episodio completado de no clausura certificada. En particular, una exploración parcial puede haber atestiguado ya la alcanzabilidad de ambas clases terminales y, con ello, establecido la no unicidad de la clausura binaria; aun así, el presente régimen exige completar el episodio de certificación declarado antes de emitir la etiqueta `U` de la semántica finita general. En la realización SV se aplica después, además, la regla de autorización soberana.

En la semántica finita general, un perfil no unitario verificado se representa mediante la etiqueta `U`. La realización SV añade una capa ulterior de autoridad: el certificado verificable por máquina `η_U` establece el perfil, pero no crea por sí mismo un registro soberano de suceso que porte `U`; ese acto de registro requiere autorización humana, según se especifica en la Sección 10.2.

El teorema proporciona certificación simétrica. Un certificado cuyo perfil de clausura sea `{0}` puede denotarse `ζ₀`; uno cuyo perfil sea `{1}` puede denotarse `ζ₁`; y uno cuyo perfil tenga cardinalidad distinta de uno puede denotarse `η_U`. Estos nombres indican el veredicto verificado, no distintos estándares de prueba.

**Observación 3.6** (por qué la clausura binaria también necesita certificación). Un camino descubierto hasta `T₀` no demuestra por sí solo que `0` sea la única clausura legítima: puede quedar sin explorar un camino hasta `T₁`. El certificado exacto elimina la asimetría entre clausura binaria y no clausura al certificar el perfil completo de clausura alcanzable antes de emitir cualquier valor completado.

# Marcos ternarios tras la resolución certificada

Sea `P = {1, …, n}` un esquema finito suficiente de parámetros. Para cada coordenada `i`, instánciese un sistema local finito de resolución `ℛ_i` a partir del mismo dominio y del estado de información actual. Tras la certificación, defínase `S = (s₁, …, s_n) ∈ Σ^n, s_i = val_ℛ_i(x_*(i)).` Este es el marco ternario completado de la semántica finita general. En la realización SV, una coordenada clasificada computacionalmente mediante un perfil no unitario verificado se incorpora como `U` soberana únicamente tras el acto adicional de autorización especificado en la Sección 10.2.

Por tanto, un marco que contiene `U` no es un vector incompleto. Cada coordenada `U` descansa sobre un episodio finito de resolución admitida ya completado y sobre un certificado aceptado cuyo perfil de clausura no es unitario; en SV registra además la autorización soberana requerida.

El marco comprime deliberadamente la procedencia. Por ejemplo, los dos perfiles `C_ℛ(x_*) = ∅ y C_ℛ′(x_*′) = {0, 1}` producen ambos el valor visible `U`. No tienen por qué presentar el mismo comportamiento futuro. Esto no constituye un defecto del alfabeto visible; es la razón por la que un sistema de revisión puede requerir soporte certificado oculto además del marco actual.

# Morfismos conservativos y preservación de la no clausura certificada

El teorema anterior certifica un único sistema finito de resolución. Preguntamos ahora cuándo un cambio de representación o de implementación preserva su resultado.

## Morfismos de recubrimiento de resolución

Sean `ℛ = (X, 𝒜, →,x_*, T₀, T₁), ℛ′ = (X′, 𝒜′, → ′, x_*′, T₀′, T₁′)` dos sistemas locales finitos de resolución.

**Definición 5.1** (morfismo de recubrimiento de resolución). Un par `(ϕ, α)` con `ϕ : X → X′` y `α : 𝒜 → 𝒜′` es un morfismo de recubrimiento de resolución de `ℛ` a `ℛ′` en `x_*` si:

1.  `ϕ(x_*) = x_*′`;

2.  simulación hacia delante: `x -[a]→ y` implica `φ(x) -[α(a)]→' φ(y)`;

3.  levantamiento de caminos: para todo `x ∈ Reach_ℛ(x_*)` y toda arista `φ(x) -[a']→' y',` existen `a ∈ 𝒜` e `y ∈ X` tales que `x -[a]→ y`, `α(a) = a′` y `ϕ(y) = y′`;

4.  preservación y reflexión terminal: para todo `x` alcanzable y `v ∈ {0, 1}`, `x ∈ T_v ⇔ ϕ(x) ∈ T_v′.`

La simulación hacia delante establece que el trabajo de resolución previo sigue disponible. El levantamiento de caminos establece que el destino no ha introducido silenciosamente una nueva rama interna de resolución desde un estado imagen. La condición terminal establece que la semántica de clausura no ha cambiado bajo el reetiquetado. El aspecto de levantamiento de caminos es deliberadamente próximo a la tradición de aplicaciones abiertas y bisimulación funcional en teoría de concurrencia [17]; no se reivindica novedad para el levantamiento de caminos de forma aislada. Aquí queda tipado por las dos clases de clausura y se acopla posteriormente a la semántica de revisión.

**Teorema 5.2** (preservación y reflexión del perfil alcanzable). Si `(ϕ, α)` es un morfismo de recubrimiento de resolución, entonces `ϕ(Reach_ℛ(x_*)) = Reach_ℛ′(x_*′)` así como `C_ℛ(x_*) = C_ℛ′(x_*′).` En consecuencia, `val_ℛ(x_*) = val_ℛ′(x_*′).` En particular, la etiqueta `U` de la semántica finita general se preserva y se refleja.

Demostración. La simulación hacia delante transforma todo camino desde `x_*` en un camino desde `x_*′`, por lo que `ϕ(Reach_ℛ(x_*)) ⊆ Reach_ℛ′(x_*′).` Para la inclusión inversa, tómese cualquier camino en el destino `x_*′ = x₀′ → ′x₁′ → ′⋯ → ′x_k′.` Supóngase inductivamente que `x_j′ = ϕ(x_j)` para algún `x_j` alcanzable en `ℛ`; esto se cumple para `j = 0`. El levantamiento de caminos proporciona una arista `x_j → x_(j + 1)` con `ϕ(x_(j + 1)) = x_(j + 1)′`. Por tanto, todo estado alcanzable en el destino tiene una preimagen alcanzable.

Ahora, `v` pertenece a `C_ℛ(x_*)` si y solo si algún `x` alcanzable pertenece a `T_v`. Por preservación terminal, `ϕ(x)` es alcanzable y pertenece a `T_v′`, de modo que `v` pertenece al perfil de destino. Recíprocamente, si un `x′` alcanzable en el destino pertenece a `T_v′`, la primera parte da `x′ = ϕ(x)` para algún `x` alcanzable, y la reflexión terminal da `x ∈ T_v`. En consecuencia, los perfiles de clausura coinciden y (1) produce veredictos iguales. (c.q.d.)

**Proposición 5.3** (composición de recubrimientos de resolución). Las aplicaciones identidad son morfismos de recubrimiento de resolución. Además, si `(ϕ, α) : ℛ → ℛ′ y (ψ, β) : ℛ′ → ℛ″` son morfismos de recubrimiento de resolución en sus estados iniciales declarados, entonces `(ψ ∘ ϕ, β ∘ α) : ℛ → ℛ″` también es un morfismo de recubrimiento de resolución.

Demostración. Los estados iniciales y la simulación hacia delante se preservan por composición. Para el levantamiento de caminos, sea `x` alcanzable en `ℛ` y supóngase `ψ(φ(x)) -[c]→'' z''.` Como `ϕ(x)` es alcanzable en `ℛ′`, el levantamiento de caminos para `(ψ, β)` proporciona una arista `φ(x) -[b]→' z'` con `β(b) = c` y `ψ(z′) = z″`. El levantamiento de caminos para `(ϕ, α)` proporciona entonces `x -[a]→ z` con `α(a) = b` y `ϕ(z) = z′`. Por tanto, `(β ∘ α)(a) = c` y `(ψ ∘ ϕ)(z) = z″`. La preservación y reflexión terminales se componen de inmediato. (c.q.d.)

**Corolario 5.4** (transporte de alcanzabilidad certificada a través de un recubrimiento). Sea `χ = (R, d, p)` un certificado exacto de alcanzabilidad aceptado para `(ℛ, x_*)` y sea `(ϕ, α) : ℛ → ℛ′` un morfismo de recubrimiento de resolución verificado. Entonces `ϕ(R) = Reach_ℛ′(x_*′).` Por tanto, el testigo compuesto por el certificado de origen aceptado y las condiciones de recubrimiento comprobadas certifica el perfil de clausura alcanzable del destino sin una búsqueda independiente de alcanzabilidad en el sistema destino. A lo largo de cualquier cadena finita de recubrimientos de resolución verificados, el mismo perfil certificado puede transportarse por composición.

Demostración. El Lema 3.3 da `R = Reach_ℛ(x_*)`, y el Teorema 5.2 da `ϕ(Reach_ℛ(x_*)) = Reach_ℛ′(x_*′).` El perfil se lee entonces exactamente de las clases terminales de destino sobre `ϕ(R)`. La afirmación final se sigue de la Proposición 5.3. (c.q.d.)

**Corolario 5.5** (criterio estructural para sobrerrefinamiento conservativo). Una ampliación representacional que induce un morfismo de recubrimiento de resolución no puede cambiar un `0`, un `1` o una `U` certificados. Por tanto, una célula mayor solo puede eliminar una `U` previa si la ampliación incumple al menos una condición de recubrimiento: cambia la correspondencia declarada entre estados iniciales, introduce una rama de destino que no puede levantarse, deja de preservar una rama previa del origen, cambia la semántica terminal de clausura o deja de representar el mismo problema declarado.

Este resultado formaliza en el nivel operativo el principio de economía anterior. La afirmación no sostiene que las representaciones mayores sean inútiles. Sostiene que una representación mayor que sea únicamente una reexpresión por recubrimiento del sistema de resolución anterior es conservativa respecto del comportamiento.

## Novedad de dominio fijo frente a revisión del dominio

Dentro de un `D` fijo, un estado de información posterior `I′` puede habilitar una rama ya contemplada por el dominio pero no disponible en `I`. Tal cambio puede hacer que el nuevo resolvedor instanciado `ℛ_(D, I′, i)` incumpla la condición de levantamiento de caminos respecto de `ℛ_(D, I, i)` y constituye auténtica novedad resolutiva dentro del dominio.

Por el contrario, añadir un método que no era admisible bajo `D`, cambiar el criterio de clausura, sustituir la pregunta objetivo o cambiar la política declarada de representación no es una reapertura ordinaria bajo un `D` fijo. Es una revisión de dominio `D ⇝ D′`. Esta separación impide que la “novedad” oculte un cambio de universo matemático.

# Sistemas de revisión con soporte y equivalencia futura

La certificación local describe un episodio. Estudiamos ahora cómo evolucionan los estados completados con soporte cuando se producen incrementos admisibles posteriores.

## Sistemas deterministas de revisión por episodios completados

Sea `Y_D` un conjunto finito de estados completados con soporte. Cada `y ∈ Y_D` contiene un marco certificado actual y datos de soporte suficientes para instanciar el episodio siguiente. Sea `Φ_D : Y_D → Σ^n` la aplicación de marco visible. Sea `Δ_D` un alfabeto finito de incrementos externos admisibles bajo el dominio fijo, y sea `δ_D : Y_D × Δ_D → Y_D` la aplicación determinista que registra el siguiente estado completado con soporte una vez que se han completado el incremento y toda la resolución interna requerida bajo `D`. Extendemos `δ_D` a palabras `w ∈ Δ_D^*` de la forma habitual, escribiendo `δ_D^*(y, w)`. Fijemos un estado inicial declarado con soporte `y₀` y denotemos por `Y_D^r ⊆ Y_D` el conjunto de sus estados alcanzables.

No se afirma que esta abstracción determinista finita modele toda aplicación no determinista. Es la clase para la cual puede formularse una minimalidad futura exacta sin elecciones adicionales.

## Equivalencia futura

**Definición 6.1** (equivalencia futura de revisión). Para `y, z ∈ Y_D`, defínase `y ≡_D z ⇔ Φ_D(δ_D^*(y, w)) = Φ_D(δ_D^*(z, w)) para toda w ∈ Δ_D^*.`

Así, dos estados con soporte son equivalentes exactamente cuando ningún futuro finito admisible puede distinguir el comportamiento de sus marcos visibles.

**Definición 6.2** (realización determinista exacta de revisión). Una realización determinista exacta del comportamiento de revisión alcanzable es una tupla `(M, τ, o, h),` donde `M` es un conjunto de estados, `τ : M × Δ_D → M` es determinista, `o : M → Σ^n` es una aplicación de salida y `h : Y_D^r → M` satisface `h(δ_D(y, a)) = τ(h(y), a), o(h(y)) = Φ_D(y)` para todo `y` alcanzable y todo `a ∈ Δ_D`.

**Lema 6.3** (congruencia derecha). La relación `≡_D` es una relación de equivalencia, es compatible con la observación actual `Φ_D` y es una congruencia derecha: `y ≡_D z ⇒ δ_D(y, a)≡_Dδ_D(z, a)` para todo `a ∈ Δ_D`.

Demostración. La equivalencia se sigue inmediatamente de la igualdad de todas las aplicaciones residuales de observación. Tomando `w = ε` se obtiene `Φ_D(y) = Φ_D(z)`. Para la congruencia derecha, si `y ≡_D z`, entonces, para cualquier `w`, `Φ_D(δ_D^*(δ_D(y, a), w)) = Φ_D(δ_D^*(y, aw)) = Φ_D(δ_D^*(z, aw)) = Φ_D(δ_D^*(δ_D(z, a), w)).` (c.q.d.)

**Teorema 6.4** (cociente mínimo exacto de revisión). El cociente `𝒩_D := Y_D^r/ ≡_D` con transición `[y] -[a]→ [δ_D(y,a)]` y salida `[y] ↦ Φ_D(y)` es un sistema determinista de revisión bien definido que preserva todos los marcos visibles futuros.

Además, toda realización determinista exacta de revisión en el sentido de la Definición 6.2 debe distinguir cada par de estados alcanzables no equivalentes. Por tanto, su imagen alcanzable contiene al menos `|𝒩_D|` estados, y el cociente es mínimo, salvo isomorfismo, entre las realizaciones deterministas exactas de revisión.

Demostración. La buena definición se sigue del Lema 6.3. El cociente preserva observaciones y transiciones por construcción y, por tanto, preserva toda la aplicación residual `w ↦ Φ_D(δ_D^*(y, w))`.

Sea `(M, τ, o, h)` una realización determinista exacta de revisión y supóngase `h(y) = h(z)` para estados alcanzables `y, z`. Por inducción sobre la longitud de la palabra, la preservación exacta de transiciones da `h(δ_D^*(y, w)) = h(δ_D^*(z, w))` para toda `w ∈ Δ_D^*`. Aplicando `o` se obtiene que los marcos visibles correspondientes son iguales para toda `w` y, por tanto, `y ≡_D z`. En consecuencia, `h` no puede identificar estados alcanzables no equivalentes. El cociente identifica exactamente los estados equivalentes, por lo que alcanza la cota inferior. Si una realización exacta alcanza esa cota, cada clase de `≡_D` posee exactamente un estado imagen alcanzable; la aplicación inducida desde las clases del cociente hacia los estados alcanzables de la realización es, por tanto, una biyección que preserva salidas y transiciones y, en consecuencia, un isomorfismo. (c.q.d.)

El teorema es un resultado de minimización de tipo máquina de Moore/Nerode aplicado a la semántica de revisión, no una reivindicación de novedad para la minimización en sí. Su función aquí es definir la cantidad exacta de estado oculto que exige el comportamiento futuro de revisión.

## Cambio conservativo de resolvedor e invariancia del cociente de revisión

Considérense dos sistemas deterministas de revisión por episodios completados sobre el mismo alfabeto de incrementos, `𝒮 = (Y, Δ_D, δ, Φ), 𝒮′ = (Y′, Δ_D, δ′, Φ′),` con estados iniciales declarados `y₀, y₀′`. Denotemos por `Y^r` y `Y′^r` sus conjuntos de estados alcanzables, extendamos `δ, δ′` a palabras de la forma habitual y escribamos `≡, ≡′` para sus respectivas relaciones de equivalencia futura. Para cada estado alcanzable con soporte `y` y cada coordenada `i`, sea `ℛ_i(y)` el resolvedor local certificado que sustenta la coordenada `i`; defínase `ℛ_i′(y′)` de forma análoga. En toda esta subsección, “sustentar” se utiliza en el sentido coherente con la salida `Φ(y)_i = val_ℛ_i(y)(x_*(i,y)), Φ′(y′)_i = val_ℛ_i′(y′)(x_*′(i,y′)),` donde los estados iniciales mostrados son los que portan los correspondientes resolvedores locales. Esta condición de coherencia entre soporte y salida hace explícito el vínculo entre los perfiles locales certificados de clausura y las salidas visibles de revisión.

**Definición 6.5** (aplicación conservativa de resolvedores compatible con la revisión). Una aplicación `h : Y^r → Y′^r` es compatible con la revisión y conservativa respecto de la resolución cuando:

1.  `h(y₀) = y₀′`;

2.  `h(δ(y, a)) = δ′(h(y), a)` para todo `y` alcanzable y todo `a ∈ Δ_D`; y

3.  para todo `y` alcanzable y toda coordenada `i`, existe un morfismo de recubrimiento de resolución `ℛ_i(y) → ℛ_i′(h(y)).`

La Definición 6.5 es una condición estructural suficiente, no una afirmación de necesidad. Para sistemas finitos representados explícitamente es comprobable de forma finita una vez suministrados `h`, los certificados locales de alcanzabilidad aceptados y un testigo candidato de recubrimiento para cada par alcanzable `(y, i)`: las condiciones 1–2 son comprobaciones finitas de tabla y cada testigo de la condición 3 se comprueba frente a la Definición 5.1. El teorema siguiente no exige ninguna condición de coherencia entre los testigos de recubrimiento elegidos en distintos estados con soporte. Su única función consiste en establecer, estado por estado, el perfil local de clausura que sustenta la salida visible; la coherencia temporal la aporta la condición 2.

La condición 3 es local a cada episodio certificado; la condición 2 acopla esos cambios conservativos locales a la dinámica externa de revisión. La Figura 2 muestra las dos compatibilidades utilizadas por el teorema de invariancia.

``` text
Compatibilidad con incrementos

       h
 y ----------→ h(y)
 |              |
δ_a            δ'_a
 |              |
 v       h      v
δ(y,a) ------→ δ'(h(y),a)

h ∘ δ_a = δ'_a ∘ h

Invariancia del cociente mínimo

       h
 Y^r --------→ (Y')^r
 |              |
 q              q'
 |              |
 v      h̄ ≅     v
 𝓝 ----------→ 𝓝'

Recubrimientos locales por estado de los resolvedores con soporte.
```

**Figura 2.** Interacción del cambio conservativo de resolvedor con la revisión. La compatibilidad con cada incremento hace que h conmute con la dinámica de revisión; los morfismos de recubrimiento de resolución en los episodios locales con soporte preservan los perfiles visibles de clausura. La aplicación inducida h̄ preserva y refleja, por tanto, la equivalencia respecto de todos los futuros y es un isomorfismo de los cocientes mínimos alcanzables.

**Teorema 6.6** (invariancia del cociente mínimo de revisión bajo cambio conservativo de resolvedor). Sea `h` una aplicación que satisface la Definición 6.5. Entonces `h(Y^r) = Y′^r`. Además, para todo `y` alcanzable y toda palabra `w ∈ Δ_D^*`, `h(δ^*(y, w)) = δ′^*(h(y), w)` Asimismo, `Φ(δ^*(y, w)) = Φ′(δ′^*(h(y), w)).` En consecuencia, para todos los `y, z` alcanzables, `y ≡ z ⇔ h(y) ≡′ h(z).` Por tanto, `h` induce un isomorfismo entre los dos cocientes mínimos de revisión alcanzables. En particular, ambos tienen exactamente el mismo número de estados de comportamiento.

Demostración. La primera identidad mostrada se sigue por inducción sobre `|w|` a partir de la compatibilidad de transición. Como `h(y₀) = y₀′`, todo estado alcanzable del destino tiene la forma `δ′^*(y₀′, w) = h(δ^*(y₀, w))` para alguna `w ∈ Δ_D^*`; por tanto, `h(Y^r) = Y′^r`. Para todo estado alcanzable obtenido a lo largo de una palabra, la condición 3 y el Teorema 5.2 preservan y reflejan el perfil de clausura de cada coordenada; por la coherencia entre soporte y salida establecida antes de la Definición 6.5, queda preservado el marco visible completo, lo que proporciona la segunda identidad mostrada. Si `y ≡ z`, la igualdad de todos los marcos futuros de origen y esta identidad dan la igualdad de todos los marcos futuros de `h(y)` y `h(z)`, de modo que `h(y) ≡′ h(z)`. Recíprocamente, si `h(y) ≡′ h(z)`, la misma identidad refleja la igualdad hacia los futuros de origen, por lo que `y ≡ z`. Así, la aplicación inducida sobre clases de equivalencia es inyectiva; la sobreyectividad de `h` sobre los estados alcanzables la hace sobreyectiva sobre las clases del cociente. Preserva salidas y transiciones y, por tanto, es un isomorfismo. (c.q.d.)

El Teorema 6.6 es el punto en el que interactúan las capas de resolución y revisión: un cambio conservativo únicamente episodio por episodio todavía no controla la memoria futura; la compatibilidad con incrementos admisibles es lo que hace invariante el cociente mínimo de revisión. No se requiere como condición adicional coherencia entre los distintos testigos de recubrimiento estado por estado, porque dichos testigos establecen únicamente las salidas locales sustentadas, mientras que la condición 2 controla la trayectoria. El teorema se formula para la semántica finita general. Una implementación SV que utilice registros soberanos de `U` debe exigir además que `h` preserve los metadatos de autorización correspondientes; se trata de una condición de instancia sobre la interpretación SV de `Φ`, no de una hipótesis adicional del teorema finito general.

# Fronteras de soporte y cuándo son suficientes

Un certificado que sustenta el valor actual puede dejar de ser adecuado tras un incremento externo. Las fronteras de soporte de un paso constituyen una forma compacta de registrar esa posibilidad, pero no se presupone que determinen automáticamente todo el comportamiento futuro.

Para cada estado con soporte `y` y cada coordenada `i`, sea `κ_i(y)` su objeto de soporte actual. El dominio proporciona un predicado que expresa si ese soporte sigue siendo aplicable tras un incremento bruto admisible. Defínase la frontera de un paso `B_i(y) := {a ∈ Δ_D : κ_i(y) debe reabrirse tras a}.` El predicado de reapertura se trata extensionalmente como parte del dominio declarado `D`, del mismo modo que la legitimidad terminal en la Sección 3. La presente teoría analiza las consecuencias de ese predicado declarado; no infiere ni valida las reglas de reapertura específicas de un dominio. Sea `B(y) = (B₁(y), …, B_n(y))` y defínase el descriptor de frontera `ℬ_D(y) := (Φ_D(y), B(y)).`

El descriptor siempre contiene el marco actual. La cuestión es si contiene suficiente información oculta para reproducir todos los marcos visibles futuros.

**Teorema 7.1** (caracterización de la memoria de frontera exacta). En el subsistema alcanzable `Y_D^r`, sea `K_B` el núcleo del descriptor de frontera: `y K_B z ⇔ ℬ_D(y) = ℬ_D(z), y, z ∈ Y_D^r.` Entonces:

1.  Si `K_B` es una congruencia derecha para `δ_D`, es decir, `y K_B z ⇒ δ_D(y, a) K_B δ_D(z, a) ∀a ∈ Δ_D,` entonces `K_B ⊆ ≡_D`. En consecuencia, `ℬ_D` es suficiente para reproducir todo marco visible futuro.

2.  Si, además, los descriptores de frontera distintos son separables en el futuro, es decir, siempre que `ℬ_D(y) ≠ ℬ_D(z)` existe `w ∈ Δ_D^*` tal que `Φ_D(δ_D^*(y, w)) ≠ Φ_D(δ_D^*(z, w)),` entonces `K_B = ≡_D`. Por tanto, el descriptor de frontera realiza el cociente mínimo exacto del Teorema 6.4, salvo reetiquetado.

Demostración. Para la parte 1, supóngase `y K_B z`. Como el descriptor incluye `Φ_D`, los marcos visibles actuales son iguales. La estabilidad por congruencia derecha implica por inducción sobre `|w|` que `δ_D^*(y, w) K_B δ_D^*(z, w)` para toda palabra `w`. Sus descriptores y, por tanto, sus marcos visibles son iguales para toda palabra futura. De aquí, `y ≡_D z`.

Para la parte 2, la parte 1 da `K_B ⊆ ≡_D`. Si `y` y `z` no son equivalentes por `K_B`, sus descriptores difieren, de modo que la separabilidad futura proporciona una palabra que distingue sus marcos visibles. Por tanto, `y ≢_D z`, lo que demuestra `≡_D ⊆ K_B`. (c.q.d.)

**Proposición 7.2** (prueba local finita de suficiencia de la frontera). Para un sistema determinista finito de revisión representado explícitamente, la congruencia derecha de `K_B` sobre el subsistema alcanzable puede comprobarse sin enumerar palabras de `Δ_D^*`. Basta particionar `Y_D^r` mediante `ℬ_D` y verificar, para cada clase de descriptor `C` y cada `a ∈ Δ_D`, que todos los estados de `C` transitan bajo `a` hacia una única clase de descriptor.

Demostración. La condición indicada es exactamente `y K_B z ⇒ δ_D(y, a) K_B δ_D(z, a),` comprobada una vez para cada transición de un paso desde cada clase de descriptor. Si se cumple, el Teorema 7.1 propaga por inducción la igualdad a todas las palabras finitas. Una vez disponibles los identificadores de descriptor, esta comprobación requiere una única pasada por la tabla explícita de estados alcanzables y acciones, es decir, `O(|Y_D^r| |Δ_D|)` entradas de tabla. (c.q.d.)

**Corolario 7.3** (certificado suficiente, enteramente local, de memoria de frontera exacta). Supóngase que `K_B` es una congruencia derecha y que, para todo par alcanzable `y, z` con `ℬ_D(y) ≠ ℬ_D(z)`, se cumple `Φ_D(y) ≠ Φ_D(z)` o existe un incremento `a ∈ Δ_D` tal que `Φ_D(δ_D(y, a)) ≠ Φ_D(δ_D(z, a)).` Entonces `K_B = ≡_D`, por lo que el descriptor de frontera realiza el cociente mínimo exacto de revisión. Ambas hipótesis pueden comprobarse únicamente a partir de los descriptores actuales y de transiciones de un paso; no se requiere enumerar palabras de `Δ_D^*`.

Demostración. La congruencia derecha da `K_B ⊆ ≡_D` por el Teorema 7.1(1). Si dos estados tienen descriptores diferentes, la hipótesis indicada los distingue o bien en la palabra vacía o bien tras un incremento, por lo que no pueden ser equivalentes en el futuro. En consecuencia, `≡_D ⊆ K_B`. (c.q.d.)

Una vez establecida la congruencia derecha, la segunda hipótesis puede comprobarse sin comparar explícitamente de forma cuadrática todos los pares de estados: asígnese a cada clase de descriptor la firma de salida de un paso `(Φ_D(y), (Φ_D(δ_D(y,a))) para a∈Δ_D)` utilizando cualquier representante `y` de la clase, y compruébese la inyectividad de estas firmas entre clases de descriptor. La congruencia derecha hace que la firma sea independiente del representante. Con identificadores de clase y de firma mediante tablas de dispersión (hash), el coste vuelve a ser lineal en la tabla explícita de estados alcanzables y acciones, salvo las operaciones ordinarias de diccionario.

**Observación 7.4** (las fronteras de un paso no son automáticamente completas). El Teorema 7.1 proporciona una condición suficiente de congruencia y un criterio de exactitud cuando se añade separabilidad futura, mientras que el Corolario 7.3 proporciona un certificado suficiente de exactitud más fuerte pero enteramente local. El fallo de la prueba local de congruencia derecha significa únicamente que la Proposición 7.2 deja de certificar la suficiencia de la frontera; no demuestra por sí mismo que los datos de frontera sean insuficientes. Puede requerirse entonces un análisis adicional o una procedencia enriquecida.

Para una coordenada cuyo valor visible sea `U`, el conjunto `B_i(y)` es la frontera de reapertura de esa no clausura certificada. Dos valores visibles `U` pueden, por tanto, ser iguales en el marco y pertenecer, sin embargo, a clases distintas del cociente mínimo de revisión.

# Memoria cuantitativa oculta de revisión

La sección anterior es cualitativa. Primero cuantificamos la multiplicidad oculta de revisión sin ninguna hipótesis de independencia y después recuperamos como especialización la fórmula de producto independiente.

## Fibras del marco y multiplicidad oculta

Para un marco visible alcanzable `s ∈ Φ_D(Y_D^r)`, defínase `m_D(s) := |{[y]_≡D : y ∈ Y_D^r, Φ_D(y) = s}|.` Así, `m_D(s)` cuenta los estados mínimos de revisión con comportamientos distintos que permanecen ocultos tras el mismo marco presente.

**Proposición 8.1** (descomposición por fibras de la memoria mínima de revisión). Para todo sistema determinista finito de revisión, `|𝒩_D| = ∑[s ∈ Φ_D(Y_D^r)] m_D(s).` En particular, `|𝒩_D| ≥ |Φ_D(Y_D^r)|`, con desigualdad estricta exactamente cuando al menos un marco visible oculta más de una clase de equivalencia futura.

Demostración. Los estados equivalentes en el futuro tienen la misma salida actual por el Lema 6.3. Por tanto, cada clase de `≡_D` está contenida en una única fibra de `Φ_D`. El cociente es, en consecuencia, la unión disjunta de las clases de cociente contenidas en esas fibras, lo que proporciona la suma. La desigualdad es estricta exactamente cuando alguna fibra aporta al menos dos clases. (c.q.d.)

La Proposición 8.1 es deliberadamente elemental: su función no es reivindicar una nueva identidad de partición, sino aislar la multiplicidad oculta que el Corolario 8.2 hace computable a partir de la diversidad de fronteras de un paso cuando el descriptor de frontera es exacto.

**Corolario 8.2** (fórmula de frontera bajo memoria de frontera exacta). Si se cumplen las hipótesis de la parte 2 del Teorema 7.1, entonces, para todo marco alcanzable `s`, `m_D(s) = |{B(y) : y ∈ Y_D^r, Φ_D(y) = s}|.` En consecuencia, `|𝒩_D| = ∑[s ∈ Φ_D(Y_D^r)] |{B(y) : y ∈ Y_D^r, Φ_D(y) = s}|.` Así, un objeto de soporte de un paso calcula la multiplicidad oculta exacta del cociente mínimo respecto de todos los futuros siempre que el criterio de frontera sea exacto.

Demostración. Bajo el Teorema 7.1(2), `K_B = ≡_D`. Dentro de una fibra visible fija `Φ_D⁻¹(s)`, dos estados tienen el mismo descriptor de frontera si y solo si tienen el mismo vector de frontera `B(y)`. Por tanto, las clases de vectores de frontera y las clases de equivalencia futura coinciden dentro de esa fibra. (c.q.d.)

Una realización determinista exacta necesita, por tanto, al menos `m_D(s)` estados internos distinguibles mientras muestra el marco `s`, o al menos `⌈log₂ m_D(s)⌉` bits solo para distinguir esas clases ocultas de comportamiento cuando `m_D(s) > 1`.

## Clases residuales locales

Para la coordenada `i`, proyéctese el marco visible mediante `Φ_i : Y_i → Σ` en un sistema local finito de revisión `(Y_i, Δ_i, δ_i, Φ_i)`. Sea `≡_i` la equivalencia futura definida como en la Definición 6.1 utilizando `Φ_i`.

Sea `r_i` el número de clases distintas de `≡_i` cuyo valor visible actual es `U`. Supóngase que existe al menos una clase futura alcanzable con valor actual `0` y al menos una con valor actual `1`. Como las salidas actuales ya distinguen `0` de `1` y ambas de `U`, el cociente mínimo local contiene al menos `2 + r_i` clases.

## Productos independientes

Para cada sistema local, sea `Y_i^r` su conjunto de estados alcanzables. Considérense `n` sistemas locales de revisión cuyo producto alcanzable independiente es `Y^r = ∏[i=1…n] Y_i^r,` con salida visible `Φ(y₁, …, y_n) = (Φ₁(y₁), …, Φ_n(y_n)),` y un alfabeto externo que permite acciones coordenada a coordenada con un símbolo neutro en toda coordenada no afectada. Supóngase que este producto completo de estados/clases locales alcanzables es también globalmente alcanzable. Estas son hipótesis explícitas de independencia y realizabilidad; sin ellas no se afirma la fórmula de producto siguiente.

**Teorema 8.3** (cociente de revisión del producto). Bajo las hipótesis de producto independiente, dos estados globales son equivalentes en el futuro si y solo si sus correspondientes estados locales son equivalentes en el futuro en cada coordenada. En consecuencia, `|Y^r/≡| = ∏[i=1…n] |Y_i^r/≡_i|.`

Demostración. Si `y_i ≡_i z_i` para todo `i`, toda palabra global se proyecta en una palabra local de cada coordenada, y todas las secuencias de salida locales coinciden; por tanto, las salidas globales en tupla coinciden para toda palabra.

Recíprocamente, supóngase `y_j ≢_j z_j` para alguna coordenada `j`. Existe una palabra local `w_j` que distingue sus salidas. Elévese `w_j` a una palabra global aplicando sus acciones a la coordenada `j` y acciones neutras al resto. Los marcos visibles globales resultantes difieren en la coordenada `j`, de modo que los estados globales no son equivalentes en el futuro. Por tanto, las clases de equivalencia son exactamente los productos cartesianos de las clases locales, lo que da la fórmula de cardinalidad. (c.q.d.)

**Corolario 8.4** (cota de multiplicidad oculta de revisión). Si la coordenada `i` contiene `r_i` clases distinguibles por sus futuros con valor visible actual `U`, además de clases actuales alcanzables `0` y `1`, entonces toda realización global determinista exacta de revisión del producto independiente plenamente realizable requiere al menos `N_min ≥ ∏[i=1…n] (2+r_i).` Si `r_i = r` para todo `i`, entonces `N_min ≥ (2 + r)^n.` Para todo `r > 1`, `(2 + r)^n > 3^n,` por lo que la memoria mínima exacta de revisión es estrictamente mayor que el espacio de marcos ternarios visibles.

La cota no afirma que el marco sea incorrecto. Cuantifica una compresión deliberada: `3^n` veredictos visibles pueden coexistir con más de `3^n` estados con soporte distintos por su comportamiento.

# Ejemplo finito desarrollado

Presentamos un ejemplo explícito que ejercita la certificación, valores visibles `U` iguales con procedencias distintas, separación futura y la cota cuantitativa.

## Dos no clausuras certificadas diferentes

Considérense dos sistemas locales finitos de resolución con el mismo alfabeto visible de salida.

El sistema `ℛ_A` tiene estados `X_A = {s, a, b},` aristas internas `s → a` y `s → b`, y carece de estados terminales binarios: `T₀^A = T₁^A = ∅.` El conjunto exacto alcanzable es `R_A = X_A`, por lo que su perfil de clausura es vacío y `val_ℛ_A(s) = U.`

El sistema `ℛ_B` tiene estados `X_B = {s′, c, d},` aristas internas `s′ → c` y `s′ → d`, con `T₀^B = {c}, T₁^B = {d}.` Su conjunto exacto alcanzable es `R_B = X_B`, de modo que `C_ℛ_B(s′) = {0, 1}` y, de nuevo, `val_ℛ_B(s′) = U.`

Ambos sistemas tienen certificados exactos pequeños: tómese como `R` el propio conjunto alcanzable, asígnese rango `1` a los dos sucesores y regístrense sus aristas entrantes. El verificador acepta ambos. El mismo valor visible `U` cubre, por tanto, dos perfiles de clausura certificados: `U_A : ∅, U_B : {0, 1}.` No se introduce ningún valor de verdad visible nuevo.

## Un sistema mínimo de revisión de cuatro estados

Defínanse ahora los cuatro estados completados con soporte `Y = {u_A, u_B, z₀, z₁}, Δ = {α, β},` con `Φ(u_A) = Φ(u_B) = U`, `Φ(z₀) = 0` y `Φ(z₁) = 1`. Sus transiciones deterministas y fronteras de reapertura se muestran en la Figura 3; `z₀` y `z₁` son absorbentes para ambos incrementos.

``` text
u_A [Φ=U] --α→ z_0 [Φ=0]
   | β             ↺ α,β
   v
  u_A

u_B [Φ=U] --β→ z_1 [Φ=1]
   | α             ↺ α,β
   v
  u_B

B(u_A)={α}    B(u_B)={β}    u_A ≢ u_B
```

**Figura 3.** Sistema de revisión de cuatro estados con dos estados actuales U distintos por su comportamiento. El incremento α envía u_A a 0 pero mantiene u_B en U; simétricamente, β los separa en la otra dirección. Así, la etiqueta visible U oculta dos clases de soporte distinguibles por sus futuros.

Los cuatro estados son distinguibles por sus futuros de dos en dos: `z₀` y `z₁` se distinguen mediante la palabra vacía; cualquier estado binario se distingue de cualquier estado `U` mediante la palabra vacía; y `u_A, u_B` se distinguen tras un incremento. Por tanto, el cociente mínimo exacto de revisión tiene cuatro estados aunque el alfabeto visible solo tenga tres.

El ejemplo es deliberadamente pequeño. Muestra por qué la exactitud de frontera debe establecerse y no presuponerse: aquí el descriptor de frontera es exacto porque su núcleo es la relación identidad y, por tanto, una congruencia derecha. Además, los distintos descriptores `U` quedan separados tras un incremento, de modo que el Corolario 7.3 certifica la minimalidad usando únicamente datos de un paso.

## Ilustración canónica de nueve coordenadas

Tómense nueve copias independientes del sistema local de revisión precedente, correspondientes al número de coordenadas de la célula fundacional `SV(9, 3)`. Cada coordenada tiene `r_i = 2` clases `U` distinguibles por sus futuros. El Corolario 8.4 da `N_min ≥ 4⁹ = 262144.` El espacio de marcos ternarios visibles tiene `3⁹ = 19683` marcos. Por tanto, en esta construcción completamente independiente, el comportamiento exacto de revisión requiere más de trece veces tantas clases de comportamiento como marcos ternarios visibles. La comparación numérica es ilustrativa y no universal; el resultado general es la fórmula de producto con sus hipótesis explícitas de independencia.

# Clausura autorizada e historiales de sucesos de solo adición

Los teoremas nucleares anteriores no dependen de una interpretación humano-máquina. La realización SV originaria añade reglas de autoridad externas a esos teoremas: un perfil no unitario certificado por máquina no constituye por sí mismo un registro soberano de `U`, y cualquier sustitución soberana posterior de una `U` registrada es un acto autorizado distinto.

## Notación diferenciada para sucesos, horizontes y autorización

Sea `ℰ_D` un conjunto de ocurrencias soberanas de sucesos y sea `Ξ_D : ℰ_D → Y_D` la aplicación que asigna un estado completado con soporte a cada suceso. El marco visible portado por un suceso es `Ψ_D := Φ_D ∘ Ξ_D : ℰ_D → Σ^n.` Los símbolos `Φ_D` y `Ψ_D` son deliberadamente distintos: el primero lleva estados con soporte a marcos; el segundo lleva ocurrencias de sucesos a marcos.

Sea `Θ_D` un conjunto de tipos de suceso con aplicación de tipado `θ_D : ℰ_D → Θ_D.` El horizonte declarado de sucesos se denota `ℋ_D^evt ⊆ Θ_D.` Por separado, sea `𝒜_D^auth` la clase de actos de autorización admisibles. No se reutiliza ningún símbolo entre el horizonte de sucesos y la capa de autorización.

## Autorización soberana de `U` y clausura posterior

La teoría finita general separa la certificación de un perfil de clausura de las reglas adicionales de autoridad propias de una realización particular. En la realización SV, un certificado aceptado `η_U` demuestra que el episodio finito admitido tiene un perfil de clausura no unitario, pero ese hecho verificable por máquina no crea por sí mismo una ocurrencia soberana de suceso que porte el valor `U`. El registro de una `U` real requiere un elemento de `𝒜_D^auth` o una investigación cuya conclusión haya sido revisada y autorizada por un humano.

La sustitución posterior de una `U` soberana ya registrada por un valor binario constituye un segundo acto de cambio de estado, distinto, y exige igualmente el acto de clausura autorizado que corresponda. El subsistema computacional puede seguir calculando, buscando, demostrando, comparando o comprobando cuando se aporta nueva información resolutiva; también puede completar un episodio que era meramente pendiente y obtener una clausura binaria ordinaria. Lo que no hace de forma autónoma en la realización SV es constituir un registro soberano de `U` ni sobrescribirlo mediante un registro binario posterior.

Estas condiciones de autoridad son reglas de instancia de SV, no teoremas sobre todos los sistemas finitos de resolución, y no introducen un cuarto valor visible.

## Historiales de solo adición

Un historial finito de sucesos es `Γ_m = (e₀, ν₀, e₁, ν₁, …, ν_(m − 1), e_m),` donde `ν_j` registra información de transición entre ocurrencias consecutivas. Escribimos `Γ_m ≼ Γ_k` cuando `Γ_m` es un prefijo inalterado de `Γ_k`. Una evolución de solo adición satisface `Γ_m ≼ Γ_(m + 1).` El índice es ordinal. Puede asociarse un reloj como metadato, pero el orden no requiere ninguna coordenada temporal primitiva [2, 4, 5].

**Corolario 10.1** (revisión no retrospectiva). Supóngase `i < j` y `Ψ_D(e_i)_r = U, Ψ_D(e_j)_r = v ∈ {0, 1, U}.` En un historial de solo adición, la reevaluación posterior queda representada por el suceso distinto `e_j` y no altera el marco registrado de `e_i`. Por tanto, la revisión del veredicto actual es compatible con la inmutabilidad histórica.

La misma regla de registro puede aplicarse a revisiones de valores `0` o `1` anteriores. El presente trabajo se centra en `U` porque es ahí donde resulta más nítida la separación entre búsqueda inacabada y finalidad local certificada.

# Relación con formalismos próximos y origen documental

Los vecinos matemáticos deben tratarse, ante todo, como restricciones sobre lo que este trabajo puede reivindicar.

Las estructuras de Kripke parciales de Bruns y Godefroid utilizan un tercer valor para razonar sobre propiedades no determinadas por espacios de estados incompletos [7, 8]. La verificación en tiempo de ejecución utiliza de forma análoga un tercer veredicto inconcluso sobre trazas finitas [9]. La construcción presente difiere en el punto de admisión: la `U` visible de un episodio finito de resolución se emite únicamente después de que un certificado comprobable establezca el perfil completo de clausura alcanzable del resolvedor finito declarado. La mera incompletitud de observación o de ejecución no basta.

La comprobación de modelos condicional es un vecino operativo especialmente próximo porque distingue la verificación completada de un verificador que se detiene y registra una condición que resume el trabajo realizado [10]. El presente sistema sigue una vía distinta: un resolvedor que simplemente se ha detenido todavía no dispone de una `U` certificada; la cobertura finita exacta debe ser comprobable de forma independiente. De este modo, la verificación del certificado, y no la mera terminación de la herramienta, delimita el trabajo pendiente frente a la no clausura completada.

La comprobación verificada de pruebas SAT/UNSAT muestra el principio más amplio según el cual una búsqueda costosa puede separarse de un comprobador de confianza más reducido [11]. El certificado exacto de alcanzabilidad de la Sección 3 adopta esa disciplina arquitectónica, pero certifica un perfil de clausura alcanzable de tres vías en lugar de satisfacibilidad proposicional.

Los sistemas de mantenimiento de verdad y la lógica de justificación son vecinos directos de una revisión portadora de soporte [12, 13]. No intentamos construir una lógica general de razones. La capa de revisión pregunta únicamente qué distinciones ocultas son necesarias para preservar todo comportamiento futuro del marco visible.

Esta última cuestión es clásica en teoría de autómatas. El cociente del Teorema 6.4 es una equivalencia residual de tipo Nerode [18]. Del mismo modo, el levantamiento de caminos posee una historia anterior sustancial mediante aplicaciones abiertas y bisimulación [17]. La contribución reivindicada aquí no es, por tanto, la minimización ni el levantamiento de caminos de manera aislada. El Corolario 5.4 acopla primero la certificación al cambio conservativo de resolvedor al transportar un perfil alcanzable exacto a través de un recubrimiento comprobado. El Teorema 6.6 acopla después el cambio conservativo de resolvedor a la revisión: la compatibilidad con incrementos externos preserva y refleja la equivalencia respecto de todos los futuros y, por tanto, el cociente mínimo de revisión. El Corolario 7.3 proporciona un certificado de un paso para determinar cuándo el descriptor concreto de frontera ya constituye la memoria mínima respecto de todos los futuros. Las fórmulas de fibras y fronteras de la Proposición 8.1 y el Corolario 8.2 cuantifican después lo que oculta la proyección ternaria visible sin requerir independencia entre coordenadas.

Las estructuras de sucesos ya distinguen las ocurrencias y los historiales de las etiquetas de estado [14]; el control supervisor y el aprendizaje con remisión a un experto ya distinguen clases de control o de intervención experta [15, 16]. En consecuencia, no se reivindican como novedades aisladas ni la identidad del suceso ni la autorización.

Como comparación contemporánea, Complete CALM, de Hellerstein, fue remitido por primera vez el 10 de febrero de 2026 y revisado el 14 de junio de 2026, mientras que los trabajos citados sobre complejidad de las determinaciones y procedencia aparecieron el 30 de marzo y el 9 de junio [19, 20, 21]. Las fuentes SV específicas utilizadas aquí se publicaron los días 9, 11 y 14 de marzo de 2026 [1, 2, 3]. Estas fechas se registran únicamente a efectos de atribución documental: los trabajos de Hellerstein se ocupan de determinación y compromiso sobre historiales, mientras que los resultados presentes se ocupan de perfiles finitos exactos de clausura y memoria de revisión; ninguna reivindicación de prioridad sustituye a los teoremas demostrados aquí.

# Discusión y limitaciones

## Por qué las condiciones son operativas y no retóricas

La formalización finita evita utilizar “agotamiento” o “persistencia conservativa” como prosa autocertificante. Un certificado de alcanzabilidad aceptado demuestra un conjunto alcanzable exacto; la Proposición 3.2 hace visible su coste explícito de verificación. Una representación conservativa debe satisfacer levantamiento de caminos y preservación/reflexión terminal, y la Proposición 5.3 muestra que tales cambios conservativos se componen.

Del mismo modo, no se presupone que las fronteras de reapertura de un paso determinen la revisión. El Teorema 7.1 utiliza la congruencia derecha como condición suficiente para la suficiencia respecto de todos los futuros, mientras que la Proposición 7.2 reduce esa condición a una comprobación finita local de transiciones. Si la prueba local falla, simplemente deja de certificar suficiencia; la insuficiencia requiere evidencia separada, y una procedencia enriquecida constituye entonces una posible solución.

## Finalidad local y reapertura global

Dentro de la semántica finita general, un perfil no unitario de clausura certificado es localmente final para el episodio finito y recibe la etiqueta `U` mediante (1); no constituye un teorema metafísico de imposibilidad. En la realización SV, ese perfil certificado por máquina se convierte en un registro soberano de `U` únicamente mediante la regla adicional de autorización humana de la Sección 10.2. Un incremento posterior admisible bajo el mismo dominio puede instanciar un nuevo resolvedor con ramas alcanzables genuinamente nuevas, mientras que una revisión de dominio puede cambiar el propio aparato matemático admitido. Estas operaciones siguen siendo distintas.

## Ausencia de una ley universal para `U`

La regla visible de (1) pertenece a la semántica de resolución finita definida aquí. No se reivindica ninguna tabla de verdad, aritmética ni ley de composición universal para `U`. En particular, el trabajo no identifica `U` con SQL NULL, el elemento ínfimo de un retículo, un intervalo de probabilidad ni un valor genérico de “desconocido”.

## Finitud

La limitación actual más fuerte es la finitud. El certificado exacto de la Sección 3 depende del cierre explícito finito por sucesores y de un testigo finito de alcanzabilidad. Los espacios de resolución infinitos pero finitamente representados pueden admitir invariantes simbólicos, abstracciones portadoras de prueba u otros lenguajes de certificados, pero su corrección y completitud requieren teoremas separados. El presente trabajo demuestra deliberadamente el caso finito en lugar de ocultar una noción indecidible o no verificable dentro de la palabra “agotamiento”.

## Revisión determinista

El teorema de revisión mínima presupone transiciones deterministas entre episodios completados. La revisión no determinista requeriría una equivalencia observacional distinta, por ejemplo variantes de trazas, simulación o bisimulación según lo que preserve cada aplicación. Nada del teorema de certificación depende de una revisión determinista, pero sí los Teoremas 6.4–8.3.

## Probabilidad y tiempo

Los resultados no requieren ninguna medida de probabilidad ni coordenada temporal primitiva. Las aplicaciones pueden introducir evidencia estadística, relojes o escalas metrológicas como objetos declarados del dominio. Su ausencia del teorema basal no debe interpretarse como una prohibición de la medición o la estadística.

# Conclusión

La no clausura certificada puede hacerse más fuerte que una tercera etiqueta sin añadir un cuarto valor visible. La teoría finita desarrollada aquí separa tres preguntas que a menudo se confunden: `¿Es suficiente la representación? | ¿Se ha completado la resolución admitida? | ¿Qué perfil de clausura se ha certificado?` Un certificado exacto finito de alcanzabilidad responde operativamente a la segunda y a la tercera pregunta. Produce `0` o `1` únicamente cuando el perfil alcanzable completo contiene exactamente una clase de clausura binaria; en caso contrario certifica un perfil no unitario, etiquetado `U` en la semántica finita general. Un resolvedor que se limita a detenerse prematuramente carece de ese certificado y, por tanto, no ha establecido una no clausura certificada. En la realización SV, un registro soberano de `U` requiere además el acto de autorización humana definido anteriormente.

Los morfismos de recubrimiento de resolución identifican una clase componible de cambios conservativos: la simulación hacia delante, junto con el levantamiento de caminos y la reflexión terminal, preserva y refleja todo el perfil de clausura. La interacción con la revisión es más fuerte que la mera preservación episodio por episodio. Cuando esos recubrimientos locales son compatibles con todo incremento externo admisible, el Teorema 6.6 muestra que preservan y reflejan la equivalencia futura e inducen el mismo cociente mínimo de revisión alcanzable. Así, un cambio conservativo de resolvedor certificado no puede alterar silenciosamente ni el perfil de clausura presente ni la cantidad de memoria exacta requerida para una revisión posterior.

En el nivel de revisión, el marco ternario visible es únicamente una aplicación de observación. La multiplicidad oculta exacta tras un marco actual es el número de clases de equivalencia futura de su fibra. La Proposición 8.1 descompone el cociente mínimo mediante esas fibras y, cuando el descriptor de frontera de un paso es exacto, el Corolario 8.2 calcula directamente dicha multiplicidad a partir de la diversidad de fronteras. La fórmula de coordenadas independientes `N_min ≥ ∏_i(2 + r_i)` es entonces una especialización bajo realizabilidad explícita del producto y no la única afirmación cuantitativa.

El cuadro resultante no es, por tanto, “desconocido frente a conocido”. Es una semántica finita de resolución certificada cuya salida ternaria visible puede comprimir deliberadamente una estructura de revisión más rica. La evidencia posterior puede reabrir esa estructura en un nuevo suceso, mientras que el historial de solo adición conserva el resultado certificado anterior en lugar de reescribirlo.

# Disponibilidad de datos

Este trabajo es teórico y no introduce ningún conjunto de datos empírico. Los preprints SV de origen citados a continuación están disponibles públicamente a través de sus registros DOI.

# Contribuciones del autor

J.A.L.E.: conceptualización, análisis formal, metodología, investigación, redacción del borrador original, revisión y edición del manuscrito.

# Conflictos de intereses

El autor declara no tener conflictos de intereses.

# Financiación

Este trabajo no recibió financiación externa.

# Declaración de uso de IA

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para búsqueda bibliográfica, comprobación adversarial de consistencia, estructuración del manuscrito, ayuda a la formalización matemática, apoyo a la composición tipográfica y edición en lengua inglesa. Grok 4.5 (xAI; interacción el 8 de agosto de 2026) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias sobre presentación y posicionamiento. Todas las salidas de IA se trataron como materiales de investigación no autoritativos. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume plena responsabilidad por el manuscrito.

# Agradecimientos

El autor agradece a la comunidad abierta de investigación los trabajos de acceso público que hicieron posible la comparación directa con formalismos próximos.

# Referencias

[1] Lloret Egea JA. 2026. Fundamentos algebraico-semánticos del Sistema Vectorial SV: célula exacta, representación polar, indeterminación epistémica y composición tipada. IA eñ / ITVIA. Publicado el 9 de marzo de 2026. doi:10.21428/39829d0b.b0cf9a13.

[2] Lloret Egea JA. 2026. Álgebra de composición intercelular del marco SV – III. Horizonte de sucesos y reevaluación discreta. IA eñ / ITVIA. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.bb86c65d.

[3] Lloret Egea JA. 2026. Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV. IA eñ / ITVIA. Publicado el 14 de marzo de 2026. doi:10.21428/39829d0b.f433065f.

[4] Lloret Egea JA. 2026. Transiciones estructurales y trayectorias de la U en el Sistema Vectorial SV. IA eñ / ITVIA. Publicado el 16 de marzo de 2026. doi:10.21428/39829d0b.10e10f96.

[5] Lloret Egea JA. 2026. Teoría rigurosa del suceso admisible en el Sistema Vectorial SV. Doc VII.1. IA eñ / ITVIA. Publicado el 22 de marzo de 2026. doi:10.21428/39829d0b.1608c18c.

[6] Lloret Egea JA. 2026. Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable. IA eñ / ITVIA. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.f471b07c.

[7] Bruns G, Godefroid P. 1999. Model checking partial state spaces with 3-valued temporal logics. En Computer Aided Verification, LNCS 1633, pp. 274–287. doi:10.1007/3-540-48683-6_25.

[8] Bruns G, Godefroid P. 2000. Generalized model checking: reasoning about partial state spaces. En CONCUR 2000 – Concurrency Theory, LNCS 1877, pp. 168–182. doi:10.1007/3-540-44618-4_14.

[9] Bauer A, Leucker M, Schallhart C. 2011. Runtime verification for LTL and TLTL. ACM Transactions on Software Engineering and Methodology 20(4), artículo 14. doi:10.1145/2000799.2000800.

[10] Beyer D, Henzinger TA, Keremoglu ME, Wendler P. 2012. Conditional model checking: a technique to pass information between verifiers. En Proceedings of the ACM SIGSOFT 20th International Symposium on the Foundations of Software Engineering. doi:10.1145/2393596.2393664.

[11] Lammich P. 2020. Efficient verified (UN)SAT certificate checking. Journal of Automated Reasoning 64, 513–532. doi:10.1007/s10817-019-09525-z.

[12] Doyle J. 1979. A truth maintenance system. Artificial Intelligence 12, 231–272. doi:10.1016/0004-3702(79)90008-0.

[13] Artemov S. 2008. The logic of justification. Review of Symbolic Logic 1, 477–513. doi:10.1017/S1755020308090060.

[14] Winskel G. 1987. Event structures. En Petri Nets: Applications and Relationships to Other Models of Concurrency, LNCS 255, pp. 325–392. doi:10.1007/3-540-17906-2_31.

[15] Ramadge PJ, Wonham WM. 1987. Supervisory control of a class of discrete event processes. SIAM Journal on Control and Optimization 25, 206–230. doi:10.1137/0325013.

[16] Mozannar H, Sontag D. 2020. Consistent estimators for learning to defer to an expert. En Proceedings of the 37th International Conference on Machine Learning, PMLR 119, pp. 7076–7087. arXiv:2006.01862.

[17] Joyal A, Nielsen M, Winskel G. 1996. Bisimulation from open maps. Information and Computation 127(2), 164–185. doi:10.1006/inco.1996.0057.

[18] Nerode A. 1958. Linear automaton transformations. Proceedings of the American Mathematical Society 9(4), 541–544. doi:10.1090/S0002-9939-1958-0135681-9.

[19] Hellerstein JM. 2026. Complete CALM: A Coordination Criterion for Specifications. arXiv:2602.09435, v4, 14 de junio de 2026. Remitido por primera vez el 10 de febrero de 2026 con el título The Coordination Criterion. doi:10.48550/arXiv.2602.09435.

[20] Hellerstein JM. 2026. On the Complexity of Determinations. arXiv:2603.28031. Remitido por primera vez el 30 de marzo de 2026.

[21] Hellerstein JM. 2026. Determination Provenance: From Ambiguity to Algebra. arXiv:2606.10270. Remitido por primera vez el 9 de junio de 2026.
