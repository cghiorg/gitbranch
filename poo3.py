class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años." 

class Estudiante(Persona):
    def __init__(self, nombre, edad, legajo, carrera):
        super().__init__(nombre, edad)
        self.legajo = legajo
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."


alumno1 = Estudiante("Lucía",
    24,
    "A1542",
    "Ciencia de Datos"
)

print(alumno1.estudiar())

print(alumno1.presentarse())

