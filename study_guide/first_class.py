#Q1

def double(x):
    return x * 2

twice = double

print(twice(5))

"""
10, this works because functions are first-class, meaning they can be assigned to variables, and 
thos variables point to the area in memory holding that function, allowing us to treat them like the function
"""

#Q2

def greet(): return "Hey"
def farewell(): return "Bye"

actions = [greet, farewell]

for action in actions:
    print(action())

"""
"Hey
Bye

First class functions can be stored in lists/arrays
"""

#Q3

def outer():
    def inner():
        return "I’m inside"
    return inner

new_func = outer()
print(new_func())

"""
I'm inside

This is a higher order function, since you can use functions as params or return values

Are all functions that are use in a function parameter considered callbacks?
"""

#Q4

def square(x): return x * x

def operate_on(x, func):
    return func(x)

print(operate_on(4, square))

"""
16

High order functions can be passed as arguments and returned as return values
here it calls the func in the 2nd arg, and applies the first arg as its parameter, and returns the param 4 * 4


"""

#Q5

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))

"""
15

This is called a closure, where the value of n passed as param in the outer function is saved in memory and 
can be accessed by the inner function

Here add5 sets the outer function n to 5, so any subsequent call to add5 will pass in the value of x and return x + 5
"""

#Q6
"""
A. map() - yes high order b/c uses a func in the arg
B. print() - yes high order b/c can use functions in arg (string.upper())
C. filter() - yes high order can pass funcs in arg
D. sorted() - yes high order, can pass funcs to key

"""