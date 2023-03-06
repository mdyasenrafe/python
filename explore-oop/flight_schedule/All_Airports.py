import csv
from Airport import Airport
from math import radians, sin, cos, acos, sqrt, atan2, atan


class AllAirports:
    def __init__(self):
        self.airports = None
        self.load_airport_data("./data/airport.csv")
        self.distance = None

    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        with open("./data/currencyrates.csv", 'r', encoding='utf-8') as file:
            lines = csv.reader(file)

            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()

        with open("./data/countrycurrency.csv", 'r', encoding='utf-8') as file:
            lines = csv.reader(file)
            # skip header
            header = next(lines)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = csv.reader(file)

            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(
                        line[4], line[1], line[2], line[3], line[6], line[7], rate)
            except KeyError as e:
                # print(e)
                pass

        file.close()
        self.airports = airports

        for airport in airports.items():
            # print(airport)
            # print(airport)
            pass

    def get_distance_beetween_two_airports(self, lat1, lon1, lat2, lon2):
        radius = 6371
        lat_diff = radians(lat1 - lat2)
        lon_diff = radians(lon1 - lon2)
        a = sin(lat_diff / 2) * sin(lat_diff / 2) + cos(radians(lat1)) * \
            cos(radians(lat2)) * sin(lon_diff / 2) * sin(lon_diff / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = radius * c
        self.distance = d
        return d

    def distance_between_two_airports(self, airport1_code, airport2_code):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_beetween_two_airports(
            airport1.lat, airport1.lon, airport2.lat, airport2.lon)
        return distance

    def ticket_price(self, start, end):
        distance = self.distance_between_two_airports(start, end)
        airport1 = self.airports[start]
        fare = distance * float(airport1.rate)
        return fare


test = AllAirports()
fare = test.ticket_price('DAC', 'PRA')
