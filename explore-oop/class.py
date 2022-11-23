class Laptop:
    def __init__(self, band, price, color, spec):
        self.band = band
        self.price = price
        self.color = color
        self.spec = spec

    def run(self):
        print('Laptop is running')

    def purchase(self, money):
        if money >= self.price:
            print('You can buy this laptop')
            return money - self.price

        else:
            print('You can not buy this laptop')


class Phone:
    def __init__(self, band, price, color, spec, sim_number):
        self.band = band
        self.price = price
        self.color = color
        self.spec = spec
        self.sim_number = sim_number

    def is_dual_sim(self):
        if self.sim_number == 2:
            print('This phone is dual sim')
        else:
            print('This phone is single sim')


class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital(self):
        if self.watch_type == 'digital':
            return True
        else:
            return False
