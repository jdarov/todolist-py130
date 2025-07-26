import re

# `pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

# user_input = input("Please enter an emal: ")

# if(re.search(pattern, user_input)):
#     print("Valid Input")
# else:
#     print("Invalid Input")`

text = r"""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789

Ha HaHa

coreyms.com

MetaCharacters (Need to be escaped):
. ^ $ * * ? { } [ ] \ | ( )

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr.
"""

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'\D')
matches = pattern.finditer(text)
for match in matches:
    print(match)