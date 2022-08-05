import datetime

from reader.open_weather_json import DataSource


def test_read():
    reader = DataSource()
    for key, value in reader.read(file_name='./data/moscow.json').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value