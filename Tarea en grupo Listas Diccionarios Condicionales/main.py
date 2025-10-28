# Tarea grupal 3 - Listas, Diccionarios y Condicionales
# Grupo B - Programación III

# Lista de nombres
nombres = ["Ana", "Carlos", "Lucía", "Miguel", "Rances"]

# Diccionario con las edades
edades = {
    "Michael": 25,
    "Jose": 25,
    "David": 31,
    "Alexis": 35,
    "Rances": 23
}

# Solicitar nombre al usuario
# Agregamos .capitalize() para estandarizar la entrada y evitar problemas con mayúsculas/minúsculas
print("Hola, bienvenido al sistema de registro de edades.")
nombre_usuario = input("Ingresa un nombre: ").capitalize()

# Verificar si el nombre existe en el diccionario
if nombre_usuario in edades:
    print(f"{nombre_usuario} tiene {edades[nombre_usuario]} años.")
else:
    print(f"La persona '{nombre_usuario}' no fue encontrada en el registro.")
