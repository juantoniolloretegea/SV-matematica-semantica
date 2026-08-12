# Curvatura sin sustancia y exceso gravitatorio sin materia: dos teoremas sobre un dominio observable declarado

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), 28029 Madrid, España  
ORCID: 0000-0002-6634-3351  

> **Preprint — 10 de agosto de 2026.** Esta versión no ha sido sometida a revisión por pares.

## Resumen

En este trabajo no se niegan ni el régimen cosmológico acelerado ni el exceso gravitatorio observado en galaxias, cúmulos y sistemas de lente gravitacional. Se examina una etapa clasificatoria anterior: bajo qué condiciones positivas puede denominarse sustancia a un retorno observacional. El análisis se desarrolla dentro del Sistema Vectorial (SV), marco formal en el que cada magnitud se declara con su dominio, unidad, frontera, residual y retorno.

El primer teorema obtiene la tasa ciclo-distancial κ(T)=1/T mediante la normalización de una tendencia de separación declarada e introduce la ley constitutiva de curvatura del SV:

```text
Λ_SV(T) = [tr(∇V_sep^SV) · κ(T)] / c²
```

Para un campo de separación isótropo tridimensional,

```text
V_sep^SV(r) = κ(T)r
```

se deriva:

```text
Λ_SV,puro(T) = 3/(c²T²)
```

Para la escala declarada

```text
T_obs = 4,3549488 × 10¹⁷ s
```

se obtiene:

```text
Λ_SV,puro = 1,7600043527547774 × 10⁻⁵² m⁻²
```

La relación se obtiene con independencia de las ecuaciones de Friedmann. Su forma algebraica coincide con la relación de curvatura de de Sitter, pero la tasa, el dominio y el origen interpretativo permanecen diferenciados.

El segundo teorema examina la inferencia que conduce desde un exceso gravitatorio observado hasta la afirmación de una sustancia material. Bajo un protocolo positivo de admisión material —identidad, magnitud, unidad, frontera, traza, retorno propio y ausencia de doble cómputo—, el término genérico «materia oscura», cuando comparece únicamente como residual gravitatorio y no como materialidad identificada positivamente, presenta contribución sustancial nula:

```text
ρ_DM,sustancia^SV = 0
m_DM,sustancia^SV = 0
```

El fenómeno gravitatorio no se niega: se conserva mediante materialidad retornada, densidad gravitatoria efectiva de sutura y un residual explícito de no clausura. Curvatura y sutura se coordinan mediante transducción, pero no son magnitudes física ni dimensionalmente idénticas.

**Palabras clave:** constante cosmológica; energía oscura; materia oscura; curvatura ciclo-distancial; sutura gravitatoria; admisión material; dominio observable.

### Antecedentes del preprint

Los resultados teóricos nucleares y parte del formalismo de apoyo fueron divulgados previamente por el autor en preprints en español no revisados por pares, citados expresamente por DOI en este trabajo. El presente preprint los consolida, unifica su notación y reformula su arquitectura argumental.

---

# 1. Introducción

El sector oscuro de la cosmología contemporánea reúne dos problemas físicos diferentes bajo un vocabulario común de ausencia. El sector de la constante cosmológica representa un régimen a gran escala mediante un término de curvatura, una densidad efectiva o la denominación «energía oscura». El sector de la materia oscura representa efectos gravitatorios que no quedan agotados por el contenido material inventariado convencionalmente en galaxias, cúmulos, sistemas de lente gravitacional, fondo cósmico de microondas y estructura a gran escala. En ambos casos, las observaciones y la eficacia instrumental de los modelos son reales. Persiste, sin embargo, una cuestión adicional: qué clase de objeto físico se afirma cuando un retorno observacional recibe la denominación de sustancia.

Este trabajo aborda esa cuestión mediante el Sistema Vectorial (SV). El SV no utiliza la ciencia contemporánea como fuente de verdad constitutiva. Las teorías externas, las mediciones y las estimaciones de parámetros cosmológicos operan como bancos declarados de contraste y de retorno metrológico. El resultado interno debe generarse primero dentro de un dominio declarado, haciendo explícitas su magnitud, unidad, ecuación, frontera, residual y retorno. Sólo después puede compararse con un banco externo.

Se presentan dos teoremas.

El primero es el **Teorema de resolución física de la constante cosmológica**. Parte de una escala ciclo-distancial declarada T para un dominio observable retornado y obtiene, a partir de la tendencia de separación declarada, una tasa estructural normalizada:

```text
κ(T) = 1/T
```

A continuación, un campo de separación isótropo tridimensional se proyecta a curvatura mediante una ley constitutiva explícita. Se obtiene así:

```text
Λ_SV,puro(T) = 3/(c²T²)
```

El resultado no se importa de un ajuste que emplee H₀, Ω_Λ, el fondo cósmico de microondas, las oscilaciones acústicas bariónicas o supernovas de tipo Ia. La derivación no invoca las ecuaciones de Friedmann. Su forma algebraica final es compatible con la relación de de Sitter, pero su tasa se genera como magnitud ciclo-distancial del dominio SV declarado, en lugar de introducirse como parámetro de Hubble de una solución relativista.

El segundo es el **Teorema de nulidad sustancial de la materia oscura**. No niega las curvas de rotación, las lentes gravitacionales, la dinámica de cúmulos, la separación entre plasma bariónico y potencial gravitatorio reconstruido, las anisotropías del fondo cósmico de microondas ni la formación de estructura. Niega que un exceso gravitatorio constituya, por sí solo, evidencia positiva de una sustancia material. Bajo un protocolo explícito de admisión material, el término genérico «materia oscura», cuando comparece únicamente como inferencia gravitatoria y no retorna como materialidad identificada positivamente, aporta cero al inventario material admitido:

```text
ρ_DM,sustancia^SV = 0
m_DM,sustancia^SV = 0
```

El retorno gravitatorio observado se conserva mediante una descomposición en capacidad estructural, materialidad retornada, densidad gravitatoria efectiva de sutura y residual explícito de no clausura.

El trabajo aporta cinco elementos:

1. Formula dentro del propio teorema la ley constitutiva de curvatura ciclo-distancial, en vez de dejarla implícita en la demostración.
2. Deriva `Λ_SV,puro(T)=3/(c²T²)` a partir de un campo interno de separación sin invocar las ecuaciones de Friedmann.
3. Distingue la curvatura interna del dominio puro de las reconstrucciones observacionales `Λ_obs[B]`, dependientes de un banco externo `B`.
4. Formula la nulidad sustancial bajo criterios positivos de admisión material, conservando íntegramente el fenómeno gravitatorio.
5. Coordina curvatura y sutura gravitatoria efectiva mediante una transducción dimensionalmente explícita, sin identificarlas como una misma magnitud física.

El alcance es deliberadamente acotado. No se afirma una sustitución completa de ΛCDM, un modelo acabado de curvas de rotación galáctica, una reconstrucción universal de lentes gravitacionales ni una teoría perturbativa completa. Se presentan dos resultados formales, su instancia numérica, sus interpretaciones permitidas, sus condiciones de fallo y los dominios empíricos que permanecen abiertos.

# 2. Relación con trabajos previos revisados por pares

## 2.1. La ciencia externa como banco de contraste

Esta sección no pretende reconstruir el SV a partir de la relatividad general, ΛCDM, la materia oscura de partículas o la gravedad modificada. Esos marcos constituyen dominios externos de comparación. Sus ecuaciones y observaciones delimitan aquello que una formulación competidora debe conservar, distinguir o retornar, pero no constituyen las premisas internas de los teoremas del SV.

La constante cosmológica desempeña una función geométrica en la cosmología relativista y una función observacional en modelos ajustados a supernovas, fondo cósmico de microondas, oscilaciones acústicas bariónicas y estructura a gran escala [1]–[6]. La interpretación en términos de energía del vacío conduce al conocido problema de la constante cosmológica cuando una contribución microscópica desnuda del vacío se identifica directamente con la curvatura cosmológica retornada por observación [5]. La formulación presente separa energía desnuda del vacío, magnitudes renormalizadas, densidad efectiva, presión, término cosmológico y curvatura retornada. No se admite identidad directa entre esos planos sin una transducción declarada.

El sector de la materia oscura cuenta con evidencia gravitatoria convergente, entre ella la dinámica galáctica, las lentes gravitacionales, los cúmulos en colisión, las anisotropías del fondo cósmico de microondas y la formación de estructura [6]–[8]. Los candidatos de partículas, los programas de gravedad modificada, la fenomenología de tipo MOND y los planteamientos de gravedad emergente ofrecen explicaciones o parametrizaciones diferentes de partes de esa evidencia [9]–[11]. El SV no rechaza por su nombre ninguna de esas aproximaciones. Formula una pregunta clasificatoria anterior: qué condiciones físicas positivas autorizan que una magnitud inferida gravitatoriamente ingrese en un inventario material.

## 2.2. Punto exacto de convergencia con la relación de de Sitter

Para un régimen de de Sitter, la relación conocida puede escribirse como [1]:

```text
Λ = 3H²/c²                                            (1)
```

El teorema del SV alcanza la misma forma algebraica después de definir independientemente una tasa ciclo-distancial y proyectar a curvatura un campo de separación isótropo tridimensional. Por ello, este trabajo no reivindica como novedad la forma algebraica externa `3(tasa)²/c²`. La posible contribución teórica reside en la vía interna que genera la tasa, en el estatuto de dominio declarado de esa tasa y en la interpretación no sustancial de la curvatura resultante.

La diferencia no consiste en un mero cambio de símbolo:

```text
H  ⟶  κ
```

El SV no parte de la ecuación de de Sitter para sustituir `H`. Parte de:

```text
V_sep^SV(D;T) = D/T
```

normaliza por distancia la tendencia de separación, construye el campo vectorial asociado, toma su traza tridimensional y aplica la ley constitutiva de curvatura. La igualdad entre las formas algebraicas finales constituye la convergencia de dos cadenas, no el origen de la cadena SV.

## 2.3. Reconstrucción observacional externa

Para un banco cosmológico externo `B`, la reconstrucción observacional se expresa como:

```text
Λ_obs[B] = 3Ω_Λ[B]H₀[B]²/c²                         (2)
```

La ecuación (2) no constituye un segundo resultado constitutivo del SV. Es una identidad dependiente de banco bajo las convenciones del modelo cosmológico declarado. Su función consiste en conservar el valor retornado por el banco externo junto con su unidad, incertidumbre, residual y dictamen.

Por tanto, la magnitud SV del dominio puro y la magnitud dependiente de banco no son automáticamente idénticas:

```text
Λ_SV,puro(T) ≠ Λ_obs[B]                              (3)
```

Una razón numérica entre ambas no constituye, por sí sola, un residual físico homogéneo, porque numerador y denominador pertenecen a planos constituidos de manera diferente.

# 3. Antecedentes, dominio y notación

## 3.1. Preprints antecedentes

El presente trabajo consolida y reformula resultados divulgados previamente en los siguientes preprints en español no revisados por pares:

- J. A. Lloret Egea, *Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable*, DOI `10.21428/39829d0b.41afec0f` [12].
- J. A. Lloret Egea, *La materia oscura no existe como sustancia: demostración formal de nulidad sustancial, densidad gravitatoria efectiva de sutura y contraste físico escalable*, DOI `10.21428/39829d0b.7b41835f` [13].
- J. A. Lloret Egea, *Radio, frontera y densidad del universo observable — Trilogía Cosmológica, Parte III*, DOI `10.21428/39829d0b.0430adc0` [14].
- J. A. Lloret Egea, *Edades relativas del universo observable y de sus objetos físicos*, DOI `10.21428/39829d0b.b56ed853` [15].

El presente texto no consiste en una mera concatenación de aquellos antecedentes. Establece una notación común para los dos teoremas, hace explícita en el primer teorema la ley constitutiva de curvatura, incorpora al argumento principal la distinción entre radio estructural y radio comóvil, separa inventarios internos de bancos externos y formula condiciones de fallo de manera explícita y evaluable.

## 3.2. Dominios y bancos

No deben confundirse tres clases de colecciones internas o externas:

```text
B_inv = inventario material positivo                         (4)
B_obs = banco externo observacional o cosmológico            (5)
B_cmp = banco externo empleado para contraste                (6)
```

El dominio principal del primer teorema es el dominio observable retornado:

```text
Ω_obs(T)
```

El dominio global principal del segundo teorema se escribe:

```text
Ω_T
```

y designa el dominio físicamente realizado bajo el régimen ciclo-distancial declarado `T`.

Los subdominios galáctico, de lente gravitacional, de cúmulo o compacto requieren su propio soporte, banco, frontera y residual. Los resultados obtenidos en `Ω_T` no se transfieren automáticamente a dichos subdominios.

## 3.3. Símbolos

| Símbolo | Significado | Unidad | Estatuto |
|---|---|---:|---|
| `T` | escala ciclo-distancial declarada | s | parámetro interno |
| `T_obs` | instancia SV declarada de `T` | s | instancia fijada; genealogía fuera del alcance presente |
| `κ(T)` | tasa ciclo-distancial normalizada | s⁻¹ | magnitud interna |
| `V_sep^SV` | campo ciclo-distancial de separación | m·s⁻¹ | campo interno |
| `Λ_SV,puro` | curvatura ciclo-distancial del dominio puro | m⁻² | resultado interno |
| `Λ_obs[B]` | constante cosmológica observacional retornada por el banco `B` | m⁻² | resultado de banco externo |
| `R_SV(T)` | radio estructural interno | m | magnitud interna |
| `V_SV(T)` | volumen estructural interno | m³ | magnitud interna |
| `ρ_cap^SV` | densidad de capacidad estructural | kg·m⁻³ | magnitud interna transducida |
| `ρ_ret^SV` | densidad de materialidad retornada | kg·m⁻³ | dependiente de inventario |
| `ρ_sut,grav^SV` | densidad gravitatoria efectiva de sutura | kg·m⁻³ | magnitud estructural derivada |
| `ρ_C^SV` | residual de no clausura | kg·m⁻³, intervalo o U | residual explícito |
| `U` | no clausura honesta | — | indeterminación no escalar o acotada |

Los símbolos `Λ_SV,puro` y `ρ_sut,grav^SV` designan magnitudes distintas. La primera es una curvatura; la segunda es un retorno estructural equivalente en densidad.

# 4. Premisas formales y criterios de admisión material

## 4.1. Premisas ciclo-distanciales

Sea `T>0` una escala ciclo-distancial declarada de un dominio observable retornado. La tendencia escalar de separación sobre una distancia declarada `D` es:

```text
V_sep^SV(D;T) = D/T                                  (7)
```

La normalización por distancia proporciona:

```text
κ(T) = V_sep^SV(D;T)/D = 1/T                         (8)
```

El campo vectorial isótropo ideal correspondiente, en tres direcciones ortogonales, es:

```text
V_sep^SV(r;T) = κ(T)r                                (9)
```

## 4.2. Ley constitutiva de curvatura del SV

La ley constitutiva se formula como parte del teorema y no se introduce después de haber anunciado su resultado:

```text
Λ_SV(T) := [tr(∇V_sep^SV(r;T)) · κ(T)] / c²          (10)
```

La ecuación (10) constituye la proyección SV desde un campo de separación ciclo-distancial hacia una magnitud de curvatura inversa cuadrática. La corrección dimensional, por sí sola, no selecciona de forma única esta ley: se trata de una declaración constitutiva del marco SV. La demostración determina su consecuencia bajo el campo isótropo declarado.

## 4.3. Criterios positivos de admisión material

Un candidato `i` sólo puede ingresar en el inventario material bajo un dominio y un banco declarados. Su indicador local de admisión es:

```text
μ_i^M(Ω;B_inv) ∈ {1, 0, U}                          (11)
```

donde:

- `1` designa materialidad admitida;
- `0` designa exclusión del inventario material admitido;
- `U` conserva un candidato no resuelto, manteniendo visibles su causa y su banco.

La admisión exige los siguientes atributos:

- **Identidad material:** el candidato no es un mero rótulo asignado a un residual.
- **Magnitud:** se declara una cantidad física asociada al candidato.
- **Unidad:** la magnitud se expresa en una unidad válida.
- **Frontera:** puede identificarse el soporte o la frontera operativa.
- **Traza:** el candidato deja una traza física que no se reduce al mismo residual utilizado para postularlo.
- **Retorno propio:** el candidato retorna mediante un canal físicamente especificado.
- **Ausencia de doble cómputo:** una misma contribución física no ingresa en varias clases del inventario.

Estos criterios no restringen la materia a objetos ópticamente luminosos. Bariones no luminosos, gas frío, plasma, polvo, objetos compactos, neutrinos masivos u otra componente material pueden ingresar cuando su identidad material y su dominio retornan positivamente.

## 4.4. Operador de materialidad retornada

Sea `I_i^R` la unidad másica factual asignada a un elemento admitido del inventario. El número másico retornado es:

```text
N_M,ret^SV(Ω;B_inv)
=
Σ_[i∈Supp_M(Ω;B_inv)] μ_i^M(Ω;B_inv) · I_i^R        (12)
```

Tras la transducción a unidades SI, la densidad de materialidad retornada es:

```text
ρ_ret^SV(Ω;B_inv)
=
(1/V_Ω^SV) · 𝔛_M^(SV→SI)(N_M,ret^SV · UFM)          (13)
```

La salida completa del inventario no tiene por qué reducirse a un único escalar:

```text
Ret_M^SV = (ρ_A^SV, ρ_U^SV, ρ_E^SV, ρ_X^SV)        (14)
```

donde `A` representa materialidad admitida, `U` materialidad candidata no resuelta, `E` retorno energético separado y `X` recoge exclusiones como inferencia gravitatoria pura, doble cómputo dependiente de modelo o sustancialización sin admisión positiva.

# 5. Teorema 1: resolución ciclo-distancial de la constante cosmológica

## 5.1. Enunciado

**Teorema 1 — Resolución física de la constante cosmológica en el SV.** Sea `Ω_obs(T)` un dominio observable retornado con escala ciclo-distancial declarada `T>0`. Sea su campo ideal de separación:

```text
V_sep^SV(r;T) = κ(T)r
κ(T) = 1/T
```

Supónganse tres direcciones ortogonales isótropas y la ley constitutiva de curvatura (10). Entonces, la curvatura ciclo-distancial del dominio puro es:

```text
Λ_SV,puro(T) = 3/(c²T²)                              (15)
```

con unidad `m⁻²`.

## 5.2. Demostración

Para:

```text
V_sep^SV = (κx, κy, κz)
```

las derivadas diagonales son:

```text
∂V_x/∂x = ∂V_y/∂y = ∂V_z/∂z = κ
```

Por tanto:

```text
tr(∇V_sep^SV) = ∇·V_sep^SV = 3κ                     (16)
```

Sustituyendo en la ley constitutiva:

```text
Λ_SV,puro = [(3κ)κ]/c² = 3κ²/c²
```

y utilizando `κ=1/T`:

```text
Λ_SV,puro(T) = 3/(c²T²)
```

Finalmente:

```text
(s⁻¹ · s⁻¹)/(m² · s⁻²) = m⁻²
```

con lo que queda completado el retorno dimensional. ∎

## 5.3. Instancia numérica

Para la escala SV declarada:

```text
T_obs = 4,3549488 × 10¹⁷ s                          (17)
```

y para el valor SI exacto:

```text
c = 299 792 458 m·s⁻¹
```

la tasa normalizada es:

```text
κ_obs = 1/T_obs
      = 2,296238247393402 × 10⁻¹⁸ s⁻¹               (18)
```

Por tanto:

```text
Λ_SV,puro
=
1,7600043527547774 × 10⁻⁵² m⁻²                      (19)
```

Las cifras de (18) y (19) son exactas respecto del valor declarado `T_obs`, del valor SI exacto de `c` y de las operaciones formales realizadas. No se presentan como una determinación empírica independiente de `T_obs`.

El teorema general es (15); la ecuación (19) constituye su instancia numérica declarada.

## 5.4. Interpretación

La interpretación SV de `Λ_SV,puro` es la de **curvatura ciclo-distancial del dominio observable retornado**. No es:

- una sustancia material;
- una masa oculta;
- calor ni temperatura;
- una fuerza local entre cuerpos;
- la energía desnuda del vacío de la teoría cuántica de campos;
- ni la densidad gravitatoria efectiva de sutura que se introduce más adelante.

No se niegan los fenómenos observacionales asignados al régimen cosmológico acelerado. Se rechaza su interpretación sustancial.

## 5.5. Convergencia sin dependencia derivativa

La ecuación (15) presenta la misma forma algebraica que la relación de curvatura de de Sitter cuando esta última se expresa mediante su tasa constante de expansión [1]. Sin embargo, la cadena SV no se deriva de esa solución relativista ni invoca las ecuaciones de Friedmann. La convergencia se expresa, por tanto, como compatibilidad entre formas finales:

```text
3κ²/c²  ↔  3H_dS²/c²                                (20)
```

y no como identidad entre las variables generadoras, las teorías de las que proceden o sus dominios.

# 6. Radio estructural interno y radio comóvil externo

La primera objeción previsible frente a (15) aparece cuando la escala inversa de curvatura se interpreta como si fuese el radio convencional del universo observable. El SV no establece esa identificación.

## 6.1. Radio estructural interno

La curvatura del dominio puro define el radio estructural interno:

```text
R_SV(T) := √[3/Λ_SV,puro(T)] = cT                   (21)
```

El volumen estructural ideal asociado es:

```text
V_SV(T) = (4π/3)(cT)³                               (22)
```

Para `T=T_obs`, `R_SV` es aproximadamente 13,8 mil millones de años luz. Se trata de un radio estructural ciclo-distancial generado por el teorema interno.

## 6.2. Radio comóvil externo

El radio comóvil del universo observable pertenece a una construcción observacional FLRW externa. Se obtiene a partir de la historia de expansión, típicamente mediante una integral en la que interviene `H(z)`, y bajo el modelo cosmológico estándar suele situarse en torno a 46 mil millones de años luz para un observador actual [4], [6].

Ambos radios no constituyen estimaciones alternativas de una misma cantidad:

```text
R_SV(T) ≠ R_comóvil[B]                              (23)
```

El primero se genera mediante la cadena interna de curvatura ciclo-distancial. El segundo es retornado por un banco cosmológico externo y su modelo de distancias. Su diferencia no constituye un error aritmético y ninguno de los dos radios corrige al otro sin un transductor declarado.

## 6.3. Consecuencia para las masas integradas

Una densidad es una magnitud intensiva. La masa obtenida al integrarla depende del volumen de soporte elegido. Por tanto, cuando una densidad externa se multiplica por `V_SV`, el resultado debe denominarse:

**masa transducida al volumen estructural SV**

y no «masa convencional del universo observable».

Esta distinción es obligatoria en la sección numérica. Impide que una densidad externa inferida dentro de una construcción cosmológica se integre silenciosamente sobre un volumen estructural diferente y se presente después como si no hubiese existido cambio de dominio.

# 7. Teorema 2: nulidad sustancial de la materia oscura

## 7.1. Enunciado

**Teorema 2 — Nulidad sustancial de la materia oscura en el SV.** Sea `Ω` un dominio físico declarado y `B_inv` un inventario material con unidad, frontera, traza, residual y control de doble cómputo explícitos. Sea `ρ_ret^SV(Ω;B_inv)` la materialidad admitida positivamente mediante el protocolo de la sección 4.

Si la magnitud denominada «materia oscura» en un banco `B_cmp`:

- comparece exclusivamente como exceso gravitatorio sobre el inventario material admitido; y
- no retorna como materialidad admitida positivamente bajo `B_inv`;

entonces su contribución sustancial al inventario material admitido es:

```text
ρ_DM,sustancia^SV(Ω;B_inv,B_cmp) = 0                (24)
```

y, sobre un soporte común declarado:

```text
m_DM,sustancia^SV(Ω;B_inv,B_cmp) = 0                (25)
```

El retorno gravitatorio que motivó el término «materia oscura» se conserva y no debe hacerse cero.

## 7.2. Demostración

Una componente material puede producir retorno gravitatorio. La implicación recíproca:

```text
retorno gravitatorio  ⇒  sustancia material identificada       (26)
```

no se sostiene sin evidencia positiva adicional.

Bajo las hipótesis del teorema, la entrada «materia oscura» es introducida por el banco de contraste como exceso entre el retorno gravitatorio y la materialidad ordinaria inventariada. Si ese mismo exceso se incorporara directamente a `ρ_ret^SV` como materia, el inventario denominaría material precisamente al término discutido porque el modelo externo ya lo habría denominado material. Esa operación daría por supuesta la conclusión sustancial que se pretende examinar.

El protocolo positivo de admisión material evalúa, por tanto, al candidato con independencia de su rótulo residual. Por hipótesis, el término genérico «materia oscura» no retorna con identidad material, magnitud, unidad, frontera, traza, retorno propio y soporte no duplicado. En consecuencia, su indicador de admisión es cero en el inventario sustancial:

```text
μ_DM^M = 0                                           (27)
```

Sus contribuciones de densidad material y masa material integrada son, por tanto, las expresadas en (24) y (25). El exceso gravitatorio permanece en los términos de retorno estructural definidos en la sección 8. ∎

## 7.3. Lo que el teorema no niega

El teorema no hace cero ninguna de las siguientes observaciones:

- velocidades orbitales y curvas de rotación;
- deflexión gravitatoria y potenciales reconstruidos por lente gravitacional;
- estimadores dinámicos de masa;
- retornos de cúmulos y cúmulos en colisión;
- anisotropías del fondo cósmico de microondas;
- crecimiento de la estructura a gran escala.

El teorema bloquea únicamente la conversión automática de esos retornos en una entrada del inventario material.

## 7.4. Controles positivos y materia no luminosa

El protocolo de admisión no equivale a «sólo materia luminosa». Un candidato material no luminoso puede ingresar con valor `1` cuando su identidad, magnitud, unidad, soporte y traza retornan positivamente. Un candidato no resuelto puede permanecer en `U`. El teorema tampoco autoriza a reclasificar automáticamente cualquier descubrimiento futuro como materia ordinaria con el único fin de conservar la igualdad nula.

## 7.5. Refutación

Dado que (24) expresa una nulidad sustancial exacta dentro de su alcance, la identificación positiva de una componente material oscura con:

```text
ρ_x > 0                                               (28)
```

refuta la igualdad nula en el dominio cubierto por esa identificación, aunque la componente explique sólo una parte del exceso gravitatorio total.

La cuestión más fuerte —si esa componente explica todo el sector atribuido a materia oscura— es independiente.

Una componente refutadora debe presentar identidad material reproducible, magnitud másica no nula, traza y dominio especificados de manera independiente y evidencia que no se reduzca únicamente al mismo residual que se pretende explicar.

# 8. Capacidad estructural y sutura gravitatoria efectiva

## 8.1. Transducción de curvatura a capacidad

La curvatura pura puede transducirse a una densidad de capacidad estructural:

```text
ρ_cap^SV(T) = Λ_SV,puro(T)c²/(8πG)                  (29)
```

Utilizando (15):

```text
ρ_cap^SV(T) = 3/(8πGT²)                             (30)
```

La ecuación (29) coordina una curvatura inversa cuadrática con una magnitud equivalente en densidad. No establece identidad física entre curvatura y densidad.

## 8.2. Balance rector

Para un dominio y un inventario declarados:

```text
ρ_cap^SV(Ω)
=
ρ_ret^SV(Ω;B_inv)
+
ρ_sut,grav^SV(Ω;B_inv,B_cmp)
+
ρ_C^SV(Ω;B_inv,B_cmp)                               (31)
```

y, por tanto:

```text
ρ_sut,grav^SV
=
ρ_cap^SV - ρ_ret^SV - ρ_C^SV                        (32)
```

El término `ρ_sut,grav^SV` se denomina **densidad gravitatoria efectiva de sutura**. No se reclasifica ni se denomina materia oscura y no ingresa en el inventario material. Es el término estructural que conserva un retorno gravitatorio una vez mantenidas visibles la materialidad admitida y el residual de no clausura.

## 8.3. Residual y no clausura honesta

El residual `ρ_C^SV` no es un término de error desechable. Si el inventario material contiene candidatos no resueltos cuya clausura escalar no está autorizada, la salida correcta no es un escalar falsamente preciso. Debe conservarse un intervalo, una contribución no resuelta tipada o `U`, con causa y banco declarados.

En consecuencia, el valor simplificado:

```text
ρ_sut,grav^SV = ρ_cap^SV - ρ_A^SV                   (33)
```

sólo puede utilizarse como auxiliar inicial explícitamente rotulado cuando los términos `U` y los residuales no sean tratados silenciosamente como cero.

## 8.4. Familias de dominio

El formalismo de sutura es escalable en notación, pero no queda automáticamente validado en todas las escalas. Las distintas familias requieren ejecuciones diferentes:

- dominio cosmológico `Ω_T`;
- dominio galáctico `Ω_gal`;
- dominio de lente gravitacional `Ω_lens`;
- dominio de cúmulo `Ω_cl`;
- dominio compacto `Ω_comp`.

Cada familia exige su propio soporte, inventario, banco, transductor, residual y retorno observable. Un cálculo escalar global no puede presentarse como un modelo ya completado de curvas de rotación, lentes gravitacionales o cúmulos.

# 9. Coordinación dimensional sin identidad física

Los dos teoremas están conectados mediante una transducción formal, pero no sostienen que energía oscura y materia oscura constituyan una sola entidad física observada a dos escalas.

Las dimensiones pertinentes son:

```text
[Λ_SV,puro] = m⁻²

[ρ_cap^SV]
=
[ρ_ret^SV]
=
[ρ_sut,grav^SV]
=
[ρ_C^SV]
=
kg·m⁻³
```

La cadena permitida es:

```text
T
⟶ κ(T)
⟶ Λ_SV,puro(T)
⟶ ρ_cap^SV(T)
⟶ (ρ_ret^SV, ρ_sut,grav^SV, ρ_C^SV)                (34)
```

Quedan excluidas las identidades:

```text
Λ_SV,puro = ρ_sut,grav^SV                            (35)

Λ_SV,puro = ρ_DM                                     (36)

energía oscura = materia oscura como una sola sustancia   (37)
```

El primer teorema retorna una magnitud de curvatura. El segundo gobierna la admisión a materialidad y la clasificación del exceso gravitatorio. Su coordinación es estructural y metrológica, no una fusión ontológica.

# 10. Reproducción numérica y separación de bancos

## 10.1. Entradas declaradas

La instancia numérica utiliza:

```text
T_obs = 4,3549488 × 10¹⁷ s
c     = 299 792 458 m·s⁻¹
G     = 6,67430 × 10⁻¹¹ m³·kg⁻¹·s⁻²
```

Las primeras salidas son:

```text
Λ_SV,puro
=
1,7600043527547774 × 10⁻⁵² m⁻²                      (38)

ρ_cap^SV
=
9,429953786784435 × 10⁻²⁷ kg·m⁻³                    (39)
```

El volumen estructural interno es:

```text
V_SV
=
(4π/3)(cT_obs)³
=
9,321802096489210 × 10⁷⁸ m³                         (40)
```

y la capacidad estructural integrada:

```text
m_cap^SV
=
ρ_cap^SV · V_SV
=
c³T_obs/(2G)
=
8,790416297944350 × 10⁵² kg                          (41)
```

Estas unidades de masa expresan capacidad estructural tras la transducción. No designan masa material oculta.

## 10.2. Origen externo de la instancia inicial de materialidad retornada

La instancia numérica publicada inicialmente empleó una densidad bariónica externa derivada de un banco Planck ΛCDM y un término mínimo de neutrinos masivos. Produjo una escala inicial de materialidad admitida de aproximadamente:

```text
ρ_A^SV(B₀) ≈ 4,3 × 10⁻²⁸ kg·m⁻³                    (42)
```

Esta procedencia debe permanecer explícita. El operador `ρ_ret^SV` se define internamente, pero la instancia numérica de (42) está alimentada externamente y depende del modelo. Una estimación de parámetros cosmológicos no es idéntica a un inventario material directo objeto por objeto.

Por ello, este trabajo distingue:

```text
B_obs,0 = banco cosmológico externo basado en Planck

B_inv,0 = inventario material positivamente admitido que haya quedado
          efectivamente clausurado

B_cmp,0 = banco gravitatorio externo de comparación
```

Cuando estos bancos no coinciden, la discrepancia se conserva como `U` o como residual explícito, en lugar de ocultarse dentro de un único escalar.

## 10.3. Valor auxiliar inicial de sutura

Si sólo se resta el escalar inicial admitido de (42) y los términos no resueltos permanecen conceptualmente activos, la densidad auxiliar de sutura es:

```text
ρ_sut,grav^SV
≈
8,999953786784434 × 10⁻²⁷ kg·m⁻³                    (43)
```

que en una presentación ordinaria debe redondearse a:

```text
9,00 × 10⁻²⁷ kg·m⁻³
```

La masa correspondiente, transducida al volumen estructural SV, es:

```text
m_sut,SI^SV
≈
8,389578807795314 × 10⁵² kg                          (44)
```

Ni (43) ni (44) constituyen un valor final universal ni un inventario de materia oscura material.

## 10.4. Separación respecto del banco cosmológico observacional

Para los valores Planck base-ΛCDM:

```text
H₀  = 67,4 km·s⁻¹·Mpc⁻¹
Ω_m = 0,315
Ω_Λ = 0,685
```

el valor de `Ω_Λ` se declara expresamente porque interviene en (2) y es necesario para reproducir la razón siguiente. Las magnitudes cosmológicas inferidas permanecen externas y dependientes de modelo [6].

La razón:

```text
Λ_obs[B] / Λ_SV,puro ≈ 0,619833980                   (45)
```

compara un retorno mixto dependiente de banco con la curvatura interna del dominio puro. Sin un transductor adicional, esta razón no se utiliza como validación, refutación ni residual físico.

La proximidad del 0,57 % comunicada con anterioridad entre una magnitud integrada normalizada y una suma de componentes externas del sector oscuro no se emplea como evidencia en este trabajo. A lo sumo puede conservarse como reproducción histórica del cálculo de los preprints antecedentes.

# 11. Condiciones de fallo, discriminantes empíricos y dominio abierto

Un resultado teórico no puede quedar inmunizado denominando «diferencia de dominio» a todo conflicto. Las condiciones siguientes delimitan dónde la formulación presente puede fallar o debe permanecer abierta.

## 11.1. Condiciones de fallo del Teorema 1

El teorema ciclo-distancial queda afectado si:

- la ley lineal `V_sep(D)=D/T` no resulta admisible en el dominio reivindicado;
- el campo requiere términos anisótropos o no lineales que invaliden la traza empleada en (16);
- la ley constitutiva (10) no puede justificarse físicamente como proyección de curvatura;
- el `T` pertinente no puede fijarse de manera independiente para una aplicación física;
- la magnitud resultante no retorna el comportamiento que se atribuye a la curvatura cosmológica;
- la correspondencia con bancos observacionales externos exige parámetros libres no declarados o importa silenciosamente el resultado que pretende obtener.

Para la instancia numérica actual, el operador histórico que generó el valor exacto declarado `T_obs` permanece fuera del perímetro documental restituido del presente trabajo. Esto limita la activación empírica independiente de la instancia numérica, pero no modifica el teorema paramétrico (15).

## 11.2. Condiciones de fallo del Teorema 2

La nulidad sustancial queda afectada, en un dominio declarado, si se identifica una componente que:

- posea identidad material reproducible;
- tenga masa o densidad no nula;
- disponga de soporte o frontera declarados;
- deje una traza independiente que no se reduzca únicamente al residual gravitatorio empleado para postularla;
- no sea objeto de doble cómputo con una componente material ya admitida.

Una densidad positiva de esa componente refuta la igualdad nula en el dominio cubierto, aunque explique sólo una fracción del exceso gravitatorio.

## 11.3. Condiciones de fallo de la interpretación de sutura

La interpretación de sutura queda afectada si:

- no puede vincularse a ningún retorno observable más allá de conservar por definición un balance escalar;
- sus transductores específicos de dominio fallan para curvas de rotación, lentes gravitacionales, cúmulos, fondo cósmico de microondas o formación de estructura;
- el residual se utiliza para absorber sin restricción cualquier resultado contrario;
- una misma contribución material se elimina del inventario y se reintroduce después como sutura;
- una inferencia dependiente de banco se presenta como magnitud constitutiva interna.

## 11.4. Dominios abiertos

El presente trabajo deja abiertos:

- la derivación completa del generador histórico exacto del `T_obs` declarado;
- los perfiles radiales galácticos de `ρ_sut,grav^SV`;
- los transductores proyectados de lente gravitacional;
- las ejecuciones en cúmulos y cúmulos en colisión;
- las consecuencias para el crecimiento de perturbaciones y el espectro de potencias del fondo cósmico de microondas;
- la relación entre una curvatura ciclo-distancial constante y bancos de energía oscura dependientes del tiempo;
- una matriz completa de novedad frente a la literatura primaria.

Estos dominios abiertos no quedan clausurados silenciosamente por los dos teoremas globales.

# 12. Discusión

## 12.1. Aportación del primer teorema

La forma algebraica final del Teorema 1 no se presenta como una ecuación desconocida. Su convergencia con la relación de de Sitter es explícita. La aportación teórica propuesta consiste en obtener la misma forma mediante una cadena interna diferente:

```text
T
→ κ(T)
→ V_sep^SV
→ tr(∇V_sep^SV)
→ Λ_SV,puro
```

La cadena no pasa por las ecuaciones de Friedmann, por un `H₀` ajustado ni por un `Ω_Λ` importado. Asigna a `Λ` el estatuto de curvatura ciclo-distancial de un dominio declarado e impide su sustancialización directa como materia del vacío, contenido térmico o fuerza local.

La cuestión científica central no es, por tanto, si (15) resulta algebraicamente compatible con una forma relativista conocida. Es si la ley constitutiva SV (10) posee contenido físico suficiente y si la tasa ciclo-distancial dispone de un retorno susceptible de comprobación independiente.

## 12.2. Aportación del segundo teorema

El Teorema 2 separa la realidad de un retorno gravitatorio de la clasificación material que se le atribuye. Su proposición central no sostiene que todo fenómeno inexplicado sea no material. Sostiene que un residual no adquiere identidad material por el mero hecho de que un modelo eficaz lo represente como componente material.

Esta distinción es relevante porque la evidencia de materia oscura es convergente, pero predominantemente gravitatoria. El SV exige admisión material positiva antes de que el término ingrese en el inventario material. El teorema examina, por tanto, una inferencia; no niega las observaciones.

La densidad gravitatoria efectiva de sutura constituye el término estructural que conserva el retorno una vez separadas la materialidad y la no clausura. No es un candidato de partícula y no se convierte en explicación física por el mero hecho de cerrar algebraicamente un balance. Su adecuación física debe establecerse mediante transductores específicos de dominio.

## 12.3. Por qué los dos teoremas deben permanecer diferenciados

El teorema de la constante cosmológica y el teorema de materia oscura comparten una disciplina contraria a la sustancialización automática de retornos efectivos. Esa disciplina común no convierte sus magnitudes en idénticas.

El primer teorema produce una curvatura. El segundo regula la admisión material y el retorno gravitatorio estructural. La transducción de (29) coordina ambos dominios, pero ninguna ecuación de este trabajo afirma que energía oscura y materia oscura sean una misma sustancia o un mismo campo observado a escalas diferentes.

## 12.4. Relación con la cosmología contemporánea

La cosmología externa proporciona un contraste indispensable:

- las supernovas restringen el régimen acelerado distancia–corrimiento al rojo [2], [3];
- Planck retorna parámetros cosmológicos dependientes de modelo [6];
- las medidas de distancia convencionales distinguen distancias comóvil, de diámetro angular y de luminosidad [4];
- los programas de partículas y de gravedad modificada establecen cargas explicativas alternativas [9]–[11].

El SV no necesita que esos bancos autoricen su derivación interna. Sí necesita confrontarse con ellos para comprobar si las magnitudes derivadas retornan los fenómenos físicos que pretenden abordar.

## 12.5. Límites del presente trabajo teórico

Este trabajo constituye una contribución teórica formal, no una cosmología numérica completa. Proporciona:

- dos enunciados teoremáticos;
- demostraciones dentro del marco declarado;
- retornos dimensionales;
- una instancia numérica global reproducible;
- separación explícita de bancos;
- condiciones de fallo.

Todavía no proporciona un análisis de verosimilitud ajustado, un código de Boltzmann, un ajuste de catálogos de curvas de rotación, una reconstrucción de mapas de lente gravitacional ni un modelo perturbativo de crecimiento. Esos elementos constituyen pruebas posteriores y no premisas que puedan darse por supuestas.

# 13. Conclusión

Este trabajo ha presentado dos teoremas del Sistema Vectorial SV.

El primero parte de una escala ciclo-distancial declarada `T`, define la tasa estructural:

```text
κ(T) = 1/T
```

y aplica la ley constitutiva explícita de curvatura:

```text
Λ_SV = [tr(∇V_sep^SV) · κ]/c²
```

Para un campo de separación isótropo tridimensional deriva:

```text
Λ_SV,puro(T) = 3/(c²T²)
```

El resultado se obtiene con independencia de las ecuaciones de Friedmann. Su forma algebraica final coincide con la relación de curvatura de de Sitter, mientras que su tasa y su dominio son generados internamente por la cadena SV. Para la instancia declarada `T_obs`, la curvatura es:

```text
1,7600043527547774 × 10⁻⁵² m⁻²
```

El segundo teorema establece que un exceso gravitatorio no constituye, por sí solo, una sustancia material. Cuando el término genérico «materia oscura» comparece únicamente como inferencia gravitatoria y no supera la admisión material positiva, su contribución sustancial al inventario es exactamente nula:

```text
ρ_DM,sustancia^SV = 0
m_DM,sustancia^SV = 0
```

El retorno gravitatorio permanece físicamente activo y se conserva mediante materialidad retornada, densidad gravitatoria efectiva de sutura y un residual explícito de no clausura.

Los dos teoremas están coordinados, pero no identificados. La curvatura tiene dimensión `m⁻²`; la densidad gravitatoria efectiva de sutura tiene dimensión `kg·m⁻³`. La literatura cosmológica y astrofísica externa se utiliza como banco de contraste y retorno, no como fundamento constitutivo de los resultados SV.

El trabajo siguiente exigido es la ejecución empírica por dominios: determinación independiente de la escala ciclo-distancial, transductores galácticos y de lente gravitacional, aplicaciones a cúmulos, crecimiento de perturbaciones y confrontación explícita con verosimilitudes cosmológicas. El presente trabajo fija los objetos teóricos que esas pruebas deberán evaluar.

# Apéndice A. Identidades de reproducibilidad

A partir del Teorema 1:

```text
δΛ_SV,puro / Λ_SV,puro = -2 δT/T                    (46)
```

Para:

```text
R_SV = cT
```

se obtiene:

```text
δR_SV / R_SV = δT/T                                 (47)
```

Para:

```text
V_SV = (4π/3)(cT)³
```

se obtiene:

```text
δV_SV / V_SV = 3 δT/T                               (48)
```

Para:

```text
ρ_cap^SV = 3/(8πGT²)
```

se obtiene:

```text
δρ_cap^SV / ρ_cap^SV = -2 δT/T                      (49)
```

Para:

```text
m_cap^SV = c³T/(2G)
```

se obtiene:

```text
δm_cap^SV / m_cap^SV = δT/T                         (50)
```

# Apéndice B. Declaración mínima de dominio para una ejecución de sutura

Toda aplicación de:

```text
ρ_sut,grav^SV(Ω;B)
```

debe declarar:

- dominio `Ω`;
- geometría del soporte;
- inventario material `B_inv`;
- banco observacional `B_obs`;
- banco de contraste `B_cmp`;
- unidad y transductor;
- materialidad no resuelta `U`;
- residual `ρ_C^SV`;
- control de doble cómputo;
- retorno observable empleado para la evaluación.

Sin estas declaraciones, un valor de sutura no se admite como resultado físico clausurado.

# Contribución de autoría según CRediT

**Juan Antonio Lloret Egea:** conceptualización; análisis formal; investigación; metodología; administración del proyecto; recursos; validación; redacción del borrador original; revisión y edición.

# Financiación

Esta investigación no recibió financiación específica de organismos del sector público, comercial o sin ánimo de lucro.

# Declaración de intereses

El autor declara que no existen intereses financieros concurrentes ni relaciones personales conocidas que pudieran haber influido en el trabajo presentado.

# Disponibilidad de datos y código

En este estudio no se generaron ni analizaron nuevos datos empíricos. Todos los resultados numéricos pueden reproducirse a partir de las ecuaciones y constantes consignadas en el trabajo. Se dispone de un guion de reproducción en Python y de su salida como material suplementario. Los preprints antecedentes que sustentan el desarrollo formal se citan por DOI.

# Declaración sobre el uso de inteligencia artificial generativa y tecnologías asistidas por IA durante la preparación del manuscrito

Durante la preparación de este trabajo, el autor utilizó ChatGPT de OpenAI (GPT-5.6 Thinking) y Claude de Anthropic (Claude Opus 5) para la redacción en lengua inglesa, la organización estructural, la revisión adversarial y la crítica editorial del manuscrito internacional del que deriva el presente preprint. Tras utilizar estas herramientas, el autor revisó y editó el contenido según fue necesario y asume plena responsabilidad sobre el contenido del trabajo. La concepción científica, los trabajos teóricos previos, el marco matemático, las ecuaciones, las derivaciones, la selección de fuentes, las interpretaciones físicas, los resultados y las conclusiones pertenecen al autor.

# Referencias

[1] S. M. Carroll, “The cosmological constant”, *Living Reviews in Relativity* 4 (2001) 1. https://doi.org/10.12942/lrr-2001-1.

[2] A. G. Riess et al., “Observational evidence from supernovae for an accelerating universe and a cosmological constant”, *Astronomical Journal* 116 (1998) 1009–1038. https://doi.org/10.1086/300499.

[3] S. Perlmutter et al., “Measurements of Omega and Lambda from 42 high-redshift supernovae”, *Astrophysical Journal* 517 (1999) 565–586. https://doi.org/10.1086/307221.

[4] D. W. Hogg, “Distance measures in cosmology”, arXiv:astro-ph/9905116 (1999). https://doi.org/10.48550/arXiv.astro-ph/9905116.

[5] S. Weinberg, “The cosmological constant problem”, *Reviews of Modern Physics* 61 (1989) 1–23. https://doi.org/10.1103/RevModPhys.61.1.

[6] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters”, *Astronomy & Astrophysics* 641 (2020) A6. https://doi.org/10.1051/0004-6361/201833910.

[7] V. C. Rubin, W. K. Ford Jr., N. Thonnard, “Rotational properties of 21 SC galaxies with a large range of luminosities and radii, from NGC 4605 (R = 4 kpc) to UGC 2885 (R = 122 kpc)”, *Astrophysical Journal* 238 (1980) 471–487. https://doi.org/10.1086/158003.

[8] D. Clowe et al., “A direct empirical proof of the existence of dark matter”, *Astrophysical Journal Letters* 648 (2006) L109–L113. https://doi.org/10.1086/508162.

[9] M. Milgrom, “A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis”, *Astrophysical Journal* 270 (1983) 365–370. https://doi.org/10.1086/161130.

[10] J. D. Bekenstein, “Relativistic gravitation theory for the modified Newtonian dynamics paradigm”, *Physical Review D* 70 (2004) 083509. https://doi.org/10.1103/PhysRevD.70.083509.

[11] E. Verlinde, “Emergent gravity and the dark universe”, *SciPost Physics* 2 (2017) 016. https://doi.org/10.21468/SciPostPhys.2.3.016.

[12] J. A. Lloret Egea, *Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable*, preprint no revisado por pares (22 de mayo de 2026). https://doi.org/10.21428/39829d0b.41afec0f.

[13] J. A. Lloret Egea, *La materia oscura no existe como sustancia: demostración formal de nulidad sustancial, densidad gravitatoria efectiva de sutura y contraste físico escalable*, preprint no revisado por pares (25 de mayo de 2026). https://doi.org/10.21428/39829d0b.7b41835f.

[14] J. A. Lloret Egea, *Radio, frontera y densidad del universo observable — Trilogía Cosmológica, Parte III*, preprint no revisado por pares (16 de junio de 2026). https://doi.org/10.21428/39829d0b.0430adc0.

[15] J. A. Lloret Egea, *Edades relativas del universo observable y de sus objetos físicos*, preprint no revisado por pares (2026). https://doi.org/10.21428/39829d0b.b56ed853.
