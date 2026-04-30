#!/usr/bin/env python3
"""Ejecutor complementario de los laboratorios termodinámicos SV.

Este archivo delega en `runner.py` para mantener una única política material
de ejecución: fail-fast, catálogo de errores obligatorio y ausencia de pases
silenciosos.
"""
import sys
from runner import main

if __name__ == "__main__":
    sys.exit(main())
