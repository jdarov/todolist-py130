practice_list = [1, 2, "hello", None]

new_list = list(filter(lambda element: element is not None, practice_list))

print(new_list)
