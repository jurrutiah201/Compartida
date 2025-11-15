def seleccionar_dificultad():
    print("--- SELECCIONA LA DIFICULTAD ---")
    print("1. Facil   (1 - 10)")
    print("2. Medio   (1 - 20)")
    print("3. Dificil (1 - 50)")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        return 10
    elif opcion == "2":
        return 20
    elif opcion == "3":
        return 50
    else:
        print("Opción inválida. Se elige dificultad media (1–20).")
        return 20