from functools import reduce

string_list = ["hello, ", "world"]

strings = reduce(lambda string, accum: string + accum, string_list)
