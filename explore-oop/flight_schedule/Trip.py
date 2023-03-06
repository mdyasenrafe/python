class Trip:
    def __init__(self, trip_city, start_date):
        self.trip_city = trip_city
        self.start_date = start_date
        self.aircraft = None
        self.trip_route = None
        self.cost = None

    def __repr__(self):
        return f'Trip to {self.trip_city} on {self.start_date} with {self.aircraft} and route {self.trip_route} will cost {self.cost}'
