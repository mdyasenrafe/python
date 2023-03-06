class Aircraft:
    def __init__(self, make, code, typ, flight_range):
        self.make = make
        self.code = code
        self.type = typ
        self.flight_range = float(flight_range)

    def get_make(self):
        return self.make

    # def __repr__(self):
    #     return f'Aircraft make is {self.make}, code is {self.code}, type is {self.type}, flight range is {self.flight_range}'
