class Libro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        estado: str = "Disponible",
        prestado_a: str | None = None,
        categoria: str | None = None,
    ):
        if not titulo or not autor or not isbn:
            raise ValueError("Título, autor e ISBN son obligatorios")
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado
        self.prestado_a = prestado_a
        self.categoria = categoria

    @property
    def disponible(self) -> bool:
        return self.estado == "Disponible"

    def prestar_a(self, cliente_id: str):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")
        self.estado = "Prestado"
        self.prestado_a = cliente_id

    def devolver(self):
        if self.disponible:
            raise ValueError("El libro no está prestado")
        self.estado = "Disponible"
        self.prestado_a = None

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}', estado='{self.estado}')"
