Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0 | ISSN 2695-6411

Versión: 1 | Lugar y fecha: Madrid, 11/03/2026

---

# Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable

## Resumen

Este trabajo formaliza una capa semántica auditada en el Sistema Vectorial SV como arquitectura de interfaz entre dominio, representación ternaria, consulta formal y clausura estructural. La tesis central sostiene que dicha capa no debe entenderse como teoría general del significado ni como sustituto de técnicas estadísticas o inferenciales, sino como disciplina rigurosa de entrada legítima, conservación honesta de la indeterminación y devolución trazable de resultados. El régimen constitutivo del sistema es eventivo: la evolución se organiza por sucesos declarados y reevaluación discreta, mientras que el tiempo comparece sólo como medida o metadato de auditoría. Sobre esa base, la entrada del dominio se articula mediante captura, admisibilidad y transducción al alfabeto `{0,1,U}`; la salida, mediante consulta trazable reconstruible desde trayectoria, justificación y metadatos. La `U` se interpreta como indeterminación estructural y no como probabilidad, mezcla o ausencia trivial de valor. El programa experimental se apoya en la célula meta SV(9,3)-IA, cuyo universo completo de `3^9 = 19.683` vectores permite verificación exhaustiva sin estadística, minería de datos, inferencia ni aprendizaje opaco. En el estado técnico público aquí tomado como referencia, los invariantes estructurales defendidos encuentran expresión explícita en N4/Uso del Lenguaje SV mediante la IR canónica v0.2, sin que la tesis del artículo dependa de una versión concreta del lenguaje.

## Abstract

This work formalizes an auditable semantic layer within the SV System as an interface architecture between domain input, ternary representation, formal query and structural closure. The central thesis is that this layer should not be understood as a general theory of meaning nor as a substitute for statistical or inferential techniques, but as a rigorous discipline of legitimate input, honest preservation of indeterminacy and traceable output. The constitutive regime of the system is event-based: evolution is governed by declared events and discrete reevaluation, while time appears only as measurement or audit metadata. On this basis, domain input is processed through capture, admissibility and transduction into the alphabet `{0,1,U}`; output is produced through traceable query reconstructable from trajectory, justification and metadata. `U` is treated as structural indeterminacy rather than probability, mixture or trivial absence of value. The experimental program is grounded in the SV(9,3)-IA meta-cell, whose complete state space of `3^9 = 19,683` vectors enables exhaustive verification without statistics, data mining, inference or opaque learning. In the current public technical state, the structural invariants defended in this article already find explicit expression in N4/Usage of the SV Language through canonical IR v0.2, although the thesis itself does not depend on any particular language version.

## Palabras clave

Sistema Vectorial SV; semántica estructural; transducción ternaria; indeterminación; consulta trazable; reproducibilidad; Lenguaje SV; SV(9,3)-IA.

## 1. Introducción

El objeto de este trabajo no consiste en construir una teoría general del significado, ni en ofrecer una variante terminológica de arquitecturas inferenciales opacas, ni en prometer una solución total al problema del lenguaje. Su finalidad es más delimitada y, por ello mismo, más susceptible de cierre riguroso: establecer bajo qué condiciones puede formalizarse en el Sistema Vectorial SV una capa semántica auditada capaz de admitir contenido procedente de un dominio, traducirlo legítimamente al alfabeto ternario, conservar la indeterminación cuando el cierre no sea lícito y devolver una respuesta trazable compatible con la trayectoria del sistema.

La exposición seguirá una progresión estrictamente estructural. En primer lugar, se fijará el régimen del cambio por sucesos. En segundo lugar, se formalizará la entrada del dominio mediante captura, admisibilidad y transducción. En tercer lugar, se tratará la consulta formal y la trazabilidad de la respuesta. Sólo después se abordarán el estatuto de la `U`, la relación con el Lenguaje SV y las condiciones de clausura. Esta secuencia no responde a una conveniencia pedagógica superficial, sino a la jerarquía interna del problema: algunos conceptos sólo adquieren sentido preciso una vez fijados sus suelos formales previos.

La delimitación negativa del trabajo debe ser explícita. Quedan fuera del fundamento del artículo la estadística, la minería de datos, la inferencia y el aprendizaje opaco. Esta exclusión no tiene carácter polémico, sino constitutivo: el propio marco SV adoptado aquí no delega en tales mecanismos la legalidad de la entrada, la resolución de la indeterminación ni la trazabilidad de la respuesta. Cuando no exista cobertura suficiente, el sistema deberá mantener `U`, degradar o rechazar, antes que producir una apariencia de cierre.

Debe fijarse también una precisión de alcance respecto del alfabeto. Este trabajo se desarrolla íntegramente dentro de la suficiencia local de la terna `{0,1,U}` para el problema formal tratado. No se introduce aquí arquitectura cuaternaria alguna. La ampliación del alfabeto sólo sería legítima si apareciera una contradicción estructural no resoluble dentro de la terna. En ausencia de esa contradicción, la complicación algebraica carecería de fundamento metodológico. La suficiencia de la terna `{0,1,U}` se establece exclusivamente en el dominio formal delimitado en este trabajo y no constituye una afirmación de completitud semántica universal.

## 2. Marco formal mínimo

Sea \(H\) un conjunto no vacío de **sucesos admisibles** y sea \(S\) un conjunto de **frames** o estados semánticamente evaluables del sistema. La dinámica básica se formula mediante una aplicación parcial de transición:

\[
T: S \times H \rightharpoonup S
\]

donde \(T(s,h)\) está definida si y sólo si el suceso \(h\) pertenece al horizonte pertinente del estado \(s\) y satisface las condiciones mínimas de admisibilidad.

Sea además el alfabeto ternario canónico:

\[
\Sigma = \{0,1,U\}
\]

y sea \(P=\{p_1,\dots,p_n\}\) un conjunto finito de parámetros semánticamente relevantes. Una **configuración ternaria** es una función:

\[
v : P \to \Sigma
\]

que, fijado un orden en \(P\), podrá representarse como vector de \(\Sigma^n\).

Se introduce una aplicación de captura:

\[
C : D \rightharpoonup O
\]

desde un dominio \(D\) de entradas o contenidos posibles hacia un espacio \(O\) de observaciones utilizables, y un predicado de admisibilidad:

\[
A : O \to \{\mathrm{adm},\mathrm{inad}\}
\]

tal que sólo las observaciones \(o \in O\) con \(A(o)=\mathrm{adm}\) pueden entrar en la cadena de transducción.

La **transducción ternaria** se expresa mediante una aplicación parcial:

\[
\tau : O \rightharpoonup \Sigma^n
\]

definida sobre observaciones admisibles. Si una observación no dispone de fundamento suficiente para clausurarse en \(0\) o \(1\) respecto de un parámetro, el valor correspondiente deberá ser \(U\), salvo regla conservadora explícita fijada ex ante.

Para el tratamiento de cierre se introduce un predicado de clausura:

\[
\operatorname{Cl} : \Sigma^n \to \{\mathrm{cerrable},\mathrm{no\_cerrable},\mathrm{rechazable}\}
\]

que decide, respecto de una configuración ternaria \(v\), si el sistema puede cerrarse sobre sí mismo, si debe permanecer en régimen de indeterminación estructural o si debe rechazar la operación.

Finalmente, la consulta formal se modela mediante una aplicación:

\[
Q : S \times \mathcal{Q} \to R \times J \times M
\]

donde \(\mathcal{Q}\) es un conjunto de firmas de consulta, \(R\) el espacio de respuestas, \(J\) el espacio de justificaciones y \(M\) el espacio de metadatos.

## 3. Régimen del cambio: primacía del suceso

Toda semántica rigurosa del SV debe comenzar por una tesis básica: el sistema no cambia porque transcurra el tiempo, sino porque se instancian sucesos pertenecientes a un horizonte declarado. Esta tesis excluye de entrada una semántica basada en flujos continuos, en evolución temporal difusa o en gradientes interpretativos no vinculados a acontecimientos formalmente pertinentes.

El horizonte de sucesos no se identifica con una colección empírica de “cosas que pasan”, ni con una estadística de frecuencias. Es una declaración formal de relevancia. Un suceso entra en el horizonte cuando su presencia, su ausencia verificada o su indeterminación pueden alterar legítimamente la reevaluación del sistema.

## 4. Entrada legítima del dominio: captura, admisibilidad y transducción

Si el régimen de sucesos gobierna el cambio del sistema, la cadena de captura, admisibilidad y transducción gobierna la entrada del dominio. No existe acceso directo ni transparente del mundo a la representación ternaria. Entre ambos media una secuencia formal compuesta por captura, admisibilidad, transducción al alfabeto `{0,1,U}` e interfaz paramétrica, dejando además una región no absorbida por la cobertura finita de toda interfaz: la `U` silenciosa.

La captura produce material formalmente manipulable; la admisibilidad establece si ese material puede entrar legítimamente en la cadena de transducción; la transducción lo expresa en el alfabeto ternario; y la interfaz paramétrica lo integra en la estructura del sistema. Ninguno de estos pasos equivale por sí mismo a verdad, resolución o clausura.

`U` no codifica incertidumbre cuantificable ni distribución de probabilidad alguna; su naturaleza es estrictamente estructural y dependiente de condiciones de admisibilidad y resolución. Se llamará `U` al valor ternario asignado a un parámetro o configuración cuando, dadas las condiciones de captura, admisibilidad, contexto y mecanismo de resolución disponibles, no existe clausura legítima en `0` o `1` sin pérdida estructural.

## 5. Consulta formal y trazabilidad

Consultar no equivale a preguntar a un modelo opaco, sino a activar algebraicamente una arquitectura especializada y obtener una respuesta compatible con trayectoria, justificación y metadatos. La consulta no reemplaza la historia del sistema por un acto puntual de decisión; la hace legible.

La respuesta sólo es legítima si puede reconstruirse desde los componentes ya constituidos del sistema. Esto confiere a la capa semántica una responsabilidad doble: hacer inteligible la salida y no ocultar la indeterminación residual que siga afectándola.

## 6. U como indeterminación estructural y trayectoria

`U` no puede tratarse como probabilidad, mezcla, `null`, `NaN` o valor intermedio. Su especificación exige contexto y mecanismo de resolución, admite reaperturas y retornos a `U` cuando cae el fundamento previo, y prohíbe su colapso silencioso.

Si la indeterminación puede persistir, reaparecer o resolverse sólo bajo ciertas condiciones, entonces la capa semántica no consiste en expulsar `U` del sistema cuanto antes, sino en tratarla con la misma dignidad formal que a los estados cerrados.

## 7. Representación geométrica auxiliar

La representación plana sigue siendo semánticamente suficiente; la elevación de `U` en `ℝ³` es auxiliar; y el parámetro `h` no cuantifica incertidumbre ni redefine el signo. Su función es epistémica. La representación geométrica no participa en la constitución semántica del sistema; su eliminación no altera ningún resultado formal del presente trabajo.

Las magnitudes derivadas —`L₂`, `L₃`, `ΔL`, `Cz`, `Eρ`, `Ez`— permiten estudiar de forma visible cierta textura estructural de la indeterminación y de sus transiciones, y ofrecen resultados formalmente verificables como `Ez = k(v)·h²`. La geometría refuerza; no funda.

## 8. Relación con el Lenguaje SV

El artículo no se formula al margen del lenguaje. Debe dialogar con el **Lenguaje SV** con plena precisión terminológica: archivos `.svp`, IR canónica, niveles ontológicos y, especialmente, N4/Uso. La tesis del artículo se formula a nivel de invariantes estructurales, mientras que el estado técnico público actual del Lenguaje SV funciona como primera materialización explícita de varios de esos compromisos.

El presente trabajo no identifica la semántica del SV con la IR canónica v0.2. Sostiene, más precisamente, que N4/Uso del Lenguaje SV constituye, en el estado técnico público actual, una instancia explícita en la que varios de los compromisos estructurales aquí formulados encuentran expresión formal reconocible. Las referencias a IR v0.2 deben entenderse como instancia concreta de invariantes estructurales, no como dependencia versionada del modelo.

En este artículo, el término **puerto semántico** designa exclusivamente una frontera formal de exposición controlada del sistema cuando no es posible alcanzar clausura interna bajo condiciones de admisibilidad. No constituye una vía de corrección silenciosa del Lenguaje SV ni un mecanismo de delegación de decisión. Tampoco constituye una interfaz técnica ni un canal de integración, sino una noción formal de frontera estructural en ausencia de clausura legítima.

## 9. Antecedentes y posición del trabajo

El presente artículo no surge en vacío histórico. La problemática de los sistemas multivaluados, de los valores indefinidos y de las semánticas formales cuenta con antecedentes bien conocidos en lógica y teoría de la computación. Existen, en particular, tradiciones relacionadas con lógicas ternarias y multivaluadas, sistemas con valores indefinidos, semánticas modales y arquitecturas formales de consulta o evaluación.

Ahora bien, el trabajo aquí presentado no se identifica sin más con esas familias previas. Su especificidad reside en la conjunción de cinco rasgos: primacía del suceso sobre el tiempo como motor del cambio; cadena explícita de captura, admisibilidad y transducción; tratamiento de `U` como indeterminación estructural con persistencia, resolución y reapertura; consulta formal con exigencia de trazabilidad integral; y realización exhaustiva sobre un banco de prueba ternario completo sin recurrir a estadística ni inferencia opaca.

## 10. Metodología experimental, tres vallas y reproducibilidad

La parte experimental del trabajo no cumple una función ornamental. Su objeto es someter a prueba, de forma exacta y reproducible, las afirmaciones teóricas formuladas previamente. El diseño experimental no adopta una lógica estadística ni inferencial, sino una lógica de recorrido exhaustivo, construcción explícita y verificación computacional reproducible.

El objeto experimental primario es la célula meta **SV(9,3)-IA**, con `n=9`, umbral `T(9)=7` y universo completo `3^9 = 19.683`. Esta célula se adopta no porque agote el sistema, sino porque permite una primera verificación fuerte, exacta y exhaustiva sin aproximación. La elección de SV(9,3)-IA no responde a simplificación, sino a la posibilidad de verificación exhaustiva, lo cual constituye una condición más fuerte que cualquier validación aproximativa.

La experimentación se organiza mediante un régimen de **tres vallas**:
1. **Valla doctrinal**: verifica que la afirmación sometida a prueba pertenece legítimamente al horizonte del artículo y no introduce elementos prohibidos.
2. **Valla formal-computacional**: exige que la afirmación pueda traducirse a procedimiento exacto, reproducible y verificable.
3. **Valla de clausura con calidad**: determina si el resultado obtenido puede entrar en el cuerpo fuerte del artículo o si permanece como material en revisión.

### 10.1. Estatuto de validación del presente trabajo

La validación ofrecida en este artículo es, en sentido estricto, **interna al marco formal adoptado**. El trabajo no pretende demostrar la verdad externa del Sistema Vectorial SV frente a un dominio independiente ni competir empíricamente con arquitecturas predictivas de otra naturaleza. Su objetivo es más delimitado: explicitar, formalizar y verificar la coherencia y realizabilidad de una capa semántica auditada dentro del propio marco SV.

### 10.2. Criterios de refutación o fallo

Se consideran criterios de refutación o debilitamiento del modelo:
- imposibilidad de recorrer exhaustivamente el universo `3^9` o inconsistencias en su partición;
- existencia de consultas cuyo resultado no pueda reconstruirse desde trayectoria, justificación y metadatos;
- necesidad de colapsar `U` sin contexto y mecanismo explícitos;
- contradicciones entre las magnitudes geométricas auxiliares y la estructura ternaria;
- imposibilidad de expresar, en el estado técnico público del Lenguaje SV, los compromisos estructurales invocados.

## 11. Resultados experimentales

### 11.1. Partición exhaustiva del espacio ternario

Se ha generado y recorrido exhaustivamente el universo completo de configuraciones `v ∈ {0,1,U}^9`, con cardinalidad `3^9 = 19.683`. El dataset primario contiene la enumeración íntegra del espacio, junto con los conteos y estructuras derivados pertinentes. La ejecución del script de generación verifica cardinalidad, integridad y codificación homogénea.

El resultado principal es que el espacio ternario de la célula meta es íntegramente recorrible, clasificable y verificable sin necesidad de muestreo ni aproximación.

![Figura 1. Partición exhaustiva del espacio ternario de la célula meta SV(9,3)-IA en coordenadas (n₁, n_U). La figura no sustituye la partición algebraica: la hace visible.](fig_01_sv93_particion_exhaustiva.png)

**Figura 1.** Partición exhaustiva del espacio ternario de la célula meta SV(9,3)-IA en coordenadas `(n₁, n_U)`.

### 11.2. Trayectorias estructurales de la indeterminación

Se han construido y verificado familias de trayectorias de `U`, incluyendo resolución (`U→0`, `U→1`), persistencia (`U→U`), reapertura (`0→U`, `1→U`) y ciclos (`0→U→0`, `1→U→1`). Cada trayectoria queda registrada con su secuencia de estados y su justificación estructural.

El resultado principal es que la `U` presenta comportamiento dinámico formalizable mediante trayectorias exactas dependientes de sucesos, y no mediante gradientes, probabilidades o heurísticas.

![Figura 2. Trayectorias estructurales ejemplares de U. La ordenación vertical 0, U, 1 se usa sólo para legibilidad y no introduce ordinalidad semántica.](fig_02_trayectorias_u.png)

**Figura 2.** Trayectorias estructurales ejemplares de `U`.

### 11.3. Consulta trazable

Se ha implementado un conjunto de consultas formales cuyo resultado incluye vector de entrada, trayectoria relevante, justificación explícita, política de `U`, criterio de clausura y metadatos. Cada salida puede reconstruirse íntegramente desde sus componentes formales.

El resultado principal es que la capa semántica devuelve respuestas auditables y reconstruibles. La consecuencia es que el sistema opera sin inferencia negra: su semántica de uso es formalmente trazable.

### 11.4. Verificación geométrica auxiliar

Se han calculado y contrastado las magnitudes geométricas auxiliares relevantes, con especial atención a la verificación de la relación `Ez = k(v)·h²`. Los resultados muestran coherencia entre la estructura ternaria y la visualización auxiliar.

![Figura 3. Verificación geométrica auxiliar de la relación E_z = k(v)·h² para h=1. La figura refuerza la inteligibilidad; no constituye la semántica del sistema.](fig_03_verificacion_geometrica_auxiliar.png)

**Figura 3.** Verificación geométrica auxiliar de la relación `E_z = k(v)·h²` para `h=1`.

### 11.5. Clausura y frontera semántica

Se han estudiado casos formales de cierre autónomo, degradación a `U`, rechazo y apertura de frontera controlada. Estos casos se alinean con nociones análogas ya reconocibles en N4/Uso del Lenguaje SV, especialmente en torno a `u_policy`, `transduction_policy` y `closure_criterion`.

El resultado principal es que el sistema distingue de forma formal y reproducible cuándo puede cerrarse y cuándo debe permanecer abierto, degradado o expuesto a una frontera controlada.

![Figura 4. Régimen experimental de tres vallas: licitud doctrinal, código exacto y clausura con calidad. La figura sintetiza la disciplina de paso del programa experimental.](fig_04_tres_vallas.png)

**Figura 4.** Régimen experimental de tres vallas: licitud doctrinal, código exacto y clausura con calidad.

## 12. Discusión crítica y análisis adversarial

La arquitectura propuesta no se presenta como heurística eficaz ni como modelo aproximativo, sino como formalización exacta de una capa semántica auditada. Una primera objeción afecta a la expresividad de la terna `{0,1,U}`. La respuesta del presente trabajo es precisa: no se afirma que la terna capture toda la riqueza imaginable del dominio, sino que es suficiente como infraestructura de decisión estructural para el problema aquí tratado.

El presente trabajo no se plantea como alternativa comparativa frente a arquitecturas de aprendizaje estadístico, sino como formalización de un régimen estructural distinto, no reducible a términos de rendimiento predictivo.

## 13. Condiciones de aplicabilidad y límites

La arquitectura propuesta es aplicable cuando el dominio puede describirse en términos de sucesos relevantes, existe un criterio de admisibilidad formalizable, la transducción al alfabeto `{0,1,U}` es legítima, la indeterminación puede mantenerse sin forzar cierre y las consultas requieren trazabilidad estructural.

El modelo presenta también límites claros. No sustituye a sistemas de predicción probabilística, no optimiza decisiones bajo incertidumbre estadística, no modela fenómenos continuos sin discretización previa y no pretende capturar toda la complejidad semántica del lenguaje natural.

## 14. Conclusión

Se ha desarrollado una formalización rigurosa de la capa semántica del Sistema Vectorial SV como interfaz auditada entre dominio y representación. El trabajo ha mostrado que el régimen de sucesos sustituye al tiempo como principio organizador; que la entrada del dominio puede disciplinarse mediante captura, admisibilidad y transducción; que la `U` admite tratamiento estructural, persistencia, resolución y reapertura; que la consulta puede ser completamente trazable; y que la clausura puede gobernarse formalmente.

La suficiencia de la terna `{0,1,U}` defendida en este artículo tiene alcance local, estructural y condicionado por el problema formal tratado. No se afirma que dicha terna agote toda posibilidad semántica concebible, sino que, dentro del régimen de sucesos, admisibilidad, transducción, consulta y clausura aquí formalizado, no ha aparecido contradicción local suficiente que obligue a una ampliación del alfabeto. En este sentido preciso, la terna no se adopta por costumbre ni por reducción previa del problema a su medida, sino porque hasta este punto continúa absorbiendo legítimamente el fenómeno que se le exige formalizar.

## 15. Referencias

Lloret Egea, J. A. (s. f.). *Sistema Vectorial SV: Matemática y semántica* [Repositorio]. GitHub. https://github.com/juantoniolloretegea/SV-matematica-semantica

Lloret Egea, J. A. (s. f.). *Lenguaje de computación del Sistema Vectorial SV* [Repositorio]. GitHub. https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion

Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta* (Release 2). ITVIA. https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iii-horizonte-de-sucesos-y-reevaluacion-discreta/release/2

Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema* (Release 1). ITVIA. https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iv-transduccion-al-alfabeto-ternario-e-interfaz-parametrica-del-sistema/release/1

Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — V. Invariantes, agentes especializados y operador de consulta del sistema* (Release 2). ITVIA. https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--v-invariantes-agentes-especializados-y-operador-de-consulta-del-sistema/release/2

Lloret Egea, J. A. (2026). *Álgebra de composición intercelular del marco SV — VI. Análisis discreto, representaciones y herramientas de secuencias del sistema* (Release 1). ITVIA. https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--vi-analisis-discreto-representaciones-y-herramientas-de-secuencias-del-sistema/release/1

Lloret Egea, J. A. (2026). *Transiciones estructurales y trayectorias de la U en el Sistema Vectorial SV* (Release 2). ITVIA. https://www.itvia.online/pub/transiciones-estructurales-y-trayectorias-de-la-u-en-el-sistema-vectorial-sv/release/2

Lloret Egea, J. A. (2026). *Análisis del comportamiento geométrico del polígono del Sistema Vectorial SV: Del plano cartesiano a una carta espacial afín auxiliar como vía de razonamiento para situaciones complejas* (Release 2). ITVIA. https://www.itvia.online/pub/analisis-del-comportamiento-geometrico-del-poligono-del-sistema-vectorial-sv-del-plano-cartesiano-a-una-carta-espacial-afin-auxiliar-como-via-de-razonamiento-para-situaciones-complejas/release/2

Lloret Egea, J. A. (2026). *Compilador doctrinal y célula meta SV(9,3)-IA* (Release 5). ITVIA. https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/5

SVcustos / SVperitus. (s. f.). *Dataset SV(9,3)-IA* [Conjunto de datos]. En *Compilador doctrinal y célula meta SV(9,3)-IA*. ITVIA. https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/5

