# Tarea grupal 3 - Listas, Diccionarios y Condicionales
# Grupo B - Programación III

# Lista de nombres
nombres = ["Ana", "Carlos", "Lucía", "Miguel", "Rances"]

# Diccionario con las edades
edades = {
    "Michael": 30,
    "Jose": 25,
    "David": 28,
    "Alexis": 35,
    "Rances": 23
}

# Solicitar nombre al usuario
nombre_usuario = input("Ingresa un nombre: ")

# Verificar si el nombre existe en el diccionario
if nombre_usuario in edades:
    print(f"{nombre_usuario} tiene {edades[nombre_usuario]} años.")
else:
    print(f"La persona '{nombre_usuario}' no fue encontrada en el registro.")
