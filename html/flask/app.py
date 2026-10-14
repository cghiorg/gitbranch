from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():

    nombre = "Juan"

    return render_template(
        "index.html",
        nombre=nombre
    )
    
@app.route("/contacto")
def contacto():
    return "Página de contacto"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola tu nombre es {nombre}"

@app.route("/edad/<nombre>/<int:edad>")
def edad(nombre, edad):

    if edad >= 18:
        estado = "mayor de edad"
    else:
        estado = "menor de edad"

    return f"{nombre} tiene {edad} años y es {estado}"


@app.route("/productos")
def productos():

    productos = [
        "Notebook",
        "Mouse",
        "Teclado",
        "Monitor",
        "Disco Rigido"
    ]

    return render_template(
        "productos.html",
        productos=productos
    )

@app.route("/formulario", methods=["GET", "POST"])
def formulario():

    if request.method == "POST":

        nombre = request.form["nombre"]

        return f"Hola {nombre}"

    return render_template("formulario.html")

@app.route("/nosotros")
def nosotros():
    return "Información sobre nosotros"


if __name__ == "__main__":
    app.run(debug=True)