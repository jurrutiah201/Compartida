from juegos.Dificultad import seleccionar_dificultad
from juegos.generar_numero import generar_numero
from juegos.controlar_intentos import controlar_intentos
from juegos import bienvenida, despedida, pregunta_continuar


def main():
    bienvenida()

    jugar = True
    while jugar:
        # 1. Elegir dificultad (1-10, 1-20, 1-50)
        limite_superior = seleccionar_dificultad()

        # 2. Generar número secreto según dificultad
        numero_secreto = generar_numero(limite_superior)

        print("\n***** Intenta adivinar el número secreto *****")
        print(f"El número está entre 1 y {limite_superior}")
        print("Tienes 5 intentos, ¡buena suerte!\n")

        # 3. Manejar los intentos del jugador
        controlar_intentos(numero_secreto)

        # 4. Preguntar si quiere jugar otra vez
        jugar = pregunta_continuar()

    despedida()


if __name__ == "__main__":
    main()
