import flet as ft
from vistas.libros_view import crear_vista_libros
from vistas.clientes_view import crear_vista_clientes


def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    # Aquí se mostrará la vista seleccionada (Libros / Clientes)
    contenido = ft.Column(expand=True)

    # Cambiar entre pestañas
    def cambiar_vista(e):
        seleccion = e.control.selected_index
        contenido.controls.clear()

        if seleccion == 0:           # Pestaña Libros
            contenido.controls.append(crear_vista_libros(page))
        elif seleccion == 1:         # Pestaña Clientes
            contenido.controls.append(crear_vista_clientes(page))

        page.update()

    # Pestañas de la app
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Libros"),
            ft.Tab(text="Clientes"),
        ],
        on_change=cambiar_vista,
    )

    # Vista inicial (Libros)
    contenido.controls.append(crear_vista_libros(page))

    # Layout principal
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
