class Dog:
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"


class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"


bobo = JackRussellTerrier()
print(bobo.speak())

# inheritance type
# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarchical inheritance
# 5. hybrid inheritance
