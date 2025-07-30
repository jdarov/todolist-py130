#Q1

names = ["Josh", "Amy", "Zed", "Timothy"]

result = list(map(lambda name: name.upper(), filter(lambda name: len(name) <= 4, names)))

print(result)

"""
[JOSH, AMY, ZED]

1. first filter is called, which returns a gen expression based on the first param callback
In this case, any name with str len <= 4 will be return in a lazy gen expression
Then map is called with it's callback, which runs the callback in first param through the iterable,
In this case, upper() on all names in iterable
Then, since this is a lazy expression, we need to wrap it all in a list() in order to view it

Lambda is like an anonymous function. Here we define it by creating our callbacks using it so we don't have
to create whole entire functions, They have plenty of advantages, but also disadvantages including:
    expression is limited to single expression
    no assignments, loops, if or other statements allowed
    docstrings not allowed
    difficult to debug
    dont take *args and *kwargs params
"""

#Q2

nums = [1, 2, 3, 4, 5]

evens = list(filter(lambda x: x % 2 == 0, nums))
squares = map(lambda x: x ** 2, evens)

print(next(squares))
print(evens[0])

"""
output: 4, 4
1. it prints two values but since next() consumes one gen expression in evens, it will print the next number 
in its generator which in this case is 4

"""

#Q3

def double_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num * 2)
    return result
nums = [1,2,3,4,5]
print(list(map(lambda x: x * 2, filter(lambda num: num % 2 ==0, nums))))
"""
A lazy expression like this takes up less space and goes faster than holding the elements in a list 
in memory and keeping that memory being used for the list
"""