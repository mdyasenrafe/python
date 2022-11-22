class Calculator:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        return self.X + self.n

    def pow(self):
        return self.X ** self.n


X, n = map(int, input("enter numbers: ").split())

calc = Calculator(X, n)

print("sum is:", calc.sum())

print("power is:", calc.pow())
