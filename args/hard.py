
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

print(skip_substrings('') == [])
