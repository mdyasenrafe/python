n1 = input("Enter a first string: ")
n2 = input("Enter a second string: ")

def checkStr(s1 , s2) : 
    new_str =''
    for x in s1:
        for y in s2:
            if(x == y) :
               new_str = new_str + y
                
    
    if(new_str == s1) :
        return True
    else :
        return False

print(checkStr(n1,n2))