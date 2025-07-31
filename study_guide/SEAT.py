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