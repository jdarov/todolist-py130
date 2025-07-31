#Q1 

def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))
print(times5(10))

"""
30
50

yes closure means having access to the variable from the outer scope even after 
the function has closed or finished 

Does this mean x is still available always or n?
"""

#Q2

def counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())

"""
Here there are no value being passed as arguments, so there are not outside variables being saved to memory
for the inside function to access

How do you know when to use nonlocal
"""

#Q3

def make_greeter(name):
    def greet(greeter):
        return f'{greeter}, {name}'
    return greet

#
def minus(x, y):
        return x - y
        
def make_subtractor(y):
        def subtract_from(x):
                return minus(x, y)
                
        return subtract_from
        
sub10 = make_subtractor(10)
sub50 = make_subtractor(50)

print(sub50(25)) # -25
# when we call sub50, it "remembers" that y = 50
print(sub10(100)) # 90
# when we call sub10, it "remembers" that y = 10

#Can you use PFA to always send an email from 'Alice"
from functools import partial

def format_message(name):
    def from_alice(recipient, message):

        return f"From: {name} To: {recipient} — {message}"
    return from_alice

from_alice = format_message('Alice')


print(from_alice('Bob', 'Hi!'))
print(from_alice('Josh', 'Bye!'))

