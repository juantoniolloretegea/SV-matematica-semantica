# Laboratorios reproducibles

**Autor / Author:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Sello editorial / Editorial imprint:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación / Publication:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia / License:** CC BY-NC-ND 4.0  
**Copyright:** © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.  
**Lugar y fecha / Place and date:** Madrid, mayo de 2026


---

## Objeto

Esta carpeta contiene veintiocho laboratorios reproducibles asociados a la publicación **Interacción, intercomposición y transmisión factual entre campos en el Sistema Vectorial SV**.

Los laboratorios verifican computacionalmente compuertas, teoremas, preservación de `U`, distancia factual fibrosa, intercomposición, célula `SV(36,6)`, transmisión factual, residual de canal y comparación subordinada con Shannon.

## Ejecución

```bash
python3 runner.py
```

Resultado esperado:

```text
28/28 laboratorios superados
```

## Organización

- `LAB-01` a `LAB-10`: núcleo de interacción e intercomposición.
- `LAB-11` a `LAB-18`: aparato de distancia factual fibrosa, célula `SV(36,6)` y casos adversariales.
- `LAB-T01` a `LAB-T10`: transmisión factual, codificación, canal, residual y frontera con Shannon.
- `CATALOGO-DE-ERRORES.md`: catálogo de treinta códigos de error estructural.
- `runner.py`: ejecutor unificado bajo régimen fail-fast.

## Estatuto

Los laboratorios verifican estructura formal y coherencia interna. No constituyen dataset empírico externo ni sustituyen al documento principal. Operan como soporte reproducible subordinado a la publicación y a la doctrina vigente del Sistema Vectorial SV.
