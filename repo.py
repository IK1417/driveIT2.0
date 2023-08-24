import sqlite3


class Repo:
    def __init__(self, conn):
        self.conn = conn

    def get_holiday(self, date):
        cur = self.conn.cursor()
        records = cur.execute(
            'SELECT holiday_name FROM holidays WHERE date=?', (date,)
        )
        if records:
            return [x[0] for x in records.fetchall()]
        else:
            return []
    def get_stations(self):
        cur = self.conn.cursor()
        cur.execute('SELECT station from stations')
        return [x[0] for x in cur.fetchall()]
