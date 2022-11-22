def reverse_string(string):
    return (" ".join([word[::-1] for word in string.split(" ")]))


print(reverse_string("Programming Hero is the best"))
