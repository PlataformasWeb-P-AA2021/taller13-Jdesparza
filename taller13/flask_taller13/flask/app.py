from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>ADMINISTRACIÓN DE EDIFICIOS</p> \
    <a href='http://127.0.0.1:5000/losedificios'>Edificios</a> \
    - <a href='http://127.0.0.1:5000/losdepartamentos'>Departamentos</a>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/",
            auth=('jordy', '123456789'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('jordy', '123456789'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({
            'nombPropietario':d['nombPropietario'], 
            'costoDept':d['costoDept'],
            'cuartos':d['cuartos'],
            'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero=numero)


# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('jordy', '123456789'))
    edificio = json.loads(r.content)['nombre']
    return edificio

app.run()