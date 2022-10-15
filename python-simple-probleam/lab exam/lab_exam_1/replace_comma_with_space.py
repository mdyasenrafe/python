def replace_comma_with_space(text):
    text_arr = text.split(',')
    return ' '.join(text_arr)


s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
