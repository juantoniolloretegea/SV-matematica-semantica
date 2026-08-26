# De los estándares profesionales a las representaciones verificables: un método trazable para la constitución del dominio médico y la suficiencia relativa a la operación

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
Título abreviado: **Constitución trazable del dominio médico**

## Resumen estructurado

**Antecedentes:** Traducir el conocimiento médico a una representación computacional exige algo más que codificar una regla. Un dominio computacional debe disponer de un ámbito profesional explícito, reglas constituidas clínicamente, entradas admisibles, representaciones que conserven las distinciones requeridas por las operaciones a las que están destinadas y una vía de retorno que permita al experto clínico cualificado continuar el razonamiento y conservar la responsabilidad sobre las actuaciones de trascendencia clínica. **Objetivos:** Definir un método trazable para constituir dominios médicos y distinguir entre la cobertura del corpus declarado, la fidelidad entre especificación e implementación y la suficiencia representacional relativa a la operación. **Métodos:** Se utilizaron cuatro fuentes oficiales de formación y acreditación en inmunología y alergología para construir un corpus profesional acotado, mantenido deliberadamente separado de la evidencia clínica empleada para constituir las reglas operativas. El método se concretó en una arquitectura de matriz ternaria finita y etiquetada, y se sometió a prueba mediante el demostrador publicado IMMUNO-1 y la especificación y el motor de trabajo IMMUNO-2. **Resultados:** El corpus profesional resultó sustancialmente más amplio que los artefactos computacionales actuales, lo que demuestra que la cobertura implementada no puede equipararse a la cobertura de la especialidad. El parámetro P02 de IMMUNO-2 mostró una discrepancia reproducible entre su especificación escrita fijada y el motor cuando las entradas estaban parcialmente cumplimentadas. De manera independiente, dos asignaciones P02 completamente observadas produjeron el mismo estado ternario expuesto a partir de ramas distintas de la regla; por ello, el estado escalar es insuficiente para recuperar el fundamento **si** dicha recuperación forma parte del contrato de operación declarado. Un puente tipado IMMUNO-1→IMMUNO-2 proporcionó el control contrario: la pérdida deliberada de información fue suficiente cuando la operación receptora solo necesitaba la clase transmitida. **Conclusiones:** La fidelidad y la suficiencia son comprobaciones independientes dentro de un proceso más amplio de constitución del dominio médico. El método propuesto mantiene el razonamiento clínico, la autoridad y la responsabilidad en el experto humano cualificado, mientras que los componentes computacionales y de IA se emplean exclusivamente como apoyo subordinado.

**Palabras clave:** Informática médica; Sistemas de apoyo a la decisión clínica; Guías de práctica clínica como asunto; Validación de programas informáticos; Representación del conocimiento

## Introducción

La informática clínica depende cada vez más de sistemas capaces de traducir el conocimiento profesional, las observaciones clínicas y las orientaciones de práctica asistencial a representaciones computables. La cuestión crítica surge antes incluso de que se ejecute un algoritmo: ¿qué se ha constituido realmente como dominio médico, qué evidencia respalda sus reglas y qué información debe seguir disponible cuando el resultado regresa al clínico? La arquitectura considerada en este trabajo es la de un experto clínico cualificado asistido por componentes computacionales y, cuando resulten útiles, por agentes de IA. El experto conserva la responsabilidad de interpretar el estado médico, integrar el contexto y decidir si un resultado formal puede utilizarse y de qué manera. La IA puede ampliar las capacidades de recuperación de información, comparación, cálculo y análisis estructurado; no se convierte por ello en decisora clínica por el mero hecho de participar en el cómputo.

Las guías clínicas interpretables por ordenador proporcionan una base consolidada para transformar recomendaciones clínicas en objetos ejecutables o implementables. La bibliografía sobre esta materia aborda la adquisición del conocimiento, su representación formal, verificación, ejecución, integración, mantenimiento y tratamiento de excepciones; GLIF3, además, separó expresamente los niveles conceptual, computable e implementable. [1,2] Métodos multidisciplinares de desarrollo rápido han acortado posteriormente el tránsito desde las orientaciones narrativas hasta las reglas computables, [3] mientras que las *SMART Guidelines* de la OMS y los *Digital Adaptation Kits* organizan las recomendaciones en flujos de trabajo, elementos de datos, lógica de apoyo a la decisión, indicadores y requisitos de implementación. [4] Estos enfoques demuestran que la orientación médica puede formalizarse. No resuelven, sin embargo, una cuestión previa que adquiere especial relevancia cuando un sistema afirma representar una especialidad o un subdominio médico: qué obligaciones profesionales pertenecen al dominio declarado y cómo deben mantenerse separadas de la evidencia clínica utilizada para constituir cada regla operativa.

Una vez constituido un conjunto de reglas, todavía pueden producirse dos fallos técnicos distintos. El primero es la **fidelidad vertical**: una implementación puede no ejecutar la especificación que afirma implementar, incluso aunque varias implementaciones coincidan entre sí. El segundo es la **suficiencia relativa a la operación**: una implementación puede producir fielmente una representación que, aun así, resulte demasiado grosera para una operación posterior porque ya se haya descartado una distinción clínicamente pertinente. Son cuestiones independientes. Una implementación fiel puede materializar una representación insuficiente; una representación suficientemente rica puede estar implementada de forma incorrecta; y ninguna de estas propiedades confiere por sí sola autoridad clínica. La determinación de consultas en bases de datos y otros trabajos formales afines establecen ya el principio elemental de que una representación puede determinar, o no, la consulta solicitada. [9] Trabajos previos del SV aplicaron esta misma idea, relativa a la operación, a niveles de representación situados aguas abajo, una vez constituido el estado etiquetado. [21] El presente estudio desplaza el límite de inspección aguas arriba, hacia la propia constitución y hacia el trayecto que lleva de la observación al estado.

Existe además un requisito relativo a lo que recibe el clínico. El experto no necesita reproducir el código fuente, la ejecución en WebAssembly ni el cálculo interno de un agente de IA. El sistema sí debe devolver el estado médico de una forma que preserve las etiquetas y distinciones necesarias para que el experto pueda seguir razonando. La analítica visual clínica y las interfaces explicables de apoyo a la decisión son muy anteriores a este trabajo y permiten mostrar evidencia, incertidumbre y vías alternativas. [8] Aquí la cuestión es más estrecha y estrictamente representacional: si una representación destinada al experto conserva el estado etiquetado que afirma exponer y, cuando la operación receptora así lo exige, mantiene explícitamente vinculados la procedencia, el fundamento basado en la evidencia y las limitaciones. Se trata de un requisito estructural, no de la afirmación de que una determinada representación gráfica mejore la usabilidad o los resultados clínicos.

El estudio parte, por tanto, de términos convencionales de informática biomédica. Un estado computacional constituido se trata como una fila de una matriz de datos finita y etiquetada: las columnas poseen significados médicos declarados y la fila registra el estado asignado a cada parámetro. La bibliografía originaria del SV denomina **células** a estos objetos finitos estructurados y ofrece una realización ternaria basada en los estados atómicos 0, 1 y U, junto con transducción tipada, historial de sucesos, representación visual y restricciones aplicables a agentes especializados. [14–19,24] Estos componentes constituyen trabajo previo y no se presentan aquí como novedades. Se utiliza la inmunología como dominio constructor porque la existencia de artefactos publicados de 25 parámetros y de implementaciones ejecutables permite examinar, en un mismo entorno trazable, la cobertura profesional, la fidelidad entre especificación y motor, la pérdida de información y el retorno al experto.

La aportación es, en consecuencia, delimitada, pero práctica. Se propone un método que comienza por un corpus profesional declarado antes de realizar las reglas; mantiene separado el ámbito profesional de la evidencia clínica; contrasta verticalmente la implementación con la especificación de reglas fijada; y pregunta si cada representación continúa sustentando la operación que se declara para ella. El método puede detectar pérdidas en la frontera de transducción antes de los niveles de representación posteriores estudiados con anterioridad. [21] Preserva asimismo una frontera nítida de gobernanza clínica: el experto humano sigue siendo quien razona y responde de la actuación, y la autoridad no sustituye la exigencia de que toda clausura esté respaldada por evidencia legítima y por un mecanismo aplicable. El estudio no emplea pacientes ni cohortes, no formula afirmaciones diagnósticas, pronósticas, terapéuticas, de calibración ni de resultados clínicos, y no prescribe modificaciones del lenguaje de programación del SV.

## Objetivos

El objetivo principal fue definir un procedimiento trazable para constituir un dominio médico acotado a partir de fuentes profesionales y clínicas declaradas, hasta obtener representaciones computacionales verificables. Los objetivos específicos fueron: (1) comprobar si toda obligación extraída del corpus profesional declarado recibe una clasificación explícita; (2) distinguir la fidelidad vertical entre especificación e implementación de la conformidad arquitectónica actual de la propia especificación; (3) comprobar la suficiencia representacional relativa a la operación sin fabricar una operación a partir del comportamiento del programa; (4) identificar cuándo una pérdida deliberada de información sigue siendo legítima para la operación receptora; (5) definir un criterio de ausencia de pérdida para una representación visual destinada al experto sin formular afirmaciones empíricas sobre factores humanos; y (6) derivar requisitos abstractos para su posterior contraste con el inventario del lenguaje de programación, sin ordenar nueva sintaxis ni nuevos objetos de representación intermedia.

## Métodos

### Diseño del estudio y alcance epistémico

Este estudio de métodos formales e informática biomédica examina artefactos computacionales deterministas y testigos pertenecientes a dominios de reglas. Los objetos analizados son estándares profesionales, orientaciones clínicas, especificaciones publicadas, asignaciones explícitas de reglas, implementaciones informáticas y contratos de representación. El acto clínico de constituir un dominio **no** se modela como una función determinista que transforme mecánicamente documentos fuente en un único sistema de reglas. Es un proceso experto gobernado en el que las fuentes se seleccionan, interpretan, acotan y adoptan para una finalidad declarada. No se utilizaron como evidencia experimental pacientes reales, historias clínicas, cohortes ni relatos de pacientes sintéticos. Las asignaciones formales aparecen únicamente como elementos de dominios de reglas declarados. La inmunología es el único dominio constructor de este trabajo; la falsación en otras especialidades queda reservada para trabajos posteriores.

### Búsqueda del estado del arte y genealogía del SV

Se realizó una búsqueda intensiva y dirigida de la bibliografía disponible hasta el 26 de agosto de 2026 en bases de datos bibliográficas, plataformas editoriales, repositorios institucionales y de prepublicaciones, así como en fuentes académicas de acceso más amplio en la web. Las familias de búsqueda incluyeron guías clínicas interpretables por ordenador, digitalización de guías, representación del conocimiento médico, supervisión humana, analítica visual clínica, procedencia y registros de auditoría, determinación de consultas, suficiencia de las representaciones, historiales de sucesos y registros exclusivamente acumulativos. La búsqueda estuvo orientada a mecanismos: términos como *ternary*, *frame*, *system*, *traceability* o *human in the loop* se utilizaron como indicios de búsqueda, no como prueba de equivalencia material. La búsqueda se dio por agotada cuando las principales familias conceptuales comenzaron a repetirse sin que apareciera un método materialmente equivalente para la aportación concreta sometida aquí a prueba. Se conservaron los trabajos externos relacionados con independencia de su cronología. Las fechas públicas del SV se consignan únicamente para preservar su genealogía; de la proximidad cronológica no se infiere dependencia ni plagio.

### *Corpus* profesional y constitución gobernada del dominio

Para un dominio médico candidato `D` se mantienen separadas dos clases de fuentes. `K_D^prof` es el corpus profesional declarado, utilizado para identificar las obligaciones propias de la especialidad, las poblaciones y el alcance. `E_D^clin` es el corpus de evidencia clínica utilizado para constituir reglas médicas operativas. La relación es deliberadamente paralela, no secuencial: un programa formativo puede establecer que una obligación pertenece al ejercicio profesional sin proporcionar un umbral clínico, mientras que una guía puede sustentar un umbral sin definir por ello todo el ámbito profesional de la especialidad.

La constitución se expresa de la siguiente forma, en notación textual compatible con GitHub:

`Constituir_H_D(K_D^prof, E_D^clin) → (Alcance_D, Π_D, Reglas_D, O_D, Q_D)`

`H_D` denota la gobernanza clínica humana cualificada. La flecha representa un acto gobernado de constitución, no la afirmación de que los corpus fuente determinen de manera única un sistema de reglas médicas. `O_D` designa los observables admitidos para la finalidad declarada y `Q_D`, las operaciones declaradas que la representación computacional pretende sustentar.

El constructor de inmunología utilizó cuatro sistemas oficiales e independientes de formación o acreditación: el Royal Australasian College of Physicians, el Royal College of Physicians and Surgeons of Canada, el currículo de Alergología del General Medical Council del Reino Unido y los requisitos de Alergología e Inmunología del Accreditation Council for Graduate Medical Education. [10–13] Estas fuentes se eligieron como marcos oficiales de competencias independientes, no como afirmación de representatividad mundial. La aportación británica es, específicamente, el currículo de Alergología del GMC y no debe interpretarse como cobertura completa de todos los ejes de la inmunología de laboratorio. A cada obligación extraída se le asignó una población y una finalidad y, a continuación, una única clasificación explícita: cubierta por el constructor actual; competencia profesional transversal o no resolutiva; fuera de la población declarada; expresamente excluida del ámbito actual; o no cubierta. La prueba concierne, por tanto, al **corpus declarado**, no a la integridad universal de la inmunología.

![Figura 1. Constitución gobernada del dominio médico](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura1.png)

*Figura 1. Constitución gobernada del dominio médico. Las obligaciones profesionales y la evidencia clínica entran como capas de fuentes paralelas. Los componentes computacionales y de IA permanecen dentro de una gobernanza clínica humana cualificada; la representación del estado destinada al experto se mantiene separada de la procedencia, la evidencia y las limitaciones vinculadas, de modo que dicha representación no se redefina como si fuese el objeto canónico completo **Frame**.*

### Gobernanza clínica humana y responsabilidad

La arquitectura está gobernada explícitamente por el ser humano. Un experto clínico cualificado sigue siendo el actor que interpreta la evidencia, define o aprueba las reglas médicas y finalidades aplicables, revisa los resultados formales y autoriza actuaciones clínicas de trascendencia dentro del marco institucional correspondiente. Los agentes de IA pueden recuperar, extraer, comparar, calcular, estructurar o proponer, pero sus salidas son entradas de investigación o de cómputo carentes de autoridad propia. El papel humano no consiste en un clic final de aprobación colocado después del razonamiento de la máquina: el experto debe poder examinar el estado constituido, rechazar una conclusión carente de fundamento, solicitar evidencia adicional o mantener sin resolver una no clausura genuina. La autoridad no sustituye la exigencia de que la clausura se apoye en evidencia legítima y en un mecanismo aplicable.

### Admisión, transducción y estado etiquetado

Las observaciones brutas encuentran primero una frontera de admisión:

`O_D^brutas →[Adm_D] O_D^adm →[τ_D] S_D`, con `S_D ∈ {0,1,U}^n`.

La arquitectura actual distingue el fallo técnico de captura, la inadmisibilidad o la adquisición pendiente de una U ternaria genuinamente constituida. Por consiguiente, U no puede emplearse simplemente para ocultar un paso de admisión fallido o incompleto. Esta distinción es especialmente importante para el testigo histórico de P02 en IMMUNO-2, porque su especificación fijada de 6 de marzo de 2026 situaba determinadas entradas necesarias no disponibles dentro de una cláusula U. El presente estudio separa, por ello, dos preguntas: si el motor es fiel a esa especificación fijada y si el tratamiento que la propia especificación fijada da a las entradas no disponibles es conforme con la arquitectura actual de admisión y no clausura. La primera pregunta puede resolverse mediante un testigo de especificación frente a motor; la segunda no puede decidirse únicamente por la fidelidad.

La arquitectura originaria del SV utiliza un objeto canónico **Frame** más amplio. Para no redefinirlo, este estudio emplea `S` para el estado ternario etiquetado ya constituido y `Vis(S)` únicamente para la representación visual destinada al experto que aquí se analiza. La procedencia, el fundamento basado en la evidencia y las limitaciones pueden vincularse a la interfaz de retorno cuando la operación lo requiera, pero no se presupone que formen parte de los campos de `Vis(S)`.

### Representación visual destinada al experto

Sea `I = {P1, …, Pn}` un conjunto de coordenadas etiquetadas fijas y sea `λ: Pi → θi` la aplicación que asigna a cada etiqueta una posición visual declarada y distinta. Sea `r: {0,1,U} → ℝ` una codificación radial categórica e inyectiva. Se define:

`Vis(S) = ((Pi, θi, r(Si))) para i = 1, …, n`.

Por construcción, `Vis` es inyectiva sobre el estado ternario etiquetado: la correspondencia fija entre etiqueta y posición identifica la coordenada, y la inversa de `r` recupera su valor ternario. Esto establece la recuperabilidad exacta del estado etiquetado a partir de la codificación abstracta. No establece que una imagen rasterizada conserve toda la información bajo cualquier forma de reproducción, ni que los clínicos interpreten la representación con mayor rapidez, mayor exactitud o menor carga cognitiva. Estas son cuestiones empíricas diferentes.

![Figura 2. Marco ternario sintético vinculado a un vector explícito](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura2.png)

*Figura 2. Marco ternario sintético e ilustrativo vinculado a un vector explícito de parámetros. La configuración se incluye exclusivamente para mostrar la representación destinada al experto de un estado ternario etiquetado de 25 parámetros. No representa a un paciente, no contiene datos clínicos, no formula una recomendación clínica ni constituye material evidencial de los resultados analíticos. Los niveles radiales codifican los estados atómicos 0, 1 y U; la distancia radial no es una magnitud clínica. La clase global mostrada obedece a la regla de umbral del marco completo `T(25)=19`, no a una regla aplicada a un parámetro individual.*

### Pruebas internas

El método emplea cuatro comprobaciones internas. **T1, cobertura del corpus declarado**, pregunta si toda obligación extraída de `K_D^prof` recibe una clasificación explícita dentro del alcance, la población y la finalidad declarados. **T2, fidelidad vertical**, pregunta si la implementación ejecuta, en el dominio admitido aplicable, la especificación de reglas fijada que afirma implementar. Esto es distinto de preguntar si dicha especificación sigue siendo conforme con la arquitectura actual. **T3, suficiencia relativa a la operación**, pregunta si una representación `R` conserva las distinciones requeridas por una operación declarada `Q`. Un testigo con `R(x)=R(y)` y `Q(x)≠Q(y)` demuestra insuficiencia para esa operación. **T4, frontera de retorno y autoridad**, es un invariante de diseño, no un resultado de factores humanos: pregunta si el retorno expone la información, las limitaciones y la frontera de control requeridas por la operación experta declarada sin transferir autoridad clínica al componente computacional.

### Constructor de inmunología y testigos P02

IMMUNO-1 es un demostrador técnico previamente publicado, de 25 parámetros y cinco capas, destinado a profilaxis de infecciones y vacunación en adultos con neoplasias hematológicas e inmunosupresión. [14] IMMUNO-2 es una representación de trabajo de 25 parámetros para estratificar el riesgo de infección grave en adultos que reciben inmunosupresión farmacológica sistémica no relacionada con trasplante; la Capa 1 ha sido objeto de una revisión más profunda, mientras que las Capas 2–5 continúan bajo revisión especializada. Ninguno de ambos artefactos se trata aquí como instrumento de riesgo clínicamente validado.

El repositorio público se inspeccionó en el *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd`. [27] P02 es un parámetro compuesto cardiometabólico y renal. Su especificación fijada asigna el estado 1 cuando está presente cualquiera de los criterios declarados de diabetes, insuficiencia cardiaca, afectación renal o acontecimiento isquémico reciente; asigna el estado 0 cuando ninguno está presente o cuando la comorbilidad menor está controlada; y asigna U cuando no están disponibles determinadas evaluaciones o información reciente sobre HbA1c o eGFR. La implementación y la prueba de conformidad situada en `especificaciones/conformidad/test_immuno2.py` se compararon directamente con esa especificación escrita.

La suficiencia se comprobó de forma independiente mediante dos asignaciones formales completamente observadas, ordenadas como `(dm_complicated, HbA1c, NYHA, eGFR, evento isquémico reciente)`:

`x_DM = (True, 7.0, 0, 90, False)`  
`x_CKD = (False, 7.0, 0, 40, False)`

Ambas producen `P02=1`, pero la primera lo hace porque `dm_complicated=True` representa la rama de diabetes complicada; el valor de HbA1c de 7,0 **no** satisface el umbral independiente `HbA1c≥8`. La segunda asignación alcanza el estado 1 a través de la rama renal. Estas asignaciones permiten, por tanto, comprobar la pérdida de información sin apoyarse en entradas ausentes.

![Figura 3. P02 como dos pruebas metodológicas distintas](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura3.png)

*Figura 3. P02 separa dos preguntas metodológicas. El panel A comprueba la fidelidad vertical frente a la especificación fijada; la conformidad arquitectónica actual de esa especificación constituye una cuestión distinta. El panel B comprueba la suficiencia relativa a la operación mediante asignaciones completamente observadas y su resultado sigue condicionado a que la recuperación del fundamento forme parte del contrato de operación declarado.*

### Control positivo: puente tipado y pérdida legítima

P25 de IMMUNO-2 se especifica como un único puente desde la evaluación terminal de IMMUNO-1, sujeto a condiciones de vigencia definidas por el dominio, y no como transporte del estado completo de 25 coordenadas de IMMUNO-1. [27] Proporciona un control positivo para la pérdida legítima de información. Si la operación receptora necesita únicamente el estado del puente tipado representado por P25, no es necesario transmitir el vector más rico de IMMUNO-1. Aquí «vigencia» es una condición declarada por el dominio; no implica que la recencia determinada por el reloj del sistema anfitrión ni una regla de «prevalece el último» sean primitivas del sistema formal.

### Traslado al lenguaje de programación

Un hallazgo médico no crea directamente una característica del lenguaje de programación. La transferencia sigue esta secuencia:

`Hallazgo → Necesidad(Q) → RequisitoAbstracto → ContrasteConInventario → L0 … L4`

El proceso receptor clasifica si una necesidad ya puede expresarse (L0), requiere la composición correcta de construcciones existentes (L1), establece una extensión candidata después de superar la comprobación del inventario (L2), pertenece a una capa de agente, interfaz o dominio y no al núcleo del lenguaje (L3), o exige una realización material posterior (L4). La aplicación de los hallazgos actuales al inventario vigente **no** demostró un requisito L2: las presiones observadas pueden clasificarse, por ahora, como uso o capacidad ya existente, o bien como cuestiones de dominio o interfaz. Este es un resultado actual, no una regla de clausura. Una operación futura legítima que no pueda expresarse correctamente con el inventario existente todavía podría establecer un requisito L2.

### Consideraciones éticas

No se recopilaron ni analizaron participantes humanos, datos de pacientes, datos de cohortes, intervenciones clínicas ni conjuntos de datos derivados de pacientes. Las asignaciones formales son testigos pertenecientes a dominios de reglas y no pacientes sintéticos. El marco visual ilustrativo es una configuración ternaria esquemática utilizada exclusivamente para mostrar la representación y no constituye material evidencial. No se formula recomendación clínica, afirmación diagnóstica, afirmación de efecto terapéutico ni autorización clínica alguna. En consecuencia, la revisión ética de investigación con seres humanos no resultaba aplicable al trabajo aquí presentado.

## Resultados

### La cobertura del corpus declarado no equivale a la cobertura de la especialidad

Las cuatro fuentes profesionales oficiales definen una especialidad sustancialmente más amplia que los dos artefactos actuales del constructor de inmunología. En el corpus declarado, las obligaciones se extienden más allá de la profilaxis de infecciones, la vacunación y el riesgo de infección grave, e incluyen inmunodeficiencias, alergia e hipersensibilidad, enfermedades autoinmunitarias y autoinflamatorias, investigación clínica, prescripción, procedimientos, comunicación, mejora de la calidad y otras actividades profesionales. [10–13] El constructor actual aborda únicamente cuestiones acotadas en poblaciones adultas declaradas. Toda obligación extraída puede recibir una clasificación explícita, pero este hecho no implica que las representaciones implementadas cubran la especialidad. El método distingue, por tanto, entre **cobertura de clasificación de un corpus declarado** y **cobertura computacional del dominio médico**.

### P02 establece una discrepancia de fidelidad vertical

Se identificó una discrepancia no vacía entre la especificación fijada de P02 y la implementación en Python. La regla escrita sitúa la ausencia de la evaluación necesaria o de información sobre HbA1c o eGFR dentro de su cláusula U. [27] El motor, sin embargo, puede devolver 0 en cuanto dispone de al menos un dato metabólico y de eGFR y no se ha activado ninguna rama positiva. La batería de conformidad fijada contiene expresamente `P02({"dm_complicated": False, "egfr": 90}) == "0"`, aun cuando faltan los campos HbA1c, NYHA y acontecimiento isquémico reciente. [27] Por tanto, la implementación y la especificación fijada no coinciden en esa región documentada de entrada.

El resultado es deliberadamente local. Constituye un **certificado de fidelidad vertical**, no una refutación clínica del diseño compuesto de P02 ni una demostración de que la salida correcta actual deba ser U. En la arquitectura vigente, la información ausente o no admitida debe clasificarse primero en la frontera de admisión y no puede convertirse automáticamente en una U ternaria genuina. P02 expone así dos preguntas separables: el motor no es fiel a la especificación histórica fijada en la región testigo, y el tratamiento que la propia especificación fijada da a las entradas no disponibles requiere una revisión independiente frente al invariante actual de admisión y no clausura.

### La suficiencia de P02 depende de la operación

Las asignaciones completamente observadas `x_DM` y `x_CKD` exponen el mismo estado escalar P02, 1, pese a que la rama constitutiva de la regla es diferente. El estado escalar es, por tanto, suficiente para una operación que solo solicite el valor de P02, pero no puede determinar una operación de recuperación del fundamento `Q_basis`:

`Tri_P02(x_DM) = Tri_P02(x_CKD) = 1`  
`Q_basis(x_DM) ≠ Q_basis(x_CKD)`

Por consiguiente, `¬Suff(Tri_P02, Q_basis)` como resultado formal condicional. Esto **no** demuestra que IMMUNO-2 deba admitir `Q_basis`. La pertenencia de la recuperación del fundamento al contrato de operación declarado o clínicamente legítimo permanece abierta y no puede crearse por el mero hecho de que una implementación sea capaz de mostrar un campo explicativo.

### La pérdida deliberada de información puede ser suficiente

El puente P25 demuestra el caso contrario. Un receptor cuya operación declarada necesita únicamente el estado del puente terminal tipado de IMMUNO-1 no precisa la representación fuente completa de 25 coordenadas. Para esa operación, las distinciones descartadas en el nivel de coordenadas son irrelevantes. Este control positivo impide que la suficiencia relativa a la operación degenere en una preferencia universal por representaciones de riqueza máxima: la cuestión pertinente es si sobrevive la información requerida por `Q`, no si sobrevive toda la información de la fuente.

### La recuperabilidad del estado destinado al experto es verdadera por construcción

Dada una correspondencia fija entre etiquetas y posiciones y una codificación categórica inyectiva de 0, 1 y U, la aplicación abstracta `Vis(S)` mantiene una correspondencia biunívoca con el estado ternario etiquetado. El resultado se sigue directamente de la construcción y no se presenta como descubrimiento empírico. La Figura 2 muestra una configuración sintética e ilustrativa de 25 parámetros y el vector explícito a partir del cual se dibuja el polígono. La implementación actual del SV utiliza los niveles radiales 1, 2 y 3 como codificación categórica de 0, 1 y U, respectivamente, [27] mientras que la regla terminal del marco completo utiliza `T(n) = ⌊7n/9⌋`. Para `n=25`, `T(25)=19`. La ilustración sintética contiene `n₀=13`, `n₁=5` y `n_U=7`; por ello, su clase global es indeterminada, ya que ni `n₀` ni `n₁` alcanzan 19. El umbral clasifica el **marco completo**, no un parámetro individual.

### Delimitación frente al estado del arte

La búsqueda bibliográfica identificó abundantes trabajos previos sobre guías computables, adaptación digital de recomendaciones sanitarias, verificación de programas informáticos, supervisión humana, visualización clínica, procedencia y suficiencia de la información dependiente de la operación. [1–9] No se reivindica novedad para ninguno de estos mecanismos de manera aislada. Trabajos anteriores del SV preceden también a este manuscrito en células ternarias, transducción, representación visual, no clausura, autoridad, sustitución de interfaces, composición ejecutable y fronteras de resolución situadas aguas abajo. [14–24]

Dentro de la bibliografía examinada hasta el 26 de agosto de 2026 no se encontró evidencia publicada de un método que comience por un **corpus profesional declarado antes de realizar las reglas** y combine después ese paso de constitución con una **prueba de fidelidad entre especificación fijada y motor** y una **prueba de suficiencia relativa a la operación capaz de localizar pérdidas de información en la frontera de transducción entre observación y estado**. Es un hallazgo acotado de búsqueda, no una prueba de inexistencia de tal método. Esta delimitación define también la separación respecto de la prepublicación anterior *Resolution Frontiers*: aquel trabajo parte de un estado etiquetado `F0` ya constituido y estudia la pérdida de representación aguas abajo; el presente trabajo pregunta qué sucede **antes de `F0` y en el propio `F0`**, incluida la constitución profesional, la admisión, la transducción y la fidelidad vertical. [21]

### Exigencia actual sobre el lenguaje de programación

El contraste con el inventario actual del lenguaje receptor no produjo una necesidad demostrada de introducir una nueva extensión nuclear en este constructor. La distinción admisión/U es ya un invariante arquitectónico; la discrepancia de P02 constituye, por tanto, una presión de conformidad o de uso y no una razón para modificar el alfabeto ternario. La suficiencia relativa a la operación requiere, en primer lugar, tipar explícitamente al receptor y su operación declarada, mientras que el requisito de retorno al experto es ante todo una cuestión de dominio e interfaz. No se establece actualmente ningún requisito L2. Esta afirmación es provisional y relativa a la evidencia disponible: no limita una evolución posterior del lenguaje si una operación legítima demuestra una capacidad que el inventario actual no puede expresar.

## Discusión

La aportación principal es un método para determinar qué debe ser cierto **antes** de considerar que una representación computacional médica constituye una realización adecuada de un dominio declarado. Los métodos consolidados de formalización de guías ya muestran cómo convertir recomendaciones en objetos computables. [1–4] El método presente añade una capa profesional previa: las obligaciones se extraen de un corpus declarado de competencias, reciben clasificaciones explícitas y permanecen separadas de la evidencia clínica que constituye cada regla. Esta separación impide confundir un módulo implementado con la especialidad profesional por el mero hecho de que sus reglas internas sean clínicamente plausibles.

El testigo P02 muestra por qué la fidelidad vertical merece un lugar explícito en el método. La coincidencia entre implementaciones no basta si la implementación compartida se aparta de la especificación que afirma materializar. Al mismo tiempo, la fidelidad no consagra la especificación. La especificación histórica de P02 y la arquitectura actual de admisión y no clausura ilustran con claridad esta diferencia: puede establecerse que el motor diverge de la especificación fijada y, simultáneamente, seguir preguntando si el tratamiento que la propia especificación hace de las entradas no disponibles continúa siendo arquitectónicamente legítimo. Ambas cuestiones no deben fundirse en un único juicio de «correcto» o «incorrecto».

La suficiencia relativa a la operación aborda un fallo distinto. Las dos asignaciones P02 completamente observadas demuestran que el estado ternario escalar elimina la identidad de la rama. Este hecho es matemáticamente inevitable cuando varios predicados clínicamente distintos se comprimen en un único valor escalar. No constituye automáticamente un defecto. Si la operación receptora solo pregunta por el estado P02, el escalar es suficiente. Si una operación legítimamente constituida debe recuperar la rama que sustentó ese estado, el escalar es insuficiente. El puente P25 aporta el contrapeso necesario: las interfaces clínicamente o computacionalmente útiles son con frecuencia deliberadamente reductoras, y la pérdida es aceptable cuando la operación receptora no necesita la información descartada.

Este trabajo precisa asimismo la relación con el estudio anterior del SV *Resolution Frontiers*. [21] Allí, el objeto fuente es un estado ternario etiquetado ya constituido y la pregunta es hasta qué punto puede agregarse aguas abajo sin perder soporte para una operación solicitada. Aquí la frontera puede aparecer antes: en la admisión o en la transducción, antes incluso de que se haya constituido el estado etiquetado `F0`. La diferencia no es terminológica. Una vez eliminada una distinción durante la transducción, ninguna representación posterior puede recuperarla sin información adicional.

La gobernanza humana establece la frontera clínica en torno a estas pruebas técnicas. Los trabajos contemporáneos sobre IA sanitaria subrayan cada vez más la importancia de una supervisión significativa, y no de una mera presencia humana nominal. [5–7] En la arquitectura estudiada, sin embargo, la relación pretendida es más sencilla que la de un sistema autónomo seguido de aprobación humana: se trata de un **experto humano asistido por agentes de IA**. El clínico no necesita seguir cada instrucción de la máquina, pero el sistema debe devolver el estado médico mediante una representación que permita la inspección experta y la continuación del razonamiento. La salida de la IA, la evidencia admitida, el resultado formal y la autoridad clínica son, por tanto, categorías distintas. El experto humano conserva la responsabilidad sobre las actuaciones clínicas de trascendencia, mientras que la IA permanece como instrumento computacional subordinado.

El marco visual resulta útil en esta arquitectura porque aborda el problema del retorno sin fingir que un clínico deba leer el cómputo al nivel de implementación. El resultado aquí establecido es deliberadamente modesto: el estado ternario etiquetado puede recuperarse exactamente de la codificación visual abstracta por construcción. La Figura 2 sintética muestra esta correspondencia de forma transparente al situar el vector explícito junto al polígono representado. **No** demuestra reconocimiento más rápido, menor carga cognitiva, mejores decisiones ni resultados clínicos superiores. Estas cuestiones requieren estudios específicos de factores humanos con clínicos cualificados.

La perspectiva de un historial exclusivamente acumulativo complementa esa vía de retorno. Una U genuinamente constituida puede permanecer abierta cuando la evidencia disponible no justifica la clausura. Si un suceso posterior aporta un fundamento evidencial legítimo y un mecanismo de resolución aplicable, puede añadirse un estado ulterior sin reescribir el anterior como si su no clausura nunca hubiese existido. La nueva evidencia no clausura U automáticamente y la autoridad experta, por sí sola, tampoco fabrica una clausura. La traza registra el fundamento por el que U permaneció abierta y, cuando procede, la clausura gobernada posterior. Se trata de una afirmación de trazabilidad lógica; la persistencia material duradera, la protección frente a reversiones y las garantías forenses son cuestiones independientes de implementación.

Las implicaciones clínicas y de salud pública son, por tanto, indirectas pero concretas. Antes de evaluar los resultados clínicos de un sistema computacional médico, los desarrolladores y las instituciones deberían poder declarar qué dominio profesional se ha constituido realmente, qué reglas y condiciones de admisibilidad sustentan cada parámetro, si el motor ejecutable es verticalmente conforme con su especificación fijada, qué distinciones sobreviven en la representación entregada al receptor, qué operación se afirma que dicha representación sustenta y dónde reside la responsabilidad sobre las actuaciones de trascendencia. Estas comprobaciones no sustituyen la validación clínica, los estudios de usabilidad, la vigilancia de la seguridad ni la revisión regulatoria; identifican requisitos previos que deberían hacerse explícitos antes de interpretar esas evaluaciones posteriores.

Varias limitaciones son deliberadas. La inmunología es el único dominio constructor de este estudio y la falsación entre dominios queda pendiente. El corpus profesional de cuatro fuentes está acotado y no establece una integridad universal de la especialidad; en particular, la fuente del GMC corresponde a un currículo de Alergología y no a un marco exhaustivo de inmunología de laboratorio. IMMUNO-2 continúa siendo un artefacto técnico de trabajo cuyas capas posteriores siguen bajo revisión especializada. El resultado de recuperación del fundamento en P02 está condicionado por el contrato de operación. El resultado visual es representacional, no evidencia empírica de usabilidad. La búsqueda bibliográfica fue intensiva y orientada a mecanismos, pero no constituyó una revisión sistemática PRISMA. Por último, el resultado actual del inventario del lenguaje no encontró ningún requisito L2 demostrado; ello no implica que el lenguaje esté completo ni que deba dejar de evolucionar.

## Conclusiones

Un dominio médico no queda adecuadamente representado por el mero hecho de que pueda codificarse una regla o de que un sistema computacional pueda devolver una respuesta. El dominio debe acotarse primero a partir de obligaciones profesionales declaradas y evidencia clínica; las observaciones deben admitirse antes de su transducción; la implementación debe contrastarse con la especificación que afirma ejecutar; y la representación entregada a un receptor debe preservar las distinciones exigidas por la operación que se declara. El experto clínico cualificado conserva la responsabilidad sobre el razonamiento y sobre las actuaciones de trascendencia, asistido —no sustituido— por agentes de IA. En el constructor de inmunología, P02 demuestra tanto una discrepancia entre especificación fijada y motor como una frontera condicional de pérdida de información, mientras que P25 muestra que una compresión deliberada puede ser plenamente legítima cuando la operación receptora no requiere un estado más rico. El método es, por tanto, un procedimiento trazable de constitución y verificación, no un agente autónomo clínicamente validado. Su siguiente prueba científica es la falsación en un dominio médico materialmente distinto, manteniendo cualquier requisito resultante para el lenguaje sometido a una revisión independiente del inventario.

## Contribuciones del autor

Juan Antonio Lloret Egea: Conceptualización; Metodología; Análisis formal; Desarrollo de programas informáticos; Validación; Investigación; Redacción — borrador original; Redacción — revisión y edición.

## Financiación

Este estudio no recibió financiación externa.

## Conflictos de intereses

El autor declara no tener conflictos de intereses.

## Disponibilidad de datos y código

Los resultados no se sustentan en conjuntos de datos de pacientes ni de cohortes. Las especificaciones e implementaciones de trabajo de inmunología están disponibles públicamente en el repositorio de GitHub `SVperitus-dataset`. La inspección de la implementación de P02 y de la prueba de conformidad está fijada en el *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd`; la prueba pertinente es `especificaciones/conformidad/test_immuno2.py`. Las construcciones del SV citadas están identificadas públicamente mediante DOI.

## Declaración sobre el uso de IA generativa

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para la localización bibliográfica, la comprobación crítica de coherencia, la estructuración del manuscrito, la asistencia en la formalización matemática y en la composición tipográfica, y la edición lingüística en inglés. Grok 4.5 (xAI) se utilizó como herramienta de apoyo a la investigación para la revisión crítica de versiones sucesivas del manuscrito, la identificación de mejoras estructurales y matemáticas y la formulación de sugerencias sobre presentación y posicionamiento. DeepSeek-V4-Pro (DeepSeek AI) contribuyó a la revisión crítica y a la comprobación de la coherencia formal del manuscrito. Todas las salidas de IA se trataron como insumos de investigación carentes de autoridad propia. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, demostraciones, interpretaciones y conclusiones, y asume plena responsabilidad por el manuscrito presentado.

## Referencias

1. Peleg M. Computer-interpretable clinical guidelines: a methodological review. J Biomed Inform. 2013;46(4):744-763. doi:10.1016/j.jbi.2013.06.009.

2. Boxwala AA, Peleg M, Tu S, et al. GLIF3: a representation format for sharable computer-interpretable clinical practice guidelines. J Biomed Inform. 2004;37(3):147-161. doi:10.1016/j.jbi.2004.04.002.

3. Nan S, Tang T, Feng H, et al. A Computer-Interpretable Guideline for COVID-19: Rapid Development and Dissemination. JMIR Med Inform. 2020;8(10):e21628. doi:10.2196/21628.

4. Mehl G, Tunçalp Ö, Ratanaprayul N, et al. WHO SMART guidelines: optimising country-level use of guideline recommendations in the digital age. Lancet Digit Health. 2021;3(4):e213-e216. doi:10.1016/S2589-7500(21)00038-8.

5. Lekadir K, Frangi AF, Porras AR, et al; FUTURE-AI Consortium. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554.

6. Strong J, Rogers H, Sun E, et al. Human-AI Collaboration in Healthcare: A Scoping Review. npj Digit Med. Publicado el 20 de junio de 2026. doi:10.1038/s41746-026-02918-6.

7. van de Sande D, Economou-Zavlanos N, van Genderen ME. Meaningful oversight of medical AI beyond human in the loop. npj Digit Med. 2026;9:569. doi:10.1038/s41746-026-02971-1.

8. Müller J, Stoehr M, Oeser A, et al. A visual approach to explainable computerized clinical decision support. Comput Graph. 2020;91:1-11. doi:10.1016/j.cag.2020.06.004.

9. Nash A, Segoufin L, Vianu V. Views and Queries: Determinacy and Rewriting. ACM Trans Database Syst. 2010;35(3):Article 21. doi:10.1145/1806907.1806913.

10. Royal Australasian College of Physicians. Clinical Immunology and Allergy - Advanced Training; Advanced Training in Immunology and Allergy curriculum standards. Página vigente del programa y estándares curriculares de marzo de 2025; implantación del nuevo currículo a partir de 2027. Consultado el 26 de agosto de 2026.

11. Royal College of Physicians and Surgeons of Canada. Clinical Immunology and Allergy Competencies (2025). Ottawa, Canadá; 2025.

12. General Medical Council. Allergy curriculum. Currículo vigente: Allergy curriculum 2021. Página publicada el 1 de marzo de 2023. Consultado el 26 de agosto de 2026.

13. Accreditation Council for Graduate Medical Education. ACGME Program Requirements for Graduate Medical Education in Allergy and Immunology. En vigor en 2026.

14. Lloret Egea JA. De SVcustos, el marco de intrusión, hasta SVperitus: IMMUNO-1 - Profilaxis infecciosa y vacunación. Célula SV(25,5). IA eñ. Publicado el 5 de marzo de 2026. doi:10.21428/39829d0b.272c2f67. [Prepublicación en español].

15. Lloret Egea JA. Fundamentos algebraico-semánticos del Sistema Vectorial SV. IA eñ. Publicado el 9 de marzo de 2026. doi:10.21428/39829d0b.b0cf9a13. [Prepublicación en español].

16. Lloret Egea JA. Álgebra de composición intercelular del marco SV-IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema. IA eñ. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.5c31d534. [Prepublicación en español].

17. Lloret Egea JA. Formalización de una interfaz visual estructurada en el Sistema Vectorial SV. IA eñ. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.b96fee32. [Prepublicación en español].

18. Lloret Egea JA. Fundamentos, exigencias y arquitectura general de los agentes especializados en el Sistema Vectorial SV: formulación transversal desde el caso director del Agente Especializado en Inmunología. IA eñ. Publicado el 12 de abril de 2026. doi:10.21428/39829d0b.183e10f3. [Prepublicación en español].

19. Lloret Egea JA. Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity. IA eñ. Publicado el 8 de agosto de 2026. doi:10.21428/39829d0b.f0892864. [Prepublicación].

20. Lloret Egea JA. Informational Substitution Does Not Transfer Authority in AI-Assisted Decision Systems. Prepublicación. Publicado el 14 de agosto de 2026. doi:10.21428/39829d0b.d6cb2e1d.

21. Lloret Egea JA. Resolution Frontiers in Stratified Ternary Cells: Infection Prophylaxis, Vaccination, and AI System Integrity. Prepublicación. Publicado el 20 de agosto de 2026. doi:10.21428/39829d0b.739ed2b6.

22. Lloret Egea JA. Sustitución de interfaces heterogéneas en sistemas finitos de resolución: constitución del episodio y preservación exacta de los perfiles de terminales alcanzables. Prepublicación. Publicado el 13 de agosto de 2026. doi:10.21428/39829d0b.e5347310. [En español].

23. Lloret Egea JA. Executable Composition and Post-Composition Event Admissibility in Partial Ternary Systems. Prepublicación. 2026. doi:10.21428/39829d0b.8ea18396.

24. Lloret Egea JA. Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable. Prepublicación. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.f471b07c. [En español].

25. Kamboj M, Bohlke K, Baptiste DM, et al. Vaccination of adults with cancer: ASCO guideline. J Clin Oncol. 2024;42(14):1699-1721. doi:10.1200/JCO.24.00032.

26. Taplitz RA, Kennedy EB, Bow EJ, et al. Antimicrobial prophylaxis for adult patients with cancer-related immunosuppression: ASCO and IDSA clinical practice guideline update. J Clin Oncol. 2018;36(30):3043-3054. doi:10.1200/JCO.18.00374.

27. Lloret Egea JA. SVperitus-dataset [programa informático y especificaciones]. GitHub. Repositorio: juantoniolloretegea/SVperitus-dataset. Inspección de la fuente fijada en el *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd` (24 de agosto de 2026). Consultado el 26 de agosto de 2026.
