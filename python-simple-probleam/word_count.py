def word_count(text) :
    count =0 
    for word in text:
        if(word == " "):
            count = count +1 
    # last word for digit
    count = count + 1
    print(count)
text = "Hello Mama!"
word_count(text)

