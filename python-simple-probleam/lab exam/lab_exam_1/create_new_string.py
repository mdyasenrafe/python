a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


def create_new_string(x, y):
    output = ''
    remove_comma = y.replace(',', '')
    split_y = remove_comma.lower().split(" ")
    x_lower = [b.lower() for b in x]
    for i in split_y:
        if i in x_lower:
            if (i != 'to'):
                output += split_y[split_y.index(i) + 1] + " "

    output = output + "Bangladesh"
    with open("out.txt", 'w') as txt:
        txt.write(output)
    return output


print(create_new_string(a, s))
