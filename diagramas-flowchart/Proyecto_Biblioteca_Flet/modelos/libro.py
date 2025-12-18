class Libro:
    """
    Representa un libro en la biblioteca con gestión de estado y préstamos.
    """

    # Usamos constantes de clase para evitar errores de dedo al escribir "Disponible" o "Prestado"
    ESTADO_DISPONIBLE = "Disponible"
    ESTADO_PRESTADO = "Prestado"

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        categoria: str = "General"
    ):
        # Validaciones básicas
        if not titulo or not isbn:
            raise ValueError("El título y el ISBN son obligatorios.")

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria = categoria
        
        # Inicializamos siempre como disponible
        self._estado = self.ESTADO_DISPONIBLE 
        self._prestado_a = None  # ID del cliente

    @property
    def estado(self):
        """Permite leer el estado pero no modificarlo directamente desde fuera."""
        return self._estado

    @property
    def prestado_a(self):
        """Permite ver a quién se prestó, pero protege la variable."""
        return self._prestado_a

    def prestar_a(self, cliente_id: str) -> bool:
        """
        Intenta prestar el libro a un cliente.
        Retorna True si tuvo éxito, False si el libro ya estaba prestado.
        """
        if self._estado == self.ESTADO_PRESTADO:
            print(f"❌ Error: El libro '{self.titulo}' ya está prestado a {self._prestado_a}.")
            return False
        
        self._estado = self.ESTADO_PRESTADO
        self._prestado_a = cliente_id
        print(f"✅ Éxito: Libro '{self.titulo}' prestado a cliente {cliente_id}.")
        return True

    def devolver(self) -> bool:
        """
        Registra la devolución del libro.
        Retorna True si se devolvió correctamente, False si ya estaba disponible.
        """
        if self._estado == self.ESTADO_DISPONIBLE:
            print(f"⚠️ Aviso: El libro '{self.titulo}' ya estaba disponible en estantería.")
            return False

        cliente_anterior = self._prestado_a
        self._estado = self.ESTADO_DISPONIBLE
        self._prestado_a = None
        print(f"📚 Libro '{self.titulo}' devuelto por el cliente {cliente_anterior}.")
        return True

    def __str__(self):
        """Representación en texto del libro para imprimirlo bonito."""
        info = f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn})"
        if self._estado == self.ESTADO_PRESTADO:
            return f"{info} - [PRESTADO a: {self._prestado_a}]"
        return f"{info} - [DISPONIBLE]"

# --- BLOQUE DE PRUEBA ---
if __name__ == "__main__":
    # 1. Crear un libro
    try:
        mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
        print(mi_libro)  # Usa el método __str__

        # 2. Prestarlo a Juan
        mi_libro.prestar_a("JuanPerez123")
        print(mi_libro)

        # 3. Intentar prestarlo a María (Debería fallar)
        mi_libro.prestar_a("MariaLopez456")

        # 4. Devolverlo
        mi_libro.devolver()
        print(mi_libro)

        # 5. Intentar devolverlo de nuevo (Debería avisar)
        mi_libro.devolver()

    except ValueError as e:
        print(f"Error al crear el libro: {e}")
