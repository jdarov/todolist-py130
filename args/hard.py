"""
Create a function that takes a string and returns every substring of that string, 
with each consecutive substring skipping evey other character
Return the list sorted by word length. If multiple words have the same length, leave the two elements in the same order
"""
def all_substrings(string):
    substrings = list()
    for x in range(len(string)):
        new_string = ''
        for y in range(x, len(string), 2):
            new_string += string[y]
            substrings.append(new_string)
    return substrings

def skip_substrings(string):
    return sorted(all_substrings(string), key=len)

print(skip_substrings('abcdef') == [
 'a', 'b', 'c', 'd', 'e', 'f',
 'ac', 'bd', 'ce', 'df',
 'ace', 'bdf'
]
)

print(skip_substrings('xyz') == [
 'x', 'y', 'z',
 'xz',
]
)

print(skip_substrings('xxx') == ['x', 'x', 'x', 'xx'])

print(skip_substrings('') == [])

def what_is_different(number_list):
    return [number for number in number_list if number_list.count(number) == 1][0]

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)