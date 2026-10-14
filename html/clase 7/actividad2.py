# 1. Crear la clase Vehiculo
class Vehiculo:

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)


# 2. Crear la subclase Auto
class Auto(Vehiculo):

    def __init__(self, marca, modelo, anio, puertas):
        # Llamar al constructor de la clase padre
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    # Sobreescribir el método mostrar_info
    def mostrar_info(self):
        super().mostrar_info()
        print("Puertas:", self.puertas)


# 3. Crear un objeto de la clase Vehiculo
vehiculo1 = Vehiculo("Honda", "CB 250", 2022)

# 4. Crear un objeto de la clase Auto
auto1 = Auto("Toyota", "Corolla", 2023, 4)


# 5. Mostrar la información
print("=== VEHÍCULO ===")
vehiculo1.mostrar_info()

print("\n=== AUTO ===")
auto1.mostrar_info()
