# Álgebra de composición intercelular del marco SV

## V. Invariantes, agentes especializados y operador de consulta del sistema

### Cierre funcional del primer nivel superior del Sistema Vectorial SV

**Autor:** Juan Antonio Lloret Egea

**ORCID:** 0000-0002-6634-3351

**Versión:** 2

**Lugar y fecha:** Madrid, 11/03/2026

**Estado:** Documento doctrinal publicado

CC BY-NC-ND 4.0 · ISSN 2695-6411

---

## Resumen

Este documento formaliza el primer nivel funcional superior del Sistema Vectorial SV: cómo el sistema, una vez dotado de célula, composición, reevaluación y transducción, puede especializarse por dominios, configurarse como agente y ser consultado sin romper sus invariantes estructurales.

El documento introduce tres primitivos formales: el dominio especializado 𝔇 como firma de instanciación del SV sobre una arquitectura dada, el agente especializado A_𝔇 como arquitectura SV tipada por dominio, y el operador de consulta 𝒬_ω como mecanismo formal para interrogar al sistema con respuesta trazable.

Sobre esta base se establecen seis teoremas de invariancia y tres proposiciones del operador de consulta, que juntos garantizan que la especialización y la consulta no destruyen la identidad algebraica del sistema.

---

## 1. Objeto y alcance

### 1.1. Tesis central

El Sistema Vectorial SV no solo compone, reevalúa y transduce. También puede especializarse por dominios y ser consultado bajo invariantes comunes sin perder su identidad algebraico-semántica. La especialización es instanciación, no modificación. La consulta es lectura estructurada, no inferencia opaca.

### 1.2. Qué hace este documento

Formaliza tres piezas del nivel funcional superior del SV:

1. Los **invariantes** que ninguna especialización ni consulta puede romper sin salir del marco.
2. El **dominio especializado** y el **agente especializado** como objetos formales del sistema.
3. El **operador de consulta** como mecanismo para interrogar al sistema con respuesta, justificación y metadatos.

### 1.3. Qué no hace este documento

Este documento no:

- formaliza el operador de entrenamiento como objeto cerrado;
- instancia neurología como dominio maduro;
- formaliza el análisis discreto de trayectorias, funciones generatrices, transformada Z ni álgebra lineal del grafo de composición;
- formaliza representaciones y cambios de codificación del sistema;
- introduce humanoides como arquitectura encarnada;
- introduce estadística, minería de datos ni aprendizaje opaco.

### 1.4. Posición en la serie

- Los **Fundamentos** fijaron la célula y el núcleo semántico.
- El **Documento I** fijó la transmisión intercelular.
- El **Documento II** fijó la gramática de composición.
- El **Documento III** fijó sucesos, frame y trayectoria.
- El **Documento IV** fijó la entrada del mundo al sistema.
- El **Documento V** fija la especialización, la consulta y el cierre funcional.

Los Documentos I–IV construyen la maquinaria. El Documento V dice cómo se usa sin romperla.

---

## 2. Subordinación doctrinal y herencia de la serie

Este documento es doctrina derivada de segundo nivel. La autoridad normativa suprema reside en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. En caso de discrepancia, prevalecen los *Fundamentos*.

### Lo que este documento hereda

El Documento V no crea un sistema nuevo. Extrae el régimen de especialización y consulta del mismo SV ya construido.

- De los **Fundamentos:** Σ = {0, 1, U}, la célula exacta, n = b², T(n), χᵢ, ℱ_SV, primacía humana y exclusión de la probabilidad opaca.
- Del **Documento I:** transmisión en serie, acoplamiento intercelular, puente y propagación.
- Del **Documento II:** gramática general, jerarquía relación–patrón–operador–constructor, compuerta, meta-supervisión y Comp.
- Del **Documento III:** horizonte de sucesos ℋ(𝒜), frame Sₙ, dato νₙ, operador 𝒯_{νₙ}, trayectoria T y δ_Γ.
- Del **Documento IV:** transducción τⱼ, sensor ϕⱼ, admisibilidad R, interfaz ℐ(𝒜), máscara E(C), ley de crecimiento y U silenciosa U_s.

Todo lo que el Documento V define opera sobre estos objetos. No los sustituye, no los modifica y no los reinterpreta.

---

## 3. Tabla de notación

### Símbolos heredados

Todos los de Fundamentos y Documentos I–IV permanecen vigentes.

### Símbolos introducidos en este documento

| Símbolo | Significado | Estatuto |
|---------|------------|----------|
| 𝔇 | Dominio especializado | Definición |
| 𝒫 | Parámetros pertinentes del dominio | Componente de 𝔇 |
| Π_τ | Política de transducción del dominio | Componente de 𝔇 |
| Π_U | Política de indeterminación del dominio | Componente de 𝔇 |
| Π_C | Criterio de cierre del dominio | Componente de 𝔇 |
| A_𝔇 | Agente especializado tipado por dominio | Definición |
| 𝒬_ω | Operador de consulta bajo firma ω | Definición |
| ω | Firma de consulta (tipo, alcance, restricciones) | Definición |
| r | Respuesta de la consulta | Componente de salida de 𝒬 |
| J | Justificación trazable de la respuesta | Componente de salida de 𝒬 |
| M | Metadatos de criticidad, cobertura y U | Componente de salida de 𝒬 |
| Inv_SV | Familia de invariantes del sistema | Definición |

---

## 4. Invariantes del sistema bajo especialización

### 4.1. Principio

El SV puede especializarse. No puede dejar de ser el SV. Los invariantes son las propiedades que ninguna especialización, ningún dominio, ningún agente y ninguna consulta pueden romper sin abandonar el marco.

### 4.2. Definición

**Definición 1.** La **familia de invariantes del SV**, denotada Inv_SV, es el conjunto de propiedades que todo dominio especializado, todo agente y toda operación de consulta deben preservar.

### 4.3. Teoremas de invariancia

**Teorema 1 — Conservación del alfabeto.** Todo agente especializado del SV debe cerrar primariamente en Σ o en una estructura de salida explícitamente derivada sobre Σ.

**Teorema 2 — Conservación estructural de célula.** Toda especialización respeta la ley n = b² y las restricciones estructurales de la célula o células que la soportan.

**Teorema 3 — No fabricación de certeza en consulta.** Una consulta no puede producir 0 o 1 fuertes si la cadena relevante de entrada, composición o reevaluación permanece en U no resuelta. Este principio prolonga la regla ya fijada para la cadena de transducción en el Documento IV.

**Teorema 4 — Inmutabilidad de trayectoria bajo consulta de solo lectura.** Toda consulta de lectura preserva la trayectoria previa sin reescritura. La consulta es observación estructurada del estado del sistema; no altera la historia ya constituida.

**Teorema 5 — Monotonía de cobertura bajo ampliación de interfaz.** Sea un dominio fijo D y sea ℐ' una ampliación bien formada de ℐ sobre el mismo dominio. Entonces la U silenciosa no aumenta:

> U_s(D, ℐ') ⊆ U_s(D, ℐ)

Si además se amplía el dominio semántico, la monotonía solo vale bajo una ampliación acoplada de cobertura suficiente.

**Teorema 6 — Preservación de identidad bajo crecimiento.** El crecimiento bien formado de un agente especializado preserva identidad de dominio y trazabilidad histórica, siempre que conserve Inv_SV.

---

## 5. Dominio especializado y agente especializado

### 5.1. Dominio especializado

**Definición 2.** Sea 𝒜 una arquitectura compositiva dada. Un **dominio especializado** sobre 𝒜 es una tupla:

> 𝔇 = (𝒫, ℐ, ℋ, Π_τ, Π_U, Π_C)

donde:

- 𝒫 es un conjunto de instancias de parámetro sobre 𝒜, del tipo (C, j), con C ∈ 𝒜 y 1 ≤ j ≤ n_C;
- ℐ es la interfaz permitida;
- ℋ es el horizonte de sucesos del dominio;
- Π_τ es la política de transducción;
- Π_U es la política de indeterminación;
- Π_C es el criterio de cierre.

El dominio especializado no crea una semántica externa al SV. Tipifica una parte del sistema y declara cómo debe instanciarse sobre una arquitectura dada.

### 5.2. Agente especializado

**Definición 3.** Un **agente especializado** del SV es una tupla:

> A_𝔇 = (𝒜, 𝔇, 𝒬)

donde:

- 𝒜 es la arquitectura compositiva del agente;
- 𝔇 es el dominio especializado que la tipifica;
- 𝒬 es el operador de consulta asociado.

Un agente especializado no es una entidad antropomórfica. Es una configuración SV que sabe evaluar, reevaluar, transducir y responder consultas dentro de su dominio.

### 5.3. Dominios maduros hoy

Los dominios que hoy tienen madurez suficiente para declarar su firma 𝔇 de forma prácticamente completa son:

**Inmunología.**

- 𝒫: instancias de parámetros de IMMUNO-1 e IMMUNO-2 ya fijadas o en continuidad directa con la serie.
- ℐ: interfaz clínico-analítica.
- ℋ: sucesos infecciosos, hematológicos y terapéuticos.
- Π_τ: criterios documentados de transducción clínica.
- Π_U: política de indeterminación explícita.
- Π_C: criterio de cierre del agente inmunológico.

**Neumología.**

- 𝒫: instancias de SV-ADC_L y SV-ADC_V.
- ℐ: interfaz radiológica + clínica.
- ℋ: sucesos neumológicos (detección de nódulo, biopsia, estadificación).
- Π_τ: umbrales de imagen y criterios morfológicos documentados.
- Π_U: resolución guiada por criticidad.
- Π_C: criterio definido por compuerta, criticidad y meta-veto.

### 5.4. Proto-dominios

Los dominios que tienen vocación SV pero cuya firma 𝔇 no está cerrada hoy:

**Genética.**

- 𝒫: parámetros de SV-GEN_L en fase de definición.
- ℐ: interfaz genómica.
- Estado: fase I acotada; ℋ, Π_τ, Π_U y Π_C siguen en discusión.
- Hoja de ruta: crecimiento por fases.

Un proto-dominio no es exterior al SV. Es un dominio que ha comenzado su instanciación pero aún no puede declarar 𝔇 completa.

### 5.5. Proposición de unidad de marco

Dominios distintos pertenecen al mismo SV si preservan Inv_SV. La especialización diferencia semántica de parámetros, transductores, horizonte y políticas, pero no la estructura algebraica subyacente.

Inmunología y neumología son hoy instanciaciones maduras del mismo sistema. Genética constituye hoy una proto-instanciación del mismo marco.

### 5.6. Composición entre agentes

La composición entre agentes de dominios distintos se admite solo bajo relación semántica declarada R(𝒜) y con interfaces compatibles. No se componen agentes «porque sí». Se componen cuando la relación semántica entre sus dominios lo justifica y cuando los invariantes se preservan.

---

## 6. Operador de consulta

### 6.1. Principio

Consultar el SV no es «preguntar a un modelo». Es activar algebraicamente una región pertinente de una arquitectura especializada bajo una firma de consulta, y obtener una respuesta trazable con justificación y metadatos.

### 6.2. Firma de consulta

**Definición 4.** Una **firma de consulta** es una tupla:

> ω = (tipo, alcance, restricciones)

donde:

- tipo: clase de consulta (evaluación puntual, estado de trayectoria, comparación entre frames, estado de cobertura, listado de U pendientes, criticidad global);
- alcance: región de la arquitectura que la consulta activa;
- restricciones: condiciones adicionales declaradas.

### 6.3. Definición del operador

**Definición 5.** Sea A_𝔇 un agente especializado y sₙ su estado actual. El **operador de consulta** es una función:

> 𝒬_ω(A_𝔇, sₙ) = (r, J, M)

donde:

- r: respuesta, perteneciente a una estructura de salida tipada y derivada sobre Σ; el lenguaje del dominio es la presentación semántica de r, no un alfabeto autónomo.
- J: justificación, cadena trazable que conecta r con valores, reglas y trayectorias.
- M: metadatos, incluyendo criticidad, cobertura de interfaz, U pendientes y estado de admisibilidad de los transductores relevantes.

### 6.4. Condiciones de buena formación de la consulta

**CQ1 — Trazabilidad.** Toda respuesta debe venir acompañada de J reconstruible.

**CQ2 — No opacidad.** J no puede contener pasos opacos ni inferencia estadística no declarada.

**CQ3 — No reescritura.** La consulta no modifica la trayectoria T.

**CQ4 — Dependencia de cobertura.** La respuesta declara explícitamente de qué porción de la interfaz depende.

**CQ5 — Consistencia con trayectoria.** La consulta no puede contradecir el estado del sistema sin una regla explícita de reconciliación.

**CQ6 — Gestión de U y criticidad.** Toda consulta debe declarar la criticidad y las U que afectan a su cierre.

### 6.5. Proposiciones del operador de consulta

**Proposición 1 — Consulta trazable.** Toda respuesta de consulta debe venir acompañada de una justificación reconstruible.

**Proposición 2 — Consistencia con trayectoria.** La consulta debe ser compatible con la trayectoria ya constituida del sistema.

**Proposición 3 — No conclusión fuerte bajo cobertura insuficiente.** Si la cobertura relevante es insuficiente, la respuesta debe degradarse conforme a la política de U del dominio.

---

## 7. Límites de cierre

Quedan fuera del Documento V como cierre fuerte:

- operador de entrenamiento;
- neurología como dominio formalmente instanciado;
- análisis discreto de trayectorias, funciones generatrices y herramientas de secuencias del sistema;
- álgebra lineal del grafo de composición;
- representaciones y cambios de codificación;
- humanoides como arquitectura encarnada;
- aprendizaje estadístico;
- teoría multiagente plena.

---

## 8. Líneas futuras

### 8.1. Neurología

Como dominio estratégico futuro, una vez existan parámetros, interfaz, transductores y políticas suficientes para declarar una firma 𝔇 madura.

### 8.2. Operador de entrenamiento

Como derivación futura del operador de consulta y de la estructura de trayectorias.

### 8.3. Compatibilidad futura con humanoides

Como condición de borde del sistema, no como núcleo actual.

### 8.4. Documento VI

El Documento VI abordará el análisis matemático propio del SV en el dominio discreto: análisis de trayectorias mediante diferencias finitas y criterios de estabilización, funciones generatrices del espacio combinatorio, transformada Z de secuencias canónicas del sistema, álgebra lineal del grafo de composición y representaciones con invariantes preservados. Lo hará sobre la base funcional ya cerrada por el Documento V, no en lugar de ella. El cálculo clásico (derivadas, integrales, variable compleja, residuos, Laplace) queda como horizonte condicionado a la existencia futura de un puente formal entre el dominio discreto y el continuo.

---

## 9. Conclusión

El marco SV queda extendido con un nivel funcional superior que formaliza cómo el sistema puede especializarse y ser consultado sin perder su identidad.

La especialización se formaliza mediante el dominio 𝔇 = (𝒫, ℐ, ℋ, Π_τ, Π_U, Π_C) sobre una arquitectura dada 𝒜. El agente se formaliza como A_𝔇 = (𝒜, 𝔇, 𝒬). La consulta se formaliza mediante el operador 𝒬_ω con salida (r, J, M). Seis teoremas de invariancia garantizan que nada de esto destruye la identidad algebraica del sistema. Tres proposiciones del operador de consulta garantizan que la respuesta es trazable, coherente con la trayectoria y honesta con la incertidumbre.

Con los cinco documentos, el SV tiene: célula (Fundamentos), composición (I, II), evolución (III), entrada del mundo (IV) y uso (V). La maquinaria está construida. El modo de empleo está formalizado. Lo que viene después — análisis discreto, nuevos dominios, entrenamiento, humanoides — se construye sobre esta base, no al lado de ella.

Este documento hereda de los cinco pilares que lo preceden y no tendría sentido sin ellos. Cierra el primer nivel funcional del SV. No cierra el SV.

---

## Referencias

[R1] Juan Antonio Lloret Egea. *Fundamentos algebraico-semánticos del Sistema Vectorial SV.* v1.0.0, Release 3. ITVIA, 2026.
https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

[R2] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — I. Transmisión en serie por parámetro puente.* v1, Release 4. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv/release/4

[R3] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — II. Gramática general de composición.* v1.0, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--ii-gramatica-general-de-composicion/release/1

[R4] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta.* v1, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iii-horizonte-de-sucesos-y-reevaluacion-discreta/release/1

[R5] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema.* v1, Release 1. ITVIA, 2026.
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iv-transduccion-al-alfabeto-ternario-e-interfaz-parametrica-del-sistema/release/1

[R6] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

---

## Apéndice breve de notación

| Símbolo | Significado |
|---------|------------|
| 𝔇 | Dominio especializado |
| A_𝔇 | Agente especializado |
| 𝒬_ω | Operador de consulta |
| ω | Firma de consulta |
| (r, J, M) | Respuesta, justificación, metadatos |
| Inv_SV | Familia de invariantes |
| Π_τ | Política de transducción |
| Π_U | Política de indeterminación |
| Π_C | Criterio de cierre |

---

*Documento doctrinal del Sistema Vectorial SV. ISSN 2695-6411.*
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
