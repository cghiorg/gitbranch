from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():

    usuario = "Juan Perez"

    return render_template(
        "index.html",
        usuario=usuario
    )


@app.route("/productos")
def productos():

    lista_productos = [

        {
            "nombre": "Notebook",
            "precio": 850000,
            "stock": 4
        },

        {
            "nombre": "Mouse",
            "precio": 25000,
            "stock": 10
        },

        {
            "nombre": "Monitor",
            "precio": 300000,
            "stock": 0
        }

    ]

    return render_template(
        "productos.html",
        productos=lista_productos
    )


@app.route(
    "/contacto",
    methods=["GET", "POST"]
)
def contacto():

    mensaje_enviado = False
    nombre = ""

    if request.method == "POST":

        nombre = request.form["nombre"]

        mensaje = request.form["mensaje"]

        print(nombre)
        print(mensaje)

        mensaje_enviado = True


    return render_template(
        "contacto.html",
        mensaje_enviado=mensaje_enviado,
        nombre=nombre
    )


if __name__ == "__main__":

    app.run(debug=True)