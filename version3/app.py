import datetime


class App:

    def __init__(self, data_source, plot):
        self.data_source = data_source
        self.plot = plot

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


    import sys
    from open_weather_json import DataSource
    from plotly_plot import Plot
    file_name = sys.argv[1]
    app = App(DataSource(), Plot())
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)