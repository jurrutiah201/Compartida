from juegos.utilidad import mostrar_mayor, mostrar_menor, mensaje_perder

def controlar_intentos(numero_secreto: int, intentos_maximos: int = 5) -> bool:
    """
    Controla los intentos del jugador.
    Devuelve True si adivina el número, False si pierde.
    """
    for intento in range(1, intentos_maximos + 1):
        try:
            intento_usuario = int(input(f"Intento {intento}/{intentos_maximos}. Ingresa un número: "))
        except ValueError:
            print("Por favor ingresa un número válido.\n")
            continue

        if intento_usuario == numero_secreto:
            print(f"\n🎉 ¡Correcto! Adivinaste el número {numero_secreto} 🎉\n")
            return True
        elif intento_usuario < numero_secreto:
            mostrar_mayor()
        else:
            mostrar_menor()

    # Si sale del bucle, no adivinó
    mensaje_perder(numero_secreto)
    return False