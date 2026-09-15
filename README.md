# Calculadora de Huella de Carbono

Proyecto de grado sobre cambio climático: una calculadora web que estima las emisiones de CO2 generadas por el consumo de electricidad y agua en el hogar, junto con consejos para reducirlas.

## Tecnologías

- Python 3
- Flask
- HTML / CSS
- Jinja2 (motor de plantillas de Flask)

## Instalación

1. Clona el repositorio:
```
git clone https://github.com/juansebastiam984-glitch/cambio-climatico
```

2. Entra a la carpeta del proyecto:
```
cd cambio-climatico
```

3. Crea un entorno virtual:
```
python -m venv venv
```

4. Actívalo:

En Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```

En Mac/Linux:
```
source venv/bin/activate
```

5. Instala las dependencias:
```
pip install -r requirements.txt
```

## Uso

Con el entorno virtual activado, corre:
```
python app.py
```

Luego abre tu navegador en:
```
http://127.0.0.1:5000
```

## Estructura del proyecto

```
cambio-climatico/
├── app.py                  # Rutas de Flask
├── calculos.py               # Lógica de cálculo de emisiones y consejos
├── requirements.txt
├── templates/
│   ├── home.html             # Página de inicio
│   ├── index.html            # Formulario de la calculadora
│   └── consejos.html          # Consejos para reducir emisiones
└── static/
    ├── css/
    │   └── style.css
    └── img/
        └── 1.png
```

## Factores de emisión usados

- Electricidad: 0.19 kg CO2/kWh (Ecuador, CENACE/ARCONEL)
- Agua: 0.28 kg CO2/m³ (referencia EMASESA, ciclo integral del agua)

## Autor

Heo_787
