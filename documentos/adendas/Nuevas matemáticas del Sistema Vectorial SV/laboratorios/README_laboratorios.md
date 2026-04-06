# Laboratorios del Sistema Vectorial SV
## Nuevas matemáticas del SV y Física factual como conjunto iniciador

**Autor:** Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
**Sello:** ITVIA — IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411
**Licencia:** CC BY-NC-ND 4.0 | Madrid, 2026

---

## Estructura del paquete

```
laboratorios/
├── lab_01_calculo_suceso.py          ← XIV módulos A-D + XV runner NMSV
├── lab_02_ejemplo_director.py        ← XII §7 ejemplo director (7 planos)
├── lab_03_geometrico.py              ← XXI-XXII laboratorio geométrico G1-G5
├── lab_04_recorrido_completo.py      ← XXIV §15 pipeline completo
├── lab_05_maxwell_factual.py         ← I §3 Maxwell factual sintético
├── lab_06_gravedad_factual.py        ← II §4 Gravedad factual sintética
├── lab_07_higgs_factual.py           ← III §3 Higgs factual sintético
├── runner_sv_nmsv.py                 ← Runner maestro XV (7 labs)
├── salida_calculo_suceso.json        ← Salida congelada lab 01
├── salida_ejemplo_director.json      ← Salida congelada lab 02
├── salida_geometrico.json            ← Salida congelada lab 03
├── salida_recorrido_completo.json    ← Salida congelada lab 04
├── salida_maxwell_factual.json       ← Salida congelada lab 05
├── salida_gravedad_factual.json      ← Salida congelada lab 06
├── salida_higgs_factual.json         ← Salida congelada lab 07
├── salida_runner_sv.json             ← Salida maestra del runner
└── README_laboratorios.md            ← Este fichero
```

## Requisitos

- Python 3.9 o superior
- No requiere dependencias externas (stdlib únicamente: `json`, `hashlib`, `subprocess`)

## Ejecución

**Laboratorio individual:**
```bash
python3 lab_01_calculo_suceso.py
python3 lab_02_ejemplo_director.py
python3 lab_03_geometrico.py
python3 lab_04_recorrido_completo.py
```

**Runner completo (ejecuta los 4 labs y emite veredicto):**
```bash
python3 runner_sv_nmsv.py
```

## Correspondencia con el documento

| Laboratorio | Sección del documento | Qué verifica |
|---|---|---|
| `lab_01_calculo_suceso.py` | XIV (módulos A-D), XV (NMSV) | Derivada, acumulación, sensibilidad, custodia, 5 casos canónicos, NMSV001-008 |
| `lab_02_ejemplo_director.py` | XII §7 | Los 7 planos del ejemplo director sobre SV(9,3) |
| `lab_03_geometrico.py` | XXI, XXII, XXIV §3.11-12 | Flujo, divergencia, cancelación, balance, conservación U (G1-G5) |
| `lab_04_recorrido_completo.py` | XXIV §15 | Pipeline completo: tabla resumen de 14 operadores → APTO |
| `lab_05_maxwell_factual.py` | I §3 | Maxwell factual: residuales sin tiempo soberano, sensibilidad, APTO |
| `lab_06_gravedad_factual.py` | II §4 | Gravedad: coincidencia, fork por ruido sísmico, append-only, APTO |
| `lab_07_higgs_factual.py` | III §3 | Higgs: evidencia acumulada, fork fondo, J_clausura=0, APTO |
| `runner_sv_nmsv.py` | XV | Runner maestro (7 labs), invariantes y huellas de integridad |

## Invariantes verificados (XV §4)

1. **No degradación de U**: ninguna posición U se cierra sin suceso de resolución declarado (NMSV006)
2. **Append-only**: los frames anteriores de la trayectoria son inmutables (NMSV007)
3. **Separación de planos**: los valores K₃ ≠ booleanos Python ni números reales (NMSV005)
4. **No cierre favorable ilegítimo**: APTO solo si n₀ ≥ T(n) sin infracciones (NMSV008)
5. **Frontera explícita**: ninguna célula geométrica opera sin frontera declarada (G3)

## Valores verificados del ejemplo director (XII §7)

| Plano | Resultado | Verificado |
|---|---|---|
| f(νⱼ) | [3, 2, 1, 0] | ✓ |
| 𝔇_Γ f(j) | [-1, -1, -1] | ✓ |
| 𝔄 = f(ν₃)-f(ν₀) | -3 | ✓ |
| ΔN | 3 | ✓ |
| J_SV(ν₃) | 0 | ✓ |
| Dictamen ν₃ | APTO | ✓ |

## Valores verificados del recorrido completo (XXIV §15)

| Operador | Resultado | Verificado |
|---|---|---|
| Φ(F₀₁) | 3 | ✓ |
| Div(C₁) | 1 | ✓ |
| ∫_M F dω | 6 | ✓ |
| Balance ΔF | -3 | ✓ |
| ∇F(ν₀) | (-1, -1) | ✓ |
| J_clausura | 0 | ✓ |
| Dictamen | APTO | ✓ |
