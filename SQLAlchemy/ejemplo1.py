from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creamos la aplicación Flask
app = Flask(__name__)

# Indicamos dónde guardar la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.db"

# Asociamos SQLAlchemy con Flask
db = SQLAlchemy(app)


# Creamos el modelo Producto
class Producto(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)
    
    descripcion = db.Column(db.String(150), nullable=False)

    precio = db.Column(db.Float, nullable=False)


with app.app_context():

    productos = Producto.query.all()

    for producto in productos:
        print(producto.nombre, producto.descripcion, producto.precio)


# Creamos las tablas
with app.app_context():
    db.create_all()

    print("Base de datos preparada correctamente")