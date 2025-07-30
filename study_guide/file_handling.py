#Q1

with open("data.txt", "r") as f:
    f.readline()
    # f.write("Omega")
"""
first it will read the first line in the data, so "Alpha"
Then it will throw an error since it is in WRITE ONLY mode
This will NOT print anything

No the file won't be changed because it is simply just in read mode
"""

#Q2 

with open("log.txt", "a") as file:
    file.write("Started\n")

with open("log.txt", "r") as file:
    print(file.read())

"""
output: "boot\nStarted"

This is the output because we open the file in append mode, then write() to file which will append
any data to the end of the file instead of overwriting the entire file

Then in the second line we open it in read mode, and .read() reads the entire file, the prints it to scree

What happens if we input other data except a string, like nums or floats or bool values?
"""

#Q3

file = open("example.txt", "w")
file.write("Hello world!\n")
file.close()

file = open("example.txt", "r")
print(file.read())
file.close()

with open('example.txt', 'w') as file:
    file.write("Hello World!\n")
with open("example.txt", 'r') as file:
    print(file.read())

"""
This is better because like in C, opening a file means you are use that computers memory and keeping the file
open can cause bad things to happen, so we need to make sure to always manually close a file that has 
been opened. In this case, python will do the work for us if we simply put the open in a with statement.
"""