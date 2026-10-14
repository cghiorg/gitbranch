diccionario_estudiantes = {}


for nombre, edad, materias in lista_estudiantes:
    diccionario_estudiantes[nombre] = {
        "edad": edad,
        "materias": materias
    }


print("=== SISTEMA DE ESTUDIANTES ===")

for nombre, datos in diccionario_estudiantes.items():
    print("-------------------------")
    print("Nombre:", nombre)
    print("Edad:", datos["edad"])
    print("Materias:")

    for materia in datos["materias"]:
        print(" -", materia)