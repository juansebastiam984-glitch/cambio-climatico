FACTOR_ELECTRICIDAD = 0.19 

def calcular_electricidad(kwh: float) -> float:
    """Emisiones por consumo eléctrico mensual (kWh)."""
    kwh = max(kwh, 0)
    return round(kwh * FACTOR_ELECTRICIDAD, 2)
