#!/usr/bin/env python3

from flask import Flask, jsonify, request
from fundamentus import get_data
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# First update
lista, hora = dict(get_data()), datetime.now().hour


@app.route("/")
def json_api():
    global lista, hora
    setor = request.args.get('setor')

    # Then only update once a day
    if not setor and hora < datetime.now().hour:
        lista, dia = dict(get_data()), datetime.now().hour
    else:
        lista, dia = dict(get_data(setor=setor)), datetime.now().hour
    return jsonify(lista)


@app.route('/cotacao')
def cotacao():
    global lista, hora
    ticker = request.args.get('ticker')

    if hora < datetime.now().hour:
        lista, dia = dict(get_data()), datetime.now().hour

    if ticker == None or ticker not in lista:
        return '0.0'
    else:
        ticker = ticker.upper()
        return lista[ticker]['cotacao'].replace(',', '.')


if __name__ == '__main__':
    app.run()
