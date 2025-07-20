string_list = ["hello", "world"]

capitals = (string.capitalize() for string in string_list)

print(tuple(capitals))

def capitalize_strings(string_list):
    for string in string_list:
        yield string.capitalize()

print(tuple(capitalize_strings(string_list)))

