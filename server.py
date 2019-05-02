#!/usr/bin/env python3

from flask import Flask, jsonify, request
from fundamentus import get_data
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')


@app.route("/")
def json_api():
    global lista, dia
    setor = request.args.get('setor')

    # Then only update once a day
    if not setor:
        if dia == datetime.strftime(datetime.today(), '%d'):
            return jsonify(lista)
        else:
            lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
            return jsonify(lista)
    else:
        lista, dia = dict(get_data(setor=setor)), datetime.strftime(datetime.today(), '%d')
        return jsonify(lista)


if __name__ == '__main__':
    app.run()
