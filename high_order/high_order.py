def i_have_such_a_long_and_annoying_name(value):
    print(value)

too_long = i_have_such_a_long_and_annoying_name
too_long('Some text')
too_long(3.141592)
too_long('Some text' == 3.141592)

numbers = [1,2,3,4,5]


transformed_numbers = map(lambda x: numbers, numbers)

print(list(transformed_numbers))

even_numbers = list(filter(lambda x: x%2==0, numbers))

print(even_numbers)

strings = ['cat', 'dog']

upper_strings = list(map(lambda string: string.upper(), strings))

sorted_last_letter = sorted(strings, key=lambda names: names[-1])

print(sorted_last_letter)

def for_each(callback, my_list):

    for item in my_list:
        callback(item)
for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])
# 1
# 4
# 9
# 16
# 25

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)
# Cat
# Dog
# Fish
# Bearded Dragon

nested_lists = [[1, 2], [3, 4], [5, 6, 7]]
for_each(lambda sublist: sublist.pop(), nested_lists)
print(nested_lists)
# [[1], [3], [5, 6]]

