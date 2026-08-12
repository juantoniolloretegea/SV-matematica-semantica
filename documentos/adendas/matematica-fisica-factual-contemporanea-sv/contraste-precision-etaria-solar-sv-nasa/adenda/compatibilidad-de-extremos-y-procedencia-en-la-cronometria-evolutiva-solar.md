# Compatibilidad de extremos y procedencia en la cronometría evolutiva solar

## Un criterio reproducible para combinar anclajes de edad presente y fronteras evolutivas futuras

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
Autor de correspondencia: publicaciones@itvia.es

> **Preprint — 10 de agosto de 2026.** Esta versión no ha sido sometida a revisión por pares.

## Resumen

**Contexto.** La cronometría solar y estelar combina edades radiométricas, edades estelares dependientes de modelo, hitos de trayectorias evolutivas y enunciados redondeados sobre la duración de las fases. La igualdad de unidades no garantiza un origen temporal común ni una misma frontera evolutiva; por ello, la combinación de registros heterogéneos puede producir residuales numéricos precisos sin definir una única trayectoria cronológica física.

**Objetivos.** Se formula un criterio de admisibilidad específico de trayectoria para determinar cuándo pueden componerse un anclaje de edad presente, un intervalo evolutivo restante y un enunciado de edad terminal. El criterio se aplica a registros solares heterogéneos, incluido un residual de 432 Myr comunicado anteriormente.

**Métodos.** Cada registro temporal se caracteriza por dominio, origen, extremos, procedencia, unidad, clase de presentación y, cuando procede, la transformación de coordenadas aplicada antes de la composición. Se distingue el residual numérico de una terna escalar completa del residual físico de clausura, que sólo se asigna cuando los registros presentan extremos homólogos. Las sustituciones nominales se descomponen mediante un balance residual exacto.

**Resultados.** La trayectoria de Schröder y Connon Smith proporciona una referencia interna de consistencia:

```text
4,58 + 5,42 = 10,00 Gyr
```

Respecto de esa referencia, sustituir el intervalo de 5,42 Gyr por el valor redondeado de 5 Gyr aporta 0,420 Gyr al residual nominal. Sustituir además la coordenada de 4,58 Gyr de la trayectoria por el registro de 4,568 Gyr del Sistema Solar utilizado anteriormente aporta otros 0,012 Gyr y conduce a:

```text
0,420 + 0,012 = 0,432 Gyr
```

Se trata de una descomposición aritmética por procedencia, no de dos efectos físicos independientes. La clausura física permanece no resuelta porque no se aporta una transformación común de dominio y origen. Sustituir 5 por 6 Gyr desplaza todos los residuales numéricos en −1 Gyr. Asimismo, un bloque genérico de 1 Gyr atribuido a la fase de gigante roja no es admisible como representación del intervalo de 10,00 a 12,17 Gyr comprendido entre el final de la secuencia principal y el extremo de la rama de las gigantes rojas en la trayectoria empleada, salvo que se establezca la equivalencia de sus fronteras.

**Conclusiones.** El criterio convierte la semántica de los extremos y la procedencia en condiciones previas explícitas de toda composición cronológica. Proporciona un diagnóstico reproducible para agregar valores de la bibliografía y comparar escalas evolutivas estelares: la precisión aritmética se conserva, pero el significado físico sólo se asigna después de haber establecido una trayectoria cronológica común.

**Palabras clave:** Sol: evolución; estrellas: evolución; edades estelares; métodos analíticos; análisis de datos; tiempo.

## Antecedente del preprint

Una formulación anterior y materialmente distinta de una parte del ejemplo solar fue divulgada previamente en español como *Contraste de precisión etaria solar SV–NASA*, DOI `10.21428/39829d0b.22c326bf`. El presente trabajo no reproduce aquel texto ni lo traduce: introduce un formalismo de compatibilidad de extremos y procedencia, utiliza un referente evolutivo publicado, deriva la genealogía aritmética del residual de 432 Myr, elimina extrapolaciones posteriores que no pueden adscribirse a fronteras homólogas y restringe expresamente la interpretación física del resultado.

---

# 1. Introducción

Las edades estelares no son lecturas directas de un reloj. La edad de una estrella se infiere mediante un marco físico o empírico cuya exactitud depende de las observaciones disponibles y de las hipótesis utilizadas para relacionar el estado presente con una historia evolutiva [1,2]. El Sol constituye un caso especialmente bien restringido porque su estado actual puede estudiarse mediante cronometría radiométrica, heliosismología, observaciones de neutrinos y modelos solares detallados.

Incluso en este caso privilegiado, la expresión «edad del Sol» puede designar magnitudes con orígenes operativos diferentes. Una edad meteorítica puede fechar un marcador de formación del Sistema Solar; una edad heliosismológica se obtiene ajustando la estructura interna solar; y una edad evolutiva es la coordenada temporal de una trayectoria estelar especificada. Las tres magnitudes están científicamente relacionadas, pero no son intercambiables por el solo hecho de expresarse en Gyr.

El mismo problema aparece al describir el futuro del Sol. Los cálculos de evolución estelar distinguen hitos como el final de la combustión central de hidrógeno, el comienzo de la combustión de hidrógeno en capa, el ascenso por la rama de las gigantes rojas, el extremo de esa rama, la ignición del helio y la rama asintótica de las gigantes. Las exposiciones dirigidas al público general condensan con frecuencia esa jerarquía en expresiones como «dentro de unos cinco mil millones de años» o «dentro de unos seis mil millones de años» antes de que el Sol se convierta en gigante roja. Esas expresiones son adecuadas a la resolución comunicativa para la que fueron formuladas, pero no especifican por sí mismas un mismo suceso terminal, un mismo modelo ni una misma precisión.

Tratarlas como datos numéricos exactos y libremente componibles puede generar residuales aparentemente precisos carentes de estatuto físico independiente.

El problema que se aborda es, por tanto, un problema de **composición cronológica**:

**¿Cuándo pueden tratarse un anclaje de edad, un intervalo evolutivo restante y un enunciado de edad terminal como coordenadas pertenecientes a una misma trayectoria cronológica física?**

Se propone un criterio de admisibilidad específico de trayectoria. Cada registro cronológico conserva, como mínimo:

- el objeto físico o dominio;
- el origen temporal;
- el suceso de referencia o presente;
- la frontera evolutiva terminal;
- la procedencia de la fuente o del modelo;
- la unidad;
- la clase de presentación, incluida la incertidumbre o el carácter redondeado;
- y cualquier transformación explícita aplicada antes de componer registros.

El residual numérico continúa siendo una cantidad aritmética ordinaria. Sin embargo, sólo se asigna un residual físico de clausura cuando se ha establecido la homología de los extremos. La compatibilidad semántica precede así a la propagación estadística: una pequeña diferencia numérica no sirve para inferir que las cantidades comparadas pertenezcan a la misma trayectoria.

Existen métodos astronómicos que resuelven capas próximas de este problema. Los esquemas de puntos evolutivos equivalentes coordinan las fases entre trayectorias estelares antes de interpolarlas [15], mientras que los modelos de procedencia astronómica preservan la genealogía de los productos de datos y de sus procesos de obtención [17]. Las revisiones sobre edades estelares y los estudios de modelos solares cuantifican, además, la dependencia respecto de métodos y modelos [1,2,6,7]. Esas herramientas son complementarias, pero no deciden por sí solas si una edad anclada en un origen, un intervalo futuro referido a una frontera determinada o insuficientemente determinada y una edad terminal procedente de otro registro constituyen una misma trayectoria cronológica.

Se distinguen de manera natural tres situaciones:

1. **Clausura interna.** Las cantidades proceden de un mismo modelo o cronología y poseen extremos homólogos.
2. **Comparación homóloga de procedencias distintas.** Existe una transformación explícita entre extremos, aunque las cantidades procedan de métodos o fuentes diferentes.
3. **Composición no homóloga.** Falta o es ambigua alguna identidad de extremos. La resta numérica puede existir, pero no se convierte en residual físico de clausura.

La aportación no consiste en proponer un nuevo reloj estelar. Consiste en hacer explícito un criterio que decide cuándo pueden componerse tiempos astronómicos heterogéneos y qué estatuto físico cabe atribuir al residual obtenido.

El ejemplo solar proporciona una prueba cuantitativa. En la trayectoria de Schröder y Connon Smith [13], el modelo solar presente a 4,58 Gyr y el modelo final de secuencia principal a 10,00 Gyr implican un intervalo restante de 5,42 Gyr:

```text
4,58 + 5,42 = 10,00 Gyr
```

Esta igualdad es una identidad interna de la propia trayectoria, no una validación independiente del modelo. Si el intervalo coherente de 5,42 Gyr se sustituye por el valor público redondeado de 5 Gyr, aparece un residual nominal de 0,420 Gyr. Si, además, la coordenada de 4,58 Gyr de la trayectoria se sustituye por el registro sistémico de 4,568 Gyr empleado en el preprint anterior, se añaden 0,012 Gyr y se obtienen 0,432 Gyr.

La descomposición:

```text
0,432 = 0,420 + 0,012 Gyr
```

es exacta como genealogía de sustituciones aritméticas. No constituye una descomposición de efectos físicos independientes. Como el registro del Sistema Solar y la frontera estelar terminal no vienen acompañados de una transformación común demostrada entre dominio y origen, el valor híbrido se conserva numéricamente pero no recibe estatuto de clausura física.

La misma disciplina explica por qué un bloque genérico de 1 Gyr asignado a la fase de gigante roja no puede trasladarse como duración precisa a una trayectoria cuyos hitos «final de secuencia principal» y «extremo de la rama de las gigantes rojas» se sitúan, respectivamente, en 10,00 y 12,17 Gyr.

El objetivo no es sustituir los cálculos de evolución estelar por aritmética. Es subordinar la aritmética cronológica a las definiciones físicas que hacen significativa la comparación. Esta necesidad aparece siempre que se agregan edades y duraciones procedentes de catálogos estelares, rejillas de modelos, tablas de revisión, material educativo o cadenas de tratamiento computacional.

# 2. Cronometría solar y fronteras evolutivas en la bibliografía

## 2.1. Las edades estelares son magnitudes inferidas

El punto de partida es que la edad estelar se infiere; no se observa directamente. Soderblom [1] revisó las técnicas disponibles y mostró que ningún método proporciona edades uniformemente exactas para todos los tipos y estados evolutivos de estrellas. Los procedimientos dependientes de modelos sitúan una estrella observada respecto de cálculos evolutivos; los procedimientos empíricos recurren a observables calibrados sensibles a la edad. La precisión alcanzable depende, por tanto, del objeto, de los observables y de la descripción física adoptada.

Lebreton, Goupil y Montalbán [2] analizaron con detalle esta dependencia. La edad inferida puede resultar sensible a las restricciones observacionales, la composición química inicial, las opacidades, las tasas de reacciones nucleares, los tratamientos de mezcla, la difusión, la convección y otros componentes de la física del modelo. Esta dependencia no constituye un defecto de la cronometría estelar: forma parte del significado mismo de una edad obtenida mediante un modelo.

Para el presente trabajo se sigue una consecuencia metodológica directa: una coordenada temporal extraída de un modelo evolutivo debe conservar la procedencia de ese modelo cuando se combina con un intervalo tomado de otra fuente.

El Sol permite añadir restricciones que no están disponibles para la mayoría de las estrellas. La heliosismología sondea su estructura interna y puede utilizarse para inferir una edad evolutiva. Bonanno, Schlattl y Paternò [3], incorporando correcciones relativistas en la ecuación de estado, obtuvieron como mejor ajuste heliosismológico:

```text
t_seis = 4,57 ± 0,11 Gyr                              (1)
```

Ese valor es una edad del objeto estelar inferida mediante un modelo de interior solar y diagnósticos sísmicos. Su significado operativo difiere del de una cronología radiométrica del Sistema Solar aunque los valores centrales sean próximos.

Un análisis heliosismológico bayesiano posterior de Bonanno y Fröhlich [4] muestra la dependencia respecto del modelo incluso cuando las anchuras estadísticas comunicadas son mucho menores. Modelos calibrados con distintas elecciones de tasas de reacción nuclear produjeron:

```text
4,587 ± 0,007 Gyr

4,569 ± 0,006 Gyr                                     (2)
```

La estrechez de cualquiera de esas distribuciones no elimina la dependencia respecto de la física adoptada.

Más recientemente, Bétrisey et al. [5] emplearon 26,5 años de observaciones de GOLF y BiSON y mostraron que la edad solar inferida por técnicas asterosismológicas presenta una huella medible del ciclo de actividad magnética. En su experimento de modelización encontraron variaciones de hasta el 6,5 % entre extremos de actividad. La edad física del Sol no cambia: el resultado cuantifica una sensibilidad sistemática del procedimiento inferencial. Esta distinción es directamente pertinente aquí: una coordenada cronológica no debe separarse de la procedencia del procedimiento que la estimó.

Los modelos solares estándar modernos aportan otro ejemplo. Vinyoles et al. [6] compararon modelos actualizados que incorporaban cambios en tasas de reacción, ecuación de estado, tratamiento de la opacidad y composición, y los contrastaron con observables heliosismológicos y de neutrinos. Christensen-Dalsgaard [7] revisó la estructura y evolución solares desde las ecuaciones de estructura estelar hasta la evolución en la secuencia principal, incluidos los efectos de las hipótesis físicas y de la implementación numérica.

Estos trabajos no se utilizan para seleccionar una única edad terminal privilegiada. Se utilizan para fijar una exigencia metodológica: una coordenada evolutiva solar pertenece a un modelo con física, calibración y condiciones de frontera declaradas; no puede reducirse a una edad escalar desprovista de contexto.

## 2.2. Cronometría del Sistema Solar y significado del origen

La cronometría radiométrica utiliza una convención de origen diferente.

Bouvier y Wadhwa [8] definieron explícitamente la edad del Sistema Solar mediante la formación de los primeros sólidos de la nebulosa solar y comunicaron una edad Pb–Pb de:

```text
4568,2 Myr                                             (3)
```

para una inclusión rica en calcio y aluminio, CAI.

Connelly et al. [9], mediante datación Pb–Pb corregida en uranio, obtuvieron un breve intervalo de formación de CAI correspondiente a:

```text
4567,30 ± 0,16 Myr                                    (4)
```

Estos valores no son lecturas repetidas de un reloj universal con diferente número de cifras. Proceden de cronómetros, muestras, correcciones y definiciones concretas del suceso que se fecha.

La importancia de declarar el origen temporal aparece con particular claridad en la cronometría estadística de Desch et al. [10]. Bajo una referencia especificada de ²⁶Al/²⁷Al, infirieron una edad para `t = 0` del Sistema Solar de:

```text
4568,42 ± 0,24 Myr                                    (5)
```

y defendieron la conveniencia de expresar los tiempos de formación respecto de un `t = 0` explícito cuando el objetivo es modelizar astrofísicamente la nebulosa solar.

La revisión reciente de Amelin y Yin [11] refuerza la separación entre resolución numérica y exactitud cronológica. Los métodos isotópicos actuales pueden resolver sucesos separados por escalas aproximadas de 0,1–0,3 Myr, pero siguen existiendo limitaciones relativas a exactitud, heterogeneidad isotópica y extracción de edades de sucesos a partir de materiales complejos. Añadir cifras decimales a un resultado cronométrico no equivale a establecer una coordenada temporal más universal; la definición del suceso y el cronómetro continúan formando parte de la magnitud.

Por consiguiente, un valor como 4,568 Gyr puede utilizarse como anclaje sistémico nominal cuando así se declara, pero no debe rebautizarse silenciosamente como edad heliosismológica del objeto solar. En sentido inverso, el valor central de 4,57 Gyr procedente de un ajuste heliosismológico no puede sustituir al `t = 0` definido por CAI sin declarar el cambio de objeto, origen y procedencia.

La diferencia numérica entre ambos registros puede ser pequeña respecto de la vida estelar y, sin embargo, ser formalmente relevante cuando se comunican residuales con resolución de Myr.

## 2.3. El futuro del Sol constituye una sucesión de fronteras definidas por modelos

Las predicciones sobre el futuro solar proceden de modelos de evolución estelar y no de una simple extrapolación de la edad presente. Sackmann, Boothroyd y Kraemer [12] desarrollaron un cálculo detallado de la evolución presente y futura del Sol hasta fases avanzadas. Schröder y Connon Smith [13] revisaron posteriormente el futuro lejano mediante un código evolutivo con una prescripción calibrada de pérdida de masa por viento frío.

La Tabla 1 de este último trabajo proporciona una secuencia especialmente útil de hitos cronológicos:

```text
Secuencia principal de edad cero (ZAMS)       0,00 Gyr
Modelo presente                               4,58 Gyr
Punto más caliente de la secuencia principal  7,13 Gyr
Modelo final de secuencia principal           10,00 Gyr
Extremo de la rama de las gigantes rojas      12,17 Gyr
Hitos posteriores de la AGB                   ~12,30 Gyr
```

El mismo estudio describe el cambio físico en torno a 10 Gyr: la combustión central de hidrógeno cede el paso a la combustión de hidrógeno en capa mientras el núcleo se contrae y las capas externas se expanden; después el Sol asciende por la rama de las gigantes rojas.

Ésta es una frontera físicamente especificada. No es equivalente a cualquier aparición de la expresión «se convierte en gigante roja» en material divulgativo, porque dicha expresión puede aludir al final de la combustión central de hidrógeno, al comienzo de una expansión apreciable, a una fase ya establecida en la rama de las gigantes rojas o a un hito posterior.

La propia tabla del modelo muestra por qué deben conservarse los nombres de los extremos. Desde el modelo presente hasta el modelo final de secuencia principal:

```text
H_MS^SC08
=
10,00 − 4,58
=
5,42 Gyr                                               (6)
```

Desde el final de la secuencia principal hasta el extremo de la rama de las gigantes rojas:

```text
Δ_MSf→RGBtip^SC08
=
12,17 − 10,00
=
2,17 Gyr                                               (7)
```

Ninguno de estos intervalos debe sustituirse por un número redondeado sin cambiar, al mismo tiempo, la clase de presentación de la magnitud.

Otros estudios resumen el futuro solar mediante escalas algo diferentes. Veras [14], al estudiar la dinámica del Sistema Solar a largo plazo, señala que una estrella de una masa solar alcanza una duración de secuencia principal próxima a 11 Gyr y que al Sol le quedan aproximadamente 6,5 Gyr en la secuencia principal. Sus integraciones incorporan después aproximadamente 1,5 Gyr de fases gigantes, y el mismo trabajo describe por separado una escala de unos 0,8 Gyr para la rama de las gigantes rojas.

Estos intervalos redondeados responden a preguntas dinámicas distintas de las que definen los hitos tabulados por Schröder y Connon Smith. No deben forzarse dentro de una misma denominación de fase por la sola coincidencia de unidades.

La importancia computacional de alinear las fases también aparece en la infraestructura de modelos estelares. Dotter [15], al construir las isocronas MIST, transformó las trayectorias evolutivas a una base evolutiva uniforme antes de interpolar entre masas y fases. Su procedimiento no es el criterio de clausura aquí propuesto, pero constituye un antecedente independiente de la idea subyacente: las coordenadas evolutivas sólo resultan comparables después de coordinar la estructura de fases pertinente.

Expresiones como «tiempo restante en la secuencia principal» o «duración de la rama de las gigantes» no son, por ello, escalares independientes de su fuente.

## 2.4. Los enunciados públicos redondeados constituyen una clase de presentación distinta

Las páginas públicas de NASA proporcionan un contraste útil precisamente porque condensan intencionadamente la secuencia solar futura. Una descripción pública indica que el Sol se convertirá en gigante roja dentro de unos 5 Gyr; otra exposición educativa sitúa el acercamiento a la evolución gigante aproximadamente 6 Gyr en el futuro [18,19].

Estos valores no tienen por qué interpretarse como mediciones mutuamente contradictorias. Son descripciones redondeadas elaboradas en contextos explicativos diferentes y sus fronteras físicas están menos especificadas que las de una tabla de trayectoria evolutiva.

En un análisis de precisión deben recibir, por tanto, una clase de presentación diferente de la correspondiente a los hitos de un modelo o a magnitudes con incertidumbre cuantificada.

El error metodológico aparecería si la palabra «aproximadamente» se leyera como si proporcionase un intervalo con precisión de milésimas de Gyr y, a continuación, las últimas cifras de una resta se interpretasen como precisión física.

La operación correcta es condicional: si 5 Gyr se adopta como representante nominal del enunciado redondeado, la aritmética respecto de ese representante puede ser exacta. El representante, sin embargo, sigue siendo redondeado y no adquiere una resolución metrológica que la fuente nunca le atribuyó.

## 2.5. Exactitud nominal y exactitud empírica son conceptos distintos

La metrología astronómica ofrece un precedente útil, aunque limitado, para distinguir exactitud numérica de estimación empírica.

La Resolución B3 de la UAI de 2015 definió determinadas magnitudes nominales solares y planetarias como constantes exactas de conversión. Prša et al. [16] subrayaron que esos valores nominales no constituyen las propiedades físicas verdaderas del Sol o de los planetas ni las mejores estimaciones actuales de dichas propiedades.

La exactitud puede ser, por consiguiente, una propiedad de una convención declarada sin implicar conocimiento exacto del objeto físico.

Los enunciados redondeados de 5 y 6 Gyr utilizados aquí **no** son constantes nominales de la UAI y no se les atribuye ese estatuto. La analogía es exclusivamente metrológica: una vez declarado un representante para un cálculo, la aritmética puede ser exacta condicionada a esa declaración, mientras que el contenido empírico y semántico permanece limitado por la fuente.

Esta distinción permite analizar el residual de 432 Myr del preprint anterior sin descartar su aritmética y, al mismo tiempo, sin atribuir a las entradas una precisión que no poseen.

# 3. Formalismo de clausura con tipificación de procedencia

## 3.1. Registros cronológicos y extremos

Sea `D` el objeto físico o dominio al que se refiere un enunciado cronológico. Sea `O` su origen temporal declarado, `P` un suceso presente o de referencia y `B` una frontera evolutiva terminal.

Se representa un registro cronológico mediante la tupla de metadatos:

```text
Θ = (D, O, P, B, S, u, π)                            (8)
```

donde:

- `S` designa la procedencia de la fuente o del modelo;
- `u`, la unidad;
- `π`, la clase de presentación, incluida cualquier incertidumbre declarada o el estatuto de redondeo.

Se distinguen tres magnitudes escalares según sus extremos:

```text
A = τ_D(P) − τ_D(O)                                   (9)

H = τ_D(B) − τ_D(P)                                  (10)

C = τ_D(B) − τ_D(O)                                  (11)
```

`A` es el anclaje de edad desde el origen hasta el suceso de referencia; `H`, el intervalo restante desde el suceso de referencia hasta la frontera; y `C`, el intervalo completo desde el mismo origen hasta esa misma frontera.

Si los tres registros se refieren al mismo `D`, `O`, `P` y `B`, la ley de composición cronológica es:

```text
C = A + H                                             (12)
```

La ecuación (12) es algebraicamente elemental. El contenido científico reside en las condiciones de tipado que deciden si las tres cantidades describen realmente una misma trayectoria.

Para el tratamiento de datos resulta útil escribir separadamente:

```text
𝔄 = (A; D_A, O_A, P_A, S_A, u_A, π_A)

ℍ = (H; D_H, P_H, B_H, S_H, u_H, π_H)

ℂ = (C; D_C, O_C, B_C, S_C, u_C, π_C)              (13)
```

Una condición necesaria de compatibilidad de extremos es:

```text
Γ_end = 1
si y sólo si

D_A ≃ D_H ≃ D_C
O_A ≃ O_C
P_A ≃ P_H
B_H ≃ B_C

y u_A, u_H, u_C son mutuamente convertibles.          (14)
```

El símbolo `≃` significa identidad o correspondencia justificada explícitamente.

La posibilidad de una correspondencia es importante. Un marcador de formación del Sistema Solar y un origen estelar ZAMS no son literalmente el mismo suceso. Un estudio puede relacionarlos mediante un desfase o una transformación física expresamente declarados, pero esa transformación debe **aplicarse** antes de evaluar la clausura.

Si los registros transformados a un sistema común se denotan por:

```text
Ã, Ĥ, C̃
```

la compatibilidad no autoriza a restar las coordenadas originales sin transformar. La proximidad numérica no crea identidad de extremos.

### Secuencia operativa de admisibilidad

Antes de cualquier propagación estadística, una composición propuesta se evalúa en el orden siguiente:

1. conservar dominio, origen, extremos del intervalo, procedencia, unidad y clase de presentación de cada registro;
2. comprobar la homología de extremos;
3. aplicar cualquier transformación de coordenadas declarada y registrar su procedencia;
4. normalizar las unidades que sean convertibles;
5. clasificar la relación de procedencia;
6. calcular `R_num` cuando exista una terna escalar completa;
7. asignar `ℛ` sólo después de haber establecido la compatibilidad;
8. propagar incertidumbres o intervalos únicamente para los registros que hayan superado la prueba de compatibilidad.

El fallo en los pasos 2 o 3 no elimina el valor aritmético cuando éste existe. Cambia su estatuto físico a **no resuelto**.

El orden es deliberadamente preestadístico: primero se pregunta si las magnitudes pertenecen a la misma trayectoria cronológica; después se pregunta con qué precisión se conoce dicha trayectoria.

## 3.2. Clases de procedencia

La compatibilidad de extremos no exige que todas las cantidades procedan de una misma publicación. Sí modifica, en cambio, la interpretación del residual.

Se distinguen tres clases.

### 1. Clausura interna

```text
S_A = S_H = S_C
```

o bien las tres magnitudes se extraen de un mismo modelo o cronología explícitamente coherentes.

Un residual no nulo indica entonces una inconsistencia de extracción, redondeo o implementación respecto de esa fuente.

### 2. Comparación homóloga entre procedencias distintas

La transformación de extremos está declarada y aplicada, pero las cantidades proceden de métodos o fuentes diferentes.

El residual mide una discrepancia entre esos registros bajo la transformación declarada. No constituye por sí solo una falsación de ninguna fuente.

### 3. Composición no homóloga

Una o más identidades de extremos están ausentes o son ambiguas.

La resta numérica puede efectuarse tras normalizar unidades, pero no se asigna un residual físico de clausura.

La clasificación evita un error categorial: un residual híbrido no se convierte en un nuevo observable de evolución estelar porque su valor numérico esté bien definido.

## 3.3. Residual numérico y residual físico

Para tres escalares expresados en unidades comunes puede calcularse:

```text
R_num = C − A − H                                     (15)
```

El residual con interpretación física se define solamente después del tipado de extremos y, cuando resulte necesario, después de aplicar la transformación declarada:

```text
                 C̃ − Ã − Ĥ,   si Γ_end = 1
ℛ(𝔄,ℍ,ℂ) = {
                 U,            si Γ_end ≠ 1
                               o no puede establecerse.       (16)
```

Cuando los extremos son literalmente idénticos, los valores transformados coinciden con los valores de origen.

`U` designa **clausura física no resuelta**, no incertidumbre estadística. Registra que la aritmética disponible no puede recibir la interpretación física solicitada con la información de extremos existente.

Un residual cero tiene, asimismo, un significado limitado. Si `A`, `H` y `C` proceden de una misma trayectoria, `ℛ = 0` confirma coherencia cronológica interna. No valida de manera independiente el modelo estelar.

En sentido inverso, un residual no nulo entre procedencias diferentes no implica necesariamente que una de las fuentes sea errónea. Puede ser la consecuencia esperable de orígenes, fronteras, hipótesis de modelo o resoluciones de presentación diferentes.

## 3.4. Cambio de origen

Supóngase que la coordenada temporal cambia mediante un desplazamiento común `δ`, mientras el intervalo físico comprendido entre `P` y `B` permanece invariable:

```text
A' = A + δ

C' = C + δ

H' = H                                               (17)
```

El residual es invariante:

```text
R'_num
=
C' − A' − H'
=
C − A − H
=
R_num                                                (18)
```

Esta identidad proporciona una prueba sencilla de auditoría.

Si el anclaje de edad cambia de una convención de origen a otra, pero la edad terminal `C` no se transforma de manera coherente, el residual cambia exactamente por el desfase no compensado.

Un cambio de origen debe actuar sobre todas las edades que funcionan como coordenadas y comparten ese origen. No actúa sobre el intervalo transcurrido `H`.

## 3.5. Sustituciones nominales y balance residual

Sean los símbolos con circunflejo representantes comunicados o adoptados:

```text
Â = A + ε_A

Ĥ = H + ε_H

Ĉ = C + ε_C                                         (19)
```

Entonces:

```text
R̂
=
Ĉ − Â − Ĥ

=
R + ε_C − ε_A − ε_H                                (20)
```

Para una terna de referencia coherente con `R = 0`:

```text
R̂ = ε_C − ε_A − ε_H                               (21)
```

Esta igualdad constituye el balance residual empleado para localizar la procedencia del residual solar.

Las sensibilidades locales son:

```text
∂R/∂C = +1

∂R/∂A = −1

∂R/∂H = −1                                         (22)
```

Si las magnitudes se proporcionan mediante intervalos y no mediante valores puntuales:

```text
A ∈ [A₋, A₊]

H ∈ [H₋, H₊]

C ∈ [C₋, C₊]                                       (23)
```

y no existen restricciones conjuntas adicionales, la monotonía proporciona la envolvente garantizada:

```text
R
∈
[C₋ − A₊ − H₊ ,
 C₊ − A₋ − H₋]                                     (24)
```

La ecuación (24) es una envolvente. No afirma que ambos extremos puedan alcanzarse simultáneamente cuando las entradas estén correlacionadas.

## 3.6. Identidad simétrica de la mitad del intervalo

El preprint anterior empleaba una clausura redondeada de secuencia principal:

```text
C = 10 Gyr
```

junto con una mitad nominal del intervalo:

```text
H = 5 Gyr
```

Bajo la condición especial:

```text
C = 2H
```

se cumple:

```text
R
=
C − A − H
=
H − A
=
C − (A + H)                                         (25)
```

Por consiguiente:

```text
5 − 4,568
=
10 − (4,568 + 5)
=
0,432 Gyr                                           (26)
```

Las dos expresiones de la ecuación (26) no constituyen comprobaciones independientes. Son el mismo residual escrito antes y después de trasladar por el semintervalo común.

Esta identidad es decisiva para reinterpretar el valor de 432 Myr sin doble cómputo de evidencia.

# 4. Matriz de datos y procedencia

La tabla siguiente reúne los registros utilizados en el contraste. Se mezclan deliberadamente clases cronológicas distintas porque el objetivo es determinar las condiciones bajo las cuales pueden componerse.

Ninguna fila se adopta como referencia cronométrica universal. Cada una conserva el objeto, el origen, el método, la frontera y la resolución de presentación declarados.

| Fuente | Valor comunicado | Objeto / dominio | Origen o referencia | Frontera / tipo de magnitud | Clase de presentación |
|---|---:|---|---|---|---|
| Bonanno et al. (2002) | 4,57 ± 0,11 Gyr | Sol | origen evolutivo del modelo solar | estado solar presente | edad heliosismológica inferida mediante modelo |
| Bonanno y Fröhlich (2015) | 4,587 ± 0,007 o 4,569 ± 0,006 Gyr | Sol | coordenada de modelo solar calibrado | estado solar presente | edad heliosismológica bayesiana; dependiente de modelo |
| Bouvier y Wadhwa (2010) | 4568,2 Myr | Sistema Solar | cronología de los primeros sólidos | marcador de formación de CAI | edad radiométrica Pb–Pb |
| Connelly et al. (2012) | 4567,30 ± 0,16 Myr | Sistema Solar | cronología nebular temprana | intervalo de formación de CAI | edad Pb–Pb corregida en uranio |
| Desch et al. (2023) | 4568,42 ± 0,24 Myr | Sistema Solar | `t = 0` declarado para ²⁶Al/²⁷Al canónico | `t = 0` del Sistema Solar | anclaje cronométrico estadístico |
| Schröder y Connon Smith (2008) | 4,58 Gyr | Sol / modelo | ZAMS | modelo presente | hito evolutivo tabulado |
| Schröder y Connon Smith (2008) | 10,00 Gyr | Sol / modelo | ZAMS | final de secuencia principal | hito evolutivo tabulado |
| Schröder y Connon Smith (2008) | 12,17 Gyr | Sol / modelo | ZAMS | extremo de la rama de las gigantes rojas | hito evolutivo tabulado |
| Páginas públicas NASA | aproximadamente 5 o 6 Gyr desde el presente | Sol | presente | evolución gigante descrita de forma amplia | enunciado público redondeado |
| Preprint SV anterior | `A_SS = 4,568 Gyr` | dominio Sistema Solar | origen sistémico declarado | corte sistémico presente | registro nominal adoptado |
| Preprint SV anterior | `A_⊙ = 4,570 Gyr` | objeto solar | origen solar declarado | corte solar presente | registro nominal adoptado |

Se desprenden dos conclusiones inmediatas.

En primer lugar, las magnitudes próximas a 4,57 Gyr no fechan todas el mismo suceso físico. Las cronologías radiométricas del Sistema Solar y una edad heliosismológica del objeto solar poseen definiciones operativas diferentes.

En segundo lugar, los enunciados sobre el futuro son todavía más heterogéneos. Un modelo final de secuencia principal tabulado y una expresión pública sobre «convertirse en gigante roja» no tienen necesariamente la misma frontera.

Para los ejercicios numéricos siguientes, el valor anterior:

```text
A_SS = 4,568 Gyr
```

se conserva únicamente como registro sistémico nominal porque es el valor que generó el residual previamente publicado de 432 Myr. No se presenta como una nueva medición ni se utiliza para desplazar las edades de la bibliografía.

El registro nominal del objeto solar:

```text
A_⊙ = 4,570 Gyr
```

se trata de la misma manera.

# 5. Contraste solar

## 5.1. Clausura interna de una trayectoria evolutiva publicada

El contraste más limpio comienza con una sola fuente y un único conjunto de extremos.

En Schröder y Connon Smith [13], el modelo solar presente tiene:

```text
A_SC08 = 4,58 Gyr                                     (27)
```

y el modelo final de secuencia principal:

```text
C_SC08 = 10,00 Gyr                                    (28)
```

Para esos mismos extremos, el intervalo restante de secuencia principal no constituye un dato empírico adicional, sino:

```text
H_SC08
=
C_SC08 − A_SC08

=
5,42 Gyr                                              (29)
```

Por tanto:

```text
ℛ_SC08
=
10,00 − 4,58 − 5,42

=
0                                                     (30)
```

El cero es una comprobación de consistencia interna, no una validación independiente del modelo.

La misma trayectoria proporciona una prueba de frontera posterior a la secuencia principal. Con el extremo de la rama de las gigantes rojas situado en 12,17 Gyr:

```text
Δ_MSf→RGBtip^SC08
=
12,17 − 10,00

=
2,17 Gyr                                              (31)
```

En consecuencia, un enunciado como «la fase de gigante roja dura 1 Gyr» no puede insertarse en esta trayectoria concreta entre final de secuencia principal y extremo de la rama de las gigantes rojas sin redefinir los extremos.

El problema no es que 1 Gyr sea aritméticamente imposible. El problema es que no representa el intervalo que esta trayectoria atribuye a esos dos sucesos nombrados.

## 5.2. Genealogía exacta del residual nominal de 432 Myr

La referencia interna coherente es:

```text
(A, H, C)_0
=
(4,58 ; 5,42 ; 10,00) Gyr

R_0 = 0                                               (32)
```

Primero se sustituye el intervalo de 5,42 Gyr por un representante público redondeado de 5 Gyr:

```text
ε_H
=
5,00 − 5,42

=
−0,420 Gyr                                           (33)
```

Con `A` y `C` sin modificar:

```text
R
=
−ε_H

=
+0,420 Gyr                                           (34)
```

Después se sustituye la coordenada presente de 4,58 Gyr de la trayectoria por el registro sistémico nominal de 4,568 Gyr:

```text
ε_A
=
4,568 − 4,580

=
−0,012 Gyr                                           (35)
```

El balance de la ecuación (21) produce:

```text
R̂
=
−ε_A − ε_H

=
0,012 + 0,420

=
0,432 Gyr                                            (36)
```

La descomposición:

```text
0,432 = 0,420 + 0,012 Gyr                            (37)
```

es exacta respecto de las sustituciones nominales declaradas.

No constituye dos pruebas independientes del mismo efecto físico. El primer término procede del cambio de intervalo evolutivo; el segundo, del cambio de coordenada presente. Además, como el registro sistémico de 4,568 Gyr y la frontera estelar de 10,00 Gyr no disponen aquí de una transformación común demostrada entre dominio y origen, la composición es híbrida.

El valor numérico se conserva, pero:

```text
ℛ = U                                                 (38)
```

para la clausura física.

## 5.3. Sensibilidad a los anclajes presentes

Para un cierre nominal fijo:

```text
C = 10 Gyr
```

y un intervalo nominal fijo:

```text
H = 5 Gyr
```

se define:

```text
H* = 10 − A

R_5 = 10 − A − 5                                     (39)
```

Los representantes centrales empleados producen:

| `A` (Gyr) | `H*` (Gyr) | `R_5` (Gyr) |
|---:|---:|---:|
| 4,56800 | 5,43200 | 0,43200 |
| 4,57000 | 5,43000 | 0,43000 |
| 4,56820 | 5,43180 | 0,43180 |
| 4,56730 | 5,43270 | 0,43270 |
| 4,56842 | 5,43158 | 0,43158 |
| 4,57000 | 5,43000 | 0,43000 |
| 4,56900 | 5,43100 | 0,43100 |
| 4,58700 | 5,41300 | 0,41300 |
| 4,58000 | 5,42000 | 0,42000 |

La dispersión entre el menor y el mayor de estos valores centrales de `R_5` es:

```text
0,43270 − 0,41300
=
0,01970 Gyr

=
19,70 Myr                                             (40)
```

Este resultado no constituye un presupuesto completo de incertidumbre de la edad solar. Compara únicamente las sustituciones nominales centrales seleccionadas.

Bétrisey et al. [5], por ejemplo, encontraron variaciones de hasta el 6,5 % en determinaciones asterosismológicas de la edad solar asociadas al ciclo de actividad, una escala del orden de 0,3 Gyr para un Sol de unos 4,6 Gyr. Por tanto, los 19,70 Myr de la tabla no deben interpretarse como incertidumbre empírica de la edad solar.

Lo que la tabla demuestra es más restringido: dentro de esta familia de representantes nominales, el cambio de anclaje central produce desplazamientos de escala Myr a decenas de Myr, mientras un cambio de 1 Gyr en el intervalo futuro se propaga uno a uno al residual.

## 5.4. Propagación local de incertidumbres declaradas

El formalismo es compatible con la propagación ordinaria de incertidumbre después de haber establecido la compatibilidad.

Si se propaga únicamente la incertidumbre heliosismológica:

```text
A = 4,57 ± 0,11 Gyr
```

de Bonanno et al. [3], manteniendo como representantes nominales fijos:

```text
C = 10 Gyr

H = 5 Gyr
```

se obtiene:

```text
R_5 ∈ [0,32 ; 0,54] Gyr                              (41)
```

porque un aumento del anclaje de edad disminuye el residual en la misma cuantía.

Para la cronometría de CAI de Connelly et al. [9], una incertidumbre de ±0,16 Myr en el anclaje desplaza en ±0,16 Myr un residual híbrido central próximo a 432,7 Myr.

Ninguna de estas propagaciones resuelve el problema conceptual: `H = 5 Gyr` sigue siendo un enunciado externo redondeado y las fuentes no constituyen de manera automática una sola cronología nativa.

La propagación estadística cuantifica la incertidumbre **después** de establecer la semántica de la trayectoria; no crea la homología de extremos que falta.

## 5.5. Sensibilidad a los representantes nominales de 5 y 6 Gyr

El contraste entre 5 y 6 Gyr es útil porque muestra el efecto de convertir silenciosamente un enunciado público redondeado en un intervalo de frontera preciso.

Con:

```text
A_SS = 4,568 Gyr

C = 10 Gyr
```

resulta:

```text
R_num,5
=
+0,432 Gyr

R_num,6
=
−0,568 Gyr                                           (42)
```

La diferencia es:

```text
R_6 − R_5
=
−1 Gyr                                               (43)
```

Para el anclaje de la propia trayectoria SC08:

```text
A_SC08 = 4,58 Gyr
```

los valores correspondientes son:

```text
R_num,5 = +0,42 Gyr

R_num,6 = −0,58 Gyr                                  (44)
```

El cambio de signo no demuestra que una página pública sea correcta y otra incorrecta. Demuestra que el residual depende directamente de cómo se asigne un enunciado de baja resolución a los extremos formales.

Si los dos enunciados públicos aluden a hitos efectivos distintos, `Γ_end` no está establecido y el residual físico debe conservarse como:

```text
U
```

en lugar de atribuirse a uno u otro valor numérico.

## 5.6. La duración genérica de 1 Gyr de la fase gigante no es transportable

La trayectoria de Schröder y Connon Smith establece, para sus extremos nombrados:

```text
10,00 Gyr  →  final de secuencia principal

12,17 Gyr  →  extremo de la rama de las gigantes rojas
```

y, por tanto:

```text
12,17 − 10,00 = 2,17 Gyr                             (45)
```

Un bloque genérico de 1 Gyr sin extremos homólogos especificados no puede sustituir a ese intervalo.

Esta conclusión tiene una consecuencia directa para la publicación anterior: las extensiones posteriores que empleaban bloques genéricos de fase no se trasladan al resultado cerrado de este trabajo como predicciones cronológicas de precisión.

La parte robusta que se conserva es la disciplina de dominio y origen y la genealogía algebraica del residual de 432 Myr. Las duraciones de fases posteriores requieren extremos específicos de modelo y quedan fuera de la clausura física establecida aquí.

# 6. Interpretación del residual de 432 Myr

## 6.1. Es un residual, no una corrección de la vida solar

Bajo la terna nominal:

```text
(A, H, C)
=
(4,568 ; 5 ; 10) Gyr                                 (46)
```

el residual numérico es exactamente:

```text
R_num
=
10 − 4,568 − 5

=
0,432 Gyr                                             (47)
```

Con el mismo `A` y el mismo `C`, el intervalo necesario para la clausura aritmética es:

```text
H* = 10 − 4,568 = 5,432 Gyr                          (48)
```

por lo que:

```text
R_num
=
5,432 − 5

=
0,432 Gyr                                             (49)
```

Para esta composición híbrida entre registro sistémico y frontera estelar:

```text
ℛ = U
```

mientras no exista una transformación explícita entre dominio y origen.

El residual numérico cuantifica la diferencia entre el intervalo futuro nominal redondeado de 5 Gyr y el intervalo requerido por los dos anclajes seleccionados. No determina de manera independiente la duración física de la secuencia principal solar.

Ésta es la distinción esencial entre **exactitud condicional** y **precisión empírica**.

Una vez declarados tres escalares nominales, su sustracción es exacta en aritmética ordinaria. No existe una regla de cifras significativas que impida conservar el resultado decimal exacto de ese cálculo declarado. Lo que no está permitido es atribuir la resolución decimal de la salida a una entrada que nunca fue comunicada con esa resolución.

Por tanto, 432 Myr es un resultado aritmético exacto de la construcción nominal. La afirmación «la vida del Sol en la secuencia principal es exactamente 432 Myr menor que 10 Gyr» no está respaldada por las mismas entradas.

## 6.2. La duplicación simétrica no aporta evidencia adicional

La construcción anterior expresaba el mismo valor mediante:

```text
5 − 4,568
=
0,432 Gyr                                             (50)
```

y mediante:

```text
10 − 9,568
=
0,432 Gyr                                             (51)
```

La ecuación (25) demuestra que ambas expresiones son la misma identidad cuando:

```text
C = 2H
```

Su coincidencia es una propiedad de conservación bajo la traslación por `H`; no constituye evidencia independiente del valor físico del residual.

La reinterpretación elimina un posible doble cómputo de respaldo sin eliminar la invariancia algebraica útil de la construcción.

## 6.3. Qué demuestra y qué no demuestra el desplazamiento de 2 Myr

Cambiar el registro nominal presente desde:

```text
A_SS = 4,568 Gyr
```

a:

```text
A_⊙ = 4,570 Gyr
```

modifica el residual híbrido desde 432 a 430 Myr.

La diferencia de 2 Myr es obligatoria matemáticamente porque, con `H` y `C` fijos:

```text
ΔR = −ΔA                                              (52)
```

El resultado sirve como control contable: el cálculo no borra de forma silenciosa el cambio de anclaje.

No debe interpretarse, sin embargo, como una separación física medida entre la formación sistémica y el origen del objeto estelar. Las edades radiométricas del Sistema Solar y las edades del objeto solar se establecen mediante métodos y convenciones de origen distintos. Sus incertidumbres y definiciones de suceso deben conservarse.

# 7. De la caracterización de las fuentes al uso cronológico reproducible

El formalismo puede trasladarse a un procedimiento práctico de cronometría estelar sin introducir un nuevo modelo evolutivo.

Para cada magnitud temporal importada deben conservarse, como mínimo:

- objeto o dominio;
- origen;
- suceso de referencia;
- frontera terminal;
- fuente o modelo;
- unidad;
- clase de presentación;
- y, cuando proceda, la transformación de coordenadas aplicada.

Una composición:

```text
A + H → C
```

se evalúa en este orden:

```text
homología de extremos
→ transformación de coordenadas
→ normalización de unidades
→ clase de procedencia
→ residual numérico
→ propagación de incertidumbre o intervalo
→ interpretación física
```

La clasificación es deliberadamente más estricta que la aritmética ordinaria. Una terna escalar completa puede ser calculable y mantener, no obstante, la clausura física en estado no resuelto.

La matriz siguiente resume los casos solares representativos.

| Composición | Estado de extremos | Procedencia | `R_num` | `ℛ` | Interpretación |
|---|---|---|---:|---:|---|
| SC08: `4,58 + 5,42 → 10,00 Gyr` | idénticos | interna | 0 | 0 | Clausura cronológica interna a la precisión tabulada de los hitos del modelo. |
| Presente SC08 + 5 Gyr público nominal → final MS SC08 | frontera insuficientemente especificada | híbrida | +0,42 Gyr | U | Sustitución contrafactual; la expresión pública no es un intervalo exacto al final MS de SC08. |
| SV sistémico 4,568 + 5 nominal → 10 Gyr nominal | falta transformación dominio/origen | híbrida | +0,432 Gyr | U | Genealogía numérica del residual anterior; no es una estimación independiente de vida estelar. |
| SV solar 4,570 + 5 nominal → 10 Gyr nominal | transformación origen/frontera incompleta | híbrida | +0,430 Gyr | U | Misma construcción nominal tras cambiar el registro presente. |
| SV sistémico 4,568 + 6 nominal → 10 Gyr nominal | falta transformación dominio/origen | híbrida | −0,568 Gyr | U | Sensibilidad uno a uno frente al intervalo futuro redondeado. |
| Bloque genérico de 1 Gyr «RGB» → extremo RGB de SC08 | no establecido | mixta | no asignado | U | El intervalo carece de extremos que permitan identificarlo con la evolución final-MS → extremo RGB de SC08. |
| Edad radiométrica `t=0` + intervalo heliosismológico o estelar futuro sin transformación de origen | incompleto | mixta | no asignado | U | La similitud de unidades y valores centrales no crea una trayectoria cronológica común. |

El enfoque es compatible con el análisis estadístico ordinario.

Cuando `A`, `H` y `C` son estimaciones con errores probabilísticos y una matriz de covarianzas, la propagación puede efectuarse mediante los procedimientos correspondientes **después** de haber establecido la homología de extremos.

Cuando las entradas son únicamente enunciados redondeados sin un modelo probabilístico, asignarles una distribución gaussiana incorporaría información que la fuente no proporcionó. En ese caso, los valores nominales o los intervalos deterministas son representaciones más fieles.

Por ello, el presente formalismo precede a la propagación estadística; no la sustituye.

La exigencia tiene relevancia para la agregación automatizada de bibliografía. Las bases astronómicas legibles por máquina combinan cada vez con mayor frecuencia resultados de modelos y valores procedentes de publicaciones heterogéneas. La astronomía ya trata la procedencia como un problema explícito de metadatos: el Modelo de Datos de Procedencia de IVOA [17] normaliza información destinada a reconstruir cómo se obtuvieron los productos astronómicos y a valorar su fiabilidad y aptitud para usos posteriores.

La propuesta presente es mucho más estrecha y no sustituye ese estándar. Añade una observación específica para escalares cronológicos: un esquema que conserve únicamente número y unidad puede preservar la dimensión y, al mismo tiempo, perder el significado de los sucesos que actúan como extremos.

Los tiempos evolutivos destinados a composición deberían conservar, por tanto, identificadores explícitos de origen y frontera, y las transformaciones entre orígenes deberían registrarse en vez de inferirse a partir de etiquetas.

# 8. Relación con el preprint anterior del SV

El preprint anterior [20] forma parte de la procedencia de este estudio y se declara de manera explícita. Introdujo la distinción entre un registro sistémico del Sistema Solar y un registro del objeto solar, empleó un origen formal para cada dominio y exigió controles residuales al añadir intervalos futuros.

También comunicó los valores:

```text
9,568 Gyr

9,570 Gyr

432 Myr
```

que se vuelven a examinar aquí.

El presente trabajo introduce cuatro modificaciones sustantivas.

### Primera

Los dos registros nominales del presente dejan de tratarse como si su mera diferencia numérica estableciera dos relojes físicos independientes. Se conservan como registros declarados y se sitúan junto a la cronometría radiométrica y heliosismológica de la bibliografía. Su objeto y su origen permanecen explícitos.

### Segunda

La cantidad:

```text
9,568 Gyr
=
4,568 + 5
```

se interpreta exclusivamente como un **horizonte cronológico trasladado** bajo el intervalo nominal adoptado de 5 Gyr.

No se presenta como una duración intrínseca de secuencia principal predicha independientemente.

La trayectoria evolutiva utilizada como referente proporciona, por separado, un hito final de secuencia principal a 10,00 Gyr. La diferencia entre ambos valores constituye precisamente el residual híbrido asociado a la sustitución.

### Tercera

El resultado de 432 Myr recibe una genealogía algebraica explícita:

```text
5 − 4,568
=
10 − (4,568 + 5)
```

La igualdad se deriva de la condición especial:

```text
C = 2H
```

y, por tanto, representa un único residual invariante, no dos confirmaciones independientes.

### Cuarta

Las extensiones anteriores mediante un bloque genérico de 1 Gyr para la rama de las gigantes rojas y una convención estrecha posterior a esa fase no se incorporan al resultado físico cerrado de este trabajo.

El contraste con una trayectoria publicada muestra que las duraciones de fase dependen de fronteras nombradas y de definiciones de modelo. Un bloque genérico de una etapa posterior no puede promoverse a cronología de precisión sin esas definiciones.

Con estas modificaciones, el trabajo actual reduce la fuerza de determinadas interpretaciones físicas anteriores y amplía, al mismo tiempo, la aplicabilidad metodológica del criterio.

La aportación deja de formularse como una comparación en la que un sistema obtiene un futuro solar más preciso que una fuente externa. Se formula como un criterio de procedencia y extremos capaz de decidir qué significa un residual cronológico mixto y cuándo su interpretación física permanece no resuelta.

# 9. Discusión

## 9.1. Valor diagnóstico del residual de clausura

La aritmética de:

```text
R_num = C − A − H
```

es elemental. La necesidad de tipar los extremos no lo es cuando se trabaja con registros astronómicos heterogéneos.

Una cadena numérica compleja puede conservar muchas cifras mientras combina cantidades no homólogas. A la inversa, una resta simple puede tener significado científico cuando los sucesos de origen y frontera están definidos sin ambigüedad.

El valor del residual de clausura no reside, por tanto, en la complejidad matemática, sino en su capacidad para revelar errores de procedencia antes de que queden ocultos dentro de cálculos posteriores.

El ejemplo solar separa escalas distintas que no deben confundirse. Entre los representantes centrales de edad presente seleccionados aparecen diferencias de Myr a decenas de Myr. Sustituir un intervalo restante coherente con un modelo por el enunciado redondeado de 5 Gyr genera residuales próximos a 0,42–0,433 Gyr; cambiar ese enunciado desde 5 a 6 Gyr desplaza el residual exactamente en 1 Gyr.

Estas comparaciones no implican que la incertidumbre empírica de la edad solar sea de unos pocos Myr. La incertidumbre heliosismológica comunicada en trabajos anteriores y la sensibilidad asociada al ciclo de actividad estudiada recientemente pueden ser mucho mayores.

La jerarquía obtenida es una jerarquía de **sustituciones nominales declaradas**, no una jerarquía universal de incertidumbres astrofísicas.

La conclusión es más precisa que afirmar que una fuente «redondea» mientras otra «formaliza». El redondeo no constituye por sí mismo un error.

El error aparece cuando a un enunciado redondeado se le atribuye una clase de precisión o una identidad de frontera para la cual no fue formulado.

Un enunciado público de 5 Gyr puede ser plenamente adecuado como comunicación científica general y, al mismo tiempo, resultar inadmisible como intervalo de alta resolución de un modelo concreto.

## 9.2. Dominio y origen son problemas diferentes

La distinción entre cronometría del Sistema Solar y edad estelar del Sol requiere atención específica.

Un `t = 0` del Sistema Solar definido por formación de CAI o por una relación radionucleídica canónica es una coordenada de formación del sistema.

Una edad solar heliosismológica es una coordenada estelar inferida.

Una trayectoria evolutiva puede utilizar ZAMS como origen cero.

Estas elecciones afectan tanto al objeto o dominio físico como al suceso de origen. Tratarlas como una sola cuestión puede ocultar la transformación necesaria entre ambos.

La ecuación de invariancia por cambio de origen proporciona un control sencillo cuando el cambio de origen es conocido: todas las edades que actúan como coordenadas y comparten el origen deben desplazarse conjuntamente, mientras un intervalo transcurrido no cambia.

Si el desfase físico entre dos orígenes es desconocido o depende del modelo, la transformación no puede obtenerse mediante notación. Su estado correcto es:

```text
U
```

y no cero.

Esta observación también limita la interpretación de:

```text
A_⊙ − A_SS = 2 Myr
```

en el preprint anterior. La diferencia se conserva exactamente en cualquier cálculo que mantenga `H` y `C` fijos, pero no identifica por sí sola la separación física entre los sucesos de origen subyacentes.

## 9.3. La semántica de las fronteras es tan importante como la precisión de la edad

La bibliografía sobre el futuro solar proporciona una segunda lección.

Términos como:

- TAMS;
- final de secuencia principal;
- comienzo de la fase subgigante;
- base de la rama de las gigantes rojas;
- gigante roja establecida;
- extremo de la rama de las gigantes rojas;
- ignición central del helio;
- extremo de la rama asintótica de las gigantes;

designan sucesos físicos diferentes.

Un intervalo entre fases sólo tiene significado cuando se nombran ambos extremos.

Por ello, el bloque genérico de 1 Gyr del preprint anterior se elimina del resultado cerrado en lugar de limitarse a asignarle una incertidumbre mayor. Si sus extremos no son homólogos a los de un intervalo de un modelo publicado, el problema no es el tamaño de la barra de error, sino el **tipo de magnitud**.

En la notación de la ecuación (16), el residual físico permanece en:

```text
U
```

hasta que se aporte la transformación de fronteras.

El mismo principio se aplica fuera del Sol. Las rejillas de modelos estelares pueden utilizar definiciones internas distintas para los hitos evolutivos, especialmente cuando intervienen interpolación, umbrales de abundancia central o criterios en el diagrama de Hertzsprung–Russell.

La coordinación de fases no es, por tanto, una sutileza terminológica, sino un requisito computacional.

## 9.4. Limitaciones

Este trabajo presenta límites deliberados.

No calcula una nueva trayectoria evolutiva solar, no recalibra un modelo del Sol y no infiere una nueva edad empírica.

No decide entre distintas elecciones de física de entrada en la modelización solar.

No afirma que la cronología de Schröder y Connon Smith sea única o universalmente correcta. Esa trayectoria se utiliza porque reúne varios hitos relevantes dentro de un único cálculo internamente coherente. Otras trayectorias modernas pueden y deben analizarse mediante las mismas reglas de tipado.

El formalismo residual tampoco sustituye a la inferencia estadística. Cuando existen distribuciones posteriores completas y covarianzas, deben propagarse una vez establecida la compatibilidad.

A la inversa, el formalismo no asigna distribuciones probabilísticas inventadas a expresiones cualitativas como «aproximadamente». Se mantiene la diferencia entre incertidumbre cuantificada y semántica insuficientemente especificada.

Finalmente, el tipado de procedencia no puede crear una transformación física ausente.

Si un marcador de formación del Sistema Solar debe trasladarse a una edad estelar basada en ZAMS, el desfase correspondiente tiene que proceder de un modelo físico o cronológico explícito. El formalismo puede registrar y auditar esa transformación; no puede deducirla de la proximidad numérica.

# 10. Conclusiones

Se ha formulado un criterio de clausura con procedencia tipificada para la cronometría evolutiva solar y se ha aplicado a anclajes radiométricos del Sistema Solar, una edad heliosismológica del Sol, una trayectoria evolutiva publicada y enunciados públicos redondeados sobre el futuro solar.

Los resultados principales son los siguientes.

1. Una composición cronológica:

```text
C = A + H
```

sólo posee interpretación física cuando el objeto o dominio, el origen, el suceso de referencia y la frontera terminal son idénticos o están relacionados mediante una transformación explícita. La igualdad de unidades es necesaria, pero no suficiente.

2. Deben distinguirse la sustracción numérica y la clausura física. Cuando no puede establecerse la compatibilidad de extremos, el residual escalar puede seguir siendo calculable, pero su estatuto físico permanece no resuelto.

3. En la trayectoria internamente coherente de Schröder y Connon Smith:

```text
4,58 + 5,42 = 10,00 Gyr
```

cierra aritméticamente a la precisión tabulada. Respecto de esa referencia, el residual nominal previo de 0,432 Gyr se descompone exactamente como:

```text
0,432
=
0,420 + 0,012 Gyr
```

El primer término se genera al sustituir 5,42 Gyr por el intervalo redondeado de 5 Gyr. El segundo se genera al sustituir la coordenada de 4,58 Gyr de la trayectoria por el registro sistémico de 4,568 Gyr.

Es una descomposición aritmética de procedencia, no una descomposición de efectos físicos independientes. Como las coordenadas sistémica y estelar no disponen de una transformación de origen común demostrada, la clausura física permanece en `U`. El valor de 0,432 Gyr no es una nueva corrección física de la vida solar.

4. Las dos expresiones:

```text
5 − 4,568
```

y:

```text
10 − (4,568 + 5)
```

son algebraicamente idénticas bajo la condición `C = 2H`. Su coincidencia proporciona una sola identidad de conservación, no dos mediciones independientes.

5. Entre los representantes centrales de edad presente seleccionados, los valores nominales de `R_5` abarcan 19,70 Myr. Sustituir el intervalo futuro redondeado de 5 Gyr por 6 Gyr desplaza todos los residuales numéricos en −1 Gyr e invierte su signo. Es un resultado de sensibilidad para los representantes elegidos, no una afirmación de que las incertidumbres de la edad estelar sean despreciables.

6. Una duración genérica de 1 Gyr atribuida a la rama de las gigantes rojas no puede trasladarse a un intervalo definido por un modelo entre final de secuencia principal y extremo de la rama de las gigantes rojas. Los hitos de la trayectoria utilizada proporcionan aproximadamente 2,17 Gyr entre esas fronteras. Las duraciones de fase deben permanecer asociadas a extremos nombrados y a la procedencia del modelo.

El resultado general es metodológico.

La aritmética exacta puede coexistir con entradas redondeadas, heterogéneas o de baja resolución, pero la salida hereda las limitaciones físicas de esas entradas.

Conservar la procedencia y la semántica de los extremos impide que la precisión nominal se transforme, por mera operación matemática, en una nueva determinación astronómica.

El caso solar constituye un banco reproducible y compacto para aplicar esta disciplina a la cronometría estelar en general.

# Agradecimientos

El autor agradece a los responsables de las bases de datos científicas públicas y de los archivos de revistas utilizados para verificar la procedencia bibliográfica y numérica de las magnitudes empleadas.

# Disponibilidad de datos

No se generaron nuevos datos observacionales. Todas las entradas numéricas empleadas en el contraste proceden de las publicaciones citadas o del preprint anterior identificado expresamente. Los cálculos necesarios para reproducir los resultados numéricos y las matrices de admisibilidad se encuentran en las ecuaciones y en los apéndices de este trabajo.

# Divulgación previa

El preprint español *Contraste de precisión etaria solar SV–NASA* contiene una formulación anterior y materialmente diferente de una parte del ejemplo solar. El presente trabajo constituye una reconstrucción: introduce el formalismo de compatibilidad con procedencia tipificada, utiliza una trayectoria evolutiva publicada como referente, deriva de manera explícita la genealogía del residual de 432 Myr, elimina extrapolaciones de fase no sustentadas por extremos homólogos y restringe la interpretación física del resultado anterior.

El antecedente permanece disponible mediante DOI `10.21428/39829d0b.22c326bf`.

# Declaración sobre el uso de inteligencia artificial generativa y tecnologías asistidas por IA

Durante la preparación del manuscrito internacional en lengua inglesa y de su fuente LaTeX, el autor utilizó ChatGPT de OpenAI (GPT-5.6 Sol), bajo su supervisión, para tareas de redacción y mejora de claridad en inglés, organización estructural, comprobaciones de coherencia interna y asistencia de formato en LaTeX.

La herramienta no fue utilizada como fuente científica ni para generar datos observacionales, simulaciones, figuras o datos visuales.

El autor verificó de manera independiente las fuentes citadas, las ecuaciones, los cálculos numéricos, las interpretaciones científicas y el texto final, y asume plena responsabilidad sobre el contenido.

# Apéndice A. Reproducibilidad de los cálculos residuales nominales

Los cálculos de sensibilidad utilizan:

```text
H* = 10 − A

R_5 = 10 − A − 5

R_6 = 10 − A − 6                                     (A.1)
```

con todas las magnitudes expresadas en Gyr.

Para los valores centrales empleados:

```text
A = 4,56800
H* = 5,43200
R_5 = 0,43200
R_6 = −0,56800
```

```text
A = 4,57000
H* = 5,43000
R_5 = 0,43000
R_6 = −0,57000
```

```text
A = 4,56820
H* = 5,43180
R_5 = 0,43180
R_6 = −0,56820
```

```text
A = 4,56730
H* = 5,43270
R_5 = 0,43270
R_6 = −0,56730
```

```text
A = 4,56842
H* = 5,43158
R_5 = 0,43158
R_6 = −0,56842
```

```text
A = 4,57000
H* = 5,43000
R_5 = 0,43000
R_6 = −0,57000
```

```text
A = 4,56900
H* = 5,43100
R_5 = 0,43100
R_6 = −0,56900
```

```text
A = 4,58700
H* = 5,41300
R_5 = 0,41300
R_6 = −0,58700
```

```text
A = 4,58000
H* = 5,42000
R_5 = 0,42000
R_6 = −0,58000
```

La amplitud de `R_5` entre el menor y el mayor de los valores centrales anteriores es:

```text
0,43270 − 0,41300
=
0,01970 Gyr
=
19,70 Myr                                             (A.2)
```

Cambiar únicamente el intervalo futuro nominal desde 5 a 6 Gyr produce:

```text
R_6 − R_5
=
−1 Gyr                                                (A.3)
```

para todas las filas, como exige la sensibilidad lineal de la ecuación (22).

# Apéndice B. Esquema mínimo de metadatos para registros cronológicos

Para una agregación reproducible, un valor temporal escalar debería acompañarse de un registro de la forma:

```text
𝕋 = {x, D, O, E₁, E₂, S, u, π, Φ, q}                (B.1)
```

donde:

- `x` es el escalar comunicado;
- `D`, el objeto físico o dominio;
- `O`, la convención de origen;
- `E₁` y `E₂`, los extremos del intervalo;
- `S`, la procedencia de la fuente o del modelo;
- `u`, la unidad;
- `π`, la clase de precisión o presentación;
- `Φ`, la identidad o transformación explícita aplicada antes de una composición entre coordenadas;
- `q`, el estado de admisibilidad para la composición prevista.

El campo de transformación debe conservar procedencia suficiente para reconstruir cualquier desfase o correspondencia. No basta con registrar que «existe una transformación».

En el presente trabajo se utilizan cualitativamente los estados:

```text
interna

híbrida

U = clausura física no resuelta
```

Una implementación en base de datos puede formalizar esos estados con mayor detalle siempre que no elimine las definiciones de los extremos ni las transformaciones aplicadas.

# Referencias

[1] Soderblom, D. R. (2010). *Ages of stars*. Annual Review of Astronomy and Astrophysics, 48, 581–629. DOI `10.1146/annurev-astro-081309-130806`.

[2] Lebreton, Y., Goupil, M. J. y Montalbán, J. (2014). EAS Publications Series, 65, 99. DOI `10.1051/eas/1465004`.

[3] Bonanno, A., Schlattl, H. y Paternò, L. (2002). Astronomy & Astrophysics, 390, 1115. DOI `10.1051/0004-6361:20020749`.

[4] Bonanno, A. y Fröhlich, H.-E. (2015). Astronomy & Astrophysics, 580, A130. DOI `10.1051/0004-6361/201526419`.

[5] Bétrisey, J., Farnir, M., Breton, S. N. et al. (2024). Astronomy & Astrophysics, 688, L17. DOI `10.1051/0004-6361/202451365`.

[6] Vinyoles, N., Serenelli, A. M., Villante, F. L. et al. (2017). The Astrophysical Journal, 835, 202. DOI `10.3847/1538-4357/835/2/202`.

[7] Christensen-Dalsgaard, J. (2021). Living Reviews in Solar Physics, 18, 2. DOI `10.1007/s41116-020-00028-3`.

[8] Bouvier, A. y Wadhwa, M. (2010). Nature Geoscience, 3, 637. DOI `10.1038/ngeo941`.

[9] Connelly, J. N., Bizzarro, M., Krot, A. N. et al. (2012). Science, 338, 651. DOI `10.1126/science.1226919`.

[10] Desch, S. J., Dunlap, D. R., Dunham, E. T., Williams, C. D. y Mane, P. (2023). Icarus, 402, 115607. DOI `10.1016/j.icarus.2023.115607`.

[11] Amelin, Y. y Yin, Q.-Z. (2025). National Science Review, 12, nwaf281. DOI `10.1093/nsr/nwaf281`.

[12] Sackmann, I.-J., Boothroyd, A. I. y Kraemer, K. E. (1993). The Astrophysical Journal, 418, 457. DOI `10.1086/173407`.

[13] Schröder, K.-P. y Connon Smith, R. (2008). Monthly Notices of the Royal Astronomical Society, 386, 155. DOI `10.1111/j.1365-2966.2008.13022.x`.

[14] Veras, D. (2016). Monthly Notices of the Royal Astronomical Society, 463, 2958. DOI `10.1093/mnras/stw2170`.

[15] Dotter, A. (2016). The Astrophysical Journal Supplement Series, 222, 8. DOI `10.3847/0067-0049/222/1/8`.

[16] Prša, A., Harmanec, P., Torres, G. et al. (2016). The Astronomical Journal, 152, 41. DOI `10.3847/0004-6256/152/2/41`.

[17] Servillat, M., Riebe, K., Boisson, C. et al. (2020). *IVOA Provenance Data Model*, versión 1.0. International Virtual Observatory Alliance.

[18] NASA (2024). *Aging Into Gianthood*. NASA Science. Actualización: 29 de octubre de 2024; consulta: 7 de agosto de 2026.

[19] NASA (2024). *Stars*. NASA Science: Exoplanets. Actualización: 11 de diciembre de 2024; consulta: 7 de agosto de 2026.

[20] Lloret Egea, J. A. (2026). *Contraste de precisión etaria solar SV–NASA*. Preprint no revisado por pares. DOI `10.21428/39829d0b.22c326bf`.
