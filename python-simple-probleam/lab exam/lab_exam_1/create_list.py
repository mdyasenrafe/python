def create_list(dictV):
    output = []
    for x, y in dictV.items():
        output.append(x)
        output.append(y)
    return output


d = {'a': 1, 'b':  2, 'c': 3, 'd': 4}
print(create_list(d))
