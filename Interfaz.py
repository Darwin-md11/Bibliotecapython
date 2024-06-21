import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Autor import Autor
from Biblioteca import Biblioteca
from Categoria import Categoria
from Libro import Libro
from Usuario import Usuario

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Biblioteca Celular")

        # Ajustar tamaño de la ventana y centrar en la pantalla
        self.root.geometry("400x700")  # Tamaño adecuado para dispositivos móviles
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (700 // 2)
        self.root.geometry(f"400x700+{x}+{y}")

        # Crear una instancia de Biblioteca
        self.biblioteca = Biblioteca()

        # Estilo para los widgets
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TEntry", fieldbackground="#ffffff")
        self.style.configure("TButton", background="#e0e0e0", font=("Arial", 10))

        # Frame para contener las pestañas y la imagen
        self.frame_tabs_imagen = ttk.Frame(self.root, style="TFrame")
        self.frame_tabs_imagen.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Notebook para las pestañas
        self.notebook = ttk.Notebook(self.frame_tabs_imagen)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Frame para la imagen de la biblioteca
        self.frame_imagen = ttk.Frame(self.frame_tabs_imagen, style="TFrame")
        self.frame_imagen.pack(pady=10, padx=10, fill=tk.BOTH, expand=True, side=tk.BOTTOM)

        # Mostrar imagen con transición al abrir la aplicación
        self.mostrar_imagen_con_transicion()

        # Llamar a iniciar_aplicacion después de un breve retraso
        self.root.after(2000, self.iniciar_aplicacion)  # Retraso de 2000 milisegundos (2 segundos)

    def mostrar_imagen_con_transicion(self):
        # Cargar imagen y mostrar con transición
        imagen = Image.open("imagen.png")  # Reemplaza "imagen.png" con la ruta de tu imagen
        imagen = imagen.resize((400, 300))  # Ajustar tamaño para la ventana móvil
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.label_imagen = ttk.Label(self.frame_imagen, image=self.imagen_tk)
        self.label_imagen.pack()

    def iniciar_aplicacion(self):
        # Crear las pestañas
        self.tab_registro_libro = ttk.Frame(self.notebook, style="TFrame")
        self.tab_mostrar_libros = ttk.Frame(self.notebook, style="TFrame")
        self.tab_registro_usuario = ttk.Frame(self.notebook, style="TFrame")

        self.notebook.add(self.tab_registro_libro, text="Registrar Libro")
        self.notebook.add(self.tab_mostrar_libros, text="Mostrar Libros")
        self.notebook.add(self.tab_registro_usuario, text="Registrar Usuario")

        # Configurar cada pestaña
        self.configurar_tab_registro_libro()
        self.configurar_tab_mostrar_libros()
        self.configurar_tab_registro_usuario()

        # Botón para alternar entre las pestañas
        self.boton_alternar = ttk.Button(self.frame_tabs_imagen, text="Alternar Pestañas", command=self.alternar_pestanas)
        self.boton_alternar.pack(pady=10, padx=10, anchor=tk.NW)  # Alineación al noroeste

    def configurar_tab_registro_libro(self):
        ttk.Label(self.tab_registro_libro, text="Registrar Libro", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.tab_registro_libro, text="Título").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_titulo = ttk.Entry(self.tab_registro_libro)
        self.entry_titulo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.tab_registro_libro, text="ISBN").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_isbn = ttk.Entry(self.tab_registro_libro)
        self.entry_isbn.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.tab_registro_libro, text="Registrar Libro", command=self.registrar_libro).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def configurar_tab_mostrar_libros(self):
        ttk.Label(self.tab_mostrar_libros, text="Seleccionar Libro", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.combo_libros = ttk.Combobox(self.tab_mostrar_libros, state="readonly", width=30)
        self.combo_libros.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.combo_libros.bind("<<ComboboxSelected>>", self.mostrar_info_libro)

        self.label_info_libro = ttk.Label(self.tab_mostrar_libros, text="", font=("Arial", 10), wraplength=380)
        self.label_info_libro.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.actualizar_combo_libros()

    def configurar_tab_registro_usuario(self):
        ttk.Label(self.tab_registro_usuario, text="Registrar Usuario", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        ttk.Label(self.tab_registro_usuario, text="Nombre").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(self.tab_registro_usuario)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.tab_registro_usuario, text="Apellido").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_apellido = ttk.Entry(self.tab_registro_usuario)
        self.entry_apellido.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.tab_registro_usuario, text="Registrar Usuario", command=self.registrar_usuario).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def registrar_libro(self):
        titulo = self.entry_titulo.get()
        isbn = self.entry_isbn.get()
        autor = Autor("Gabriel", "García Márquez")
        categoria = Categoria("Ficción")
        libro = Libro(titulo, isbn, autor, categoria)
        self.biblioteca.registrar_libro(libro)
        self.actualizar_combo_libros()
        self.entry_titulo.delete(0, tk.END)
        self.entry_isbn.delete(0, tk.END)
        messagebox.showinfo("Registro exitoso", f"Libro '{titulo}' registrado con éxito")

    def actualizar_combo_libros(self):
        libros_disponibles = [libro.titulo for libro in self.biblioteca.libros]
        self.combo_libros["values"] = libros_disponibles

    def mostrar_info_libro(self, event):
        selected_book = self.combo_libros.get()
        if selected_book:
            libro = self.biblioteca.buscar_libro_por_titulo(selected_book)
            if libro:
                info = f"Título: {libro.titulo}\nISBN: {libro.isbn}\nAutor: {libro.autor.nombre} {libro.autor.apellido}\nCategoría: {libro.categoria.nombre}"
                self.label_info_libro.config(text=info)
            else:
                self.label_info_libro.config(text="No se encontró información del libro seleccionado.")
        else:
            self.label_info_libro.config(text="")

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        usuario = Usuario(nombre, apellido, 12345)
        self.biblioteca.registrar_usuario(usuario)
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito")

    def alternar_pestanas(self):
        current_tab = self.notebook.index("current")
        next_tab = (current_tab + 1) % self.notebook.index("end")
        self.notebook.select(next_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
