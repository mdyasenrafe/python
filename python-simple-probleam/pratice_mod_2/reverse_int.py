x = int(input("Enter a number: "))
reverse = 0
remainder = 0
check = False
if (x < 0):
    x = x * -1
    check = True

while x != 0:
    remainder = x % 10
    reverse = reverse * 10 + remainder
    x //= 10

if (check):
    reverse = reverse * -1
else:
    reverse = reverse
if res > 2**31+1 or res < -2**31-1:
    print(0)

print(reverse)
