import flet as ft
from data.persistence import cargar_libros, guardar_libros, cargar_clientes


def crear_vista_prestamos(page: ft.Page) -> ft.Container:
    # 🔹 Cargar datos persistentes
    lista_libros = cargar_libros()
    lista_clientes = cargar_clientes()

    libro_dropdown = ft.Dropdown(label="Libro disponible", width=400)
    cliente_dropdown = ft.Dropdown(label="Cliente", width=400)
    libro_prestado_dropdown = ft.Dropdown(label="Libro prestado", width=400)

    lista_visual = ft.Column()

    # --- Actualizar dropdowns ---
    def actualizar_dropdowns():
        libro_dropdown.options = [
            ft.dropdown.Option(
                libro.isbn,
                f"{libro.titulo}"
            )
            for libro in lista_libros
            if libro.estado == "Disponible"
        ]

        libro_prestado_dropdown.options = [
            ft.dropdown.Option(
                libro.isbn,
                f"{libro.titulo}"
            )
            for libro in lista_libros
            if libro.estado == "Prestado"
        ]

        cliente_dropdown.options = [
            ft.dropdown.Option(
                cli.cedula,
                cli.nombre_completo()
            )
            for cli in lista_clientes
        ]

        page.update()

    # --- Actualizar lista visual ---
    def actualizar_lista():
        lista_visual.controls.clear()
        for libro in lista_libros:
            if libro.estado == "Prestado":
                lista_visual.controls.append(
                    ft.Text(
                        f"{libro.titulo} → Prestado a {libro.prestado_a}"
                    )
                )
        page.update()

    # --- Prestar libro ---
    def prestar_libro(e):
        if not libro_dropdown.value or not cliente_dropdown.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Debe seleccionar un libro y un cliente")
            )
            page.snack_bar.open = True
            page.update()
            return

        for libro in lista_libros:
            if libro.isbn == libro_dropdown.value:
                libro.prestar_a(cliente_dropdown.value)
                guardar_libros(lista_libros)
                break

        actualizar_dropdowns()
        actualizar_lista()

    # --- Devolver libro ---
    def devolver_libro(e):
        if not libro_prestado_dropdown.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Seleccione un libro prestado")
            )
            page.snack_bar.open = True
            page.update()
            return

        for libro in lista_libros:
            if libro.isbn == libro_prestado_dropdown.value:
                libro.devolver()
                guardar_libros(lista_libros)
                break

        actualizar_dropdowns()
        actualizar_lista()

    actualizar_dropdowns()
    actualizar_lista()

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Préstamo de Libros", size=22, weight="bold"),

                libro_dropdown,
                cliente_dropdown,
                ft.ElevatedButton("Prestar libro", on_click=prestar_libro),

                ft.Divider(),

                libro_prestado_dropdown,
                ft.ElevatedButton("Devolver libro", on_click=devolver_libro),

                ft.Divider(),
                ft.Text("Libros prestados:", size=18),
                lista_visual,
            ]
        ),
    )

