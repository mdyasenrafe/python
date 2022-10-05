numbers = [15 ,14,15,136]
def remove_duplicate(numbers) :
    unique = []
    for number in numbers:
        if(number not in unique) :
            unique.append(number)
    return unique
#function call 
result =  remove_duplicate(numbers)
print(result)
