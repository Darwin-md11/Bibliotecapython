class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        print(f"Autor: {self.nombre} {self.apellido}")
