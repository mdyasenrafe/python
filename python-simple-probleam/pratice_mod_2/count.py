n = input("Enter a string: ")
lower =0
upper =0
digit =0
spc =0;
for x in n:
    if(x >= 'a' and x <= 'z') :
        lower += 1
    elif(x >= 'A' and x <= 'Z') :
        upper += 1
    elif(x >= '1' and x <= '9') :
        digit += 1
    else :
        spc +=1

print("Uppercase  = ", upper)
print("Lowercase = ", lower)
print("Digits  = ", digit)
print("Symbol = ", spc)

