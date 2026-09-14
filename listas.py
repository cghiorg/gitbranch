provincias = [ "Tierra del Fuego", "Santa Cruz", "Chubut", "Río Negro", "Neuquén" ]

print(provincias[2])


print (len(provincias))

provincias.append("Buenos Aires")

provincias.insert(2, "Jujuy")

print(provincias)

mas_provincias = ["Córdoba", "Mendoza"]

provincias.extend(mas_provincias)

print(provincias)

provincias.pop()

provincias.pop(1)

del provincias[1]

