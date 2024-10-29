class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"El motor {self.tipo} está encendido.")


class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)  # El motor se crea como parte del coche

    def encender_motor(self):
        print(f"Encendiendo el coche {self.marca}...")
        self.motor.encender()


# Ejemplo de uso:
coche1 = Coche("Toyota", "V8")
coche1.encender_motor()
