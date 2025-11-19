from sistemas.Login import iniciar_sesion


def mostrar_menu(nombre):
    print(f"\n--- MENÚ DEL CAJERO ({nombre}) ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")


def pedir_opcion():
    while True:
        opcion = input("Selecciona una opción: ").strip()
        if opcion in ("1", "2", "3", "4", "5"):
            return opcion
        print("❌ Opción inválida. Elige 1, 2, 3, 4 o 5.")


def pedir_monto(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            monto = float(entrada)
            if monto <= 0:
                print("❌ El monto debe ser mayor que 0.")
            else:
                return monto
        except ValueError:
            print("❌ Ingresa un número válido (ejemplo: 1500 o 1500.50).")


def mostrar_historial(usuario_data):
    print("\n📜 HISTORIAL DE MOVIMIENTOS:")
    if not usuario_data["historial"]:
        print("No hay movimientos registrados todavía.")
    else:
        for mov in usuario_data["historial"]:
            print("•", mov)


def cajero(usuario_data):
    nombre = usuario_data["nombre"]

    while True:
        mostrar_menu(nombre)
        opcion = pedir_opcion()

        if opcion == "1":
            # Consultar saldo
            print(f"\n💰 Tu saldo actual es: ${usuario_data['saldo']:.2f}")

        elif opcion == "2":
            # Depositar dinero
            monto = pedir_monto("¿Cuánto deseas depositar? $")
            usuario_data["saldo"] += monto
            usuario_data["historial"].append(f"Depósito: +${monto:.2f}")
            print("✔ Depósito realizado con éxito.")

        elif opcion == "3":
            # Retirar dinero
            monto = pedir_monto("¿Cuánto deseas retirar? $")
            if monto > usuario_data["saldo"]:
                print("❌ Fondos insuficientes para realizar esta operación.")
            else:
                usuario_data["saldo"] -= monto
                usuario_data["historial"].append(f"Retiro: -${monto:.2f}")
                print("✔ Retiro realizado con éxito.")

        elif opcion == "4":
            # Ver historial
            mostrar_historial(usuario_data)

        elif opcion == "5":
            print("👋 Gracias por usar el cajero. Volviendo a la pantalla de inicio de sesión...\n")
            break


def main():
    print("*** Bienvenido al Cajero Automático ***\n")

    while True:
        pin, usuario_data = iniciar_sesion()

        # Si iniciar_sesion devuelve (None, None), el usuario salió o se bloqueó
        if pin is None and usuario_data is None:
            print("*** Saliendo del sistema... ***")
            break

        # Si el login fue correcto, entramos al cajero para ese usuario
        cajero(usuario_data)


if __name__ == "__main__":
    main()
