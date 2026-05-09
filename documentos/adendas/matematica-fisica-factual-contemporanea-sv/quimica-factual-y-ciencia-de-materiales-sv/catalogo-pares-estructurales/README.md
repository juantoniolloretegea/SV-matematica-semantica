# Catálogo de Pares Estructurales SV (CPS-SV)

## Enlace, aleación y compatibilidad posicional desde los 118 elementos base hasta los 443 candidatos del dominio extendido

![Portada CPS-SV](imagenes/Portada.png)

**Autor:** Juan Antonio Lloret Egea | ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)  
**Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™ | **ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0 | **Fecha:** Madrid, 09/05/2026  
**DOI:** pendiente de asignación (HCOMMONS)

---

## Descripción

El CPS-SV establece los cinco criterios de admisibilidad de enlace estructural (B.1–B.5), el Teorema de predominancia de U (Teorema 1.6.1) y la función de dictamen D(A,B) sobre el dominio completo de 97.903 pares no ordenados del catálogo SV-443.

**Resultado canónico del laboratorio:**

| Dictamen | Pares | % |
|---|---|---|
| APTO-M (metálico estructural) | 9.515 | 9,7% |
| APTO-C (covalente estructural) | 37.580 | 38,4% |
| APTO-I (iónico estructural) | 5.075 | 5,2% |
| NO-APTO | 45.733 | 46,7% |
| **APTO total** | **52.170** | **53,3%** |

---

## Contenido del repositorio

```
catalogo-pares-estructurales/
├── catalogo-pares-estructurales.md    ← Publicación completa
├── README.md                          ← Este archivo
├── imagenes/
│   ├── Portada.png                    ← Portada de la publicación
│   ├── tabla_cero_sv.svg              ← Tabla Cero SV (vectorial)
│   ├── tabla_cero_sv.png              ← Tabla Cero SV (PNG 2×)
│   ├── tabla_global_sv.svg            ← Tabla Global SV (vectorial)
│   ├── tabla_global_sv.png            ← Tabla Global SV (PNG 2×)
│   └── registros-criptograficos/     ← Sellos OTS y firmas
├── PDF/                               ← PDF firmado (pendiente de depósito)
└── laboratorios/
    ├── runner.py                      ← Punto de entrada del laboratorio
    ├── src/
    │   └── sv_cps.py                  ← Módulo central CPS-SV
    ├── datos/
    │   ├── tabla_global_sv443.csv     ← Tabla Global (443 elementos)
    │   └── catalogo_pares_sv443.csv  ← CPS-SV completo (97.903 pares)
    └── resultados/
        └── verificacion_cps_sv.json  ← Verificación canónica
```

## Tablas estructurales SV

| Tabla | SVG | OTROS |
|---|---|---|
| Tabla Cero SV (118 elementos base) | [tabla_cero_sv.svg](imagenes/tabla_cero_sv.svg) | [tabla_cero_sv.png](imagenes/tabla_cero_sv.png) |
| Tabla Global SV (443 elementos) | [tabla_global_sv.svg](imagenes/tabla_global_sv.svg) | [tabla_global_sv_vectorial.pdf](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/imagenes/tabla_global_sv_vectorial.pdf) |

## Laboratorio reproducible

**Ejecución:**
```bash
cd laboratorios
PYTHONPATH=src python3 runner.py
```

**Depósito Zenodo:** Pendiente

## Publicación base

**Catálogo SV-443:** Pendiente

---

## Identificación DOI

- DOI de la publicación: **pendiente de asignación (HCOMMONS)**
- DOI del laboratorio canónico: Pendiente

## Registro criptográfico de referencia

| Fichero | Función | SHA-256 |
|---|---|---|
Pendiente

© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0 | Madrid, 09/05/2026
