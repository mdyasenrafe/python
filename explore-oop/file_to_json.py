import json


class Item:
    all_items = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.all_items.append(self)

    def __repr__(self):
        return f"{self.name} costs {self.price}"

    @staticmethod
    def from_json():
        with open("json.txt", 'r') as f:
            data = f.read()
            json_content = json.loads(data)
            for item in json_content:
                Item(item["name"], item["price"])


Item.from_json()
print(Item.all_items)
