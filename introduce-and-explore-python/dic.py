marks = {"english": 24, "bangla": 207}
marks["math"] = 100
# del marks["english"]
# get value of a key
marks_key = marks.keys()
marks_value = marks.values()
marks_pair = marks.items()
print(marks_pair)

for key in marks:
    print(key, marks[key])
