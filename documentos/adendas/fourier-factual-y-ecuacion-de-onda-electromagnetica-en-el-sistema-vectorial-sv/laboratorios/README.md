# Laboratorios — Fourier factual y ecuación de onda electromagnética en el Sistema Vectorial SV

**Carpeta:** `laboratorios/`
**Base canónica en GitHub:**
`https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv/laboratorios`

---

## Suite mínima reproducible

| ID | Título | Fichero MD | JSON congelado |
|---|---|---|---|
| LAB-EM-01 | Modos cíclicos factuales del campo electromagnético | `laboratorios/LAB-EM-01.md` | `laboratorios/json_congelados/lab-em-01.json` |
| LAB-EM-02 | Desarrollo cíclico factual y transformada modal electromagnética | `laboratorios/LAB-EM-02.md` | `laboratorios/json_congelados/lab-em-02.json` |
| LAB-EM-03 | Balance factual modal | `laboratorios/LAB-EM-03.md` | `laboratorios/json_congelados/lab-em-03.json` |
| LAB-EM-04 | Residual de borde factual | `laboratorios/LAB-EM-04.md` | `laboratorios/json_congelados/lab-em-04.json` |
| LAB-EM-05 | Ecuación factual de onda electromagnética | `laboratorios/LAB-EM-05.md` | `laboratorios/json_congelados/lab-em-05.json` |

---

## Runners

| Fichero | Función |
|---|---|
| `laboratorios/runners/runner_maestro_emf.py` | Ejecuta la suite completa LAB-EM-01 a LAB-EM-05 en régimen fail-fast |
| `laboratorios/runners/runner_rapido_emf.py` | Verificación rápida de propagación (2 pasos) |
| `laboratorios/runners/runner_ed_em_01.py` | Ejecución completa del caso director ED-EM-01 |
| `laboratorios/runners/sv_emf_core.py` | Librería central: transformada modal, propagación, freeze_json |

---

## JSON congelados

| Fichero | Contenido |
|---|---|
| `laboratorios/json_congelados/lab-em-01.json` | Salida de LAB-EM-01 (autosellada con MD5) |
| `laboratorios/json_congelados/lab-em-02.json` | Salida de LAB-EM-02 (autosellada con MD5) |
| `laboratorios/json_congelados/lab-em-03.json` | Salida de LAB-EM-03 (autosellada con MD5) |
| `laboratorios/json_congelados/lab-em-04.json` | Salida de LAB-EM-04 (autosellada con MD5) |
| `laboratorios/json_congelados/lab-em-05.json` | Salida de LAB-EM-05 (autosellada con MD5) |
| `laboratorios/json_congelados/runner_rapido_emf.json` | Salida de `runner_rapido_emf.py` (autosellada) |
| `laboratorios/json_congelados/runner_ed_em_01.json` | Salida de `runner_ed_em_01.py` (autosellada) |
| `laboratorios/json_congelados/reporte_laboratorios_emf.json` | Reporte global de la suite (autosellado) |

---

## Pseudocódigo doctrinal

| Fichero | Contenido |
|---|---|
| `laboratorios/pseudocodigo/gobernar_ed_em_01.sv.txt` | Pseudocódigo del procedimiento GOBERNAR_ED_EM_01 |
| `laboratorios/pseudocodigo/runner_maestro_emf.sv.txt` | Pseudocódigo del runner maestro |

---

## Catálogo de errores

`laboratorios/catalogo/CATALOGO_ERRORES_EJECUCION.md`

---

## Caso director

**ED-EM-01**: pulso electromagnético factual localizado sobre `SV(3,9)`, en vacío factual,
propagándose sobre ciclo y trayectoria poligonal.

Parámetros canónicos de ejecución:

| Parámetro | Valor | Unidad |
|---|---|---|
| Posición inicial del pulso (1-indexada) | `2` | — |
| Amplitud escalarizada inicial | `1.0` | UFM·UFE·UFC⁻¹·UE_MFC⁻³ |
| Δξ | `0.5` | UE_MFC |
| Δℓ | `1.0` | UFE |
| c_SV | `1.0` | UFE·UE_MFC⁻¹ |

---

## Ejecución

```bash
cd laboratorios/runners
python3 runner_maestro_emf.py
```

Salida esperada: ruta a `laboratorios/json_congelados/reporte_laboratorios_emf.json`
con `"dictamen_final": "APTO"`.
