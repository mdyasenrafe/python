# normal loop
names = ["hablu" ,"coltu"]
for name in names :
    print(name)
ages =[14 ,18 ]
# nested loop
for x in names :
    for y in ages : 
        print(y)
# continue
fruits =["apple" ,"bannna" ,"orange" ,"toltu    "]
for fruit in fruits :
    if(fruit ==  "bannna"):
        continue
    print(fruit)
# Break
fruits =["apple" ,"bannna" ,"orange"]
for fruit in fruits :
    if(fruit ==  "orange"):
        break
    print(fruit)

a="Bd"
for i in range(len(a)):
    print(a[i],end="")