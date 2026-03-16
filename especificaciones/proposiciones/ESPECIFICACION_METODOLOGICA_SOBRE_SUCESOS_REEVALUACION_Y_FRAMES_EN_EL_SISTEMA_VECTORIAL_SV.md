# ESPECIFICACION_METODOLOGICA_SOBRE_SUCESOS_REEVALUACION_Y_FRAMES_EN_EL_SISTEMA_VECTORIAL_SV

**Fecha:** 16/03/2026  
**Estado:** Especificación metodológica de trabajo  
**Rango:** Pieza subordinada de encuadre  
**Ámbito:** Proyecto SV — régimen ternario canónico `(0,1,U)`

## 1. Objeto

La presente especificación fija una regla metodológica necesaria para el desarrollo ulterior del Sistema Vectorial SV: el sistema no debe describirse como arquitectura regida por el tiempo, sino como arquitectura regida por **horizonte de sucesos, reevaluación discreta y frames resultantes**.

Su finalidad es evitar deslizamientos conceptuales que confundan:

- orden de paso;
- índice de reevaluación;
- medida externa;
- y tiempo constitutivo del sistema.

## 2. Regla constitutiva

La cadena correcta de inteligibilidad del sistema es:

`horizonte de sucesos → suceso → reevaluación → frame → lecturas auxiliares`

De acuerdo con esta regla:

1. el sistema declara un **horizonte de sucesos**;
2. un **suceso** activa o justifica una **reevaluación**;
3. la reevaluación produce un **frame ternario**;
4. y sobre ese frame pueden aplicarse lecturas auxiliares de tipo combinatorio, geométrico o computacional.

Esta cadena tiene prioridad metodológica sobre cualquier descripción basada en cronología o flujo temporal.

## 3. Delimitación negativa

Quedan excluidas, como formulaciones impropias o de riesgo, las siguientes expresiones cuando pretendan describir el núcleo del sistema:

- “evolución temporal del sistema”;
- “dinámica temporal de la U”;
- “trayectoria temporal del frame”;
- “flujo temporal constitutivo”;
- y, en general, toda formulación que otorgue al tiempo el papel de principio interno del sistema.

También queda excluido identificar:

- iteración de cálculo con constitución del objeto;
- orden de actualización con tiempo ontológico;
- o secuencia de estados con cronología sustantiva.

## 4. Estatuto del tiempo

El tiempo no queda prohibido absolutamente, pero su estatuto queda restringido.

En el Sistema Vectorial SV, el tiempo solo puede aparecer como:

1. **medida externa**;
2. **marca observacional**;
3. **dato de registro**;
4. o **coordenada auxiliar de instrumentación**.

No puede aparecer como principio constitutivo primario del sistema.

## 5. Estatuto del índice de paso

Para describir secuencias ordenadas de reevaluación, se recomienda utilizar índices de paso o de revisión del tipo:

`S^(k) → S^(k+1)`

y no notaciones del tipo:

`S_t → S_(t+1)`

si la letra `t` pudiera inducir lectura temporal fuerte.

El índice `k` debe interpretarse como:

- contador de reevaluaciones;
- orden de paso;
- o posición relativa en una secuencia de frames.

Nunca como tiempo interno necesario del sistema.

## 6. Reformulación de las trayectorias de U

A la luz de esta especificación, una trayectoria de `U` no debe entenderse como curva temporal en sentido clásico.

Debe entenderse como:

**secuencia estructural de persistencias, desplazamientos, aperturas o resoluciones del estado `U` entre frames consecutivos inducidos por sucesos y reevaluaciones.**

Por tanto, expresiones del tipo `U ⇒ τ` solo serán legítimas si `τ` se interpreta como **trayectoria estructural por sucesos y reevaluaciones**, no como simple devenir temporal.

## 7. Estatuto del frame

El frame es el resultado formalmente relevante de una reevaluación.

Su lectura puede ser:

- interna, en el propio alfabeto `{0,1,U}`;
- combinatorio-semántica, como palabra cíclica u otra estructura discreta;
- geométrica, mediante carta auxiliar;
- o computacional, mediante representación operativa.

Pero el frame no debe ser confundido con:

- la historia completa del sistema;
- la sucesión total de observaciones;
- ni un instante temporal autosuficiente.

El frame pertenece al plano de resultado estructural, no al de tiempo.

## 8. Relación con cartas auxiliares

Las cartas auxiliares en `R²`, `R³` u otras representaciones no constituyen el sistema.

Su función correcta es:

- leer mejor la morfología del frame;
- hacer visibles ciertos patrones;
- o facilitar comparación y control.

No pueden introducir por sí solas:

- una ontología temporal;
- una dinámica constitutiva;
- ni una explicación geométrica suficiente de los sucesos.

La relación correcta es siempre:

`frame → carta auxiliar`

y no:

`carta auxiliar → fundamento del sistema`

## 9. Consecuencia metodológica para trayectorias y comparaciones

Toda secuencia de frames que se pretenda estudiar en SV deberá declarar explícitamente:

1. cuál es el suceso o clase de sucesos pertinente;
2. cuál es el acto de reevaluación considerado;
3. cuál es el frame resultante;
4. y qué cambia entre un frame y el siguiente.

De este modo, la comparación entre frames no se apoyará en un supuesto flujo temporal, sino en una cadena explícita de sucesos y reevaluaciones.

## 10. Consecuencia operativa para futuras unidades y desarrollos

Toda unidad futura que trabaje sobre:

- trayectorias de `U`;
- visión estructural;
- diálogo estructural;
- análisis geométrico;
- o dinámica de células,

deberá respetar esta regla de formulación:

**antes de hablar de cambio, evolución o trayectoria, deberá identificarse el suceso, la reevaluación y el frame resultante.**

## 11. Cierre

Se fija, por tanto, como criterio metodológico del proyecto SV, que el sistema trabaja sobre horizonte de sucesos y reevaluación discreta, y no sobre tiempo constitutivo.

Esta especificación no modifica la célula ternaria canónica `(0,1,U)`, sino que protege su desarrollo ulterior frente a formulaciones impropias y ordena con mayor precisión el tratamiento de frames, trayectorias y representaciones auxiliares.
