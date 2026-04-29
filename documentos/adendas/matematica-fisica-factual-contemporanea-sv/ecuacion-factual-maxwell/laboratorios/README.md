# Laboratorios canónicos de Maxwell-SV

© 2026. Todos los derechos reservados. Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)  
IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411  
Licencia CC BY-NC-ND 4.0 | Madrid, 20/04/2026

## Publicación principal

**Absolute structural reduction of Maxwell in the Sistema Vectorial SV and single equation of factual electromagnetic physics**

DOI Commons/KCWorks de la publicación principal:  
https://doi.org/10.17613/kep1t-57539

Colección canónica:  
https://doi.org/10.17613/r4dwa-d9b30

Fuente material canónica en GitHub:  
https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/ecuacion-factual-maxwell

## Objeto del paquete

Este paquete conserva los laboratorios reproducibles asociados a la reducción estructural absoluta de Maxwell en el Sistema Vectorial SV. Los laboratorios implementan, en forma ejecutable, el recorrido visible de consistencia reforzado del bloque electromagnético factual fijado en el documento principal.

El caso positivo de control reproduce **21 bancos de verificación**: cuatro ecuaciones factuales, balance, conservación de carga, cuatro contornos interfaciales, criterio absoluto de frontera, activación de frontera, reconfiguración, tres relaciones constitutivas, dos formas maestras, ecuación única, cosido dimensional soberano e identidad de onda factual.

El banco adversarial contiene **15 casos negativos**. Estos casos no son ornamentales: su finalidad es asegurar falsación local, impedir pases silenciosos y exigir la detección del código de error prescrito.

## Estructura

| Elemento | Descripción |
|---|---|
| `datos/caso_control_svtresnueve.json` | Caso positivo canónico SV(3,9). |
| `datos/casos_negativos.json` | Banco de 15 ataques negativos. |
| `modulo/verificador_maxwell_sv.py` | Núcleo verificador de 21 bancos positivos y 15 negativos. |
| `run_all.py` | Ejecutor reproducible complementario. |
| `runner.py` | Runner maestro equivalente para ejecución directa. |
| `resultados/` | Resultados regenerados del runner maestro. |
| `catalogo_errores.json` | Catálogo explícito de códigos `MAXWELL`. |
| `MANIFEST.json` | Manifiesto material del paquete. |
| `SHA256SUMS.txt` | Huellas SHA-256 de todos los archivos. |
| `EXECUTION_REPORT.txt` | Informe breve de ejecución. |
| `EXECUTION_LOG_FULL.txt` | Registro completo de ejecución. |
| `CITATION.cff` | Metadatos de citación. |
| `ZENODO_UPLOAD_FIELDS.md` | Campos recomendados para depósito Zenodo. |

## Cómo reproducir

Desde esta carpeta:

```bash
python run_all.py
```

o bien:

```bash
python runner.py
```

El runner termina con `exit 0` sólo si:

1. los 21 bancos positivos pasan;
2. los 15 casos negativos son detectados;
3. cada caso negativo produce el código de error esperado;
4. no se produce ningún pase silencioso.

## Resultado verificado

Estado del paquete preparado:

- Bancos positivos superados: 21/21.
- Casos negativos detectados correctamente: 15/15.
- Sintaxis Python verificada.
- Paquete sin `__pycache__` ni bytecode.
- Metadatos de preservación añadidos.

## Depósito reproducible preservado

Los laboratorios de esta carpeta están preservados en Zenodo como suplemento computacional reproducible de la publicación principal.

DOI de versión:  
https://doi.org/10.5281/zenodo.19895446

DOI conceptual de todas las versiones:  
https://doi.org/10.5281/zenodo.19895445

Registro Zenodo:  
https://zenodo.org/records/19895446

## Licencia

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).
