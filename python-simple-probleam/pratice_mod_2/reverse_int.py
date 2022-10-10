x = int(input("Enter a number: "))
reverse = 0
remainder = 0
if(x < 0) :
    x = x * -1

while x != 0 :
    remainder = x % 10
    reverse = reverse * 10 + remainder
    x //= 10
print(reverse)



