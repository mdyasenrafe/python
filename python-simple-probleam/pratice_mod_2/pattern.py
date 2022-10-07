number = int(input("Enter a number: "))
for x in range(number):
    result = ''
    for y in range(x +1):
        result = result + "*"
    print(result)
for x in range(number-2, -1,-1):
    result = ''
    for y in range(x +1):
        result = result + "*"
    print(result)
