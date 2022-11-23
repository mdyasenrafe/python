class Vehicle:
    def __init__(self, name, license_plate, price):
        self.name = name
        self.license_plate = license_plate
        self.price = price

    def start(self):
        print('Vehicle is starting')


class Bus(Vehicle):
    def __init__(self, name, license_plate, price, seat, ticket_price):
        super().__init__(name, license_plate, price)
        self.seat = seat
        self.ticket_price = ticket_price
        self.avialable_seat = seat

    def sell_ticket(self, name, quantity, amount):
        self.avialable_seat -= quantity
        reminder = amount - self.ticket_price * quantity
        if (reminder >= 0):
            return 'You can buy this ticket'


class Ac_Bus(Bus):
    def __init__(self, name, license_plate, price, seat, ticket_price):
        super().__init__(name, license_plate, price, seat, ticket_price)


class Non_Ac_Bus(Bus):
    def __init__(self, name, license_plate, price, seat, ticket_price):
        super().__init__(name, license_plate, price, seat, ticket_price)


Hanif = Ac_Bus('Hanif', 'Dhaka', 1000, 50, 100)

print(Hanif.sell_ticket('Rahim', 2, 200))
