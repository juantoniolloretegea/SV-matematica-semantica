# Laboratorios reproducibles — 2026l Entropía factual SV

Infraestructura laboratorial autocontenida en Python estándar para verificar numéricamente
todos los cálculos del documento **"Entropía factual e irreversibilidad estructural en el
Sistema Vectorial SV"** (Lloret Egea, 2026l).

---

## Requisitos

- Python 3.8 o superior.
- Sin dependencias externas (todo Python estándar).

---

## Estructura

```
2026l-entropia-factual/
├── README.md                               — este archivo
├── CATALOGO_ERRORES.md                     — grietas detectadas y corregidas
├── sv_core.py                              — primitivas SV compartidas
├── run_all.py                              — ejecuta todos los laboratorios
├── lab_04_4_verificacion_preternaria.py   — verifica §4.4 (3 posiciones, n=3)
├── lab_11_recorrido_consistencia.py        — caso patrón §11 (5 posiciones, n=6)
├── lab_11_10_violacion_simulada.py         — contraste §11.10 retroactivo
├── lab_ejemplo_A_cierre_determinado.py    — ejemplo A: dictamen m_0
├── lab_ejemplo_B_residual_en_U.py          — ejemplo B: dictamen U
├── lab_ejemplo_C_clase_emergente.py        — ejemplo C: dictamen χ_α
├── requirements.txt                        — vacío (solo stdlib)
└── tests/
    └── test_monotonia.py                   — suite de tests de teoremas
```

---

## Uso rápido

Ejecutar un laboratorio concreto:

```bash
python3 lab_11_recorrido_consistencia.py
```

Ejecutar todos los laboratorios y tests en una sola pasada:

```bash
python3 run_all.py
```

Ejecutar solo los tests:

```bash
python3 tests/test_monotonia.py
```

---

## Qué verifica cada laboratorio

### `lab_04_4_verificacion_preternaria.py`

Verifica **§4.4** del documento:

- Tabla de sesgos polares δ_i(k) sobre 3 posiciones en el tramo preternario.
- Cálculo de V_i(δ, 3), A_i(3), H_pre(Γ, 3) = 10.2.
- Contraste con trayectoria sin oscilación: H_pre^sin-osc = 9.0.
- Diferencia por oscilación: 1.2 unidades factuales.

### `lab_11_recorrido_consistencia.py`

Verifica **§11** (caso patrón) completo:

- Configuración SV(3,9) con 5 posiciones, tramo [0, 6].
- Proyección Π_3^H en cada cruce.
- 14 assertions contra valores declarados: A_Γ(6) = 28, H_pre(6) = 31,0,
  H_Ξ(6) = 35,3, H_Σc(6) = 36,3, H_Σk(6) = 38,3, H_SV(6) = 38,6
  y los correspondientes para n = 5.
- Teorema 8.2 (monotonía): H_SV(6) − H_SV(5) = 5,2 > 0.

### `lab_11_10_violacion_simulada.py`

Verifica **§11.10**:

- Reescritura retroactiva δ_3(2) = 0.2 → 0.1 sin base compatible.
- Decremento estricto: V_3(orig) = 0.4 → V_3(viol) = 0.2.
- Confirmación de violación del Teorema 4.5 y exclusión por Proposición 4.7.

### `lab_ejemplo_A_cierre_determinado.py`

Ejemplo de principio a fin con dictamen **𝔗_SV(Γ) = m_0**:

- 3 posiciones con cruces determinados |δ| ≥ θ_0, θ_1.
- Resultado: H_SV(Γ, 4) = 16.8, monotonía Δ[3, 4] = 3.7 > 0.

### `lab_ejemplo_B_residual_en_U.py`

Ejemplo de principio a fin con dictamen **𝔗_SV(Γ) = U**:

- 2 posiciones: ξ_1 con cierre determinado, ξ_2 con |δ| < θ_U y base insuficiente.
- δ_U(Γ, 5) = 0.5 contribuye al dictamen final.
- Resultado: H_SV(Γ, 5) = 15.0, monotonía Δ[3, 5] = 4.7 > 0.

### `lab_ejemplo_C_clase_emergente.py`

Ejemplo de principio a fin con dictamen **𝔗_SV(Γ) = χ_α**:

- 2 posiciones con cruces determinados.
- Activación de clase emergente en n = 5 bajo criterio G(χ_α) = 1.
- δ_χ(Γ, 5) = 0.6 aporta contribución transmutativa.
- Resultado: H_SV(Γ, 5) = 15.0, monotonía Δ[4, 5] = 2.0 > 0.

### `tests/test_monotonia.py`

Suite de 13 tests unitarios que verifican:

- Teorema 4.5 (monotonía H_pre en tramo preternario y post-cruce).
- Teorema 5.4 (monotonía H_K3; transiciones virtuales; cota por posición).
- Teorema 6.3 (monotonía H_Ξ).
- Teorema 8.2 (monotonía H_SV) sobre caso patrón y ejemplos A, B, C.
- Proposición 4.7 (decremento bajo reescritura retroactiva).
- Todos los valores numéricos declarados en §11 del documento.

---

## Principio metodológico

Todos los laboratorios operan bajo las prohibiciones constitutivas del SV:

1. No se introduce tiempo soberano ni se invoca ordenamiento temporal externo.
2. No se usa probabilidad fundante ni estadística como criterio de verdad.
3. No se emplean coordenadas externas al SV.
4. Todas las magnitudes se derivan exclusivamente de acumulaciones
   append-only y variaciones totales del sesgo polar preternario.
5. La monotonía emerge como propiedad estructural del sistema, no como
   consecuencia de principio físico externo.

---

## Enlaces al documento

- Documento principal: `../2026l-entropia-factual-sv.md` (en el mismo repositorio).
- Cuerpo Maxwell + anexo (documento base): Lloret Egea (2026k).
- Origen preternario: Lloret Egea (2026j).

---

## Licencia

**© 2026 Juan Antonio Lloret Egea** — ORCID 0000-0002-6634-3351 — ITVIA — ISSN 2695-6411 —
Licencia **CC BY-NC-ND 4.0**. Publicación protegida por **CEDRO**.
