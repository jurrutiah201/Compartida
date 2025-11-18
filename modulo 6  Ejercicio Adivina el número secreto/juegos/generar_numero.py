import random

def generar_numero(limite_superior: int) -> int:
    """
    Genera un número aleatorio entre 1 y limite_superior (incluido).
    """
    return random.randint(1, limite_superior)
