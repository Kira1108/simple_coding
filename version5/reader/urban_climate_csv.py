import csv
import datetime


class DataSource:

    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(kwargs['file_name'], 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                hour = datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour