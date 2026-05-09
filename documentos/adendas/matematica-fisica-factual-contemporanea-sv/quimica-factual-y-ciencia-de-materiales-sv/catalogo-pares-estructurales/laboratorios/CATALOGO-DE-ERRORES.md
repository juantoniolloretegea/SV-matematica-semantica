# Catálogo de errores — Laboratorio CPS-SV

**Publicación:** Catálogo de Pares Estructurales SV (CPS-SV)  
© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | CC BY-NC-ND 4.0

---

## Grupo I — Errores de carga

| Código | Condición |
|---|---|
| `CPS-LOAD-CSV` | Archivo de Tabla Global no encontrado o no legible |
| `CPS-LOAD-COLS` | Columnas requeridas ausentes (k, nombre, EN_SV, IP_SV, r_SV, M_SV) |
| `CPS-LOAD-COUNT` | Número de elementos ≠ 443 |
| `CPS-LOAD-FLOAT-{k}-{col}` | Valor no convertible a float en elemento k, columna col |
| `CPS-LOAD-RANGE-EN-{k}` | EN_SV(k) fuera de [0,0 ; 3,0] |
| `CPS-LOAD-RANGE-IP-{k}` | IP_SV(k) fuera de [300 ; 5000] kJ/mol |
| `CPS-LOAD-RANGE-R-{k}` | r_SV(k) fuera de [100 ; 400] pm |
| `CPS-LOAD-RANGE-M-{k}` | M_SV(k) fuera de [0,0 ; 100,0] % |

## Grupo II — Errores de salida

| Código | Condición |
|---|---|
| `CPS-OUT-WRITE` | Error de escritura del CSV de salida |
| `CPS-OUT-COUNT` | CSV de salida no contiene exactamente 97.903 filas |
| `CPS-OUT-COLS` | Cabecera del CSV de salida incorrecta |
| `CPS-OUT-DICT-{n}` | Dictamen inválido en fila n |
| `CPS-OUT-READ` | Error de relectura del CSV de salida |

## Grupo III — Errores de invariante (§6.4)

| Código | Proposición | Condición |
|---|---|---|
| `CPS-INV-NOBLE` | 6.1 | Par noble×noble con dictamen ≠ NO-APTO |
| `CPS-INV-MARGINAL` | 6.2 | Recuento de pares marginales B.2 ≠ 9.858 |
| `CPS-INV-FECROMO` | F.1 | Par Fe-Cr (k=24,26) no recibe APTO-M |
| `CPS-INV-CUZN` | F.1 | Par Cu-Zn (k=29,30) no recibe APTO-M |
| `CPS-INV-KCL` | F.1 | Par KCl (k=17,19) no recibe APTO-I |
| `CPS-INV-ARKR` | F.1 | Par Ar-Kr (k=18,36) no recibe NO-APTO |
