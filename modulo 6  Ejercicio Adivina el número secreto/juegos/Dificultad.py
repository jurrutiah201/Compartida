def seleccionar_dificultad():
    print("--- SELECCIONA LA DIFICULTAD ---")
    print("1. Facil   (1 - 10)")
    print("2. Medio   (1 - 20)")
    print("3. Dificil (1 - 50)")

   while True:
        opcion = input("Ingresa el número de opción (1, 2 o 3): ")
        
        if opcion == '1':
            return 10  # Retorna el límite superior
        elif opcion == '2':
            return 20
        elif opcion == '3':
            return 50
        else:
        print("Opción inválida. Se elige dificultad media (1–20).")
        return 20
