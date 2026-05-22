# Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable

![Portada de Campo y energía, génesis de la masa y definición física de la gravedad](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/imagenes/portada.png)

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)  
**Institución:** [Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ — ITVIA](https://www.itvia.online/)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** [2695-6411](https://portal.issn.org/resource/ISSN/2695-6411)  
**Licencia:** [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)  
**Fecha:** Madrid, 22/05/2026  
**Repositorio canónico:** [https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad)

## Contenido

Esta carpeta contiene la publicación **Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable**, su portada, sus laboratorios reproducibles y los manifiestos de integridad asociados. El texto principal está en [`campo-energia-masa-gravedad.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/campo-energia-masa-gravedad.md). La portada se aloja en [`imagenes/portada.png`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/imagenes/portada.png). Los laboratorios están en [`laboratorios/`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios) y comprueban los bancos visibles del apartado XIV, la separación G–Λ, la transducción de Λ con banco declarado, la matriz de absorción, los negativos de dominio y la salida global. El Anexo A forma parte material del texto principal y fija el tratamiento de Λ mediante `Λ_SV,puro`, `Λ_obs[B]` y `Λ_SV,ret[B]` como tupla auditada.

## Estructura

| Ruta | Función |
|---|---|
| [`campo-energia-masa-gravedad.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/campo-energia-masa-gravedad.md) | Texto canónico de la publicación, con conclusión, laboratorios, Anexo A y bibliografía integrada. |
| [`imagenes/portada.png`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/imagenes/portada.png) | Portada cerrada de la publicación. |
| [`laboratorios/`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios) | Laboratorios Python, bancos CSV, catálogo de errores, salida esperada y salida obtenida. |
| [`laboratorios/README.md`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/README.md) | Instrucciones de ejecución, trazabilidad y política de dictamen del paquete ejecutable. |
| [`laboratorios/datos/`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/datos) | Constantes, bancos positivos, negativos, transductivos y observacionales de Λ. |
| [`MANIFIESTO_SHA256.txt`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/MANIFIESTO_SHA256.txt) | Manifiesto de integridad SHA-256 de la carpeta principal. |
| [`laboratorios/MANIFIESTO_SHA256.txt`](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/laboratorios/MANIFIESTO_SHA256.txt) | Manifiesto SHA-256 del paquete de laboratorios. |
| [`registros/`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/campo-energia-masa-gravedad/registros) | Carpeta reservada para registros de custodia, firma, sellado temporal, hashes y preservación. |

## Verificación material

El paquete de laboratorios se ejecuta con Python 3.8 o superior, sin dependencias externas. Desde la carpeta de laboratorios:

```text
python runner.py
```

La ejecución debe producir `salida_obtenida.txt` idéntica a `salida_esperada.txt`. El runner verifica 16 laboratorios, los bancos positivos, negativos, transductivos, observacionales de Λ y de salida global. El cierre no depende de una salida favorable aislada: exige dominio declarado, unidad correcta, banco observacional cuando corresponda, residual explícito, dictamen material y ausencia de pase silencioso.

## Criterios de cierre

La publicación mantiene separados los planos físicos que evalúa: energía como eficacia estructural no nula de dominio, masa como persistencia material de energía retenida por frontera compatible, gravedad como respuesta del dominio de separación, G como coeficiente metrológico de retorno local fuente-respuesta y Λ como curvatura efectiva ciclo-distancial del dominio cosmológico observable retornado. En el régimen de Λ, `Λ_SV,puro` es magnitud estructural; `Λ_obs[B]` es valor observacional dependiente de banco; `Λ_SV,ret[B]` es tupla auditada con banco, unidad, incertidumbre, residual y dictamen. Ningún valor externo entra como magnitud constitutiva sin banco declarado y retorno controlado.

## Autoría y licencia

© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados. Este material se publica bajo licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional. La cita, consulta, preservación y lectura académica quedan permitidas en los términos de la licencia, siempre que se conserven título, autoría, ORCID, institución, fuente canónica, licencia y referencia bibliográfica completa. Queda prohibida la modificación, redistribución derivada, fragmentación engañosa, apropiación, reatribución, explotación comercial o uso incompatible con la licencia declarada.
