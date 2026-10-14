
from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con el formulario
@app.route("/")
def inicio():
    return render_template("index.html")


# Recibir los datos del formulario
@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.form.get("nombre", "").strip()

    if not nombre:
        return render_template(
            "index.html",
            error="Por favor, ingresá tu nombre."
        )

    return render_template("saludo.html", nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True)
