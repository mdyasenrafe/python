numbers = [14,15,12,36,48,75,6,3]
def average_number(input) :
    x = 0
    result = 0
    for number in numbers:
         x = x + number
    return (x / len(numbers) , len(numbers))
result = average_number(numbers)
print(result)