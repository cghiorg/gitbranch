class Animal:
    def hablar(self):
        return "Sonido genérico"


class Perro(Animal):
    def hablar(self):
        return "Guauu"
    

class Gato(Animal):
    def hablar(self):
        return "Miauu"
    

animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hablar())
