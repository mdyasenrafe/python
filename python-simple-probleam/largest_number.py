numbers =[14 ,25,36,69,47,74,85 , 45 ]
def largest_number(input) : 
    x = 0
    for number in input : 
        if(number > x) :
             x = number
    return x
result = largest_number(numbers)
print(result)
# shortcut way
shortcutResult =  max(numbers)
print(shortcutResult)