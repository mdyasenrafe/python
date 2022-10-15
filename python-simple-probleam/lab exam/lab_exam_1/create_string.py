l = ["This", "is", "very", "fantastic"]


def create_string(l):
    output = ''
    for x in l:
        output += x + " "
    return output


print(create_string(l))
