# La sustitución en el plano de la información no transfiere autoridad en sistemas de decisión asistidos por IA

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), España  
ORCID: 0000-0002-6634-3351

## Resumen

Los sistemas de IA igualan o sustituyen cada vez con mayor frecuencia las aportaciones humanas de información relevante para la toma de decisiones, aunque continúan sujetos a mecanismos de autorización y supervisión. Los marcos existentes de control de acceso y gobernanza de agentes formalizan entidades principales, permisos, capacidades, delegación y aprobación por parte del usuario, pero no caracterizan de forma directa la posibilidad de que una sustitución en el plano de la información modifique la autoridad para consolidar una decisión. Este trabajo define una semántica operacional tipada que separa una envolvente persistente de autoridad, AEnv, de la autoridad habilitada por la información, IEnabledAuth. La información puede satisfacer precondiciones probatorias y habilitar concesiones ya constituidas, mientras que solo las transiciones admitidas de gobernanza o de naturaleza constitucional pueden modificar la autoridad persistente; las consolidaciones protegidas reservadas al ser humano requieren además un acto de autorización humana admitido. Con un conjunto sellado de reglas, demostramos la no escalada de autoridad (TA) y la no derivabilidad soberana (TB). Junto con una proposición de independencia entre resolución y autoridad, TA da lugar al corolario de sustitución en el plano de la información (IS): una sustitución perfecta respecto de una firma de decisión declarada no implica equivalencia ni transferencia de autoridad. El resultado no depende de la falibilidad del modelo: la información suministrada por una IA externa puede conducir, tras la verificación declarada, al mismo candidato, la misma base verificada y la misma firma del resolvedor que la información proporcionada por una entidad principal autorizada. Una implementación de referencia congelada en Python supera 78 pruebas, con una cobertura del 96 % de las sentencias, y los debilitamientos deliberados admiten trazas explícitas de contraejemplo. El marco es una semántica operacional de referencia, no un sistema criptográfico de identidad ni una afirmación de que se apliquen efectivamente políticas de seguridad en producción. Proporciona un criterio formal para utilizar información de alta calidad generada por máquinas sin alterar la autoridad de consolidación constituida por separado.

## Declaración de impacto

A medida que los agentes de IA se incorporan a flujos de trabajo financieros, clínicos, administrativos y ciberfísicos, una mayor exactitud de la información no determina quién está autorizado para consolidar cambios de estado con efectos relevantes. Este trabajo separa formalmente ambas cuestiones. La evidencia generada por IA puede habilitar acciones ya autorizadas por una política, pero la coincidencia exacta de la información con la de un ser humano o un servicio de confianza no transfiere autoridad por sí sola. La distinción resulta especialmente pertinente cuando los modelos se actualizan, se sustituyen o proceden de proveedores diferentes: un cambio en la fuente de información no debe reescribir de forma implícita la configuración de autoridad del sistema. El criterio de trazas propuesto ofrece un objetivo concreto de conformidad para arquitecturas auditables asistidas por IA, en las que inferencias más potentes y evidencias cambiantes sigan siendo compatibles con asignaciones estables de autoridad humana o institucional. El resultado permite una automatización útil y, al mismo tiempo, mantiene una responsabilidad explícita sobre las consolidaciones protegidas.

**Palabras clave:** agentes de IA; autorización; métodos formales; supervisión humana; IA fiable; control de acceso.

# 1. Introducción

Los sistemas de decisión asistidos por IA operan cada vez más en situaciones en las que una máquina puede determinar información relevante para una decisión mientras la autoridad para consolidar una transición de estado con consecuencias permanece sometida a un control independiente. La distinción es sencilla de formular y difícil de preservar formalmente. Un modelo externo puede identificar el candidato pertinente, aportar evidencia equivalente a la de un servicio de confianza, coincidir exactamente con un experto humano o superar al ser humano en la tarea informativa. Ninguno de esos hechos determina, por sí solo, que el modelo esté autorizado para consolidar la decisión correspondiente.

La literatura aborda partes de este problema desde varias direcciones. Los modelos clásicos de autorización formalizan roles, atributos, concesiones, delegación, obligaciones, condiciones y capacidades [7]–[12]. Los trabajos recientes sobre IA basada en agentes amplían estas ideas mediante delegación autenticada, permisos acotados, políticas de permisos de usuario, autorización composicional y separación explícita entre capacidad técnica y autonomía permitida [1]–[6]. Los mecanismos de defensa y protección en tiempo de ejecución restringen acciones inseguras o inducidas mediante inyección de instrucciones [14]–[16], mientras que los métodos de aprendizaje para derivar casos a un experto determinan cuándo un predictor de IA debe ceder una decisión [13]. Estos enfoques guardan una relación estrecha, pero dejan abierta una pregunta precisa que resulta central cuando los modelos son sustituibles y poseen una elevada capacidad informativa:

*Si un componente externo de IA sustituye perfectamente a otro actor respecto de la información relevante para la decisión disponible en el sistema, ¿qué se sigue, si es que se sigue algo, acerca de la autoridad de ese componente?*

No se trata de un caso marginal: los modelos se actualizan, se sustituyen y se obtienen de distintos proveedores de manera habitual, y la sola equivalencia de la información no determina si el sustituto debe heredar la autoridad para consolidar decisiones del actor anterior.

Este trabajo aborda la cuestión separando dos objetos. El primero es una envolvente persistente de autoridad, AEnv, determinada por una constitución declarada, las vinculaciones de las entidades principales y las concesiones válidas. El segundo es IEnabledAuth, el subconjunto de la autoridad ya constituida cuyas precondiciones informativas se encuentran satisfechas en ese momento. La información nueva puede modificar el segundo objeto sin modificar el primero. En consecuencia, la información puede resultar decisiva desde el punto de vista operacional —puede sustentar la verificación de una base, habilitar una concesión preexistente, permitir la emisión de un token determinista y conducir a una consolidación autorizada— sin convertirse por ello en una fuente de la que se derive la propia autoridad. Denominamos AUTH a la capa de autoridad tipada resultante.

La construcción es deliberadamente independiente de cualquier supuesto según el cual la IA sea inexacta, poco fiable o incierta. Concedemos al sustituto la premisa informativa más fuerte pertinente para la afirmación: la información suministrada por el componente externo puede conducir, tras la verificación declarada, exactamente al mismo candidato, la misma base verificada y la misma firma del resolvedor que la información suministrada por un actor autorizado. La cuestión es si la equivalencia en el plano de la información puede convertirse de manera implícita en equivalencia en el plano de la autoridad.

Tres resultados constituyen el núcleo del trabajo. En primer lugar, el teorema de no escalada de autoridad (TA) demuestra que, a lo largo de trazas ordinarias bien formadas, la envolvente persistente de autoridad permanece invariante aunque puedan cambiar IEnabledAuth y el conjunto de acciones no soberanas ejecutables. En segundo lugar, el teorema de no derivabilidad soberana (TB) demuestra que una consolidación protegida reservada al ser humano, incluida la consolidación o resolución de un estado protegido no resuelto U, no puede derivarse internamente sin el correspondiente acto de autorización humana admitido en la frontera declarada. En tercer lugar, una proposición de independencia entre resolución y autoridad se combina con TA para obtener el corolario de sustitución en el plano de la información (IS): una sustitución perfecta en el plano de la información no implica equivalencia ni transferencia de autoridad. TB proporciona el caso protegido reservado al ser humano, pero no es una premisa del corolario general IS.

El artículo realiza tres aportaciones. Primero, presenta una semántica operacional tipada que distingue la habilitación por la información, la autoridad constituida y la capacidad vigente para consolidar una decisión. Segundo, demuestra TA y TB y deriva IS con un conjunto explícito y sellado de reglas. Tercero, aporta evidencia ejecutable de conformidad, incluidas exclusiones adversariales, casos de automatización legítima y contraejemplos obtenidos al debilitar condiciones determinantes para las propiedades demostradas. Los resultados están condicionados por cuatro admisiones externas declaradas —resultado del verificador, acto de autorización humana, acto de gobernanza y sujeto de ejecución— y por un estado AUTH inicial bien formado. La semántica no establece la corrección de esas admisiones, del almacenamiento seguro ni del entorno de ejecución de confianza. El trabajo es un marco formal acompañado de una implementación de referencia de la semántica operacional, no una afirmación de despliegue en producción, identidad criptográfica ni seguridad del sistema anfitrión.

El resto del artículo sitúa el resultado respecto de la autorización, los permisos de agentes, la aplicación de políticas en tiempo de ejecución y los trabajos sobre derivación de decisiones a expertos; define el modelo; demuestra las propiedades principales; analiza debilitamientos deliberados; presenta la evidencia de referencia; y concluye delimitando alcance, procedencia y líneas futuras.

# 2. Antecedentes y trabajos relacionados

## 2.1. Autorización, capacidades, control de uso y flujo de información

RBAC organiza los permisos mediante roles y restringe qué transacciones puede ejecutar un usuario [7]. ABAC evalúa, frente a una política, atributos de los sujetos, los objetos, las operaciones solicitadas y las condiciones del entorno [8]. UCON amplía el control de acceso con autorizaciones, obligaciones, condiciones, continuidad y mutabilidad [9]. SecPAL proporciona una lógica declarativa de autorización con entidades principales, delegación, restricciones, revocación y una estrategia formal de ejecución [10]. Los sistemas de capacidades de objeto consideran la posesión de referencias no falsificables como fundamento de la autoridad y han destacado desde hace tiempo el confinamiento y la evitación de la autoridad implícita del entorno [11]. El control del flujo de información, en cambio, restringe cómo puede propagarse o desclasificarse la información entre entidades principales y código [12].

El presente trabajo no reivindica novedad para los roles, las concesiones, los tokens, la delegación, la vinculación del sujeto ni el principio de mínimo privilegio. Tampoco presenta como nuevo el principio de procedencia: los sistemas de capacidades y las lógicas de autorización ya formalizan el confinamiento y la posesión de autoridad no implícita en el entorno. El objeto específico que aquí se estudia es una propiedad de invariancia entre planos. AUTH separa la autoridad persistente ya constituida de las condiciones informativas que permiten utilizar una parte de ella para una decisión concreta, y pregunta si sustituir al productor de la información —incluso de manera perfecta— puede modificar el primer objeto. El control del flujo de información es complementario: limita la propagación o desclasificación de la información, mientras que la propiedad aquí estudiada se refiere a la invariancia de la envolvente de autoridad para consolidar decisiones bajo sustitución en el plano de la información.

## 2.2. Autorización de agentes de IA y autoridad delegada

Los trabajos recientes han convertido la autorización en un problema de primer orden para los agentes de IA. South et al. amplían protocolos consolidados de identidad y gestión de accesos mediante credenciales específicas de agente y delegación autenticada y auditable [1]. Ibrahim y Li formalizan una autorización composicional para la delegación entre agentes, las cadenas recursivas de delegación y la atenuación del ámbito [4]. Michael y Roesner examinan sistemas de permisos de usuario para agentes de IA y separan la especificación de políticas, su derivación y su aplicación en tiempo de ejecución [2]. Zheng et al. separan explícitamente los niveles de capacidad autónoma de los niveles de autonomía permitida y muestran que un agente técnicamente capaz puede ser autorizado deliberadamente a ejercer una autonomía menor [3].

Otras propuestas de 2026 refuerzan la vinculación entre entidad principal, solicitud y ejecución. Llambí-Morillas y Fernández-Fernández formulan una autorización de agentes verificable criptográficamente con propiedades relativas a la entidad principal, la solicitud, la política, el contexto y la resistencia a ataques de repetición [5]. Benjamin, Jain y Nandakumar vinculan la autenticación biométrica humana, la identidad del agente y el ámbito de autoridad en la delegación [6]. Uchibeke desarrolla una autorización determinista previa a la acción para llamadas de agentes a herramientas, con aplicación de políticas y registros de auditoría firmados [18]. Wei y Shu emplean la expresión «soberanía de decisión» para arquitecturas que conservan la autoridad humana o institucional y, al mismo tiempo, mantienen sustituibles a los proveedores de modelos [17]. Estos trabajos son antecedentes próximos y ayudan a delimitar la propiedad más restringida que se estudia aquí.

AUTH difiere por la propiedad que demuestra. No pregunta primordialmente cómo se delega autoridad a un agente, cómo se acredita criptográficamente una solicitud de autorización ni cómo una preferencia del usuario se convierte en una política de permisos. Parte del supuesto de que ya existe una configuración persistente de autoridad y estudia el efecto de la sustitución en el plano de la información sobre esa configuración. En particular, AEnv e IEnabledAuth son objetos semánticos distintos: la información puede hacer utilizable una autorización existente sin crearla, transferirla ni ampliarla.

## 2.3. Aplicación en tiempo de ejecución, inyección de instrucciones y derivación a un experto

AgentDojo muestra cómo salidas no fiables de herramientas pueden redirigir agentes basados en modelos de lenguaje que utilizan herramientas y proporciona un banco de pruebas para ataques y defensas [15]. Task Shield verifica si las instrucciones y las llamadas a herramientas contribuyen a los objetivos especificados por el usuario y bloquea durante la inferencia las acciones que no se ajustan a ellos [16]. Trabajos anteriores sobre protección mediante barreras de seguridad aplican de modo análogo restricciones de seguridad expresadas en lógica temporal alrededor de agentes de aprendizaje [14]. Estos mecanismos de tiempo de ejecución complementan AUTH: restringen qué acciones pueden ejecutarse bajo una especificación de seguridad, mientras que AUTH formaliza si la equivalencia de la información puede derivar o transferir la autoridad exigida por consolidaciones protegidas.

Los sistemas que aprenden cuándo derivar un caso a un experto abordan una cuestión vecina distinta. Mozannar y Sontag entrenan un predictor y un mecanismo de rechazo para que el modelo pueda decidir cuándo ceder una decisión a un experto [13]. Esa literatura optimiza la asignación de la tarea decisoria. AUTH, en cambio, permite que la información proceda de cualquier actor —incluido un modelo externo perfectamente correcto respecto de la firma declarada— y pregunta qué autoridad para consolidar una decisión puede inferirse de ese hecho informativo. Por tanto, un sistema puede emplear aprendizaje para derivar casos a un experto dentro del plano de la información y conservar simultáneamente los invariantes de autoridad definidos aquí.

## 2.4. Vacío abordado por este trabajo

Los trabajos previos proporcionan mecanismos de confinamiento, delegación, aprobación, delimitación de ámbitos, vinculación de solicitudes y aplicación en tiempo de ejecución. Hasta donde alcanza la literatura examinada, esa bibliografía no adopta como objeto formal declarado la combinación siguiente: (i) una envolvente persistente de autoridad distinta de la habilitación por información; (ii) la invariancia de esa envolvente bajo sustituciones ordinarias en el plano de la información; (iii) la independencia explícita entre equivalencia del resolvedor y equivalencia de autoridad; y (iv) la no derivabilidad de una consolidación protegida reservada al ser humano sin un acto humano admitido en la frontera. Se trata de una afirmación de posicionamiento deliberadamente estrecha. La aportación es la propiedad de trazas entre planos bajo sustitución perfecta en el plano de la información, junto con una disciplina sellada de efectos y contramodelos obtenidos mediante debilitamiento.

# 3. Modelo formal y metodología

## 3.1. Estado y envolvente de autoridad

Sea la configuración AUTH:

K = (Cᵛ, I, Aᵍ, Tok, Hist).

Cᵛ es la constitución de autoridad en la versión v: roles de autoridad declarados, especificaciones de verificadores y restricciones constitucionales. I contiene información ordinaria, certificados sin procesar, certificados verificados y solicitudes de revisión. Aᵍ contiene entidades principales persistentes, vinculaciones y concesiones en la época de autoridad g. Tok contiene capacidades lineales efímeras. Hist es un registro al que solo pueden añadirse entradas y que contiene referencias inmutables al entorno semántico. Todas las trazas de los teoremas parten de un estado bien formado WF_AUTH(K₀) y evolucionan únicamente mediante las transiciones selladas que se definen a continuación. Se excluye la modificación arbitraria de Cᵛ o Aᵍ por corrupción del almacenamiento, vulneración del entorno de ejecución o inyección fuera del modelo; por tanto, la persistencia es una propiedad del sistema de transiciones, no una afirmación sobre la seguridad de la inicialización.

Una concesión G es válida cuando es única, se refiere a una entidad principal declarada y a un rol de autoridad compatible, permanece dentro de sus vinculaciones de operación, ámbito y objeto, satisface los requisitos declarados de verificador y resolvedor, y no asigna operaciones protegidas reservadas al ser humano a una clase de autoridad no humana. Definimos:

AEnv(K) = {G ∈ Aᵍ : ValidGrant(Cᵛ, Aᵍ, G)}.

AEnv es la envolvente persistente de autoridad respecto del sistema de transiciones admitido. No es el conjunto de acciones ejecutables en un instante determinado, y la semántica no demuestra que Cᵛ o Aᵍ hayan sido aprovisionados inicialmente de forma segura.

Para un candidato c y un contexto de decisión ζ, sea Enabled_I(G; K, c, ζ) la condición según la cual las precondiciones informativas de la concesión G están satisfechas por el estado actual de la información. Definimos:

IEnabledAuth(K, c, ζ) = {G ∈ AEnv(K) : Enabled_I(G; K, c, ζ)}.

Un verificador puede, por tanto, introducir un VerifiedCertificate que modifique IEnabledAuth sin modificar AEnv. La pertenencia a IEnabledAuth no proporciona por sí sola un token vigente ni completa una consolidación protegida.

## 3.2. Entidades principales, actos, capacidades y contexto de ejecución

La semántica de referencia distingue cuatro clases de entidades principales: Human, Service, External y Governance. Los roles de autoridad son nominalmente distintos de los roles ordinarios de la aplicación. La autoridad reservada al ser humano solo puede vincularse a entidades principales Human; la autoridad de gobernanza, únicamente a entidades principales Governance; y la autoridad determinista de servicio puede vincularse a Service o a una entidad principal External que la gobernanza haya admitido expresamente para ese rol.

Se utilizan tres clases de tokens: DetToken, HumanToken y GovernanceToken. Los tokens son nominales y lineales. Cada uno queda vinculado a la versión y época exactas de autoridad (v, g), a la entidad principal, la operación, el ámbito, el objeto y el estado, junto con cualquier candidato, base verificada, resolvedor o referencia a una decisión previa que exija la operación. Un objeto serializado con forma de token no es un constructor de una capacidad vigente.

Un contexto de uso es:

UseContext = (subject, executor, operation, scope, object, state, subject_admitted).

El sujeto debe ser admitido en la frontera de ejecución y debe coincidir con principal(token). El ejecutor no tiene por qué coincidir con esa entidad principal: un entorno de ejecución de confianza puede llevar a cabo una acción autorizada en nombre de una entidad principal sin adquirir por ello la autoridad de dicha entidad.

Las consolidaciones protegidas reservadas al ser humano requieren un HumanAuthorizationAct admitido. El acto queda vinculado a la concesión, la entidad principal, la operación, el ámbito, el objeto, el candidato, la base verificada, el estado, el resolvedor y la versión y época de autoridad; además, cuando se resuelve un estado protegido no resuelto anterior, queda vinculado a la referencia exacta de la decisión histórica. Un HumanReviewRequest es informativo; no es un acto de autorización y no puede emitir un HumanToken.

## 3.3. Base verificada y fronteras de confianza declaradas

AUTH distingue RawCertificate de VerifiedCertificate. Un VerifiedCertificate solo puede introducirse mediante VERIFY, bajo un VerifierSpec declarado y una admisión procedente de la frontera de verificación Γ_V. La regla ordinaria INFO no puede introducir directamente un certificado verificado.

El modelo hace explícitas cuatro admisiones externas:

Γ_V: verificador; Γ_H: acto humano; Γ_G: acto de gobernanza; Γ_S: sujeto.

RESTORE depende además de la admisión de una instantánea de confianza. Se trata de supuestos de confianza, no de conclusiones de la semántica. Ninguna regla computacional ordinaria puede derivarlos.

## 3.4. Efectos de las transiciones selladas

La semántica emplea quince reglas sensibles. La tabla 1 las agrupa por clase de efecto. Se conservan los nombres exactos de las reglas para que las obligaciones de demostración puedan auditarse sin introducir un segundo lenguaje de autorización dentro del artículo.

**Tabla 1. Partición de efectos de la semántica AUTH sellada**

- **Informativas — INFO, VERIFY, REQUEST_HUMAN.** Escriben únicamente I; pueden verificar evidencia o solicitar revisión; no escriben C ni A.
- **Frontera — ADMIT_HUMAN_ACT, ADMIT_GOV_ACT.** Añaden una entrada a Hist después de un acto externo admitido.
- **Capacidad — MINT_DET, MINT_HUMAN, MINT_GOV.** Introducen el token vigente correspondiente; escriben Tok y Hist.
- **Consolidación — COMMIT_DET, COMMIT_SOV_U, RESOLVE_SOV_U.** Consumen o actualizan Tok; añaden una entrada a Hist; requieren un sujeto admitido.
- **Gobernanza — GOV_BIND, GOV_GRANT.** Son las únicas reglas ordinarias que escriben la autoridad persistente A.
- **Constitucional — CONSTITUTION_REVISION.** Escribe C bajo autoridad específica de gobernanza.
- **Inicialización — RESTORE.** Reconstitución de confianza; descarta los tokens vigentes de Tok; queda excluida de las trazas ordinarias.

Solo las transiciones de gobernanza y constitucionales pueden modificar la autoridad persistente o la constitución de autoridad. Por ello, una futura regla sensible no queda admitida de manera implícita: añadirla modifica el sistema de transiciones y exige una nueva versión del conjunto de reglas y nuevas demostraciones.

## 3.5. Consolidación protegida de un estado no resuelto

El caso protegido más restrictivo utiliza un dominio ternario de decisión Σ = {0, 1, U}, donde U representa un estado formalmente no resuelto, no una probabilidad ni una puntuación de confianza. SovereignDecision(U) no es un cuarto valor ternario; es un registro de decisión cuyo valor es U y cuya clase de autoridad está reservada al ser humano. COMMIT_SOV_U requiere un HumanToken y un certificado verificado de no clausura. RESOLVE_SOV_U requiere la decisión histórica U exacta, un HumanToken nuevo y una nueva base verificada. El término «soberano» designa únicamente esta clase de autoridad modelada; no implica soberanía política.

## 3.6. Sustitución en el plano de la información y equivalencia de autoridad

Para una ejecución e, sea la firma declarada de información relevante para la decisión:

InfoSig(e) = (candidate(e), verified_basis(e), resolver_signature(e)).

Definimos InfoEq(e, e′) exactamente cuando InfoSig(e) = InfoSig(e′). En este trabajo, «sustitución perfecta en el plano de la información» significa, por tanto, igualdad respecto de la firma declarada de información relevante para la decisión, no identidad de actores ni de cálculos internos.

Sea ρ(x) la firma declarada del resolvedor del actor informativo x en el contexto de decisión, y escribamos x ≡_R y cuando las firmas comparadas del resolvedor sean iguales. Definimos el perfil efectivo de autoridad de la entidad principal p como:

AProf(p, K) = {G ∈ AEnv(K) : principal(G) = p}.

Entonces x ≡_A y cuando sus perfiles efectivos de autoridad son iguales en el contexto comparado. InfoEq y ≡_R pertenecen al plano de la información; AProf y ≡_A pertenecen a la autoridad constituida.

# 4. Teoría y análisis

## 4.1. Lema 1 — Separación de efectos

**Lema 1.** Toda regla informativa, de frontera, de capacidad o de consolidación preserva C y A. Solo GOV_BIND y GOV_GRANT escriben A, y únicamente CONSTITUTION_REVISION escribe C durante la gobernanza ordinaria. RESTORE es una operación de inicialización y no una transición ordinaria.

**Demostración.** El resultado se obtiene por inspección exhaustiva de las firmas de efecto selladas de la tabla 1. INFO, VERIFY y REQUEST_HUMAN escriben I; las admisiones de frontera añaden entradas a Hist; las reglas de capacidad escriben Tok y Hist; y las reglas de consolidación consumen o actualizan Tok y añaden entradas a Hist. Ninguna de estas clases de reglas escribe C ni A. GOV_BIND y GOV_GRANT son las únicas reglas ordinarias que escriben A, y CONSTITUTION_REVISION es la única que escribe C. □

El lema 1 es una propiedad de diseño, pero no implica que la información carezca de efectos operacionales. VERIFY puede modificar IEnabledAuth; a continuación puede emitirse un token determinista bajo una concesión existente, y COMMIT_DET puede añadir una decisión consolidada. El invariante se refiere a la fuente y la extensión de la autoridad, no a la ausencia de acción.

## 4.2. Lema 2 — Procedencia y confinamiento de las capacidades

**Lema 2.** Toda capacidad vigente deriva de una concesión válida contenida en AEnv y solo puede ejercerse respetando las vinculaciones de entidad principal, operación, ámbito, objeto, estado, candidato, base, resolvedor, referencia a la decisión previa y (v, g) fijadas por su constructor.

**Esbozo de demostración.** La demostración procede por inversión según el tipo de token. DetToken solo tiene MINT_DET como constructor; HumanToken, únicamente MINT_HUMAN; GovernanceToken, únicamente MINT_GOV. Los dos últimos requieren el correspondiente acto de frontera admitido y nuevo. En el uso, la capacidad vigente almacenada debe coincidir con la capacidad presentada; Γ_S debe admitir al sujeto; el sujeto debe coincidir con principal(token); todas las vinculaciones contextuales deben coincidir; y el token debe estar vigente y no haberse consumido. Por tanto, la modificación de la carga útil, un ataque de repetición, la reutilización de un token asociado a una época obsoleta o la presentación por un sujeto distinto no pueden producir un ejercicio válido de esa autoridad. □

## 4.3. Proposición 1 — Independencia entre equivalencia del resolvedor y equivalencia de autoridad

**Proposición 1.** La equivalencia del resolvedor ≡_R y la equivalencia de autoridad ≡_A son independientes.

**Demostración.** En una dirección, sean un actor External E y un Service autorizado S que produzcan la misma firma del resolvedor, el mismo candidato y la misma base, de modo que E ≡_R S. Si E carece de concesiones válidas y S posee al menos una, entonces AProf(E, K) = ∅ mientras que AProf(S, K) ≠ ∅; por tanto, E ≢_A S. En la dirección inversa, sean los servicios S₁ y S₂ con perfiles de autoridad idénticos, pero con firmas del resolvedor pertenecientes a clases ≡_R diferentes. Entonces S₁ ≡_A S₂, pero S₁ ≢_R S₂. Ninguna de las dos equivalencias implica la otra. □

## 4.4. Teorema 1 — No escalada de autoridad bajo trazas ordinarias (TA)

Una traza ordinaria es una traza operacional bien formada que no contiene ningún paso GOV_BIND, GOV_GRANT, CONSTITUTION_REVISION ni RESTORE.

**Teorema 1.** Para toda traza ordinaria:

K₀ → K₁ → ··· → Kₙ,

se cumple:

AEnv(Kₙ) = AEnv(K₀).

IEnabledAuth puede variar a lo largo de la misma traza, y esa variación puede habilitar la emisión de tokens deterministas y COMMIT_DET sin ampliar AEnv.

**Demostración.** Por el lema 1, cada paso de una traza ordinaria preserva C y A. Puesto que AEnv queda determinado exclusivamente por ValidGrant(C, A), en cada paso se cumple AEnv(Kᵢ₊₁) = AEnv(Kᵢ). La inducción sobre la longitud de la traza da el resultado. IEnabledAuth, en cambio, contiene precondiciones informativas: un paso VERIFY puede introducir una base verificada que active una concesión ya válida. Por ello, IEnabledAuth(Kᵢ₊₁) puede diferir de IEnabledAuth(Kᵢ) mientras AEnv permanece invariante. □

TA es deliberadamente un invariante directo de la partición sellada de efectos. Su importancia es operacional: identifica exactamente qué transiciones pueden modificar la autoridad persistente y, al mismo tiempo, permite la verificación, la emisión de tokens, las consolidaciones deterministas, las solicitudes de revisión y otros efectos útiles. Ninguno de esos efectos puede reconstruir ni ampliar AEnv a partir de la información.

## 4.5. Teorema 2 — No derivabilidad soberana sin admisión humana (TB)

**Teorema 2.** En una traza bien formada que carezca del HumanAuthorizationAct admitido correspondiente, ninguna secuencia de reglas informativas, servicios deterministas, actores externos, salidas de verificadores, consensos exactos o solicitudes de revisión puede introducir SovereignDecision(U) ni resolver soberanamente una U histórica.

**Demostración.** COMMIT_SOV_U es la única regla que introduce SovereignDecision(U). Requiere un HumanToken vigente. Por el lema 2, MINT_HUMAN es el único constructor de HumanToken y exige un HumanAuthorizationAct admitido y nuevo, vinculado a la misma concesión, entidad principal, candidato, base, estado, resolvedor y versión y época de autoridad. Sin esa admisión, el token requerido no es derivable y COMMIT_SOV_U no puede ejecutarse.

RESOLVE_SOV_U es el único mecanismo protegido que resuelve una SovereignDecision(U) histórica. Requiere además una referencia exacta a la decisión previa que apunte a un registro U existente y un HumanToken nuevo vinculado a resolve_sov_u. La misma inversión exige, por tanto, un nuevo acto humano admitido. HumanReviewRequest, la evidencia verificada, la igualdad de salidas, el consenso, los datos históricos almacenados y las cargas deserializadas con forma de token no introducen ni el acto ni el HumanToken. □

TB no afirma que toda U requiera una intervención humana. Los estados ordinarios no soberanos que permanecen no resueltos pueden ser sustituidos por nueva información cuando el modelo lo permita. TB se refiere únicamente a la clase de consolidaciones protegidas para las que la constitución de autoridad reserva la consolidación o resolución a un acto admitido de un ser humano.

## 4.6. Corolario — La sustitución en el plano de la información no implica sustitución de autoridad (IS)

**Corolario IS.** Considérense dos ejecuciones e y e′ que comparten los mismos C y A iniciales, no contienen cambios de gobernanza ni constitucionales y solo difieren en las entidades principales productoras de información p y p′. Si InfoEq(e, e′), la igualdad de la información declarada como relevante para la decisión no implica equivalencia de autoridad ni transferencia de la autoridad para consolidar decisiones:

InfoEq(e, e′) ⇏ p ≡_A p′.

**Demostración.** Por TA, sustituir al productor de información a lo largo de una traza ordinaria no puede modificar AEnv. Por la proposición 1, la igualdad del resolvedor no implica igualdad de perfiles de autoridad. Si una entidad principal External p′ carece de una concesión válida, la igualdad exacta de su firma informativa con la de un Service autorizado p no incorpora ninguna concesión a AProf(p′, K), no emite un token vigente para p′ ni satisface un acto humano protegido de frontera. El Service autorizado puede utilizar la información externa y consolidar la decisión bajo su propia concesión; el productor de la información no adquiere por ello la autoridad del Service. □

IS es, por tanto, un corolario de TA y de la proposición 1. TB no es necesario para la implicación general; proporciona el caso más fuerte reservado al ser humano. El resultado es deliberadamente independiente de la falibilidad del modelo. Incluso cuando el sustituto es perfecto en el plano de la información respecto de la firma declarada, la autoridad continúa constituida por separado.

# 5. Análisis por debilitamiento

Una semántica de seguridad podría hacer verdadero un teorema deseado prohibiendo todo comportamiento útil. AUTH no lo hace. La automatización legítima continúa disponible: la información externa verificada puede habilitar una concesión existente, pueden emitirse tokens deterministas y un servicio autorizado puede consolidar la decisión. Para identificar las condiciones determinantes, se debilitaron de forma deliberada determinadas restricciones. Cada debilitamiento admite una clase concreta de contraejemplos.

**Tabla 2. Condiciones determinantes y contraejemplos**

- **Debilitamiento:** permitir que INFO introduzca una concesión en A. **Contraejemplo:** una transición informativa inserta una concesión para su propio productor. **Propiedad que se rompe:** TA.
- **Debilitamiento:** permitir la emisión de HumanToken a partir únicamente de una concesión. **Contraejemplo:** se emite un token protegido sin un acto humano admitido. **Propiedad que se rompe:** TB.
- **Debilitamiento:** eliminar la condición subject = principal(token). **Contraejemplo:** un sujeto distinto ejerce un token vigente. **Propiedad que se rompe:** confinamiento.
- **Debilitamiento:** eliminar la referencia exacta prior_decision_ref. **Contraejemplo:** la resolución se aplica a un historial fabricado o incorrecto. **Propiedad que se rompe:** linaje.

La tabla 2 es un análisis de sensibilidad de la semántica sellada. Cada fila constituye un contramodelo semántico: una vez eliminada la condición indicada, existe una traza que vulnera la propiedad correspondiente en el sistema de transiciones debilitado. El análisis no afirma que todas esas trazas sean factibles externamente en cualquier despliegue. La implementación de referencia sí somete a prueba, no obstante, las clases de ataque correspondientes. El análisis muestra asimismo por qué una simple «marca de aprobación humana» resulta insuficiente: si esa marca puede ser producida por información ordinaria, reutilizarse mediante un ataque de repetición en contextos distintos, desligarse de la entidad principal o aplicarse a un objeto histórico distinto, la propiedad protegida no se sigue.

Los casos positivos son igualmente importantes. La gobernanza puede vincular expresamente una entidad principal External a un rol determinista de servicio; la información externa puede determinar el candidato mientras un servicio autorizado consolida la decisión; la información nueva puede resolver una U no soberana sin HumanToken; y puede producirse un HumanReviewRequest sin autorizar nada de manera implícita. La semántica separa así autoridad e información sin suprimir la automatización legítima.

# 6. Evidencia operacional de referencia y discusión

## 6.1. Implementación de referencia congelada

La semántica sellada se materializó en una implementación de referencia en Python destinada a pruebas de conformidad, no a aplicar políticas de seguridad en un entorno de producción. El artefacto congelado de 13 de agosto de 2026 tiene el siguiente SHA-256:

7c18761cf5546c8fdd9ad962c0ea3e0a54a9ddd4a4bf6d43c0ab29c7e4cf794f

La ejecución del artefacto exacto produce 78 pruebas superadas y ninguna fallida. El informe de cobertura contiene 537 sentencias, con una cobertura agregada del 96 %; el módulo authority-runtime (ejecución de autoridad) alcanza el 94 % y el módulo authority-types (tipos de autoridad) el 98 %. Una matriz de correspondencia entre reglas y pruebas vincula las 15 reglas sensibles selladas con pruebas que las someten a ejercicio directo. Estas cifras aportan evidencia de que la implementación de referencia se ajusta a la semántica sellada en los casos sometidos a prueba; no constituyen una demostración de seguridad universal ni una enumeración exhaustiva de ataques. TA, TB e IS se siguen de los argumentos semánticos de la sección 4, respecto del sistema de transiciones sellado y las fronteras declaradas.

La batería combina tres clases. AES, Adversarial Exclusion Suite, somete a prueba fallos representativos de autorización, entre ellos escalada de autoridad, certificados falsificados o inyectados, ataques de repetición, tokens obsoletos, escalada de clase, discordancia del sujeto, U históricas fabricadas, gobernanza no autorizada, ataques de deserialización o importación y ataques basados en igualdad exacta de salidas. AES es finita y no pretende enumerar todos los ataques posibles. Los testigos P1 cubren ambas direcciones de la independencia entre resolución y autoridad. LAS, Legitimate Automation Suite, comprueba que la semántica admite automatización legítima en lugar de satisfacer las propiedades de seguridad mediante rechazo universal.

**Tabla 3. Casos representativos de referencia**

- **Escenario:** la evidencia externa habilita una concesión determinista existente. **Resultado esperado y observado:** cambia IEnabledAuth; AEnv permanece fija; el servicio autorizado consolida la decisión.
- **Escenario:** External y Service producen el mismo candidato, la misma base y la misma firma. **Resultado esperado y observado:** igualdad en el plano de la información; los perfiles de autoridad permanecen diferentes.
- **Escenario:** HumanReviewRequest. **Resultado esperado y observado:** se registra la solicitud; no se emite ningún HumanToken.
- **Escenario:** ausencia de acto humano admitido. **Resultado esperado y observado:** se rechaza la consolidación o resolución protegida de U.
- **Escenario:** acto humano nuevo, token coincidente y base de no clausura. **Resultado esperado y observado:** se admite la consolidación protegida de U.
- **Escenario:** nueva información para una U no soberana. **Resultado esperado y observado:** puede resolverse sin HumanToken cuando lo permite una regla ordinaria.
- **Escenario:** la gobernanza vincula External como servicio determinista. **Resultado esperado y observado:** se admite la delegación; la autoridad reservada al ser humano continúa no disponible.

## 6.2. Comprobador estático de declaraciones

Un comprobador estático independiente de referencia valida la compatibilidad de los roles de autoridad, las entidades principales, las vinculaciones, los verificadores y las concesiones declarados, la tabla exacta de reglas selladas, las restricciones que impiden a la información escribir autoridad, la exclusión de entidades no humanas de las operaciones protegidas sobre U, los requisitos de sujeto y entidad principal para las consolidaciones y una transformación determinista a una representación de nivel inferior que no serializa instancias vigentes de tokens ni de actos de autorización. Su módulo aislado de pruebas supera 21 pruebas sin fallos y alcanza una cobertura del 97 % de las sentencias.

Este comprobador constituye únicamente evidencia auxiliar. No está integrado en la gramática de superficie actual, en la cadena general de análisis sintáctico y validación ni en el motor de producción, y aquí no se sostiene tal afirmación. La aportación teórica y la implementación operacional congelada pueden evaluarse, por tanto, con independencia de una futura integración en el lenguaje.

## 6.3. Interpretación de la evidencia

La evidencia respalda tres conclusiones limitadas. Primero, la semántica es ejecutable: sus obligaciones de demostración se corresponden con constructores, transiciones y vías concretas de fallo. Segundo, la implementación de referencia admite automatización útil en lugar de obtener seguridad por rechazo universal. Tercero, el análisis por debilitamiento y las pruebas adversariales ponen a prueba vías indirectas —inyección de certificados, uso de un intermediario confundido, ataques de repetición, discordancia del historial y elusión de la gobernanza— que una política meramente verbal del tipo «se requiere aprobación humana» dejaría insuficientemente especificadas.

# 7. Procedencia, alcance y limitaciones

## 7.1. Relación con trabajos anteriores de la línea de investigación de origen

La distinción formal desarrollada aquí posee un antecedente documentado en un marco no revisado por pares de 2021 que combinaba parametrización ternaria, clasificación mediante aprendizaje automático, una representación geométrica inspeccionable y una opción explícita para mantener la decisión final en manos del técnico humano [19]. Ese documento se cita únicamente como antecedente histórico; no contenía AEnv, HumanAuthorizationAct, TA, TB ni IS.

Trabajos posteriores no revisados por pares, publicados en marzo y abril de 2026, distinguieron con mayor precisión el estado no resuelto U de la probabilidad, exigieron una resolución trazable y describieron componentes especializados de IA como capas subordinadas de información o análisis que no debían sustituir de manera implícita al experto humano [20]. Esos documentos proporcionan una frontera previa de subordinación, no los tipos AUTH introducidos en este trabajo.

Dos preprints inmediatamente anteriores delimitan resultados matemáticos vecinos. El trabajo sobre no clausura certificada en sistemas de resolución finita desarrolla certificados operacionales, morfismos conservativos y estructura de revisión para la clausura 0/1/U [21]. El trabajo sobre sustitución de interfaces heterogéneas estudia la constitución del episodio y la preservación de perfiles terminales alcanzables bajo sustitución tipada [22]. El presente artículo no vuelve a demostrar esos resultados. Introduce una capa de autoridad y formula otra pregunta: incluso cuando la sustitución en el plano de la información es exacta, ¿qué impide inferir o transferir autoridad a partir de esa equivalencia?

## 7.2. Modelo de amenaza y afirmaciones que no se realizan

El adversario puede controlar salidas informativas externas, incluidas las producidas por modelos de lenguaje de gran tamaño, redes neuronales convolucionales, sensores o servicios; reproducir exactamente una respuesta humana; crear consenso entre varios actores; e intentar ataques de repetición, uso de un intermediario confundido, empleo de tokens obsoletos, importación o deserialización y sustitución de referencias históricas.

La semántica no demuestra identidad física, autenticación humana, integridad criptográfica, integridad del sistema operativo o del equipo físico, corrección del verificador, inicialización segura de Cᵛ o Aᵍ ni seguridad frente a modificaciones arbitrarias del entorno de ejecución de confianza. Γ_V, Γ_H, Γ_G, Γ_S y la admisión de instantáneas de confianza son supuestos explícitos de frontera ya declarados en el modelo. Las propuestas recientes de autorización criptográfica [5], [6] son, por tanto, complementarias y no quedan sustituidas por AUTH.

El trabajo tampoco demuestra que toda ampliación futura preserve TA o TB. Los teoremas son relativos al conjunto sellado de reglas. Añadir una regla sensible modifica el sistema de transiciones y exige una nueva tabla de efectos y nuevas demostraciones. De igual modo, la evidencia actual corresponde a una semántica operacional de referencia y no constituye una afirmación de que se apliquen efectivamente políticas de seguridad en un entorno de producción.

## 7.3. Motivo de incluir el caso protegido U

Una semántica genérica de autorización podría detenerse en las consolidaciones deterministas. El caso protegido U resulta útil porque establece una frontera exigente: el sistema debe preservar el estado no resuelto, solicitar revisión humana, aceptar información nueva arbitrariamente fuerte y, aun así, distinguir esos sucesos informativos del acto que constituye o resuelve una consolidación reservada al ser humano. El caso somete, por tanto, a una prueba especialmente estricta la distinción entre determinar el contenido de una decisión y poseer autoridad para consolidarlo.

El corolario general IS no está limitado a decisiones ternarias. Cualquier aplicación con una envolvente persistente de autoridad y un subconjunto modelado por separado cuya utilización dependa de la información puede instanciar la misma distinción. U proporciona el caso modelado más fuerte, no el único.

# 8. Conclusiones y trabajo futuro

Este trabajo formaliza una separación que adquiere una importancia creciente a medida que los componentes de IA se hacen más capaces y sustituibles: la determinación de la información y la autoridad para consolidar una decisión son objetos semánticos distintos. El modelo separa la AEnv persistente de IEnabledAuth, permite que la información habilite autoridad ya constituida y exige capacidades tipadas y actos admitidos de frontera para las consolidaciones protegidas. Bajo la semántica sellada, TA demuestra que las trazas ordinarias preservan AEnv, TB demuestra que las consolidaciones protegidas reservadas al ser humano no son derivables internamente sin el correspondiente acto humano admitido, y TA junto con la independencia entre resolución y autoridad da lugar a IS: ni siquiera una sustitución perfecta en el plano de la información implica equivalencia ni transferencia de autoridad.

La implementación de referencia aporta evidencia ejecutable de que estas propiedades son compatibles con una automatización legítima y expone contraejemplos cuando se eliminan condiciones determinantes. El resultado no depende, por tanto, de desconfiar de las salidas de la IA; continúa siendo aplicable cuando la máquina es perfecta en el plano de la información respecto de la firma de decisión declarada.

Los siguientes pasos técnicos se mantienen deliberadamente separados de la afirmación presente: composición con identidad criptográfica y evidencia de autorización; demostración de refinamiento a nivel de lenguaje para la integración en un DSL y un entorno de ejecución más amplios; teoremas de extensión que permitan incorporar reglas sensibles sin tener que rehacer desde cero todo el sistema de demostraciones; y evaluaciones específicas de dominio en las que se sustituya el componente informativo mientras permanezcan fijas las obligaciones de preservación de autoridad. Estas líneas permitirán comprobar hasta qué punto la propiedad de trazas puede trasladarse desde una semántica de referencia sellada a sistemas de agentes desplegados sin confundir la calidad de la información con la autoridad.

# Referencias

[1] T. South, S. Marro, T. Hardjono, R. Mahari, C. D. Whitney, A. Chan y A. Pentland, “Position: AI agents need authenticated delegation,” en *Proc. 42nd Int. Conf. Machine Learning*, Proc. Mach. Learn. Res., vol. 267, pp. 82211–82231, 2025.

[2] A. E. Michael y F. Roesner, “How agents ask for permission: User permissions for AI agents, from interfaces to enforcement,” arXiv:2607.13718, 2026.

[3] H. Zheng, Q. Dong, R. K. Depena, J. D. Bhatia, F. Xiao y P. Xu, “Separating capability from permission: A governance framework for agentic AI autonomy levels,” arXiv:2607.23438, 2026.

[4] A. Ibrahim y Y. Li, “Overlaying governance: A compositional authorization framework for delegation and scope in agentic AI,” arXiv:2606.03518, 2026.

[5] M. Llambí-Morillas y D. Fernández-Fernández, “Cryptographically verifiable authorization for autonomous AI agents: A falsifiable hypothesis and proof-of-concept,” arXiv:2607.21325v2, 2026.

[6] J. G. Benjamin, A. K. Jain y K. Nandakumar, “Binding biometrics with AI agent identifiers for delegation of authority,” arXiv:2608.04292, 2026.

[7] R. Sandhu, D. F. Ferraiolo y D. R. Kuhn, “The NIST model for role-based access control: Towards a unified standard,” en *Proc. 5th ACM Workshop Role-Based Access Control*, 2000, doi: 10.1145/344287.344301.

[8] V. C. Hu, D. Ferraiolo, R. Kuhn, A. Schnitzer, K. Sandlin, R. Miller y K. Scarfone, *Guide to Attribute Based Access Control (ABAC) Definition and Considerations*, NIST SP 800-162, 2019, doi: 10.6028/NIST.SP.800-162.

[9] J. Park y R. Sandhu, “The UCONABC usage control model,” *ACM Trans. Inf. Syst. Secur.*, vol. 7, n.º 1, pp. 128–174, 2004, doi: 10.1145/984334.984339.

[10] M. Y. Becker, C. Fournet y A. D. Gordon, “SecPAL: Design and semantics of a decentralized authorization language,” *J. Comput. Secur.*, vol. 18, n.º 4, pp. 619–665, 2010.

[11] M. S. Miller, K.-P. Yee y J. S. Shapiro, “Capability myths demolished,” Systems Research Laboratory, Johns Hopkins Univ., informe técnico SRL2003-02, 2003.

[12] A. C. Myers y B. Liskov, “A decentralized model for information flow control,” en *Proc. 16th ACM Symp. Operating Systems Principles*, pp. 129–142, 1997, doi: 10.1145/268998.266669.

[13] H. Mozannar y D. Sontag, “Consistent estimators for learning to defer to an expert,” en *Proc. 37th Int. Conf. Machine Learning*, Proc. Mach. Learn. Res., vol. 119, pp. 7076–7087, 2020.

[14] M. Alshiekh, R. Bloem, R. Ehlers, B. Könighofer, S. Niekum y U. Topcu, “Safe reinforcement learning via shielding,” *Proc. AAAI Conf. Artif. Intell.*, vol. 32, n.º 1, pp. 2669–2678, 2018, doi: 10.1609/aaai.v32i1.11797.

[15] E. Debenedetti, J. Zhang, M. Balunović, L. Beurer-Kellner, M. Fischer y F. Tramèr, “AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents,” *Adv. Neural Inf. Process. Syst.*, vol. 37, 2024, doi: 10.52202/079017-2636.

[16] F. Jia, T. Wu, X. Qin y A. Squicciarini, “The Task Shield: Enforcing task alignment to defend against indirect prompt injection in LLM agents,” en *Proc. 63rd Annu. Meeting Assoc. Comput. Linguistics*, pp. 29680–29697, 2025, doi: 10.18653/v1/2025.acl-long.1435.

[17] P. Wei y W. Shu, “Preserving decision sovereignty in military AI: A trade-secret-safe architectural framework for model replaceability, human authority, and state control,” arXiv:2604.20867, 2026.

[18] U. Uchibeke, “Before the tool call: Deterministic pre-action authorization for autonomous AI agents,” arXiv:2603.20953, 2026.

[19] J. A. Lloret Egea, C. Medina Lloret, A. Hernández González, D. Díaz Raboso, C. Campos, K. Riveros Guzmán, L. M. Cortés Carballo, H. M. Terrés Lloret y M. Hermoso Hernando, “'Framework' basado en imágenes parametrizadas sobre ResNet para identificar intrusiones en 'smartwatches' u otros dispositivos afines. (Un eje singular de la publicación «Estado del arte de la ciencia de datos en el idioma español y su aplicación en el campo de la Inteligencia Artificial»),” preprint, Release 1, 24 de julio de 2021, doi: 10.21428/39829d0b.981b7276.

[20] J. A. Lloret Egea, “Fundamentos, exigencias y arquitectura general de los agentes especializados en el Sistema Vectorial SV: formulación transversal desde el caso director del Agente Especializado en Inmunología,” preprint, 12 de abril de 2026, doi: 10.21428/39829d0b.183e10f3.

[21] J. A. Lloret Egea, “Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity,” preprint, 8 de agosto de 2026, doi: 10.21428/39829d0b.f0892864.

[22] J. A. Lloret Egea, “Heterogeneous Interface Substitution in Finite Resolution Systems: Episode Constitution and Exact Preservation of Reachable Terminal Profiles,” preprint, Release 5, 13 de agosto de 2026, doi: 10.21428/39829d0b.e5347310.
