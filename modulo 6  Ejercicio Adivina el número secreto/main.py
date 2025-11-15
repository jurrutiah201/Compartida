from juego.generar import seleccion_dificultad, generar_numero
from juego.intentos import controlar_intentos
from juegos.reiniciar import pregunta_continuar
from juegos.mensajes import bienvenida, despedida

def main()v:
    bienvenida()
    
    jugar = True
    
    while jugar:
        nivel_dificultad = seleccion_dificultad()
        numero_secreto = generar_numero(nivel_dificultad)
        
        print("\n***** Intenta adivinar el numero secreto *****")
        print(f"\nEl numero esta entre 1 y {nivel_dificultad}")
        print("Tienes 5 intentos, !Buena suerte!\n")
        
        controlar_intentos(numero_secreto,nivel_dificultad)
        
        jugar = pregunta_continuar
        
    despedida()
