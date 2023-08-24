import pickle

def load_model():
    with open('model.pkl', 'rb') as modelf:
        model = pickle.load(modelf)
    return model

def predict(holiday, date, hour, precipitation, station, line, weekday):
    month = int(date.split('-')[1])
    season = ["winter", 'spring', 'summer', 'autumn'][month//3%4]
    is_holiday = bool(holiday)
    holiday = holiday or '-'
    
    return (hour, line, station, holiday, precipitation, weekday, is_holiday, season)


# удалите функцию выше и переименуйте эту как только будет готова моделька
def ppredict(holiday, date, hour, precipitation, line, station, weekday):
    month = int(date.split('-')[1])
    season = ["winter", 'spring', 'summer', 'autumn'][month//3%4]
    is_holiday = bool(holiday)
    holiday = holiday or '-'
    
    return model.predict(hour, line, station, holiday, precipitation,
            weekday,
            is_holiday, season)

# уберите хештег как только моделька будет готова
# model = load_model()
