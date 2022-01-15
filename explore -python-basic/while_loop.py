# normal while loop

ages =[12 ,15,13,14]
i = 0
while i < len(ages):
    age = ages[i]
    print(age)
    i += 1
    
# contine
numbers = [ 11,12,13,14,15,54,57]
while i < len(numbers):
    number =numbers[i]
    i += 1
    if number == 13:
        continue
    print(i , number)

 # break
while i < len(numbers):
    number =numbers[i]
    i += 1
    if number == 13:
         break
    print(i , number)
