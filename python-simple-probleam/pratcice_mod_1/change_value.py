numbers =[]
for num in range(3) :
    numbers.append(int(input("Enter number: ")))

for i in range(len(numbers)) :
    if(numbers[i] < 0) :
        numbers[i] = numbers[i] * -1
    else :
        numbers[i] = numbers[i]

print(numbers) 