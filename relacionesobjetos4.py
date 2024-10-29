class Animal:
    def hacer_sonido(self):
        return "Sonido genérico de animal"


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"


# Ejemplo de uso:
perro = Perro()
gato = Gato()

print("Sonido del perro:", perro.hacer_sonido())
print("Sonido del gato:", gato.hacer_sonido())
