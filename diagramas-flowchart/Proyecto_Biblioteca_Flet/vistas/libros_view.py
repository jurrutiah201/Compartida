import flet as ft
from modelos.libro import Libro
from data.persistence import cargar_libros, guardar_libros


def crear_vista_libros(page: ft.Page) -> ft.Container:
    """Vista para gestión de libros."""

    # 🔹 Cargar libros guardados
    lista_libros = cargar_libros()

    titulo_input = ft.TextField(label="Título del libro", width=300)
    autor_input = ft.TextField(label="Autor", width=300)
    isbn_input = ft.TextField(label="ISBN", width=200)

    lista_visual = ft.Column()

    # --- Actualizar lista en pantalla ---
    def actualizar_lista():
        lista_visual.controls.clear()
        for libro in lista_libros:
            lista_visual.controls.append(
                ft.Text(
                    f"{libro.titulo} - {libro.autor} | ISBN: {libro.isbn} | Estado: {libro.estado}"
                )
            )
        page.update()

    actualizar_lista()

    # --- Agregar libro ---
    def agregar_libro(e):
        if not titulo_input.value or not autor_input.value or not isbn_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Todos los campos son obligatorios"))
            page.snack_bar.open = True
            page.update()
            return

        # Validar ISBN repetido
        for libro in lista_libros:
            if libro.isbn == isbn_input.value:
                page.snack_bar = ft.SnackBar(ft.Text("Ya existe un libro con ese ISBN"))
                page.snack_bar.open = True
                page.update()
                return

        nuevo_libro = Libro(
            titulo=titulo_input.value,
            autor=autor_input.value,
            isbn=isbn_input.value,
        )

        lista_libros.append(nuevo_libro)
        guardar_libros(lista_libros)

        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""

        actualizar_lista()

    boton_agregar = ft.ElevatedButton("Agregar libro", on_click=agregar_libro)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Gestión de Libros", size=22, weight="bold"),
                ft.Row([titulo_input]),
                ft.Row([autor_input]),
                ft.Row([isbn_input]),
                boton_agregar,
                ft.Divider(),
                ft.Text("Inventario de libros:", size=18, weight="w600"),
                lista_visual,
            ],
            expand=True,
        ),
        padding=20,
    )
