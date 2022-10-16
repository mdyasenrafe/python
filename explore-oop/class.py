class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def increase_price(self, amount):
        self.last_price = self.price
        self.price = self.price + amount


my_phone = Phone("Apple", "iPhone 12", 80000)
my_phone.increase_price(1000)
print(my_phone.__dict__)
