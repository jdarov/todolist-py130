string = 'hello'

reverse_string = (string[i] for i in range(len(string)-1, -1, -1))

for char in reverse_string:
    print(char)

    