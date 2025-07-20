"""
C  input: 
        callback function with 2 arguments (current element of iterable, current accum value)
        iterable
        first accum value
    output:
        single value from iterable

    explicit:
        take the arguments and return a SINGLE value of the arguments combined
        combination should be determine by the callback function
        the first accum value will ALWAYS be the first argument passed to accum in the callback
    implicit:
        the third arg accum is simply the first addition to the function

O
    numbers = (1, 2, 4, 8, 16)
    total = lambda number, accum: accum + number
    print(reduce(total, numbers, 0))        # 31

    numbers = [10, 3, 5]
    product = lambda number, accum: accum * number
    print(reduce(product, numbers, 2))      # 300

    colors = ['red', 'orange', 'yellow', 'green',
            'blue', 'indigo', 'violet']
    rainbow = lambda color, accum: accum + color[0].upper()
    print(reduce(rainbow, colors, ''))      # ROYGBIV

D
    lists, ints, strings

    functions:
        
    main:
        how can i differentiate between a list of ints and strings?
        set an initial variable accum to the third argument
        for each element in the iterable
            accum = implement callback function with the element and accum

        return the final accum value
E
"""

def reduce(callback, iterable, accum):
    return [accum := callback(element, accum) for element in iterable][-1]


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
        'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV
