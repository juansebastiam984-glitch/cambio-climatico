from flask import Flask, render_template, request
from calculos import calcular_electricidad

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    kwh = None

    if request.method == "POST":
        kwh = request.form.get("kwh", type=float)
        if kwh is not None:
            resultado = calcular_electricidad(kwh)

    return render_template("index.html", resultado=resultado, kwh=kwh)


if __name__ == "__main__":
    app.run(debug=True)