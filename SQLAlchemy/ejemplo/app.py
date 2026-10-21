
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///productos.db"

db = SQLAlchemy(app)


# MODELO
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    fecha_ingreso = db.Column(db.Date,nullable=False,default=date.today)
    
    
# MOSTRAR PRODUCTOS
@app.route("/")
def inicio():

    productos = Producto.query.order_by(Producto.id).all()

    return render_template(
        "productos.html",
        productos=productos
    )


# AGREGAR PRODUCTO
@app.route("/agregar", methods=["POST"])
def agregar():

    nombre = request.form.get("nombre", "").strip()
    precio_texto = request.form.get("precio", "")
    stock = request.form.get("stock", "")
    fecha_ingreso = date.fromisoformat(request.form["fecha_ingreso"])


    try:
        precio = float(precio_texto)
    except (ValueError, TypeError):
        return "El precio debe ser un número", 400

    if not nombre or precio < 0:
        return "Datos del producto inválidos", 400

    nuevo = Producto(
        nombre=nombre,
        precio=precio,
        stock=stock,
        fecha_ingreso=fecha_ingreso
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for("inicio"))


# ACTUALIZAR PRODUCTO
@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):

    producto = db.get_or_404(Producto, id)

    try:
        precio = float(request.form["precio"])
    except (ValueError, KeyError):
        return "Precio inválido", 400

    if precio < 0:
        return "El precio no puede ser negativo", 400

    producto.precio = precio

    db.session.commit()

    return redirect(url_for("inicio"))


# ELIMINAR PRODUCTO
@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):

    producto = db.get_or_404(Producto, id)

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for("inicio"))


# CREAR BASE DE DATOS
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
