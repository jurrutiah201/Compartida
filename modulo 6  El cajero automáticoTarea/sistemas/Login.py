from sistemas.usuarios import usuarios

MAX_INTENTOS = 3


def iniciar_sesion():
    """
    Solicita el PIN y devuelve (pin, datos_usuario) si es correcto.
    Si el usuario decide salir o se bloquea la tarjeta, devuelve (None, None).
    """
    print("=== INICIO DE SESIÓN ===")
    print("Escribe 0 para salir.\n")

    intentos = 0

    while intentos < MAX_INTENTOS:
        pin = input("Ingresa tu PIN: ").strip()

        if pin == "0":
            # El usuario decide salir antes de iniciar sesión
            return None, None

        if pin in usuarios:
            nombre = usuarios[pin]["nombre"]
            print(f"\n✅ Bienvenido/a {nombre}.\n")
            return pin, usuarios[pin]

        intentos += 1
        restantes = MAX_INTENTOS - intentos

        if restantes > 0:
            print(f"❌ PIN incorrecto. Te quedan {restantes} intento(s).\n")
        else:
            print("🚫 Tarjeta bloqueada. Demasiados intentos.\n")

    return None, None
