text ="Hello, I am Mohammad Yasen Rafi"
def vowel_count(sentence) :
    count = 0
    vowels =["a" , "e" , "i" , "o" , "u", ]
    for char in sentence :
        if char.lower() in vowels  :
            count = count + 1 
    return count

result = vowel_count(text)
print(result)