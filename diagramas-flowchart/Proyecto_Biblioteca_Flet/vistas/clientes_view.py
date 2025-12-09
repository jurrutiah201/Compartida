import flet as ft
from data.clientes_data import lista_clientes
from modelos.cliente import Cliente


def crear_vista_clientes(page: ft.Page) -> ft.Container:
    """Vista para la gestión de clientes."""

    nombre_input = ft.TextField(label="Nombre", width=250)
    apellido_input = ft.TextField(label="Apellido", width=250)
    cedula_input = ft.TextField(label="Cédula/ID", width=200)

    lista_visual = ft.Column()

    # --- Función para actualizar la lista en pantalla ---
    def actualizar_lista():
        lista_visual.controls.clear()
        for cli in lista_clientes:
            lista_visual.controls.append(
                ft.Text(f"{cli.nombre} {cli.apellido} - {cli.cedula}")
            )
        page.update()

    actualizar_lista()

    # --- Función para agregar cliente ---
    def agregar_cliente(e):
        if not nombre_input.value or not apellido_input.value or not cedula_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Todos los campos son obligatorios"))
            page.snack_bar.open = True
            page.update()
            return

        # Validar si la cédula ya existe
        for cli in lista_clientes:
            if cli.cedula == cedula_input.value:
                page.snack_bar = ft.SnackBar(ft.Text("Ya existe un cliente con esa cédula"))
                page.snack_bar.open = True
                page.update()
                return

        nuevo_cliente = Cliente(
            nombre_input.value,
            apellido_input.value,
            cedula_input.value
        )

        lista_clientes.append(nuevo_cliente)

        # Limpiar campos
        nombre_input.value = ""
        apellido_input.value = ""
        cedula_input.value = ""

        actualizar_lista()

    boton_agregar = ft.ElevatedButton("Registrar Cliente", on_click=agregar_cliente)

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Gestión de Clientes", size=22, weight="bold"),
                ft.Row([nombre_input]),
                ft.Row([apellido_input]),
                ft.Row([cedula_input]),
                boton_agregar,
                ft.Divider(),
                ft.Text("Clientes registrados:", size=18, weight="w600"),
                lista_visual,
            ]
        )
    )
