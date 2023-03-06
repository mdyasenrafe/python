class Device:
    def __init__(self, band, price, color):
        self.band = band
        self.price = price
        self.color = color

    def start(self):
        print('Starting device')


class Laptop(Device):
    def __init__(self, band, price, color, disk_size):
        super().__init__(band, price, color)
        self.disk_size = disk_size

    def __repr__(self):
        return f'Laptop({self.band}, {self.price}, {self.color}, {self.disk_size})'

    def run(self):
        print('Laptop is running')

    def purchase(self, money):
        if money >= self.price:
            print('You can buy this laptop')
            return money - self.price

        else:
            print('You can not buy this laptop')


class Phone(Device):
    def __init__(self, band, price, color, spec, sim_number):
        super().__init__(band, price, color)
        self.spec = spec
        self.sim_number = sim_number

    def __repr__(self):
        return f'Phone ({self.band}, {self.price}, {self.color}, {self.spec}, {self.sim_number})'

    def is_dual_sim(self):
        if self.sim_number == 2:
            print('This phone is dual sim')
        else:
            print('This phone is single sim')


class Watch(Device):
    def __init__(self, band, price, color, watch_type):
        super().__init__(band, price, color)
        self.watch_type = watch_type

    def is_digital(self):
        if self.watch_type == 'digital':
            return True
        else:
            return False


oppo = Phone('Oppo', 1000, 'black', '4G', 2)
macbook = Laptop('Macbook', 2000, 'silver', 500)
apple_watch = Watch('Apple', 500, 'black', 'digital')
oppo.start()
print(macbook)
print(apple_watch)
