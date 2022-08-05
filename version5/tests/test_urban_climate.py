
import datetime
from reader.urban_climate_csv import DataSource


def test_read():
    reader = DataSource()
    for key, value in reader.read(file_name='./data/london.csv').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value