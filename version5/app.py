import datetime
import json
from reader.base import DataReader
from plotting.base import DataPlotting
import importlib


class App:

    def __init__(self, data_source:DataReader, plot:DataPlotting):
        self.data_source = data_source
        self.plot = plot

    @classmethod
    def configure(cls, filename):
        with open(filename) as file:
            config = json.load(file)
            
            
        data_source = importlib.import_module(f"reader.{config['data_source']['name']}").DataSource()
        plot = importlib.import_module(f"plotting.{config['plot']['name']}").Plot()
        return cls(data_source, plot)


    def read(self, **kwargs):
        return self.data_source.read(**kwargs)

    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []

        for date, temperature in temperatures_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temperature)

        self.plot.draw(dates, temperatures)

if __name__ == '__main__':
    # import sys
    # from urban_climate_csv import DataSource
    # file_name = sys.argv[1]
    # app = App(DataSource())
    # temperatures_by_hour = app.read(file_name=file_name)
    # app.draw(temperatures_by_hour)


    # import sys
    # from open_weather_json import DataSource
    # file_name = sys.argv[1]
    # app = App(DataSource())
    # temperatures_by_hour = app.read(file_name=file_name)
    # app.draw(temperatures_by_hour)


    # import sys
    # from open_weather_json import DataSource
    # from plotly_plot import Plot
    # file_name = sys.argv[1]
    # app = App(DataSource(), Plot())
    # temperatures_by_hour = app.read(file_name=file_name)
    # app.draw(temperatures_by_hour)


    import sys
    config_file = sys.argv[1]
    file_name = sys.argv[2]
    app = App.configure(config_file)
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)