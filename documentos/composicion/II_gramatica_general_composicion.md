# Álgebra de composición intercelular del marco SV

## II. Gramática general de composición

### Patrones compositivos tipados, relación semántica previa y grados de madurez formal

**Autor:** Juan Antonio Lloret Egea
**Versión:** 1.0
**Lugar y fecha:** Madrid, 11/03/2026
**Estado:** Documento doctrinal publicado
**URL canónica:** https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--ii-gramatica-general-de-composicion/release/1

---

## 1. Objeto y alcance

El presente documento es la segunda pieza de la teoría de composición intercelular del Sistema Vectorial SV. Su objeto es elevar la discusión desde un patrón compositivo particular — la transmisión en serie por parámetro puente, ya formalizada en el Documento I — a una gramática tipada de patrones compositivos.

La tesis central es la siguiente:

> El Sistema Vectorial SV no posee una única ley de composición entre células, sino una gramática tipada de patrones compositivos. Cada patrón se rige por una relación semántica previa entre los elementos implicados — sean células individuales, pares de células o subsistemas ya compuestos — que determina qué mecanismo de realización es lícito. La elección del mecanismo no es libre una vez fijadas la relación semántica y la especificación del sistema: está condicionada por la naturaleza de la relación y debe estar formalmente declarada antes de la ejecución.

### Qué hace este documento

Clasifica los patrones compositivos reconocidos en el marco SV, establece sus condiciones de validez, define la relación semántica previa como paso obligatorio de todo diseño compositivo, y fija una jerarquía conceptual que distingue entre relación, patrón, operador y constructor.

### Qué no hace este documento

Este documento no rehace el Documento I: la serie por puente entra como patrón ya cerrado, por referencia. No formaliza la composición temporal — qué ocurre cuando el mismo sistema se evalúa más de una vez a lo largo del tiempo —, que pertenece a una pieza futura autónoma. No cierra exhaustivamente el horizonte del marco: otros planos de estructuración, dinámica o evolución podrán abordarse en piezas posteriores. No valida clínicamente ningún dominio. No delega autoridad en inteligencia artificial, estadística ni minería de datos.

La separación respecto a la composición temporal es deliberada y firme. Este documento trata la composición espacial: cómo se combinan células dentro de un instante de evaluación. La composición temporal — qué pasa entre instantes — es un plano ortogonal que requiere su propia teoría.

### Por qué la composición pertenece al sistema

La composición intercelular no es propiedad de SVperitus ni de SVcustos. Es una capacidad del Sistema Vectorial SV en cuanto tal. Cualquier rama del sistema que opere con más de una célula necesita una gramática de composición. El Documento I lo demostró para la serie; la evidencia interna del proyecto muestra que otros dominios usan otros patrones. La gramática general es pieza del sistema, no de una aplicación.

---

## 2. Subordinación a Fundamentos

Este documento es doctrina derivada de segundo nivel. La autoridad normativa suprema del Sistema Vectorial SV reside en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV* (Release 3). Todo lo que aquí se establece debe ser coherente con dicho documento. En caso de discrepancia, prevalecen los *Fundamentos*.

La familia de operadores reconocida en los *Fundamentos* (§7.5) es:

> ℱ_SV = { max, min, ⊗_gate, σ_{k,φ}, ▷, Γ, Comp }

Este documento no amplía la familia ℱ_SV; introduce definiciones auxiliares — como la tabla de admisibilidad 𝒯 y el objeto supervisable 𝒮 — para realizar y organizar operadores ya reconocidos. El principio de cierre de los *Fundamentos* (§7.12) establece que la gramática de composición puede ampliarse pero no reducirse indebidamente: este documento amplía la gramática sin reducirla y sin añadir operadores a la familia básica.

---

## 3. Tabla de notación y estatutos

### Símbolos heredados de los Fundamentos y del Documento I

Todos los símbolos fijados en los *Fundamentos* (§§2–9) y en el Documento I (§2.3) permanecen vigentes sin modificación. Se destacan los que este documento emplea con mayor frecuencia:

| Símbolo | Significado | Origen |
|---------|------------|--------|
| Σ = {0, 1, U} | Alfabeto ternario | Fundamentos §2 |
| Cᵢ = (vᵢ, Ωᵢ, κᵢ, ρᵢ) | Célula composable canónica | Fundamentos §7.2 |
| Kᵢ | Codominio tipado (≡ Ωᵢ) | Doc I §2.3 |
| χᵢ : Cᵢ → Ωᵢ | Función de evaluación | Fundamentos §7.3 |
| Ĉᵢ = (Cᵢ, Bᵢ) | Célula acoplable | Doc I §3.3 |
| σ_{k,φ} | Operador de sustitución (serie) | Fundamentos §7.8 |
| ⊗_gate | Compuerta jerárquica | Fundamentos §7.7 |
| ▷ | Supervisión meta / veto | Fundamentos §7.9 |
| Γ | Función de criticidad | Fundamentos §7.10 |
| Comp | Constructor de arquitectura | Fundamentos §7.11 |
| Ψ_{i,k} | Operador de conflicto | Doc I §8.2 |

### Símbolos introducidos en este documento

| Símbolo | Significado | Estatuto |
|---------|------------|----------|
| R(𝒜) | Relación semántica previa sobre una arquitectura compositiva | Definición |
| K_comp | Codominio de la salida compuesta por compuerta | Definición |
| 𝒯 : Kᵢ × Kⱼ → K_comp | Tabla de admisibilidad de una compuerta | Definición |
| 𝒮 | Objeto supervisable (célula, par compuesto o sistema) | Definición |

---

## 4. Relación semántica previa (R)

### 4.1. Principio

Antes de elegir un mecanismo de composición, el diseñador debe fijar explícitamente qué relación semántica existe entre los elementos implicados. La relación es una decisión de modelización: pertenece al diseñador humano, no al álgebra. El álgebra determina, una vez fijada la relación, qué mecanismo es lícito y qué propiedades garantiza.

### 4.2. Alcance de R

La relación semántica previa no se limita a pares de células individuales. Puede definirse sobre:

**Dos células individuales:** R(Cᵢ, Cⱼ). Es el caso más simple. La salida de una célula alimenta a la otra (dependencia funcional), o ambas miden lo mismo y la más severa gobierna (dominancia homogénea).

**Un conjunto de células:** R(Cᵢ, Cⱼ, …, Cₖ). Células independientes que se combinan por admisibilidad cruzada (habilitación cruzada), o varias células que transmiten a una integradora por puentes distintos (fusión paralela en serie).

**Una célula y un subsistema ya compuesto:** R(Cₘ, 𝒮). Una célula de segundo orden supervisa el resultado de una composición previa (supervisión de integridad).

**Una arquitectura compositiva completa:** R(𝒜). Un constructor organiza varias células heterogéneas con operadores distintos en su interior (ensamblaje multicapa).

La forma general es R(𝒜), donde 𝒜 designa la arquitectura compositiva sobre la que se aplica la relación. Las formas R(Cᵢ, Cⱼ) y R(Cᵢ, Cⱼ, …, Cₖ) son casos particulares.

### 4.3. Clasificación inicial de relaciones semánticas

Las siguientes son modos relacionales previos al diseño, no operadores. Cada uno describe un tipo de vínculo entre los elementos que se van a componer. El operador o constructor correspondiente viene después, condicionado por la relación.

| Relación semántica | Sobre qué actúa | Qué describe |
|-------------------|-----------------|-------------|
| Dependencia funcional | Par de células | La salida de una célula es dato necesario para otra |
| Habilitación cruzada | Conjunto de células | Células independientes cuya validez conjunta depende de una tabla de admisibilidad |
| — Dominancia homogénea (subtipo) | Par de células con mismo codominio | Caso particular de habilitación cruzada bajo comparabilidad ordinal homogénea |
| Supervisión de integridad | Célula + subsistema | Una célula evalúa la validez de un resultado ya compuesto |
| Ensamblaje multicapa | Arquitectura completa | El dominio exige organizar varias células heterogéneas con mecanismos distintos |

### 4.4. Estatuto de esta clasificación

Inicial y abierta. No es un catálogo metafísicamente cerrado. Desarrollos futuros podrán añadir relaciones si el sistema lo requiere. Lo que no debe hacerse es elegir mecanismo sin fijar R.

---

## 5. Jerarquía conceptual: relación, patrón, operador, constructor

Para evitar confusión terminológica, este documento fija cuatro niveles conceptuales distintos. Los niveles son progresivos: cada uno presupone el anterior.

### Nivel 1 — Relación semántica previa (R)

Qué tipo de vínculo existe entre los elementos que se van a componer. Es una decisión de modelización que el diseñador humano documenta. No es un objeto algebraico: es la condición previa que determina todo lo que sigue.

### Nivel 2 — Patrón compositivo

Clase de composición asociada a una relación semántica. Cada patrón tiene sus condiciones de validez, sus propiedades formales y su grado de madurez. Los patrones reconocidos en este documento son: serie por puente, compuerta jerárquica (que subsume la dominancia homogénea como caso particular bajo comparabilidad ordinal homogénea), y supervisión meta.

### Nivel 3 — Operador

Mecanismo algebraico concreto que realiza un patrón. Tiene firma (dominio y codominio), definición formal y comportamiento demostrable. Los operadores reconocidos en los *Fundamentos* son los de ℱ_SV. Un patrón puede tener un operador principal y operadores auxiliares (Ψ para conflicto, Γ para criticidad).

### Nivel 4 — Constructor

Mecanismo que no compone dos objetos sino que organiza una arquitectura completa con operadores distintos en su interior. Comp es el único constructor reconocido actualmente. Su estatuto formal es inferior al de los operadores: es un organizador, no una función con firma cerrada.

### Tabla resumen

| Nivel | Qué es | Ejemplo |
|-------|--------|---------|
| 1. Relación | Vínculo semántico entre elementos | "La salida de IMMUNO-1 es dato necesario para IMMUNO-2" |
| 2. Patrón | Clase de composición | Serie por puente |
| 3. Operador | Mecanismo algebraico | σ_{k,φ} |
| 4. Constructor | Organizador de arquitectura | Comp |

---

## 6. Escala de madurez formal

No todos los patrones compositivos poseen el mismo grado de cierre formal. Esta diferencia se declara explícitamente para que el lector sepa qué nivel de confianza puede depositar en cada sección.

| Grado | Significado | Requisitos |
|-------|------------|------------|
| **A** | Plenamente formalizado | Definición algebraica completa, proposiciones demostradas, condiciones de buena formación, caso verificado |
| **B** | Formalizado con caso de referencia | Definición algebraica, condiciones de validez, propiedades defendibles, caso interno como instancia |
| **C** | Abierto formalmente | Definición operativa, condiciones mínimas, sin proposiciones fuertes. Borde del documento |

---

## 7. Estatuto de los casos internos del proyecto

Los casos internos del proyecto — inmunología, neumología, genética — cumplen función de instancia, contraste y tensionamiento de los patrones. No sustituyen la formulación general ni constituyen por sí mismos prueba suficiente de universalidad.

La teoría se formula general. Los casos se presentan como instancias que ilustran. Si un patrón solo se sostiene por un caso interno, su grado de madurez lo refleja (Grado B o C, no A).

---

## 8. Reabsorción del patrón serie (Grado A)

### Relación semántica: dependencia funcional

La salida de una célula es dato necesario para otra. La primera evalúa; su resultado se traduce por un conector tipado y entra como parámetro puente en la segunda.

### Referencia

Este patrón está plenamente formalizado en el Documento I (*Álgebra de composición intercelular del marco SV — I. Transmisión en serie por parámetro puente*, Release 4). No se reescribe aquí. Se resume su contenido y se incorpora como instancia de la gramática general.

### Contenido formalizado en el Documento I

- Célula acoplable Ĉᵢ = (Cᵢ, Bᵢ) como extensión compositiva.
- Parámetro puente, conector tipado φⱼ→ᵢ⁽ᵏ⁾ : Kⱼ → Σ.
- Tríada del flujo: xᵢ⁽⁰⁾ → x̃ᵢ → yᵢ = χᵢ(Cᵢ[x̃ᵢ]).
- Grafo dirigido acíclico 𝒢 = (V, E, Φ).
- Dos regímenes de buena formación: simple (RS) y general (RG).
- Operador de conflicto Ψ_{i,k} con tres familias (consenso, precedencia, soberanía local).
- Criticidad condicionada al puente ΔΓₖ ∈ {0, 1}.
- Nueve proposiciones demostradas.
- Siete principios doctrinales.

### Operador: σ_{k,φ} (serie)

Mecanismo de Nivel 3 con firma, definición y comportamiento completamente demostrado.

### Caso verificado: IMMUNO-1 → IMMUNO-2

Composición en régimen simple, DAG de profundidad 1, 25 parámetros por célula, puente en P25.

---

## 9. Compuerta jerárquica (Grado B)

### 9.1. Relación semántica: habilitación cruzada

Dos o más células se evalúan independientemente. Ninguna alimenta un parámetro de la otra. La validez de la composición global depende de que las salidas de ambas satisfagan conjuntamente una tabla de admisibilidad.

La diferencia con la serie es nítida: en la serie, una célula transmite dato a otra; en la compuerta, cada célula produce su salida por separado y la composición opera sobre esas salidas, no sobre los vectores internos.

### 9.2. Definición

**Definición 1.** Sean Ĉᵢ y Ĉⱼ dos células acoplables con salidas yᵢ ∈ Kᵢ y yⱼ ∈ Kⱼ. Una **compuerta jerárquica** entre Cᵢ y Cⱼ es una aplicación

> 𝒯 : Kᵢ × Kⱼ → K_comp

donde K_comp es el codominio de la salida compuesta y 𝒯 es la **tabla de admisibilidad**, una función explícita, finita y determinista que el diseñador define y documenta.

La compuerta no es conmutativa en general. El orden de los argumentos puede importar si la semántica es asimétrica: una célula de sospecha y una célula de confirmación no son intercambiables.

### 9.3. Extensión a más de dos células

La definición se extiende naturalmente a k células:

> 𝒯 : K₁ × K₂ × … × Kₖ → K_comp

Las condiciones de validez se mantienen: la tabla debe ser explícita, finita y determinista para toda combinación de entradas.

### 9.4. Condiciones de validez

**CV1 — Independencia de evaluación.** Las células de entrada se evalúan independientemente. No existe parámetro puente entre ellas en la dirección de la compuerta.

**CV2 — Tabla explícita.** La tabla de admisibilidad está completamente definida antes de la ejecución del sistema. No se aprende, no se infiere, no se delega.

**CV3 — Determinismo.** Para cada combinación de entradas, la tabla produce exactamente una salida.

**CV4 — Documentación semántica.** La asimetría entre las células de entrada, si existe, está documentada. El diseñador explica por qué una célula no suplanta a la otra.

### 9.5. Proposición 1 — Determinismo de la compuerta

Si las evaluaciones χᵢ(Cᵢ) y χⱼ(Cⱼ) son deterministas y la tabla 𝒯 es determinista, entonces la composición por compuerta es determinista.

**Demostración.** La salida compuesta es 𝒯(yᵢ, yⱼ) con yᵢ = χᵢ(Cᵢ) y yⱼ = χⱼ(Cⱼ). Si χᵢ, χⱼ y 𝒯 son funciones deterministas, su composición es determinista. ∎

### 9.6. Proposición 2 — La compuerta no fabrica certeza

Si 𝒯 está definida de modo que toda combinación que incluya al menos una entrada indeterminada produce una salida indeterminada o conservadora, entonces la compuerta no fabrica certeza a partir de la indeterminación.

**Demostración.** Por la definición de la tabla. Si el diseñador exige que 𝒯(yᵢ, yⱼ) ∉ {cierre favorable, cierre desfavorable} cuando yᵢ o yⱼ es indeterminado, la compuerta no puede producir certeza donde no la hay. La propiedad depende del diseño de la tabla, no del operador en abstracto. ∎

**Nota.** Esta propiedad no es automática de toda compuerta: es una condición de diseño prudente. El Documento II la recomienda como principio pero no la impone como axioma, porque podría haber dominios donde una entrada determinada sea suficiente para cerrar el sistema incluso con otra indeterminada.

### 9.7. Dominancia homogénea como caso particular

La dominancia homogénea (max/min de los *Fundamentos* §7.6) es un caso particular de compuerta jerárquica donde:

- Las dos células comparten el mismo codominio: Kᵢ = Kⱼ = K.
- Existe un orden total sobre K.
- La tabla de admisibilidad es trivial: 𝒯(yᵢ, yⱼ) = max(yᵢ, yⱼ) según ese orden.

Las cuatro condiciones de validez de los *Fundamentos* §7.6 (compatibilidad de codominio, ordinal, estructural y orden explícito) son condiciones adicionales que la dominancia exige sobre la compuerta general.

La dominancia se subsume formalmente en la compuerta. Su identidad histórica en el proyecto y sus condiciones específicas justifican mencionarla con nombre propio, pero no requiere una sección independiente: es una compuerta con tabla trivial y requisitos de compatibilidad reforzados.

### 9.8. Caso de referencia: SV-ADC (neumología)

La arquitectura SV-ADC del dominio de neumología instancia la compuerta jerárquica:

- **Célula L:** SV-ADC_L(25,5). Sospecha clínico-lesional. Salida: K_L = {LOW_L, U_L, HIGH_L}.
- **Célula V:** SV-ADC_V(16,4). Validez confirmatoria. Salida: K_V = {NONCONF_V, U_V, CONF_V}.
- **Tabla de admisibilidad 𝒯:** GLOBAL_HIGH solo si L = HIGH_L y V = CONF_V. GLOBAL_LOW solo si L = LOW_L y V = NONCONF_V. Todo lo demás → GLOBAL_U.

Las células L y V tienen tamaños distintos (25 y 16 parámetros) y semántica asimétrica: la sospecha no puede confirmar, la confirmación no puede generar sospecha. La compuerta formaliza exactamente esta relación de habilitación cruzada.

La supervisión META(9,3) actúa sobre el resultado de esta compuerta, no dentro de ella. Es un nivel distinto, formalizado en §10.

### 9.9. Lo que queda abierto

- Axiomática general de tablas de admisibilidad: ¿existen propiedades que toda tabla bien formada deba satisfacer, independientemente del dominio?
- Comportamiento formal de la compuerta cuando una entrada es U: ¿debe exigirse siempre conservadurismo, o hay dominios donde una sola entrada determinada basta?

---

## 10. Supervisión meta del sistema (Grado B)

### 10.1. Relación semántica: supervisión de integridad

Una célula de segundo orden no evalúa el contenido de un dominio. Evalúa la validez, integridad o clasificabilidad de un resultado ya producido por el sistema. Su función es decidir si el resultado puede aceptarse, si debe tensionarse o si debe anularse.

### 10.2. Tres niveles de supervisión

| Nivel | Qué supervisa | Ejemplo |
|-------|--------------|---------|
| (a) | Una célula individual | Meta-célula SV(9,3)-IA sobre IMMUNO-2 |
| (b) | Una relación entre células o un resultado compuesto | SV-ADC_META(9,3) sobre el par L/V ya compuesto |
| (c) | Un sistema completo | Meta-célula con poder de veto sobre toda la arquitectura |

### 10.3. Definición

**Definición 2.** Sea 𝒮 un **objeto supervisable**: una célula individual, un resultado de compuerta, un par de salidas tipadas, o un sistema compuesto. Sea M una célula de segundo orden con salida yₘ ∈ Kₘ. La **supervisión meta** es la aplicación del operador

> M ▷ 𝒮

cuyo efecto depende de yₘ:

- Si yₘ indica integridad, el resultado de 𝒮 se acepta.
- Si yₘ indica tensión, el resultado se acepta con señal de cautela.
- Si yₘ indica veto, el resultado de 𝒮 queda anulado.

### 10.4. Separación respecto a la compuerta

La supervisión meta NO forma parte de la compuerta. Son dos niveles secuenciales: primero las células base se componen (por compuerta, por serie o por cualquier otro patrón); después la meta-célula supervisa el resultado de esa composición. En neumología: primero ⊗_gate combina L y V; después META supervisa ese resultado y puede bloquearlo.

### 10.5. Condiciones de validez

**CV1 — Segundo orden.** La meta-célula no evalúa contenido de dominio. Sus parámetros miden completitud, coherencia, suficiencia, resolubilidad y clasificabilidad — propiedades del proceso, no del sujeto evaluado.

**CV2 — Parámetros automáticos.** Los parámetros de la meta-célula son derivados del sistema (no manuales del dominio). Se calculan a partir de los vectores y salidas de las células base.

**CV3 — Veto como principio de diseño.** Si la meta-célula emite veto, el resultado del sistema queda anulado independientemente de lo que digan las células base. Este principio se adopta como regla de diseño del marco SV: el sistema no debe producir resultados que no pasen control de integridad. Su formulación como propiedad formal requiere una definición cerrada de "anulación" que este documento deja abierta.

### 10.6. Proposición 3 — Determinismo de la supervisión

Si la evaluación de M es determinista y la regla de interpretación de yₘ (aceptar, tensionar, vetar) es determinista, entonces la supervisión meta es determinista.

**Demostración.** Análoga a la de la Proposición 1. La supervisión es una función de yₘ, que es función determinista de los parámetros de M. ∎

### 10.7. El objeto supervisable 𝒮

La formalización del objeto supervisable es una cuestión abierta cuando 𝒮 es un resultado compuesto (nivel b). En neumología, META supervisa "el par L/V ya compuesto por compuerta". Formalmente, 𝒮 podría definirse como:

- La tupla (yᵢ, yⱼ, 𝒯(yᵢ, yⱼ)) — las salidas de las células base y la salida compuesta.
- O directamente 𝒯(yᵢ, yⱼ) — solo la salida compuesta.

La primera opción da más información a la meta-célula (puede detectar discordancia entre las entradas). La segunda es más simple. El parámetro M03 de SV-ADC_META mide explícitamente la discordancia L/V, lo que sugiere que la primera opción es la que el proyecto ya usa en la práctica.

Este documento no cierra la definición formal de 𝒮. La deja como línea de investigación abierta con la evidencia neumológica como orientación.

### 10.8. Caso de referencia: SV-ADC_META (neumología)

La meta-célula SV-ADC_META(9,3) instancia la supervisión de nivel (b):

- Supervisa el par L/V ya compuesto por compuerta.
- Sus 9 parámetros miden: completitud de L, completitud de V, discordancia L/V, suficiencia morfológica, suficiencia IHQ, suficiencia molecular, coherencia global, resolubilidad de U, integridad para clasificación.
- Salida: K_META = {META_BLOCK, META_TENSE, META_READY}.
- Si META_BLOCK, la salida global del sistema no puede ser GLOBAL_HIGH ni GLOBAL_LOW: cae a GLOBAL_U.

---

## 11. Composición multinivel / Comp (Grado C)

### 11.1. Relación semántica: ensamblaje multicapa

El dominio exige varias células heterogéneas organizadas con operadores distintos. Ningún patrón individual basta para describir la arquitectura completa. Se necesita un constructor que organice el conjunto.

### 11.2. Estatuto

Comp no es un operador al mismo nivel formal que σ_{k,φ}, ⊗_gate o ▷. Es un **constructor organizativo** de Nivel 4 que:

- recibe un conjunto de células y de relaciones entre ellas;
- asocia a cada relación su patrón y su operador lícito;
- y define el orden de evaluación del sistema resultante.

Su formalización algebraica con la misma nitidez que los operadores de Nivel 3 no está cerrada. Entra en este documento como **borde**, no como centro.

### 11.3. Lo que puede decirse hoy

Comp es el mecanismo que responde a la pregunta: "dado un conjunto de células con relaciones semánticas heterogéneas, ¿cómo se ensambla el sistema completo?" En la práctica, Comp asigna a cada relación su patrón, ordena la evaluación y produce una salida global.

### 11.4. Instancias conocidas

**Neumología (SV-ADC):** el compositor secuencial integra L + V (por compuerta) + META (por supervisión) + Γ multinivel, y produce un `composer_state` que mide progresión diagnóstica. Es la instancia más concreta disponible.

**Genética (horizonte):** se ha identificado como dominio futuro que necesitará composición entre subdominios heterogéneos (drivers, supresores, reparación, CNV). La composición multinivel será probablemente su patrón natural.

### 11.5. Lo que no se cierra

- Firma formal de Comp como función.
- Proposiciones fuertes.
- Axiomática del constructor.
- Relación entre Comp y el grafo 𝒢 del Documento I.
- Criterio formal para distinguir cuándo un sistema necesita Comp y cuándo basta con una combinación de patrones individuales.

---

## 12. Criticidad compositiva

### 12.1. Γ en la gramática general

La función de criticidad Γ, definida en los *Fundamentos* (§7.10), se aplica dentro de cada célula individual sobre su vector. El Documento I extendió su uso al contexto de la serie con la criticidad condicionada al puente ΔΓₖ. Este documento amplía el marco de criticidad para cubrir los demás patrones.

### 12.2. Niveles de criticidad

| Nivel | Qué mide | Dónde existe | Estado |
|-------|---------|--------------|--------|
| Γ per-cell | Criticidad dentro de una célula individual | Fundamentos §7.10 | Definido |
| ΔΓₖ condicionado al puente | Efecto de resolver la transmisora sobre la receptora | Doc I, Proposición 9 | Demostrado (∈ {0,1}) |
| Γ per-cell en compuerta | Criticidad de cada célula por separado dentro de una compuerta | Neumología (Γ_ADC-L, Γ_ADC-V) | Instanciado |
| Γ global del sistema | Criticidad del sistema compuesto como un todo | Neumología (Γ_ADC-GLOBAL) | Instanciado |

### 12.3. Γ per-cell en compuerta

Cuando dos células se combinan por compuerta, cada una mantiene su Γ propio. La criticidad de la célula L es independiente de la criticidad de la célula V: cada una tiene sus propias U, sus propias distancias a umbral y su propio Γ. No hay parámetro puente entre ellas, luego no hay ΔΓₖ. Lo que hay es un par de valores (Γ_L, Γ_V) que informa al diseñador sobre dónde conviene resolver indeterminación primero.

### 12.4. Γ global del sistema

La criticidad global mide si el sistema compuesto tiene indeterminación activa y resoluble. En neumología, Γ_ADC-GLOBAL indica si existe un próximo paso diagnóstico con alto valor resolutivo.

La definición formal de Γ global es una cuestión abierta. Dos caminos posibles:

**Opción A — Función de los Γ per-cell.** Γ_global = f(Γ₁, Γ₂, …, Γₘ, yₘ_META). Ventaja: se construye sobre lo que ya existe. Desventaja: puede perder información sobre la interacción entre células.

**Opción B — Definición autónoma.** Γ_global se define directamente sobre el estado del sistema compuesto, no como función de los Γ individuales. Ventaja: puede capturar criticidad emergente. Desventaja: requiere formalización nueva.

Este documento no resuelve la cuestión. La deja abierta con la evidencia neumológica como orientación.

---

## 13. Conflicto y prioridad en la gramática general

### 13.1. En la serie

El Documento I formalizó el operador Ψ para resolución de concurrencia sobre un mismo puente en el régimen general. Queda vigente sin modificación.

### 13.2. En la compuerta

En la compuerta no hay conflicto externo adicional comparable al de la serie. No existe concurrencia de varias transmisiones sobre un mismo destino. La tabla de admisibilidad absorbe internamente la resolución de todas las combinaciones de entrada, incluidas las semánticamente incompatibles: para cada combinación, la tabla produce exactamente una salida determinista.

### 13.3. En la supervisión meta

Si dos meta-células supervisan el mismo sistema, puede haber conflicto entre sus veredictos (una acepta, otra veta). Este escenario no se presenta en la arquitectura actual del proyecto (cada sistema tiene a lo sumo una meta-célula). Se deja como cuestión abierta para arquitecturas futuras.

### 13.4. En Comp

Abierto. El constructor no tiene aún la formalización suficiente para determinar si genera conflictos internos.

### 13.5. Principio general

Ψ no se universaliza. Si otros patrones requieren resolución de conflicto, se definirán mecanismos específicos para cada caso. La resolución de conflicto es siempre determinista y declarada, nunca aprendida.

---

## 14. Casos internos del proyecto

| Dominio | Patrón principal | Operadores usados | Grado | Estado |
|---------|-----------------|-------------------|-------|--------|
| Inmunología | Serie | σ_{k,φ}, ▷, Γ, ΔΓₖ, Ψ | A | Doc I cerrado, R4 |
| Neumología — compuerta L/V | Compuerta | ⊗_gate | B | Arquitectura cerrada |
| Neumología — supervisión META | Meta-supervisión | ▷ | B | Arquitectura cerrada |
| Neumología — compositor | Comp | Comp | C | Arquitectura cerrada |
| Genética | Compilación (horizonte) | Comp (futuro) | C | Prospectivo |

### Afinidades dominio-operador

| Dominio | Relación semántica dominante | Por qué |
|---------|----------------------------|---------|
| Inmunología | Dependencia funcional | Una célula (profilaxis) condiciona a otra (riesgo) |
| Neumología | Habilitación cruzada | Sospecha y confirmación son independientes pero ambas necesarias |
| Genética | Ensamblaje multicapa | Subdominios heterogéneos que no se reducen a un solo patrón |

Estas afinidades son observaciones empíricas, no leyes. Otros dominios futuros podrán gravitar hacia patrones distintos de los que aquí se documentan.

---

## 15. Límites de cierre actuales

**L1 — Densidad proposicional desigual.** La serie tiene nueve proposiciones. La compuerta tiene dos. La meta-supervisión tiene una. Comp no tiene ninguna. Esta asimetría es honesta, no un defecto: refleja los grados reales de madurez.

**L2 — Objeto supervisable 𝒮 no formalizado para nivel (b).** Se ha identificado la cuestión y se ha orientado con la evidencia neumológica. No se ha cerrado.

**L3 — Comp sin definición algebraica cerrada.** Entra como constructor organizativo, no como operador con firma.

**L4 — Γ global sin definición formal.** Instanciado en neumología. Dos caminos posibles identificados, ninguno cerrado.

**L5 — Firma general de R(𝒜) no cerrada.** La clasificación inicial es suficiente para este documento. La formalización como objeto algebraico queda abierta.

**L6 — Axiomática de tablas de admisibilidad no desarrollada.** Las condiciones de validez son suficientes, pero una teoría de tablas bien formadas no existe todavía.

**L7 — No cubre composición temporal.** Deliberado. Pieza futura autónoma.

---

## 16. Líneas futuras

### 16.1. Axiomática de Comp

Formalizar el constructor como objeto con propiedades demostrables. Estudiar su relación con el grafo 𝒢 del Documento I.

### 16.2. Definición formal de Γ global

Resolver la disyuntiva entre función de Γ per-cell y definición autónoma. Demostrar propiedades de acotación si las hay.

### 16.3. Formalización de 𝒮

Definir el objeto supervisable para supervisión de nivel (b) y (c). Estudiar qué información debe pasar a la meta-célula.

### 16.4. Axiomática de tablas de admisibilidad

Estudiar si existen propiedades universales de las tablas bien formadas (completitud, conservadurismo, monotonía).

### 16.5. Composición temporal

Frames, factor ν, trayectorias auditables. Pieza autónoma que presupone la gramática espacial aquí definida.

### 16.6. Firma cerrada de R(𝒜)

Formalizar la relación semántica previa como objeto algebraico con propiedades verificables.

### 16.7. Nuevos dominios

Genética como horizonte de compilación. Otros dominios no clínicos (cibernética, humanoides) como horizontes lejanos.

---

## 17. Conclusión doctrinal

El Sistema Vectorial SV, tras este desarrollo, queda formalmente equipado con una gramática de composición intercelular que reconoce múltiples patrones y los organiza bajo una jerarquía explícita de relaciones semánticas, patrones, operadores y constructores.

La gramática no es monolítica. Distingue entre tres grados de madurez formal. El patrón de serie por puente (Grado A) está plenamente formalizado en el Documento I con nueve proposiciones y dos regímenes de buena formación. La compuerta jerárquica y la supervisión meta (Grado B) tienen definición algebraica, condiciones de validez, propiedades defendibles y caso de referencia en el proyecto. La composición multinivel (Grado C) entra como constructor organizativo en el borde del documento, sin pretensión de cierre algebraico.

La relación semántica previa R(𝒜) se introduce como paso obligatorio de todo diseño compositivo: antes de elegir un operador, el diseñador debe fijar qué tipo de vínculo existe entre los elementos que se van a componer. La clasificación inicial reconoce cuatro modos relacionales principales — dependencia funcional, habilitación cruzada, supervisión de integridad y ensamblaje multicapa — más la dominancia homogénea como subtipo reconocido de la habilitación cruzada bajo comparabilidad ordinal homogénea.

La dominancia queda subsumida en la compuerta como caso particular con tabla trivial. Esto simplifica la gramática sin eliminar la identidad histórica de la dominancia en el proyecto. La criticidad compositiva se amplía desde el puente individual (ΔΓₖ del Documento I) hasta la criticidad per-cell en compuerta y la criticidad global del sistema, cuya definición formal queda como línea de investigación abierta.

Los casos internos del proyecto — inmunología para serie, neumología para compuerta y meta-supervisión, genética como horizonte de compilación — ilustran y tensionan los patrones sin fundamentarlos. La teoría se ha formulado general; los dominios la instancian.

Este documento es la segunda pieza de la teoría compositiva del marco SV. No es la última. Quedan expresamente reservados para piezas futuras: la composición temporal, la axiomática de Comp, la definición formal de Γ global, la formalización del objeto supervisable y la firma cerrada de R(𝒜). El horizonte permanece abierto.

El conjunto resultante — la relación semántica que clasifica, el patrón que organiza, el operador que ejecuta y el constructor que ensambla — constituye una gramática algebraica de células ternarias combinables cuya validez depende de la semántica de la relación entre ellas. Su resolución es determinista, trazable y auditable. No interviene la estadística. No interviene la minería de datos. No interviene la inteligencia artificial como autoridad. El ser humano fija las relaciones, elige los patrones, documenta las tablas, diseña las meta-células y gobierna el sistema. El álgebra garantiza que sus decisiones se ejecutan con exactitud.

---

## Referencias

[R1] Juan Antonio Lloret Egea. *Fundamentos algebraico-semánticos del Sistema Vectorial SV.* v1.0.0, Release 3. ITVIA, 2026.
https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

[R2] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — I. Transmisión en serie por parámetro puente.* v1, Release 4. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv/release/4

[R3] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

[R4] Juan Antonio Lloret Egea. *Compilador doctrinal y célula meta SV(9,3)-IA.* Release 5. ITVIA, 2026.
https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/5

---

*Documento doctrinal del Sistema Vectorial SV. ISSN 2695-6411.*
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
