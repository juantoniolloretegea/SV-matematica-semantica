"""Errores tipados del paquete FFSV."""

class FFSVError(ValueError):
    """Excepción tipada con código estructural FFSV."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")
