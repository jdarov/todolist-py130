import unittest
#Q1

def subtract(a, b): return a - b

class TestMath(unittest.TestCase):
    def test_subtract(self):
        # Setup and Exercise
        result = subtract(10, 4)
        # Assert
        self.assertEqual(result, 6)
    #No teardown

#Q2

def greet(name):
    return f"Hello, {name}!"

class TestGreet(unittest.TestCase):
    def test_greet(self):
        # Setup
        name = "Josh"

        # Exercise
        greet_josh = greet(name)

        # Assert
        self.assertEqual(greet_josh, "Hello, Josh")

#Q3

def is_even(n):
    return n % 2 == 0

class TestEven(unittest.TestCase):
    def test_is_even(self):
        # Setup
        even_number, odd_number = 4, 5
        # Exercise
        check_even = is_even(even_number)
        check_odd = is_even(odd_number)
        # Assert
        self.assertTrue(check_even)
        self.assertFalse(check_odd)

if __name__ == '__main__':
    unittest.main()

"""
Wrtie a function named log_function_call that takes a function as an argument.
when decorated function is called, the decorator should print the name of the function
its positional and keyword arguments and its return value

the decorate function should still execute as normal

AVOID DRY
"""
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} was called with args {args} and kwargs {kwargs}')
        print(f"'{func.__name__}()' returned {func(*args)}")
        return func(*args)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3,5)
print(f"Final result: {result}")

#Expected output:
"""
Calling function 'add()' with args (3,5) and kwargs ()
'add' returned 8
Final result: 8
"""
class CheckEven:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.nums = (a, b)

    def is_even(self):
        return (self.a % 2 == 0 and self.b % 2 == 0)
    
    def add(self):
        return self.a + self.b
    
"""
create a unit test using SEAT that :
    creates a setup for one with only even numbers and only odd numbers
    uses this setup to test both methods in the class with different asserts
    checks if a and b are actually in nums using an assert

Don't forget the import, inheritance and main() needed for unittest!impo
"""
