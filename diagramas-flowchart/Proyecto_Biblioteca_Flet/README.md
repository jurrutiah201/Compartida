# Proyecto Biblioteca con Flet

Sistema de control de biblioteca hecho en Python + Flet.

## Cómo ejecutar

1. Abrir el proyecto desde la carpeta raíz del repositorio.
2. En la terminal, ir a la carpeta del proyecto:

   ```bash
   cd diagramas-flowchart/Proyecto_Biblioteca_Flet
   python main.py

### Funcionalidades implementadas hasta ahora:

1. Gestión de Libros:
Formulario para registrar libros (Título, Autor, ISBN).

2. Lista de inventario que se actualiza al agregar un libro.

3. Gestión de Clientes:
Formulario para registrar clientes (Nombre, Apellido, Cédula).

4. Lista de clientes registrados en la sesión.

#### Pendientes para terminar el proyecto:

1. Préstamo de Libros

2. Vista donde se pueda:
Seleccionar un libro disponible.
Seleccionar un cliente.
Registrar el préstamo (cambiar estado del libro a "Prestado" y guardar quién lo tiene).
Validar que solo se puedan prestar libros con estado Disponible.

3. (Opcional) Devolución de Libros. Si quieren agregar dicha parte.
Permitir seleccionar un libro prestado y marcarlo como "Disponible" de nuevo.

4. Datos del equipo:
Cada integrante debe agregarse en data/clientes_data.py

5. Mejorar mensajes de error / validaciones en formularios.

6. Agregar los diagramas pendientes.