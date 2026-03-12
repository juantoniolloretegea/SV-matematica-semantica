<!-- Publicado en PubPub: https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iv-transduccion-al-alfabeto-ternario-e-interfaz-parametrica-del-sistema/release/1 -->

# Álgebra de composición intercelular del marco SV

## IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema

### Extensión algebraica del marco SV para la entrada auditable de magnitudes no nativas

**Autor:** Juan Antonio Lloret Egea

**ORCID:** 0000-0002-6634-3351

**Versión:** 1

**Lugar y fecha:** Madrid, 11/03/2026

**Estado:** Documento doctrinal publicado

CC BY-NC-ND 4.0 · ISSN 2695-6411

> *Su padre es la inteligencia humana que diseña la interfaz.*
> *Su madre es el álgebra que garantiza que lo diseñado es exacto, auditable y no miente.*

---

## Resumen

Este documento extiende el Sistema Vectorial SV con una capa formal de transducción que especifica cómo magnitudes no nativas del alfabeto ternario ingresan en el sistema de forma auditable. Su objeto es el eslabón que los Documentos I, II y III presuponen pero no formalizan: la conversión del mundo exterior en valores de Σ = {0, 1, U}.

El documento introduce siete primitivos formales: el dominio observacional tipado Wⱼ, el sensor ϕⱼ como función de captura a codominio ampliado Oⱼ^⊥, el espacio observacional Oⱼ, el estado de admisibilidad rⱼ ∈ R, el transductor τⱼ como función de ternarización, la interfaz paramétrica ℐ(𝒜) con máscara de exogeneidad E(C) y ley de crecimiento, y la U silenciosa U_s como límite estructural de la interfaz.

Sobre esta base se establecen cinco proposiciones nucleares: determinismo de la transducción, propagación conservadora de la inadmisibilidad, acotación de los patrones de transición ternaria, no fabricación de certeza en la cadena y monotonía de reducción de la U silenciosa.

---

## 1. Objeto y alcance

### 1.1. Tesis central

El Sistema Vectorial SV opera exclusivamente con Σ = {0, 1, U}. El mundo no habla ternario. Entre el mundo y el sistema existe una cadena formal de captura, admisibilidad y ternarización que este documento formaliza. Sin esa cadena, los Documentos I, II y III permanecen como una gramática exacta sobre valores ya legibles. Con ella, el SV puede hacer algebraicamente tratable una porción expuesta del mundo.

### 1.2. Qué hace este documento

Este documento extiende el álgebra del SV con una capa de transducción que formaliza la entrada auditable de magnitudes al sistema. Define:

1. Wⱼ: dominio observacional tipado del mundo para cada parámetro.
2. ϕⱼ : Wⱼ → Oⱼ^⊥: sensor o procedimiento de captura, con fallo explícito.
3. Oⱼ: espacio de objetos observacionales válidos.
4. R = {ok, degradado, fallido, U}: conjunto de estados de admisibilidad observacional.
5. τⱼ : Oⱼ → Σ: transductor o función de ternarización.
6. ℐ(𝒜), con E(C): interfaz paramétrica con máscara de exogeneidad y ley de crecimiento.
7. U_s: U silenciosa, entendida como límite estructural de la interfaz.

### 1.3. Qué no hace este documento

Este documento no:

- formaliza actuadores o la salida del sistema hacia el mundo;
- formaliza la capa de humanoide como agente autónomo;
- introduce predicción, estadística, modelado continuo ni minería de datos;
- cierra la interfaz expandible en ejecución.

### 1.4. Relación con los documentos anteriores

El Documento I formalizó la transmisión entre células. El Documento II fijó la gramática general de composición. El Documento III formalizó el horizonte de sucesos, la reevaluación discreta y la trayectoria. Los tres presuponen que los valores ternarios ya están dentro del sistema. El Documento IV formaliza cómo llegan.

La cadena mínima queda así:

> x ∈ Wⱼ → ϕⱼ → oⱼ ∈ Oⱼ^⊥ → rⱼ ∈ R → τⱼ → σ ∈ Σ → Pⱼ → célula → composición → frame → trayectoria

No hay hueco en la cadena formal mínima que cubre la porción del mundo efectivamente expuesta y tipada por la interfaz. Cada eslabón tiene un objeto formal. Lo que queda fuera de la interfaz es U silenciosa.

### 1.5. Estatuto del documento

Este documento no cierra la ingeniería de transductores. Fija su base algebraica. Dice qué es un transductor formalmente, qué propiedades mínimas debe cumplir, cómo se organiza la interfaz y qué permanece fuera de ella. La construcción concreta de sensores, protocolos, umbrales o criterios expertos pertenece al trabajo de dominio que se levanta sobre esta especificación.

---

## 2. Subordinación doctrinal y deuda con la serie

Este documento es doctrina derivada de segundo nivel. La autoridad normativa suprema del Sistema Vectorial SV reside en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. Todo lo que aquí se establece debe ser coherente con dicho documento. En caso de discrepancia, prevalecen los *Fundamentos*.

### Lo que este documento hereda

El Documento IV nace de cuatro piezas previas:

- Los **Fundamentos** fijaron Σ = {0, 1, U}, la célula exacta, la restricción n = b², el umbral T(n), la función de evaluación χᵢ, la familia ℱ_SV, la primacía humana y la exclusión de la probabilidad opaca.
- El **Documento I** formalizó la transmisión en serie entre células acopladas.
- El **Documento II** elevó ese resultado a gramática general de composición.
- El **Documento III** formalizó horizonte de sucesos, frame canónico, dato de transición, operador inducido y trayectoria.

El Documento IV añade la pieza que todos ellos presuponen: cómo una magnitud del mundo llega a adquirir estatuto algebraico legítimo dentro del SV.

### Apoyos explícitos

- **Fundamentos §2:** Σ = {0, 1, U} como alfabeto canónico.
- **Fundamentos §9:** exclusión de la probabilidad opaca.
- **Guía §13:** umbralización de variables continuas como caso de referencia de τⱼ.
- **Guía §14:** niveles de madurez de la interfaz biológico-algebraica.
- **Documento III §4:** el horizonte ℋ(𝒜) como conjunto de sucesos declarados; el Documento IV formaliza cómo magnitudes externas llegan a ser sucesos legibles para ese horizonte.

---

## 3. Tabla de notación

### Símbolos heredados

Todos los símbolos de Fundamentos y de los Documentos I, II y III permanecen vigentes.

### Símbolos introducidos en este documento

| Símbolo | Significado | Estatuto |
|---------|------------|----------|
| Wⱼ | Dominio observacional del mundo para el parámetro Pⱼ | Definición |
| ϕⱼ : Wⱼ → Oⱼ^⊥ | Sensor o procedimiento de captura | Definición |
| Oⱼ | Espacio de objetos observacionales válidos | Definición |
| Oⱼ^⊥ = Oⱼ ∪ {⊥} | Espacio observacional ampliado | Definición |
| R = {ok, degradado, fallido, U} | Estados de admisibilidad observacional | Definición |
| rⱼ ∈ R | Estado de admisibilidad de una observación concreta | Definición |
| τⱼ : Oⱼ → Σ | Transductor o función de ternarización | Definición |
| B₀, B₁, B_U | Partición del dominio del transductor | Definición |
| E(C) ⊆ {1, …, n} | Máscara de exogeneidad de la célula C | Definición |
| ℐ(𝒜) | Interfaz paramétrica de la arquitectura | Definición |
| ℐ^exo(𝒜) | Conjunto de instancias exógenas (C, j) | Definición |
| U_s(𝒜) | U silenciosa | Definición |

### Separación entre ϕⱼ y τⱼ

ϕⱼ captura. τⱼ decide. Son funciones distintas. ϕⱼ va del mundo al espacio observacional ampliado; τⱼ va del espacio observacional válido a Σ. Medir no es clasificar.

---

## 4. La cadena de transducción

### 4.1. Estructura completa

La entrada de una magnitud del mundo al sistema SV sigue esta cadena formal:

> x ∈ Wⱼ → ϕⱼ(x) ∈ Oⱼ^⊥ → rⱼ ∈ R → [oⱼ ∈ Oⱼ] → τⱼ(oⱼ) ∈ Σ → Pⱼ → célula

Si ϕⱼ(x) = ⊥, la cadena se corta y Pⱼ recibe U directamente. Si ϕⱼ(x) = oⱼ ∈ Oⱼ pero la admisibilidad no es suficiente, la regla conservadora gobierna el resultado. Solo si oⱼ ∈ Oⱼ y rⱼ = ok, el transductor se ejecuta sin restricción.

### 4.2. Wⱼ — Dominio observacional tipado

Cada parámetro Pⱼ tiene un dominio observacional propio:

> Wⱼ ⊆ W

donde W es un dominio ambiente y Wⱼ el subdominio relevante para ese parámetro. El tipado es obligatorio. No es lo mismo el dominio de magnitudes hematológicas que el de magnitudes radiológicas o genómicas.

Los dominios Wⱼ pueden solaparse, pero cada parámetro tiene su propio sensor, su propio espacio observacional y su propio transductor.

### 4.3. ϕⱼ — Sensor o procedimiento de captura

**Definición 1.** Sea Pⱼ un parámetro con exposición exógena. El sensor asociado a Pⱼ es una función de captura a codominio ampliado:

> ϕⱼ : Wⱼ → Oⱼ^⊥

donde Oⱼ^⊥ = Oⱼ ∪ {⊥}.

Si la captura produce un objeto observacional válido, ϕⱼ(x) = oⱼ ∈ Oⱼ. Si la captura falla, ϕⱼ(x) = ⊥.

La ampliación del codominio con ⊥ resuelve de forma limpia la posibilidad de fallo sin volver parcial la función. ϕⱼ es total sobre Wⱼ: siempre produce o bien un objeto observacional, o bien ⊥.

El sensor puede ser instrumental, procedimental o humano. Lo esencial es que produzca un objeto observacional documentable o declare formalmente que no pudo producirlo.

### 4.4. Oⱼ — Espacio observacional

Oⱼ es el espacio de objetos observacionales válidos que ϕⱼ puede producir para el parámetro Pⱼ. Puede ser numérico, categorial o estructurado.

Lo que Oⱼ no puede ser es Σ directamente. El paso de Oⱼ a Σ es la tarea del transductor.

### 4.5. rⱼ — Admisibilidad observacional

**Definición 2.** El estado de admisibilidad de una observación es un valor

> rⱼ ∈ R = {ok, degradado, fallido, U}

Si ϕⱼ(x) = ⊥, entonces rⱼ = fallido automáticamente. Si ϕⱼ(x) = oⱼ ∈ Oⱼ, entonces rⱼ se determina por la calidad del proceso de captura.

- **ok:** la observación es admisible.
- **degradado:** la observación es utilizable solo bajo política previa documentada.
- **fallido:** no existe observación utilizable.
- **U:** no puede cerrarse la calidad de la captura.

R no es Σ. R califica el proceso observacional; Σ califica el valor algebraizado.

### 4.6. Regla conservadora de admisibilidad

- Si ϕⱼ(x) = ⊥ o rⱼ = fallido, el transductor no se ejecuta y Pⱼ = U.
- Si rⱼ = U, cualquier resultado queda degradado a U, salvo regla de cierre conservador documentada ex ante.
- Si rⱼ = degradado, la política de tratamiento debe estar declarada ex ante en la especificación del transductor o del dominio. Las opciones admisibles son: aceptación bajo metadato de calidad inferior; degradación automática a U; regla conservadora documentada.
- Si rⱼ = ok, el transductor se ejecuta sin restricción.

---

## 5. El transductor

### 5.1. Principio

El transductor recibe un objeto observacional y produce un valor ternario. Es el punto en que una observación pasa a ser legible para el álgebra del SV.

### 5.2. Definición

**Definición 3.** Sea Oⱼ el espacio observacional del parámetro Pⱼ. El transductor es una función

> τⱼ : Oⱼ → Σ

definida mediante una partición de Oⱼ en tres regiones disjuntas: B₀ ∪ B₁ ∪ B_U = Oⱼ.

- τⱼ(oⱼ) = 0 si oⱼ ∈ B₀
- τⱼ(oⱼ) = 1 si oⱼ ∈ B₁
- τⱼ(oⱼ) = U si oⱼ ∈ B_U

### 5.3. Condiciones de buena formación del transductor

**CT1 — Completitud.** Para todo oⱼ ∈ Oⱼ, τⱼ(oⱼ) está definido.

**CT2 — Determinismo.** Para todo oⱼ ∈ Oⱼ, τⱼ(oⱼ) produce exactamente un valor de Σ.

**CT3 — Criterio de partición documentado.** La definición de B₀, B₁, B_U debe ser explícita y auditable.

**CT4 — Semántica declarada.** El significado de 0, 1, U para el parámetro receptor debe constar antes de la ejecución.

**CT5 — Independencia.** El transductor no conoce el resultado de la evaluación de la célula; solo conoce la observación de entrada.

### 5.4. Transducción por juicio humano

En algunos dominios, el transductor no es código ni umbral numérico, sino juicio experto aplicado sobre un objeto observacional estructurado. En ese caso siguen vigentes CT1–CT5. La diferencia es que la auditabilidad de la transducción depende de un criterio experto documentado y debe quedar acompañada de metadato de calidad.

### 5.5. Escalado del transductor con la célula

La restricción arquitectónica del SV es n = b², con b ≥ 3. El número de transductores exógenos de una célula no puede exceder n. Una SV(9,3) admite a lo sumo nueve transductores; una SV(25,5), a lo sumo veinticinco.

El escalado de la percepción sigue la misma ley que el escalado de la evaluación. El sistema no añade ventanas al mundo al margen del crecimiento de su propia célula.

---

## 6. La interfaz paramétrica

### 6.1. Máscara de exogeneidad

**Definición 4.** Sea C una célula SV(n, b) con parámetros P₁, …, Pₙ. La máscara de exogeneidad es el subconjunto

> E(C) ⊆ {1, …, n}

que declara qué parámetros tienen exposición al mundo exterior y cuáles son puramente endógenos.

Si j ∈ E(C), Pⱼ admite transductor exógeno. Si j ∉ E(C), su valor se determina por composición interna.

### 6.2. Interfaz paramétrica

**Definición 5.** Sea 𝒜 una arquitectura compositiva. Su interfaz paramétrica es el conjunto

> ℐ(𝒜) = { (C, j, ϕⱼ, τⱼ, eⱼ) : C ∈ 𝒜, j ∈ E(C), eⱼ = exo }

Cada elemento identifica una instancia exógena concreta de parámetro dentro de una célula concreta.

### 6.3. Interfaz exógena total canónica

**Definición 6.** Una célula C tiene interfaz exógena total canónica cuando E(C) = {1, …, n}. En ese caso, todos sus parámetros tienen exposición exógena.

### 6.4. Interfaz exógena parcial

Cuando E(C) ⊊ {1, …, n}, la interfaz es parcial. Esto es legítimo y frecuente. Los parámetros fuera de E(C) son endógenos y deben quedar declarados como tales en la especificación de la célula.

### 6.5. Ley de crecimiento de la interfaz

**LC1 — Techo de exposición.** Para una célula SV(n, b), |E(C)| ≤ n.

**LC2 — Crecimiento por escalado celular.** El paso a una célula mayor SV(n', b') con n' > n puede ampliar la interfaz exógena dentro del nuevo techo n'.

**LC3 — Preservación de identidad.** Al escalar la interfaz debe declararse qué parámetros heredados conservan exposición exógena, cuáles cambian de estatuto y cuáles parámetros nuevos se abren al mundo.

**LC4 — Inmutabilidad de la trayectoria previa.** Ampliar la interfaz no reescribe la trayectoria ya existente. Solo cambia la cobertura futura del sistema.

### 6.6. Proposición 1 — Determinismo de la transducción

Si τⱼ satisface CT1 y CT2, rⱼ = ok y oⱼ está determinado, entonces τⱼ(oⱼ) ∈ Σ es determinista.

### 6.7. Proposición 2 — Propagación conservadora de la inadmisibilidad

Si rⱼ ∈ {fallido, U}, entonces Pⱼ = U.

La causa puede ser distinta — fallo de captura o incertidumbre de calidad — pero el tratamiento algebraico es el mismo: el sistema no fabrica certeza donde la cadena de entrada no la tiene.

### 6.8. Proposición 3 — Acotación de los patrones de transición ternaria

Sea

> ℐ^exo(𝒜) = { (C, j) : C ∈ 𝒜, j ∈ E(C) }

El número de patrones elementales de transición ternaria inducibles por la interfaz exógena está acotado por

> Σ_{C ∈ 𝒜} |E(C)| × 6

donde 6 es el número de transiciones elementales posibles por parámetro ternario: 0→1, 0→U, 1→0, 1→U, U→0, U→1.

Esta proposición acota efectos sobre Σ, no causas sobre W.

---

## 7. No fabricación de certeza

### 7.1. Principio

La cadena de transducción no fabrica certeza. Si un eslabón de la cadena es inadmisible o indeterminado, el sistema no puede producir 0 ni 1 sin una regla explícita de cierre conservador documentada ex ante.

### 7.2. Proposición 4 — No fabricación de certeza en la cadena

Sea la cadena completa para el parámetro Pⱼ:

> x ∈ Wⱼ → ϕⱼ(x) ∈ Oⱼ^⊥ → rⱼ ∈ R → τⱼ(oⱼ) ∈ Σ → Pⱼ

Si se cumple alguna de estas condiciones:

- ϕⱼ no produjo observación utilizable;
- rⱼ ∈ {fallido, U};
- oⱼ ∈ B_U;

entonces Pⱼ = U, salvo que exista una regla de cierre conservador documentada ex ante que justifique otra asignación.

---

## 8. La U silenciosa

### 8.1. Definición

**Definición 7.** Sea D el conjunto de clases de magnitud relevantes para un dominio y sea Cov(ℐ(𝒜)) la cobertura real de la interfaz paramétrica. La U silenciosa es

> U_s(𝒜) = D \ Cov(ℐ(𝒜))

### 8.2. Naturaleza

La U silenciosa no es un error del sistema. Es un límite estructural de toda interfaz finita. Lo que el sistema no parametriza no puede hacerlo legible para sí mismo.

### 8.3. Proposición 5 — Monotonía de reducción

Si se amplía la interfaz paramétrica añadiendo nuevos transductores, entonces

> U_s(𝒜, ℐ') ⊆ U_s(𝒜, ℐ)

Ampliar la interfaz no aumenta la U silenciosa: la reduce o la mantiene.

### 8.4. No eliminación necesaria

En dominios abiertos o no completamente conocibles, una ampliación finita de la interfaz no garantiza la eliminación total de U_s. Siempre queda un resto fuera de la ventana formal del sistema.

---

## 9. Casos internos del proyecto

| Dominio | Wⱼ | Sensor ϕⱼ | Oⱼ | Admisibilidad | τⱼ | Criterio | Parámetro |
|---------|-----|-----------|-----|---------------|-----|----------|-----------|
| Inmunología | Neutrófilos/μL | Hemograma | ℝ⁺ | laboratorio válido | umbrales | numérico | P01 |
| Inmunología | Estado esplénico | Ecografía + exploración | categorial | variable | juicio clínico | protocolo | P04 |
| Neumología | Tamaño nódulo | TC torácica | mm | equipo válido | umbral | numérico | L11 |
| Neumología | Captación PET | PET/TC | SUV | equipo válido | umbral institucional | numérico | L21 |
| Neumología | Espiculación | Imagen TC | patrón morfológico | depende de imagen | criterio radiológico | morfológico | L12 |
| Genética | Variante genómica | Panel NGS | variante + clasificación | panel válido | patogenicidad | base + experto | sector GEN |

### Ejemplo completo: inmunología, P01

- W₁: concentración de neutrófilos en sangre periférica.
- ϕ₁: hemograma automatizado con recuento diferencial.
- O₁ = ℝ⁺.
- r₁ = ok si el laboratorio y la muestra cumplen el protocolo.
- τ₁: B₀ = {x > 1500}, B₁ = {x < 500}, B_U = {500 ≤ x ≤ 1500}.
- Resultado: P01 ∈ Σ.

### Ejemplo de interfaz parcial: IMMUNO-2

IMMUNO-2 tiene 25 parámetros. P25 es puente endógeno. Por tanto, E(IMMUNO-2) = {1, …, 24}. La interfaz exógena tiene 24 transductores. P25 no tiene transductor exógeno.

---

## 10. Proposiciones nucleares (resumen)

1. **Determinismo de la transducción.** Si τⱼ está bien formado, rⱼ = ok y oⱼ está determinado, τⱼ(oⱼ) es determinista.
2. **Propagación conservadora de la inadmisibilidad.** Si rⱼ ∈ {fallido, U}, entonces Pⱼ = U.
3. **Acotación de patrones de transición ternaria.** Σ_{C ∈ 𝒜} |E(C)| × 6 acota patrones elementales de efecto en Σ.
4. **No fabricación de certeza.** Un eslabón inadmisible o indeterminado obliga a U, salvo regla conservadora ex ante.
5. **Monotonía de la U silenciosa.** Ampliar la interfaz no aumenta U_s.

---

## 11. Límites de cierre

Quedan fuera del cierre actual:

- una axiomática completa de transductores bien formados;
- una métrica cuantitativa de cobertura para U_s;
- la interfaz expandible en ejecución;
- la composición formal de transductores;
- los actuadores;
- un criterio general de dimensionamiento suficiente de la interfaz;
- la formalización de latencias de captura.

---

## 12. Líneas futuras

1. Axiomática más rica de transductores.
2. Composición de transductores para observaciones concurrentes.
3. Interfaz expandible bajo preservación de trayectoria.
4. Métrica de cobertura del dominio.
5. Actuadores y cadena inversa Σ → mundo.
6. Desarrollo de interfaces para humanoides bajo escalado b².

---

## 13. Conclusión

El marco SV queda extendido con una capa de transducción que formaliza la entrada auditable de magnitudes del mundo al sistema.

La cadena es esta: una magnitud x ∈ Wⱼ llega a un sensor ϕⱼ, que produce un objeto observacional o declara fallo; el estado de admisibilidad rⱼ califica la captura; si la observación es utilizable, el transductor τⱼ aplica un criterio de partición documentado y produce σ ∈ Σ; ese valor alimenta un parámetro Pⱼ; y la maquinaria de los Documentos I, II y III se activa.

Lo que queda fuera de la interfaz es U silenciosa. Ampliar la interfaz la reduce; no la elimina necesariamente. La calidad del sistema depende de la solidez de su álgebra y de la calidad formal de su interfaz.

Con los cuatro documentos, la cadena formal mínima del SV cubre la porción del mundo efectivamente expuesta y tipada por la interfaz, desde la magnitud hasta la trayectoria auditable. La cadena no fabrica certeza: si un eslabón es inadmisible, el resultado es U.

Este documento no es un cierre terminal. Es el embrión formal de la puerta de entrada del mundo al SV. Nace sabiendo qué es, qué se espera de él y cómo puede crecer bajo la misma disciplina algebraica que gobierna la célula.

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

[R5] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

---

## Apéndice breve de notación

| Símbolo | Significado |
|---------|------------|
| Wⱼ | Dominio observacional tipado |
| ϕⱼ | Sensor o procedimiento de captura |
| Oⱼ | Espacio observacional válido |
| Oⱼ^⊥ | Espacio observacional ampliado |
| R | Estados de admisibilidad |
| τⱼ | Transductor |
| E(C) | Máscara de exogeneidad |
| ℐ(𝒜) | Interfaz paramétrica |
| U_s(𝒜) | U silenciosa |

---

## Ejemplo mínimo de la cadena

    Dominio tipado:     W₁ = concentraciones hematológicas (ℝ⁺)
    Magnitud:           x = 320 neutrófilos/μL
    Sensor:             ϕ₁(x) = o₁ = 320 ∈ O₁
    Admisibilidad:      r₁ = ok
    Transductor:        τ₁(320) → B₁ → σ = 1
    Parámetro:          P01 = 1
    Célula:             IMMUNO-1 reevalúa con P01 = 1
    Composición:        el puente actualiza el parámetro receptor
    Frame:              Sₙ₊₁ = ℰ(𝒜, Pₙ₊₁)
    Trayectoria:        T = (…, νₙ, Sₙ₊₁)

---

*Documento doctrinal del Sistema Vectorial SV. ISSN 2695-6411.*
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
