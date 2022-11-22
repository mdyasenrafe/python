def sum(a, b, c):
    return a + b + c


a, b, c = map(float, input("enter numbers: ").split("-"))
result = sum(a, b, c)
print("result is:", result)
