# Primitivos metrológicos del Sistema Vectorial SV: instanciaciones contingentes de las constantes fundacionales del Sistema Internacional, justificación algebraica y tabla de equivalencias factuales

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Lugar y fecha:** Madrid, 9/04/2026  
**URL PubPub:** https://www.itvia.online/pub/primitivos-metrologicos-del-sistema-vectorial-sv-instanciaciones-contingentes-de-las-constantes-fundacionales-del-sistema-internacional-justificacion-algebraica-y-tabla-de-equivalencias-factuales/release/1  
**Colección PubPub:** [Nueva Matemática y Física Factual del SV](https://www.itvia.online/nueva-matematica-y-fisica-factual-del-sv)  
**Carpeta de laboratorios GitHub:** [`documentos/adendas/primitivos-metrologicos-sv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/primitivos-metrologicos-sv)

---

## Resumen

El presente documento establece la **articulación metrológica** del [Sistema Vectorial SV](https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3) con el [Sistema Internacional de Unidades (SI)](https://www.bipm.org/en/measurement-units) en su revisión de 2019. Se identifican y justifican las instanciaciones contingentes compatibles mediante las cuales los seis primitivos metrológicos físicamente necesarios del SV quedan formalmente declarados: la Unidad Elemental del Medidor Factual de Ciclo (UE\_MFC) para el tiempo, ya presente en el corpus; y las cinco unidades nuevas aquí declaradas — Unidad Factual de Extensión (UFE) para la longitud, Unidad Factual de Masa (UFM) para la masa, Unidad Factual de Corriente (UFC) para la corriente eléctrica, Unidad Factual de Temperatura (UFT) para la temperatura termodinámica, y Unidad Factual de Cantidad de Entidad (UFCE) para la cantidad de sustancia. La séptima unidad del SI, la candela, se difiere por ser una constante psicofísica sin fundamento físico fundamental. Para cada primitivo se ofrece justificación en prosa, formulación algebraica exacta, tabla de equivalencias y referencia a un laboratorio en Python autocontenido. Todas las declaraciones incluyen la delimitación negativa constitutiva que garantiza la integridad doctrinal del SV: ninguna instanciación contingente importa la teoría física de la que procede la constante ancla.

**Palabras clave:** Sistema Vectorial SV; metrología factual; primitivos metrológicos; Sistema Internacional de Unidades; revisión SI 2019; constante de Planck; constante de Boltzmann; carga elemental; número de Avogadro; velocidad de la luz; frecuencia hiperfina del cesio; Unidad Elemental del Medidor Factual de Ciclo; Unidad Factual de Extensión; Unidad Factual de Masa; Unidad Factual de Corriente; Unidad Factual de Temperatura; Unidad Factual de Cantidad de Entidad; instanciación contingente; delimitación negativa; masa invariante; convergencia ternaria

---

## I. Estatuto del documento y objeto

El Sistema Vectorial SV (Lloret Egea, 2019, 2026a) evalúa estructuras complejas mediante el alfabeto ternario $\{0, 1, U\}$, donde $U$ designa indeterminación estructural honesta, $0$ designa aptitud verificada y $1$ designa no aptitud verificada. Su núcleo opera sobre sucesos, frames vectoriales y observables en el espacio discreto $K_3^n$. La articulación de este núcleo con las magnitudes de la física requiere la declaración explícita de unidades que sirvan de escala para comparar observaciones en dominios físicos con las operaciones del corpus.

El presente documento no refunda ningún primitivo doctrinalmente establecido ni introduce nueva álgebra. Su función es precisa: declarar formalmente los primitivos metrológicos del SV que permiten expresar en términos SV cualquier magnitud del SI, y establecer la tabla de equivalencias bidireccional que hace posible el mapeo sin ambigüedad.

Rigen dos condiciones constitutivas que ninguna declaración puede violar:

$$\text{instanciación contingente} \neq \text{verdad constitutiva del SV}$$

$$\text{adopción de constante ancla} \not\Rightarrow \text{importación de su teoría de origen}$$

La primera condición establece que cada primitivo metrológico declarado en este documento es una elección física reproducible, no una derivación algebraica interna del SV. La segunda establece que adoptar $h$ no importa la mecánica cuántica, adoptar $k_B$ no importa la mecánica estadística, y adoptar $e$ no importa la electrodinámica cuántica. El modelo de toda declaración es el Medidor Factual de Ciclo (Lloret Egea, 2026b, §13), que adoptó el cesio-133 como instanciación física contingente sin que ello introdujera la mecánica cuántica atómica en el corpus SV.

---

## II. Taxonomía de los siete primitivos del SI 2019 y su afinidad con el SV

La revisión del SI aprobada por la 26.ª CGPM en noviembre de 2018 y en vigor desde el 20 de mayo de 2019 define el sistema completo de unidades mediante siete constantes numéricas exactas (BIPM, 2019; Bureau International des Poids et Mesures, 2019):

$$\Delta\nu_{\mathrm{Cs}} = 9\,192\,631\,770 \;\text{Hz}, \quad c = 299\,792\,458 \;\text{m/s}$$

$$h = 6{,}626\,070\,15 \times 10^{-34} \;\text{J\,s}, \quad e = 1{,}602\,176\,634 \times 10^{-19} \;\text{C}$$

$$k_B = 1{,}380\,649 \times 10^{-23} \;\text{J/K}, \quad N_A = 6{,}022\,140\,76 \times 10^{23} \;\text{mol}^{-1}$$

$$K_{cd} = 683 \;\text{lm/W a } 540 \times 10^{12} \;\text{Hz}$$

Antes de adoptar cada una, el corpus SV exige clasificarlas por su afinidad con la ontología discreta y determinista del sistema. La clasificación que emerge del análisis adversarial consolidado es la siguiente:

| Constante | Tipo | Afinidad doctrinal SV | Decisión |
|---|---|---|---|
| $\Delta\nu_{\mathrm{Cs}}$ | Evento discreto contable | Máxima | Primitivo SV pleno — ya declarado |
| $c$ | Constante de propagación universal | Alta | Primitivo SV pleno — se declara aquí |
| $e$ | Cuanto discreto de carga | Alta | Primitivo SV pleno — se declara aquí |
| $N_A$ | Número puro de conteo | Alta | Primitivo SV pleno — se declara aquí |
| $h$ | Constante de acción cuántica | Media — con delimitación | Instanciación contingente con delimitación negativa |
| $k_B$ | Constante de proporcionalidad estadística | Media — con delimitación | Instanciación contingente con delimitación negativa |
| $K_{cd}$ | Constante psicofísica (ojo humano) | Baja | **Diferida** |

La candela se difiere porque $K_{cd}$ es la eficacia luminosa de la radiación verde para el ojo humano promedio según la función de luminosidad CIE 1931. Su base no es física sino psicofísica; varios autores han cuestionado su estatuto de unidad base (Davis, 2020). Si un dominio de aplicación SV requiere fotometría, puede referenciar directamente el SI sin necesidad de elevar $K_{cd}$ a rango de primitivo SV.

---

## III. Primitivo [T] — Unidad Elemental del Medidor Factual de Ciclo (UE\_MFC)

### III.1. Estatuto

La Unidad Elemental del Medidor Factual de Ciclo (UE\_MFC) está ya declarada en el corpus SV en el §13 del conjunto unificado (Lloret Egea, 2026b). Este apartado la presenta junto a los nuevos primitivos para completar la tabla de equivalencias.

### III.2. Justificación

El Medidor Factual de Ciclo (MFC) es el instrumento metrológico factual subordinado al cálculo del suceso del SV. Su unidad elemental, la UE\_MFC, se define como la escala bajo la cual se comparan variaciones factuales en una trayectoria cíclica de referencia sobre la célula canónica $SV(3, 9)$ (Lloret Egea, 2026b, §13.2.2).

La UE\_MFC tiene sustrato discreto propio: el Suceso Activador de Referencia del cesio-133 (SAR\_Cs), la transición hiperfina del cesio-133 empleada por el estándar metrológico contemporáneo del segundo. Contar eventos discretos es exactamente la operación central de la ontología SV; de ahí que la UE\_MFC sea el primitivo con mayor afinidad doctrinal del sistema.

### III.3. Formulación algebraica exacta

La instancia canónica sobre $SV(3,9)$ determina:

$$\mathrm{UE}_{\mathrm{MFC}} = \frac{\Delta\nu_{\mathrm{Cs}}}{n} = \frac{9\,192\,631\,770}{9} = 1\,021\,403\,530 \;\mathrm{SAR}_{\mathrm{Cs}}$$

donde $n = 9$ es el número de posiciones de la célula de referencia $SV(3,9) = SV(b, b^2)$ con $b=3$. La división es exacta (residuo cero). La trayectoria abstracta de referencia tiene longitud estructural $n = 9$ y longitud normalizada $9\,\mathrm{UE}_{\mathrm{MFC}}$.

Equivalencia con el segundo SI:

$$9 \;\mathrm{UE}_{\mathrm{MFC}} = 9\,192\,631\,770 \;\mathrm{SAR}_{\mathrm{Cs}} = 1 \;\text{segundo}_{\mathrm{SI}} \quad \text{(exacto)}$$

Por tanto:

$$1 \;\mathrm{UE}_{\mathrm{MFC}} = \frac{1}{9} \;\text{segundo}_{\mathrm{SI}} \qquad \text{(bajo instanciación contingente SAR\_Cs = Cs-133)}$$

### III.4. Delimitación negativa

La UE\_MFC no introduce el tiempo como primitivo ontológico ni como causa autónoma del cambio factual. El SAR\_Cs es una instanciación física contingente y reproducible; la matemática del MFC opera sobre cualquier suceso activador de referencia discreto compatible (Lloret Egea, 2026b, §13.6.3).

### III.5. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_01_tiempo_ue_mfc.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_01_tiempo_ue_mfc.py)

---

## IV. Primitivo [L] — Unidad Factual de Extensión (UFE)

### IV.1. Justificación

La Unidad Factual de Extensión (UFE) es el primitivo espacial del SV. Se define siguiendo el mismo molde de instanciación contingente que la UE\_MFC: una constante física exacta fija la escala sin que el SV necesite derivarla de su álgebra interna.

La constante ancla es $c = 299\,792\,458 \;\text{m/s}$, exacta por convención desde 1983 y confirmada en el SI 2019 (BIPM, 2019). La UFE es la distancia recorrida por la luz en el vacío durante el intervalo temporal $\frac{1}{c}$ segundo SI, es decir, durante $\frac{9}{299\,792\,458}$ UE\_MFC.

A diferencia de la UE\_MFC, la UFE no tiene sustrato discreto propio en la ontología SV: la carta $\mathbb{R}^2$ auxiliar que soporta representaciones geométricas del SV es externa al corpus, como establece la Definición 3 del aparato TPA (Lloret Egea, 2026b, §TPA.Def3). La legitimidad de la UFE reposa exclusivamente en la instanciación contingente, no en una derivación estructural.

### IV.2. Formulación algebraica exacta

$$1 \;\mathrm{UFE} = c \times \frac{1}{c} \;\text{s} = 1 \;\text{m}_{\mathrm{SI}} \quad \text{(bajo instanciación contingente)}$$

Expresada en unidades temporales SV:

$$1 \;\mathrm{UFE} \;\text{corresponde al intervalo temporal } \frac{9}{299\,792\,458} \;\mathrm{UE}_{\mathrm{MFC}}$$

La fracción irreducible en SAR\_Cs:

$$\frac{\Delta\nu_{\mathrm{Cs}}}{c} = \frac{9\,192\,631\,770}{299\,792\,458} = \frac{656\,616\,555}{21\,413\,747} \approx 30{,}663 \;\mathrm{SAR}_{\mathrm{Cs}}$$

donde $\gcd(9\,192\,631\,770,\; 299\,792\,458) = 14$. Este valor no es entero, lo que confirma que la UFE no tiene un análogo discreto-contable en la ontología SAR\_Cs.

La velocidad de la luz en unidades SV:

$$c = 299\,792\,458 \;\frac{\mathrm{UFE}}{\mathrm{segundo}_{\mathrm{SI}}} = \frac{299\,792\,458}{9} \;\frac{\mathrm{UFE}}{\mathrm{UE}_{\mathrm{MFC}}} \approx 33\,310\,273{,}1 \;\frac{\mathrm{UFE}}{\mathrm{UE}_{\mathrm{MFC}}}$$

Nótese que $c \;\mathrm{mod}\; 9 = 1 \neq 0$: la velocidad de la luz no es múltiplo entero de UE\_MFC por UFE, lo que refleja correctamente la ausencia de sustrato discreto propio para la longitud.

### IV.3. Delimitación negativa

La adopción de $c$ como constante ancla de la UFE no introduce geometría diferencial, relatividad especial ni relatividad general en el SV. $c$ es aquí exclusivamente un número de propagación exacto. Su base teórica en la electrodinámica clásica y en la relatividad es contingente al estándar SI adoptado.

### IV.4. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_02_longitud_ufe.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_02_longitud_ufe.py)

---

## V. Primitivo [M] — Unidad Factual de Masa (UFM)

### V.1. Justificación

La Unidad Factual de Masa (UFM) es el primitivo de masa del SV. La constante ancla es la constante de Planck $h = 6{,}626\,070\,15 \times 10^{-34} \;\text{J\,s}$, exacta por convención del SI 2019 (Bureau International des Poids et Mesures, 2019; Newell et al., 2019).

La UFM no tiene sustrato discreto propio en la ontología SV. $h$ es una constante de proporcionalidad de la mecánica cuántica, una teoría intrínsecamente probabilística. La adopción de $h$ como ancla de escala de la UFM requiere por ello una delimitación negativa constitutiva más extensa que la de la UE\_MFC o la UFE.

El único concepto de masa admisible en el corpus SV es la **masa invariante** $m_0$ (masa en reposo), escalar de Lorentz independiente del observador. La masa relativista $M = \gamma m_0$ depende del sistema de referencia y es incompatible con la doctrina determinista e *observer-independent* del SV, exactamente por las mismas razones por las que los valores ternarios $v_i(S_k) \in \{0,1,U\}$ son independientes del observador: la soberanía del frame $S_k$ es inviolable (Lloret Egea, 2026b, §J3.2).

### V.2. Formulación algebraica exacta

La UFM se define como la unidad de masa tal que:

$$h = 6{,}626\,070\,15 \times 10^{-34} \;\mathrm{UFM} \cdot \mathrm{UFE}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^{-1} \quad \text{(exacto)}$$

Dado que $\mathrm{UFE} = \mathrm{m}_{\mathrm{SI}}$ y $\mathrm{UE}_{\mathrm{MFC}} = \frac{1}{9}\,\mathrm{s}_{\mathrm{SI}}$ bajo las instanciaciones contingentes adoptadas:

$$1 \;\mathrm{UFM} = 1 \;\text{kg}_{\mathrm{SI}} \quad \text{(exacto)}$$

La relación fundamental masa-energía en reposo, única forma admisible en el SV:

$$E_0 = m_0 \cdot c^2 = m_0 \cdot (299\,792\,458)^2 \;\frac{\mathrm{UFE}^2}{\mathrm{UE}_{\mathrm{MFC}}^2} = m_0 \times 8{,}988 \times 10^{16} \;\frac{\mathrm{UFE}^2}{\mathrm{UE}_{\mathrm{MFC}}^2}$$

La masa-energía equivalente del fotón Cs sirve como escala atómica de referencia:

$$m_{\mathrm{Cs}} = \frac{h \cdot \Delta\nu_{\mathrm{Cs}}}{c^2} = \frac{6{,}626\,070\,15 \times 10^{-34} \times 9\,192\,631\,770}{(299\,792\,458)^2} \approx 6{,}777 \times 10^{-41} \;\mathrm{UFM}$$

De modo que $1\;\mathrm{UFM} \approx 1{,}476 \times 10^{40} \times m_{\mathrm{Cs}}$.

### V.3. Delimitación negativa constitutiva

> La adopción de $h = 6{,}626\,070\,15 \times 10^{-34} \;\mathrm{UFM} \cdot \mathrm{UFE}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^{-1}$ como ancla de escala de la Unidad Factual de Masa constituye una instanciación contingente compatible, análogamente a la adopción del SAR\_Cs en el §13 del corpus. Esta adopción **no** introduce en el SV el principio de incertidumbre de Heisenberg, **ni** la estadística de Bose-Einstein o Fermi-Dirac, **ni** ninguna interpretación probabilista de los observables cuánticos. $h$ es aquí exclusivamente un número de escala exacto. Su base teórica en la mecánica cuántica es contingente al estándar SI adoptado, no una verdad constitutiva del Sistema Vectorial SV.

### V.4. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_03_masa_ufm.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_03_masa_ufm.py)

---

## VI. Primitivo [I] — Unidad Factual de Corriente (UFC)

### VI.1. Justificación

La Unidad Factual de Corriente (UFC) es el primitivo eléctrico del SV. La constante ancla es la carga elemental $e = 1{,}602\,176\,634 \times 10^{-19} \;\text{C}$, exacta por convención del SI 2019.

La UFC tiene la mayor afinidad doctrinal de todos los primitivos pendientes, junto con la UFCE. $e$ es el cuanto mínimo de carga eléctrica: discreto, contable y determinista. Su estructura es análoga a la del SAR\_Cs: igual que el SV cuenta transiciones hiperfinas del Cs-133 para el tiempo, contaría eventos de carga elemental para la corriente. La relación $1\;\text{C} = (1/e)$ eventos de carga, con $1/e \approx 6{,}242 \times 10^{18}$ eventos, es directamente expresable en la ontología de conteo del SV.

### VI.2. Formulación algebraica exacta

La UFC se define como la unidad de corriente tal que:

$$e = 1{,}602\,176\,634 \times 10^{-19} \;\mathrm{C} = 1{,}602\,176\,634 \times 10^{-19} \;\mathrm{UFC} \cdot \mathrm{UE}_{\mathrm{MFC}} \quad \text{(exacto)}$$

Equivalentemente, el culombio en unidades SV:

$$1\;\text{C} = \frac{1}{e}\;\mathrm{eventos\;de\;carga} \approx 6{,}242 \times 10^{18}\;\text{eventos por UE\_MFC}$$

Bajo las instanciaciones contingentes adoptadas:

$$1 \;\mathrm{UFC} = 1 \;\text{A}_{\mathrm{SI}} \quad \text{(exacto)}$$

Las principales unidades electromagnéticas derivadas en términos SV (requieren UFM previamente declarada):

$$\text{V} \equiv \frac{\mathrm{UFM} \cdot \mathrm{UFE}^2}{\mathrm{UFC} \cdot \mathrm{UE}_{\mathrm{MFC}}^3}, \quad \Omega \equiv \frac{\mathrm{UFM} \cdot \mathrm{UFE}^2}{\mathrm{UFC}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^3}, \quad \text{T} \equiv \frac{\mathrm{UFM}}{\mathrm{UFC} \cdot \mathrm{UE}_{\mathrm{MFC}}^2}$$

### VI.3. Delimitación negativa

La adopción de $e$ no introduce electrodinámica cuántica en el SV. $e$ es aquí un número de escala exacto y un cuanto de conteo compatible con la ontología SV. Su naturaleza discreta no implica que el SV adopte el modelo del electrón como partícula cuántica.

### VI.4. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_04_corriente_ufc.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_04_corriente_ufc.py)

---

## VII. Primitivo [Θ] — Unidad Factual de Temperatura (UFT)

### VII.1. Justificación

La Unidad Factual de Temperatura (UFT) es el primitivo térmico del SV. La constante ancla es la constante de Boltzmann $k_B = 1{,}380\,649 \times 10^{-23} \;\text{J/K}$, exacta por convención del SI 2019.

Un resultado crítico del análisis adversarial de este documento es la distinción entre **definición** e **implementación** del kelvin. La definición SI 2019 fija $k_B$ sin requerir equilibrio termodinámico, distribuciones estadísticas ni mecánica estadística. Para medir temperatura en laboratorio sí se necesitan esos marcos, pero la **definición** de la UFT es independiente de ellos — del mismo modo que la definición de la UE\_MFC no requiere comprender la mecánica cuántica atómica del cesio para fijar su valor numérico.

La UFT requiere que [T], [L] y [M] estén previamente declarados, pues $k_B$ tiene dimensiones $\text{J} \cdot \text{K}^{-1} = \text{UFM} \cdot \text{UFE}^2 \cdot \text{UE}_{\mathrm{MFC}}^{-2} \cdot \text{UFT}^{-1}$.

### VII.2. Formulación algebraica exacta

La UFT se define como la unidad de temperatura tal que:

$$k_B = 1{,}380\,649 \times 10^{-23} \;\mathrm{UFM} \cdot \mathrm{UFE}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^{-2} \cdot \mathrm{UFT}^{-1} \quad \text{(exacto)}$$

La relación fundamental energía-temperatura (dominio de aplicabilidad: sistemas en equilibrio térmico):

$$E_{\mathrm{térmica}} = k_B \cdot T$$

Bajo las instanciaciones contingentes adoptadas:

$$1 \;\mathrm{UFT} = 1 \;\text{K}_{\mathrm{SI}} \quad \text{(exacto)}$$

La energía térmica por UE\_MFC a temperatura ambiente ($T = 293\;\text{K}$):

$$E_{293} = 1{,}380\,649 \times 10^{-23} \times 293 \approx 4{,}045 \times 10^{-21} \;\mathrm{UFM} \cdot \mathrm{UFE}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^{-2}$$

La constante de gas ideal derivada:

$$R = N_A \cdot k_B = 6{,}022\,140\,76 \times 10^{23} \times 1{,}380\,649 \times 10^{-23} \approx 8{,}314 \;\frac{\mathrm{UFM} \cdot \mathrm{UFE}^2}{\mathrm{UE}_{\mathrm{MFC}}^2 \cdot \mathrm{UFCE} \cdot \mathrm{UFT}}$$

### VII.3. Delimitación negativa constitutiva

> La adopción de $k_B = 1{,}380\,649 \times 10^{-23} \;\mathrm{UFM} \cdot \mathrm{UFE}^2 \cdot \mathrm{UE}_{\mathrm{MFC}}^{-2} \cdot \mathrm{UFT}^{-1}$ como ancla de escala de la Unidad Factual de Temperatura constituye una instanciación contingente compatible. Esta adopción **no** importa la mecánica estadística al SV. **No** introduce la distribución de Maxwell-Boltzmann, **ni** los ensembles de Gibbs, **ni** las fluctuaciones térmicas. $k_B$ es aquí exclusivamente un número de escala exacto. La $U$ honesta del SV es indeterminación estructural; la temperatura termodinámica es una magnitud de equilibrio estadístico. Son categorías ontológicamente distintas que no se confunden ni solapan.

### VII.4. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_05_temperatura_uft.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_05_temperatura_uft.py)

---

## VIII. Primitivo [N] — Unidad Factual de Cantidad de Entidad (UFCE)

### VIII.1. Justificación

La Unidad Factual de Cantidad de Entidad (UFCE) es el primitivo de cantidad de sustancia del SV. La constante ancla es el número de Avogadro $N_A = 6{,}022\,140\,76 \times 10^{23} \;\text{mol}^{-1}$, exacto por convención del SI 2019.

La UFCE es el primitivo con mayor afinidad doctrinal de todos los pendientes, junto con la UFC. $N_A$ es un número puro de conteo — un factor de escala entre la escala atómica y la escala macroquímica — sin dimensión física propia en el sentido en que la tienen el metro o el kilogramo. El SV es un sistema de conteo discreto; $N_A$ extiende esa capacidad de conteo al dominio de las entidades moleculares y atómicas. Además, la UFCE es **independiente** de [T], [L] y [M]: puede declararse en cualquier orden.

### VIII.2. Formulación algebraica exacta

La UFCE se define como la unidad de cantidad de entidad tal que:

$$1 \;\mathrm{UFCE} \text{ contiene exactamente } N_A = 6{,}022\,140\,76 \times 10^{23} \text{ entidades elementales}$$

La constante de gas ideal derivada de $N_A$ y $k_B$:

$$R = N_A \cdot k_B = 8{,}314\,462\,618 \;\frac{\mathrm{UFM} \cdot \mathrm{UFE}^2}{\mathrm{UE}_{\mathrm{MFC}}^2 \cdot \mathrm{UFCE} \cdot \mathrm{UFT}} \quad \text{(exacto)}$$

Bajo las instanciaciones contingentes adoptadas:

$$1 \;\mathrm{UFCE} = 1 \;\text{mol}_{\mathrm{SI}} \quad \text{(exacto)}$$

Análogo de la relación SAR\_Cs / UE\_MFC para la UFCE:

$$\frac{N_A}{\Delta\nu_{\mathrm{Cs}}} = \frac{6{,}022\,140\,76 \times 10^{23}}{9\,192\,631\,770} \approx 6{,}551 \times 10^{13} \;\text{entidades por SAR\_Cs}$$

Este cociente muestra cuántas entidades moleculares corresponden a cada transición hiperfina del cesio: un número muy grande pero finito, coherente con la ontología de conteo del SV.

### VIII.3. Delimitación negativa

La adopción de $N_A$ no introduce química, bioquímica ni física molecular en el SV. $N_A$ es aquí un número puro de referencia para comparar cantidades de entidades elementales.

### VIII.4. Referencia al laboratorio

Laboratorio Python autocontenido: [`lab_06_cantidad_ufce.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_06_cantidad_ufce.py)

---

## IX. Tabla de equivalencias factuales completa

La tabla siguiente recoge el mapeo bidireccional entre los primitivos del SI 2019 y los del SV. La columna «Constante ancla» indica el número exacto que establece la correspondencia. La columna «Delimitación» señala qué no se importa con cada adopción. Las equivalencias son exactas bajo todas las instanciaciones contingentes declaradas en este documento.

| Primitivo SV | Nombre completo (abreviatura) | Dim. | Primitivo SI | Constante ancla | Equivalencia exacta | Delimitación |
|---|---|---|---|---|---|---|
| **Unidad Elemental del Medidor Factual de Ciclo** (UE\_MFC) | [T] | segundo (s) | $\Delta\nu_{\mathrm{Cs}} = 9\,192\,631\,770\;\text{Hz}$ | $9\;\mathrm{UE\_MFC} = 1\;\text{s}$ | No introduce tiempo soberano |
| **Unidad Factual de Extensión** (UFE) | [L] | metro (m) | $c = 299\,792\,458\;\text{m/s}$ | $1\;\mathrm{UFE} = 1\;\text{m}$ | No introduce geometría diferencial |
| **Unidad Factual de Masa** (UFM) | [M] | kilogramo (kg) | $h = 6{,}626\,070\,15{\times}10^{-34}\;\text{J\,s}$ | $1\;\mathrm{UFM} = 1\;\text{kg}$ | No introduce mecánica cuántica |
| **Unidad Factual de Corriente** (UFC) | [I] | amperio (A) | $e = 1{,}602\,176\,634{\times}10^{-19}\;\text{C}$ | $1\;\mathrm{UFC} = 1\;\text{A}$ | No introduce electrodinámica cuántica |
| **Unidad Factual de Temperatura** (UFT) | [Θ] | kelvin (K) | $k_B = 1{,}380\,649{\times}10^{-23}\;\text{J/K}$ | $1\;\mathrm{UFT} = 1\;\text{K}$ | No introduce mecánica estadística |
| **Unidad Factual de Cantidad de Entidad** (UFCE) | [N] | mol (mol) | $N_A = 6{,}022\,140\,76{\times}10^{23}\;\text{mol}^{-1}$ | $1\;\mathrm{UFCE} = 1\;\text{mol}$ | No introduce química molecular |
| — (diferida) | [J] | candela (cd) | $K_{cd} = 683\;\text{lm/W}$ | — | Psicofísica; sin base física fundamental |

Las unidades derivadas más relevantes de la física moderna en notación SV son:

| Magnitud | Símbolo SI | Dimensión SV |
|---|---|---|
| Fuerza | N | $\mathrm{UFM \cdot UFE \cdot UE\_MFC^{-2}}$ |
| Energía | J | $\mathrm{UFM \cdot UFE^2 \cdot UE\_MFC^{-2}}$ |
| Potencia | W | $\mathrm{UFM \cdot UFE^2 \cdot UE\_MFC^{-3}}$ |
| Presión | Pa | $\mathrm{UFM \cdot UFE^{-1} \cdot UE\_MFC^{-2}}$ |
| Voltaje | V | $\mathrm{UFM \cdot UFE^2 \cdot UFC^{-1} \cdot UE\_MFC^{-3}}$ |
| Resistencia | Ω | $\mathrm{UFM \cdot UFE^2 \cdot UFC^{-2} \cdot UE\_MFC^{-3}}$ |
| Capacidad | F | $\mathrm{UFC^2 \cdot UE\_MFC^4 \cdot UFM^{-1} \cdot UFE^{-2}}$ |
| Inductancia | H | $\mathrm{UFM \cdot UFE^2 \cdot UFC^{-2} \cdot UE\_MFC^{-2}}$ |
| Campo magnético | T | $\mathrm{UFM \cdot UFC^{-1} \cdot UE\_MFC^{-2}}$ |
| Entropía | J/K | $\mathrm{UFM \cdot UFE^2 \cdot UE\_MFC^{-2} \cdot UFT^{-1}}$ |
| Masa molar | kg/mol | $\mathrm{UFM \cdot UFCE^{-1}}$ |
| Cte. de gas ideal R | J/(mol·K) | $\mathrm{UFM \cdot UFE^2 \cdot UE\_MFC^{-2} \cdot UFCE^{-1} \cdot UFT^{-1}}$ |

Laboratorio Python con el catálogo completo: [`lab_07_unidades_derivadas.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/laboratorios/lab_07_unidades_derivadas.py)

---

## X. Orden lógico de declaración en el corpus SV

El orden que respeta todas las dependencias jerárquicas es:

$$[\mathrm{T}] \xrightarrow{\Delta\nu_{\mathrm{Cs}}} \mathrm{UE\_MFC} \quad \text{(ya declarado, SS13)}$$

$$[\mathrm{L}] \xrightarrow{c} \mathrm{UFE} \quad \text{(requiere [T])}$$

$$[\mathrm{M}] \xrightarrow{h} \mathrm{UFM} \quad \text{(requiere [T], [L])}$$

$$[\mathrm{I}] \xrightarrow{e} \mathrm{UFC} \quad \text{(requiere [T])}$$

$$[\Theta] \xrightarrow{k_B} \mathrm{UFT} \quad \text{(requiere [T], [L], [M])}$$

$$[\mathrm{N}] \xrightarrow{N_A} \mathrm{UFCE} \quad \text{(independiente de todos los anteriores)}$$

Con [M] + [I] declarados se desbloquean en cadena todos los instrumentos de la mecánica clásica y el electromagnetismo completo. Con [M] + [Θ] se desbloquea la termodinámica. Con [N] se desbloquea la química molar. La cobertura resulta ser el **100 % del catálogo SI útil para física e ingeniería**, con la candela disponible por referencia directa al SI en los dominios de fotometría que la requieran.

---

## XI. Deudas técnicas

**DT-PME-1.** Formalizar un horizonte mínimo para cada nuevo primitivo, análogo al horizonte $\mathcal{H}_{\mathrm{MFC}} = \{\mathrm{SAR}\}$ del Medidor Factual de Ciclo, que especifique con exactitud el tipo de suceso activador de referencia para cada instanciación.

**DT-PME-2.** Estudiar si la naturaleza discreta de $e$ permite construir una «Unidad Elemental de Carga Factual» con sustrato estructural propio en el SV, análoga a la UE\_MFC para el tiempo.

**DT-PME-3.** Delimitar con mayor rigor la condición de aplicabilidad de la UFT: bajo qué condiciones estructurales un dominio evaluado por el SV puede considerarse «en equilibrio térmico» y por tanto tiene temperatura termodinámica bien definida.

**DT-PME-4.** Estudiar extensiones a otras células $SV(b, b^2)$ con particiones exactas compatibles de las constantes ancla.

**DT-PME-5.** Elaborar el documento de adopción formal para el corpus SV de cada primitivo declarado en este documento, siguiendo exactamente el formato del §13 del conjunto unificado (Lloret Egea, 2026b).

---

## Registro de errores del conjunto

Este documento se distribuye junto con un registro formal de los errores detectados durante la auditoría adversarial del conjunto `primitivos-metrologicos-sv`. El archivo documenta cada error encontrado, su gravedad, el archivo afectado, la corrección aplicada y su estado de resolución.

Registro de errores: [`ERRORES.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/ERRORES.md)

---

## Infraestructura laboratorial y operativa del conjunto

La presente publicación se acompaña de una infraestructura autocontenida análoga a la del conjunto matemático unificado ya cerrado. Su función es permitir ejecución local, auditoría dura, trazabilidad del resultado y acceso directo desde GitHub o PubPub sin ambigüedad de rutas.

| Componente | Ruta GitHub |
|---|---|
| Runner maestro | [`runners/runner_maestro.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/runners/runner_maestro.py) |
| Runner rápido | [`runners/runner_rapido.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/runners/runner_rapido.py) |
| Catálogo operativo de errores | [`CATALOGO_ERRORES_EJECUCION.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/CATALOGO_ERRORES_EJECUCION.md) |
| Historial de errores detectados | [`ERRORES.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/ERRORES.md) |
| Conversor HTML/JavaScript | [`web/conversor-si-sv.html`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/web/conversor-si-sv.html) |
| README raíz del paquete | [`README.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/primitivos-metrologicos-sv/README.md) |

Los laboratorios se ejecutan como suite gobernada y no como elementos aislados:

```bash
python runners/runner_maestro.py
python runners/runner_rapido.py
```

La colección PubPub a la que debe dirigir el conjunto, cuando corresponda enlazar colección y no GitHub, es la siguiente:

[https://www.itvia.online/nueva-matematica-y-fisica-factual-del-sv](https://www.itvia.online/nueva-matematica-y-fisica-factual-del-sv)

---

## Bibliografía

Bureau International des Poids et Mesures. (2019). *Le Système International d'Unités (SI) / The International System of Units* (9.ª ed.). BIPM. https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf

Bureau International des Poids et Mesures. (2019). *Resolución 1 de la 26.ª Conferencia General de Pesos y Medidas: Sobre la revisión del Sistema Internacional de Unidades (SI)*. CGPM. https://www.bipm.org/en/-/resolution-cgpm-26-1

Davis, R. S. (2020). Cómo definir las unidades del SI revisado a partir de siete constantes con valores numéricos fijos. *Journal of Research of the National Institute of Standards and Technology*, 125, 125015. https://doi.org/10.6028/jres.125.015

Einstein, A. (1905). ¿Es la inercia de un cuerpo dependiente de su contenido de energía? *Annalen der Physik*, 18, 639-641.

Kibble, B. P. (1975). A measurement of the gyromagnetic ratio of the proton by the strong field method. En A. F. Eves (Ed.), *Atomic masses and fundamental constants 5* (pp. 545-551). Plenum Press.

Lloret Egea, J. A. (2019). *Sistema Vectorial SV: fundamentos, célula y cuerpo algebraico*. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026a). *Fundamentos algebraico-semánticos del Sistema Vectorial SV* (Release 3). Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/3

Lloret Egea, J. A. (2026b). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411.

Lloret Egea, J. A. (2026c). *Convergencia ternaria y gobierno determinista de trayectorias en el Sistema Vectorial SV: tipología de la indeterminación, HNA como teorema y fundamentos de la célula NLP*. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026d). *Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV* (Release 1). Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. https://www.itvia.online/pub/origen-doctrinal-definicion-y-alcance-de-la-u-en-el-sistema-vectorial-sv/release/1

Mohr, P. J., Newell, D. B., y Taylor, B. N. (2016). CODATA recommended values of the fundamental physical constants: 2014. *Reviews of Modern Physics*, 88(3), 035009. https://doi.org/10.1103/RevModPhys.88.035009

Newell, D. B., y Tiesinga, E. (Eds.). (2019). *NIST SP 330: El Sistema Internacional de Unidades (SI)*. National Institute of Standards and Technology. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.330-2019.pdf

Okun, L. B. (1989). The concept of mass. *Physics Today*, 42(6), 31-36. https://doi.org/10.1063/1.881171

Particle Data Group. (2022). Review of particle physics. *Progress of Theoretical and Experimental Physics*, 2022(8), 083C01. https://doi.org/10.1093/ptep/ptac097

Planck, M. (1900). Zur Theorie des Gesetzes der Energieverteilung im Normalspectrum. *Verhandlungen der Deutschen Physikalischen Gesellschaft*, 2, 237-245.

Tolman, R. C. (1987). *Relativity, thermodynamics, and cosmology*. Dover Publications. (Obra original publicada en 1934)

---

## Palabras clave

Sistema Vectorial SV; metrología factual; primitivos metrológicos; Sistema Internacional de Unidades; revisión SI 2019; constante de Planck; constante de Boltzmann; carga elemental; número de Avogadro; velocidad de la luz; frecuencia hiperfina del cesio; Unidad Elemental del Medidor Factual de Ciclo; Unidad Factual de Extensión; Unidad Factual de Masa; Unidad Factual de Corriente; Unidad Factual de Temperatura; Unidad Factual de Cantidad de Entidad; instanciación contingente; delimitación negativa; masa invariante; convergencia ternaria
