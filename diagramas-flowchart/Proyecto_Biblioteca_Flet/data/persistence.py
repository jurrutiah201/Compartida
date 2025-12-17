import json
import os
from modelos.cliente import Cliente
from modelos.libro import Libro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------- CLIENTES ----------
def guardar_clientes(lista_clientes):
    data = [
        {"nombre": c.nombre, "apellido": c.apellido, "cedula": c.cedula}
        for c in lista_clientes
    ]
    with open(os.path.join(BASE_DIR, "clientes.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def cargar_clientes():
    try:
        with open(os.path.join(BASE_DIR, "clientes.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Cliente(**c) for c in data]
    except FileNotFoundError:
        return []


# ---------- LIBROS ----------
def guardar_libros(lista_libros):
    data = [
        {
            "titulo": l.titulo,
            "autor": l.autor,
            "isbn": l.isbn,
            "estado": l.estado,
            "prestado_a": l.prestado_a,
            "categoria": l.categoria,
        }
        for l in lista_libros
    ]
    with open(os.path.join(BASE_DIR, "libros.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def cargar_libros():
    try:
        with open(os.path.join(BASE_DIR, "libros.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Libro(**l) for l in data]
    except FileNotFoundError:
        return []
