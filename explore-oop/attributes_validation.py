class Item:
    def __init__(self, name, price):
        assert price > 0, f"Price {price} is not greater than zero"
        assert len(name) > 2, f"Name {name} is not greater than two characters"
        self.name = name
        self.price = price


Item = Item("Ph", 100)

print(Item.price)
