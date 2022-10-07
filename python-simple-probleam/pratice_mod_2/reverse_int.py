n = int(input("Enter a number: "))
reverse = 0
remainder = 0
while n != 0 :
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n //= 10
print(reverse)

