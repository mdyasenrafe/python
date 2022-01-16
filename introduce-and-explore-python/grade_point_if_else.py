# 80 -100 = A+
# 70-79 =A
# 60 - 69 =A-
# 50 - 59 =	B
# 40 - 49 =	C
# 33 - 39 =	D
number = 70

if(number >= 80 and number <= 100) :
    print("A+")
elif (number >= 70 and number <= 79) :
    print("A")
elif (number >= 60 and number <= 69) :
    print("A-")
elif (number >= 50 and number <= 59) :
    print("B")
elif (number >= 40 and number <= 59) :
    print("C")
elif (number >= 33 and number <= 39) :
    print("D")
else : 
    print("Fail")