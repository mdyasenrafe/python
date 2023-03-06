from abc import ABC, abstractmethod


class Animal (ABC):
    @abstractmethod
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def sleep(self):
        print("sleep")


class Dog (Animal):
    def __init__(self):
        self.__name = "dog"

    def eat(self):
        super().eat()

    def bark(self):
        print("bark")

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name


Tommie = Dog()
print(Tommie.name)
# Tommie.set_name = "Tommie"
Tommie.eat()
