# # def sum(x): return x * 2


# # arr_num = [1, 2, 3, 4, 5]


# # def print_name(x, y):
# #     print(x, y)


# # result = map(lambda x: x * 2, arr_num)

# # print(list(result))
# names = [
#     {"name": "md yasnen", "roll": 7},
#     {"naem": "hassan", "roll": 8},
#     {"name": "ali", "roll": 1},
# ]

# filter_item = filter(lambda x:  x["roll"] < 2, names)
# print(list(filter_item))

list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]
new_list = []

for x in range(len(list1)):
    new_str = list1[x] + list2[x]
    new_list.append(new_str)

# print(new_list)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = zip(keys, values)

print(dict(tuple(result)))
