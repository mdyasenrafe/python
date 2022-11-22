def sorted_string(s):
    convert_arr = list(s)
    new_str = ''

    for i in range(len(convert_arr)):
        if (i % 2 != 0):
            num = convert_arr[i]
            sing_str = convert_arr[i-1]
            for x in range(int(num)):
                new_str += sing_str
    return ''.join(sorted(new_str, key=str.lower))


val = input('Enter a string: ')
print(sorted_string(val))
