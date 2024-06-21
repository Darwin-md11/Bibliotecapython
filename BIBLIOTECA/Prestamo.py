
class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        print("Información del préstamo:")
        self.libro.mostrar_info()
        self.usuario.mostrar_info()
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")

