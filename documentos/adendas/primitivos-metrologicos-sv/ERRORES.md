# ERRORES.md — Registro de errores detectados y corregidos

**Pack:** `primitivos-metrologicos-sv`  
**Auditoría:** adversarial rigurosa pieza a pieza  
**Autor:** Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351  
**ITVIA — IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Madrid, 2026**

---

## Clasificación de gravedad

| Nivel | Descripción |
|---|---|
| **GRAVE** | Compromete la ejecución correcta o la validez del resultado |
| **MEDIO** | Compromete la robustez o la trazabilidad, sin afectar el resultado numérico |
| **DOCTRINAL** | Inconsistencia conceptual que requiere aclaración formal |

---

## E-01 — Sin gestión de errores en todos los laboratorios

**Gravedad:** GRAVE  
**Archivos afectados:** `lab_01` a `lab_07` (todos)  
**Descripción:** Ningún laboratorio incluía `try/except`, `sys.exit()` ni `import sys`. Un runner no-benevolente que examine el código de salida del proceso no recibe señal explícita de éxito o fallo. Ante cualquier excepción en tiempo de ejecución (nombre de variable incorrecto, desbordamiento numérico, error de entorno), Python imprime un traceback crudo a `stderr` y el proceso termina con `exit=1` por comportamiento implícito del intérprete, no por control explícito del laboratorio.  
**Consecuencia:** La diferencia entre un fallo de verificación matemática y un fallo de entorno es indistinguible desde stderr. El runner ve el mismo `exit=1` y el mismo flujo de error en ambos casos.  
**Corrección aplicada:** Se añade a todos los laboratorios el patrón:

```python
import sys

def verificar(condicion, mensaje_error):
    if not condicion:
        print(f"[FALLO DE VERIFICACION] {mensaje_error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as e:
        print(f"[ERROR NO CONTROLADO] {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
```

**Estado:** RESUELTO en V2.

---

## E-02 — `assert` sin captura en lab_01 (vulnerable a `python3 -O`)

**Gravedad:** GRAVE  
**Archivo afectado:** `lab_01_tiempo_ue_mfc.py` (versión V1)  
**Descripción:** El laboratorio usaba sentencias `assert` nativas de Python para verificar que `9 × N_SAR_POR_UE_MFC == DELTA_NU_CS` y que la división es exacta. El flag `-O` (`--optimize`) del intérprete CPython desactiva silenciosamente todos los `assert` nativos. Un runner que invoque `python3 -O lab_01_tiempo_ue_mfc.py` obtiene `exit=0` y ningún error aunque las constantes sean incorrectas.  
**Consecuencia:** La verificación nuclear del laboratorio (exactitud de la división 9 192 631 770 / 9) puede saltarse sin ninguna señal de aviso.  
**Corrección aplicada:** Todos los `assert` sustituidos por llamadas a la función `verificar(condicion, mensaje)` que no depende del flag `-O`.  
**Estado:** RESUELTO en V2.

---

## E-03 — Sin verificaciones numéricas en labs 02–07 (versión V1)

**Gravedad:** GRAVE  
**Archivos afectados:** `lab_02` a `lab_07` (versión V1)  
**Descripción:** Los laboratorios 02 a 07 se limitaban a calcular e imprimir resultados sin comprobar en ningún momento que los valores obtenidos estuvieran dentro de los márgenes esperados. Un error silencioso en una constante (p.ej. `C_LUZ = 29_792_458` con un dígito omitido) producía salida numericamente incorrecta con `exit=0`. El runner no-benevolente no tenía forma de detectarlo.  
**Corrección aplicada:** Se añaden llamadas a `verificar()` en puntos críticos de cada laboratorio: signos positivos de todas las constantes, magnitud aproximada de los resultados clave, consistencias cruzadas (p.ej. `E = h*nu == m*c^2`).  
**Estado:** RESUELTO en V2.

---

## E-04 — Error matemático en lab_03: frecuencia dividida por 9 al calcular E = h·ν

**Gravedad:** GRAVE  
**Archivo afectado:** `lab_03_masa_ufm.py` (versión V1)  
**Descripción:** El laboratorio calculaba la energía del fotón del cesio como:

```python
freq_ue = DELTA_NU_CS / N_CELDA     # 1 021 403 530 (en UE_MFC^-1)
E_foton = H_PLANCK * freq_ue        # INCORRECTO
```

La constante de Planck `h` tiene unidades `J·s = kg·m²·s⁻¹`; el segundo (`s`) es la unidad de tiempo del SI. La frecuencia `ν` debe expresarse en `Hz = s⁻¹` para que las unidades se cancelen: `[J·s] × [s⁻¹] = [J]`. Al dividir `DELTA_NU_CS` por `N_CELDA = 9`, el código estaba usando la frecuencia en `UE_MFC⁻¹` (unidades SV estructurales, no SI), lo que introduce un factor de error de 1/9.

**Valores afectados:**

| Magnitud | V1 (incorrecto) | V2 (correcto) | Error relativo |
|---|---|---|---|
| E fotón Cs | 6.768×10⁻²⁵ J | 6.091×10⁻²⁴ J | factor 1/9 |
| m fotón Cs | 7.530×10⁻⁴² UFM | 6.777×10⁻⁴¹ UFM | factor 1/9 |

**Corrección aplicada:**

```python
# CORRECTO: nu en Hz (s^-1), que cancela con la s en h [J*s]
E_foton = H_PLANCK * DELTA_NU_CS    # h [J*s] * nu [s^-1] = E [J]
M_foton = E_foton / c2
```

**Nota doctrinal añadida:** Para fórmulas físicas que involucran `h`, `k_B`, u otras constantes SI cuya unidad de tiempo es el segundo, se debe usar la frecuencia en `Hz` (unidades SI), no en `UE_MFC⁻¹`. La conversión `9 UE_MFC = 1 s` aplica al recuento estructural del SV, no a los cálculos energéticos donde `h` es el operador de escala.  
**Estado:** RESUELTO en V2. La verificación detecta el fallo correctamente: con V1 el laboratorio termina con `exit=1` y el mensaje `[FALLO DE VERIFICACION] m_Cs incorrecto`.

---

## E-05 — Ausencia de este archivo (`ERRORES.md`)

**Gravedad:** GRAVE  
**Descripción:** El pack no incluía `ERRORES.md`. El encargo especifica explícitamente que este registro debe estar presente en la carpeta del laboratorio.  
**Estado:** RESUELTO en V2 con el presente archivo.

---

## E-06 — Documento principal sin referencia a `ERRORES.md`

**Gravedad:** MEDIO  
**Archivo afectado:** `primitivos-metrologicos-sv.md` (versión V1)  
**Descripción:** El documento principal no referenciaba el registro de errores, rompiendo la cadena de trazabilidad del pack.  
**Corrección aplicada:** Se añade sección «Registro de errores» al final del documento principal con enlace vivo a este archivo.  
**Estado:** RESUELTO en V2.

---

## Nota sobre ImportError antes del bloque `try`

**Gravedad:** INFORMATIVA (no corregible sin dependencias externas)  
**Descripción:** Si un laboratorio usa `import modulo_externo` y ese módulo no está disponible en el entorno, el `ImportError` se lanza antes de que el bloque `try/except` del `__main__` pueda capturarlo. En ese caso, Python imprime un traceback crudo a `stderr` y termina con `exit=1`. Este comportamiento es inherente al ciclo de importación de Python y no puede evitarse con el patrón `try/main/except`.

Los laboratorios del pack solo usan módulos de la biblioteca estándar (`sys`, `math`, `fractions`) disponibles en cualquier instalación Python ≥ 3.8. El riesgo de `ImportError` es por tanto nulo bajo condiciones normales.

---

## Resumen de correcciones V1 → V2

| Error | Archivo(s) | Corrección | Estado |
|---|---|---|---|
| E-01: sin try/except/sys.exit | labs 01–07 | Patrón completo añadido | ✅ V2 |
| E-02: assert vulnerable a -O | lab_01 | Reemplazado por `verificar()` | ✅ V2 |
| E-03: sin verificaciones numéricas | labs 02–07 | Verificaciones añadidas en puntos críticos | ✅ V2 |
| E-04: frecuencia /9 en E=hν | lab_03 | `E = H * DELTA_NU_CS` (no /9) | ✅ V2 |
| E-05: ERRORES.md ausente | pack completo | Este archivo | ✅ V2 |
| E-06: .md sin ref. a ERRORES.md | primitivos-metrologicos-sv.md | Sección añadida | ✅ V2 |
