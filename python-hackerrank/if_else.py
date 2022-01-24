"""
If n  is odd, print Weird
If  n is even and in the inclusive range of 2  to 5 , print Not Weird
If  n is even and in the inclusive range of 6 to 20 , print Weird
If  n is even and greater than 20 , print Not Weird
"""
def if_else(n) : 
    if(n % 2) :
        print("Weird") 
    elif(n%2==0 and n>=2 and n <= 5) :
        print("Not Weird")
    elif(n%2==0 and n>=6 and n <= 20) :
        print("Weird")
    else :
        print("Not Weird")
number = 24
if_else(number)