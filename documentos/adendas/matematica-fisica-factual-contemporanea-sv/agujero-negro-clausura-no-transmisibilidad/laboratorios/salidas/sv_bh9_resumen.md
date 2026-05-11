# Resumen de ejecución SV-BH9

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Derechos:** © 2026. Todos los derechos reservados.  
**Licencia:** CC BY-NC-ND 4.0  

Estado global: **APTO**

Casos totales: 54
Casos aptos: 54
Casos fallidos: 0
Errores adversariales detectados: 15

| Bloque | Caso | Estado | Esperado | Obtenido | Error |
|---|---|---|---|---|---|
| formas_equivalentes_BH | F-BH-OK-01 | PASS | BH_CERRADO | BH_CERRADO |  |
| formas_equivalentes_BH | F-BH-LUZ-01 | PASS | NO_APTO | NO_APTO | BH-LUZ-002 |
| formas_equivalentes_BH | F-BH-TN-01 | PASS | NO_APTO | NO_APTO | BH-UPOST-001 |
| formas_equivalentes_BH | F-BH-ABS-01 | PASS | NO_APTO | NO_APTO | BH-ABS-001 |
| DΣ_celular | C9-01 | PASS | NO_APTO | NO_APTO |  |
| DΣ_celular | C9-02 | PASS | APTO | APTO |  |
| DΣ_celular | C9-03 | PASS | U | U |  |
| DΣ_celular | C9-04 | PASS | NO_APTO | NO_APTO |  |
| DΣ_celular | C36-01 | PASS | NO_APTO | NO_APTO |  |
| DΣ_celular | C36-02 | PASS | U | U |  |
| DΣ_celular | C36-03 | PASS | APTO | APTO |  |
| DΣ_celular | C36-04 | PASS | NO_APTO | NO_APTO |  |
| Schwarzschild | SCH-01 | PASS | False | False |  |
| Schwarzschild | SCH-02 | PASS | False | False |  |
| Schwarzschild | SCH-03 | PASS | False | False |  |
| Schwarzschild | SCH-04 | PASS | True | True |  |
| Schwarzschild | SCH-05 | PASS | True | True |  |
| Schwarzschild | SCH-06 | PASS | True | True |  |
| Schwarzschild | SCH-07 | PASS | True | True |  |
| termodinamica_BH | M1 | PASS | C_TH=0;C_H=0 | C_TH=0;C_H=0 |  |
| termodinamica_BH | M10 | PASS | C_TH=0;C_H=0 | C_TH=0;C_H=0 |  |
| termodinamica_BH | SGRA | PASS | C_TH=0;C_H=0 | C_TH=0;C_H=0 |  |
| termodinamica_BH | M87 | PASS | C_TH=0;C_H=0 | C_TH=0;C_H=0 |  |
| Kerr | KERR-01 | PASS | True | True |  |
| Kerr | KERR-02 | PASS | True | True |  |
| Kerr | KERR-03 | PASS | True | True |  |
| Kerr | KERR-04 | PASS | True | True |  |
| Kerr | KERR-05 | PASS | True | True |  |
| Kerr | KERR-06 | PASS | False | False | BH-KERR-001 |
| singularidad_geometrica | K-01 | PASS | no_fundamento | LIMITE_DE_PROYECCION |  |
| singularidad_geometrica | K-02 | PASS | no_fundamento | LIMITE_DE_PROYECCION |  |
| singularidad_geometrica | K-03 | PASS | no_fundamento | LIMITE_DE_PROYECCION |  |
| singularidad_geometrica | K-04 | PASS | no_fundamento | LIMITE_DE_PROYECCION |  |
| singularidad_geometrica | K-05 | PASS | BH-SING-001 | NO_EVALUABLE_COMO_FUNDAMENTO | BH-SING-001 |
| absorcion_modelos | ABS-01 | PASS | ABSORBIDO | ABSORBIDO |  |
| absorcion_modelos | ABS-02 | PASS | ABSORBIDO | ABSORBIDO |  |
| absorcion_modelos | ABS-03 | PASS | RECHAZADO | RECHAZADO | BH-SING-001 |
| absorcion_modelos | ABS-04 | PASS | ABSORBIDO | ABSORBIDO |  |
| absorcion_modelos | ABS-05 | PASS | ABSORBIDO_PARCIALMENTE | ABSORBIDO_PARCIALMENTE |  |
| absorcion_modelos | ABS-06 | PASS | ABSORBIDO_PARCIALMENTE | ABSORBIDO_PARCIALMENTE |  |
| absorcion_modelos | ABS-07 | PASS | ABSORBIDO_PARCIALMENTE | ABSORBIDO_PARCIALMENTE |  |
| absorcion_modelos | ABS-08 | PASS | ABSORBIDO_PARCIALMENTE | ABSORBIDO_PARCIALMENTE |  |
| absorcion_modelos | ABS-09 | PASS | RECHAZADO | RECHAZADO | BH-LUZ-002 |
| postfrontera_MN2 | PF-01 | PASS | APTO | APTO |  |
| postfrontera_MN2 | PF-02 | PASS | NO_APTO | NO_APTO | BH-UPOST-001 |
| postfrontera_MN2 | PF-03 | PASS | NO_APTO | NO_APTO | BH-TN-002 |
| postfrontera_MN2 | PF-04 | PASS | NO_APTO | NO_APTO | BH-TN-002 |
| postfrontera_MN2 | PF-05 | PASS | NO_APTO | NO_APTO | BH-TN-002 |
| postfrontera_MN2 | PF-MN2-NE-U | PASS | M_N2-SV≠U | M_N2-SV≠U |  |
| falsacion_luminosa_externa | EXT-01 | PASS | BH_FISICO_EQ_BH_SV | BH_FISICO_EQ_BH_SV |  |
| falsacion_luminosa_externa | EXT-02 | PASS | NO_APTO | NO_APTO | BH-LUZ-002 |
| falsacion_luminosa_externa | EXT-03 | PASS | NO_APTO | NO_APTO | BH-TE-001 |
| falsacion_luminosa_externa | EXT-04 | PASS | NO_APTO | NO_APTO | BH-INT-001 |
| falsacion_luminosa_externa | EXT-05 | PASS | NO_APTO | NO_APTO | BH-TN-002 |
