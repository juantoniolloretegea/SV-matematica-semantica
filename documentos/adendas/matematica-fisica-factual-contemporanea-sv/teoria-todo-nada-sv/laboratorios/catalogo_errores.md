# Catálogo de códigos de error del conjunto laboratorial reproducible

**Documento canónico vinculado:** [Teoría del TODO y de la NADA en el Sistema Vectorial SV](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv)

**Autor:** Juan Antonio Lloret Egea — ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)
**Editor:** IA eñ™ — La Biblia de la IA™ (ITVIA) — ISSN 2695-6411
**Licencia:** CC BY-NC-ND 4.0 — Protegida por [CEDRO](https://www.cedro.org/english?lng=en)
**© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.**

---

## Cláusula de subordinación

Este catálogo de errores está **subordinado** al documento canónico fijado. Sus códigos derivan literalmente del §24.2 del documento. Cualquier código de error reportado por un laboratorio se interpreta exclusivamente con remisión al documento canónico.

---

## Códigos de error canónicos

### E1 — Pertenencia al alfabeto Σ

**Disparo:** una componente del cómputo no pertenece al alfabeto canónico Σ = { 0, 1, U }.

**Sección doctrinal:** §2.1 (alfabeto del Sistema Vectorial SV).

**Síntoma técnico:** la función `alphabet_check` de `sv_lib.py` retorna False sobre una secuencia de componentes.

**Acción del laboratorio:** abortar y reportar la componente fuera del alfabeto. El veredicto no se emite.

---

### E2 — Restricción arquitectónica n = b² con b ≥ 3

**Disparo:** se intenta operar sobre una célula con n que no satisface la restricción del §3.1 del documento de fundamentos algebraico-semánticos.

**Sección doctrinal:** §1bis.2 (granularidad operatoria) y §2.1 del corpus.

**Síntoma técnico:** un parámetro b < 3 o un n ≠ b² se pasa a una función que requiere célula admisible.

**Acción del laboratorio:** abortar y reportar el parámetro inadmisible. El laboratorio es NO APTO si el caso pretende ser canónico.

---

### E3 — Veredicto contradictorio del motor normativo

**Disparo:** una inscripción factual produce simultáneamente N₀(**v**) ≥ T(n) y N₁(**v**) ≥ T(n).

**Sección doctrinal:** §1bis.3 (motor normativo) y §5.3 del documento de fundamentos algebraico-semánticos (Proposición 6).

**Síntoma técnico:** ningún caso real debería disparar E3, pues la Proposición 6 garantiza unicidad. Si se dispara, indica fallo de construcción del caso de prueba o error en la implementación de los conteos.

**Acción del laboratorio:** abortar y reportar la inscripción contradictoria. Indica error material en el laboratorio o en su entrada.

---

### E4 — Indeterminación crítica con motor cumplido

**Disparo:** el motor normativo alcanza T(n) hacia 0 o 1, pero existe una posición crítica con valor U (N_{U,crit}(**v**) ≠ 0).

**Sección doctrinal:** §1bis.6 (criticidad de parámetros) y §6.3 del documento de movilidad estructural y legitimidad de exposición (condición C4).

**Síntoma técnico:** los conteos cumplen la mayoría cualificada pero la habilitación H falla por C4.

**Acción del laboratorio:** preservar U honesta como veredicto global. No es error operativo del laboratorio: es la disciplina de honestidad cognoscitiva del SV. El laboratorio reporta verdict = U y passes_E7 = False.

---

### E5 — Falsa cita bibliográfica detectada

**Disparo:** un laboratorio detecta una referencia a un objeto canónico (cuadro, axioma, teorema, ley) que no existe en el documento canónico fijado ni en el corpus disponible.

**Sección doctrinal:** transversal (asepsia editorial).

**Síntoma técnico:** una verificación de trazabilidad bibliográfica falla.

**Acción del laboratorio:** abortar y reportar la falsa cita detectada. Es error material grave.

---

### E6 — Desviación numérica sobre cifra

**Disparo:** el cómputo del laboratorio produce una cifra que no coincide con la cifra fijada en el documento (e.g. 163, 19 357, 19 683 sobre SV(9, 3); 144 + 18 + 1 = 163; tabla maestra con Δ_res ≠ 0,00 sobre alguna celda).

**Sección doctrinal:** §1bis.4, §13.5, §20, §21 del documento canónico.

**Síntoma técnico:** la cifra computada por el laboratorio difiere de la cifra esperada extraída literalmente del documento.

**Acción del laboratorio:** abortar y reportar la desviación con cifras computada y esperada. El laboratorio es NO APTO.

---

### E7 — Nulidad estricta de los componentes (código de aptitud)

**Disparo:** verificación de aptitud declarada literalmente en el §24.2 del documento canónico:

> *"(ii) `passes_E7 = True`, donde el código E7 verifica nulidad estricta sobre todos los componentes declarados en la sección de origen."*

**Sección doctrinal:** §24.2 (criterio uniforme de aptitud).

**Síntoma técnico:** la función `passes_E7(components)` de `sv_lib.py` retorna False, esto es, alguna componente vale 1 o U.

**Acción del laboratorio:** reportar passes_E7 = False y dictamen NO APTO. El veredicto del verificador 𝓝★_SV se calcula igualmente y se reporta.

---

## Aptitud del laboratorio

Por el §24.2 del documento canónico:

> *"Un laboratorio es **APTO** si y sólo si su salida cumple las dos condiciones siguientes:*
> *(i) `verdict = 0` sobre la entrada del apartado correspondiente;*
> *(ii) `passes_E7 = True`."*

> *"Un laboratorio es **NO APTO** si `verdict ∈ { 1, U }` sobre la entrada de cierre estructural o si `passes_E7 = False`."*

La aptitud se evalúa por la conjunción estricta de ambas condiciones.
