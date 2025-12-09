# modelos/cliente.py

class Cliente:
    def __init__(self, nombre: str, apellido: str, cedula: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"
