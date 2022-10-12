my_list = ['@F1', 'Ofd', '!', "Rafe", "@Ad", "ask"]
my_dic = {}

for index, val in enumerate(my_list):
    if val[0] == '@':
        my_dic[val] = my_list[index + 1]

print(my_dic)
