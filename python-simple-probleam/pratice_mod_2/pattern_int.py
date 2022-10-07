number = int(input("Enter a number: "))
for x in range(number):
    result = ''
    for y in range(x +1):
        result = result + str(y +1)
    print(result)
