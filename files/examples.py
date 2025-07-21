file = open('example.txt', 'r')

content = file.read()

file.close()

print(content)

with open('example.txt', 'a') as file:
    file.write("Hello, again\n")


with open('example.txt', 'r') as file:
    for line in file:
        print(repr(line))


