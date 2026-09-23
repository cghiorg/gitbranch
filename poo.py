class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre} - ${self.precio} - Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def valor_inventario(self):
        return self.precio * self.stock

notebook = Producto("Notebook", 1200000, 5)
mouse = Producto("Mouse", 25000, 20)

notebook.mostrar_info()
notebook.actualizar_stock(-1)
notebook.mostrar_info()
print(notebook.valor_inventario())

mouse.mostrar_info()


