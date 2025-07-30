from itertools import islice

#Q1

nums = [10, 20, 30]
gen = (n * 2 for n in nums)

nums.append(40)

print(next(gen))
print(next(gen))
nums.append(50)
print(list(gen))

"""
1. gen is a generator expression that stores only the generator of n * 2 for each n in an iterable
these are not stored in a seperate list but rather a generator expression that only uses the info when asked
for it. This saves space and time

2. Yes, since the generator is not storing any data but rather generating it as needed, the list can change after
expression has been called and it will still be able to access those values later

3. Once you use next(), it is using up that generator expression in memory, resulting in that generator no longer
being accessible. That is why this line will print [60, 80, 100] as that is the remaining generators left in the 
expression ([30, 40, 50])
"""

#Q2

def custom_range(start, stop):
    def generator():
        return (start + i for i in range(stop - start))
    return generator()

r = custom_range(3, 5)

print(sum(r))
print(sum(r))  # Attempt to reuse

"""
1. No, you can not reuse this as once a generator expression is called it uses up the data and doesn't store
anything in memory like an iterable, which saves time and space 
"""

#Q3

squares = islice((x**2 for x in range(10) if x % 2 == 0), 0, 3)

"""
Generators do not use as much space and take up much less time as you aren't storing any unneccessary 
data in an array on memory
"""