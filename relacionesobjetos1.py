class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if self.libros:
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene libros registrados.")


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        autor.agregar_libro(self)


# Ejemplo de uso:
autor1 = Autor("Isabel Allende")
libro1 = Libro("La casa de los espíritus", autor1)
libro2 = Libro("Paula", autor1)

autor1.mostrar_libros()
