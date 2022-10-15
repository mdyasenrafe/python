replace_with = ["chief", "thief", "superintendent",
                "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


def replace_word(s, replace_with):
    spilt_arr = s.lower().split(" ")
    final_output = ''
    for x in spilt_arr:
        if x in replace_with:
            index = replace_with.index(x)
            final_output += replace_with[index + 1] + " "
        else:
            final_output += x + " "
    return final_output


output = replace_word(s, replace_with)
print(output)
