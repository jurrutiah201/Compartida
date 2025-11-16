from sistemas.usuarios import usuarios

MAX_INTENTOS = 3

def iniciar_sesion():
    """--Valida el PIN para iniciar sesión.--"""

    print("=== INICIO DE SESIÓN ===")
    print("Escribe 0 para salir.\n")

    intentos = 0

    while intentos < MAX_INTENTOS:
        pin = input(" Ingresa tu PIN: ")

        if pin == "0":
            return None, None  # Fin del programa

        if pin in usuarios:
            print(f"\nBienvenido/a {usuarios[pin]['nombre']}.\n")
            return pin, usuarios[pin]

        intentos += 1
        print(f"PIN incorrecto. Intento {intentos}/{MAX_INTENTOS}\n")

    print("Tarjeta bloqueada. Demasiados intentos.")
    return None, None