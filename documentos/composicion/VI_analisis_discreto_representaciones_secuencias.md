# Álgebra de composición intercelular del marco SV

## VI. Análisis discreto, representaciones y herramientas de secuencias del sistema

### Herramientas matemáticas propias del SV en el dominio discreto

**Autor:** Juan Antonio Lloret Egea

**ORCID:** 0000-0002-6634-3351

**Versión:** 1

**Lugar y fecha:** Madrid, 11/03/2026

**Estado:** Documento doctrinal publicado

CC BY-NC-ND 4.0 · ISSN 2695-6411

---

## Resumen

Este documento dota al Sistema Vectorial SV de herramientas matemáticas propias para analizar trayectorias, estudiar la estructura de la composición y comparar configuraciones, sin abandonar el dominio discreto que el sistema habita por diseño.

El documento introduce cuatro bloques formales: el análisis discreto de trayectorias mediante operadores de diferencia finita y criterios de estabilización; las funciones generatrices y series formales del espacio combinatorio del SV; la transformada Z aplicada a secuencias extraídas de trayectorias; y el álgebra lineal del grafo de composición. A estos cuatro pilares se añade una capa de representaciones y cambios de codificación con sus invariantes.

Sobre esta base se establecen siete proposiciones que permiten hablar formalmente de estabilización, oscilación, estructura combinatoria, influencia estructural y equivalencia entre representaciones del sistema.

---

## 1. Objeto y alcance

### 1.1. Tesis central

El SV admite un análisis matemático propio en el dominio discreto. Las trayectorias son secuencias de frames. Las arquitecturas son grafos dirigidos. Los espacios combinatorios son finitos y enumerables. Estas estructuras tienen una matemática natural que no es el cálculo infinitesimal clásico, sino el análisis discreto, la combinatoria y el álgebra lineal sobre grafos.

El Documento VI no importa herramientas del continuo al discreto. Extrae las herramientas que el discreto ya tiene y las aplica al SV.

### 1.2. Qué hace este documento

Dota al SV de cuatro bloques de herramientas formales:

1. **Análisis discreto de trayectorias** — operadores de diferencia finita, estabilización, oscilación, ciclos, función de mérito.
2. **Funciones generatrices y series formales** — codificación del espacio combinatorio, conteo de configuraciones, comparación entre familias de células.
3. **Transformada Z del SV** — análisis de secuencias extraídas de trayectorias en dominio transformado.
4. **Álgebra lineal del grafo de composición** — matrices de adyacencia, operadores de propagación, profundidad efectiva, estructura de influencia.

A estos cuatro pilares se añade una capa transversal de **representaciones y cambios de codificación** con invariantes preservados.

### 1.3. Qué no hace este documento

Este documento no:

- introduce derivadas ni integrales en sentido clásico (continuo);
- introduce variable compleja ni teoría de residuos;
- introduce transformada de Laplace (continua);
- introduce integrales múltiples;
- introduce estadística, minería de datos ni aprendizaje opaco;
- formaliza humanoides ni autonomía fuerte.

### 1.4. Posición en la serie

- Los **Fundamentos** fijaron la célula y Σ.
- El **Documento I** fijó la transmisión intercelular.
- El **Documento II** fijó la gramática de composición.
- El **Documento III** fijó sucesos, frame y trayectoria.
- El **Documento IV** fijó la entrada del mundo al sistema.
- El **Documento V** fijó la especialización, la consulta y el cierre funcional.
- El **Documento VI** dota al sistema de herramientas de análisis en su propio dominio.

Los Documentos I–V construyen el sistema y dicen cómo usarlo. El Documento VI dice cómo estudiarlo.

---

## 2. Subordinación doctrinal y herencia de la serie

Este documento es doctrina derivada de segundo nivel. La autoridad normativa suprema reside en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. En caso de discrepancia, prevalecen los *Fundamentos*.

### Lo que este documento hereda y necesita

El Documento VI opera sobre objetos ya definidos en la serie:

- De los **Fundamentos:** Σ = {0, 1, U}, célula SV(n, b), restricción n = b², T(n) = ⌊7n/9⌋, χᵢ, ℱ_SV. El espacio combinatorio 3ⁿ por célula.
- Del **Documento I:** grafo dirigido de composición en serie, conector σ_{k,φ}, propagación por puente.
- Del **Documento II:** gramática de patrones, relación semántica R(𝒜), arquitectura 𝒜 como DAG de células acopladas.
- Del **Documento III:** trayectoria T = (S₁, ν₁, S₂, …, Sₙ), frame Sₙ, dato νₙ, relación δ_Γ. La trayectoria es la secuencia sobre la que operan las herramientas del Documento VI.
- Del **Documento IV:** interfaz ℐ(𝒜), máscara E(C), U silenciosa U_s. La cobertura de la interfaz condiciona qué se puede analizar.
- Del **Documento V:** invariantes Inv_SV, dominio 𝔇, agente A_𝔇. Las herramientas del Documento VI respetan los invariantes.

---

## 3. Tabla de notación

### Símbolos heredados

Todos los de Fundamentos y Documentos I–V permanecen vigentes.

### Símbolos introducidos en este documento

| Símbolo | Significado | Estatuto |
|---------|------------|----------|
| Δf(k) | Operador de diferencia finita: f(k+1) − f(k) | Definición |
| n₀(k), n₁(k), nU(k) | Secuencias de conteo de 0, 1, U en el frame Sₖ | Primitiva de T |
| κ(k) | Secuencia de clasificación codificada a lo largo de T | Primitiva de T |
| Γ(k) | Secuencia de criticidad a lo largo de T | Derivada de T |
| 𝒵{f} | Transformada Z de una secuencia f(k) | Definición |
| G_C(x, y, z) | Función generatriz del espacio combinatorio de la célula C | Definición |
| A_𝒜 | Matriz de adyacencia del grafo de composición 𝒜 | Definición |
| P_𝒜 | Operador de propagación sobre el grafo 𝒜 | Definición |
| d_eff(𝒜) | Profundidad efectiva de cascada de la arquitectura | Definición |
| ρ(C, 𝒜) | Influencia estructural de la célula C en la arquitectura | Definición |
| [v]_B | Representación del vector v en la codificación B | Definición |

---

## 4. Análisis discreto de trayectorias

### 4.1. Principio

La trayectoria T = (S₁, ν₁, S₂, …, Sₙ) es una secuencia de frames. Cada frame contiene vectores ternarios, clasificaciones, criticidades y metadatos. De T se pueden extraer secuencias numéricas que son analizables con herramientas discretas estándar.

### 4.2. Secuencias canónicas del sistema

Antes de aplicar cualquier herramienta de análisis, el Documento VI fija qué secuencias numéricas se extraen canónicamente de una trayectoria T. Todas las herramientas posteriores (diferencia finita, transformada Z, funciones de mérito) operan sobre estas secuencias, no sobre frames completos ni sobre objetos no numéricos.

**Definición 1.** Sea T una trayectoria de longitud N. Para cada célula C de la arquitectura, se definen las siguientes **secuencias primitivas** sobre k = 1, …, N:

- n₀(k): número de parámetros con valor 0 en el frame Sₖ.
- n₁(k): número de parámetros con valor 1 en el frame Sₖ.
- nU(k): número de parámetros con valor U en el frame Sₖ.
- κ(k): clasificación codificada (0 = APTO, 1 = NO_APTO, U = INDETERMINADO).

Y las siguientes **secuencias derivadas:**

- Γ(k): criticidad de la célula en el frame Sₖ (derivada de los conteos; definida cuando κ(k) = U).
- Δn₀(k), Δn₁(k), ΔnU(k): diferencias finitas de los conteos (derivadas de las primitivas).

Las secuencias primitivas se leen directamente del frame. Las derivadas se calculan a partir de las primitivas.

Para un sistema multicelular, cada célula produce su propia familia de secuencias. El sistema completo produce una familia indexada por (C, secuencia).

### 4.3. Operador de diferencia finita

**Definición 2.** Sea f(k) una secuencia numérica extraída de T. El **operador de diferencia finita** es:

> Δf(k) = f(k+1) − f(k)

para k = 1, …, N−1.

La diferencia finita mide el cambio entre frames consecutivos. Es el análogo discreto de la derivada, nativo del SV.

### 4.4. Diferencias de conteo

Las diferencias de las secuencias de conteo satisfacen una restricción estructural:

> Δn₀(k) + Δn₁(k) + ΔnU(k) = 0

porque n₀(k) + n₁(k) + nU(k) = n para todo k. La suma de parámetros no cambia. Lo que cambia es su distribución entre 0, 1 y U.

**Proposición 1 — Conservación del conteo total.** Para toda célula SV(n, b) y todo par de frames consecutivos de su trayectoria, la suma de las diferencias de conteo es cero.

### 4.5. Estabilización

**Definición 3.** Una secuencia f(k) extraída de T se dice **estabilizada a partir de K** si:

> Δf(k) = 0 para todo k ≥ K

Una trayectoria se dice **estabilizada** si todas sus secuencias de conteo y clasificación están estabilizadas.

### 4.6. Oscilación

**Definición 4.** Una secuencia f(k) **oscila** si Δf(k) cambia de signo al menos dos veces. La **amplitud de oscilación** es max(f) − min(f) sobre la ventana observada.

Una trayectoria que oscila no se estabiliza. El sistema va y viene entre estados. Esto es información diagnóstica real: un paciente cuyo Γ oscila no alcanza estabilización eventual.

### 4.7. Ciclos

**Definición 5.** Una trayectoria T tiene un **ciclo de período p** a partir de K si:

> Sₖ₊ₚ = Sₖ para todo k ≥ K (igualdad de frames como evaluaciones completas)

Un ciclo no viola la inmutabilidad de T (los frames no se reescriben; el sistema repite estados). Pero indica que la dinámica de sucesos ha entrado en un bucle.

**Proposición 2 — Finitud del espacio de estados y existencia de ciclos.** En un sistema con espacio de estados finito (3ⁿ configuraciones por célula), toda trayectoria suficientemente larga o bien se estabiliza o bien entra en un ciclo. No hay tercera opción en un espacio finito sin fuente infinita de sucesos.

### 4.8. Taxonomía del comportamiento asintótico discreto

El término «convergencia» no se usa en este documento como palabra genérica. Se sustituye por una taxonomía explícita de comportamientos asintóticos de las secuencias canónicas del SV:

**Estabilización eventual.** Δf(k) = 0 para todo k ≥ K. La secuencia deja de cambiar. Caso más favorable.

**Fijación de clase.** κ(k) = constante para todo k ≥ K. La clasificación se fija aunque los conteos puedan seguir variando dentro de la misma clase. Es más débil que la estabilización completa.

**Periodicidad.** Existe p ≥ 1 tal que f(k+p) = f(k) para todo k ≥ K. La secuencia repite un patrón. El ciclo de frames (Definición 5) es un caso particular donde todo el frame se repite.

**Oscilación.** Δf(k) cambia de signo repetidamente sin periodicidad regular. La secuencia no se estabiliza ni cicla; va y viene de forma irregular.

**Divergencia discreta.** n₁(k) crece monótonamente o nU(k) crece monótonamente a lo largo de T. El sistema se degrada sin recuperación observable. En un espacio finito, la divergencia pura es imposible (eventualmente se satura), pero puede mantenerse hasta el límite del espacio.

Cada secuencia canónica de una célula puede exhibir un comportamiento distinto: los conteos pueden estabilizarse mientras la criticidad oscila. El comportamiento de la trayectoria completa se describe como la composición de los comportamientos de todas sus secuencias canónicas.

### 4.9. Función de mérito de trayectoria

**Definición 6.** Una **función de mérito** de trayectoria es una función:

> μ : T → ℝ

que asigna un valor numérico a una trayectoria completa. La función de mérito es dependiente del dominio (Π_C del dominio 𝔇 del Documento V la condiciona).

Candidatas naturales:

- μ₁(T) = nU(N) — cantidad de U residuales en el último frame (menor es mejor).
- μ₂(T) = Σₖ nU(k) — acumulado de U a lo largo de toda la trayectoria (menor es mejor).
- μ₃(T) = N_estab — frame en que se estabiliza (menor es mejor, si se estabiliza).

**Proposición 3 — Dependencia de dominio de la función de mérito.** No existe una función de mérito universal independiente del dominio. La función de mérito μ depende de Π_C, Π_U y de la semántica del dominio especializado 𝔇. Lo que es «bueno» en inmunología (resolver U prioritarias de Γ) puede no ser «bueno» en neumología (cerrar estadificación por compuerta). El Documento VI no propone ninguna μ como canónica; establece la estructura formal y deja la elección al dominio.

---

## 5. Funciones generatrices y series formales

### 5.1. Principio

El espacio combinatorio de una célula SV(n, b) tiene 3ⁿ configuraciones posibles. Ese espacio es finito y enumerable. Las funciones generatrices codifican su estructura en un polinomio formal.

### 5.2. Alcance inicial

Este documento aplica funciones generatrices exclusivamente al espacio combinatorio de una célula SV(n, b) y a las distribuciones de conteo (n₀, n₁, nU) derivadas de ese espacio. La extensión a arquitecturas multicelulares completas o a familias de trayectorias queda como línea futura: solo se abrirá cuando el objeto codificado por la generatriz esté formalmente definido.

### 5.3. Función generatriz de la célula

**Definición 7.** Sea C una célula SV(n, b). La **función generatriz** de C es:

> G_C(x, y, z) = Σ_{v ∈ {0,1,U}ⁿ} x^{n₀(v)} · y^{n₁(v)} · z^{nU(v)}

donde n₀(v), n₁(v), nU(v) son los conteos del vector v.

Esta función es un polinomio homogéneo de grado n en tres variables. Cada monomio codifica una clase de configuraciones con los mismos conteos.

### 5.4. Evaluación sobre el generatriz

Para x = y = z = 1: G_C(1,1,1) = 3ⁿ (número total de configuraciones).

Para z = 0: G_C(x, y, 0) solo cuenta configuraciones sin U (vectores completamente determinados).

Para y = 0, z = 0: G_C(x, 0, 0) = xⁿ (la única configuración todo-cero).

### 5.5. Conteo de configuraciones por clase

El número de vectores con exactamente a ceros, b unos y c indeterminaciones (a + b + c = n) es:

> C(n; a, b, c) = n! / (a! · b! · c!)

que es el coeficiente multinomial estándar. Este conteo es exacto y no requiere aproximación.

**Proposición 4 — Descomposición multinomial del espacio SV.** El espacio combinatorio de SV(n, b) se descompone en clases de equivalencia por conteo (a, b, c), cada una con C(n; a, b, c) configuraciones. La clasificación T(n) = ⌊7n/9⌋ particiona estas clases en APTO, NO_APTO e INDETERMINADO.

### 5.6. Comparación entre familias de células

La función generatriz permite comparar formalmente el crecimiento combinatorio entre SV(9,3), SV(16,4), SV(25,5), etc. El grado del polinomio crece con n; la proporción de configuraciones APTAS versus INDETERMINADAS cambia conforme n escala.

---

## 6. Transformada Z del SV

### 6.1. Principio

La transformada Z es la herramienta natural para analizar secuencias discretas en un dominio transformado. Es el análogo discreto de la transformada de Laplace. Opera sobre secuencias, que es exactamente lo que el SV produce.

### 6.2. Secuencias transformables

La transformada Z opera exclusivamente sobre las **secuencias canónicas** definidas en §4.2. Las secuencias primitivas (n₀(k), n₁(k), nU(k), κ(k)) y las derivadas (Γ(k), diferencias finitas) son numéricas y por tanto transformables.

**Condición:** la Z solo se aplica a secuencias numéricas extraídas canónicamente de la trayectoria T. No se aplica a frames completos, a objetos observacionales ni a estructuras no numéricas del sistema.

### 6.3. Definición

**Definición 8.** Sea f(k) una secuencia numérica de longitud N extraída de T. La **transformada Z** de f es:

> 𝒵{f}(z) = Σₖ₌₁ᴺ f(k) · z⁻ᵏ

donde z es una variable compleja formal.

### 6.4. Propiedades relevantes para el SV

**Linealidad.** 𝒵{αf + βg} = α𝒵{f} + β𝒵{g}. Las combinaciones lineales de secuencias de conteo se transforman linealmente.

**Desplazamiento.** 𝒵{f(k+1)}(z) = z · 𝒵{f}(z) − z · f(1). El desplazamiento temporal (avance de un frame) se traduce en multiplicación por z.

**Relación con la diferencia finita.** 𝒵{Δf}(z) = (z−1) · 𝒵{f}(z) − z · f(1) + f(1). La diferencia finita en el dominio temporal se convierte en multiplicación por (z−1) en el dominio Z.

**Nota analítica sobre estabilización.** En la definición adoptada por este documento, la transformada Z de una trayectoria finita de longitud N es un polinomio en z⁻¹, no una función racional con polos intrínsecos. Por tanto, la caracterización clásica de estabilidad mediante polos dentro del círculo unitario (propia de sistemas discretos infinitos o de funciones de transferencia racionales) no se aplica directamente. La transformada Z del SV es una herramienta descriptiva: codifica la estructura de la secuencia finita y simplifica operaciones como la diferencia y la acumulación, pero no produce por sí sola un criterio de estabilización tipo «si y solo si». La estabilización se determina en el dominio temporal (§4.5) mediante Δf(k) = 0 para k ≥ K. La Z la describe; no la demuestra.

### 6.5. Interpretación

La transformada Z no predice. Codifica la estructura de la secuencia en un dominio donde ciertas operaciones (diferencia, acumulación, convolución) se simplifican. Para el SV, su utilidad principal es analítica: caracterizar formalmente si una trayectoria se estabiliza, oscila, cicla o diverge (taxonomía de §4.8).

---

## 7. Álgebra lineal del grafo de composición

### 7.1. Principio

La arquitectura 𝒜 del Documento II es un DAG (grafo dirigido acíclico) de células acopladas. Los grafos dirigidos tienen estructura matricial analizable con álgebra lineal exacta.

### 7.2. Matriz de adyacencia

**Definición 9.** Sea 𝒜 una arquitectura con m células C₁, …, Cₘ. La **matriz de adyacencia** A_𝒜 es la matriz m × m donde:

> (A_𝒜)ᵢⱼ = 1 si existe un conector de Cⱼ a Cᵢ (la salida de Cⱼ alimenta a Cᵢ)
> (A_𝒜)ᵢⱼ = 0 en otro caso

La convención es: las columnas emiten, las filas reciben.

### 7.3. Operador de propagación

**Definición 10.** El **operador de propagación** P_𝒜 es la clausura transitiva de A_𝒜:

> P_𝒜 = A_𝒜 + A_𝒜² + A_𝒜³ + …

En un DAG, esta suma es finita (no hay ciclos, luego Aᵏ = 0 para k > profundidad del grafo). La entrada (P_𝒜)ᵢⱼ indica cuántos caminos dirigidos existen de Cⱼ a Cᵢ de cualquier longitud.

### 7.4. Profundidad efectiva

**Definición 11.** La **profundidad efectiva** de la arquitectura es:

> d_eff(𝒜) = min{ k : A_𝒜ᵏ⁺¹ = 0 }

Es la longitud máxima de cualquier camino dirigido en el DAG. Determina cuántos pasos de propagación puede recorrer un cambio.

**Proposición 5 — Acotación de cascada por profundidad efectiva.** Un cambio en una célula fuente se propaga a lo sumo d_eff(𝒜) pasos antes de agotar su efecto. Esto refuerza y cuantifica la Proposición 3 del Documento III (acotación de cascada en régimen simple).

### 7.5. Influencia estructural

**Definición 12.** La **influencia estructural** de una célula Cⱼ en la arquitectura es:

> ρ(Cⱼ, 𝒜) = Σᵢ (P_𝒜)ᵢⱼ

Es la suma de la columna j de P_𝒜: el número total de caminos que parten de Cⱼ y llegan a cualquier otra célula, de cualquier longitud.

Una célula con influencia alta es una célula cuyas variaciones se propagan a muchas otras. Una célula con influencia cero es una célula hoja sin sucesores.

**Proposición 6 — Influencia nula de las hojas.** En un DAG, toda célula sin sucesores tiene ρ = 0. Su estado no se propaga a ninguna otra célula. Esto es una propiedad estructural del grafo, no del estado.

### 7.6. Horizonte: invariantes espectrales

Los autovalores de A_𝒜 o de matrices derivadas (como la laplaciana del grafo) podrían revelar propiedades de la estructura de composición: número de componentes conexas, simetría, regularidad. Sin embargo, esta línea requiere fijar primero con precisión qué operador representa qué fenómeno del SV. Queda como exploración subordinada a los invariantes y operadores ya definidos en §7.2–7.5, no como centro del bloque.

---

## 8. Representaciones y cambios de codificación

### 8.1. Principio

El vector ternario v ∈ Σⁿ es la representación canónica del SV. Pero en diferentes contextos (implementación WASM, visualización, transmisión) el vector puede codificarse de otras formas. Lo esencial es que la representación preserve la información y que los invariantes del SV se mantengan.

### 8.2. Codificaciones principales

**Ternaria canónica.** v = (v₁, …, vₙ) con vᵢ ∈ {0, 1, U}. Es la representación nativa.

**Binaria.** Cada valor ternario se codifica en dos bits: 0 → 00, 1 → 01, U → 10. El vector ocupa 2n bits. Esta es la codificación usada en la implementación Rust/WASM.

**Real.** Se asigna un valor numérico a cada estado: 0 → 0.0, 1 → 1.0, U → 0.5 (u otro valor convencional). Útil para visualización polar y cálculos de mérito.

**Codificación posicional.** El vector se interpreta como un número en base 3: Σᵢ vᵢ · 3ⁱ⁻¹ (con U = 2). Produce un entero único en [0, 3ⁿ − 1]. Útil para indexación y enumeración.

### 8.3. Invariantes bajo cambio de codificación

**Proposición 7 — Preservación de clasificación bajo codificación inyectiva.** Sea φ : Σⁿ → B una codificación inyectiva (sin pérdida de información). Entonces la clasificación T(n), la criticidad Γ y los conteos n₀, n₁, nU son recuperables desde φ(v).

**Justificación.** Si φ es inyectiva, existe φ⁻¹. Aplicar φ⁻¹ recupera v. Aplicar T, Γ o conteos sobre v produce el mismo resultado. La clasificación no depende de la representación; depende del vector.

### 8.4. Codificaciones con pérdida

Una codificación que colapse dos estados distintos (por ejemplo, tratar U como 0) no es inyectiva y destruye información. El SV no admite codificaciones con pérdida como representaciones equivalentes. Pueden existir como proyecciones (por ejemplo, «vista optimista» que trata U como 0 para una estimación rápida), pero deben estar declaradas como tales.

---

## 9. Límites de cierre

Quedan fuera del Documento VI como cierre fuerte:

- cálculo diferencial clásico (derivadas en sentido continuo);
- integrales clásicas (Riemann, Lebesgue);
- variable compleja y teoría de funciones analíticas;
- teoría de residuos;
- transformada de Laplace e inversa (continua);
- integrales múltiples como herramienta nativa;
- invariantes espectrales completos del grafo de composición;
- función de mérito universal independiente de dominio.

---

## 10. Líneas futuras

### 10.1. Puente discreto-continuo

Si en el futuro se construye una representación formal del SV en un dominio continuo o analítico que preserve los invariantes Inv_SV, entonces podrá abrirse un documento posterior sobre análisis continuo, variable compleja, residuos o Laplace. Esa expansión se haría sobre la base funcional ya cerrada por los Documentos I–VI, no en lugar de ella.

### 10.2. Invariantes espectrales

El análisis espectral del grafo de composición (autovalores de la laplaciana, espectro de matrices de propagación) puede revelar propiedades estructurales profundas. Queda como exploración futura.

### 10.3. Teoría de la información discreta

La entropía de Shannon del vector ternario, la información mutua entre células acopladas y la capacidad del canal de transducción son herramientas de la teoría de la información que operan sobre objetos discretos y podrían aplicarse al SV sin salir del marco.

### 10.4. Operadores de convolución discreta

La convolución de secuencias de trayectoria (útil para analizar respuestas a sucesos recurrentes) tiene formalización natural en dominio Z y en dominio temporal discreto. Queda abierta.

---

## 11. Conclusión

El marco SV queda dotado de herramientas de análisis propias de su dominio discreto.

Las trayectorias se analizan con diferencias finitas: Δf(k) mide el cambio entre frames. La estabilización, la oscilación y los ciclos tienen definición formal. Las funciones generatrices codifican el espacio combinatorio 3ⁿ de cada célula. La transformada Z opera sobre secuencias numéricas canónicas extraídas de T y codifica su estructura en un dominio donde las operaciones se simplifican. La matriz de adyacencia, el operador de propagación y la influencia estructural cuantifican la arquitectura compositiva. Los cambios de codificación preservan los invariantes si son inyectivos.

Estas herramientas no importan el continuo al discreto. Son nativas del dominio que el SV habita. El cálculo clásico queda como horizonte condicionado: solo entrará cuando un puente formal entre el discreto y el continuo lo justifique.

Con los seis documentos, el SV tiene: célula (Fundamentos), composición (I, II), evolución (III), entrada del mundo (IV), uso (V) y análisis (VI). La serie queda abierta hacia arriba — siempre lo estará — pero el primer nivel completo del sistema está construido.

---

## Referencias

[R1] Juan Antonio Lloret Egea. *Fundamentos algebraico-semánticos del Sistema Vectorial SV.* v1.0.0, Release 3. ITVIA, 2026.
https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

[R2] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — I. Transmisión en serie por parámetro puente.* v1, Release 4. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv/release/4

[R3] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — II. Gramática general de composición.* v1.0, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--ii-gramatica-general-de-composicion/release/1

[R4] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta.* v1, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iii-horizonte-de-sucesos-y-reevaluacion-discreta/release/2

[R5] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema.* v1, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iv-transduccion-al-alfabeto-ternario-e-interfaz-parametrica-del-sistema/release/1

[R6] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — V. Invariantes, agentes especializados y operador de consulta del sistema.* v2, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--v-invariantes-agentes-especializados-y-operador-de-consulta-del-sistema/release/2

[R7] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

---

## Apéndice breve de notación

| Símbolo | Significado |
|---------|------------|
| Δf(k) | Diferencia finita |
| n₀(k), n₁(k), nU(k) | Secuencias de conteo |
| Γ(k) | Secuencia de criticidad |
| κ(k) | Clasificación codificada |
| 𝒵{f} | Transformada Z |
| G_C(x, y, z) | Función generatriz |
| A_𝒜 | Matriz de adyacencia |
| P_𝒜 | Operador de propagación |
| d_eff | Profundidad efectiva |
| ρ(C, 𝒜) | Influencia estructural |
| [v]_B | Representación en codificación B |

---

*Documento doctrinal del Sistema Vectorial SV. ISSN 2695-6411.*
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
