import sqlite3
import json

from flask import Flask, request, g, jsonify

from repo import Repo
from ml_model import predict


def get_db_connection():
    conn = sqlite3.connect('db')
    return conn

def predict_traffic():
    print(request.data)
    data = json.loads(request.data)
    date, time = data['datetime'].split()
    precipitation = float(data['precipitationMm'])
    time = time.removesuffix(':00')

    traffic = {}

    repo = g.repo
    stations = repo.get_stations()
    holiday_name = repo.get_holiday(date)
    for station in stations:
        traffic[station] = predict(date, time, precipitation, holiday_name)

    return jsonify({"stations": traffic}), 200


def create_app():
    app = Flask(__name__)

    @app.before_request
    def add_repo():
        conn = get_db_connection()
        g.repo = Repo(conn)

    app.add_url_rule('/predict', view_func=predict_traffic, methods=['POST'])
    return app

def main():
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()
