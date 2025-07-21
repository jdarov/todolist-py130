
from functools import reduce


number_list = [1,2,3,4]

product = reduce(lambda element, accum: accum*element, number_list, 1)

print(product)