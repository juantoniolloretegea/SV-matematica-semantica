# Orientación exacta con interfaces heterogéneas: constitución del episodio y sustitución que preserva la clausura

**Autor:** Juan Antonio Lloret Egea  
**Afiliación:** Instituto Tecnológico de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
**ORCID:** 0000-0002-6634-3351  
**Fecha:** 9 de agosto de 2026  
**Estado:** PREPRINT — NO REVISADO POR PARES  
[DOI: 10.21428/39829d0b.e5347310](https://doi.org/10.21428/39829d0b.e5347310)

> **English** — official IEEE wording
> 
This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.

> **Español**
Este trabajo ha sido enviado al IEEE para su posible publicación. Los derechos de autor podrán ser transferidos sin previo aviso, tras lo cual esta versión podría dejar de estar accesible.

## Resumen

Las interfaces heterogéneas de percepción e información pueden ser válidas por separado y, sin embargo, resultar conjuntamente insuficientes para constituir un episodio de decisión; también pueden aportar evidencias legítimas pero contradictorias que no deben eliminarse antes de la resolución. Los trabajos existentes abordan la planificación consciente de la incertidumbre, el filtrado de seguridad, la abstención, los contratos de interfaz, la admisión en tiempo de ejecución y la certificación de acciones, pero estos mecanismos no distinguen por sí solos entre un fallo previo a la resolución para constituir un episodio de orientación y una no clausura finita exacta; tampoco proporcionan un criterio, formulado en el nivel de los testigos, que permita preservar el perfil exacto de clausura alcanzable cuando se sustituyen interfaces.

Este trabajo desarrolla un marco finito para la orientación exacta con interfaces heterogéneas. Un contrato de orientación declarado induce un soporte estructural conservador, testigos tipados posteriores a la transducción, bases constitutivas, congruencias contextuales canónicas para los valores relevantes para la resolución y un sistema finito de resolución cociente. Se demuestra que la igualdad de las clases locales de resolución implica la igualdad de las firmas globales de resolución y que tres condiciones suficientes formuladas en el nivel de los testigos —congruencia local, preservación de las bases constitutivas y completitud de las clases locales— inducen sistemas de resolución cociente isomorfos y, por tanto, preservan el perfil exacto de clausura alcanzable. Las condiciones son suficientes, no necesarias. Ocho escenarios finitos diseñados para someter a contraste cada hipótesis delimitan su alcance y muestran por qué deben mantenerse separados la captura inválida, el episodio no constituido, la evidencia contradictoria, la no clausura certificada y la pérdida de un certificado de preservación.

**Palabras clave:** orientación formal; interfaces heterogéneas; sistemas de estados finitos; certificación de no clausura.

## 1. Introducción

Los sistemas autónomos y corpóreos rara vez dependen de un único canal de información. Una plataforma móvil o humanoide puede combinar cámaras, LiDAR, mapas, propiocepción, lenguaje, bases de datos externas y observaciones mediadas por programas informáticos. Por ello, el problema de ingeniería no consiste únicamente en cómo fusionar datos o elegir una acción, sino también en determinar cuándo la realización disponible de las interfaces constituye legítimamente el problema que un sistema de resolución debe resolver. Un sistema puede ser físicamente capaz de desplazarse e incluso disponer de una acción candidata segura y, aun así, carecer de la evidencia tipada exigida por el problema de orientación declarado. A la inversa, varias interfaces válidas pueden discrepar de una forma que deba conservarse en lugar de ser eliminada mediante una regla de fusión previa a la resolución.

En este trabajo, *orientación* se utiliza en un sentido propio de los sistemas formales: un dominio y una consulta declarados se conectan con un esquema finito de resolución mediante testigos tipados, trazables y posteriores a la transducción. Esta acepción es más restringida que la navegación en general y distinta del filtrado de seguridad. Los modelos de decisión parcialmente observable proporcionan procedimientos fundamentados para decidir con percepción incierta [1]; los filtros de seguridad supervisan o modifican controles candidatos para mantener la seguridad [2]; y las barreras de seguridad robóticas pueden impedir que planes inseguros alcancen la ejecución [3]. Ninguna de estas distinciones responde por sí sola a otra pregunta: si la evidencia heterogénea disponible constituye el episodio finito exacto cuyo perfil de clausura debe resolverse.

La distinción también es relevante para la abstención. Bancos de pruebas recientes sobre agentes corpóreos estudian cuándo un agente debe abstenerse de ejecutar porque una instrucción es ambigua, inviable, parte de una premisa falsa o no está respaldada por las modalidades sensoriales disponibles [4]; otros trabajos sobre abstención de agentes extienden la cuestión al uso secuencial de herramientas [5], [6]. La abstención es una política de ejecución o de interacción. El marco que se desarrolla a continuación plantea primero si existe un episodio de resolución bajo un contrato declarado; solo después de su constitución construye un sistema finito de resolución y calcula su perfil exacto de clausura alcanzable. Por tanto, un episodio no constituido no se codifica como veredicto negativo, como veredicto de baja confianza ni como no clausura certificada.

Un segundo problema es la sustitución de interfaces. Las teorías de componentes, los autómatas de interfaz y el razonamiento de tipo asumir–garantizar ofrecen formalismos maduros para la compatibilidad, el refinamiento y la sustitución segura [7], [8]. Trabajos recientes sobre agentes corpóreos también emplean contratos explícitos para la composición y actualización de capacidades [9]; la atestación componible estudia la confianza incremental y la reverificación cuando cambian componentes [10]. El problema que aquí se plantea es más específico: ¿bajo qué condiciones comprobables, formuladas sobre testigos tipados de interfaz, conserva una sustitución el conjunto exacto de clausuras binarias alcanzables de un sistema finito de resolución de orientación?

El trabajo presenta cuatro contribuciones. En primer lugar, define la constitución del episodio como un predicado binario previo a la resolución sobre testigos tipados posteriores a la transducción, con un certificado explícito y sin recodificar como no clausura certificada el fallo de constitución del episodio. En segundo lugar, deriva para cada parámetro relevante para la resolución una congruencia contextual canónica a partir de las semánticas declaradas de las guardas y de los terminales. En tercer lugar, demuestra un teorema de elevación que preserva la clausura: la congruencia local, la preservación de las bases constitutivas y la completitud de las clases locales realizadas implican igualdad de las firmas globales de resolución, isomorfismo de los sistemas de resolución cociente y preservación exacta del perfil de clausura. En cuarto lugar, aporta ocho escenarios finitos de contraste que atacan individualmente las hipótesis y las separaciones semánticas pretendidas.

### 1.1. Relación con preprints anteriores

Una línea de preprints del SV publicada entre marzo y junio de 2026 desarrolló varios ingredientes que motivan la formulación actual, pero no contiene su teorema de elevación. Los trabajos publicados el 17 de marzo formalizaron la transducción ternaria auditada y una interfaz visual estructurada [11], [12]; preprints posteriores abordaron el soporte observacional tipado y la admisibilidad y el conflicto intermodales [13], [14]. Un preprint de orientación del 22 de junio organizó una cadena dominio–interfaz–trayectoria–residual–retorno y separó explícitamente la navegación de la orientación formal [15]. Estas publicaciones se citan como genealogía documental y conceptual; no contienen el predicado de constitución del episodio, la congruencia contextual de resolución ni el teorema de elevación desde la interfaz hasta el sistema de resolución que se presentan aquí.

Un marco separado de no clausura finita, publicado el 8 de agosto de 2026, define el perfil exacto de clausura alcanzable, certificados de conjuntos alcanzables verificables por máquina y morfismos de recubrimiento de resolución [16]. La demostración de preservación del perfil que se presenta aquí es autosuficiente una vez establecido el isomorfismo entre los sistemas de resolución; el isomorfismo resultante también constituye una instancia de la noción de recubrimiento de aquel marco. El nuevo puente matemático de este trabajo se sitúa por encima de esa capa: deriva la preservación del sistema finito de resolución a partir de condiciones sobre interfaces, formuladas en el nivel de los testigos e indexadas por el propio sistema de resolución.

## 2. Trabajos relacionados y delimitación

### 2.1. Interfaces, contratos y verificación composicional

Los autómatas de interfaz modelan hipótesis de interacción y permiten razonar sobre compatibilidad y refinamiento [7]. Las teorías de tipo asumir–garantizar extienden el razonamiento composicional a los comportamientos de componentes y a la sustitución segura [8]. Estos enfoques establecen que la sustitución consciente de las interfaces y la preservación composicional no son ideas nuevas por sí mismas. Por ello, la contribución de este trabajo no consiste en afirmar genéricamente que los componentes puedan sustituirse de forma conservadora. El invariante observado queda fijado de manera concreta: el perfil exacto de clausura binaria alcanzable de un sistema finito de resolución de orientación. El teorema deriva ese invariante a partir de clases de equivalencia contextual de los valores de testigos posteriores a la transducción y de la cobertura en el nivel de constitución.

La distinción sigue siendo pertinente en sistemas corpóreos recientes. ECM Contracts codifica firmas funcionales, hipótesis, recursos, permisos, semántica de recuperación y compatibilidad entre versiones para módulos de capacidad de agentes corpóreos [9]. Composable Attestation formaliza pruebas modulares de integridad e integración incremental sin necesidad de repetir toda la atestación [10]. Proof-Carrying Agent Actions centra la gobernanza en tiempo de ejecución en certificados de acción y en puntos de control explícitos, como la admisibilidad previa a la acción, la aprobación y la clausura del resultado [17]. Estos sistemas gobiernan componentes, evidencias de confianza o acciones; el objeto que aquí se conserva es, en cambio, el perfil exacto de clausura de un sistema finito de resolución.

### 2.2. Incertidumbre, seguridad y abstención

Los POMDP modelan percepción ruidosa y control incierto mediante decisiones sobre estados de creencia [1]. Los filtros de seguridad proporcionan una visión modular de la supervisión y la intervención en tiempo de ejecución sobre controles candidatos [2], mientras que RoboGuard aplica especificaciones de seguridad contextualizadas a robots habilitados mediante modelos de lenguaje de gran tamaño [3]. Estos métodos responden a si una acción debe planificarse o modificarse bajo incertidumbre o restricciones de seguridad, y a cómo hacerlo. No convierten la constitución del episodio en un concepto equivalente a la seguridad.

RoboAbstention estudia instrucciones corpóreas que no deberían ejecutarse por ser ambiguas, inviables, basarse en premisas falsas o carecer de respaldo suficiente [4]; Agentic Abstention y AgentAbstain estudian decisiones relacionadas de actuar o abstenerse en agentes que utilizan herramientas de manera secuencial [5], [6]. La distinción aquí formulada es ortogonal: `ConstitΘ(W) = 0` significa que el sistema de resolución declarado no queda instanciado bajo el contrato `Θ`. No prescribe por sí mismo una acción de abstención, y `ConstitΘ(W) = 1` tampoco implica que el perfil final sea unitario.

### 2.3. Admisión y aseguramiento recientes en tiempo de ejecución

Trabajos de 2026 delimitan todavía más la frontera de novedad. En conducción autónoma, el aseguramiento en tiempo de ejecución a nivel de misión separa la admisibilidad de la misión de la seguridad de la plataforma y rechaza antes de la ejecución órdenes inviables para la misión [18]. Un marco posterior para enjambres agrega evidencia distribuida y representa explícitamente conclusiones negativas no sustentadas cuando se pierde evidencia [19]. Un marco de sistemas para inteligencia corpórea confiable separa las capas de modelo, sistema, evidencia y despliegue [20]. HALO utiliza admisión heterogénea con obligaciones localizadas para conservar los componentes de respuesta que siguen respaldados mientras se vuelven a comprobar las acciones concretas [21]. CoWAM combina comprobaciones tipadas de admisibilidad con contratos de coordinación e intervención selectiva sobre políticas [22]. Estos trabajos refuerzan la necesidad de evitar afirmaciones genéricas de novedad acerca de la admisión, los contratos, la revalidación o la intervención conservadora. El resultado presente es deliberadamente más restringido: la constitución precede a la resolución finita exacta, y la sustitución de interfaces se certifica mediante la preservación de clases locales indexadas por el sistema de resolución, que inducen firmas globales de resolución idénticas.

## 3. Marco matemático

### 3.1. Contratos finitos de orientación

Sea `Θ = (D, q, 𝔾)`  (1)

un contrato de orientación para el dominio `D` y la consulta `q`, con esquema finito de resolución con guardas `𝔾 = (X, 𝒜, E, x⋆, {gₑ}ₑ∈E, {tᵥ,ₓ}ᵥ∈{0,1},ₓ∈X)`.  (2)

Aquí `X` es finito, `𝒜` es un alfabeto finito de acciones, `E ⊆ X × 𝒜 × X` es una relación estructural de transición y `x⋆` es el estado inicial. Cada `gₑ` es una guarda booleana y `tᵥ,ₓ` determina, una vez fijada la valoración, la pertenencia de `x` al conjunto terminal `Tᵥ`.

Se supone que el esquema se encuentra en **forma normal con guardas**: `X`, `𝒜` y `E` son independientes de la valoración, y toda elección dependiente de esta que afecte a la disponibilidad de transiciones o a la terminalidad binaria se representa mediante una guarda o un predicado terminal. Por tanto, los destinos o acciones dependientes de parámetros deben expandirse en alternativas estructurales provistas de guardas.

Sea `X°` el conjunto de estados alcanzables desde `x⋆` en el grafo dirigido subyacente cuando toda guarda se sustituye por el predicado constantemente verdadero, y sea `E°` el conjunto de aristas estructurales cuyo origen pertenece a `X°`. Se define el soporte estructural conservador de resolución como `PΘˢᵗʳ = ⋃ₑ∈E° supp(gₑ) ∪ ⋃ₓ∈X°,ᵥ∈{0,1} supp(tᵥ,ₓ)`.  (3)

No se afirma que este soporte sea mínimo. Un análisis estático puede refinar (3); todos los resultados posteriores son relativos al contrato `Θ` declarado.

Para cada `p ∈ PΘˢᵗʳ`, sea `𝒱ₚ` un dominio finito de valores. Las guardas y los predicados terminales son aplicaciones totales sobre sus productos finitos declarados: `gₑ : ∏ₚ∈supp(gₑ) 𝒱ₚ → {0,1}`  (4) `tᵥ,ₓ : ∏ₚ∈supp(tᵥ,ₓ) 𝒱ₚ → {0,1}`.  (5)

La totalidad garantiza que toda valoración híbrida utilizada más adelante esté definida.

### 3.2. Testigos tipados y constitución contractual del episodio

Sea `W` una familia finita de **testigos posteriores a la transducción**. Un testigo `w` contiene `w = (role(w), val(w), μ(w))`,  (6)

donde `role(w) ∈ PΘˢᵗʳ`, `val(w) ∈ 𝒱role(w)` y `μ(w)` contiene metadatos estructurales, como tipo, referencia, unidad, dominio, procedencia e información declarada de integridad. Un testigo puede ser producido por una única interfaz física o por una transducción declarada en la que intervengan varias interfaces; por tanto, el primitivo de este marco es el testigo, no el sensor bruto.

Para cada `p`, un verificador local `Vₚ : W(p) → {0,1}`  (7)

comprueba únicamente la legitimidad local. Puede examinar el tipo, la pertenencia del valor a su dominio, la referencia, la procedencia y la integridad de la captura o transducción declarada, pero es **ciego respecto de la resolución**: no puede consultar otros valores de testigos, `ℱΘ` —que se define más adelante—, la pertenencia terminal, una clausura preferida ni el perfil final.

La compatibilidad estructural conjunta se define por `J(b) = J̃(μ ∘ b)`.  (8)

La proyección de metadatos `μ` excluye contenido de resolución: no contiene `rₚΘ(val(w))`, valores de guardas, valores terminales, un perfil esperado ni campos derivados de ellos. Por consiguiente, (8) no puede utilizarse como selector oculto de resultados.

Una **base constitutiva** es una aplicación `b : PΘˢᵗʳ → W`  (9)

que, para cada `p`, satisface `role(b(p)) = p` y `Vₚ(b(p)) = 1`,  (10)

y además `J(b) = 1`. Sea `ℬΘ(W)` el conjunto de tales bases. Se define `ConstitΘ(W) = 1 ↔ ℬΘ(W) ≠ ∅`.  (11)

La ecuación (11) tiene carácter contractual: `ConstitΘ(W) = 0` significa que el contrato `Θ` no certifica la constitución y que, por ello, `𝒪Θ[W]` no queda instanciado bajo `Θ`. No afirma que ningún contrato alternativo pueda constituir el episodio.

Un certificado de constitución `ζ` consta de una base candidata junto con las referencias necesarias para verificar sus entradas. Suponiendo decidibles `Vₚ` y `J̃`, se cumple `ConstitΘ(W) = 1 ↔ ∃ζ : VerifyConstitΘ(ζ) = 1`.  (12)

El fallo de este verificador es previo a la resolución. No se le asigna un veredicto binario ni un símbolo de no clausura.

Cada `b ∈ ℬΘ(W)` induce `ν_b(p) = val(b(p))`.  (13)

Bases válidas distintas pueden discrepar. Esa discrepancia se conserva deliberadamente.

### 3.3. Congruencia contextual canónica de resolución

Sea `ℱΘ = {gₑ : e ∈ E°} ∪ {tᵥ,ₓ : v ∈ {0,1}, x ∈ X°}`.  (14)

Para `p ∈ PΘˢᵗʳ` y `a ∈ 𝒱ₚ`, se define la firma contextual `κₚΘ(a) = ( f(η[p ↦ a]) )`,

donde los componentes recorren todo `f ∈ ℱΘ` tal que `p ∈ supp(f)` y toda valoración contextual `η ∈ ∏(q∈supp(f), q≠p) 𝒱q`.  (15)

Entonces `a ≡ₚΘ b ↔ κₚΘ(a) = κₚΘ(b)`.  (16)

Por tanto, `≡ₚΘ` es canónica respecto de la semántica declarada del sistema de resolución y constituye una relación de equivalencia. Sea `rₚΘ : 𝒱ₚ → 𝒱ₚ / ≡ₚΘ`  (17)

la aplicación cociente.

Para una valoración completa `ν`, se define la firma global de resolución `ρΘ(ν) = ((gₑ(ν))ₑ∈E°, (t₀,ₓ(ν))ₓ∈X°, (t₁,ₓ(ν))ₓ∈X°)`.  (18)

Para una base `b`, se define su vector local de clases `λΘ(b) = (rₚΘ(ν_b(p)))ₚ∈PΘˢᵗʳ`,  (19)

y los conjuntos realizados `ΛΘ(W) = {λΘ(b) : b ∈ ℬΘ(W)}`  (20) `𝒮Θ(W) = {ρΘ(ν_b) : b ∈ ℬΘ(W)}`.  (21)

**Lema 1. Congruencia local-a-global de resolución.** Si dos valoraciones `ν` y `ν′` satisfacen `rₚΘ(ν(p)) = rₚΘ(ν′(p))` para todo `p ∈ PΘˢᵗʳ`,  (22)

entonces `ρΘ(ν) = ρΘ(ν′)`.  (23)

**Demostración.** Enumérese `PΘˢᵗʳ = {p₁, …, pₖ}` y fórmense las valoraciones híbridas `ν⁽⁰⁾ = ν, …, ν⁽ᵏ⁾ = ν′`, sustituyendo una coordenada cada vez. En el paso `i`, (16) establece que sustituir `ν(pᵢ)` por `ν′(pᵢ)` preserva todo `f ∈ ℱΘ` en cualquier contexto de las coordenadas restantes; la totalidad garantiza que el contexto híbrido esté definido. Por tanto, `f(ν⁽ⁱ⁻¹⁾) = f(ν⁽ⁱ⁾)` para todo `f`. Encadenando todas las sustituciones se obtiene la igualdad de todos los componentes de (18). ◻

La implicación es deliberadamente unidireccional: vectores locales de clases distintos todavía pueden inducir una misma firma global.

### 3.4. Sistema finito exacto de resolución y cociente por firmas

Una base `b` instancia `ℛΘ[b] = (X, 𝒜, →_b, x⋆, T₀ᵇ, T₁ᵇ)`,  (24)

donde `(x,a,y) = e ∈ E` habilita `x →_bᵃ y` si y solo si `gₑ(ν_b) = 1`, y `Tᵥᵇ = {x ∈ X : tᵥ,ₓ(ν_b) = 1}`.  (25)

Todas las bases legítimas se conservan mediante una raíz común `x̂⋆` y una rama independiente por cada base. Formalmente, `X̂_W = {x̂⋆} ∪ (X × ℬΘ(W))`,  (26) `Â_W = 𝒜 ⊔ {ι_b : b ∈ ℬΘ(W)}`.  (27)

Para todo `b ∈ ℬΘ(W)`, `x̂⋆ →^(ι_b) (x⋆, b)`,  (28)

y cada transición habilitada de rama se define por `(x,b) →ᵃ (y,b) ↔ x →_bᵃ y`.  (29)

Sus conjuntos terminales son `T̂ᵥ = {(x,b) : x ∈ Tᵥᵇ}`.  (30)

Este sistema finito se denota `𝒪Θ[W]`.

Para cualquier sistema finito de resolución `ℛ`, se define el **perfil exacto de clausura alcanzable** [16] como `C_ℛ(x) = {v ∈ {0,1} : Reach_ℛ(x) ∩ Tᵥ ≠ ∅}`.  (31)

El perfil es el objeto primario. Si, una vez completado un episodio constituido, se desea un resumen ternario, puede hacerse corresponder `{0}` con `0`, `{1}` con `1` y todo perfil no unitario o vacío con `U`; no se define tal resumen cuando falla (11).

Varias bases físicas pueden inducir la misma `ρΘ`. Se define el sistema de resolución cociente con conjuntos de estados y acciones `X̂_W⋆ = {x̂⋆} ∪ (X × 𝒮Θ(W))`,  (32) `Â_W⋆ = 𝒜 ⊔ {ι_s : s ∈ 𝒮Θ(W)}`.  (33)

Para cada `s ∈ 𝒮Θ(W)`, `x̂⋆ →^(ι_s) (x⋆, s)`.  (34)

Si el componente de `s` correspondiente a la guarda `g_(x,a,y)` vale `1`, entonces `(x,s) →ᵃ (y,s)`.  (35)

Finalmente, `T̂ᵥ⋆ = {(x,s) : s(tᵥ,ₓ) = 1}`.  (36)

**Lema 2. Invariancia del perfil de clausura bajo el cociente por firmas.** `C_𝒪Θ[W](x̂⋆) = C_𝒪Θ⋆[W](x̂⋆)`.  (37)

**Demostración.** Las bases con la misma firma global inducen las mismas transiciones habilitadas y los mismos conjuntos terminales y, por tanto, idénticos perfiles de rama. El cociente conserva una copia por cada firma distinta. Eliminar ramas duplicadas no puede añadir ni eliminar un terminal binario alcanzable desde la raíz común. ◻

### 3.5. Sustitución de interfaces con preservación de la clausura

Se define el conjunto de testigos activos `W_act = {w ∈ W : ∃b ∈ ℬΘ(W), ∃p, b(p) = w}`.  (38)

Considérense dos realizaciones constituidas `W` y `W′` del mismo `Θ`. Una sustitución tipada consta de `mₚ : W′_act(p) → W(p)`  (39)

para cada `p ∈ PΘˢᵗʳ`.

Se imponen tres condiciones sustantivas.

**C2 — Congruencia local de resolución:** `val(w′) ≡ₚΘ val(mₚ(w′))` para todo `w′ ∈ W′_act(p)`.  (40)

**C3 — Preservación de bases constitutivas:** `b′ ∈ ℬΘ(W′) ⇒ m ∘ b′ ∈ ℬΘ(W)`.  (41)

**C4λ — Completitud de clases locales:** `∀λ ∈ ΛΘ(W), ∃b′ ∈ ℬΘ(W′) : λΘ(b′) = λ`.  (42)

Son condiciones suficientes y conservadoras; no se afirma que caractericen toda sustitución que preserve el perfil.

**Lema 3. Igualdad de las clases locales realizadas.** Bajo C2 y C3, `ΛΘ(W′) ⊆ ΛΘ(W)`.  (43)

Si además se cumple C4λ, `ΛΘ(W′) = ΛΘ(W)`.  (44)

**Demostración.** Para cualquier `b′ ∈ ℬΘ(W′)`, C3 proporciona `m ∘ b′ ∈ ℬΘ(W)`. Por C2, cada coordenada pertenece a la misma clase contextual antes y después de la aplicación, de modo que `λΘ(b′) = λΘ(m ∘ b′) ∈ ΛΘ(W)`. Esto demuestra una inclusión; C4λ proporciona la otra. ◻

**Lema 4. La igualdad de clases locales implica igualdad de firmas.** Si se cumple (44), entonces `𝒮Θ(W′) = 𝒮Θ(W)`.  (45)

**Demostración.** Tómese una firma cualquiera inducida por una base `b′` de `W′`. La igualdad de `Λ` proporciona una base `b` de `W` con el mismo vector local de clases. El Lema 1, local-a-global, da `ρΘ(ν_b′) = ρΘ(ν_b)`. La inclusión inversa es simétrica. ◻

**Teorema 1. Elevación con preservación de la clausura desde clases locales de interfaz.** Sean `W` y `W′` realizaciones constituidas mediante interfaces heterogéneas del mismo contrato finito de orientación `Θ`. Si una sustitución tipada (39) satisface C2, C3 y C4λ, entonces `𝒮Θ(W′) = 𝒮Θ(W)`,  (46)

los sistemas de resolución cociente son isomorfos, `𝒪Θ⋆[W′] ≅ 𝒪Θ⋆[W]`,  (47)

y `C_𝒪Θ[W′](x̂⋆) = C_𝒪Θ[W](x̂⋆)`.  (48)

**Demostración.** Los dos lemas anteriores proporcionan la igualdad de las firmas globales realizadas. Ambos sistemas de resolución cociente se construyen sobre el mismo conjunto estructural de estados y con una rama por firma. La aplicación canónica `Φ(x̂′⋆) = x̂⋆` y `Φ(x,s) = (x,s)` preserva y refleja, por tanto, todas las selecciones iniciales de rama, las transiciones interiores y las pertenencias terminales; es un isomorfismo de sistemas de resolución. En consecuencia, un terminal binario es alcanzable desde la raíz de uno de los sistemas cociente si y solo si el terminal correspondiente es alcanzable desde la raíz del otro, por lo que sus perfiles exactos de clausura son iguales. El Lema 2 proporciona entonces (48) para los sistemas no cocientados. El mismo isomorfismo es, con mayor razón, un morfismo de recubrimiento de resolución en el sentido del marco finito de no clausura certificada [16]. ◻

C4λ no cuantifica sobre `ρΘ`, `𝒪Θ`, los resultados terminales ni `C`. Cuantifica sobre vectores de clases contextuales locales. El puente no trivial desde esos vectores hasta las firmas globales es precisamente el Lema 1, local-a-global.

### 3.6. Límites y obstrucción por indistinguibilidad

El incumplimiento de C2–C4λ no demuestra que el perfil cambie. Dos realizaciones pueden inducir firmas distintas y, aun así, alcanzar únicamente el mismo terminal binario: `𝒮Θ(W′) ≠ 𝒮Θ(W)` mientras `C_𝒪Θ[W′] = C_𝒪Θ[W]`.  (49)

El teorema proporciona una vía verificable de conservación, no una caracterización necesaria.

Sea `Ω_D,Θᶜᵒⁿ = {ω : ConstitΘ(W(ω)) = 1}`.  (50)

**Proposición 1. Obstrucción por indistinguibilidad de resolución.** Sea `π_S : Ω_D,Θᶜᵒⁿ → Y_S` la representación de toda la información disponible a través de la familia de interfaces `S`. Si existen `ω₁, ω₂ ∈ Ω_D,Θᶜᵒⁿ` tales que `π_S(ω₁) = π_S(ω₂)` y `C(ω₁) ≠ C(ω₂)`,  (51)

entonces ninguna aplicación determinista `F : Y_S → 𝒫({0,1})` puede recuperar el perfil exacto de clausura para ambos estados.

**Demostración.** `F` recibe la misma entrada para ambos estados y, por tanto, devuelve la misma salida, mientras que los dos perfiles correctos son distintos. ◻

### 3.7. Alcance computacional

Todos los dominios y sistemas de resolución son finitos. La construcción exhaustiva de las equivalencias contextuales tiene un coste de evaluación, en el peor caso, acotado por `O( Σₚ∈PΘˢᵗʳ |𝒱ₚ|² · Σf∈ℱΘ,p∈supp(f) [ Π(q∈supp(f), q≠p) |𝒱q| ] · c_f )`,  (52)

donde `c_f` es el coste de evaluar `f`. Por tanto, en el peor caso el coste puede crecer exponencialmente con la aridad del soporte de los predicados; el teorema no presupone un comprobador barato de congruencia. Lenguajes de guardas restringidos pueden admitir, en cambio, procedimientos simbólicos de tipo SAT/SMT.

## 4. Evaluación reproducible

La evaluación tiene dos objetivos: someter independientemente a contraste las hipótesis del teorema y mostrar que el cociente según la semántica de resolución puede eliminar grandes multiplicidades de testigos físicos sin modificar el perfil exacto. Todos los ejemplos son finitos y pueden comprobarse exhaustivamente. El verificador determinista suplementario implementa contratos finitos, verificación local de testigos, compatibilidad estructural conjunta, enumeración de bases constitutivas, congruencia contextual, firmas locales y globales, sistemas de resolución brutos y cocientados, perfiles exactos de alcanzabilidad y las condiciones C2–C4λ; comprueba mecánicamente F1–F8 y los recuentos de escalado que se presentan a continuación.

### 4.1. Sistema de resolución común

Siete escenarios utilizan el conjunto común de estados `X = {x⋆, a, b, c, d, t₀, t₁}`,  (53)

con `p ∈ {0,1,2,3}` y `q,r ∈ {0,1}`. Las aristas con guardas son `x⋆ → a ↔ r = 1` y `x⋆ → b ↔ q = 1`,  (54) `a → c ↔ q = 1` y `b → c ↔ r = 1`,  (55) `c → t₀ ↔ p ∈ {0,2}` y `c → t₁ ↔ p = 1`,  (56) `c → d ↔ p = 3`, mientras que `d → t₀` es incondicional.  (57)

Los conjuntos terminales son `T₀ = {t₀}` y `T₁ = {t₁}`. Con `q = r = 1`, `p ∈ {0,2,3} ⇒ C = {0}` y `p = 1 ⇒ C = {1}`.  (58)

Sin embargo, `0 ≡ₚΘ 2`, `0 ≢ₚΘ 1` y `0 ≢ₚΘ 3`,  (59)

porque `p = 3` alcanza `t₀` mediante una estructura distinta de guardas.

El escenario F2 utiliza una guarda acoplada `g(p,q) = [p + q > 5]` para comprobar equivalencia contextual y no mera equivalencia puntual.

### 4.2. Batería de escenarios finitos de contraste

| ID | Objeto del contraste | Construcción | Perfil de referencia | Perfil tras la sustitución |
|---|---|---|---:|---:|
| F1 | Independencia de C2 | `W` realiza `p = 0`; `W′` realiza `p = 0,1`. La aplicación tipada envía ambos valores nuevos al testigo antiguo `p = 0`. Se cumplen C3 y C4λ; C2 falla en `1 ↦ 0`. | `{0}` | `{0,1}` |
| F2 | Congruencia contextual frente a congruencia puntual | Guarda `g = [p + q > 5]`. Valor antiguo `p = 2`, nuevo `p = 3`, con `q = 3,4` legítimos. Ambos coinciden para `q = 4`, pero discrepan para `q = 3`. | `{0,1}` | `{1}` |
| F3 | Independencia de C3 | El `W` antiguo contiene `p = 0` válido y un destino equivalente en contenido para `p = 1` cuya procedencia o referencia es estructuralmente incompatible. El `W′` nuevo contiene `p = 0,1` válidos. Se cumplen C2 y C4λ; la imagen de la base `p = 1` no es constitutiva. | `{0}` | `{0,1}` |
| F4 | Independencia de C4λ | `W` realiza clases locales para `p = 0` y `p = 1`; `W′` conserva únicamente la clase `p = 0`. C2 y C3 se cumplen para todos los testigos supervivientes. | `{0,1}` | `{0}` |
| F5 | Por qué la aplicación se restringe a `W′_act` | Se añade un testigo localmente válido que no puede participar en ninguna base porque su referente incumple `J`. Exigir una aplicación para él produciría un fallo espurio aunque ninguna rama cambie. | `{0}` | `{0}` |
| F6 | Por qué el primitivo es un testigo posterior a la transducción | Dos transducciones legítimas —por ejemplo, cámara+mapa y LiDAR+mapa— producen testigos válidos distintos para el mismo papel, con valores `0` y `1`. Una fusión prematura elimina una rama legítima. | `{0,1}` cuando se conservan ambos testigos | `{0,1}` cuando se conservan ambos testigos |
| F7 | Sustitución física sin igualdad de valores brutos | La tecnología antigua produce `p = 0` y la nueva `p = 2`. Los valores brutos difieren, pero `0 ≡ₚΘ 2`; se cumplen C3 y C4λ. | `{0}` | `{0}` |
| F8 | La suficiencia no implica necesidad | La realización antigua utiliza `p = 0` y una arista directa `c → t₀`; la nueva utiliza `p = 3` y el camino `c → d → t₀`. Las clases locales y las firmas difieren, pero los perfiles coinciden. | `{0}` | `{0}` |

### 4.3. Resultados de la batería de contraste

La tabla anterior establece hechos distintos, en lugar de repetir una misma prueba por supresión. F1 muestra que C2 no es redundante respecto del tipado de los papeles, la preservación de bases y la cobertura de clases locales. F2 descarta una relajación tentadora de C2 que exigiera coincidencia únicamente en el contexto observado en ese instante. F3 demuestra que la igualdad del contenido de resolución no convierte una imagen estructuralmente inadmisible en una base; C3 es necesaria para que la aplicación inducida entre ramas esté bien definida. F4 demuestra que C4λ es necesaria para obtener la inclusión inversa en `ΛΘ(W′) = ΛΘ(W)`. Es importante observar que C2+C3 ya impiden que la sustitución cree, en el lado de referencia, clases locales no representadas; C4λ evita la pérdida de clases antiguas, en vez de vigilar simétricamente clases «nuevas».

F5 comprueba que la evidencia inactiva no debe hacer fracasar un certificado de preservación. F6 muestra por qué la fusión de interfaces queda fuera de la semántica primitiva: varias interfaces brutas pueden contribuir legítimamente a un mismo testigo y varias transducciones legítimas pueden producir testigos contradictorios que deben sobrevivir hasta el sistema de resolución. F7 demuestra que el teorema no exige identidad física ni igualdad de valores brutos. F8 proporciona la frontera opuesta: el incumplimiento de las condiciones suficientes del teorema no implica que el perfil haya cambiado.

### 4.4. Familia de escalado mediante cocientes

Para aislar la multiplicidad de la semántica, considérense `k` parámetros con dominio de valores `{0,1,2,3}` y predicados que distinguen únicamente la paridad de cada parámetro. Entonces `{0,2}` y `{1,3}`  (60)

son las dos clases contextuales de cada parámetro. Si cada valor bruto se representa de forma independiente, el número de bases físicas es `4ᵏ`, mientras que el número de vectores locales de clases es `2ᵏ`. Una familia de guardas que exponga cada bit de paridad produce una firma global por cada vector local de clases. Los recuentos exactos son los siguientes.

| k | Bases brutas 4ᵏ | Firmas 2ᵏ | Reducción |
|---:|---:|---:|---:|
| 2 | 16 | 4 | 4× |
| 3 | 64 | 8 | 8× |
| 4 | 256 | 16 | 16× |
| 5 | 1024 | 32 | 32× |
| 6 | 4096 | 64 | 64× |
| 7 | 16384 | 128 | 128× |
| 8 | 65536 | 256 | 256× |

Se trata de recuentos combinatorios exactos, no de mediciones de tiempo de ejecución. Muestran por qué cocientar las bases físicas duplicadas antes de certificar la alcanzabilidad exacta puede reducir materialmente el sistema finito de resolución, preservando a la vez su perfil de clausura por el Lema 2.

## 5. Discusión

### 5.1. Qué significa —y qué no significa— la constitución del episodio

La ecuación (11) separa tres situaciones que con frecuencia se confunden en la práctica. En primer lugar, una observación o una transducción puede incumplir su verificador local; ese testigo simplemente no puede desempeñar un papel. En segundo lugar, todos los testigos locales pueden ser válidos individualmente y, sin embargo, no existir ninguna base conjuntamente compatible; en tal caso, el episodio no está constituido bajo `Θ`. En tercer lugar, un sistema finito de resolución ya constituido puede completarse y presentar un perfil exacto de clausura no unitario o vacío. Solo el tercer caso es una propiedad del espacio de estados ya resuelto.

La distinción sigue siendo útil incluso cuando una política externa hace corresponder finalmente varios casos con una misma reacción operativa, por ejemplo «no ejecutar». Un controlador de seguridad puede bloquear el movimiento porque una acción sea insegura; una política de abstención puede solicitar una aclaración porque la tarea esté insuficientemente especificada; y la capa de constitución definida aquí puede negarse a instanciar un sistema de resolución porque los papeles de evidencia declarados no estén respaldados de manera conjunta. Que las reacciones operativas coincidan no convierte en iguales los objetos semánticos subyacentes.

### 5.2. El conflicto no es un fallo de interfaz

La factorización de `J` y la ceguera de `Vₚ` respecto de la resolución son deliberadas. Si dos testigos legítimos discrepan, la capa de constitución no puede hacer desaparecer la discrepancia simplemente porque uno de los valores resulte más conveniente. Cuando ambos valores admiten bases constitutivas, las dos ramas sobreviven en `𝒪Θ[W]`. El perfil exacto puede ser entonces `C = {0,1}`,  (61)

lo que registra que ambas clausuras binarias son alcanzables. A la inversa, la evidencia inválida se filtra antes de la resolución. De este modo se separa la validez estructural del desacuerdo semántico.

### 5.3. Relación con la sustitución de componentes y el aseguramiento en tiempo de ejecución

El teorema de elevación no debe interpretarse como una nueva teoría general de la sustituibilidad de componentes. Los autómatas de interfaz y los marcos asumir–garantizar ya proporcionan resultados generales de sustitución [7], [8]. El teorema especializa el objetivo de preservación y lo conecta con evidencia heterogénea: las clases contextuales locales se definen mediante las guardas exactas y los predicados terminales del sistema de resolución de orientación. C4λ exige entonces que la sustitución realice todo vector local de clases de la referencia, sin cuantificar directamente sobre firmas globales ni sobre resultados terminales.

Esto también distingue el resultado de una reutilización genérica de evidencia. La atestación componible puede evitar repetir toda la atestación ante cambios incrementales [10], mientras que HALO conserva componentes cuyas obligaciones localizadas continúan respaldadas [21]. Aquí, una sustitución verificada junto con un certificado finito aceptado de alcanzabilidad puede formar un testigo compuesto de que el sistema de resolución de destino posee el mismo perfil de clausura [16]. La afirmación se limita deliberadamente: no se sostiene que el mismo objeto de certificado pueda transportarse, salvo que se construya explícitamente un nuevo certificado para el sistema de destino.

### 5.4. Interfaces mediadas por inteligencia artificial

Nada en el teorema exige que un testigo proceda de un sensor físico determinista. Un programa o un modelo aprendido puede producir un testigo candidato posterior a la transducción, siempre que `Vₚ`, los campos declarados de procedencia y las comprobaciones de compatibilidad conjunta establezcan su legitimidad local sin consultar el resultado deseado del sistema de resolución. Esto permite una frontera arquitectónica estricta: los mecanismos probabilísticos o estadísticos pueden proponer evidencia, mientras que la constitución y la semántica finita de resolución permanecen explícitas y deterministas. El trabajo no afirma que toda salida de un modelo aprendido pueda verificarse de este modo; el diseño del verificador sigue siendo específico de cada dominio.

## 6. Limitaciones

El marco es finito. Las dinámicas continuas, los dominios no acotados y las semánticas de guardas parcialmente definidas requieren una abstracción o una teoría diferente. El soporte estructural de (3) es conservador y puede exigir evidencia para ramas estructuralmente alcanzables que un análisis estático más fuerte pudiera demostrar inalcanzables. En consecuencia, `ConstitΘ(W) = 0` es una afirmación relativa al contrato declarado, no un teorema de imposibilidad sobre todos los contratos alternativos.

La teoría también trata extensionalmente la corrección específica del dominio de `Vₚ`, `μ` y `J̃`. Restringe qué información pueden examinar estos objetos para impedir que oculten una selección semántica, pero no determina si una calibración concreta de cámara, una regla de procedencia cartográfica o un criterio de interfaz biológica son científicamente correctos. Tales reglas deben declararse y justificarse en el dominio de aplicación correspondiente.

La congruencia contextual puede ser computacionalmente costosa, como explicita (52). Además, C2–C4λ son suficientes pero no necesarias para la igualdad del perfil de clausura; F8 demuestra que estructuras de resolución diferentes pueden converger al mismo perfil. Por ello, el teorema proporciona una vía conservadora de certificación y no una caracterización completa de todos los cambios de interfaz que preservan el perfil.

Finalmente, la evaluación es deliberadamente estructural. El verificador suplementario comprueba exhaustivamente las construcciones formales finitas empleadas en F1–F8 y en la familia de escalado, pero el estudio no afirma rendimiento empírico de navegación sobre un robot físico. Un estudio sobre hardware debería abordar la fiabilidad de sensores, la calibración, la latencia y la cobertura ambiental, cuestiones ortogonales al teorema aquí demostrado.

## 7. Conclusión

Este trabajo separa la constitución formal del episodio de la resolución finita exacta cuando intervienen interfaces heterogéneas. Un contrato de orientación declarado determina un soporte estructural conservador; los testigos posteriores a la transducción y verificados localmente forman bases constitutivas; las clases de equivalencia contextual capturan exactamente qué valores locales son indistinguibles para la semántica declarada de guardas y terminales. Los vectores locales de clases resultantes inducen firmas globales de resolución y un sistema finito de resolución cociente.

El resultado central establece que la congruencia local de resolución, la preservación de las bases constitutivas y la completitud de las clases locales bastan para que los sistemas de resolución cociente sean isomorfos y, por tanto, para preservar el perfil exacto de clausura alcanzable bajo sustitución de interfaces. La batería de escenarios de contraste muestra que cada condición sustantiva protege frente a un modo de fallo distinto y, al mismo tiempo, demuestra que el criterio no es necesario para la igualdad del perfil. La separación resultante es precisa: una captura inválida no es un episodio no constituido; un episodio no constituido no es una no clausura certificada; la evidencia válida pero contradictoria no es evidencia inválida; y no lograr establecer un certificado de preservación no demuestra que el resultado haya cambiado.

## Agradecimientos y declaración de uso de inteligencia artificial

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para la búsqueda bibliográfica, el contraste crítico de consistencia, la estructuración del manuscrito, la asistencia en la formalización matemática, el apoyo a la composición tipográfica y la edición lingüística en inglés. Grok 4.5 (xAI; interacción del 8 de agosto de 2026) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias sobre presentación y delimitación del trabajo. Todas las salidas de inteligencia artificial se trataron como insumos de investigación carentes de autoridad propia. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume plena responsabilidad por el manuscrito.

## Conflicto de intereses

El autor declara no tener conflictos de intereses.

## Referencias

[1] M. Lauri, D. Hsu y J. Pajarinen, “Partially observable Markov decision processes in robotics: A survey,” *IEEE Transactions on Robotics*, vol. 39, n.º 1, pp. 21–40, febrero de 2023.  
[2] K.-C. Hsu, H. Hu y J. F. Fisac, “The safety filter: A unified view of safety-critical control in autonomous systems,” *Annual Review of Control, Robotics, and Autonomous Systems*, vol. 7, pp. 47–72, 2024.  
[3] Z. Ravichandran, A. Robey, V. Kumar, G. J. Pappas y H. Hassani, “Safety guardrails for LLM-enabled robots,” 2025, arXiv:2503.07885, v1, 10 de marzo de 2025.  
[4] D. Yeke, E. S. Temirel, A. Shreekumar, B. Lee, D. Xu y Z. B. Celik, “The yes-man syndrome: Benchmarking abstention in embodied robotic agents,” 2026, arXiv:2605.20544, v1, 19 de mayo de 2026.  
[5] H. Luo, B. Wen y L. L. Wang, “Agentic abstention: Do agents know when to stop instead of act?” 2026, arXiv:2606.28733, v1, 27 de junio de 2026.  
[6] X. Liu, Y. E. Zhang, V. Kasprova, P. Rabbani, P. S. Zahraei, T. Zhang, A. Ebrahimpour-Boroojeny y V. Chandrasekaran, “AgentAbstain: Do LLM agents know when not to act?” 2026, arXiv:2607.10059, v1, 11 de julio de 2026.  
[7] L. de Alfaro y T. A. Henzinger, “Interface automata,” en *Proceedings of the 8th European Software Engineering Conference (ESEC/FSE)*, ACM, 2001, pp. 109–120.  
[8] C. Chilton, B. Jonsson y M. Kwiatkowska, “Compositional assume-guarantee reasoning for input/output component theories,” *Science of Computer Programming*, vol. 91, parte A, pp. 115–137, 2014.  
[9] X. Qin, S. Luan, J. See, C. Yang y Z. Li, “ECM contracts: Contract-aware, versioned, and governable capability interfaces for embodied agents,” 2026, arXiv:2604.13097, v1, 10 de abril de 2026.  
[10] S. Sun y S. Evans, “Composable attestation: A generalized framework for continuous and incremental trust in AI-driven distributed systems,” 2026, arXiv:2603.02451, v1, 2 de marzo de 2026.  
[11] J. A. Lloret Egea, “Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable,” preprint, publicado el 17 de marzo de 2026, doi: 10.21428/39829d0b.f471b07c.  
[12] J. A. Lloret Egea, “Formalización de una interfaz visual estructurada en el Sistema Vectorial SV,” preprint, publicado el 17 de marzo de 2026, doi: 10.21428/39829d0b.b96fee32.  
[13] J. A. Lloret Egea, “Primera forma legítima del frente de corpus observacional tipado del Sistema Vectorial SV,” preprint, publicado el 20 de marzo de 2026, doi: 10.21428/39829d0b.d8304be4.  
[14] J. A. Lloret Egea, “Modelo formal de admisibilidad olfativa e indeterminación intermodal en el Sistema Vectorial SV,” preprint, publicado el 21 de marzo de 2026, doi: 10.21428/39829d0b.51507a08.  
[15] J. A. Lloret Egea, “Orientación universal y geográfica, potencial del suceso e interfaz de dominio desde el universo y los seres biológicos: humanoide,” preprint, publicado el 22 de junio de 2026, doi: 10.21428/39829d0b.5e15cabb.  
[16] J. A. Lloret Egea, “No clausura certificada en sistemas finitos de resolución: certificados operativos, morfismos conservativos y complejidad de revisión,” preprint, publicado el 8 de agosto de 2026, doi: 10.21428/39829d0b.f0892864.  
[17] Z. Wang, “Proof-carrying agent actions: Model-agnostic runtime governance for heterogeneous agent systems,” 2026, arXiv:2606.04104, v1, 2 de junio de 2026.  
[18] C. Tsai y S. Hariri, “Mission-level runtime assurance framework for autonomous driving,” 2026, arXiv:2606.06996, v1, 5 de junio de 2026.  
[19] N. Kekatos, P. Katsaros, A. Lekidis, T. Nestoridis y T. Nianios, “Mission-level runtime assurance for LLM-assisted ISR swarms over a verification-aware fabric,” 2026, arXiv:2607.23532, v1, 26 de julio de 2026; versión actual v2, 31 de julio de 2026.  
[20] X. Yang, T. Chen, H. Su, M. Wang, C. Yu, Z. Tu *et al.*, “Towards trustworthy embodied intelligence: A systems framework and graded trustworthiness levels,” 2026, arXiv:2607.26121, v1, 28 de julio de 2026.  
[21] T. Park, K. Yoo, K. Kim, S. Yoo y H. Kim, “HALO: Heterogeneous admission through localized obligations for safe agentic execution,” 2026, arXiv:2607.27636, v1, 30 de julio de 2026.  
[22] S. Liu, Q. Wen, S. Hao, Q. Luo, C. Zhang, F. You, C. Wu y N. Su, “CoWAM: Coordination contracts for selective policy intervention with WAMs,” 2026, arXiv:2608.02578, v1, 3 de agosto de 2026.
