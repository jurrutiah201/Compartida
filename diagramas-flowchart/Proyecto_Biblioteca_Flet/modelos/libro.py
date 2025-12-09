class Libro:
    def __init__(
        self,
        titulo,
        autor,
        isbn,
        estado="Disponible",
        prestado_a=None,
        categoria=None,
    ):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado
        self.prestado_a = prestado_a
        self.categoria = categoria


    def prestar_a(self, cliente_id: str):
        self.estado = "Prestado"
        self.prestado_a = cliente_id

    def devolver(self):
        self.estado = "Disponible"
        self.prestado_a = None
