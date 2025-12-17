import flet as ft
from vistas.libros_view import crear_vista_libros
from vistas.clientes_view import crear_vista_clientes
from vistas.prestamos_view import crear_vista_prestamos


def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    contenido = ft.Column(expand=True)

    def cambiar_vista(e):
        contenido.controls.clear()

        if e.control.selected_index == 0:
            contenido.controls.append(crear_vista_libros(page))
        elif e.control.selected_index == 1:
            contenido.controls.append(crear_vista_clientes(page))
        elif e.control.selected_index == 2:
            contenido.controls.append(crear_vista_prestamos(page))

        page.update()

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Libros"),
            ft.Tab(text="Clientes"),
            ft.Tab(text="Préstamos"),
        ],
        on_change=cambiar_vista,
    )

    contenido.controls.append(crear_vista_libros(page))

    page.add(
        ft.Column(
            controls=[
                ft.Text("Sistema de Biblioteca con Flet", size=26, weight="bold"),
                tabs,
                ft.Divider(),
                contenido,
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
