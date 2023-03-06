class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("animal parent sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("bark bark bark")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("meow meow meow")


class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("neigh neigh neigh")


Tom = Dog("Tom")
Jerry = Cat("Jerry")
Manik = Horse("Manik")

# Tom.make_sound()
# Jerry.make_sound()
# Manik.make_sound()

animals = [Tom, Jerry, Manik]

for animal in animals:
    animal.make_sound()
