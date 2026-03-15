# Álgebra de composición intercelular del marco SV  
## III. Horizonte de sucesos y reevaluación discreta

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Versión:** 1  
**Lugar y fecha:** Madrid, 11/03/2026  
**Estado:** Documento doctrinal publicado  
CC BY-NC-ND 4.0 · ISSN 2695-6411

> [!NOTE]
> La Release 2 publicada de este documento incorpora una demostración audiovisual complementaria, accesible en la <a href="https://juantoniolloretegea.github.io/SV-matematica-semantica/documento-iii/" target="_blank" rel="noopener noreferrer">página web auxiliar del Documento III</a>.

---

## Resumen

Este documento extiende el Sistema Vectorial SV con una capa formal de reevaluación discreta subordinada a la gramática espacial ya fijada en los *Fundamentos* y en los Documentos I y II.

Su objeto no es el tiempo como primitivo del sistema, sino la sucesión ordenada de reevaluaciones desencadenadas por sucesos declarados pertenecientes al horizonte propio de una arquitectura compositiva. El documento introduce seis primitivos formales: el horizonte de sucesos ℋ(𝒜), el frame canónico Sₙ, el dato de transición νₙ, el operador inducido 𝒰_{νₙ}, la trayectoria T y la relación general de cambio de criticidad δ_Γ.

Sobre esta base se establecen tres proposiciones nucleares: inmutabilidad del frame, reproducibilidad de la trayectoria bajo condiciones de cierre suficiente y acotación de cascada en régimen simple. La pieza no formaliza la transducción de magnitudes no nativas al alfabeto ternario. Esa cuestión queda reservada al Documento IV.

---

## 1. Objeto y alcance

### 1.1. Tesis central

El Sistema Vectorial SV evoluciona por **sucesos**, no por tiempo.

Un sistema de células acopladas se reevalúa cuando uno o varios sucesos pertenecientes a su horizonte propio presentan incidencia, ausencia verificada o indeterminación. La sucesión ordenada de esas reevaluaciones constituye la trayectoria del sistema.

### 1.2. Qué hace este documento

Este documento formaliza la reevaluación discreta de una arquitectura compositiva ya definida en el marco SV.

Para ello:
- declara el horizonte de sucesos relevante de la arquitectura;
- define el frame canónico como evaluación completa del sistema tras sucesos pertinentes;
- separa el dato de transición del operador que actualiza parámetros;
- organiza la trayectoria como secuencia *append-only* de reevaluaciones;
- y expresa el cambio de criticidad mediante una relación general entre frames.

### 1.3. Qué no hace este documento

Este documento no:
- formaliza la transducción de señales continuas al alfabeto ternario;
- introduce estadística, minería de datos o aprendizaje opaco como fundamento del sistema;
- define una norma general de convergencia de trayectorias;
- ni desarrolla todavía ciclos de reevaluación controlados con cierre completo.

### 1.4. El tiempo como medida y metadato

En el marco SV, el tiempo no comparece como primitivo ontológico ni como causa del cambio.

Puede intervenir únicamente como instrumento de medida o como metadato de auditoría para registrar intervalos entre reevaluaciones. La medida acompaña al suceso; no lo funda ni lo reorganiza por sí misma.

---

## 2. Posición del Documento III en la serie

Este documento constituye la tercera pieza de la teoría compositiva del marco SV. El Documento I formalizó la transmisión en serie por parámetro puente. El Documento II elevó ese resultado a una gramática general de composición.

El presente Documento III añade una capa nueva: la reevaluación discreta del sistema cuando se instancian sucesos relevantes ya legibles dentro del alfabeto ternario.

---

## 3. Primitivos formales

### 3.1. Arquitectura compositiva

Sea una arquitectura compositiva 𝒜 del marco SV, ya definida por los objetos heredados de los *Fundamentos* y de los Documentos I y II.

### 3.2. Horizonte de sucesos

Se define el horizonte de sucesos de la arquitectura como

> ℋ(𝒜) = {ε₁, ε₂, …, εₘ}

donde cada εᵢ es un tipo de suceso relevante declarado formalmente para la reevaluación del sistema.

El horizonte no se infiere por probabilidad ni por minería de datos. Se declara de manera explícita desde el dominio.

### 3.3. Alfabeto ternario

Todo suceso instanciado se expresa en el alfabeto

> Σ = {0, 1, U}

con la interpretación siguiente:
- 1: consta su incidencia;
- 0: consta su no incidencia conforme al protocolo de observación del dominio;
- U: el sistema no puede cerrar su estado de forma suficiente.

### 3.4. Frame canónico

Se define el frame canónico Sₙ como la evaluación completa del sistema tras la incidencia, ausencia verificada o indeterminación de sucesos pertinentes del horizonte:

> Sₙ = ℰ(𝒜, Pₙ)

donde ℰ es la evaluación espacial heredada y Pₙ el estado paramétrico actualizado del sistema.

El índice n es ordinal de secuencia. No representa una coordenada temporal fuerte.

### 3.5. Dato de transición

El dato de transición νₙ registra los sucesos instanciados que motivan la reevaluación entre Sₙ y Sₙ₊₁.

Una forma mínima de expresarlo es:

> νₙ = {(εᵢ, τᵢ)}_{i ∈ Iₙ} , τᵢ ∈ Σ

El dato puede incorporar, además, la lista constitutiva de parámetros modificados y los metadatos de auditoría pertinentes.

### 3.6. Operador inducido

A cada dato de transición suficientemente determinado le corresponde un operador inducido

> 𝒰_{νₙ}

que actúa sobre el estado paramétrico del sistema y produce la actualización necesaria para una nueva evaluación.

### 3.7. Trayectoria

La trayectoria del sistema es la secuencia ordenada

> T = (S₁, ν₁, S₂, ν₂, …, Sₙ)

con crecimiento por adición, sin reescritura retrospectiva.

### 3.8. Cambio de criticidad

El cambio de criticidad entre dos frames consecutivos se expresa mediante una relación general

> δ_Γ(Sₙ, Sₙ₊₁)

sin presuponer que toda función de criticidad del dominio admita resta aritmética.

---

## 4. Estructura del horizonte de sucesos

### 4.1. Declaración formal

El horizonte de sucesos pertenece al diseño del sistema. No es un residuo empírico ni una colección estadística de episodios observados.

### 4.2. Relevancia de dominio

Un suceso forma parte de ℋ(𝒜) si su incidencia, ausencia o indeterminación puede afectar de forma pertinente a la reevaluación del sistema.

### 4.3. Ejemplo abstracto

En una arquitectura técnica, el horizonte puede contener sucesos como pérdida de suministro, rotura de componente, degradación de material o fallo de enlace.

En una arquitectura clínica, puede contener resultados de prueba, cambios sintomáticos, eventos terapéuticos o aparición de signos de alarma. Lo relevante no es el dominio concreto, sino que los sucesos estén declarados de forma formal y evaluable.

---

## 5. Proposiciones nucleares

### 5.1. Proposición 1 — Inmutabilidad del frame

Una vez construido, un frame pasado no puede ser modificado por operaciones posteriores del sistema.

**Consecuencia:** la trayectoria conserva trazabilidad completa y no admite reescritura retrospectiva.

### 5.2. Proposición 2 — Reproducibilidad de la trayectoria

Dado un frame inicial S₁ y una secuencia de datos de transición con contenido constitutivo suficiente para determinar cada operador inducido 𝒰_{νₙ}, todo frame posterior de la trayectoria es recalculable de forma determinista.

**Observación:** los casos con indeterminación no cerrada pueden quedar fuera de este cierre fuerte.

### 5.3. Proposición 3 — Acotación de cascada en régimen simple

En un grafo dirigido acíclico bien formado, un cambio instanciado en una célula sólo puede propagarse a las células descendientes accesibles desde ella. Las células sin camino dirigido desde la célula afectada permanecen inalteradas.

---

## 6. Regímenes de crecimiento de trayectoria

### 6.1. Régimen estricto

La trayectoria crece cuando el dato de transición introduce cambio constitutivo suficiente para justificar una nueva reevaluación.

### 6.2. Régimen auditable pleno

La trayectoria puede incorporar además reevaluaciones de observación sin cambio estructural, siempre que queden marcadas como tales dentro del registro.

---

## 7. Cascadas de reacción

La reevaluación no sustituye la gramática espacial ya fijada en el SV. La reactiva.

Según el patrón compositivo, un dato de transición puede producir:
- propagación lineal en serie;
- propagación lateral en compuertas;
- veto vertical en supervisión meta;
- o reorganización arquitectónica en estructuras construidas con Comp.

La trayectoria recoge esas reevaluaciones; la gramática espacial determina cómo se propagan.

---

## 8. Frontera con el Documento IV

El Documento III opera exclusivamente con sucesos ya legibles en el alfabeto ternario.

El Documento IV formalizará cómo magnitudes no nativas del sistema llegan a ser ternarizables e ingresan en el horizonte de sucesos de la arquitectura. El Documento III no transduce. El Documento IV no organiza trayectorias. El IV presupone el III.

---

## 9. Límites de cierre

Quedan expresamente fuera del cierre actual:
- una axiomática general de horizontes bien formados;
- una norma general de convergencia o divergencia de trayectorias;
- una función de mérito inter-dominio;
- y los ciclos de reevaluación controlados con garantía formal de terminación.

---

## 10. Conclusión

El marco SV queda extendido con una capa de reevaluación discreta subordinada a su gramática espacial previa.

El mecanismo formal es el siguiente: el diseñador declara ℋ(𝒜); uno o varios sucesos del horizonte se instancian con estado en Σ; el dato νₙ registra esa actualización; el operador 𝒰_{νₙ} actúa sobre el sistema; la evaluación espacial ℰ produce un nuevo frame; y la trayectoria T acumula la secuencia sin reescritura.

Esta extensión no altera la base algebraico-semántica del SV. La hace evolucionar.

---

## Referencias

[R1] Juan Antonio Lloret Egea. *Fundamentos algebraico-semánticos del Sistema Vectorial SV.* v1.0.0, Release 3. ITVIA, 2026.  
https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

[R2] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — I. Transmisión en serie por parámetro puente.* v1, Release 4. ITVIA, 2026.  
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv/release/4

[R3] Juan Antonio Lloret Egea. *Álgebra de composición intercelular del marco SV — II. Gramática general de composición.* v1.0, Release 1. ITVIA, 2026.  
https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--ii-gramatica-general-de-composicion/release/1

[R4] Juan Antonio Lloret Egea. *La guía práctica del conocimiento profundo y la crítica de la razón pura.* v1.0.0, Release 2. ITVIA, 2026.  
https://www.itvia.online/pub/la-guia-practica-del-conocimiento-profundoy-la-critica-de-la-razon-pura/release/2

---

## Apéndice breve de notación

| Símbolo | Significado |
|---------|------------|
| 𝒜 | Arquitectura compositiva |
| ℋ(𝒜) | Horizonte de sucesos de la arquitectura |
| Σ = {0, 1, U} | Alfabeto ternario |
| Sₙ | Frame canónico |
| νₙ | Dato de transición |
| 𝒰_{νₙ} | Operador inducido por el dato |
| T | Trayectoria del sistema |
| δ_Γ | Relación de cambio de criticidad |

---

## Ejemplo mínimo de notación

Arquitectura fija: 𝒜  
Horizonte declarado: ℋ(𝒜) = {ε₁, ε₂, ε₃}  
Dato de transición: ν₁ = {(ε₂, 1), (ε₃, U)}  
Actualización: P₂ = 𝒰_{ν₁}(P₁)  
Reevaluación: S₂ = ℰ(𝒜, P₂)  
Trayectoria: T = (S₁, ν₁, S₂)

---

*Documento doctrinal del Sistema Vectorial SV.  
ISSN 2695-6411.*  
*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
