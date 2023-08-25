import pickle
import json
import sklearn

aliases = json.load(open('src/replaces.json'))


def get_alias(alias_name, name):
    return aliases[alias_name].get(name)


def get_line_alias(line):
    return get_alias('line', line)


def get_station_alias(station):
    return get_alias('station', station)


def get_holiday_alias(holiday_name):
    return get_alias('holiday_name', holiday_name)


def get_weekday_alias(day):
    return get_alias('dayofweek', day)


def get_season_alias(season):
    return get_alias('season', season)


def load_model():
    with open('model.pkl', 'rb') as modelf:
        model = pickle.load(modelf)
    return model


def predict(holiday, date, hour, precipitation, station, line, weekday):
    month = int(date.split('-')[1])
    season = ['winter', 'spring', 'summer', 'autumn'][month // 3 % 4]
    is_holiday = bool(holiday)
    holiday = holiday or '-'

    return (
        hour,
        get_line_alias(line),
        get_station_alias(station),
        get_holiday_alias(holiday),
        precipitation,
        get_weekday_alias(weekday),
        is_holiday,
        get_season_alias(season),
    )


def ppredict(holiday, date, hour, precipitation, line, station, weekday):
    month = int(date.split('-')[1])
    season = ['winter', 'spring', 'summer', 'autumn'][month // 3 % 4]
    is_holiday = bool(holiday)
    holiday = holiday or '-'
    model = load_model()
    pred_data = np.array([[hour, get_line_alias(line), get_station_alias(station), get_holiday_alias(holiday), precipitation, get_weekday_alias(weekday), is_holiday,get_season_alias(season)]])
    return float(model.predict(pred_data))
