def reduce(callback, iterable, accum):
    return [accum := callback(element, accum) for element in iterable][-1]

numbers = [1,2,3,4,5]

sum_squared = reduce(lambda number, accum: accum + number**2, numbers, 0)

print(sum_squared)