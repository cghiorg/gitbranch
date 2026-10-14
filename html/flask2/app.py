from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("index.html")


@app.route("/procesar", methods=["POST"])
def procesar():

    nombre = request.form["nombre"]

    edad = int(request.form["edad"])

    if edad >= 18:

        estado = "mayor de edad"

    else:

        estado = "menor de edad"
        
    

    return render_template(
        "resultado.html",
        nombre=nombre,
        edad=edad,
        estado=estado
    )


if __name__ == "__main__":
    app.run(debug=True)