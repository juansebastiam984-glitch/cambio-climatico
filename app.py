from flask import Flask, render_template, request
from calculos import calcular_electricidad, calcular_agua, obtener_consejos_luz, obtener_consejos_agua

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    resultado_luz = None
    resultado_agua = None
    kwh = None
    m3agua = None

    if request.method == "POST":
        kwh = request.form.get("kwh", type=float)
        if kwh is not None:
            resultado_luz = calcular_electricidad(kwh)

        m3agua = request.form.get("m3agua", type=float)
        if m3agua is not None:
            resultado_agua = calcular_agua(m3agua)

    return render_template(
        "index.html",
        resultado_luz=resultado_luz,
        resultado_agua=resultado_agua,
        kwh=kwh,
        m3agua=m3agua,
    )


@app.route("/consejos")
def consejos():
    tips_luz = obtener_consejos_luz(0)
    tips_agua = obtener_consejos_agua(0)
    return render_template("consejos.html", tips_luz=tips_luz, tips_agua=tips_agua)


if __name__ == "__main__":
    app.run(debug=True)