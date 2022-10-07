data = 'aNnaBodyelseIsHere'
lower_data = data.lower()


output = ''
for res in lower_data:
    if((res == 'a') or( res == 'e') or (res == 'i') or (res == 'o') or (res  =='u')) :
        output += res + " "
    
print(output)