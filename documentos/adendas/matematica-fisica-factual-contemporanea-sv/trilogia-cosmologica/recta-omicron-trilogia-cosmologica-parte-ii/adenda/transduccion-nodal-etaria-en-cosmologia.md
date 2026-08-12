# Transducción nodal-etaria en cosmología: DOAN-Ω16 (Lanzadera Ómicron) y coordenada de frontera del universo observable

**Juan Antonio Lloret Egea**  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
ORCID: 0000-0002-6634-3351  
Autor de correspondencia: juanantoniolloretegea@ieee.org

> **Preprint — 10 de agosto de 2026.** Esta versión no ha sido sometida a revisión por pares.

## Resumen

Este trabajo presenta DOAN-Ω16, denominación formal de la construcción originalmente designada **Lanzadera Ómicron**, como un operador nodal-etario que transforma un registro etario de dominio previamente admitido en una coordenada extensional situada. La construcción separa cuatro funciones que pueden confundirse cuando se trabaja con determinaciones de gran escala: un desplazamiento etario respecto de una referencia declarada, un factor estructural constitutivo del dominio, una coordenada nodal adimensional y una escala extensional calibrada localmente. La cadena operativa es:

```text
A_D → ΔA_D → N_A → g_D → ν_D → σ_Ω16 → λ_D
```

Para el dominio observable declarado se adoptan como entradas una edad de acceso de 13 800 000 000 años julianos, una edad de clausura declarada de 27 600 000 000 años julianos y una edad de referencia del Sistema Solar de 4 568 000 000 años julianos. El factor de dominio se define constitutivamente por:

```text
g_D = √[(1 + χ_D)/2]
```

y se mantiene fijo entre el acceso y la frontera; la variación recae en el conteo etario. La construcción devuelve una coordenada de acceso presente y una coordenada positiva de frontera de clausura, ambas referidas al origen terrestre, relacionadas por el factor racional exacto:

```text
2879/1154
```

La coordenada de frontera se coordina después, mediante una descomposición explícita por cambio de origen, con un radio estructural previamente declarado. Esa coordinación no se presenta como una segunda determinación independiente del radio.

A lo largo del trabajo se distinguen identidades racionales exactas, magnitudes evaluadas con multiprecisión, congelaciones históricas de precisión y clases de residual. No se reivindica validación observacional, unicidad universal del factor constitutivo ni equivalencia con las medidas cosmológicas convencionales de distancia.

**Palabras clave:** transducción nodal-etaria; universo observable; coordenada de frontera; operador constitutivo; cambio de origen; fundamentos cosmológicos.

## Antecedentes del preprint

El procedimiento nodal-etario y partes de su formalismo fueron divulgados previamente por el autor en tres preprints españoles no revisados por pares, citados en las referencias [8]–[10]. El presente preprint aísla y reconstruye DOAN-Ω16 como un estudio formal autónomo, con definición explícita del operador, tipado dimensional, genealogía de escala, separación entre acceso y frontera, política de precisión y residuales, comparación funcional con antecedentes y delimitación de su alcance fundacional.

---

# 1. Introducción

La distancia cosmológica no constituye una única magnitud primitiva. La cosmología contemporánea distingue, entre otras, las distancias comóviles radial y transversal, la distancia de diámetro angular, la distancia de luminosidad, el tiempo de retroceso y distintas escalas de horizonte [1]. Cada una se define dentro de un marco observacional o geométrico declarado.

Los métodos de cronómetros cósmicos emplean diferencias de edades galácticas para estimar la tasa de expansión y, a partir de ella, restringir parámetros cosmológicos [2,3]. Los métodos basados en supernovas de tipo Ia pueden inferir distancias de luminosidad sin disponer a priori de un corrimiento al rojo espectroscópico conocido, aunque el corrimiento al rojo continúe siendo una variable del procedimiento [4]. Los algoritmos cosmológicos generales calculan distancias angulares y otras magnitudes dentro de modelos Friedmann-Lemaître parametrizados [5]. La geodesia cronómica ofrece, en otro ámbito físico, un ejemplo de transformación de información temporal o frecuencial en una magnitud espacial o geopotencial mediante una ley física explícita y una calibración [6,7].

La construcción estudiada aquí plantea una cuestión formal diferente:

**¿Puede un registro etario admitido, bajo dominio, referencia, escala y frontera declarados, transformarse en una coordenada extensional situada mediante una cadena completamente tipada?**

El adjetivo **etario** se utiliza en este trabajo con un sentido técnico interno: designa magnitudes formadas a partir de un registro de edad explícitamente declarado. No equivale a probabilidad, no sustituye a la cronología en general y no designa una coordenada temporal cosmológica convencional.

DOAN-Ω16 responde a la cuestión separando el registro de entrada del operador que lo consume. No estima la función de Hubble, no marginaliza sobre corrimiento al rojo, no introduce una nueva distancia Friedmann-Lemaître y no pretende sustituir la determinación observacional de distancias. Transforma una diferencia etaria declarada en una coordenada nodal adimensional y devuelve esa coordenada mediante una escala extensional construida localmente.

El procedimiento fue divulgado previamente en español [8]. Aquella publicación conservó los valores finales de acceso y frontera, pero no reunió en una sola argumentación científica la genealogía completa de la escala, el estatuto constitutivo del factor de dominio, la separación entre firma estructural y variación etaria ni la política de precisión necesaria para reproducir los valores históricos. El presente texto hace explícitos esos elementos. La coordinación de la coordenada de frontera con un radio estructural previamente declarado utiliza únicamente la parte mínima necesaria del marco de cambio de origen formulado en un trabajo relacionado [9].

El análisis queda restringido a la ejecución correspondiente al dominio observable. No se importan construcciones de otros dominios. En particular, se establecen:

1. los tipos declarados de entrada y salida de DOAN-Ω16;
2. la construcción de la escala Ω16 a partir del marco auxiliar Tierra-Luna-Sol;
3. el estatuto constitutivo y las propiedades regulares verificables del factor de dominio;
4. la formación de las coordenadas de acceso y de frontera de clausura;
5. la relación racional exacta entre ambas;
6. la distinción entre identidades exactas y evaluación multiprecisión;
7. la coordinación de la coordenada de frontera situada con un radio estructural mediante cambio de origen;
8. los límites y las condiciones de fallo de la construcción.

No se deriva aquí una teoría general de las edades, no se reivindica exactitud observacional, no se demuestra unicidad universal del factor de dominio y no se decide si la salida es equivalente o incompatible con alguna distancia cosmológica convencional. Ésas son cuestiones independientes.

El esquema tipado fundamental puede representarse sin ambigüedad como:

```text
registro etario
    ↓
diferencia etaria ΔA_D
    ↓
conteo adimensional N_A
    ↓
factor estructural g_D
    ↓
coordenada nodal ν_D
    ↓
escala extensional σ_Ω16
    ↓
coordenada situada λ_D
```

La extensión aparece únicamente en el último tramo, cuando la coordenada nodal adimensional se proyecta mediante la escala Ω16.

# 2. Dominio declarado, entrada y salida situada

## 2.1. Dominio observable declarado

Sea `Ω_obs` el dominio observable declarado para esta ejecución. La notación no designa una totalidad absoluta de la existencia física. Designa el dominio cosmológico concreto al que se adscriben la edad admitida, la clausura declarada, la referencia, el origen y la frontera.

Las entradas declaradas son:

```text
A_Ωobs = 13 800 000 000 a_J                         (1)

F_Ωobs = 27 600 000 000 a_J                         (2)

A_ΩSS  = 4 568 000 000 a_J                          (3)
```

donde `a_J` denota el año juliano.

La ecuación (1) es la edad de acceso admitida del dominio observable declarado; la ecuación (2), su edad de clausura dentro del régimen adoptado; y la ecuación (3), la edad de referencia asignada al Sistema Solar.

Estos valores se reciben como entradas admitidas. Su derivación general queda fuera del alcance de este trabajo. La restricción es esencial: DOAN-Ω16 se evalúa como operador que consume un registro etario tipado, no como teoría general destinada a determinar edades físicas.

## 2.2. Origen situado y frontera

El origen operativo local es la Tierra, denotada `T`. La frontera del dominio observable se representa por:

```text
∂Ω_obs                                                   (4)
```

La salida principal de clausura adopta la forma:

```text
λ_∂ = D_DOAN(T, ∂Ω_obs)                                 (5)
```

Esta magnitud es distinta del radio estructural previamente declarado:

```text
R_U = D(O_U, ∂Ω_obs)                                    (6)
```

cuyo origen es el origen cosmológico formal:

```text
O_U = (0,0)
```

DOAN-Ω16 no introduce una segunda derivación autónoma de `R_U`. Su salida cosmológica propia es una coordenada de frontera referida al origen terrestre. La relación entre (5) y (6) se aborda exclusivamente mediante la descomposición por cambio de origen de la sección 7.

## 2.3. Definición de la salida

Para un dominio declarado `D`, la construcción devuelve:

```text
λ_D = σ_Ω16 · ν_D                                      (7)
```

Dentro de DOAN-Ω16, `λ_D` es una **coordenada extensional nodal-etaria situada**. Cada calificativo cumple una función:

- **situada:** la coordenada está referida a un origen declarado;
- **nodal:** se forma mediante una coordenada interna `ν_D`;
- **etaria:** su entrada variable procede de una diferencia de edades;
- **extensional:** su retorno final porta la dimensión de longitud de la escala Ω16 declarada.

Para la ejecución de clausura del dominio observable:

```text
λ_∂ = λ_Ωobs(T → ∂Ω_obs)                               (8)
```

dentro del régimen formal de la construcción.

La ecuación (8) otorga lectura física interna a la cadena completada. No establece equivalencia observacional con una medida cosmológica convencional. Este trabajo no introduce una regla de equivalencia, un resultado de incompatibilidad ni una transformación entre `λ_∂` y las medidas estándar de distancia cosmológica.

La salida es, positivamente, una coordenada interna del marco DOAN-Ω16 adscrita a una relación origen-frontera declarada. Su lectura métrica procede de la calibración declarada; no presupone una identificación externa con una distancia cosmológica convencional.

## 2.4. Sentido de «determinación»

El término **determinación** se utiliza en sentido formal restringido: unas entradas declaradas y unas reglas constitutivas producen una salida numérica bajo una política explícita de precisión y residuales.

No significa:

- observación directa de la frontera cosmológica;
- incertidumbre empírica igual a cero;
- recuperación independiente del modelo de una distancia convencional;
- validación experimental de la escala Ω16.

# 3. Rama etaria y factor constitutivo de dominio

## 3.1. Diferencia etaria y conteo

Para un dominio `D` y una edad de referencia `A_ref`, se define:

```text
ΔA_D = A_D − A_ref                                     (9)
```

El conteo etario es:

```text
N_A(D|A_ref) = ΔA_D / (1 a_J)                        (10)
```

Como numerador y denominador poseen la misma dimensión temporal:

```text
[N_A] = 1                                              (11)
```

Para el acceso presente:

```text
ΔA_acc = 13 800 000 000 − 4 568 000 000
        = 9 232 000 000 a_J

N_A,acc = 9 232 000 000                               (12)
```

Para la frontera de clausura declarada:

```text
ΔA_∂ = 27 600 000 000 − 4 568 000 000
      = 23 032 000 000 a_J

N_A,∂ = 23 032 000 000                                (13)
```

Una vez fijadas las edades declaradas, ambos conteos son enteros exactos.

## 3.2. Fracción estructural de ciclo

La fracción de ciclo se define por:

```text
χ_D = A_D / F_D                                       (14)
```

Para el estado de acceso admitido del dominio observable:

```text
χ_Ωobs = 13 800 000 000 / 27 600 000 000
       = 1/2                                          (15)
```

`χ_D` es adimensional y no se interpreta como probabilidad.

En la ejecución histórica de DOAN-Ω16, el valor admitido de `χ_Ωobs` actúa como **firma estructural** a partir de la cual se construye el factor de dominio. Una vez fijada la ejecución acceso-frontera, esa firma permanece congelada. El conteo de frontera no sustituye `χ_Ωobs=1/2` por otra fracción.

La distinción evita un error categorial: la variación entre acceso y frontera recae en `N_A`; `χ_D` conserva la firma estructural de la ejecución.

## 3.3. Factor constitutivo

El factor de dominio queda definido por:

```text
g_D = √[(1 + χ_D)/2]                                  (16)
```

Para el dominio observable:

```text
g_Ωobs = √3 / 2                                       (17)
```

La ecuación (16) posee estatuto **constitutivo** dentro de DOAN-Ω16. No se presenta como consecuencia de una ley física universal demostrada con independencia del operador, ni como la única transformación matemáticamente posible de `χ_D`.

Para:

```text
f(χ) = √[(1 + χ)/2],     0 ≤ χ ≤ 1                   (18)
```

se cumplen:

```text
f(0) = 1/√2

f(1) = 1                                               (19)
```

y:

```text
f'(χ)  = 1 / [2√2 √(1+χ)]  > 0                       (20)

f''(χ) = −1 / [4√2 (1+χ)^(3/2)] < 0                  (21)
```

Por tanto, la regla es positiva, creciente y cóncava en el intervalo admitido. Conserva el orden y comprime las diferencias al aproximarse al extremo superior normalizado. Son propiedades verificadas de la definición, no una demostración de necesidad física universal.

## 3.4. Regla de factor congelado y coordenada nodal

Para una misma ejecución declarada:

```text
g_D,acc = g_D,∂                                       (22)
```

En el caso presente:

```text
g_Ωobs,acc = g_Ωobs,∂ = √3/2                          (23)
```

La coordenada nodal adimensional es:

```text
ν_D = N_A · g_D                                       (24)
```

Por tanto:

```text
ν_acc
=
9 232 000 000 · √3/2

=
7 995 146 527,737937586922692312391106845807989...    (25)
```

y:

```text
ν_∂
=
23 032 000 000 · √3/2                                (26)
```

La razón entre frontera y acceso es exacta:

```text
ν_∂ / ν_acc
=
23 032 000 000 / 9 232 000 000
=
2879/1154                                             (27)
```

Ese cociente no depende de la escala extensional posterior porque el mismo factor estructural multiplica ambos conteos.

# 4. Construcción de la escala extensional Ω16

## 4.1. Marco auxiliar de calibración

La escala Ω16 se construye mediante un marco auxiliar Tierra-Luna-Sol. Se emplean los anclajes métricos históricos declarados:

```text
D_TS = 149 597 870 700 m                              (28)

D_TL = 384 400 000 m                                  (29)
```

y los radios:

```text
R_Tierra = 6 371 000 m
R_Luna   = 1 737 400 m
R_Sol    = 695 700 000 m                              (30)
```

Estos valores no se presentan como actualización de las mejores constantes astronómicas disponibles. Son las entradas congeladas de la ejecución histórica Ω16. El propósito consiste en exponer la genealogía interna de la escala y su régimen de precisión, no en recalibrarla silenciosamente con valores posteriores.

## 4.2. Distancia media Luna-Sol y residual solar

Bajo las hipótesis auxiliares de órbita lunar circular, distancia Tierra-Sol fija y ángulo de fase uniformemente distribuido, se define:

```text
d_LS(θ)
=
√(D_TS² + D_TL² − 2 D_TS D_TL cos θ)                (31)
```

Su media angular es:

```text
d̄_LS
=
(1/2π) ∫₀²π
√(D_TS² + D_TL² − 2 D_TS D_TL cos θ) dθ             (32)
```

Con el parámetro:

```text
m = 4 D_TS D_TL / (D_TS + D_TL)²                    (33)
```

y `E(m)` como integral elíptica completa de segunda especie:

```text
d̄_LS
=
[2(D_TS + D_TL)/π] · E(m)                            (34)
```

La evaluación multiprecisión produce:

```text
d̄_LS
=
149 598 117 634,365250679780375539616884... m         (35)
```

El residual solar construido es:

```text
N_s(Sol)
=
d̄_LS − D_TS

=
246 934,365250679780375539616884... m                 (36)
```

La cadena histórica congela el valor a doce decimales:

```text
N_s(Sol)_hist
=
246 934,365250679780 UFE                              (37)
```

En este trabajo, `UFE` designa la unidad extensional utilizada por la construcción Ω16. Como los anclajes métricos de esta ejecución se introducen numéricamente en metros y la escala conserva esa dimensión, los retornos UFE se leen en metros bajo esta calibración declarada. No se reivindica una realización independiente de UFE como unidad del SI.

La cantidad terrestre declarada es:

```text
N_s(Tierra)
=
149 213 470 700 UFE                                   (38)
```

La distancia media lunar-solar no se presenta como una observación astronómica independiente. Es una construcción geométrica auxiliar obtenida a partir de los anclajes declarados; `N_s(Sol)` es, a su vez, un residual interno de esa construcción.

## 4.3. Dos razones y acoplamiento linealizado

Se define la razón potencial:

```text
κ_P
=
N_s(Tierra) / N_s(Sol)

=
604 263,6898615683206487433327670029405...            (39)
```

y la razón radial:

```text
κ_R
=
R_Sol / (R_Tierra + R_Luna)

=
695 700 000 / (6 371 000 + 1 737 400)

=
85,7999112031966849193429036554684031...              (40)
```

El acoplamiento Ω queda definido por:

```text
κ_Ω
=
√(κ_P / κ_R)

=
83,9208414920315806537180865400762813...              (41)
```

La construcción recuperada puede expresarse mediante dos relaciones linealizadas:

```text
Π₁,Ω16:
b − a/√κ_R = 0                                        (42)

Π₂,Ω16:
c − √κ_P · b = 0                                      (43)
```

De su composición resulta:

```text
c
=
a √(κ_P/κ_R)
=
a κ_Ω                                                  (44)
```

Las ecuaciones (42)–(44) establecen una consecuencia interna del acoplamiento declarado. No demuestran que ésta sea la única forma posible de relacionar ambas razones. `κ_Ω` se trata, por tanto, como regla constitutiva de linealización de la calibración Ω16.

## 4.4. Paso extensional

El paso extensional es:

```text
σ_Ω16
=
D_TL · κ_Ω                                            (45)
```

y, empleando el residual solar histórico congelado en la rama de calibración, queda:

```text
σ_Ω16
=
32 259 171 469,536939603289232466005322538473167 UFE  (46)
```

La escala se construye localmente y posteriormente se aplica como mapa extensional de DOAN-Ω16. Esa transferencia forma parte de la definición del operador. No se presenta como ley cosmológica estándar ni como conversión universal calibrada experimentalmente.

La genealogía puede resumirse así:

```text
anclajes Tierra-Luna-Sol
        ↓
media geométrica lunar-solar
        ↓
residual N_s(Sol)
        ↓
κ_P       κ_R
   \     /
    κ_Ω
     ↓
D_TL · κ_Ω
     ↓
σ_Ω16
```

# 5. Operador completo DOAN-Ω16

La rama nodal-etaria y la escala Ω16 se combinan mediante:

```text
λ_D
=
σ_Ω16 · ν_D

=
σ_Ω16 · N_A(D|A_ref) · g_D                          (47)
```

Sustituyendo las definiciones:

```text
λ_D
=
σ_Ω16
· [(A_D − A_ref)/(1 a_J)]
· √[(1 + χ_D)/2]                                     (48)
```

La cadena dimensional es:

```text
a_J
→ a_J
→ 1
→ 1
→ 1
→ UFE
→ UFE                                                  (49)
```

Los tipos fundamentales son:

| Magnitud | Función | Dimensión / unidad | Procedencia | Estatuto |
|---|---|---:|---|---|
| `A_D` | edad admitida del dominio | `a_J` | entrada declarada | entrada |
| `A_ref` | edad de referencia | `a_J` | entrada declarada | entrada |
| `F_D` | edad de clausura declarada | `a_J` | entrada declarada | entrada |
| `χ_D` | fracción estructural de ciclo | 1 | `A_D/F_D` | derivada |
| `g_D` | factor de dominio | 1 | ecuación (16) | constitutivo |
| `N_A` | conteo etario | 1 | ecuación (10) | derivado |
| `ν_D` | coordenada nodal | 1 | ecuación (24) | derivada |
| `κ_P, κ_R, κ_Ω` | razones de escala | 1 | ecuaciones (39)–(41) | constitutivas / derivadas |
| `σ_Ω16` | paso extensional | UFE | ecuación (45) | componente calibrada |
| `λ_D` | coordenada extensional situada | UFE | ecuación (47) | salida |

La salida no es un escalar desnudo. Su interpretación depende del dominio, el origen, la referencia, la escala y la frontera declarados. Un valor numéricamente idéntico acompañado de metadatos diferentes no constituye necesariamente el mismo resultado físico.

# 6. Ejecución en el dominio observable

## 6.1. Acceso presente

Con las ecuaciones anteriores:

```text
N_A,acc = 9 232 000 000

g_Ωobs = √3/2

ν_acc = 9 232 000 000 · √3/2                         (50)
```

La coordenada de acceso es:

```text
λ_acc
=
σ_Ω16 · ν_acc                                         (51)
```

y la rama histórica devuelve:

```text
λ_acc
=
257 916 802 762 371 004 117,802115994805413096538330...
UFE                                                     (52)
```

En notación científica, al nivel de presentación empleado en el manuscrito:

```text
λ_acc ≈ 2,5791680276 × 10²⁰ UFE                       (53)
```

## 6.2. Frontera de clausura

En la edad de clausura declarada se conserva el mismo factor estructural y sólo cambia el conteo etario:

```text
N_A,∂ = 23 032 000 000

ν_∂ = 23 032 000 000 · √3/2                           (54)
```

La coordenada de frontera es:

```text
λ_∂
=
σ_Ω16 · ν_∂                                           (55)
```

y la rama histórica devuelve:

```text
λ_∂
=
643 451 018 330 039 966 078,988121273002412742576995...
UFE                                                     (56)
```

En notación científica:

```text
λ_∂ ≈ 6,4345101833 × 10²⁰ UFE                         (57)
```

El coeficiente de tránsito acceso-frontera es:

```text
κ_∂←acc^SV
=
N_A,∂ / N_A,acc
=
23 032 000 000 / 9 232 000 000
=
2879/1154                                              (58)
```

por lo que:

```text
λ_∂
=
(2879/1154) · λ_acc                                   (59)
```

La ecuación (59) es exacta respecto de la escala común y del factor estructural congelado. Los desarrollos decimales de `λ_acc` y `λ_∂` heredan, en cambio, la política de precisión de `σ_Ω16`.

La ejecución completa queda:

| Elemento | Acceso presente | Frontera de clausura | Estatuto |
|---|---:|---:|---|
| edad de dominio usada en el conteo (`a_J`) | 13 800 000 000 | 27 600 000 000 | declarada |
| edad de referencia (`a_J`) | 4 568 000 000 | 4 568 000 000 | declarada |
| conteo etario `N_A` | 9 232 000 000 | 23 032 000 000 | entero exacto |
| fracción estructural `χ_D` | 1/2 | 1/2 retenido | firma congelada |
| factor constitutivo `g_D` | `√3/2` | `√3/2` | constitutivo |
| salida extensional `λ` | `2,5791680276 × 10²⁰` | `6,4345101833 × 10²⁰` | multiprecisión |

El valor positivo de `λ_∂` establece un resultado formal limitado: **dentro de esta construcción, la clausura etaria no colapsa la coordenada extensional situada a cero**. La afirmación se refiere al operador interno y no se generaliza a todo modelo cosmológico cíclico, terminal o fronterizo.

# 7. Coordinación con el radio estructural

Un trabajo relacionado declara, desde el origen formal, el radio estructural [10]:

```text
R_U
=
130 558 080 521 615 040 000 000 000 m                 (60)
```

El presente trabajo no reproduce ni vuelve a defender toda la derivación de ese radio. Emplea el valor exclusivamente para establecer la descomposición por cambio de origen formulada en el marco radial posterior [9].

Bajo la lectura métrica de la calibración UFE declarada, la coordenada terrestre de frontera es:

```text
R_aux,loc^SV
=
D(Tierra, ∂Ω_obs)
=
λ_∂

=
643 451 018 330 039 966 078,988121273 m                (61)
```

El tramo complementario desde el origen formal hasta la Tierra se obtiene por diferencia:

```text
D(O_U, Tierra)
=
R_U − R_aux,loc^SV

=
130 557 437 070 596 709 960 033 921,011878727 m        (62)
```

Por tanto:

```text
R_U
=
D(O_U, Tierra)
+
D(Tierra, ∂Ω_obs)                                     (63)
```

y la recomposición mostrada es:

```text
130 557 437 070 596 709 960 033 921,011878727
+
643 451 018 330 039 966 078,988121273
=
130 558 080 521 615 040 000 000 000 m                 (64)
```

El residual de (64), a la resolución decimal mostrada, es cero.

Esta igualdad es una **descomposición y recomposición por cambio de origen**. No constituye una segunda derivación independiente ni una validación externa de `R_U`, porque el tramo complementario de (62) se obtiene respecto del total previamente declarado.

La utilidad científica de la relación es más restringida y precisa: la coordenada de frontera producida por DOAN-Ω16 queda coordinada geométricamente con el marco radial declarado sin identificar la Tierra con `O_U`.

# 8. Exactitud, multiprecisión y política de residuales

## 8.1. Identidades exactas

Una vez fijadas las entradas declaradas, son exactos:

```text
N_A,acc = 9 232 000 000

N_A,∂   = 23 032 000 000

g_Ωobs  = √3/2

λ_∂ / λ_acc
=
N_A,∂ / N_A,acc
=
2879/1154                                              (65)
```

Los conteos etarios son enteros exactos. La ecuación (64) es una recomposición decimal exacta a la resolución mostrada.

## 8.2. Magnitudes multiprecisión

La integral elíptica, la media lunar-solar, `N_s(Sol)`, `κ_P`, `κ_R`, `κ_Ω`, `σ_Ω16`, `λ_acc` y `λ_∂` son magnitudes numéricas evaluadas con multiprecisión. No deben describirse como físicamente exactas en todas las cifras que sea posible calcular o imprimir.

La exactitud matemática de una identidad y la cantidad de cifras disponibles en una evaluación numérica son categorías distintas.

## 8.3. Rama histórica y rama de precisión completa

La rama histórica utiliza los valores congelados de `N_s(Sol)` y `σ_Ω16`. Para auditar el efecto de esa congelación se calculó además una rama de precisión completa con 50 cifras decimales de precisión de trabajo.

Escala histórica:

```text
σ_Ω16,hist
=
32 259 171 469,536939603289232466005322538473167...
UFE
```

Escala recalculada sin la congelación histórica:

```text
σ_Ω16,full
≈
32 259 171 469,536939578759238671146760128342077...
UFE                                                     (66)
```

Diferencia:

```text
Δσ
=
σ_Ω16,full − σ_Ω16,hist

≈
−2,452999379485856241041013109 × 10⁻⁸ UFE             (67)
```

La diferencia relativa es del orden de:

```text
−7,60 × 10⁻¹⁹
```

Propagada a las salidas:

```text
Δλ_acc
≈
−196,12089471439659 UFE                                (68)

Δλ_∂
≈
−489,282544092502412 UFE                               (69)
```

Estas diferencias son despreciables frente a la magnitud global de las coordenadas, pero resultan decisivas para el estatuto epistemológico de largas expansiones decimales. La rama histórica se conserva porque reproduce la construcción divulgada; la rama completa muestra qué cambia cuando se recompone la media elíptica sin congelación intermedia.

## 8.4. Clases de residual

| Clase | Definición | Interpretación |
|---|---|---|
| residual algebraico | diferencia entre rutas simbólicas exactas | cero exacto cuando se cumple la identidad |
| residual de representación | diferencia causada por truncación decimal mostrada | numérico |
| residual de congelación | valor de precisión completa menos valor histórico congelado | numérico y declarado |
| residual de recomposición | `R_U − [D(O_U,Tierra)+λ_∂]` | cero a la resolución mostrada |
| incertidumbre de entrada | incertidumbre o estatuto convencional de anclajes externos | externa a la clausura algebraica |
| estatuto de aplicabilidad | dominio, referencia, escala y frontera suficientemente declarados | admisible / rechazado / no resuelto |

La expresión **formalmente exacto** queda siempre condicionada a las entradas, definiciones y régimen de precisión declarados. Nunca equivale a afirmar que la incertidumbre empírica sea cero.

# 9. Vecindad conceptual y antecedentes

La comparación bibliográfica se organiza por proximidad funcional, no por similitud de títulos.

## 9.1. Cronómetros cósmicos

Jimenez y Loeb propusieron utilizar edades relativas de galaxias para acceder a la tasa de expansión y, desde ella, a parámetros cosmológicos [2]. Los desarrollos posteriores de cronómetros cósmicos estiman la tasa de expansión a partir de la evolución espectroscópica diferencial de galaxias pasivas [3].

La cadena funcional puede resumirse como:

```text
edades diferenciales de galaxias
        ↓
dz/dt
        ↓
H(z)
        ↓
restricciones o distancias dependientes del modelo
```

DOAN-Ω16 opera de otra manera: recibe una diferencia de edad de dominio declarada, un factor estructural constitutivo y un paso extensional calibrado para devolver una coordenada situada. No estima `H(z)`.

## 9.2. Geodesia cronómica

La geodesia cronómica transforma diferencias relativas de frecuencia en diferencias de potencial gravitatorio o altura mediante relatividad general y relojes calibrados [6,7].

Constituye un vecino conceptual relevante porque demuestra que información temporal puede sustentar una determinación espacial siempre que existan una ley física de transformación, un sistema de referencia y un presupuesto de incertidumbre explícitos. Sin embargo, sus entradas, su ley física y su salida no coinciden con las de DOAN-Ω16.

## 9.3. Métodos con corrimiento al rojo marginalizado y algoritmos generales de distancia

Barris y Tonry determinaron distancias de luminosidad de supernovas sin requerir un corrimiento al rojo previamente conocido, mediante marginalización sobre esa variable [4]. El método sigue siendo fotométrico y conserva el corrimiento al rojo como variable latente.

Kayser, Helbig y Schramm desarrollaron métodos generales para calcular distancias cosmológicas en modelos Friedmann-Lemaître homogéneos e inhomogéneos como funciones del corrimiento al rojo y de parámetros cosmológicos [5].

Ninguno de esos procedimientos reproduce la cadena DOAN-Ω16.

## 9.4. Taxonomías de distancia

La revisión de Hogg muestra que la terminología de distancia cosmológica es plural y dependiente del modelo [1]. Por esta razón, este trabajo evita afirmar que la coordenada situada de DOAN-Ω16 sea una nueva versión de alguna distancia cosmológica convencional ya nombrada.

Una comparación de esa naturaleza exigiría una transformación específica o un análisis de incompatibilidad que aquí no se realiza.

La comparación funcional puede resumirse así:

| Familia | Entrada temporal / etaria | Salida espacial | Intermedio principal | Relación con DOAN-Ω16 |
|---|---|---|---|---|
| cronómetros cósmicos | edades diferenciales de galaxias | `H(z)` y distancias dependientes del modelo | `dz/dt` | vecino conceptual parcial |
| geodesia cronómica | diferencia de frecuencia de relojes | geopotencial o altura | ley relativista de corrimiento | precedente temporal-espacial; física distinta |
| SN Ia con `z` marginalizado | fotometría, `z` latente | distancia de luminosidad | marginalización de verosimilitud | inferencia observacional, no transducción edad-coordenada |
| algoritmos Friedmann-Lemaître | `z` y parámetros cosmológicos | distancias cosmológicas convencionales | integración FLRW | entradas y magnitudes objetivo distintas |
| DOAN-Ω16 | registro etario de dominio admitido | coordenada de frontera situada | `N_A`, `g_D`, `σ_Ω16` | construcción presente |

La búsqueda realizada no identificó un trabajo previo que ejecute la misma operación funcional completa: partir de un registro etario de dominio admitido, normalizar su desplazamiento respecto de una referencia declarada, conservar una firma estructural congelada entre acceso y frontera y devolver una coordenada extensional situada mediante una calibración local explícita.

Esta formulación describe el resultado de la búsqueda efectuada; **no constituye una afirmación lógica de inexistencia exhaustiva de antecedentes**.

# 10. Interpretación fundacional

## 10.1. Regla constitutiva frente a ley universal

La distinción entre regla constitutiva y ley universal es central.

Las ecuaciones que definen `g_D`, `κ_Ω` y `σ_Ω16` especifican el operador utilizado. Sus consecuencias matemáticas pueden demostrarse, sus dimensiones pueden auditarse y sus salidas pueden reproducirse. Ninguna de esas propiedades implica, por sí sola, que la naturaleza imponga dichas reglas con carácter único.

La afirmación posee dos niveles:

- **clausurado en el nivel del operador:** las definiciones, los tipos, las dimensiones y la ejecución declarada producen una salida reproducible;
- **abierto en el nivel universal:** no se han establecido la unicidad, la necesidad física universal ni la aplicación transdominio irrestricta.

La separación permite evaluar la construcción sin presentar una elección constitutiva como si fuese una ley física descubierta.

## 10.2. La edad como entrada extensional

DOAN-Ω16 no sostiene que el tiempo sea espacio.

Sostiene que una diferencia de edad de dominio, una vez normalizada como conteo adimensional, puede ser transformada mediante un factor estructural declarado y un paso extensional en una coordenada de extensión:

```text
ΔA_D
→ N_A
→ ν_D
→ λ_D
```

La conversión dimensional aparece únicamente en:

```text
λ_D = σ_Ω16 · ν_D
```

Esta estructura tiene analogías formales con otros procedimientos científicos en los que una magnitud temporal o frecuencial sólo adquiere lectura espacial mediante una ley de transformación y una calibración. La analogía no supone identidad física con la geodesia cronómica ni con técnicas de tiempo de vuelo.

## 10.3. Coordenada situada y dependencia del origen

La salida sólo tiene significado completo junto con su origen.

```text
D(Tierra, ∂Ω_obs)
```

no es intercambiable con:

```text
D(O_U, ∂Ω_obs)
```

aunque ambas magnitudes recorran, bajo una misma directriz radial declarada, tramos relacionados de la geometría.

La descomposición por cambio de origen conserva esta diferencia. Eliminar el metadato de origen convertiría una coordenada tipada en un escalar ambiguo.

## 10.4. Clausura sin colapso puntual

La ejecución de clausura produce:

```text
λ_∂ > 0
```

El resultado muestra que, dentro del aparato formal declarado, el final del intervalo etario no implica desaparición de la extensión ni colapso de la coordenada situada a un punto.

Se trata de una propiedad de DOAN-Ω16 y de su asignación de frontera. Una conclusión cosmológica más amplia requeriría identificar dominios, dinámica y observables que este trabajo no aporta.

# 11. Limitaciones y condiciones de fallo falsables

La construcción posee límites explícitos.

1. **Sin validación observacional.** No se presenta una campaña que mida de manera independiente la coordenada de frontera calculada.
2. **Escala constitutiva.** La transferencia de una calibración local Tierra-Luna-Sol a la rama etaria forma parte de la definición del operador; no es una ley cosmológica estándar establecida.
3. **Sin teorema de unicidad.** No se demuestra que el factor `g_D` ni el acoplamiento `κ_Ω` sean universalmente únicos.
4. **Dependencia de las edades declaradas.** La salida depende de las entradas adoptadas; su derivación general no se reabre.
5. **Entradas históricas congeladas.** La escala reproduce la calibración histórica divulgada y no sustituye subrepticiamente esos valores por constantes posteriores.
6. **Sin equivalencia métrica declarada.** No se establece ni se niega equivalencia con medidas estándar de distancia cosmológica.
7. **El cambio de origen no es validación independiente.** La recomposición de la sección 7 comprueba coherencia bajo la descomposición declarada; no constituye una segunda medición de `R_U`.
8. **Dominio restringido.** La extensión a otros dominios exige declarar de manera independiente edad, referencia, firma estructural, aplicabilidad de escala, origen y frontera.

La construcción debe fallar o permanecer no resuelta si se produce cualquiera de las situaciones siguientes:

- el dominio o la referencia no están declarados;
- la diferencia de edad es dimensionalmente inconsistente;
- `χ_D` queda fuera de su intervalo admitido sin una extensión formal de la definición;
- se utiliza una calibración diferente y, pese a ello, se etiqueta el resultado como escala histórica Ω16;
- se identifica la salida de origen terrestre con el radio estructural de origen formal sin cambio de origen;
- se mezclan silenciosamente la rama congelada y la rama de precisión completa;
- una expansión decimal se presenta como certeza observacional.

Estas condiciones hacen evaluable el resultado como afirmación sobre un operador incluso antes de disponer de validación observacional.

# 12. Conclusiones

DOAN-Ω16 ha sido formulado como una construcción nodal-etaria con cadena declarada y auditable. Un registro etario de dominio admitido se transforma en un conteo adimensional, se pondera mediante un factor estructural constitutivo y retorna a extensión mediante la escala Ω16.

Para el dominio observable declarado, el mismo factor congelado:

```text
g_Ωobs = √3/2
```

rige acceso y frontera, mientras el conteo etario cambia de:

```text
9 232 000 000
```

a:

```text
23 032 000 000
```

Las coordenadas resultantes están relacionadas por el factor racional exacto:

```text
2879/1154
```

La escala Ω16 ha quedado reconstruida a partir de su genealogía Tierra-Luna-Sol: media elíptica auxiliar, residual solar, dos razones adimensionales, acoplamiento por raíz cuadrada y congelaciones históricas de precisión. La reconstrucción separa identidades algebraicas exactas, resultados multiprecisión e incertidumbre empírica.

La coordenada de frontera de clausura es un resultado situado Tierra-frontera. Su coordinación con el radio estructural previamente declarado se realiza mediante una descomposición por cambio de origen y una recomposición exacta a la resolución mostrada. La relación no se presenta como una segunda determinación independiente del radio.

El resultado fundacional principal es, por tanto, limitado pero sustantivo: bajo entradas explícitas y reglas constitutivas declaradas, un registro etario de dominio puede transformarse en una coordenada extensional de frontera situada sin confundir edad, estado nodal, escala, origen y radio.

Permanecen abiertas la validación observacional, la comparación métrica con distancias cosmológicas convencionales y la cuestión de la unicidad universal de las reglas constitutivas.

# Financiación

Esta investigación no recibió financiación externa.

# Declaración de intereses

El autor declara que no existen intereses financieros ni no financieros concurrentes que pudieran haber influido en el trabajo.

# Contribución de autoría

**Juan Antonio Lloret Egea:** concepción del estudio; desarrollo del marco teórico y matemático; formulación de la construcción nodal-etaria; realización y verificación de los cálculos; selección y evaluación de fuentes; redacción; revisión; aprobación final.

# Disponibilidad de datos

Todas las entradas numéricas empleadas proceden de las fuentes públicas citadas o de los preprints del autor referenciados. Las ecuaciones, transformaciones, cantidades intermedias y resultados derivados necesarios para reproducir el análisis formal se encuentran en este trabajo y en las fuentes citadas. No se ha generado un nuevo conjunto de datos experimental u observacional.

# Divulgación previa

El procedimiento nodal-etario original y partes de su formalismo fueron divulgados previamente por el autor en tres preprints españoles no revisados por pares [8]–[10]. El presente trabajo aísla y reconstruye DOAN-Ω16 como estudio autónomo, con definición propia del operador, tipado dimensional, genealogía de escala, separación entre acceso y frontera, política de precisión y residuales, comparación de antecedentes, limitaciones y cuestión fundacional.

# Declaración sobre el uso de inteligencia artificial generativa y tecnologías asistidas por IA

Durante la preparación del manuscrito internacional del que deriva este preprint, el autor utilizó ChatGPT de OpenAI (GPT-5.6 Thinking) y Claude de Anthropic (Claude Opus 5) para la redacción en lengua inglesa, la organización estructural, la revisión adversarial y la crítica editorial. Tras utilizar estas herramientas, el autor revisó y editó el contenido según fue necesario y asume plena responsabilidad sobre el contenido del trabajo.

La concepción científica, los trabajos teóricos previos, el marco matemático, las ecuaciones, las derivaciones, la selección de fuentes, las interpretaciones físicas, los resultados y las conclusiones pertenecen al autor.

# Referencias

[1] D. W. Hogg, “Distance measures in cosmology”, arXiv:astro-ph/9905116 (1999). https://doi.org/10.48550/arXiv.astro-ph/9905116.

[2] R. Jimenez y A. Loeb, “Constraining cosmological parameters based on relative galaxy ages”, *Astrophysical Journal* 573, 37–42 (2002). https://doi.org/10.1086/340549.

[3] M. Moresco et al., “Improved constraints on the expansion rate of the Universe up to z ~ 1.1 from the spectroscopic evolution of cosmic chronometers”, *Journal of Cosmology and Astroparticle Physics* 2012(08), 006 (2012). https://doi.org/10.1088/1475-7516/2012/08/006.

[4] B. J. Barris y J. L. Tonry, “Redshift-independent distances to Type Ia supernovae”, arXiv:astro-ph/0408097 (2004).

[5] R. Kayser, P. Helbig y T. Schramm, “A general and practical method for calculating cosmological distances”, *Astronomy and Astrophysics* 318, 680–686 (1997), arXiv:astro-ph/9603028.

[6] P. Delva y J. Lodewyck, “Atomic clocks: new prospects in metrology and geodesy”, *Acta Futura* 7, 67–78 (2013). https://doi.org/10.2420/AF07.2013.67.

[7] H. Denker et al., “Geodetic methods to determine the relativistic redshift at the level of 10⁻¹⁸ in the context of international timescales: a review and practical results”, *Journal of Geodesy* 92, 487–516 (2018). https://doi.org/10.1007/s00190-017-1075-1.

[8] J. A. Lloret Egea, *Recta-Ómicron (Lanzadera) — Trilogía Cosmológica, Parte II*, preprint no revisado por pares (2026). https://doi.org/10.21428/39829d0b.db21f00e.

[9] J. A. Lloret Egea, *Radio, frontera y densidad del universo observable — Trilogía Cosmológica, Parte III*, preprint no revisado por pares (2026). https://doi.org/10.21428/39829d0b.0430adc0.

[10] J. A. Lloret Egea, *Determinación del radio, la superficie y el volumen del Universo — Trilogía Cosmológica, Parte I*, preprint no revisado por pares (2026). https://doi.org/10.21428/39829d0b.101f1d12.
