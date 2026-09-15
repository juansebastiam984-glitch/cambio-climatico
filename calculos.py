FACTOR_ELECTRICIDAD = 0.19 #co2/kWh
FACTOR_AGUA = 0.23


def calcular_electricidad(kwh: float) -> float:
    """Emisiones por consumo eléctrico mensual (kWh)."""
    kwh = max(kwh, 0)
    return round(kwh * FACTOR_ELECTRICIDAD, 2)


def calcular_agua(metros_cubicos: float) -> float:
    """Emisiones por consumo mensual de agua (m3)."""
    metros_cubicos = max(metros_cubicos, 0)
    return round(metros_cubicos * FACTOR_AGUA, 2)

def obtener_consejos_luz(kwh: float) -> list:
    """Devuelve una lista de consejos para reducir el consumo eléctrico."""
    consejos = [
        "Cambia los focos incandescentes por focos LED (usan hasta 80% menos energía).",
        "Desconecta cargadores y aparatos que no estés usando; en standby siguen consumiendo.",
        "Aprovecha la luz natural durante el día en vez de encender luces.",
    ]
    if kwh > 200:
        consejos.append("Tu consumo es alto: revisa si tienes electrodomésticos viejos (refrigeradora, A/C) que gastan más de lo normal.")
    return consejos


def obtener_consejos_agua(m3: float) -> list:
    """Devuelve una lista de consejos para reducir el consumo de agua."""
    consejos = [
        "Cierra la llave mientras te enjabonas o cepillas los dientes.",
        "Revisa si tienes fugas en tuberías o el tanque del baño; una gotera puede desperdiciar mucha agua al mes.",
        "Reutiliza el agua de lavar frutas/verduras para regar plantas.",
    ]
    if m3 > 15:
        consejos.append("Tu consumo es alto: considera duchas más cortas y lavar ropa solo con carga completa.")
    return consejos
