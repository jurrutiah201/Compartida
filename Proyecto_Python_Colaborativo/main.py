# main.py

# Importamos las funciones específicas de nuestros módulos
from matematicas.operaciones import sumar
from cuentos.historia import imprimir_cuento_base
from utilidades.mensajes import saludo_bienvenida  

print("### DEMO DEL PROYECTO COLABORATIVO ###")

# Usamos la función del módulo de matemáticas
resultado_suma = sumar(50, 12)
print(f"\nResultado de la suma: {resultado_suma}")

# Usamos la función del módulo de cuentos
print("\nIniciando la impresión del cuento:")
imprimir_cuento_base()

# Usamos la función del nuevo módulo de utilidades
nombre_usuario = "Equipo"
print("\nProbando el módulo de utilidades:")
print(saludo_bienvenida(nombre_usuario))
