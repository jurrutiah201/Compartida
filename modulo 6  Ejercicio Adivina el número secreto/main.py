from juegos.Dificultad import seleccionar_dificultad
from juegos.utilidad import mensaje_perder, mostrar_mayor, mostrar_menor
from juegos.generar_numero import random as generar_numero
from juegos import controlar_intentos
from juegos import pregunta_continuar
from juegos import bienvenida, despedida


def main():
    bienvenida()
    
    jugar = True
    
    while jugar:
        nivel_dificultad = seleccionar_dificultad()
        numero_secreto = generar_numero(nivel_dificultad)
        
        print("\n***** Intenta adivinar el numero secreto *****")
        print(f"\nEl numero esta entre 1 y {nivel_dificultad}")
        print("Tienes 5 intentos, !Buena suerte!\n")
        
        controlar_intentos(numero_secreto,nivel_dificultad)
        
        jugar = pregunta_continuar
        
    despedida()
