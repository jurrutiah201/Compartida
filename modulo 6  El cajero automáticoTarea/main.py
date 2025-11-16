from sistemas.Login import iniciar_sesion

print("***Bienvenido al Cajero Automático***\n")

while True:
    pin, usuario = iniciar_sesion()

    if usuario is None and pin is None:
        print("***Saliendo del sistema.***")
        break
