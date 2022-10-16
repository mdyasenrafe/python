class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item': item, 'price': price, 'quantity': quantity})

    def checkout(self, amount):
        price = 0
        for item in self.cart:
            price += item['price'] * item['quantity']
        if amount < price:
            return "Not enough money"
        elif amount > price:
            return "Here is your change: {}".format(amount - price)
        else:
            return "Thank you for shopping with us"

    def get_cart(self):
        return self.cart


my_shop = Shopper("John")
my_shop.add_to_cart("Apple", 100, 2)
my_shop.add_to_cart("Mango", 50, 3)
print(my_shop.checkout(350))
