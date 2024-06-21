from Prestamo import Prestamo
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)

    def devolver_libro(self, prestamo):
        self.prestamos.remove(prestamo)

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            libro.mostrar_info()

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

