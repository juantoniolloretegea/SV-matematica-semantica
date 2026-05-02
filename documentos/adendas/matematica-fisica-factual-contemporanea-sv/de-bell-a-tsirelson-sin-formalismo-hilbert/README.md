# De Bell a Tsirelson sin formalismo de Hilbert

**Aparato determinista no local del Sistema Vectorial SV con alfabeto ternario, unicidad del correlador angular factual acoplado y derivación estructural de la cota cuántica.**

---

**© 2026. Todos los derechos reservados.**
**Autor:** Juan Antonio Lloret Egea
**ORCID:** 0000-0002-6634-3351
**Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)
**Editor:** IA eñ™ — La Biblia de la IA™
**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0
**Madrid, 02/05/2026**

---

## Resumen

El documento articula la absorción de la cota Bell-local CHSH ≤ 2 (Bell 1964; Clauser, Horne, Shimony, Holt 1969) y de la cota cuántica de Tsirelson 2√2 (Tsirelson 1980) como dos manifestaciones operativas del mismo aparato angular factual acoplado del Sistema Vectorial SV. La articulación distingue cuatro regímenes operativos del aparato CHSH-SV bajo el coeficiente de acoplamiento estructural χ_c:

- **R₀ (χ_c = 0):** Bell exacto sobre 𝔽₂ con T(v; Q) ≡ 0 (mod 2).
- **R₁ (0 < χ_c < χ★(b)):** acoplado subcrítico, sin violación necesaria.
- **R₂ (χ★(b) ≤ χ_c < 1):** acoplado supercrítico, |S_SV| ∈ [2, 2√2).
- **R₂★ (χ_c = 1):** saturación factual de Tsirelson, |S_SV| = 2√2.

El núcleo técnico es el **Teorema de unicidad del coseno factual acoplado** (Teorema 10.2.1 del documento): bajo nueve axiomas estructurales del aparato CHSH-SV, el único correlador angular acoplado admisible es C_SV(δ) = −cos δ. La cota de Tsirelson emerge como saturación de este teorema, sin invocar el formalismo de Hilbert.

## Contenido del repositorio

- **`de-bell-a-tsirelson-sv.md`** — Documento principal con la articulación completa del aparato, los teoremas demostrados (Teorema 6.2.1, Teorema 7.7.1, Teorema 8.2.1, Teorema 10.2.1, Teorema 11.2.1, Teorema 11.3.1, Teorema 11.4.1, Teorema 11.6.1, Teorema 17.2.1) y el ejemplo trabajado de extremo a extremo sobre la célula SV(3, 9).

- **`imagenes/portada.png`** — Representación visual de la articulación operativa entre las cuatro manifestaciones del aparato y la ecuación rectora del nivel trece de la cadena ascendente.

- **`laboratorios/`** — Seis laboratorios reproducibles en Python (LAB-01 a LAB-06), un catálogo de errores y un runner unificado:
  - [LAB-01_saturacion_familia_celulas.py](laboratorios/LAB-01_saturacion_familia_celulas.py) — Saturación factual sobre familia SV(b, b²).
  - [LAB-02_factorizacion_R0.py](laboratorios/LAB-02_factorizacion_R0.py) — Factorización separable y T mod 2 sobre R₀.
  - [LAB-03_monotonia_barrido.py](laboratorios/LAB-03_monotonia_barrido.py) — Monotonía estricta sobre barrido fino de χ_c.
  - [LAB-04_equivalencia_cuantica.py](laboratorios/LAB-04_equivalencia_cuantica.py) — Equivalencia SV ↔ MQ sobre cuádruples.
  - [LAB-05_unicidad_correlador.py](laboratorios/LAB-05_unicidad_correlador.py) — Unicidad del correlador angular factual.
  - [LAB-06_fidelidad_A9.py](laboratorios/LAB-06_fidelidad_A9.py) — Fidelidad angular mínima A9.
  - [CATALOGO-DE-ERRORES.md](laboratorios/CATALOGO-DE-ERRORES.md) — Tolerancias operativas y diagnósticos.
  - [runner.py](laboratorios/runner.py) — Runner unificado que ejecuta los seis laboratorios.

## Ejecución de los laboratorios

Requiere Python 3.8 o superior con NumPy.

```
cd laboratorios
python3 runner.py
```

El runner ejecuta los seis laboratorios secuencialmente y emite un informe global de cumplimiento. Bajo política de no pases silenciosos, todo fallo numérico activa el diagnóstico explícito mediante el catálogo de errores.

## Articulación con el corpus del Sistema Vectorial SV

El documento se inscribe en la operación canónica del corpus, manifestada en absorciones precedentes:

- *Absorción de E₀ = m₀c² como sector basal de reposo en el Sistema Vectorial SV* (Lloret Egea, 2026g).
- *Reducción estructural absoluta de Maxwell al Sistema Vectorial SV* (Lloret Egea, 2026k).
- *Teoría general factual de la luz en el Sistema Vectorial SV* (Lloret Egea, 2026 — luz factual).

El elemento de cierre del corpus es la *Teoría del TODO y de la NADA en el Sistema Vectorial SV* (Lloret Egea, 2026 — todo-nada), donde la articulación R₀ / R₁ / R₂ / R₂★ del aparato CHSH-SV queda subsumida bajo la ecuación rectora ℰ★_TODO,SV(Γ_U; τ) = 0 del nivel trece de la cadena ascendente, conforme al Teorema 17.2.1 del documento.

## Citación recomendada

Lloret Egea, J. A. (2026). *De Bell a Tsirelson sin formalismo de Hilbert: aparato determinista no local del Sistema Vectorial SV con alfabeto ternario, unicidad del correlador angular factual acoplado y derivación estructural de la cota cuántica*. ITVIA, IA eñ™ — La Biblia de la IA™. ISSN 2695-6411.

---
