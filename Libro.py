class Libro:
    def __init__(self, titulo, isbn, autor, categoria):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor.nombre} {self.autor.apellido}")
        print(f"Categoría: {self.categoria.nombre}")
