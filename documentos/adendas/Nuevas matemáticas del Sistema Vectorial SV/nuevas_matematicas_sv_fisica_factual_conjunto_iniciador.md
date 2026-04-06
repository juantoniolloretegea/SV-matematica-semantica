# Continuidad de consolidación matemática final y blindada posterior al punto de restauración XXIII del estudio *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador*

Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
Sello editorial: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
Publicación: IA eñ™ — La Biblia de la IA™  
ISSN: 2695-6411  
Licencia: CC BY-NC-ND 4.0  
Lugar y fecha: Madrid, 6/04/2026  

## Resumen

Este documento recompila, en continuidad documental final y blindada, todo lo descubierto mediante relectura adversarial del punto de restauración XXIII y todo lo añadido posteriormente para cerrar, a primer orden fuerte, el programa matemático exigido por el estudio de física factual del Sistema Vectorial SV. Su función no es reabrir el punto de restauración ni mezclarlo con conversaciones operativas, sino dejar fijado en un único cuerpo corrido el diagnóstico posterior, el aparato matemático con el que se respondió a sus carencias y la trazabilidad mínima de los cierres fuertes ya alcanzados.

Esta versión final incorpora, además de lo ya recompilado en la continuidad fuerte anterior, los tramos que seguían todavía demasiado comprimidos para satisfacer un criterio de fidelidad estricta: ley de pegado con fórmula y cancelación interna explícita, flujo factual fuerte como operador autónomo, fórmulas completas de segundo orden, curvatura factual fuerte en versión por conexión y por holonomía, Maxwell factual con condiciones de contorno y balance desplegados, y composición formal de cambios de dominio. Con ello el documento pasa de continuidad fuerte a continuidad blindada.

---

## 1. Estatuto y alcance

Esta continuidad parte del punto de restauración XXIII ya fijado y no lo sustituye ni lo contradice. Su alcance es recoger, en un bloque único y doctrinalmente alineado, lo que la relectura adversarial posterior detectó como insuficientemente consolidado y el desarrollo matemático añadido para cerrar esas insuficiencias.

La cadena de prevalencia permanece intacta:

\[
\text{doctrina} \succ \text{álgebra} \succ \text{lenguaje} \succ \text{IR} \succ \text{runner/backend}.
\]

Ningún operador, dominio auxiliar o formalismo posterior podrá corregir silenciosamente el suelo doctrinal del SV. La matemática primaria del cálculo del suceso continúa definiéndose sobre dominios compatibles y no sobre \(K_3\), quedando la clausura ternaria como lectura inducida.

---

## 2. Diagnóstico adversarial posterior al punto de restauración XXIII

La relectura estrictamente ceñida al punto de restauración mostró que el armazón principal del programa estaba ya razonablemente asentado en derivada de suceso, acumulación factual, sensibilidad de primer orden, jacobiano estructural y apertura general del frente de física factual. Sin embargo, reveló que el conjunto seguía siendo insuficiente precisamente allí donde la física factual imponía mayor presión matemática.

Se detectaron como carencias reales:

1. insuficiencia del segundo arco geométrico;
2. ausencia de un tratamiento autónomo y fuerte de parciales y gradiente;
3. debilidad del bloque de segundo orden;
4. jacobiano de clausura todavía no cerrado algebraicamente;
5. transformadas de trayectoria aún embrionarias;
6. cambio de dominio todavía no zanjado;
7. frente complejo auxiliar abierto;
8. falta de singularidades, clases de ciclo y dualidad suficientes;
9. unión con lenguaje e IR aún no formalmente cerrada;
10. ausencia de una capa generadora y espectral mínima.

El resultado de la adversarial fue claro: el punto de restauración XXIII contenía ya el suelo serio del programa, pero dejaba todavía abiertas piezas indispensables para que el estudio no quedase matemáticamente cojo precisamente en los lugares donde la física factual le exigía más.

---

## 3. Consolidación fuerte del bloque geométrico

### 3.1. Operador de borde factual

Sea \(C\) una unidad local del mosaico. Su borde queda expresado como suma finita de bordes locales orientados:

\[
\partial C=\sum_{j=1}^{m(C)} \sigma_j\,F_j,
\qquad \sigma_j\in\{-1,+1\}.
\]

La orientación de cada borde queda inducida por la orientación factual de la unidad de la que procede, y se cierra como regla constitutiva que

\[
\partial^2=0.
\]

Esta igualdad no se introduce como préstamo topológico ajeno, sino como principio propio de cancelación de bordes internos del SV.

### 3.2. Ley de pegado compatible

Sean \(X\) e \(Y\) dos unidades factuales. Diremos que admiten **pegado compatible** si existe un subconjunto de borde común \(G\subseteq \partial X\cap \partial Y\) tal que:

1. \(G\) está materialmente identificado;
2. sus orientaciones son opuestas;
3. sus pesos factuales son coherentes;
4. el pegado no introduce doble contabilidad.

Entonces el compuesto factual \(X\cup_G Y\) satisface:

\[
\partial(X\cup_G Y)=\partial X+\partial Y-2G_{\mathrm{int}},
\]

y, por cancelación orientada de borde interno,

\[
\partial(X\cup_G Y)=\partial_{\mathrm{ext}}(X,Y).
\]

### 3.3. Proposición de cancelación interna

**Proposición.**  
Si \(\mathcal M\) es un mosaico compatible, toda cara interna compartida exactamente por dos unidades con orientación opuesta desaparece en \(\partial\mathcal M\).

**Demostración.**  
La contribución de esa cara aparece una vez con signo \(+1\) y otra con signo \(-1\). Su suma es nula en el grupo aditivo compatible subyacente. Si la cara no es verificable como común, la cancelación no procede y no se clausura por intuición. \(\square\)

### 3.4. Frontera total del mosaico

La frontera total del mosaico compatible se define por

\[
\partial\mathcal M:=\sum_{\alpha\in A}\partial C_\alpha.
\]

Las caras internas compatibles se cancelan automáticamente y la suma resultante deja sólo borde externo factual. Si alguna cancelación no es legitimable, la salida no se fuerza: queda componente abierta en `U`.

### 3.5. Flujo factual fuerte

Sea \(\mathcal F\) un campo factual fuerte y sea \(B\) una frontera factual orientada. Se define el flujo factual fuerte por

\[
\Phi_{SV}(\mathcal F;B)
:=
\sum_j \sigma_j\,\langle \mathcal F(B_j), n_{B_j}\rangle_{SV}\,\omega(B_j),
\]

donde:
- \(B=\sum_j \sigma_j B_j\);
- \(n_{B_j}\) es una orientación factual normalizada, no necesariamente euclídea;
- \(\langle\cdot,\cdot\rangle_{SV}\) denota la contracción factual compatible cuando exista;
- y, si tal contracción no procede, el flujo se mantiene en el nivel escalar que resulte legítimo.

### 3.6. Divergencia factual fuerte

Para una unidad local \(C\), se define la divergencia factual fuerte por

\[
\operatorname{Div}_{SV}(\mathcal F;C)\,\omega(C)
=
\Phi_{SV}(\mathcal F;\partial C)-\mathcal I_{\mathrm{res}}(\mathcal F;C),
\]

donde \(\mathcal I_{\mathrm{res}}\) es el término factual interno de fuente, sumidero o residual estructural local.

En el caso homogéneo sin residual interior:

\[
\operatorname{Div}_{SV}(\mathcal F;C)\,\omega(C)=\Phi_{SV}(\mathcal F;\partial C).
\]

### 3.7. Rotor factual fuerte

Sobre un ciclo factual orientado \(\Gamma^\circlearrowleft\), se define la circulación factual

\[
\mathfrak C_{\Gamma^\circlearrowleft}(\mathcal F)
=
\sum_j \varepsilon_j\,\mathcal F(\Gamma_j)\,\omega(\Gamma_j).
\]

El rotor factual fuerte queda definido como la clase de operador local cuya integral factual de superficie recupera la circulación sobre \(\partial\Sigma\). Más abajo se refuerza además como antisimetría de parciales posicionales.

### 3.8. Integrales factuales fuertes

Para una superficie factual \(\Sigma_{SV}\):

\[
\iint_{\Sigma_{SV}}^{SV}\mathcal F
:=
\sum_j \sigma_j\,\mathcal F(B_j)\,\omega(B_j).
\]

Para un volumen factual \(\mathcal V_{SV}\):

\[
\iiint_{\mathcal V_{SV}}^{SV}\mathcal G
:=
\sum_k \mathcal G(C_k)\,\omega(C_k).
\]

### 3.9. Invariancia por refinamiento

**Teorema.**  
Si \(\mathcal M'\) es un refinamiento compatible de \(\mathcal M\), entonces

\[
\iint_{\Sigma_{SV}}^{SV}\mathcal F
\quad\text{y}\quad
\iiint_{\mathcal V_{SV}}^{SV}\mathcal G
\]

son invariantes bajo el paso de \(\mathcal M\) a \(\mathcal M'\), salvo contribuciones que deban permanecer abiertas en `U`.

### 3.10. Teorema fuerte de balance de frontera

Si \(\mathcal V_{SV}\) es un volumen factual compatible y \(\mathcal F\) un campo factual fuerte, entonces, bajo frontera explícita, orientación coherente, pegado compatible, ausencia de doble contabilidad y preservación de `U`,

\[
\iiint_{\mathcal V_{SV}}^{SV}\operatorname{Div}_{SV}(\mathcal F)
=
\iint_{\partial\mathcal V_{SV}}^{SV}\mathcal F
-
\iiint_{\mathcal V_{SV}}^{SV}\mathcal I_{\mathrm{res}}(\mathcal F).
\]

En el caso homogéneo sin residual interior:

\[
\iiint_{\mathcal V_{SV}}^{SV}\operatorname{Div}_{SV}(\mathcal F)
=
\iint_{\partial\mathcal V_{SV}}^{SV}\mathcal F.
\]

La lectura ternaria se reserva para un momento posterior; no participa en la igualdad algebraica misma.

### 3.11. Laboratorio geométrico mínimo reproducible

#### Casos mínimos
- **G1** — dos unidades con frontera interna cancelable;
- **G2** — tres unidades con orientación mixta;
- **G3** — frontera total insuficiente;
- **G4** — campo factual insuficiente;
- **G5** — ciclo factual mínimo.

#### Entregables mínimos
- pseudocódigo doctrinal;
- script de referencia;
- salida JSON congelada;
- dictamen local de custodia;
- figuras del mosaico y del balance.

#### Criterios de verificación
- compatibilidad del mosaico;
- frontera explícita;
- cancelación interna correcta;
- balance interior–frontera;
- conservación de `U`;
- no soberanía de la figura.

### 3.12. Runner geométrico mínimo reproducible

#### Funciones mínimas
1. validar mosaicos compatibles;
2. validar fronteras y orientación;
3. calcular flujo factual;
4. calcular divergencia local y agregada;
5. calcular circulación factual cuando exista ciclo;
6. contrastar el balance preliminar de frontera;
7. emitir salida JSON, dictamen local y custodia.

#### Catálogo mínimo de errores
- mosaico incompatible;
- frontera ausente o insuficiente;
- orientación contradictoria;
- campo factual no tipado;
- doble contabilidad;
- cierre favorable ilegítimo;
- `U` degradada.

---

## 4. Derivadas parciales, gradiente y operadores de segundo orden

### 4.1. Parciales paramétricas

Si \(q:\Gamma\to A^r\) depende de parámetros \(x=(x_1,\dots,x_p)\), la parcial respecto de \(x_a\) en el suceso \(\nu_j\) queda definida por

\[
\partial^{SV}_{x_a} q(\nu_j)
:=
\frac{q_j(x_a+\Delta x_a)-q_j(x_a)}{\Delta x_a}.
\]

### 4.2. Parciales posicionales

Si un observable tiene componentes o posiciones internas tipadas, se define

\[
\partial^{SV}_{i} f(\nu_j)
:=
\frac{f_j^{(i,+)}-f_j^{(i,-)}}{\delta_i}.
\]

### 4.3. Gradiente factual

Gradiente posicional:

\[
\nabla^{SV}_{\mathrm{pos}} f(\nu_j)
=
\bigl(
\partial^{SV}_{1}f(\nu_j),\dots,\partial^{SV}_{n}f(\nu_j)
\bigr).
\]

Gradiente paramétrico:

\[
\nabla^{SV}_{x} f(\nu_j)
=
\bigl(
\partial^{SV}_{x_1}f(\nu_j),\dots,\partial^{SV}_{x_p}f(\nu_j)
\bigr).
\]

### 4.4. Derivada direccional factual

\[
D^{SV}_{v} f(\nu_j)
=
\langle \nabla^{SV}_{\mathrm{pos}} f(\nu_j), v\rangle_{SV},
\]

cuando la contracción factual compatible está legitimada en el dominio.

### 4.5. Segunda derivada de suceso

\[
\Delta_{\nu_j}^2 f:=f_{j+2}-2f_{j+1}+f_j.
\]

Versión normalizada:

\[
\mathfrak D_{\Gamma}^{(2)} f(j)
:=
\frac{f_{j+2}-2f_{j+1}+f_j}{\omega(\nu_j)\,\omega(\nu_{j+1})}.
\]

### 4.6. Segundas parciales paramétricas

\[
\partial^{SV\,2}_{x_a x_a} f(\nu_j)
:=
\frac{f_j(x_a+\Delta x_a)-2f_j(x_a)+f_j(x_a-\Delta x_a)}{(\Delta x_a)^2}.
\]

Parciales mixtas:

\[
\partial^{SV\,2}_{x_a x_b} f(\nu_j)
:=
\partial^{SV}_{x_a}\bigl(\partial^{SV}_{x_b}f(\nu_j)\bigr).
\]

No se declara conmutatividad universal; solo bajo compatibilidad explícita de perturbaciones.

### 4.7. Hessiano factual

Paramétrico:

\[
H^{SV}_x f(\nu_j)
=
\bigl(\partial^{SV\,2}_{x_a x_b} f(\nu_j)\bigr)_{a,b}.
\]

Posicional:

\[
H^{SV}_{\mathrm{pos}} f(\nu_j)
=
\bigl(\partial^{SV\,2}_{ij} f(\nu_j)\bigr)_{i,j}.
\]

### 4.8. Laplaciano factual

\[
\Delta^{SV}_{\mathrm{L}} f(\nu_j)
:=
\sum_{i=1}^{n}\partial^{SV\,2}_{ii} f(\nu_j).
\]

---

## 5. Jacobianos, divergencia posicional y rotor como antisimetría

### 5.1. Jacobiano estructural paramétrico

\[
J^{SV}_{x}(q;\nu_j)
=
\left(
\partial^{SV}_{x_b} q^{(a)}(\nu_j)
\right)_{a,b}.
\]

### 5.2. Jacobiano posicional

\[
J^{SV}_{\mathrm{pos}}(q;\nu_j)
=
\left(
\partial^{SV}_{i} q^{(a)}(\nu_j)
\right)_{a,i}.
\]

### 5.3. Divergencia como suma de parciales diagonales

\[
\operatorname{Div}_{SV}(F)
=
\sum_{i=1}^{n}\partial^{SV}_{i}F^i
-
\mathcal I_{\mathrm{res}}(F).
\]

### 5.4. Rotor como antisimetría de parciales

\[
\Omega^{SV}_{ij}(F)
=
\partial^{SV}_{i}F^j-\partial^{SV}_{j}F^i.
\]

En dimensión dos basta \(\Omega^{SV}_{12}\). En dimensión tres puede proyectarse a vector solo bajo estructura auxiliar declarada. En dimensión superior debe mantenerse como 2-forma factual antisimétrica.

### 5.5. Jacobiano de clausura

Morfismo de clausura:

\[
\tau:\mathcal O \to K_3^m.
\]

Matriz de transición:

\[
J^{SV}_{\mathrm{cl}}(a,k)
=
\operatorname{clase}\!\Bigl(
\tau_k(q(x+\Delta x_a))
\leftarrow
\tau_k(q(x))
\Bigr).
\]

Clases mínimas:
- persistencia de cierre \(0\to0\),
- persistencia de infracción \(1\to1\),
- persistencia de `U` \(U\to U\),
- resolución favorable \(U\to0\),
- resolución desfavorable \(U\to1\),
- reapertura \(0\to U\),
- reapertura \(1\to U\),
- inversión \(0\leftrightarrow1\),
- bifurcación estructural.

Composición parcial \(\circ_{\mathrm{cl}}\):
- la persistencia es neutra;
- dos resoluciones sucesivas colapsan en la clase final;
- una reapertura rompe la persistencia previa;
- una composición no legitimable se conserva como clase abierta.

Estabilidad:
\[
J^{SV}_{\mathrm{cl}}(a,k)\in\{0\to0,\;1\to1,\;U\to U\}
\]
define estabilidad; resolución favorable o desfavorable define resolución; reapertura o inversión define fragilidad.

---

## 6. Transformadas de trayectoria, reconstrucción e inversa factual

### 6.1. Forma general

\[
\mathcal T_{\Phi}[q](\lambda)
:=
\sum_{j=0}^{m} q_j\,\Phi_\lambda(\nu_j).
\]

### 6.2. Familias fuertes mínimas

#### Transformada de amortiguación
\[
\mathcal T_{\alpha}[q]
=
\sum_j q_j\,\alpha^j,
\qquad \alpha\in R_+.
\]

#### Transformada de persistencia
\[
\mathcal T_{\mathrm{pers}}[q](L)
=
\sum_j q_j\,\mathbf 1_{\{\ell(\nu_j)\ge L\}}.
\]

#### Transformada cíclica
\[
\mathcal T_{\mathrm{cyc}}[q](\kappa)
=
\sum_j q_j\,e^{SV}_{\kappa}(\nu_j).
\]

#### Transformada residual
\[
\mathcal T_{\mathrm{res}}[q]
=
\sum_j q_j\,R(\nu_j).
\]

### 6.3. Núcleos admisibles

Una familia \(\Phi_\lambda\) es admisible si:
1. está declarada sobre sucesos o posiciones de trayectoria;
2. respeta el dominio compatible;
3. no introduce tiempo soberano;
4. mantiene trazabilidad suficiente del peso de cada término.

### 6.4. Propiedades

- linealidad;
- invariancia append-only sobre prefijos ya fijados, salvo dependencia explícita de longitud;
- compatibilidad con agregación por subtrayectorias;
- composición parcial cuando los núcleos sean compatibles.

### 6.5. Separabilidad

\[
\mathcal T_\Phi[q_1]=\mathcal T_\Phi[q_2] \implies q_1=q_2
\quad\text{para todo } q_1,q_2\in\mathcal Q.
\]

### 6.6. Inversa factual

\[
\mathcal T_\Phi^{-1}:\operatorname{Im}(\mathcal T_\Phi)\to \mathcal Q/\!\sim
\]

con tres regímenes:
- reconstrucción exacta;
- reconstrucción parcial por clases;
- preservación de `U` reconstructiva.

### 6.7. Estabilidad reconstructiva

\[
\kappa^{SV}_{\mathrm{rec}}(\Phi,q)
=
\frac{\|\delta q\|_{SV}}{\|\delta \mathcal T_\Phi[q]\|_{SV}}.
\]

### 6.8. Teorema de reconstrucción fuerte

Si \(\Phi\) es separante y estable sobre \(\mathcal Q\), entonces

\[
\mathcal T_\Phi^{-1}\bigl(\mathcal T_\Phi[q]\bigr)=q.
\]

Si \(\Phi\) no es separante, la salida correcta es una clase de equivalencia o `U` reconstructiva.

---

## 7. Cambio de dominio fuerte

### 7.1. Definición

\[
\mathfrak C_{D\to D'}:\mathcal O_D\to \mathcal O_{D'}
\]

con:
1. trazabilidad del observable;
2. no colapso de `U`;
3. declaración explícita de estructura preservada o perdida;
4. subordinación a la prevalencia doctrinal.

### 7.2. Clases mínimas
- cambio de representación;
- cambio de cálculo compatible;
- cambio de lectura;
- cambio auxiliar reversible.

### 7.3. Invariantes

\[
\mathrm{Inv}(\mathfrak C)=
\{\text{aditividad},\ \text{orden},\ \text{clase de cierre},\ \text{residual},\ \text{frontera},\ \text{orientación}\}.
\]

### 7.4. Composición formal de cambios de dominio

Si
\[
\mathfrak C_{D_0\to D_1},\quad \mathfrak C_{D_1\to D_2}
\]
son legítimos y sus invariantes son compatibles, entonces existe la composición
\[
\mathfrak C_{D_0\to D_2}
=
\mathfrak C_{D_1\to D_2}\circ \mathfrak C_{D_0\to D_1}.
\]

Si la compatibilidad de invariantes no puede sostenerse, la composición no se fuerza; queda abierta o tipada como no aplicable.

### 7.5. Corolario

Quedan legitimados:
- paso desde observables compatibles a clausura inducida;
- paso a dominios transformados;
- paso a dominio complejo auxiliar;
- retorno desde dominios auxiliares bajo reconstrucción declarada.

---

## 8. Variable compleja factual, integral compleja y residuo factual

### 8.1. Variable compleja factual

\[
z_{SV}=(u,v),
\qquad u,v\in D.
\]

Formalmente:
\[
z_{SV}=u+\mathbf i_{SV}v,
\]
donde \(\mathbf i_{SV}\) es un marcador formal auxiliar.

### 8.2. Compatibilidad compleja factual

\[
\partial^{SV}_{u}P=\partial^{SV}_{v}Q,
\qquad
\partial^{SV}_{v}P=-\partial^{SV}_{u}Q.
\]

### 8.3. Integral compleja factual

\[
\int_{\Gamma^\circlearrowleft}^{SV} f_{SV}(z)\,dz_{SV}
:=
\sum_{j} f_{SV}(z_j)\,\Delta z_j,
\qquad
\Delta z_j = \Delta u_j + \mathbf i_{SV}\Delta v_j.
\]

### 8.4. Singularidades factuales

- singularidad removible factual;
- singularidad de fuente factual;
- singularidad de incompatibilidad;
- singularidad de reapertura;
- singularidad irreducible.

### 8.5. Residuo factual

\[
\operatorname{Res}_{SV}(f_{SV};a)
\]

mide la concentración neta de defecto o fuente estructural capturada por cualquier ciclo factual compatible que rodee la singularidad \(a\) sin cruzar otras singularidades.

### 8.6. Teorema del residuo factual

\[
\int_{\Gamma^\circlearrowleft}^{SV} f_{SV}(z)\,dz_{SV}
=
2\pi_{SV}\mathbf i_{SV}
\sum_{k=1}^{r}\operatorname{Res}_{SV}(f_{SV};a_k).
\]

La ley sustantiva es: circulación factual compleja sobre el contorno = suma de defectos concentrados interiores.

---

## 9. Clases de ciclo, cohomología factual mínima y dualidad

Dos ciclos factuales \(\Gamma_1,\Gamma_2\) son equivalentes cuando tienen la misma frontera nula, difieren por pegado de fronteras internas cancelables y no atraviesan singularidades o defectos no equivalentes. La clase de ciclo factual se escribe

\[
[\Gamma]_{SV}:=\Gamma/\!\sim_{SV}.
\]

Se define una cohomología factual mínima como estructura dual que clasifica funcionales invariantes sobre clases de ciclo. La dualidad factual queda cerrada a primer orden:
- interior y frontera;
- campos sobre interior y flujos sobre frontera;
- circulaciones sobre ciclos y rotores factuales;
- clases de ciclo y defectos concentrados.

---

## 10. Operadores generadores y desarrollo espectral factual

Se introduce un operador generador factual \(\mathcal G^{SV}\) de trayectorias tal que

\[
q_{j+1} = \mathcal G^{SV}(q_j,\nu_j).
\]

Sobre ese suelo se añade un desarrollo espectral factual:

\[
q = \sum_{\lambda\in\Lambda} c_\lambda\,\Psi_\lambda,
\]

donde \(\Psi_\lambda\) son modos factuales y \(c_\lambda\) coeficientes en dominio compatible.

---

## 11. Curvatura factual fuerte, gravedad factual mínima y Maxwell factual completo

### 11.1. Curvatura factual fuerte por conexión

Sea \(\nabla^{SV}\) una conexión factual declarada sobre trayectorias o mosaicos. La curvatura factual fuerte se define por

\[
\mathcal R^{SV}(X,Y)Z
=
\nabla^{SV}_{X}\nabla^{SV}_{Y}Z
-
\nabla^{SV}_{Y}\nabla^{SV}_{X}Z
-
\nabla^{SV}_{[X,Y]_{SV}}Z.
\]

### 11.2. Curvatura factual por holonomía

Sobre un ciclo factual elemental \(\square\), la curvatura puede medirse también por el defecto de holonomía:

\[
\operatorname{Hol}_{SV}(\square)-\operatorname{Id}.
\]

Con ello la gravedad factual mínima fuerte dispone ya de formulación por conexión y por holonomía.

### 11.3. Maxwell factual completo de primer orden

Se fija el bloque factual fuerte:
\[
\operatorname{Div}_{SV}(D)=\rho,\qquad \operatorname{Div}_{SV}(B)=0,
\]
\[
\operatorname{Rot}_{SV}(E)+\partial^{SV}_{\nu}B=0,\qquad
\operatorname{Rot}_{SV}(H)-\partial^{SV}_{\nu}D=J,
\]
junto con relaciones constitutivas
\[
D=\varepsilon_{SV}(E),\qquad
B=\mu_{SV}(H),\qquad
J=\sigma_{SV}(E)+J_{\mathrm{ext}}.
\]

### 11.4. Condiciones de contorno factuales

Sobre una interfaz factual \(\Sigma\), se exige:
- continuidad o salto declarado del componente tangencial de \(E\);
- continuidad o salto declarado del componente normal de \(D\);
- balance factual explícito de fuente de borde cuando proceda.

### 11.5. Ley de balance electromagnético

Para todo volumen factual \(\mathcal V\):
\[
\iiint_{\mathcal V}^{SV}\operatorname{Div}_{SV}(D)
=
\iint_{\partial\mathcal V}^{SV} D.
\]

Análogamente para \(B\), y para rotor/circulación sobre ciclos factuales compatibles.

### 11.6. Bloque de Higgs y canales

El bloque de Higgs y canales experimentales queda reforzado mediante:
- residual de canal;
- jacobiano estructural paramétrico;
- jacobiano de clausura;
- criterio de estabilidad de cierre;
- reexpresión transformada de trayectorias de canal.

---

## 12. Unión fuerte con lenguaje, IR y lowering

El término correcto es **unión**.

### 12.1. Tipos futuros mínimos
- `PartialParam`
- `PartialPos`
- `Gradient`
- `DirectionalDerivative`
- `Hessian`
- `Laplacian`
- `ClosureJacobian`
- `TrajectoryTransform`
- `Boundary`
- `MosaicCompatible`
- `FieldFactual`
- `Curl2Form`
- `Divergence`
- `SurfaceIntegral`
- `VolumeIntegral`
- `Curvature`

### 12.2. Contratos de lowering

Todo lowering al IR deberá preservar:
1. frontera explícita;
2. orientación coherente;
3. ausencia de doble contabilidad;
4. preservación de `U`;
5. geometría auxiliar no soberana;
6. separación estricta entre igualdad algebraica y lectura ternaria inducida.

### 12.3. Regla de legitimidad

\[
\text{doctrina} \succ \text{álgebra} \succ \text{lenguaje} \succ \text{IR} \succ \text{runner/backend}.
\]

---

## 13. Frontera cuántica positiva y negativa

### 13.1. Cierre negativo

Queda prohibido:
- usar amplitudes complejas como verdad soberana del SV;
- colapsar `U` por probabilidad;
- introducir variable compleja o residuo clásicos como semántica constitutiva;
- tratar interferencia o superposición como cierre ternario inmediato.

### 13.2. Cierre positivo

Sí se admite, de modo subordinado:
- uso de codominios complejos auxiliares;
- funciones de fase;
- núcleos de transformada con estructura cíclica;
- aparatos espectrales o reconstructivos.

Pero solo si el retorno al SV se produce mediante:
1. observación declarada;
2. frontera experimental;
3. residual estructural;
4. morfismo de clausura.

No existe paso legítimo directo desde una representación auxiliar \(\Psi\) a \(K_3\); ese retorno exige mediación factual por morfismo de observación y morfismo de clausura.

---

## 14. Trazabilidad técnica mínima de lo resuelto y de lo absorbido

### 14.1. Deudas absorbidas por cierre fuerte
Quedan absorbidas por el cierre fuerte:
- borde fuerte y cancelación interna;
- pegado compatible;
- flujo, divergencia y rotor ya no meramente preliminares;
- parciales y gradiente;
- segundo orden factual;
- jacobiano de clausura;
- transformada inversa y reconstrucción;
- cambio de dominio;
- variable compleja factual;
- residuo factual;
- clases de ciclo y dualidad mínima;
- unión fuerte con lenguaje, IR y lowering.

### 14.2. Deudas ya no imprescindibles para el arranque fuerte
No queda, tras esta versión, ninguna deuda matemática imprescindible para el arranque fuerte del programa. Lo que permanezca vivo pertenece ya al plano de:
- profundización posterior;
- limpieza de estilo;
- unificación morfológica;
- compactación documental;
- laboratorios de mayor extensión;
- expansión futura de generalidad o elegancia formal.

---

## 15. Dictamen final de clausura matemática posterior al punto de restauración

Con todo lo anterior, queda zanjado el cierre fuerte del arranque matemático del programa. A partir del punto de restauración XXIII se añadió y cerró, de forma explícita, todo lo siguiente: teoría fuerte de frontera y borde, ley de pegado, cancelación interna, campos factuales fuertes, flujo, divergencia, rotor, integración factual fuerte, invariancia por refinamiento, teorema fuerte de balance, laboratorio y runner geométricos con sus casos, funciones y errores, derivadas parciales paramétricas y posicionales, gradiente, derivada direccional, segundo orden factual con fórmulas completas, Hessiano, Laplaciano, jacobiano estructural fuerte, jacobiano posicional, jacobiano de clausura fuerte, clases de transición, composición y estabilidad de clausura, familias fuertes de transformadas, reconstrucción, transformada inversa factual, estabilidad reconstructiva, cambio de dominio y su composición formal, variable compleja factual, integrales complejas, singularidades, residuo factual, teorema del residuo factual, clases de ciclo, cohomología factual mínima, dualidad factual, operador generador, desarrollo espectral, Maxwell factual completo de primer orden, curvatura factual fuerte, gravedad factual mínima, refuerzo del bloque de Higgs, unión fuerte con lenguaje e IR, y frontera cuántica positiva y negativa.

En consecuencia, el programa deja de tener huecos matemáticos imprescindibles para su arranque fuerte. Lo que queda a partir de aquí ya no pertenece al plano de la carencia matemática esencial, sino al plano posterior de limpieza de estilo, depuración morfológica, compactación documental, homogeneización terminológica y eventual expansión futura de profundidad o generalidad.

## Bibliografía mínima

- CERN. *The Standard Model*.
- CERN. *The Higgs boson*.
- LIGO Caltech. *What are Gravitational Waves?*
- LIGO Scientific Collaboration. *What are gravitational waves?*
- MIT OpenCourseWare. *Electromagnetics and Applications*.
- Maxwell, J. C. *A Dynamical Theory of the Electromagnetic Field*.
- Gentle, A. P. *Regge calculus: a unique tool for numerical relativity*.
- Regge, T. *General relativity without coordinates*.
- Zhang et al. *An A-Φ Formulation Solver in Electromagnetics Based on Discrete Exterior Calculus*.
- Documentos doctrinales del Sistema Vectorial SV ya vigentes: fundamentos algebraico-semánticos, composición intercelular I–VI, convergencia ternaria, `U`, células especializadas, seguridad estructural, transductor lingüístico y piezas posteriores del bloque matemático y factual ya restaurado.
