class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} costs {self.price}"


item1 = Item("Phone", 100)
item2 = Item("Laptop", 1000)

item1.discount = 0.9

print(item1.__dict__)
