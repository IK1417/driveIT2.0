import json
import sqlite3

from flask import Flask, g, jsonify, request

from ml_model import predict
from repo import Repo
import datetime
import locale
import calendar

def get_db_connection():
    conn = sqlite3.connect('src/db')
    return conn

def get_weekday(date):
    cur_locale = locale.getlocale()
    locale.setlocale(locale.LC_ALL, '')
    date = datetime.date.fromisoformat(date)
    return date.strftime('%A').title()
    

def predict_traffic():
    data = json.loads(request.data)
    date, time = data['datetime'].split()
    precipitation = float(data['precipitationMm'])
    time = time.removesuffix(':00')

    traffic = {}

    repo = g.repo
    stations = repo.get_stations_with_line()
    holiday_name = repo.get_holiday(date)
    day = get_weekday(date)

    for (station, line) in stations:
        traffic[station] = predict(holiday_name, date, time, precipitation,
                line, station, day)


    return jsonify({'stations': traffic}), 200


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
