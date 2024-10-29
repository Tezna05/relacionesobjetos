class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class Clase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        if self.estudiantes:
            print(f"Estudiantes en la clase {self.nombre}:")
            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre}")
        else:
            print(f"No hay estudiantes en la clase {self.nombre}.")


# Ejemplo de uso:
estudiante1 = Estudiante("villegas")
estudiante2 = Estudiante("mao ying")
estudiante3 = Estudiante("fabian")

clase_matematicas = Clase("Matemáticas")
clase_matematicas.agregar_estudiante(estudiante1)
clase_matematicas.agregar_estudiante(estudiante2)

clase_lengua = Clase("Lengua")
clase_lengua.agregar_estudiante(estudiante3)

# Listar los estudiantes de cada clase
clase_matematicas.listar_estudiantes()
clase_lengua.listar_estudiantes()
