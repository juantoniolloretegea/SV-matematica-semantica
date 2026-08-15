# Aprendizaje trazable en inteligencia artificial: evolución estructural del conocimiento con frames ternarios y trazas acumulativas

**Autor:** Juan Antonio Lloret Egea  
**Institución:** Instituto Tecnológico de la Inteligencia Artificial para el Español (ITVIA)  
**Lugar:** Madrid, España  
**ORCID:** 0000-0002-6634-3351  
**DOI:** PENDIENTE DE ASIGNACIÓN  
[**Laboratorio asociado:**](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/fundamentos/aprendizaje-trazable-en-inteligencia-artificial/laboratorios)


## Resumen

Esta publicación desarrolla una semántica finita, determinista y autocontenida para el aprendizaje trazable en sistemas de inteligencia artificial que operan dentro de un dominio declarado de antemano por autoridad humana. El objeto formal central vincula un frame/vector ternario manifestado con una traza estructural de solo adición y un registro cognitivo. El aprendizaje se define como una evolución estructural que contiene al menos un incremento nuevo y sustentado. El soporte se establece mediante un certificado finito registrado cuyas hojas, aplicaciones de operadores, procedencia e incorporación pueden reconstruirse y comprobarse. La semántica distingue el aprendizaje del razonamiento, la composición, el crecimiento cardinal, la verdad, la mejora y la mera extensión de la traza. Contramodelos finitos establecen que el aprendizaje puede coexistir con la contracción del conocimiento activo y con la reapertura a `U` de una coordenada ternaria previamente sometida a clausura fuerte; que dos vectores locales extremos iguales no determinan si hubo aprendizaje; y que el razonamiento o la composición intercelular pueden producirse con aprendizaje o sin él. La realización de inteligencia artificial impone cuatro invariantes: los mecanismos estadísticos no pueden constituir aprendizaje ni clausura; los pasos de inferencia opacos son inadmisibles; las transiciones de máquina preservan el fundamento fijado bajo soberanía humana; y no se devuelve una clausura fuerte salvo que la base declarada la sustente. Una pequeña implementación determinista de referencia ejercita las definiciones finitas sobre ejemplos serializados, pero no se utiliza como oráculo de demostración. Un corolario de reconstrucción distingue la pérdida de un soporte local originario de la pérdida del conocimiento reconstruible cuando permanece disponible un código de reinicio adecuado.

**Palabras clave:** aprendizaje trazable; razonamiento automatizado; frames ternarios; certificados de soporte; evolución estructural del conocimiento; soberanía humana

## 1. Introducción

El término *aprendizaje* designa procesos formales y computacionales sustancialmente diferentes en inteligencia artificial (IA), métodos formales, razonamiento automatizado, educación, revisión de creencias y análisis de programas. En el aprendizaje activo de autómatas, un aprendiz identifica un modelo objetivo mediante consultas y contraejemplos [1, 2, 3]. En la teoría de espacios de conocimiento, un estado de conocimiento se modela como un subconjunto estructurado de un dominio de problemas [5]. En los sistemas de mantenimiento de la verdad y de revisión de creencias se introducen, retiran o revisan creencias y sus razones [6, 7, 8]. En el aprendizaje de cláusulas guiado por conflictos (CDCL), «aprender» designa la adición formalmente controlada de cláusulas dentro de un solucionador, junto con operaciones como el olvido y el reinicio [9, 10]. Estos usos son rigurosos en sus respectivos ámbitos, pero ninguno proporciona por sí solo el criterio parametrizado por dominio que aquí se estudia:

> Dadas dos fases declaradas del mismo sistema de IA, ¿en qué condiciones exactas constituye el cambio entre ellas aprendizaje trazable, y no mera ejecución, repetición, pérdida, recodificación, mutación sin soporte o actualización opaca?

Este artículo desarrolla ese criterio para una clase deliberadamente restringida de sistemas. No pretende formular una teoría universal de la cognición ni propone sustituir el aprendizaje automático estadístico. Estudia, en cambio, sistemas de IA en los que una afirmación de aprendizaje solo es admisible cuando el cambio pertinente es finito, reconstruible, acotado por un dominio y comprobable de manera independiente. La sección 3 vuelve a formular todas las convenciones ternarias, de frame, traza y célula necesarias para los resultados, de modo que el artículo pueda leerse con independencia del marco en el que tales convenciones se desarrollaron inicialmente. Las publicaciones anteriores del Sistema Vectorial (SV) se citan únicamente para dejar constancia de la procedencia de ese sustrato [18, 19, 20, 21, 22]; ningún teorema posterior exige importar una definición externa del SV. El nuevo objeto semántico estudiado aquí es el *aprendizaje*.

La proposición motivadora es deliberadamente sencilla: aprender es una evolución del conocimiento desde una fase `A` hasta una fase `B` en la que aparece un incremento reconocible dentro de un dominio declarado `D`. Convertir esa proposición en un criterio ejecutable exige cuatro separaciones. En primer lugar, el conocimiento ha de estar manifestado: un cambio interno que no está parametrizado ni registrado queda fuera del conocimiento formal certificado por el sistema. En segundo lugar, la evolución es estructural y ordinal; el tiempo físico transcurrido no es una primitiva. En tercer lugar, la presencia de un incremento no requiere crecimiento cardinal: una rectificación o una sustitución pueden constituir aprendizaje incluso cuando el conocimiento activo se contrae. En cuarto lugar, el soporte y la clausura no confieren autoridad. Una fuente, un cálculo interno o una conclusión de máquina no adquieren soberanía sobre el fundamento declarado por el ser humano por el mero hecho de estar disponibles o de obtenerse reiteradamente.

Seis aportaciones estructuran el artículo. Primera, se define una semántica finita de episodios para el conocimiento estructural manifestado, el soporte registrado, la evolución estructural, los incrementos sustentados y el aprendizaje. Segunda, se establecen la terminación y el determinismo del problema finito de decisión bajo hipótesis explícitas de finitud y decidibilidad. Tercera, contramodelos finitos muestran que el aprendizaje no es monótono por componentes ni reducible al crecimiento cardinal. Cuarta, se demuestra que los vectores locales extremos son insuficientes para decidir el aprendizaje. Quinta, se separan razonamiento y composición respecto del aprendizaje, incluido un criterio de esencialidad respecto del registro para atribuir soporte a una ejecución compositiva. Sexta, la realización de IA satisface un resultado de invariancia: cualquier secuencia finita de transiciones de máquina admisibles preserva el fundamento fijado bajo soberanía humana. El artículo se acompaña de una implementación determinista de referencia como ejemplo ejecutable de las definiciones; las demostraciones y los contramodelos no dependen de esa implementación.

## 2. Trabajos relacionados y frontera de la contribución

### 2.1. Aprendizaje exacto y activo

El marco `L*` de Angluin aprende lenguajes regulares a partir de consultas de pertenencia y equivalencia bajo un maestro mínimamente adecuado [1]. Desde entonces, el aprendizaje activo de autómatas se ha convertido en una metodología relevante de verificación para inferir modelos de máquinas de estados a partir de observaciones; las pruebas de conformidad y los aprendices escalables sensibles a los datos siguen siendo cuestiones activas [2, 3, 4]. Estos métodos proporcionan algoritmos de aprendizaje exacto para identificar modelos objetivo bajo sus respectivas hipótesis de consulta y equivalencia. El objeto considerado aquí es diferente: el artículo no intenta identificar un lenguaje objetivo desconocido ni inferir un autómata de caja negra. Pregunta si un cambio declarado en el propio conocimiento manifestado satisface un criterio de aprendizaje trazable, y una decisión positiva exige un certificado de soporte registrado para el incremento considerado.

### 2.2. Estados de conocimiento, revisión y cambio no monótono

La teoría de espacios de conocimiento representa el estado de una persona respecto de un dominio como un subconjunto de un conjunto especificado de problemas y estudia familias estructuradas de tales estados [5]. Proporciona, por ello, un precedente importante para tratar el conocimiento estructuralmente y no como una puntuación escalar. La semántica desarrollada aquí aborda un objeto diferente: el conocimiento manifestado se tipa en contenidos, relaciones y rutas; una historia estructural de solo adición se vincula a los frames del sistema; y el predicado de aprendizaje depende de un testigo registrado para un incremento estructural históricamente nuevo, no de la pertenencia a una familia de estados de conocimiento.

Los sistemas de mantenimiento de la verdad registran explícitamente justificaciones y revisan las creencias actualmente sostenidas cuando cambian los supuestos [6, 7]; la teoría AGM formaliza la contracción y la revisión de conjuntos de creencias mediante postulados y resultados de representación [8]. Estas tradiciones constituyen precedentes directos para tratar la retirada y la rectificación como operaciones de primer orden. No se reivindica aquí novedad alguna para la revisión en sí misma. El objeto distinto es un predicado de aprendizaje sobre un episodio finito que combina no clausura ternaria, trazas acumulativas, certificados de soporte registrados y un invariante separado de soberanía para las transiciones de máquina.

### 2.3. Aprendizaje de cláusulas, razonamiento asistido por aprendizaje y verificación de certificados

El término *aprendizaje* también es interno a la deducción automatizada. En SAT, Blanchette et al. formalizan en Isabelle/HOL un marco CDCL con aprendizaje, olvido, reinicio e incrementalidad [9]; de modo análogo, SCL(EQ) desarrolla un cálculo de aprendizaje de cláusulas para lógica de primer orden con igualdad en el que se exige que las cláusulas aprendidas no sean redundantes [10]. Estos resultados descartan directamente cualquier identificación general entre aprendizaje formal y almacenamiento monótono. Un uso diferente del término aparece en la demostración de teoremas asistida por aprendizaje: Kaliszyk y Urban combinan demostradores automatizados con selección de premisas mediante aprendizaje automático sobre el corpus Flyspeck [11]. El presente artículo no generaliza ninguno de esos cálculos ni mecanismos de aprendizaje. Define, en cambio, un predicado estructural que determina si un cambio registrado en conocimiento manifestado cuenta como aprendizaje dentro de la clase de sistemas estudiada.

El precedente metodológico más próximo para la implementación asociada es la validación independiente de certificados. El verificador de certificados SAT formalmente verificado de Lammich separa un generador complejo de un verificador más pequeño cuya corrección está formalmente demostrada [12]. Trabajos más recientes en *Journal of Automated Reasoning* mantienen este énfasis en la producción de pruebas y en el cómputo comprobable de forma independiente, incluida la generación distribuida de pruebas de insatisfacibilidad y el cómputo verificado dentro de demostradores HOL [13, 14]. La procedencia posee también precedentes formales independientes del dominio, entre ellos el modelo de datos W3C PROV [15]. Este artículo emplea una estructura de procedencia más estrecha, específica del episodio y vinculada a los incrementos de aprendizaje. El verificador asociado sigue el principio de separación de confianza únicamente como patrón de implementación: los resultados matemáticos se derivan de las definiciones y demostraciones del artículo, no de una ejecución satisfactoria del programa.

### 2.4. Información parcial, sucesos y procedencia histórica

La verificación de modelos trivalorada utiliza desde hace tiempo un tercer valor semántico para fórmulas que no pueden decidirse sobre espacios de estados incompletos [16], mientras que las estructuras de sucesos proporcionan una formulación clásica de sucesos, causalidad y conflicto [17]. Son formalismos vecinos pertinentes, pero no se identifican con los objetos ternarios definidos a continuación. En particular, el valor `U` utilizado aquí no es una probabilidad, una puntuación de confianza, un valor nulo, un código de error ni un punto medio numérico, y tampoco se divide en subclases. Una consulta ternaria legítima devuelve el mismo `U` irreducible siempre que el procedimiento exhaustivo declarado no sustente ninguna de las dos clausuras fuertes.

Las convenciones de célula, frame, traza y composición que se vuelven a formular en la sección 3 poseen una historia documentada en trabajos anteriores del SV [18, 19, 20, 21, 22]. Trabajos separados estudian la no clausura certificada y la autoridad bajo sustitución informacional [23, 24]. Estas citas establecen únicamente genealogía y fronteras de comparación. El presente artículo es formalmente autocontenido: su predicado de aprendizaje, sus testigos, contramodelos y resultado de soberanía utilizan solo definiciones e hipótesis expuestas aquí. La frontera comparativa es deliberadamente probatoria y no absoluta: la literatura examinada no aporta el mismo predicado a nivel de episodio, pero no se formula una afirmación universal de inexistencia bibliográfica.

## 3. Sustrato formal

### 3.1. Dominios, valores ternarios, células, frames y trazas acumulativas

Sea `D` un dominio declarado. El alfabeto ternario es:

`Σ = {0, 1, U}`

No se presupone ningún orden aritmético sobre `Σ`. El valor `U` no es una probabilidad, una puntuación de confianza, un valor numérico ausente ni un código de error. Los objetos mal formados se rechazan antes de la evaluación ternaria; no se representan mediante `U`. Una **clausura fuerte** es una decisión ternaria admisible perteneciente a `{0, 1}`; `U` denota no clausura bajo las condiciones declaradas.

Una célula ternaria finita tiene una base estructural `b ∈ ℕ`, con `b ≥ 3`, un tamaño `n = b²`, una familia ordenada de parámetros `P = (P₁, …, Pₙ)` y un vector de estado `v = (v₁, …, vₙ) ∈ Σⁿ`. Definimos:

`Nₐ(v) = |{k : vₖ = a}|`, para `a ∈ {0, 1, U}`.

Por tanto, `N₀(v) + N₁(v) + N_U(v) = n`, y el umbral fuerte se define como:

`T(n) = ⌊7n/9⌋`.

El clasificador celular empleado a lo largo del artículo es la aplicación determinista:

```text
κ(v) = NO_APTO        si N₁(v) ≥ T(n)
       APTO           si N₀(v) ≥ T(n)
       INDETERMINADO  en cualquier otro caso
```

La primera rama establece precedencia desfavorable de clausura. Como `T(n) > n/2` para todo `n = b²` admisible con `b ≥ 3`, las dos condiciones fuertes de recuento no pueden cumplirse simultáneamente. Las etiquetas son nombres de las tres clasificaciones celulares; no introducen orden ni aritmética sobre `Σ`.

Un **frame** `Fᵣ` es una realización manifestada e inmutable de una evaluación celular en el índice ordinal `r`. Su vector asociado es explícito: una realización proporciona un decodificador determinista y declarado `Vec_D` que satisface:

`Vec_D(Fᵣ) = vᵣ`.

Por tanto, el frame es una realización declarada del vector, y no una inferencia obtenida de su apariencia visual. Cualquier codificación gráfica, incluido el color, pertenece al nivel de interfaz y carece de fuerza semántica salvo declaración independiente. El par manifestado es:

`Mfrm(r) = (Fᵣ, vᵣ)`.

Un dato de transición `νᵣ` identifica los sucesos declarados y los cambios de parámetros inducidos necesarios para reconstruir la transición de `Fᵣ` a `Fᵣ₊₁`. Un segmento de traza acumulativa es:

`Γ[i:j] = (Fᵢ, νᵢ, Fᵢ₊₁, …, νⱼ₋₁, Fⱼ)`.

La extensión se realiza exclusivamente por adición y no admite mutación retrospectiva de frames. El orden de índices es estructural y ordinal; el tiempo físico transcurrido no es una primitiva. Para una fase `r`, el binomio frame–traza es:

`Bᵣ = ((Fᵣ, vᵣ), Γ[0:r])`.

El registro cognitivo que se introduce a continuación no es otra copia de `Γ`: constituye una capa tipada de manifestación cuyos registros apuntan a esta traza acumulativa o a entradas externas admitidas explícitamente. Esta distinción permite que dos episodios compartan los mismos vectores locales extremos y, sin embargo, difieran en su historia cognitiva.

Las convenciones de este apartado son completas para todos los teoremas del artículo. Su aparición anterior en el SV constituye procedencia bibliográfica, no una premisa importada [18, 19, 20, 21, 22].

### 3.2. Conocimiento manifestado

**Definición 1 (Conocimiento manifestado).** Para un sujeto `s` y un dominio `D`, el conocimiento manifestado en la fase `r` es:

`Knowᵣ(s,D) = (Xᵣ, Rᵣ, Λᵣ)`.

Aquí `Xᵣ` es un conjunto finito de contenidos tipados, `Rᵣ` un conjunto finito de relaciones tipadas y `Λᵣ` un conjunto finito de rutas, argumentos o enlaces de derivación reconstruibles y reconocidos.

La definición es deliberadamente extensional. Una capacidad tácita o una representación interna que no se manifiesta mediante un contenido, una relación, una ruta o un registro estructural declarados queda fuera de `Knowᵣ(s,D)`. Esta restricción es epistémica y operativa, no metafísica: el formalismo no prohíbe la existencia de estados internos adicionales ni afirma que el conocimiento no manifestado no exista. Afirma únicamente que tal estado no puede citarse, por sí solo, como incremento certificado de aprendizaje ni como testigo de soporte. Si un subsistema opaco o estadístico afecta a una entrada observable, ese observable debe atravesar una frontera admitida explícitamente antes de poder participar en la semántica que sigue.

**Definición 2 (Registro cognitivo y secuencia de registro).** Sea `T = {X, R, Λ}`. Un registro cognitivo es un objeto finito y tipado con identificador único, ordinal de registro, referencia de trayectoria, enlaces de procedencia y uno de los tipos siguientes:

`Seed_τ(z), Add_τ(z), Withdraw_τ(z), ExecReason(e), ExecComp(e), Prov(p)`, con `τ ∈ T`.

La secuencia cognitiva `Lᵣ(s,D) = (ℓ₀, …, ℓₘ)` es una secuencia finita y ordenada de esos registros inmutables. `Seed`, `Add` y `Withdraw` son los únicos tipos de registro que modifican directamente el conocimiento manifestado; el razonamiento ejecutado, la composición y la procedencia pueden sustentar esas modificaciones, pero no cambian por sí mismos la proyección activa.

El registro cognitivo no constituye una segunda trayectoria. `Γ` es la secuencia de frames y transiciones a nivel de sistema, mientras que `Lᵣ` registra qué objetos de la trayectoria —o qué entradas externas admitidas— poseen significación cognitiva. La proyección activa se obtiene mediante una aplicación secuencial, ordenada y determinista. Si `K = (X, R, Λ)` y `K[τ]` denota el componente seleccionado por `τ ∈ T`, la acción de un único registro se define como:

```text
Act_D(K, ℓ) = K con z activado en K[τ]       si ℓ = Seed_τ(z) o Add_τ(z)
              K con z desactivado en K[τ]    si ℓ = Withdraw_τ(z)
              K                              si ℓ = ExecReason(e), ExecComp(e) o Prov(p)
```

Un registro `Withdraw_τ(z)` está bien formado únicamente cuando `z` se encuentra activo inmediatamente antes de dicho registro. `Seed` solo se permite en el prefijo de inicialización. Reproducir `Lᵣ = (ℓ₀, …, ℓₘ)` desde el estado activo vacío y siguiendo el orden de registro produce:

`Act_D(Lᵣ) = Knowᵣ(s,D)`.

De este modo, la reproducción del registro cognitivo constituye una semántica operativa explícita y no una mera convención informal de anotación.

La relación de solo adición entre registros es exacta, no heurística. Escribimos:

`Lᵢ ⪯_D Lⱼ`

si, y solo si, existe un sufijo finito `S` tal que `Lⱼ = Lᵢ ‖ S`, donde `‖` denota concatenación de secuencias, y todo registro ya presente en `Lᵢ` es idéntico en todos sus campos dentro de `Lⱼ`: identificador, tipo, objetivo, referencia de trayectoria, procedencia y enlaces permanecen inalterados. Como el prefijo es exacto, el sufijo es único; se denota `Suf_D(Lᵢ,Lⱼ)`. Un registro posterior puede apuntar a un frame anterior, pero no insertarse retrospectivamente en el registro previo. Los registros `Seed` pertenecen exclusivamente al prefijo de inicialización de una realización y no pueden aparecer en el sufijo añadido por la máquina en un episodio de aprendizaje admisible; de lo contrario, una incorporación podría eludir la regla de soporte mediante una falsa clasificación como conocimiento inicial. Por ello, `Lᵢ ⪯_D Lⱼ` no implica `Knowᵢ ⊆ Knowⱼ`.

### 3.3. Equivalencia de representación declarada

La duplicación sintáctica no debe fabricar aprendizaje. Para cada tipo se supone, por tanto, una relación de equivalencia declarada y decidible:

`x ≡rep[D,X] x′`, `r ≡rep[D,R] r′`, `λ ≡rep[D,Λ] λ′`.

Los conjuntos cociente:

`X̄ = X / ≡rep[D,X]`, `R̄ = R / ≡rep[D,R]`, `Λ̄ = Λ / ≡rep[D,Λ]`

se utilizan únicamente para la comparación. Los procedimientos de equivalencia forman parte de la interfaz declarada del dominio y han de ser decidibles para la clase de episodios estudiada; la teoría no formula una afirmación de complejidad independiente del dominio sobre ellos. Los operadores de dominio se ejecutan sobre representantes concretos y tipados, y no se presupone congruencia de operadores arbitrarios respecto de la equivalencia de representación.

Definimos el universo de comparación etiquetado:

`Elem_D(Know) = ({X} × X̄) ⊎ ({R} × R̄) ⊎ ({Λ} × Λ̄)`.

La etiqueta impide confundir un contenido, una relación y una ruta que compartan el mismo nombre superficial.

Para un registro cognitivo `ℓ_q`, sean `Know(q−)` y `Know(q+)` los conocimientos activos inmediatamente antes y después de reproducir ese registro. Su delta cognitivo reducido por equivalencia de representación es:

`Δ_D(ℓ_q) = (Δ⁺_D(ℓ_q), Δ⁻_D(ℓ_q))`,

con:

`Δ⁺_D(ℓ_q) = Elem_D(Know(q+)) ∖ Elem_D(Know(q−))`,  
`Δ⁻_D(ℓ_q) = Elem_D(Know(q−)) ∖ Elem_D(Know(q+))`.

Así, una sustitución atómica por una forma concreta equivalente desde el punto de vista representacional posee delta cognitivo vacío, aunque cambie el representante concreto. Sea `Hist_D(L<q)` el conjunto de clases de representación etiquetadas que han aparecido en un registro `Seed` o `Add` antes de `q`. Una clase positiva `z ∈ Δ⁺_D(ℓ_q)` es **nueva en la historia** en `q` cuando `z ∉ Hist_D(L<q)`. La reactivación de una clase adquirida previamente y retirada después constituye, por tanto, recuperación y no un segundo incremento de esa misma clase; si la recuperación incorpora una ruta, relación o argumento nuevos y no equivalentes, ese nuevo objeto estructural sí puede ser históricamente nuevo.

### 3.4. Realización de IA bajo soberanía humana

La semántica subyacente concierne al conocimiento estructural manifestado. La realización de IA añade una capa de invariantes más estricta.

**Definición 3 (Fundamento bajo soberanía humana).** Para una autoridad humana `h` y un dominio `D`, sea `F_h^D` el objeto que contiene la frontera del dominio declarada por el ser humano, su semántica, el repertorio admisible de operadores, los criterios de clausura y la región certificada de validez `V_h^D`. La región no es temporal por definición; en una aplicación ordenada concreta puede adoptar la forma de un intervalo.

Un estado de máquina se escribe:

`Aᵣ = (F_h^D, Sᵣ, Trajᵣ)`,

siendo `Sᵣ = (Knowᵣ, Lᵣ)` el estado estructural de conocimiento. El conocimiento inicial contenido en `S₀` puede revisarse mediante aprendizaje legítimo. Por el contrario, la máquina carece de autoridad para reescribir el fundamento `F_h^D`.

Todo operador de máquina admisible `ω ∈ Ω_m^D` es una función parcial, determinista y declarada, con dominio, codominio, precondiciones y semántica explícitos, así como con un registro de ejecución reconstruible. Los cuatro invariantes siguientes definen la realización de IA estudiada en este artículo.

**I₁ — Base no estadística.** Ninguna operación es constitutiva de la semántica de aprendizaje si su validez, selección de candidatos, soporte, veredicto de aprendizaje o clausura dependen de frecuencia empírica, verosimilitud, confianza, muestreo, estimación estadística u optimización de una función de pérdida.

**I₂ — Ausencia de inferencia opaca.** Todo paso constitutivo es una operación matemática finita efectivamente ejecutada, perteneciente al repertorio declarado, realizada dentro de `D` y `V_h^D`, y con entradas y salidas reconstruibles.

**I₃ — Soberanía humana.** Para toda transición de máquina admisible `M`, se preserva la proyección del fundamento:

`π_F(M(A)) = F_h^D`.

Una revisión humana es una operación tipada independiente `Rev_h` y no pertenece a `Ω_m^D`. Cada episodio queda anclado a una versión identificada del fundamento. Si `Rev_h` modifica ese fundamento, el episodio vigente termina y todo episodio posterior se evalúa respecto de la nueva versión; la traza anterior permanece como historia y no se reinterpreta como si la revisión hubiera estado vigente retrospectivamente.

**I₄ — Clausura ternaria correcta.** Solo se devuelve una conclusión ternaria fuerte cuando la base declarada la clausura. Una consulta legítima que siga sin resolverse después de completar el procedimiento exhaustivo declarado devuelve el único valor `U`. Una consulta mal formada o fuera de dominio se rechaza, en lugar de traducirse a `U`.

## 4. Episodios, soporte, evolución y aprendizaje

### 4.1. Episodios admisibles

**Definición 4 (Episodio).** Un episodio es el objeto finito:

`E[i:j; s,D] = (s, D, F_h^D, Traj[i:j], Sᵢ, Sⱼ, R_E, ρ_E)`,

con `i < j` como fronteras ordinales declaradas; `R_E` es un registro finito del episodio que enlaza registros cognitivos con conocimiento previo, entradas externas admitidas, operadores ejecutados y referencias de trayectoria; y `ρ_E` es una política finita de soporte declarada.

Las fronteras del episodio determinan los correspondientes binomios frame–traza:

`Bᵢ = ((Fᵢ, vᵢ), Γ[0:i])` y `Bⱼ = ((Fⱼ, vⱼ), Γ[0:j])`.

Los registros cognitivos situados en esas fronteras quedan anclados mediante referencias tipadas de trayectoria. No se presupone una aplicación desde el estado cognitivo completo `Knowᵣ` al vector local `vᵣ`: ambas capas comparten episodio y traza, pero codifican información distinta. Esta distinción es esencial para el resultado de insuficiencia de los extremos de la sección 5.3.

Un episodio es admisible cuando están declarados `D`, `s` y `F_h^D`; `Traj[i:j]` está bien formada; los estados de conocimiento utilizan el mismo esquema declarado de equivalencia de representación; `Act_D(Lᵢ) = Knowᵢ` y `Act_D(Lⱼ) = Knowⱼ`; `Lᵢ ⪯_D Lⱼ`; el sufijo añadido no contiene registros `Seed`; todo operador invocado está declarado y satisface sus precondiciones; todo registro cognitivo está tipado; toda referencia de trayectoria se resuelve dentro de la traza acumulativa declarada o en una frontera externa admitida explícitamente; y tanto el registro del episodio como la política de soporte son finitos y están bien formados. Estas son condiciones de alcance para los resultados posteriores; no se afirma que constituyan un conjunto mínimo de supuestos.

### 4.2. Soporte registrado

**Definición 5 (Testigo válido de soporte).** Para un registro de incorporación `a = Add_τ(z)`, un testigo `W_a = (V_a, A_a, ℓ_a)` es un grafo dirigido, finito, acíclico y con raíz, registrado en `R_E`, que satisface:

1. toda hoja es conocimiento manifestado antes del segmento de derivación o una entrada externa admitida explícitamente bajo `D`;
2. todo nodo interno aplica un operador exacto declarado que fue efectivamente ejecutado y registrado;
3. la raíz `ℓ_a` produce el objetivo concreto `z` de `a`;
4. la reproducción del registro de incorporación `a` activa la clase de representación de `z` inmediatamente después de dicho registro, es decir, `(τ, [z]rep[D,τ]) ∈ Δ⁺_D(a)`; y
5. todo nodo pertenece a un camino dirigido hasta la raíz.

La condición 5 excluye nodos ornamentales. En particular, el mero acto de escribir `a` en el registro cognitivo no puede constituir su único testigo. Una afirmación procedente de una fuente externa se trata de forma conservadora: una observación admitida puede justificar el contenido `Afirma(f,p)` sin convertir automáticamente `p` en una proposición demostrada.

La política finita de soporte `ρ_E` identifica explícitamente los elementos manifestados previamente, las entradas externas admitidas, las ocurrencias de operadores ejecutadas y los registros de incorporación relevantes para el soporte del episodio, junto con los enlaces de dependencia admisibles y una familia finita de testigos candidatos `C_ρE(a)` para cada incorporación `a`. Sea `U_ρE` el universo finito declarado resultante. El registro del episodio es **completo respecto de `ρ_E`** cuando cada identificador de `U_ρE` se resuelve en exactamente un registro tipado de `R_E`, toda dependencia y todo testigo candidato declarado por `ρ_E` se encuentran serializados, y ningún testigo ajeno a `C_ρE(a)` es admisible como soporte histórico de `a` bajo esa política.

La completitud es, por tanto, relativa a la frontera del episodio y a la política de soporte declaradas; no afirma que se hayan enumerado todas las pruebas o fuentes concebibles fuera de `D`. La política `ρ_E` se fija como parte de la especificación del episodio, bajo el fundamento humano vigente, antes de evaluar el veredicto de aprendizaje. Sustituirla después de haber inspeccionado el resultado deseado crea una especificación de episodio distinta, no una reinterpretación silenciosa del mismo episodio. La semántica es, por consiguiente, explícitamente relativa a la política de soporte declarada; no afirma que esa política sea racional de manera única, óptima globalmente ni adecuada para un dominio por el mero hecho de ser finita y estar bien formada.

Para un registro concreto de incorporación `a = Add_τ(z)`, sea `W_E(a) ⊆ C_ρE(a)` el subconjunto finito de testigos candidatos serializados que satisfacen la Definición 5.

**Definición 6 (Soporte histórico).** Para un registro de episodio completo respecto de `ρ_E`:

`Supp_D(a,E) ⇔ W_E(a) ≠ ∅`.

`Supp_D` es una proposición, no un valor ternario. Una consulta operativa posterior acerca de si el soporte histórico todavía puede verificarse a partir del registro conservado es independiente y puede devolver `U` cuando se ha completado el procedimiento exhaustivo de acceso declarado, pero el registro retenido no permite sustentar una decisión fuerte. A la inversa, si no se ha establecido la completitud respecto de `ρ_E`, el fracaso al recuperar un testigo no establece la negación del soporte histórico.

### 4.3. Evolución estructural

Sea `Cog_D(L)` la secuencia finita de deltas cognitivos no vacíos, reducidos por equivalencia de representación, `Δ_D(ℓ_q)`, generados al reproducir los registros `Seed`, `Add` y `Withdraw` del registro cognitivo. Los registros `ExecReason`, `ExecComp`, los registros exclusivamente de procedencia y los metadatos administrativos se excluyen, salvo que manifiesten una nueva relación o ruta mediante un registro `Add` tipado.

**Definición 7 (Evolución estructural).** Para un episodio admisible:

`Evol_D(E) ⇔ Lᵢ ⪯_D Lⱼ ∧ existe ℓ_q ∈ Suf_D(Lᵢ,Lⱼ) tal que Δ⁺_D(ℓ_q) ∪ Δ⁻_D(ℓ_q) ≠ ∅`.

Esta definición permite evolución estructural por pérdida exclusivamente. También permite que la proyección activa actual vuelva a un valor anterior después de una adquisición seguida de una retirada, porque los registros intermedios permanecen presentes de forma inmutable. Por ello:

`Knowᵢ = Knowⱼ`

no implica ausencia de evolución.

### 4.4. Incrementos sustentados

Un incremento sustentado se vincula a la ocurrencia de incorporación en la que la novedad estructural entra por primera vez en la historia cognitiva, y no simplemente a una diferencia entre conjuntos de estados finales.

**Definición 8 (Incremento sustentado).** Para un episodio admisible y completo respecto de `ρ_E`:

```text
Inc_D(E) = {(q, τ, [z]rep[D,τ]) :
            ℓ_q = Add_τ(z) pertenece a Suf_D(Lᵢ,Lⱼ),
            (τ, [z]rep[D,τ]) pertenece a Δ⁺_D(ℓ_q),
            (τ, [z]rep[D,τ]) no pertenece a Hist_D(L<q),
            y Supp_D(ℓ_q,E)}.
```

La definición impide que la redundancia fabrique aprendizaje adicional. Varios testigos de una misma incorporación no crean varios incrementos; un duplicado representacional posee delta positivo vacío; y la reactivación de una clase previamente adquirida y posteriormente retirada constituye recuperación, no un segundo incremento de la misma clase. Una nueva ruta de demostración registrada para un contenido ya conocido puede constituir por sí misma un incremento nuevo en `Λ`, aunque el contenido no vuelva a aprenderse.

**Definición 9 (Aprendizaje trazable).** Para un episodio admisible y completo respecto de `ρ_E`:

`Learn_D(E) ⇔ Evol_D(E) ∧ Inc_D(E) ≠ ∅`.

El aprendizaje es, por tanto, una clase particular de evolución estructural. No se identifica con la verdad, la mejora, el crecimiento monótono, el razonamiento, la composición ni la mera extensión de la traza.

### 4.5. Veredicto operativo de aprendizaje

La proposición histórica `Learn_D(E)` es distinta de una decisión operativa presente basada en un registro que puede estar incompleto o ser parcialmente inaccesible. El veredicto ternario solo se evalúa después de completar el procedimiento declarado de acceso y agotamiento de la consulta.

**Definición 10 (Veredicto operativo).** Para una vista actual bien formada `E*` de un episodio, una vez completado el procedimiento exhaustivo declarado:

`DecLearn_D(E*) ∈ {LEARN, NO_LEARN, U}`,

con:

```text
DecLearn_D(E*) = LEARN     si un registro retenido y completo respecto de ρ_E establece Learn_D(E)
                 NO_LEARN  si un registro retenido y completo respecto de ρ_E establece ¬Learn_D(E)
                 U         si la consulta es admisible, se ha agotado y ninguna base retenida
                           clausura ninguno de los dos veredictos fuertes
```

Un episodio mal formado o fuera de dominio no recibe `U`; no supera el juicio de entrada.

## 5. Resultados principales

### 5.1. Decisión finita y comprobación independiente

**Teorema 1 (Terminación y determinismo de la comprobación de episodios).** Sea `E` un episodio finito admisible tal que: a) la equivalencia de representación es decidible; b) todo testigo de soporte está serializado explícitamente como un grafo finito; c) el registro del episodio es completo respecto de `ρ_E` bajo la política finita de soporte; y d) todo operador de dominio utilizado por un testigo es una función parcial determinista con precondiciones decidibles. Entonces los predicados `Supp_D(a,E)`, `Evol_D(E)` y `Learn_D(E)` son decidibles mediante un verificador determinista que termina.

**Demostración.** El episodio contiene un número finito de registros cognitivos y un número finito de testigos de soporte serializados, cada uno representado mediante un grafo finito. La decidibilidad de la equivalencia de representación produce conjuntos finitos de comparación reducida. Cada testigo puede comprobarse respecto de aciclicidad, tipado de hojas, pertenencia de operadores, satisfacción de precondiciones, reproducción de cada operador determinista, igualdad en la raíz y pertenencia de la incorporación resultante; bajo las hipótesis enunciadas, todas esas comprobaciones terminan. Por tanto, la familia finita de candidatos `C_ρE(a)` puede enumerarse y comprobarse, lo que hace decidible `W_E(a)` para cada registro serializado de incorporación `a`. La extensión exacta por prefijo de registros finitos y los deltas cognitivos de cada registro son igualmente decidibles; en consecuencia, también lo es `Evol_D(E)`. Por último, `Inc_D(E)` es un conjunto finito filtrado y `Learn_D(E)` es la conjunción de una proposición decidible con la prueba decidible `Inc_D(E) ≠ ∅`. El determinismo se sigue de los operadores deterministas junto con las políticas fijas de comparación y soporte. **Q. E. D.**

No se afirma ninguna cota de complejidad independiente del procedimiento declarado de equivalencia y de los costes de los operadores. La implementación de referencia registra el tamaño serializado de cada objeto comprobado y no realiza búsqueda de teoremas más allá del episodio suministrado.

### 5.2. El aprendizaje no es monótono ni equivale a crecimiento cardinal

Definimos la inclusión por componentes sobre el conocimiento manifestado reducido por equivalencia de representación mediante:

`Know̄ᵢ ⊑_D Know̄ⱼ ⇔ X̄ᵢ ⊆ X̄ⱼ ∧ R̄ᵢ ⊆ R̄ⱼ ∧ Λ̄ᵢ ⊆ Λ̄ⱼ`.

**Teorema 2 (Aprendizaje no monótono).** Existe un episodio finito admisible `E` tal que `Learn_D(E)` es verdadero y, al mismo tiempo:

`¬(Know̄ᵢ ⊑_D Know̄ⱼ)`

y

`|X̄ⱼ| < |X̄ᵢ|`.

**Demostración.** Sea:

`Knowᵢ = ({α, β, γ}, ∅, ∅)`.

Admitimos un suceso externo `ε` y ejecutamos un operador exacto declarado `ω_inv(β, ε) = δ`. Se registra un testigo válido cuyas hojas son `β`, ya manifestado, y `ε`, admitido, y cuya raíz es la incorporación de `δ`. Sea:

`Knowⱼ = ({α, δ}, ∅, ∅)`.

Supongamos que los cuatro símbolos son mutuamente no equivalentes bajo `≡rep[D,X]`. Extendemos `Lᵢ` mediante el sufijo finito e inmutable formado por `Add_X(δ)`, con su testigo registrado, seguido de `Withdraw_X(β)` y `Withdraw_X(γ)`. Por tanto, `Lᵢ ⪯_D Lⱼ`, y el sufijo añadido contiene un delta cognitivo positivo no vacío y deltas negativos no vacíos; en consecuencia, `Evol_D(E)` es verdadero. Si `q` es el ordinal del registro `Add_X(δ)`, entonces `[δ]` no ha aparecido en la historia cognitiva anterior y esa incorporación posee soporte histórico, de modo que `(q, X, [δ]) ∈ Inc_D(E)`. Se sigue que `Learn_D(E)` es verdadero. Sin embargo, en la fase final `[β]` y `[γ]` están ausentes del contenido activo, lo que establece tanto la falta de inclusión como `2 < 3`. **Q. E. D.**

Por tanto, el aprendizaje trazable no implica crecimiento cardinal del conocimiento activo ni monotonía por componentes.

La misma construcción puede incluir una reevaluación legítima de una coordenada celular local desde un valor fuerte hasta `U`. El objeto aprendido es la estructura sustentada de rectificación, no `U` en sí mismo. El aprendizaje puede, por consiguiente, coexistir con la reapertura de una clausura previamente fuerte sin interpretar `U` como una mejora.

### 5.3. Los vectores extremos no determinan el aprendizaje

**Teorema 3 (Insuficiencia de los extremos locales).** Para todo tamaño admisible de célula ternaria `n = b²`, con `b ≥ 3`, no existe un clasificador universal:

`f : Σⁿ × Σⁿ → {FALSO, VERDADERO}`

que decida `Learn_D(E)` a partir únicamente de los dos vectores locales extremos para todos los episodios admisibles.

**Demostración.** Fijemos cualquier tamaño admisible `n = b²`, con `b ≥ 3`. Construimos dos episodios `E_R` y `E_L` con el mismo sujeto, dominio, célula, evaluador, equivalencia de representación, repertorio de operadores, conocimiento manifestado inicial, vector local inicial `vᵢ` y vector local final `vⱼ`. Elegimos una coordenada `k` tal que `vᵢ(k) ∈ {0,1}` y `vⱼ(k) = U` en ambos episodios, y mantenemos idénticas las restantes `n − 1` coordenadas en los dos casos.

En `E_R`, un nuevo suceso admitido y un operador exacto producen un registro sustentado de rectificación `δ`, mientras se retiran contenidos activos obsoletos. Por ello, `Inc_D(E_R) ≠ ∅` y `Learn_D(E_R)` es verdadero.

En `E_L`, la misma transición local de un valor fuerte a `U` acompaña a una retirada registrada causada exclusivamente por la pérdida de soporte de un elemento activo. No se añade ningún registro cognitivo positivo, de modo que `Inc_D(E_L) = ∅`. Puede existir evolución estructural por pérdida, pero `Learn_D(E_L)` es falso.

Como el par `(vᵢ, vⱼ)` es idéntico en ambos episodios mientras que las proposiciones de aprendizaje difieren, ninguna función del par de extremos locales por sí solo puede decidir correctamente el aprendizaje en ambos. **Q. E. D.**

Este resultado explica por qué la relación frame–traza es semánticamente necesaria: un vector local es solo una proyección del episodio, no un certificado completo de aprendizaje.

### 5.4. Razonamiento y aprendizaje son separables

**Definición 11 (Razonamiento interno ejecutado).** `Reason_D(E)` es verdadero cuando el episodio contiene un grafo interno de derivación finito, acíclico y efectivamente ejecutado, cuyas hojas ya estaban manifestadas antes del segmento de derivación, cuyos nodos internos aplican operadores internos exactos declarados y cuya ejecución puede reconstruirse a partir del registro del episodio. La mera derivabilidad lógica sin ejecución registrada no satisface `Reason_D`.

**Teorema 4 (Separabilidad en cuatro casos).** Dentro de un mismo dominio finito existen episodios admisibles que realizan las cuatro conjunciones siguientes:

```text
Reason_D(E_A)  ∧  Learn_D(E_A)
Reason_D(E_B)  ∧  ¬Learn_D(E_B)
¬Reason_D(E_C) ∧  Learn_D(E_C)
¬Reason_D(E_D) ∧  ¬Learn_D(E_D)
```

**Demostración.** Sea `ρ(α) = β` un operador interno exacto declarado. En `E_A`, partimos de `Xᵢ = {α}`, ejecutamos `ρ` e incorporamos el nuevo `β` sustentado; ambos predicados son verdaderos. En `E_B`, partimos de `Xᵢ = {α, β}` y ejecutamos la misma derivación. El razonamiento queda registrado, pero no se incorpora ningún registro cognitivo positivo históricamente nuevo, por lo que no hay aprendizaje. En `E_C`, admitimos un observable externo `o_γ` y aplicamos una transducción de adquisición declarada `μ(o_γ) = γ`; `γ` se incorpora sin una derivación interna desde conocimiento previo, por lo que hay aprendizaje, pero no razonamiento interno. Finalmente, en `E_D`, ejecutamos una transición legítima y no cognitiva del sistema que modifica al menos un parámetro del sistema —como exige el esquema de trayectoria declarado—, pero no modifica ningún registro cognitivo ni ejecuta una derivación interna. Ninguno de los dos predicados es verdadero. **Q. E. D.**

### 5.5. La composición puede sustentar aprendizaje sin ser aprendizaje

Una composición en serie mantiene formalmente diferenciados la evaluación de la célula fuente, la aplicación del conector, la actualización del puente y la reevaluación de la célula destino. Para la construcción utilizada aquí, una ocurrencia de ejecución `e_σ` serializa las cuatro etapas y la actualización de trayectoria resultante; no se requiere ninguna definición externa de composición.

Consideremos dos células `3 × 3`, por tanto `n = 9` y `T(9) = 7`. Sea:

`v₁ = (0,0,0,0,0,0,0,0,1)`,

por lo que la fuente se clasifica como `APTO`. Sea el conector:

```text
φ(APTO)          = 0
φ(NO_APTO)       = 1
φ(INDETERMINADO) = U
```

Tomemos como estado destino:

`v₂ = (1,1,1,0,0,0,0,0,0)`,

que posee `N₀ = 6`, `N₁ = 3` y, por tanto, se clasifica como `INDETERMINADO`. Una transmisión en serie por el puente `k = 1` produce:

`ṽ₂ = (0,1,1,0,0,0,0,0,0)`,

con `N₀ = 7`, de modo que el destino se reevalúa como `APTO`. La operación ejecutada es:

`C₁ —σ[1,φ]→ C₂`.

Sea `e_σ` esta ejecución concreta, no el operador abstracto. Sea `Exec_σ(E)` la proposición que indica que el episodio registra una ejecución bien formada con evaluación de la fuente, salida del conector, actualización del puente, reevaluación del destino y una transición legítima de trayectoria.

Sea `δ` la relación cognitiva que expresa que esta ejecución en serie declarada produjo durante el episodio la reevaluación registrada del destino de `INDETERMINADO` a `APTO`. En un episodio `E⁺` con `δ ∉ Rᵢ` y `δ ∈ Rⱼ`, un testigo válido de soporte para `δ` contiene la rama fuente, el conector, `σ[1,φ]`, la reevaluación del destino y la incorporación posterior al conocimiento. Entonces `Exec_σ(E⁺) ∧ Learn_D(E⁺)`.

En un episodio `E⁰` con la misma arquitectura y la misma ejecución, pero con `δ ∈ Rᵢ = Rⱼ`, el conjunto de incrementos está vacío y `Exec_σ(E⁰) ∧ ¬Learn_D(E⁰)`.

**Proposición 1 (La ejecución no implica aprendizaje).**

`Exec_σ(E) ⇏ Learn_D(E)`.

Existen, no obstante, episodios admisibles en los que una ejecución de este tipo participa en un testigo válido de soporte para un incremento aprendido.

**Demostración.** El episodio `E⁰` anterior es un contramodelo finito: `Exec_σ(E⁰)` es verdadero, mientras su conjunto de incrementos está vacío y, por tanto, `Learn_D(E⁰)` es falso. El episodio `E⁺` muestra asimismo que una ejecución del mismo tipo puede participar en un testigo válido de soporte del aprendizaje. **Q. E. D.**

Para la atribución, fijemos una ocurrencia concreta de incorporación `a_z = Add_τ(z)` y definamos `CompSupp_σ(a_z,E)` cuando al menos un testigo válido registrado para `a_z` contiene la ocurrencia de ejecución `e_σ` como nodo de operador.

**Definición 12 (Composición esencial respecto del registro).** Supuesto que el registro del episodio es completo respecto de `ρ_E` para `a_z`:

`EssRec_σ(a_z,E) ⇔ W_E(a_z) ≠ ∅ ∧ para todo W ∈ W_E(a_z), e_σ ∈ V_W`.

**Proposición 2 (Jerarquía de composición).** Para un registro de episodio completo respecto de `ρ_E`:

`EssRec_σ(a_z,E) ⇒ CompSupp_σ(a_z,E) ⇒ Exec_σ(E)`,

mientras que, en general, fallan ambas recíprocas.

**Demostración.** Las implicaciones directas se siguen inmediatamente de las definiciones. La primera recíproca falla en un modelo con dos testigos válidos de soporte para el mismo `z`, uno de los cuales contiene `e_σ` y el otro es independiente de esa ejecución. La segunda recíproca falla en `E⁰`, o en un episodio donde se ejecuta la composición mientras una adquisición externa independiente aporta el único incremento aprendido. **Q. E. D.**

La calificación «esencial respecto del registro» es deliberada: la necesidad es relativa al registro completo de soporte declarado y no afirma causalidad metafísica ni física.

### 5.6. La soberanía es invariante bajo aprendizaje de máquina admisible

**Teorema 5 (Ausencia de escalada de autoridad bajo secuencias finitas de transiciones de máquina).** Sea:

`A₀ —M₀→ A₁ —M₁→ … —M(q−1)→ A_q`

cualquier secuencia finita de transiciones de máquina admisibles, incluidas transiciones cuyos episodios satisfacen `Learn_D`. Si toda `Mᵣ` satisface el invariante `I₃`, entonces:

`π_F(A_q) = π_F(A₀) = F_h^D`.

**Demostración.** Por `I₃`, `π_F(Aᵣ₊₁) = π_F(Aᵣ)` para todo `r`. La inducción sobre la longitud de la secuencia finita de transiciones proporciona, por tanto, la igualdad entre las proyecciones inicial y final del fundamento. **Q. E. D.**

El resultado es independiente de cuánto conocimiento se haya aprendido. En particular, ninguna secuencia finita de transiciones de máquina admisibles puede ejecutar una operación `Rev_h` que cambie el fundamento en un estado donde dicha operación modifica la proyección `π_F`. Una máquina puede detectar y registrar un conflicto entre un resultado derivado y `F_h^D`, pero ese conflicto no le confiere autoridad para modificar `F_h^D`. La revisión del fundamento exige la operación humana distinta `Rev_h`, que crea una nueva versión trazable en vez de reescribir silenciosamente la versión histórica.

## 6. Realización mediante célula de conocimiento y reconstrucción

### 6.1. Código estructural finito en lugar de enumeración exhaustiva

La semántica formal del aprendizaje no exige que una célula enumere todos los elementos del conocimiento futuro. Una realización puede utilizar, en cambio, un código estructural finito como especificación generativa o de reinicio, sin tratar la célula como un catálogo exhaustivo de todos los estados que puedan desarrollarse posteriormente.

Sea:

`Cconᵣ = (Cconᵣ, Πᵣ, Lᵣ)`

una realización mediante célula de conocimiento, donde `Cconᵣ` es una célula ternaria bien formada según la sección 3.1, `Πᵣ` declara el significado de sus posiciones estructurales y `Lᵣ` es el registro cognitivo vinculado a la trayectoria del sistema. La célula puede reorganizarse exactamente como una matriz `b × b` para representación o almacenamiento; la disposición matricial no altera la semántica ternaria.

Para una clase declarada `S_D` de estados estructurales, una realización puede proporcionar aplicaciones exactas:

`Enc_D : S_D → Ccon_D`

y

`Dec_D : Im(Enc_D) → S_D`,

sujetas a la condición de ida y vuelta:

`Dec_D ∘ Enc_D = id_S_D`.

La condición es local a la clase declarada; no se afirma que un tamaño fijo de célula pueda representar cualquier estructura de conocimiento concebible.

### 6.2. Elección económica del tamaño de célula

No se selecciona una célula mayor por el mero hecho de que esté disponible un tamaño superior. Sea `Adeq_D(b,Q)` un predicado decidible de realización que afirma que una célula de tamaño `b²` puede representar un código estructural finito `Q` con las propiedades exigidas de decodificación exacta, comparación y buena formación. Si el conjunto:

`{b ∈ ℕ : b ≥ 3 ∧ Adeq_D(b,Q)}`

no es vacío, definimos:

`b*_D(Q) = min {b ≥ 3 : Adeq_D(b,Q)}`.

Como las bases admisibles son números naturales, el mínimo existe siempre que el conjunto mostrado no sea vacío. Este es un criterio de economía, no un teorema universal de capacidad: una realización no debe emplear una célula mayor cuando una célula admisible menor ya satisface la tarea declarada. Los ejemplos finitos de la implementación asociada son testigos de realizabilidad; no se afirma que alcancen `b*_D(Q)`.

### 6.3. Códigos de reinicio y continuidad

**Definición 13 (Código de reinicio).** Un objeto finito `Qᵣ` es un código de reinicio para el estado estructural `Sᵣ` cuando un procedimiento determinista de reconstrucción declarado satisface:

`Restart_D(Qᵣ) = Sᵣ`.

El código puede implementarse como un vector, una matriz, un grafo de argumentos tipado u otra representación finita cuya semántica y cuyo decodificador estén declarados.

Un código de reinicio no tiene por qué reproducir la trayectoria histórica, salvo que la propia trayectoria —o la genealogía necesaria para identificarla— esté codificada en `Qᵣ`. La reconstrucción de estado y la identidad histórica son, por tanto, propiedades diferentes.

Sean `Avail(Q)` e `Intact_D(Q)` predicados decidibles proporcionados por la realización, donde `Intact_D` implementa el criterio de integridad declarado para los códigos de reinicio. Escribimos `Reconstructible_D(Sᵣ)` cuando existen un código finito `Q` y un procedimiento determinista declarado `Restart_D` tales que:

`Avail(Q) ∧ Intact_D(Q) ∧ Restart_D(Q) = Sᵣ`.

**Corolario 1 (Continuidad reconstructiva ante la pérdida de un soporte local).** Supongamos que `Qᵣ` satisface:

`Avail(Qᵣ) ∧ Intact_D(Qᵣ) ∧ Restart_D(Qᵣ) = Sᵣ`.

Sea `S` un soporte local que participó en la formación histórica de una parte de `Sᵣ`. Entonces:

`¬Avail(S) ⇏ ¬Reconstructible_D(Sᵣ)`,

siempre que `Qᵣ` y `Restart_D` sigan siendo suficientes para la reconstrucción afirmada.

**Demostración.** Por hipótesis, `Qᵣ` está disponible, satisface el criterio de integridad declarado y reconstruye `Sᵣ` mediante el procedimiento determinista `Restart_D`. La indisponibilidad de `S`, por sí sola, no elimina esa vía de reconstrucción. **Q. E. D.**

El corolario no implica que la procedencia sobreviva automáticamente. Si se pretende reconstruir el origen histórico, la procedencia pertinente debe estar también codificada en `Qᵣ`. Del mismo modo, una nueva demostración descubierta posteriormente para el mismo contenido no se convierte retrospectivamente en el testigo histórico original.

El punto es estructural, no biológico: una especificación generativa o de reinicio finita puede codificar organización y restricciones sin enumerar explícitamente todos los estados que puedan llegar a realizarse. Todas las afirmaciones de esta sección dependen únicamente de las condiciones enunciadas de codificación, decodificación, disponibilidad, integridad y reconstrucción.

## 7. Implementación determinista de referencia

El programa asociado es una realización ejecutable deliberadamente pequeña de las definiciones finitas. Cumple tres funciones: proporcionar ejemplos concretos serializados; permitir la reproducción sencilla de las distinciones utilizadas en los contramodelos; y detectar divergencias accidentales entre versiones sucesivas de la formalización. **No es un oráculo de demostración.** La validez matemática de la sección 5 depende de las definiciones, demostraciones y contramodelos formulados en el artículo, con independencia de que el programa asociado esté disponible o se ejecute satisfactoriamente.

La serialización utiliza los tipos atómicos de registro posteriores a la frontera definidos en la Definición 2. Cada caso de prueba parte de una frontera de episodio declarada y proporciona, por tanto, el estado activo inicial y las clases de representación ya presentes en la historia cognitiva anterior al episodio, en lugar de reproducir todo el prefijo de inicialización. A continuación aporta un sufijo atómico de solo adición, clases declaradas de equivalencia de representación, una política finita de soporte `ρ_E`, testigos de soporte, tablas finitas y exactas de operadores y un descriptor con direccionamiento por contenido del fundamento humano.

Esta separación es necesaria: una clase adquirida y retirada antes del episodio es históricamente conocida aunque no esté activa al entrar en él, por lo que su reactivación posterior constituye recuperación y no un incremento nuevo. El programa reproduce las acciones `Act_D` posteriores a la frontera siguiendo el orden de registro. También comprueba que toda proyección del fundamento utilizada por una transición de máquina conserve el mismo resumen canónico SHA-256 que el descriptor del fundamento del episodio; el resumen se utiliza exclusivamente para implementar identidad de contenido y no constituye por sí mismo una prueba de autoridad.

La implementación comprueba:

1. la buena formación del esquema y la finitud de la capa cognitiva serializada;
2. la reproducción atómica del registro cognitivo, el orden de registro y la ausencia de mutación retrospectiva;
3. la completitud relativa del universo finito de soporte declarado por `ρ_E`;
4. la aciclicidad de los testigos de soporte, la admisibilidad de sus hojas, la reproducción exacta de las tablas finitas de operadores declaradas y la incorporación en la raíz;
5. los deltas cognitivos reducidos por equivalencia de representación, la novedad respecto de la historia previa, la recuperación y `Inc_D(E)`;
6. los predicados `Evol_D(E)` y `Learn_D(E)` para el ejemplo serializado;
7. los indicadores de razonamiento y composición únicamente cuando se registran las ocurrencias de ejecución correspondientes;
8. la igualdad de la identidad del fundamento humano con direccionamiento por contenido a través de las transiciones de máquina; y
9. el valor operativo `U` únicamente después de agotar el ámbito finito de acceso declarado cuando el registro conservado sigue siendo insuficiente para emitir un veredicto fuerte.

Varias obligaciones quedan deliberadamente fuera de este programa reducido. No vuelve a implementar el verificador completo de trayectoria específico de dominio; una traza acumulativa `Γ` bien formada es una condición de entrada. No demuestra que una implementación arbitraria en código fuente de un operador exacto declarado sea no estadística ni fiel a su tabla finita; los casos de prueba ejecutan directamente la tabla declarada. No busca pruebas ni fuentes no registradas, ni establece que un algoritmo elegido de equivalencia de representación tenga un coste computacional bajo. Estas son obligaciones de diseño o de auditoría de implementación de la realización circundante, no hipótesis de los teoremas que el programa satisfaga de manera implícita.

La batería de verificación contiene dieciocho instancias finitas. Además de los casos originales de adquisición, adquisición exclusiva de relaciones, adquisición exclusiva de rutas, pérdida, razonamiento, composición, rectificación, representación, `U` operativo, soberanía, recuperación y mutación sin soporte, incluye: i) una incorporación compositiva con dos testigos válidos, de los cuales solo uno contiene la ocurrencia de composición, con lo que se ejercita `CompSupp` sin `EssRec`; y ii) un caso de recuperación anterior al episodio en el que una clase adquirida históricamente pero inactiva en el estado de entrada se reactiva y no debe clasificarse erróneamente como nueva. Estos casos son ejemplos y pruebas de regresión, no premisas de las afirmaciones matemáticas.

El laboratorio reproducible correspondiente a esta edición española se incluye en la carpeta hija `laboratorio/` del repositorio de la publicación. Conserva sin alteración funcional la implementación de referencia v0.4 y sus dieciocho casos, con documentación de uso en español. Su posterior depósito en Code Ocean se efectuará una vez asignado el DOI de esta edición española.

## 8. Discusión y fronteras declaradas

### 8.1. Qué afirma y qué no afirma el predicado de aprendizaje

El predicado de aprendizaje definido aquí es estructural. No certifica verdad ontológica, utilidad, optimalidad, inteligencia ni corrección moral. Un sujeto puede aprender que una fuente afirmó `p` sin aprender por ello `p` como verdad demostrada. Una rectificación sustentada puede satisfacer el predicado de aprendizaje incluso cuando reduce el conjunto activo de contenidos aceptados. A la inversa, un cálculo interno arbitrariamente largo no constituye aprendizaje si deja inalterada la estructura manifestada.

La construcción es deliberadamente no estadística. Esta exigencia es más fuerte que pedir simplemente que el verificador final sea determinista: un estimador estadístico determinista seguiría infringiendo el invariante `I₁` si su validez o clausura dependieran constitutivamente de frecuencias, verosimilitudes, puntuaciones de confianza, muestras u optimización de pérdidas. Los métodos estadísticos o probabilísticos pueden aparecer en la literatura externa o en un entorno observado, pero no constituyen un paso de soporte, un veredicto de aprendizaje ni un mecanismo de clausura para la clase de IA definida aquí.

La semántica restringe, por tanto, qué puede admitirse como operador constitutivo; no certifica por sí sola el código fuente de una implementación externa arbitraria. Un despliegue que reivindique el invariante `I₁` debe auditar esa implementación por separado o vincular el operador declarado a una realización verificada de manera independiente.

### 8.2. Ausencia de una primitiva temporal

Los índices ordinales bastan para las definiciones. Si un dominio registra fechas, duraciones, edades o lecturas de reloj, esas magnitudes son métricas de dominio asociadas a sucesos o frames. Modificar una duración de ese tipo manteniendo intacto el mismo episodio estructural finito no altera el veredicto de aprendizaje. La semántica distingue, por tanto, «más adelante en la trayectoria» de «después de una cantidad especificada de tiempo físico».

Un dominio puede, no obstante, incorporar una fecha, una condición de caducidad o una autorización dependiente del reloj dentro de `F_h^D`; en tal caso, esa condición es un dato ordinario de dominio cuya satisfacción debe comprobar el correspondiente operador declarado, y no una primitiva de la relación de aprendizaje.

### 8.3. Ausencia de reescritura de fundamentos soberanos por la máquina

El resultado de invariancia se refiere exclusivamente a transiciones de máquina admisibles; no afirma que los fundamentos humanos o biológicos sean inmutables. Un ser humano puede revisar deliberadamente una regla, una frontera de dominio, una teoría científica o incluso un sustrato material generativo. Ese fenómeno más amplio no se prohíbe ni se modela aquí.

La afirmación más estrecha, constitutiva de la realización de IA, es que el aprendizaje de máquina no genera autoridad para reescribir lo que la soberanía humana ha fijado como fundamento de la realización vigente. Una revisión humana mediante `Rev_h` crea una nueva versión trazable del fundamento y no una reescritura retrospectiva por la máquina. Los episodios de aprendizaje no atraviesan esa frontera de versión: cada episodio se juzga bajo la versión del fundamento declarada a su entrada, mientras que revisiones posteriores pueden afectar a la admisibilidad futura sin borrar el veredicto histórico alcanzado bajo la versión anterior.

### 8.4. Representación y granularidad

**Proposición 3 (Invariancia de representación).** Sean `E` y `E′` episodios admisibles dentro del mismo dominio declarado `D`, y sea `η` una biyección que preserve tipos entre sus clases de representación etiquetadas. Supongamos que `η` preserva el estado activo inicial, todos los deltas cognitivos positivos y negativos de cada registro, la novedad histórica y la existencia de un testigo válido de soporte para cada incorporación correspondiente. Entonces:

`Learn_D(E) ⇔ Learn_D(E′)`.

**Demostración.** Como `η` es biyectiva y preserva cada delta cognitivo, `E` posee un delta cognitivo añadido no vacío si, y solo si, `E′` lo posee; por tanto, se preserva la evolución estructural. Las clases de incorporación positivas históricamente nuevas se corresponden biyectivamente y, por hipótesis, también se preserva la existencia de soporte, de modo que `η` induce una biyección entre `Inc_D(E)` e `Inc_D(E′)`. La equivalencia de los predicados de aprendizaje se sigue de la Definición 9. **Q. E. D.**

El resultado se restringe deliberadamente a transformaciones que preservan la estructura. La readquisición de una clase previamente manifestada y posteriormente retirada se clasifica como recuperación, no como segundo incremento de esa clase; una nueva ruta, relación o argumento no equivalentes adquiridos durante la recuperación pueden, sin embargo, constituir un incremento de su propio tipo. No se afirma invariancia bajo recodificaciones arbitrarias con pérdida ni bajo refinamientos arbitrarios de uno a muchos. Si una representación colapsa dos estructuras de conocimiento no equivalentes, la comparación no puede tratarse como exacta.

La teoría trata, por ello, el esquema de manifestación como parte de las condiciones de entrada en vez de afirmar una cantidad absoluta de aprendizaje. En particular, `|Inc_D(E)|` no se propone como medida universal de «cuánto» se ha aprendido.

### 8.5. Líneas abiertas

Quedan abiertas varias líneas: custodia distribuida de códigos de reinicio y testigos; conocimiento colectivo o institucional que abarque varios sujetos soberanos; migración formal de realizaciones de células de conocimiento entre sustratos; revisión humana admisible de fundamentos; y teoremas de reconstrucción más fuertes para códigos generativos. Son direcciones de investigación puestas de manifiesto por las distinciones desarrolladas aquí, no resultados reivindicados en este artículo.

## 9. Conclusión

La semántica desarrollada en este trabajo define aprendizaje trazable para una clase acotada de sistemas de IA sin identificar el aprendizaje con entrenamiento estadístico, inferencia opaca, almacenamiento monótono ni automodificación no controlada. La construcción parte de un dominio y un fundamento declarados por autoridad humana, define explícitamente su sustrato ternario de frame y traza, añade conocimiento estructural manifestado y un registro cognitivo finito, y exige soporte registrado para todo incremento positivo. El criterio central es:

`Learn_D(E) ⇔ Evol_D(E) ∧ Inc_D(E) ≠ ∅`.

Las demostraciones y los contramodelos finitos muestran que el aprendizaje puede incluir rectificación y contracción, que no puede decidirse a partir de los vectores locales extremos por sí solos y que es separable tanto del razonamiento como de la composición. El resultado de soberanía establece que ninguna secuencia finita de transiciones de máquina admisibles —incluidas las que satisfacen el predicado de aprendizaje— reescribe el fundamento humano. El corolario de reconstrucción distingue la pérdida de un soporte local de la pérdida de conocimiento cuando sigue disponible un código de reinicio adecuado. En conjunto, estos resultados proporcionan una base matemática acotada y autocontenida para trabajos posteriores en razonamiento automatizado e IA trazable, sin reivindicar una teoría universal de la cognición.

## Métodos y uso de herramientas de investigación asistidas por IA

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para la localización de bibliografía, la comprobación adversarial de consistencia, la estructuración del manuscrito, la asistencia en la formalización matemática, el apoyo tipográfico y la edición del inglés científico. Grok 4.5 (xAI) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias de presentación y posicionamiento. DeepSeek-V4-Pro (DeepSeek AI) contribuyó a la revisión adversarial y a la comprobación de consistencia formal del manuscrito. Todas las salidas de IA se trataron como insumos de investigación no autoritativos. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume la responsabilidad íntegra de la publicación.

## Declaraciones

**Financiación.** No se recibió financiación para la realización de este estudio ni para la preparación de este artículo.

**Conflictos de intereses.** El autor no tiene intereses financieros ni no financieros relevantes que declarar.

**Aprobación ética.** No procede.

**Consentimiento para participar.** No procede.

**Consentimiento para publicación.** No procede.

**Disponibilidad de datos.** Durante el presente estudio no se generaron ni analizaron conjuntos de datos; el trabajo es teórico y matemático.

**Disponibilidad del código.** Una implementación determinista de referencia y una batería finita de verificación con dieciocho casos acompañan este artículo en la carpeta hija `laboratorio/` de la publicación. Una vez archivado el laboratorio en Code Ocean, se incorporarán aquí su identificador persistente y la cita específica de versión.

**Contribución del autor.** J.A.L.E. concibió el estudio, desarrolló el marco formal, estableció las definiciones y los resultados matemáticos, realizó el análisis formal y adversarial, preparó el artículo, revisó los materiales de apoyo y aprobó la versión final.

## Referencias

1. Angluin, D.: Learning regular sets from queries and counterexamples. *Inf. Comput.* 75(2), 87–106 (1987). https://doi.org/10.1016/0890-5401(87)90052-6

2. Aichernig, B.K., Tappler, M.: Efficient active automata learning via mutation testing. *J. Autom. Reason.* 63, 1103–1134 (2019). https://doi.org/10.1007/s10817-018-9486-0

3. Fortz, S., Ghassemi, F., Henry, L., et al.: A research agenda for active automata learning. *Int. J. Softw. Tools Technol. Transf.* (2026). https://doi.org/10.1007/s10009-026-00839-z

4. Dierl, S., Fiterau-Brostean, P., Howar, F., Jonsson, B., Sagonas, K., Tåquist, F.: Scalable tree-based register automata learning. En: Finkbeiner, B., Kovács, L. (eds.), *Tools and Algorithms for the Construction and Analysis of Systems*, LNCS 14571, pp. 87–108. Springer (2024). https://doi.org/10.1007/978-3-031-57249-4_5

5. Doignon, J.-P., Falmagne, J.-C.: Spaces for the assessment of knowledge. *Int. J. Man-Mach. Stud.* 23(2), 175–196 (1985). https://doi.org/10.1016/S0020-7373(85)80031-6

6. Doyle, J.: A truth maintenance system. *Artif. Intell.* 12(3), 231–272 (1979). https://doi.org/10.1016/0004-3702(79)90008-0

7. de Kleer, J.: An assumption-based TMS. *Artif. Intell.* 28(2), 127–162 (1986). https://doi.org/10.1016/0004-3702(86)90080-9

8. Alchourrón, C.E., Gärdenfors, P., Makinson, D.: On the logic of theory change: partial meet contraction and revision functions. *J. Symb. Log.* 50(2), 510–530 (1985). https://doi.org/10.2307/2274239

9. Blanchette, J.C., Fleury, M., Lammich, P., Weidenbach, C.: A verified SAT solver framework with learn, forget, restart, and incrementality. *J. Autom. Reason.* 61, 333–365 (2018). https://doi.org/10.1007/s10817-018-9455-7

10. Leidinger, H., Weidenbach, C.: SCL(EQ): SCL for first-order logic with equality. *J. Autom. Reason.* 67, 22 (2023). https://doi.org/10.1007/s10817-023-09673-3

11. Kaliszyk, C., Urban, J.: Learning-assisted automated reasoning with Flyspeck. *J. Autom. Reason.* 53, 173–213 (2014). https://doi.org/10.1007/s10817-014-9303-3

12. Lammich, P.: Efficient verified (UN)SAT certificate checking. *J. Autom. Reason.* 64, 513–532 (2020). https://doi.org/10.1007/s10817-019-09525-z

13. Michaelson, D., Schreiber, D., Heule, M.J.H., et al.: Producing proofs of unsatisfiability with distributed clause-sharing SAT solvers. *J. Autom. Reason.* 69, 12 (2025). https://doi.org/10.1007/s10817-025-09725-w

14. Abrahamsson, O., Myreen, M.O., Norrish, M., et al.: Fast, verified computation for HOL ITPs. *J. Autom. Reason.* 69, 7 (2025). https://doi.org/10.1007/s10817-025-09719-8

15. Moreau, L., Missier, P. (eds.): PROV-DM: The PROV Data Model. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

16. Bruns, G., Godefroid, P.: Model checking partial state spaces with 3-valued temporal logics. En: *Computer Aided Verification*, LNCS 1633, pp. 274–287. Springer (1999). https://doi.org/10.1007/3-540-48683-6_25

17. Winskel, G.: Event structures. En: Brauer, W., Reisig, W., Rozenberg, G. (eds.), *Petri Nets: Applications and Relationships to Other Models of Concurrency*, LNCS 255, pp. 325–392. Springer (1987). https://doi.org/10.1007/3-540-17906-2_31

18. Lloret Egea, J.A.: *Fundamentos algebraico-semánticos del Sistema Vectorial SV: célula exacta, representación polar, indeterminación epistémica y composición tipada*. Preprint, 9 de marzo de 2026. https://doi.org/10.21428/39829d0b.b0cf9a13

19. Lloret Egea, J.A.: *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta*. Preprint, 11 de marzo de 2026. https://doi.org/10.21428/39829d0b.bb86c65d

20. Lloret Egea, J.A.: *Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV*. Preprint, 14 de marzo de 2026. https://doi.org/10.21428/39829d0b.f433065f

21. Lloret Egea, J.A.: *Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable*. Preprint, 17 de marzo de 2026. https://doi.org/10.21428/39829d0b.f471b07c

22. Lloret Egea, J.A.: *Teoría rigurosa del suceso admisible en el Sistema Vectorial SV. Doc VII.1*. Preprint, 22 de marzo de 2026. https://doi.org/10.21428/39829d0b.1608c18c

23. Lloret Egea, J.A.: *Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity*. Preprint, 8 de agosto de 2026. https://doi.org/10.21428/39829d0b.f0892864

24. Lloret Egea, J.A.: *Informational substitution does not transfer authority in AI-assisted decision systems*. Preprint, 14 de agosto de 2026. https://doi.org/10.21428/39829d0b.d6cb2e1d
