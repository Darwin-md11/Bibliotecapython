class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} {self.apellido} (ID: {self.id_usuario})")