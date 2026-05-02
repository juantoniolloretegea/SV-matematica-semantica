# Catálogo de errores y diagnóstico de los laboratorios

**© 2026. Todos los derechos reservados.** | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0

---

Este catálogo recoge los errores numéricos esperados, las tolerancias operativas y los diagnósticos posibles bajo cada laboratorio del documento *De Bell a Tsirelson sin formalismo de Hilbert*. La función operativa del catálogo es prevenir pases silenciosos: cualquier resultado fuera de la tolerancia esperada debe activar diagnóstico explícito.

## Códigos de error y tolerancias operativas

| Código | Descripción | Tolerancia operativa | Causa posible |
|:---:|:---|:---:|:---|
| E-01 | Saturación |S| ≠ 2√2 | \|S − 2√2\| ≥ 1e-14 | Aritmética IEEE 754 alterada o cálculo erróneo |
| E-02 | \|R₀(Q)\| sobre SV(3, 9) ≠ 260 bajo la codificación del SV (0↦0, 1↦+1) | exacto | Definición de dictamen o codificación alterada |
| E-03 | T mod 2 ≠ 0 sobre R₀ | exacto | Lema 7.4.1 violado: revisar factorización |
| E-04 | \|X(v)\| > 2 sobre v ∈ R₀ | exacto | κ aplicado mal o factorización rota |
| E-05 | Monotonía no estricta sobre [χ_min, 1] | exacto | Postulado 11.1.1 alterado |
| E-06 | C_SV(δ) ≠ E_QM(α, β) sobre cuádruple | \|diff\| ≥ 1e-14 | Convención de signo o fórmula equivocada |
| E-07 | Candidato canónico falla axioma | exacto | Implementación incorrecta de algún axioma |
| E-08 | Candidato alternativo cumple A1–A9 | exacto | Test de axioma defectuoso |
| E-09 | k=2,3,... admitido como fiel | exacto | Lema 9.4.1 violado: revisar test de kernel |

## Tabla de diagnóstico por laboratorio

### LAB-01 — Saturación factual sobre familia de células

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| \|S − 2√2\| ≥ 1e-14 sobre alguna célula | Error E-01 | Verificar entorno IEEE 754 |
| Saturación distinta sobre b=3 y b=11 | E-01 con dependencia espuria de b | Revisar implementación de C_SV(δ) |

### LAB-02 — Factorización separable sobre R₀

El cardinal |R₀(Q)| sobre la célula SV(3, 9) bajo la codificación del Sistema Vectorial SV (0 ↦ 0, 1 ↦ +1, U ↦ −1) es 260. Este cardinal no debe confundirse con las 320 configuraciones no degeneradas bajo la codificación binaria pura {−1, +1} del régimen separable estándar usada para computar S_sep(b) en el Postulado 11.1.1 (apartado 13.9 del documento).

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| \|R₀(Q)\| ≠ 260 bajo codificación del SV | Error E-02 | Verificar definición de dictamen y codificación |
| T mod 2 = 1 sobre alguna v ∈ R₀ | Error E-03 | Revisar Lema 7.4.1 |
| \|X(v)\| > 2 sobre alguna v ∈ R₀ | Error E-04 | Revisar aplicación κ y signos |

### LAB-03 — Monotonía estricta sobre barrido fino

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| Violaciones de monotonía | Error E-05 | Verificar Postulado 11.1.1 |
| Cruce S=2 desplazado | E-05 con error en χ★(b) | Verificar fórmula del Corolario 11.3.2 |

### LAB-04 — Equivalencia con correlador cuántico

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| \|C_SV(δ) − E_QM(α,β)\| ≥ 1e-14 | Error E-06 | Revisar convención de signo |

### LAB-05 — Unicidad del correlador angular factual

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| Candidato canónico falla un axioma | Error E-07 | Revisar implementación del axioma |
| Candidato alternativo no falla ninguno | Error E-08 | Revisar test del axioma A9 |

### LAB-06 — Fidelidad A9

| Síntoma | Diagnóstico | Acción |
|:---|:---|:---|
| k=2 o k=3 admitido como fiel | Error E-09 | Revisar test de kernel del Lema 9.4.1 |

## Política de pases silenciosos

Cada laboratorio devuelve código de salida 0 si todas las verificaciones se cumplen dentro de la tolerancia operativa, y código de salida 1 si alguna falla. El runner unificado (`runner.py`) ejecuta los seis laboratorios secuencialmente y reporta el conjunto de fallos. Bajo política de no pases silenciosos, todo fallo numérico debe activar diagnóstico explícito mediante el catálogo anterior.

## Reproducibilidad

Los seis laboratorios usan únicamente bibliotecas estándar de Python (`numpy`). La semilla aleatoria de LAB-04 está fijada (`np.random.seed(42)`) para garantizar reproducibilidad cruzada. Los resultados numéricos son deterministas a precisión de máquina IEEE 754 sobre cualquier plataforma compatible.

---
