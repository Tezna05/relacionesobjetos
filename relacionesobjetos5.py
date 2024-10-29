class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    def mostrar_informacion(self):
        print(f"Producto: {self._nombre}, Precio: ${self._precio:.2f}")


# Ejemplo de uso:
producto = Producto("Laptop", 1500.00)
producto.mostrar_informacion()

# Intentar cambiar el precio a un valor válido
producto.precio = 1200.00
producto.mostrar_informacion()

# Intentar cambiar el precio a un valor negativo
producto.precio = -500.00
producto.mostrar_informacion()
