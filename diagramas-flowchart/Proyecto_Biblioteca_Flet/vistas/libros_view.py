import flet as ft


def crear_vista_libros(page: ft.Page) -> ft.Container:
    """Vista para gestión de libros (versión base)."""

    titulo_input = ft.TextField(label="Título del libro", width=300)
    autor_input = ft.TextField(label="Autor", width=300)
    isbn_input = ft.TextField(label="ISBN", width=200)

    lista_libros = ft.Column()

    def agregar_libro(e):
        if not titulo_input.value or not autor_input.value or not isbn_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Todos los campos son obligatorios"))
            page.snack_bar.open = True
            page.update()
            return

        lista_libros.controls.append(
            ft.Text(
                f"{titulo_input.value} - {autor_input.value} (ISBN: {isbn_input.value})"
            )
        )

        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""
        page.update()

    boton_agregar = ft.ElevatedButton("Agregar libro", on_click=agregar_libro)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Gestión de Libros", size=22, weight="bold"),
                ft.Row(controls=[titulo_input]),
                ft.Row(controls=[autor_input]),
                ft.Row(controls=[isbn_input]),
                ft.Row(controls=[boton_agregar]),
                ft.Divider(),
                ft.Text("Inventario de libros:", size=18, weight="w600"),
                lista_libros,
            ],
            expand=True,
        ),
        padding=20,
    )
