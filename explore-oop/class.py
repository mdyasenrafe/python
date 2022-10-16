class Phone:
    brand = "Apple"
    model = "iPhone 12"
    features = ["Touch ID", "Face ID", "A14 Bionic Chip", "5G"]
    price = 1000

    def call(self, text):
        return f'ring ring {text}'


my_phone = Phone()
print(my_phone.call("rafe"))
