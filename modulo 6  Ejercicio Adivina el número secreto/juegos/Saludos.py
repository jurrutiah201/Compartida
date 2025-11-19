def bienvenida():
    print("======================================")
    print("  ¡Bienvenido al juego del número secreto!")
    print("======================================\n")

def despedida():
    print("\nGracias por jugar. ¡Hasta la próxima! 👋")

def pregunta_continuar() -> bool:
    """
    Pregunta al usuario si quiere jugar otra vez.
    Devuelve True si sí, False si no.
    """
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Respuesta no válida. Escribe 's' o 'n'.")
