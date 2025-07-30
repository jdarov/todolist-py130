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
        nonlocal count
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
