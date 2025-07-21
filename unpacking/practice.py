a, b, c = (1, 2, 3)
print(a, b, c) #1 2 3

a, _, c = (1, 2, 3) #2

# a, b = (1, 2, 3)
#yes, valueerror because only assigned 2 vars in a 3 var tuple

# a, b, c, d, e = (1, 2, 3)
#valueError because unpacking too many vars

a, *rest = [1, 2, 3, 4, 5] #2, 3, 4, 5

first, *middle, last = "hello"
print(f"First: {first}, Middle: {middle}, Last: {last}")
#First: h, Middle: [ell], Last: o

a = 1
b = 2

b, a = a, b

(x,y,z) = ((1,2),3)