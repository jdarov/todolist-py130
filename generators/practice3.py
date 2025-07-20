string_list = ["hello", "world", "yes"]

capital_len5 = (string.capitalize() if len(string) >= 5 else string for string in string_list)

print(set(capital_len5))

def capitalize_len5(string_list):

    yield from (string.capitalize() if len(string) >= 5 else string for string in string_list)

print(set(capitalize_len5(string_list)))

