# Catálogo de errores — 2026l Entropía factual SV

Este catálogo documenta las **grietas estructurales y numéricas detectadas y
corregidas** durante siete rondas de auditoría adversarial aplicadas al
documento 2026l. Tiene valor epistemológico propio: registra el proceso
constructivo del rigor y sirve de referencia para la metodología de
auditoría del corpus SV.

---

## Principio del proceso

Cada ronda adversarial se ejecutó con **tres preguntas guía**:

1. ¿Qué afirma el documento que no puede ser verificado?
2. ¿Qué sumando, índice, subíndice o referencia falta o sobra?
3. ¿Qué expresión usa vocabulario prohibido por las constitutivas del SV
   (probabilidad fundante, estadística como verdad, tiempo soberano,
   coordenadas externas)?

Tras cada ronda se aplicaron correcciones quirúrgicas, nunca reestructuraciones
globales. Se preservaron los resultados numéricos exactos del caso patrón
siempre que la corrección no los invalidase.

---

## Ronda 1 — Dictamen integral (grietas A a M)

**13 grietas iniciales sobre el borrador v1** (13 subsecciones teóricas y
una verificación visible).

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| A | Crítica | Tablas §4.4 y §11 mostraban δ_i ≠ 0 durante tramo preternario, contrario a la derivación nativa estricta de 2026j §3. | §3.2 generalizada: pares preternarios admisibles 𝒫^adm_i(k); la derivación nativa es una realización canónica, no la única. |
| B | Notacional | Proposición 6.2: $V_i(\delta, n)$ vs $V_\Gamma(B, n)$ sin equivalencia declarada. | Definición 6.1 aclara $V_\Gamma(B, n) := \sum_i V_i(\delta_i, n)$ componente a componente. |
| C | Conceptual | Proposición 5.4 original usaba "probabilidad de cruce", término prohibido. | §5 reescrita completa; el transporte se articula sin probabilidad. |
| D | Conceptual | §5.4 asumía $v_i(k) = U$ antes del cruce, pero en $\Omega_{pre}$ la posición no tiene valor en $K_3$. | Definición 5.1 introduce paso de activación $k_i^*$; Definición 5.2 restringe sumatorio. |
| E | Conceptual | Mezcla de estratos $\Omega_{pre}$ y $K_3$ en la definición de H_K3. | Convenio de complementariedad por posición-paso (Observación 5.5). |
| F | Crítica | §11 heredaba Grieta A numéricamente. | §11 completa reescrita con convenio general de pares admisibles. |
| G | Conceptual | §11.7 presentaba valores residuales sin justificación formal. | §11.7-§11.8 declaran explícitamente como **parámetros admisibles** cumpliendo (C1)-(C4) de la Definición 7.1. |
| H | Expositiva | §11.9 afirmaba "H_SV(5) = 35.1 por cálculo análogo truncado" sin mostrar el cálculo. | §11.9 añade cálculo completo de $n = 5$ con 30+ líneas de numérica. |
| I | Redacción | §8.4 "el orden $n < n'$ es inferible" redacción vaga. | §8.4 reformulada con garantía algebraica vía Teorema 8.2. |
| J | Circular | Teorema 9.3 apelaba al Teorema 7.5 vía operadores $\mathfrak{K}_{SV}, \mathfrak{H}_{SV}, \mathfrak{T}_{SV}$ sin cerrar el ciclo. | Demostración refactorizada por aplicación iterada del Teorema 8.2 sobre el tramo $[n_\Xi, n_Y]$. |
| K | Conceptual | "Cadena entrópica" presentada con flechas de transporte como si fuera transporte puntual. | Definición 8.1 reformulada: cadena es **sucesión de dispersiones evaluadas sobre la misma trayectoria**, no transporte funcional de valor. |
| L | Menor | §10.1 cota $H_{SV} \geq n \cdot \min_k \rho_U$ grosera. | §10.1 reemplazada por descripción estructural de complementariedad local/global. |
| M | Menor | §12.2 era comentario sin aporte formal. | §12.2 elevada a Proposición 12.2 con demostración formal de independencia. |

---

## Ronda 2 — Grietas post-corrección (N, O, R, T)

**4 grietas nuevas tras primera pasada**.

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| N | Menor | Bibliografía con 2026e y 2026g sin uso en cuerpo. | §10.2 cita 2026e (medición sin probabilidad); §10.4 cita 2026g (sector basal $E_0 = m_0 c^2$). |
| O | Expositiva | Teorema 7.5 fragmentaba la monotonía (sólo $H_{\Sigma_c}$, $H_{\Sigma_k}$, $H_{fin}$); faltaba enunciado único. | Añadido Corolario 7.7 consolidador de monotonía estratificada sobre toda la cadena. |
| R | Precisión | Proposición 12.2 afirmaba "algebraicamente independientes" — enunciado fuerte sin soporte formal. | Suavizado a "estructuralmente independientes", con demostración por inspección estructural. |
| T | Crítica numérica | §11 contaba términos espurios post-clausura en V_i y A_i; valores A_Γ(6)=28, H_pre(6)=31,0 resultaban de cómputo incorrecto. | §11 completa reescrita con convenio explícito: $a_i(k) = 1$ para $k \in [0, k_i^*]$, $a_i(k) = 0$ para $k > k_i^*$. Umbral $\theta_U = 0.4$ (antes 0.3 incompatible con $\delta_3(6) = 0.3$). Fórmula $V_i(\delta, n) = \sum_{k=0}^{\min(n, k_i^*) - 1}$ visible. |

---

## Ronda 3 — Grietas estructurales (U, X, AA)

**3 grietas sobre consistencia formal**.

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| U | Crítica | Definición 4.1 sin restricción `min(n, k_i*)`; inconsistente con aplicación en §11. | Definición 4.1 corregida: $V_i(\delta, n) = \sum_{k=0}^{\min(n, k_i^*) - 1} |\delta_i(k+1) - \delta_i(k)|$ con referencia forward a §5.1. |
| X | Crítica | Definición 5.2 sumaba desde $k_i^*$, pero §11.6 asignaba contribución al cruce como si fuera $U \to v_i(k_i^*)$ desde $k_i^* - 1$. | Definición 5.2 restaurada a suma desde $k = 0$ con **convenio operativo** $v_i(k) = U$ virtual para $k < k_i^*$. Convenio declarado explícitamente como operativo, no ontológico. |
| AA | Conceptual | Observación 5.5 presentaba H_pre y H_K3 como disjuntas por paso, pero el cruce pertenece a ambas. | Reformulada: H_pre y H_K3 capturan aspectos estructuralmente distintos sobre la misma trayectoria; monotonía simultánea garantiza no decrecimiento de la suma estratificada. |

---

## Ronda 4 — Errores aritméticos (BB, CC, DD, EE)

**4 grietas numéricas** detectadas tras verificación programática con Python.

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| BB | Crítica | §11.4 afirmaba $A_4(6) = 3.5$ con cálculo $4 + 0.5 + 0 = 3.5$. **Error aritmético**: la suma correcta es $4.5$. | $A_4(6) = 4.5$. Cascada: $A_\Gamma(6) = 28$ (era 27); $H_{pre}(6) = 31.0$ (era 30.0); $H_{SV}(6) = 38.6$ (era 37.6). |
| CC | Crítica | §11.9 usaba $A_4(5) = 3.5$ heredando Grieta BB. | $A_4(5) = 4.5$, $A_\Gamma(5) = 24.5$, $H_{pre}(5) = 27.2$, $H_{SV}(5) = 33.4$. |
| DD | Cascada | §11.9 valores posteriores heredaban Grietas BB y CC. | Toda la cascada §11.7-§11.9 recalculada con los nuevos $A_i$. Monotonía $\Delta = 5.2 > 0$ preservada. |
| EE | Redacción | §11.4 decía "todos los pares evalúan a 1" — ambiguo entre valor del par y valor tras promedio. | Texto clarificado: "cada par $(a(k), a(k+1))$ tiene valor $(1,1)$ y contribuye $1$ a la suma". |

---

## Ronda 5 — Consistencia cross-definición (FF, GG, HH, II)

**4 grietas por desalineación entre definiciones y aplicaciones**.

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| FF | Expositiva | §4.4 no declaraba $k_i^*$ explícitamente, dejando al lector verificar que la restricción $\min(n, k_i^*) = n$ se cumple. | §4.4 declara explícitamente "$k_i^* \geq 3$ para las tres posiciones". |
| GG | Crítica | Demostración del Teorema 4.5 escribía $V_i(n+1) - V_i(n) = \|\delta_i(n+1) - \delta_i(n)\|$ sin articular regímenes. | Demostración refactorizada en tres regímenes explícitos: (I) $n+1 \leq k_i^*$, (II) $n = k_i^* - 1$, (III) $n \geq k_i^*$. |
| HH | Ambigüedad | Prop 4.7 hablaba de "reclasificación de coordenada proyectada como U" pero la demostración modificaba $\delta_i(k)$: inconsistencia de dominio. | Prop 4.7 reformulada: "reescritura retroactiva del sesgo polar declarado $\delta_i(k_0)$ para algún $k_0 \in [0, k_i^*]$". |
| II | Menor | Prop 5.3 demo no trataba caso borde $k_i^* = 0$. | Añadida cláusula: "En el caso borde $k_i^* = 0$, la posición cruza en el paso inicial sin tramo virtual previo". |

---

## Ronda 6 — Coherencia de criterios (KK, LL, MM, NN)

**4 grietas finales de precisión**.

| Id | Gravedad | Descripción | Corrección |
|----|----------|-------------|------------|
| KK | Crítica | Corolario 8.3 demo citaba "Teorema 5.3" (que es proposición), no Teorema 5.4 (que es el de monotonía de H_K3). | Cita corregida a "4.5, 5.4, 6.3, 7.5". |
| LL | Consistencia | Def 7.1 exigía "independencia algebraica" (C4); Prop 12.2 afirmaba "estructuralmente independientes". Dos criterios distintos. | Homogeneizado a **"estructural"** en los tres puntos: Def 7.1 (C4), Prop 7.6 demo, y Prop 12.2. |
| MM | Tipográfica | §10.3 fórmula con `+ (\text{resto})` textual dentro de expresión matemática. | Reemplazada por suma formal: $\sum_{\mathcal{C} \in \mathfrak{C}^{adm}_{\Sigma_{conc}} \cup \mathfrak{C}^{adm}_{\Sigma_{canal}} \cup \mathfrak{C}^{adm}_{trans}} \mathcal{C}(\Gamma, n)$. |
| NN | Tipográfica | Def 7.1 usaba $\mathcal{C}$ tanto para contribución individual como para la familia $\mathcal{C}^{adm}_\Sigma$, sobrecarga tipográfica. | Refactor global: contribución genérica = $\mathcal{C}$ (caligráfico); familia = $\mathfrak{C}^{adm}_\Sigma$ (fraktur). |

---

## Ronda 7 — Verificación cero residuales (OO, PP, QQ, RR, SS)

**Auditoría final sobre el v7 HTML**, todas las grietas candidatas sin hallazgo:

- OO ✓ Cabecera no rompe índice/anclas.
- PP ✓ $\mathcal{P}^{adm}_i(k)$ es legítimo y distinto de $\mathcal{C}$ (contribución) y $\mathfrak{C}$ (familia).
- QQ ✓ Llaves `{` y `}` balanceadas en todos los bloques math.
- RR ✓ Coexistencia de Unicode HTML en texto y LaTeX dentro de ```math es el diseño validado.
- SS ✓ Cero ocurrencias de `_Γ`, `_palabra` u otros subíndices sin convertir.

---

## Octava ronda adversarial (v9 → v10)

Adversarial externa derivada del corpus completo (10 HTMLs de 2026a-j + 2 .md 2026k/k') con lectura doctrinal dura. Se identifican **9 grietas** de capas más profundas que las siete rondas anteriores: filosofía de la demostración, frontera con otras piezas del corpus, riesgo de duplicación estructural con magnitudes ya asentadas.

### Grieta 1 (CRÍTICA) — Off-by-one del índice de activación

**Detección.** Def 5.1 fijaba "*para todo k ≤ k<sub>i</sub><sup>*</sup>, permanece preternaria*" y "*para k > k<sub>i</sub><sup>*</sup>, v<sub>i</sub>(k) ∈ {0, 1, U}*", pero Prop 5.3 trabajaba explícitamente con *v<sub>i</sub>(k<sub>i</sub><sup>*</sup>) ∈ {0, 1, U}* tratando el índice de cruce como ya ternarizado. Ambigüedad material tipo off-by-one.

**Corrección aplicada.** Def 5.1 reformulada con **tres regímenes explícitos**: k < k<sub>i</sub><sup>*</sup> (preternaria íntegra), k = k<sub>i</sub><sup>*</sup> (paso del cruce con proyección Π<sup>H</sup><sub>3</sub> al final del paso; desdoblamiento frontera estructural doble), k > k<sub>i</sub><sup>*</sup> (régimen post-cruce bajo Lema 5.5 y 7.3). Observación 5.1 declara que el índice k<sub>i</sub><sup>*</sup> es frontera estructural doble, que el sesgo polar δ<sub>i</sub>(k<sub>i</sub><sup>*</sup>) sigue siendo lectura preternaria válida (para A<sub>i</sub>, V<sub>i</sub>) mientras v<sub>i</sub>(k<sub>i</sub><sup>*</sup>) emerge como proyección al final del paso.

### Grieta 2 (LEGÍTIMA) — Demo de Prop 4.7 lógicamente insuficiente

**Detección.** Prop 4.7 afirmaba "violación directa del Teorema 4.5" pero la demo sólo mostraba "puede producir decremento". Salto lógico entre enunciado y prueba: demostraba menos de lo que afirmaba.

**Corrección aplicada.** Prop 4.7 reformulada como **argumento de clase y no de instancia**, con análisis explícito de a + b vs a' + b' mediante desigualdad triangular inversa, más cláusula de bloqueo por honestidad coordenada (Lema 7.3 de 2026j). Demo cerrada por demostración estructural: la reescritura retroactiva o bien viola append-only o bien viola honestidad coordenada, no existe vía que salve ambas simultáneamente.

### Grieta 3 (PARCIAL) — Cota 2 transiciones sin unicidad demostrada

**Detección.** Prop 5.3 enunciaba que tras cruce a U se admite "*una única transición adicional U → {0, 1} bajo nueva base compatible*", pero la unicidad no se demostraba dentro del documento; se invocaba Lema 5.5 sin cerrar la prueba.

**Corrección aplicada.** Prop 5.3 reforzada con **tres regímenes disjuntos** (virtual k < k<sub>i</sub><sup>*</sup>-1; cruce k = k<sub>i</sub><sup>*</sup>-1; post-cruce k ≥ k<sub>i</sub><sup>*</sup>) con subcasos excluyentes en el post-cruce (cierre determinado vs U-indeterminado). La unicidad de la transición complementaria U → {0, 1} se fundamenta en tres bloques del corpus: no retorno preternario (Lema 5.5), no reinterpretación sin nueva base (Lema 7.3), y cierre subsiguiente automático por subcaso 1 (queda fija).

### Grieta 4 (FILOSÓFICA) — Circularidad normativa en §2.2

**Detección.** §2.2 prohibía "*operación que pueda decrementar la magnitud*", mientras el Teorema 8.2 "demostraba" la no decrecencia. Lectura hostil: la no decrecencia queda parcialmente incorporada al dominio por exclusión previa, no sólo derivada del aparato.

**Corrección aplicada.** §2.2 reformulada eliminando la prohibición circular y añadiendo **separación explícita entre dos niveles**: (1) nivel de dominio (disciplina heredada append-only + Lemas 5.5 y 7.3), (2) nivel algebraico derivado (no decrecencia de H<sub>SV</sub> como consecuencia algebraica). La exclusión de operaciones decrementales pasa a ser consecuencia (vía Prop 4.7), no axioma.

### Grieta 5 (MATIZADA) — Apoyo excesivo en K<sub>3</sub>

**Detección.** El "convenio operativo de representación ternaria" (v<sub>i</sub>(k) = U virtual para k < k<sub>i</sub><sup>*</sup>) rozaba la frontera doctrinal: el corpus exige que la matemática primaria no nazca en K<sub>3</sub>.

**Corrección aplicada.** Observación 5.2 declara explícitamente el **estatuto estrictamente instrumental** del convenio virtual: aplica sólo dentro del sumatorio de Def 5.2, no es predicación ontológica, las primitivas A<sub>i</sub>, V<sub>i</sub> siguen definidas sobre Ω<sub>pre</sub>. La lectura ternaria queda como lectura inducida, no plano de trabajo primario.

### Grieta 6 (RETÓRICA) — §8.4 sobreextiende "monotonía estricta"

**Detección.** §8.4 hablaba de "*orden temporal de sucesos inferido algebraicamente*" y "*monotonía estricta*", pero el Teorema 8.2 es de no decrecencia (no estricta); en igualdad entrópica no se reconstruye orden.

**Corrección aplicada.** §8.4 reformulada con **Proposición 8.4** (ordenamiento parcial), **Observación 8.4.1** (alcance: clases de equivalencia entrópica cuando hay igualdad; el índice factual ν<sub>j</sub> ordena el interior de cada clase), **Observación 8.4.2** (el Teorema 8.2 es no decrecencia, no monotonía estricta; la monotonía estricta emerge sólo en tramos con incremento no nulo).

### Grieta 7 (CRÍTICA) — Irreductibilidad respecto a A<sub>TPA</sub>

**Detección.** El criterio de falsación (3) del §14.2 exige probar que H<sub>SV</sub> no duplica magnitud ya asentada del corpus. El candidato más próximo, A<sub>TPA</sub> de 2026b §12, cuantifica carga acumulada de indeterminación; H<sub>SV</sub> absorbe A<sub>Γ</sub>, V<sub>Γ</sub>, ‖J‖, R, contribuciones posteriores. Si no se demuestra que H<sub>SV</sub> es estructuralmente más ancha, queda abierto el reproche "es un rebautizo ampliado del área factual".

**Corrección aplicada.** Nuevo **§12.4 "Irreductibilidad de H<sub>SV</sub> respecto al aparato TPA"** con **Proposición 12.4** y demostración por descomposición explícita que identifica **tres componentes estructurales adicionales**: variación total preternaria V<sub>Γ</sub> (oscilación interna no leída por A<sub>TPA</sub>), ‖J‖<sub>1</sub> + R<sub>Γ</sub> (sensibilidad jacobiana y residual ajenos a la codificación ternaria), y ∑<sub>𝒞</sub> 𝒞(Γ, n) sobre contribuciones post-canónicas (Σ<sub>c</sub>, Σ<sub>k</sub>, transmutación). Contraejemplo construido: dos trayectorias con misma secuencia ternaria resultante pero distintas historias de oscilación preternaria producen idéntico A<sub>TPA</sub> y distinto H<sub>SV</sub>. Observación 12.4.1 confirma que la irreductibilidad no disminuye el papel fundacional de A<sub>TPA</sub>, lo extiende. Falsación (3) exorcizada.

### Grieta 8 (TÉCNICA) — 𝒫<sup>adm</sup><sub>i</sub>(k) demasiado ancha

**Detección.** §3.2 admitía clase general de pares preternarios sin reconstrucción explícita de los indicadores nativos; quedaba abierta la acusación de que la magnitud pudiera depender del modo de provisión del par.

**Corrección aplicada.** Nuevo **Teorema 3.2 de invariancia estructural bajo cambio de realización**: si dos realizaciones (α<sub>i</sub>, β<sub>i</sub>) y (α'<sub>i</sub>, β'<sub>i</sub>) producen los mismos (δ<sub>i</sub>, a<sub>i</sub>), entonces H<sub>SV</sub>(Γ, n) coincide puntualmente. Corolario 3.2.1 fija que H<sub>SV</sub> es funcional de (δ<sub>i</sub>, a<sub>i</sub>), no de (α<sub>i</sub>, β<sub>i</sub>) directamente. La libertad de descomposición no afecta la magnitud.

### Grieta 9 (EDITORIAL) — Frontera matemática

**Detección.** El documento hablaba con cierre excesivo sobre zonas del corpus que 2026a y 2026j aún describen como abiertas (segundo orden, jacobiano de clausura, transformadas, capa espectral).

**Corrección aplicada.** §15 amplía "Plano de lo abierto" con nuevo **"Plano de frontera matemática"** que reconoce explícitamente las zonas abiertas del corpus y fija que el aparato del presente documento se apoya exclusivamente en el perímetro doctrinal ya zanjado (2026a §III, 2026b §VII, 2026j §§3-8, 2026k §§3-13).

---

## Métricas octava ronda

| Concepto | v9 | v10 |
|----------|-----|------|
| Grietas acumuladas | 28 (rondas 1-7) | 37 (añadidas 9 de ronda 8) |
| Teoremas | 6 | **7** (añadido Teo 3.2) |
| Proposiciones | 7 | **9** (añadidas Prop 8.4, 12.4) |
| Corolarios | 4 | **5** (añadido Cor 3.2.1) |
| Definiciones | 12 | 12 |
| Observaciones | — | **5** nuevas (5.1, 5.2, 8.4.1, 8.4.2, 12.4.1) |
| Enunciados formales totales | 29 | **38** |
| Q.E.D. | 16 | **19** (añadidos por Teo 3.2, Prop 8.4, Prop 12.4) |
| Líneas del documento | ~1012 | ~1148 |



Tras la séptima ronda, el documento se convirtió al formato validado de publicación:

- **Todo inline $...$** → Unicode + `<sub>`/`<sup>` HTML (706 expresiones).
- **Todo display $$...$$** → bloques ``` ```math ... ``` ``` (65 bloques).
- **Coma decimal**: `{,}` en bloques math, coma simple en texto corrido.
- Símbolos: 𝔼, 𝕏, 𝕐, ℂ (pizarra); 𝔎, 𝔥, 𝔗, 𝔠 (fraktur); 𝒞, ℒ, ℱ, 𝒫 (caligráfica); griegas Ω, Γ, Ξ, Σ, Δ, Π, etc.; operadores ≤, ≥, ⇝, ⟹, ‖·‖, 𝟙.

---

## Métricas finales

| Concepto | Valor |
|----------|-------|
| Rondas adversariales | 7 |
| Grietas documentadas | 28 (A-M, N, O, R, T, U, X, AA, BB, CC, DD, EE, FF, GG, HH, II, KK, LL, MM, NN) |
| Correcciones aplicadas | 28 |
| Líneas del documento final | 820 |
| Teoremas, proposiciones, corolarios, definiciones | 6 + 7 + 4 + 12 = 29 enunciados |
| Demostraciones con Q.E.D. | 16 |
| Bloques ```math | 65 |
| Referencias con uso en cuerpo | 2026a, 2026b, 2026e, 2026g, 2026j (21), 2026k (4) |

---

**© 2026 Juan Antonio Lloret Egea** — ORCID 0000-0002-6634-3351 — ITVIA — ISSN 2695-6411 — Licencia CC BY-NC-ND 4.0.
