def clean_string(text):
    clean_string = ''
    for x in text:
        if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
            clean_string += x

    return clean_string


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)
