
# 1. Crear una tupla con 3 estudiantes
# Cada estudiante tiene nombre, edad y materias

estudiantes = (
    ("Juan", 20, ["Matemática", "Programación"]),
    ("Ana", 22, ["Inglés", "Base de Datos"]),
    ("Pedro", 19, ["Historia", "Programación"])
)

# 2. Convertir la tupla en una lista
lista_estudiantes = list(estudiantes)

# Agregar un nuevo estudiante
lista_estudiantes.append(
    ("Lucía", 21, ["Matemática", "Inglés", "Historia"])
)

# 3. Convertir la lista en un diccionario
# La clave será el nombre del estudiante

diccionario_estudiantes = {}

for nombre, edad, materias in lista_estudiantes:
    diccionario_estudiantes[nombre] = {
        "edad": edad,
        "materias": materias
    }

# 4. Imprimir los datos de cada estudiante

print("=== SISTEMA DE ESTUDIANTES ===")

for nombre, datos in diccionario_estudiantes.items():
    print("-------------------------")
    print("Nombre:", nombre)
    print("Edad:", datos["edad"])
    print("Materias:")

    for materia in datos["materias"]:
        print(" -", materia)
