# De los estándares profesionales a las representaciones verificables: un método trazable para la constitución del dominio médico y la suficiencia relativa a la operación

**Prepublicación maestra v0.3.0 — revisión adversarial final — 26 de agosto de 2026**

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
Título abreviado: **Constitución trazable del dominio médico**

## Resumen estructurado

**Antecedentes:** Traducir conocimiento médico a una representación computacional exige algo más que codificar una regla. Un dominio médico computacional acotado requiere ámbito profesional explícito, reglas bajo gobierno clínico, observaciones admisibles, representaciones suficientes para la operación y una vía de retorno que preserve la responsabilidad humana cualificada.

**Objetivos:** Definir un método trazable para constituir dominios médicos y distinguir cobertura del ámbito profesional, fidelidad entre especificación e implementación y suficiencia representacional relativa a la operación.

**Métodos:** Se emplearon cuatro marcos oficiales de formación y acreditación en inmunología y alergología como fuentes profesionales de referencia acotadas, separadas de la evidencia clínica usada para adoptar reglas operativas. El método se materializó en una arquitectura finita de estados ternarios etiquetados y se examinó con el demostrador publicado IMMUNO-1 y la especificación e implementación de trabajo de IMMUNO-2.

**Resultados:** El conjunto profesional de referencia fue más amplio que los artefactos computacionales actuales, por lo que la cobertura implementada no pudo equipararse a la especialidad. P02 mostró una discrepancia reproducible entre su especificación escrita fijada por versión y la implementación ante una entrada parcialmente cumplimentada y documentada. Dos asignaciones completamente observadas produjeron además el mismo estado ternario a partir de ramas distintas; el estado escalar fue insuficiente para recuperar el fundamento si dicha recuperación pertenece al contrato de operación declarado. Un puente experimental IMMUNO-1→IMMUNO-2 proporcionó el control inverso: la pérdida deliberada de información fue suficiente cuando el receptor solo requería la clase transmitida.

**Conclusiones:** Fidelidad y suficiencia son comprobaciones independientes dentro de la constitución del dominio médico. El razonamiento, la autoridad y la responsabilidad clínica permanecen en el experto humano cualificado; los componentes computacionales y de IA actúan como apoyo subordinado.

**Palabras clave:** Informática médica; guías de práctica clínica; validación de programas informáticos; representación del conocimiento; alergología e inmunología

## Introducción

Las guías clínicas interpretables por ordenador han establecido métodos maduros para representar, verificar, ejecutar, integrar y mantener recomendaciones clínicas [1,2]. Los métodos de formalización rápida y las *SMART Guidelines* de la OMS han acortado además el tránsito desde la guía narrativa hasta flujos de trabajo computables, elementos de datos, lógica de apoyo a la decisión y requisitos de implementación [3,4]. Estos antecedentes demuestran que el conocimiento médico puede convertirse en material computable. Por sí solos, sin embargo, no resuelven una cuestión previa de alcance: qué dominio profesional se ha declarado realmente y qué parte de ese dominio representa un artefacto computacional determinado.

Una segunda distinción aparece una vez adoptadas las reglas. La **fidelidad vertical** pregunta si el programa informático ejecuta la especificación fijada por versión que afirma implementar. La **suficiencia relativa a la operación** pregunta si una representación conserva las distinciones exigidas por la operación receptora declarada. Ambas propiedades son independientes. La teoría de determinación de consultas proporciona el principio formal general: una representación puede contener, o no, información suficiente para determinar una consulta [5]. Una implementación fiel puede exponer una representación demasiado pobre para una operación posterior, y una representación rica puede estar mal implementada.

La tercera cuestión es el gobierno clínico. Los trabajos contemporáneos sobre IA sanitaria destacan trazabilidad, integración en el flujo de trabajo, confianza calibrada, supervisión significativa y capacidad efectiva de intervención humana [6-8]. La analítica visual clínica también precede a este trabajo y puede mostrar evidencia, incertidumbre y vías alternativas de razonamiento [9]. El requisito estudiado aquí es más estrecho y estructural: el clínico cualificado debe recibir una representación que conserve las distinciones médicas etiquetadas necesarias para la operación experta declarada, sin verse obligado a inspeccionar detalles de ejecución propios de la implementación. Esto no equivale a afirmar que una visualización concreta mejore la cognición o los resultados clínicos.

El estudio trata, por tanto, un estado computacional constituido como una fila de una matriz finita de datos etiquetados. Cada columna posee un significado médico declarado y cada fila registra el estado asignado a cada parámetro. La literatura originaria del Sistema Vectorial (SV) denomina *células* a estas estructuras finitas y ofrece una realización ternaria con los estados atómicos 0, 1 y U, junto con transducción mediante reglas, trazabilidad por sucesos, representación visual y restricciones para agentes especializados. Esos elementos son trabajos previos; la contribución presente consiste en reunir ámbito profesional, admisión, fidelidad vertical, suficiencia relativa a la operación y retorno al experto dentro de un método auditable de constitución del dominio médico.

No se utilizan pacientes ni cohortes. El estudio no formula afirmaciones diagnósticas, pronósticas, terapéuticas, de calibración ni de resultados y no presenta IMMUNO-1 o IMMUNO-2 como instrumentos de riesgo validados clínicamente.

## Objetivos

El objetivo principal fue definir un procedimiento trazable para constituir un dominio médico acotado a partir de fuentes profesionales de referencia declaradas y evidencia clínica, hasta obtener representaciones computacionales verificables. Los objetivos específicos fueron: (1) separar la cobertura del ámbito profesional de la evidencia que sustenta las reglas clínicas; (2) distinguir la fidelidad entre especificación e implementación de la validez arquitectónica actual de la propia especificación; (3) comprobar la suficiencia relativa a la operación sin inventar una operación a partir del comportamiento del programa; (4) identificar cuándo la pérdida deliberada de información sigue siendo legítima; (5) establecer una propiedad precisa de recuperabilidad para la representación ternaria destinada al humano sin formular una afirmación de factores humanos; y (6) expresar los requisitos de implementación resultantes en términos comprensibles para lectores que no conozcan previamente el SV.

## Métodos

### Diseño del estudio y alcance epistémico

Este es un estudio de métodos formales e informática biomédica sobre artefactos deterministas y testigos pertenecientes al dominio de reglas. Los objetos analizados son estándares profesionales, guías clínicas, especificaciones publicadas, asignaciones formales a predicados de reglas declarados, implementaciones informáticas y contratos de representación. La constitución de un dominio médico **no** se modela como una función mecánica que transforme documentos de manera única en un sistema de reglas. Es un proceso experto gobernado en el que las fuentes se seleccionan, interpretan, acotan y adoptan para una finalidad declarada. Las asignaciones formales de este artículo son elementos de dominios de reglas, no pacientes sintéticos.

Se realizó hasta el 26 de agosto de 2026 una búsqueda bibliográfica intensiva y orientada a mecanismos en bases de datos bibliográficas, plataformas editoriales, repositorios institucionales y de prepublicaciones y otras fuentes académicas accesibles en la Web. Las familias de búsqueda incluyeron guías interpretables por ordenador, digitalización de guías, representación formal del conocimiento, supervisión humana, visualización clínica, procedencia, determinación de consultas, suficiencia representacional e historiales de sucesos. No se trató de una revisión sistemática PRISMA; por ello, cualquier afirmación negativa de novedad queda limitada a la literatura localizada mediante esta búsqueda y a su fecha de corte declarada.

### Fuentes profesionales de referencia y constitución gobernada del dominio

Para un dominio médico candidato D se mantienen separados dos conjuntos de fuentes. `K_D^prof` designa las **fuentes profesionales de referencia declaradas**, empleadas para identificar obligaciones de la especialidad, poblaciones y alcance. `E_D^clin` designa las **fuentes de evidencia clínica** que los expertos cualificados utilizan para adoptar reglas médicas operativas. Un currículo puede demostrar que una obligación pertenece a la práctica profesional sin proporcionar un umbral clínico; una guía puede respaldar un umbral sin definir todo el alcance profesional de la especialidad.

La constitución gobernada se resume así:

`Constituir_H_D(K_D^prof, E_D^clin) ⇝ (Alcance_D, Π_D, Reglas_D, O_D, Q_D)`

`H_D` representa el gobierno clínico humano cualificado. `O_D` contiene los observables admitidos para la finalidad declarada y `Q_D`, las operaciones que se afirma que puede sostener la representación. La flecha expresa un acto gobernado de constitución, no una determinación lógica única producida por los documentos fuente.

El caso de estudio en inmunología empleó cuatro marcos oficiales e independientes de formación o acreditación: el Royal Australasian College of Physicians (RACP), el Royal College of Physicians and Surgeons of Canada, el currículo de Allergy del General Medical Council británico y los requisitos de Allergy and Immunology del Accreditation Council for Graduate Medical Education [10-13]. La fuente del RACP se etiquetó temporalmente porque su nuevo currículo de Immunology and Allergy fue aprobado en marzo de 2025 para implantarse desde 2027, mientras que los residentes anteriores permanecen bajo el programa previo [10]. Estas fuentes se seleccionaron como referencias profesionales independientes y acotadas, no como demostración de representatividad mundial ni de cobertura exhaustiva de la inmunología de laboratorio.

A cada obligación extraída se le asignan una población, una finalidad y una disposición explícita de alcance, por ejemplo: representada por los artefactos actuales; competencia profesional transversal; fuera de la población declarada; excluida expresamente del alcance presente; o no representada. Este procedimiento de control del alcance impide presentar un módulo limitado como si cubriera una especialidad completa.

![Figura 1. Constitución gobernada del dominio médico. Las fuentes profesionales de referencia y las fuentes de evidencia clínica permanecen separadas. La admisión precede a la transducción ternaria y el retorno destinado al experto permanece bajo gobierno clínico humano cualificado.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura1.png)

*Figura 1. Constitución gobernada del dominio médico. Las fuentes profesionales de referencia y las fuentes de evidencia clínica permanecen separadas. La admisión precede a la transducción ternaria y el retorno destinado al experto permanece bajo gobierno clínico humano cualificado.*

### Admisión, transducción y estado ternario

Las observaciones brutas encuentran una frontera de admisión antes de la transducción mediante reglas:

`O_D^brutas →[Adm_D] O_D^adm →[τ_D] S_D`, con `S_D ∈ {0,1,U}^n`.

La arquitectura actual del SV distingue el fallo técnico de captura, la adquisición pendiente y la no admisión de una U ternaria constituida genuinamente. Por ello, U no puede emplearse simplemente para ocultar una admisión fallida o incompleta. Esta distinción es importante para el testigo histórico de P02: la especificación de IMMUNO-2 del 6 de marzo de 2026 situaba cierta información no disponible dentro de su cláusula U. El artículo plantea, en consecuencia, dos preguntas diferentes. Primera: ¿es fiel el programa a esa especificación fijada por versión? Segunda: ¿es conforme la propia especificación histórica con la arquitectura actual de admisión y no clausura? La fidelidad puede responder la primera, pero no la segunda.

Los fundamentos del SV, la transducción ternaria, la construcción de la interfaz visual, las restricciones de los agentes especializados y la semántica auditada basada en sucesos están publicados por separado [14-18]. Trabajos posteriores formalizan además la no clausura certificada y la separación entre sustitución informativa y autoridad [19,20]. El presente artículo utiliza esos elementos como arquitectura previa y no los reintroduce como resultados nuevos.

### Suficiencia relativa a la operación y retorno destinado al humano

Sean `R` una representación y `Q` una operación declarada. `R` es suficiente para `Q` sobre un dominio X cuando dos representaciones iguales no pueden ocultar resultados diferentes de Q. Un contraejemplo tiene, por tanto, la forma:

`R(x) = R(y)` pero `Q(x) ≠ Q(y)`.

Un testigo así demuestra insuficiencia únicamente para esa operación; no demuestra que dicha operación sea clínicamente obligatoria.

Para el retorno visual, supóngase que las etiquetas de parámetros `P1,…,Pn` tienen posiciones visuales fijas y que `r:{0,1,U}→ℝ` es una codificación radial categórica e inyectiva. La representación abstracta

`Vis(S) = ((Pi, θi, r(Si))) para i = 1,…,n`

es inyectiva sobre el estado ternario etiquetado. Las etiquetas y sus valores ternarios pueden recuperarse exactamente de la codificación abstracta por construcción. Este resultado se refiere exclusivamente a la representación. No demuestra ausencia de pérdidas tras cualquier rasterización ni mayor rapidez de reconocimiento, menor carga cognitiva, mejores decisiones o mejores resultados clínicos.

![Figura 2. Estado ternario sintético de 25 parámetros y su representación radial destinada al humano. La posición radial es categórica; no representa una magnitud clínica.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura2.png)

*Figura 2. Estado ternario sintético de 25 parámetros y su representación radial destinada al humano. La posición radial es categórica; no representa una magnitud clínica.*

### Artefactos de inmunología y pruebas sobre P02

IMMUNO-1 es un demostrador técnico previamente publicado, de 25 parámetros, sobre profilaxis infecciosa y vacunación en adultos con neoplasias hematológicas e inmunosupresión [21]. Guías independientes de oncología y enfermedades infecciosas abordan la vacunación y la profilaxis antimicrobiana en adultos con inmunosupresión relacionada con el cáncer [22,23]. IMMUNO-2 es una representación de trabajo, también de 25 parámetros, para estratificar el riesgo de infección grave en adultos con inmunosupresión farmacológica sistémica no relacionada con trasplante; su primera capa ha recibido una revisión más profunda, mientras que las capas posteriores continúan bajo revisión especializada. Ninguno de los dos artefactos se considera aquí un instrumento predictivo validado clínicamente.

El repositorio público se inspeccionó en el *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd` [24]. P02 es un parámetro compuesto cardiometabólico y renal. Su especificación escrita fijada por versión asigna 1 cuando se cumple cualquiera de los criterios positivos declarados de diabetes, insuficiencia cardiaca, función renal o acontecimiento isquémico reciente; asigna 0 cuando no concurre ninguna condición positiva bajo las condiciones establecidas de comorbilidad controlada; y su cláusula U incluye expresamente la ausencia de información reciente de HbA1c o eGFR. Se compararon directamente con dicha especificación la implementación informática correspondiente y su prueba de conformidad.

La suficiencia se comprobó de forma independiente mediante dos asignaciones formales completamente observadas, ordenadas como `(dm_complicated, HbA1c, NYHA, eGFR, recent ischemic event)`:

`x_DM = (True, 7.0, 0, 90, False)`

`x_CKD = (False, 7.0, 0, 40, False)`

Ambas producen P02=1, pero por ramas diferentes. En `x_DM`, `dm_complicated=True` activa la rama de diabetes complicada; HbA1c=7,0 no alcanza por sí misma el umbral independiente HbA1c≥8. En `x_CKD`, eGFR=40 activa la rama renal. Por tanto, la prueba de pérdida de información no depende de datos ausentes.

![Figura 3. P02 separa la fidelidad vertical de la suficiencia relativa a la operación. El panel A utiliza un testigo documentado entre especificación e implementación; el panel B emplea asignaciones completamente observadas y permanece condicionado a que la recuperación del fundamento pertenezca al contrato de operación declarado.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura3.png)

*Figura 3. P02 separa la fidelidad vertical de la suficiencia relativa a la operación. El panel A utiliza un testigo documentado entre especificación e implementación; el panel B emplea asignaciones completamente observadas y permanece condicionado a que la recuperación del fundamento pertenezca al contrato de operación declarado.*

### Control positivo: pérdida deliberada de información

El compositor existente IMMUNO-1→IMMUNO-2 transporta únicamente la clase terminal de IMMUNO-1 hasta P25 de IMMUNO-2 [24]. El propio artefacto fuente lo describe expresamente como conector experimental y no como validación clínica de una dependencia entre profilaxis y riesgo de infección. Por ello, aquí se utiliza únicamente como control metodológico positivo. Si la operación receptora requiere exactamente esa clase terminal tipada, no es necesario transmitir el estado fuente completo de 25 coordenadas. La pérdida de información no es defectuosa por el mero hecho de ser pérdida; la pregunta pertinente es si elimina una distinción requerida por la operación receptora declarada.

### Lenguaje público SV e implicaciones de implementación

El SV dispone también de un lenguaje declarativo público de programación. Un ejemplo mínimo publicado declara un codominio y la especificación de una célula, asigna un vector ternario como `[Zero, One, U, …]` y evalúa el estado declarado mediante `evaluate(S1)` [25]. El entorno web destinado a la inspección por terceros se encuentra en `https://lenguaje-sv.itvia.online/`. El presente artículo no propone sintaxis ni primitivas nuevas. Sus implicaciones de implementación se reducen a tres requisitos públicos: la admisión debe preceder a la transducción ternaria; el programa debe ser conforme con la especificación de reglas fijada por versión que afirma implementar; y una interfaz debe conservar todas las distinciones exigidas por la operación que afirma sostener.

### Consideraciones éticas

No se recopilaron ni analizaron participantes humanos, historias clínicas, datos de cohortes, intervenciones clínicas ni conjuntos de datos derivados de pacientes. Las asignaciones formales son testigos de dominios de reglas. El estado ilustrativo de la Figura 2 no representa a un paciente ni constituye evidencia para una recomendación clínica. Por ello, la revisión ética propia de investigación con sujetos humanos no resultó aplicable al trabajo comunicado.

## Resultados

### La cobertura del conjunto profesional de referencia declarado no equivale a la cobertura de la especialidad

Considerados en conjunto, los cuatro marcos profesionales declarados describen un ámbito que desborda ampliamente los dos artefactos actuales de inmunología. El marco del RACP, por ejemplo, incluye fundamentos de inmunología, inmunodeficiencia, enfermedades autoinmunes y autoinflamatorias, alergia e hipersensibilidad, trasplante, vacunación, razonamiento clínico, comunicación, prescripción, procedimientos, mejora de la calidad y otras actividades profesionales [10]. Los sistemas canadiense y estadounidense muestran una amplitud comparable, mientras que la aportación del GMC es específicamente un currículo de Allergy [11-13]. IMMUNO-1 e IMMUNO-2, en cambio, abordan cuestiones acotadas de profilaxis infecciosa, vacunación y riesgo de infección grave en poblaciones adultas declaradas. Por ello, la cobertura implementada no puede equipararse al ámbito profesional descrito por el conjunto de referencia.

### P02 establece una discrepancia entre especificación e implementación

La especificación de P02 fijada por versión y la implementación informática discrepan ante una entrada parcialmente cumplimentada y documentada [24]. La batería de conformidad contiene:

`P02({"dm_complicated": False, "egfr": 90}) == "0"`

aunque falta HbA1c. La especificación escrita incluye expresamente la ausencia de información reciente de HbA1c dentro de su cláusula U. La implementación puede, por tanto, devolver 0 ante al menos una entrada documentada para la que la especificación escrita fijada por versión dirige el caso a su rama de información no disponible. Esto constituye un certificado de fidelidad vertical relativo a esa especificación histórica.

El resultado **no** demuestra que U sea la salida arquitectónica correcta hoy. Conforme a la arquitectura actual de admisión y no clausura, la información no disponible o no admitida debe tratarse primero en la frontera de admisión y no puede convertirse automáticamente en una U ternaria genuina [18,19,25]. En consecuencia, el tratamiento de los datos ausentes por la propia especificación histórica requiere una revisión arquitectónica separada. El hallazgo de fidelidad y la cuestión arquitectónica actual son distintos.

### La suficiencia de P02 depende de la operación receptora

Para las asignaciones completamente observadas, `Tri_P02(x_DM) = Tri_P02(x_CKD) = 1`, pero las ramas constituyentes son distintas. En consecuencia, el estado escalar P02 no puede determinar una operación `Q_basis` que pregunte qué rama constituyó el valor. Formalmente:

`Tri_P02(x_DM) = Tri_P02(x_CKD)` y `Q_basis(x_DM) ≠ Q_basis(x_CKD)`.

El estado escalar es, por ello, insuficiente para `Q_basis`. Se trata de un resultado **condicional**: no demuestra que IMMUNO-2 deba sostener clínicamente o por contrato la recuperación del fundamento. Si la operación legítima receptora pregunta únicamente por el estado escalar P02, ese estado es suficiente para la operación más estrecha.

### La pérdida deliberada puede ser suficiente

El puente P25 proporciona el control inverso. Descarta intencionadamente las distinciones entre coordenadas de IMMUNO-1 y transmite solo su clase terminal. Para un receptor cuya operación declarada requiera únicamente esa clase, las distinciones descartadas son irrelevantes. Esto evita convertir la suficiencia relativa a la operación en una exigencia universal de transmitir representaciones con la máxima riqueza posible.

### La recuperabilidad del estado destinado al humano es cierta por construcción

Con etiquetas de parámetros fijas y una codificación categórica e inyectiva de 0, 1 y U, la representación abstracta `Vis(S)` mantiene correspondencia biunívoca con el estado ternario etiquetado. La Figura 2 muestra un estado sintético de 25 parámetros con `n0=13`, `n1=5` y `nU=7`. Según la regla de umbral declarada para el estado completo, `T(25)=19`; ni n0 ni n1 alcanzan 19, por lo que el estado sintético global es indeterminado. El umbral clasifica el estado completo, no un parámetro individual. De ello no se deriva ningún resultado empírico de usabilidad.

### Frontera respecto del estado del arte y de la implementación

La búsqueda identificó abundante trabajo previo sobre guías computables, adaptación digital, determinación de consultas, supervisión humana y visualización clínica [1-9]. No se reivindica novedad para esos mecanismos aislados. Los trabajos anteriores del SV también preceden a este artículo en células ternarias, transducción, retorno visual, semántica de sucesos, no clausura, autoridad y fronteras de resolución aguas abajo [14-20,26]. En la literatura localizada hasta el 26 de agosto de 2026 no se identificó un método materialmente equivalente que combinara en un mismo procedimiento una **capa profesional de referencia declarada previa a la realización de reglas**, una **prueba de fidelidad entre especificación fijada por versión e implementación** y una **prueba de suficiencia relativa a la operación capaz de revelar pérdida de información en la constitución del estado ternario o antes de ella**. Es un resultado acotado de búsqueda, no una demostración de inexistencia universal.

Del caso estudiado no se deriva ninguna primitiva nueva del lenguaje de programación. Los tres requisitos de implementación indicados anteriormente ya pueden expresarse como restricciones de admisión, conformidad y contratos de operación tipados en el entorno público del lenguaje SV [25]. Una operación médica futura que no pudiera expresarse fielmente exigiría una argumentación distinta en el nivel del lenguaje; este artículo no formula esa afirmación.

## Discusión

La contribución principal es un método para preguntar qué debe quedar establecido antes de considerar que una representación computacional realiza adecuadamente un ámbito médico declarado. Los métodos existentes de guías interpretables por ordenador muestran cómo formalizar y desplegar recomendaciones [1-4]. El paso adicional consiste aquí en hacer explícito el ámbito profesional de referencia antes de equiparar un módulo implementado con una especialidad. Los estándares profesionales y la evidencia clínica cumplen funciones diferentes: los primeros pueden delimitar obligaciones y poblaciones sin proporcionar umbrales operativos; la segunda puede sustentar reglas operativas sin definir toda la especialidad.

P02 muestra por qué la fidelidad vertical merece una comprobación separada. El acuerdo entre varias implementaciones seguiría siendo insuficiente si todas se apartaran de la especificación que afirman realizar. A la inversa, la fidelidad no convierte una especificación en incuestionable. La regla histórica P02 y la arquitectura actual de admisión y no clausura ilustran con claridad la diferencia: puede certificarse una discrepancia entre especificación y código mientras la propia especificación permanece abierta a una corrección arquitectónica.

La suficiencia relativa a la operación aborda otro tipo de pérdida. Comprimir varios predicados clínicamente distintos en un único valor escalar elimina necesariamente la identidad de la rama que lo produjo. Eso no constituye automáticamente un defecto. La pregunta correcta es si una operación receptora legítima necesita la distinción descartada. Los testigos P02 completamente observados certifican la pérdida de identidad de rama sin apoyarse en datos ausentes; el puente P25 demuestra, a la inversa, que una interfaz intencionadamente reductora puede ser plenamente adecuada para una operación receptora más estrecha. Esto concuerda con los trabajos previos del SV sobre fronteras de resolución específicas de la operación, que parten de un estado ternario etiquetado ya constituido y estudian la pérdida de información en representaciones posteriores [26]. El método actual adelanta la frontera de inspección hacia la constitución profesional, la admisión y la transducción.

El gobierno humano establece la frontera clínica alrededor de estas comprobaciones formales. La supervisión significativa requiere algo más que la mera presencia nominal de una persona [6-8]. En la arquitectura estudiada, la IA no es quien decide para que un clínico se limite después a aprobar su conclusión. Los componentes computacionales y de IA pueden recuperar, estructurar, comparar, calcular o proponer, mientras que el experto cualificado conserva la responsabilidad sobre la constitución del dominio, la interpretación, la revisión y la acción clínica con consecuencias. El resultado visual es deliberadamente modesto: el estado ternario etiquetado puede recuperarse de la codificación abstracta. Determinar si dicha representación mejora la actuación clínica exige estudios posteriores de factores humanos.

El método también favorece la honestidad temporal. Una U genuinamente constituida puede permanecer abierta cuando la evidencia disponible y el mecanismo aplicable no justifican la clausura. Si una evidencia posterior permite una resolución gobernada, puede registrarse un suceso posterior sin reescribir el estado anterior como si la no clausura nunca hubiera existido [18,19]. Se trata de una propiedad lógica de trazabilidad; la persistencia material con garantías forenses constituye otra cuestión de implementación.

Las limitaciones son deliberadas. Inmunología es el único caso médico estudiado, por lo que la falsación entre especialidades queda para trabajos posteriores. Los cuatro marcos profesionales son referencias acotadas y no demuestran completitud universal de la especialidad. IMMUNO-2 sigue siendo un artefacto técnico de trabajo con capas posteriores sometidas a revisión especializada. El resultado sobre recuperación del fundamento de P02 depende del contrato de operación. El resultado visual es representacional y no una prueba de usabilidad. La búsqueda bibliográfica fue intensiva y orientada a mecanismos, pero no sistemática. Finalmente, la conclusión sobre el lenguaje público se limita a los requisitos demostrados en este caso y no implica que el lenguaje sea completo.

## Conclusiones

Una representación médica computacional no es adecuada por el mero hecho de que una regla pueda codificarse o un programa pueda devolver una respuesta. Debe declararse el ámbito profesional; la evidencia clínica y el gobierno experto deben constituir las reglas operativas; las observaciones han de atravesar una frontera explícita de admisión; la implementación debe ser conforme con la especificación fijada por versión que afirma ejecutar; y cada representación debe conservar las distinciones exigidas por su operación receptora declarada. En el caso de inmunología, P02 demuestra tanto una discrepancia entre especificación e implementación como una frontera condicional de pérdida de información, mientras que el puente experimental P25 muestra que la compresión deliberada puede ser completamente legítima. El método es un procedimiento trazable de constitución y verificación, no un agente autónomo validado clínicamente.

## Contribuciones del autor

Juan Antonio Lloret Egea: conceptualización; metodología; análisis formal; desarrollo de programas informáticos; validación; investigación; redacción del borrador original; revisión y edición del manuscrito.

## Financiación

Este estudio no recibió financiación externa.

## Conflictos de intereses

El autor declara no tener conflictos de intereses.

## Disponibilidad de datos y código

No existe un conjunto de datos de pacientes o cohortes que sustente los resultados. Las especificaciones e implementaciones de trabajo de inmunología están disponibles públicamente en el repositorio GitHub SVperitus-dataset. La inspección de P02 queda fijada al *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd`; la prueba de conformidad pertinente es `especificaciones/conformidad/test_immuno2.py` [24]. El repositorio público del lenguaje SV y su entorno web se identifican en la referencia 25.

## Declaración sobre el uso de IA generativa

OpenAI ChatGPT (GPT-5.6 Sol) se utilizó como herramienta de apoyo a la investigación para búsqueda bibliográfica, comprobación crítica de coherencia, estructuración del manuscrito, asistencia en formalización matemática y maquetación, y edición del inglés. Grok 4.5 (xAI) se utilizó para revisión crítica de versiones sucesivas del manuscrito, identificación de mejoras estructurales y matemáticas y sugerencias de presentación. DeepSeek-V4-Pro (DeepSeek AI) contribuyó a la revisión crítica y a la comprobación de coherencia formal. Todas las salidas de IA se trataron como insumos de investigación carentes de autoridad. El autor estableció, revisó y aprobó todas las definiciones, afirmaciones matemáticas, interpretaciones y conclusiones y asume plena responsabilidad por el manuscrito.

## Referencias

1. Peleg M. Computer-interpretable clinical guidelines: a methodological review. J Biomed Inform. 2013;46(4):744-763. doi:10.1016/j.jbi.2013.06.009.

2. Boxwala AA, Peleg M, Tu S, et al. GLIF3: a representation format for sharable computer-interpretable clinical practice guidelines. J Biomed Inform. 2004;37(3):147-161. doi:10.1016/j.jbi.2004.04.002.

3. Nan S, Tang T, Feng H, et al. A Computer-Interpretable Guideline for COVID-19: Rapid Development and Dissemination. JMIR Med Inform. 2020;8(10):e21628. doi:10.2196/21628.

4. Mehl G, Tunçalp Ö, Ratanaprayul N, et al. WHO SMART guidelines: optimising country-level use of guideline recommendations in the digital age. Lancet Digit Health. 2021;3(4):e213-e216. doi:10.1016/S2589-7500(21)00038-8.

5. Nash A, Segoufin L, Vianu V. Views and Queries: Determinacy and Rewriting. ACM Trans Database Syst. 2010;35(3):Article 21. doi:10.1145/1806907.1806913.

6. Lekadir K, Frangi AF, Porras AR, et al; FUTURE-AI Consortium. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554.

7. Strong J, Rogers H, Sun E, et al. Human-AI Collaboration in Healthcare: A Scoping Review. npj Digit Med. Publicado en línea el 20 de junio de 2026. doi:10.1038/s41746-026-02918-6.

8. van de Sande D, Economou-Zavlanos N, van Genderen ME. Meaningful oversight of medical AI beyond human in the loop. npj Digit Med. 2026;9:569. doi:10.1038/s41746-026-02971-1.

9. Müller J, Stoehr M, Oeser A, et al. A visual approach to explainable computerized clinical decision support. Comput Graph. 2020;91:1-11. doi:10.1016/j.cag.2020.06.004.

10. Royal Australasian College of Physicians. Clinical Immunology and Allergy – Advanced Training; Advanced Training in Immunology and Allergy curriculum standards. Nuevo currículo aprobado en marzo de 2025; implantación desde 2027. Consultado el 26 de agosto de 2026. https://www.racp.edu.au/trainees/advanced-training/clinical-immunology-and-allergy

11. Royal College of Physicians and Surgeons of Canada. Clinical Immunology and Allergy Competencies. Version 2.0. 2025. En vigor desde el 1 de julio de 2025.

12. General Medical Council. Allergy curriculum. Currículo vigente: Allergy curriculum 2021. Página publicada el 1 de marzo de 2023. Consultado el 26 de agosto de 2026. https://www.gmc-uk.org/education/standards-guidance-and-curricula/curricula/allergy-curriculum

13. Accreditation Council for Graduate Medical Education. ACGME Program Requirements for Graduate Medical Education in Allergy and Immunology. 2026. https://www.acgme.org/globalassets/pfassets/programrequirements/2026-prs/020_allergyimmunology_2026.pdf

14. Lloret Egea JA. Fundamentos algebraico-semánticos del Sistema Vectorial SV. IA eñ. Publicado el 9 de marzo de 2026. doi:10.21428/39829d0b.b0cf9a13.

15. Lloret Egea JA. Álgebra de composición intercelular del marco SV-IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema. IA eñ. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.5c31d534.

16. Lloret Egea JA. Formalización de una interfaz visual estructurada en el Sistema Vectorial SV. IA eñ. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.b96fee32.

17. Lloret Egea JA. Fundamentos, exigencias y arquitectura general de los agentes especializados en el Sistema Vectorial SV: formulación transversal desde el caso director del Agente Especializado en Inmunología. IA eñ. Publicado el 12 de abril de 2026. doi:10.21428/39829d0b.183e10f3.

18. Lloret Egea JA. Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable. Prepublicación. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.f471b07c.

19. Lloret Egea JA. Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity. IA eñ. Publicado el 8 de agosto de 2026. doi:10.21428/39829d0b.f0892864.

20. Lloret Egea JA. Informational Substitution Does Not Transfer Authority in AI-Assisted Decision Systems. Prepublicación. Publicado el 14 de agosto de 2026. doi:10.21428/39829d0b.d6cb2e1d.

21. Lloret Egea JA. De SVcustos, el marco de intrusión, hasta SVperitus: IMMUNO-1 – Profilaxis infecciosa y vacunación. Célula SV(25,5). IA eñ. Publicado el 5 de marzo de 2026. doi:10.21428/39829d0b.272c2f67.

22. Kamboj M, Bohlke K, Baptiste DM, et al. Vaccination of adults with cancer: ASCO guideline. J Clin Oncol. 2024;42(14):1699-1721. doi:10.1200/JCO.24.00032.

23. Taplitz RA, Kennedy EB, Bow EJ, et al. Antimicrobial prophylaxis for adult patients with cancer-related immunosuppression: ASCO and IDSA clinical practice guideline update. J Clin Oncol. 2018;36(30):3043-3054. doi:10.1200/JCO.18.00374.

24. Lloret Egea JA. SVperitus-dataset [programas informáticos y especificaciones]. GitHub. Repositorio: juantoniolloretegea/SVperitus-dataset. Inspección de fuente fijada al *commit* 1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd, de 24 de agosto de 2026. Consultado el 26 de agosto de 2026. https://github.com/juantoniolloretegea/SVperitus-dataset

25. Lloret Egea JA. SV-lenguaje-de-computacion [programas informáticos y especificación del lenguaje]. GitHub. Repositorio: juantoniolloretegea/SV-lenguaje-de-computacion. Entorno web público: https://lenguaje-sv.itvia.online/. Consultado el 26 de agosto de 2026. https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion

26. Lloret Egea JA. Resolution Frontiers in Stratified Ternary Cells: Infection Prophylaxis, Vaccination, and AI System Integrity. Prepublicación. Publicado el 20 de agosto de 2026. doi:10.21428/39829d0b.739ed2b6.
