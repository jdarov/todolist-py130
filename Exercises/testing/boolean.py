import unittest
class NoExperienceError(Exception):
    def __init__(self):
        super().__init__("You don't have any experience!")
    def __str__(self):
        return f"NoExperienceError: {self.args[0]}"

class Employee:
    def hire(self):
        raise NoExperienceError

class Numeric:
    pass
    
class Test(unittest.TestCase):
    
    def test_boolean(self):
        value = 5
        self.assertTrue(value % 2 != 0, 'value is not odd')
    def test_equality(self):
        value = 'xyz'
        self.assertEqual('xyz', value.lower(), "value must be 'xyz'")
    def test_None(self):
        value = None
        self.assertIsNone(value, 'value must be None')
    def test_included(self):
        lst = ['xyz']
        self.assertIn('xyz', lst)
    def test_not_included(self):
        lst = ['abc']
        self.assertNotIn('xyz', lst)
    def test_exception(self):
        employee = Employee()
        with self.assertRaises(NoExperienceError):
            employee.hire()
    def test_type(self):
        numeric = Numeric()
        self.assertIsInstance(numeric, Numeric)
    @unittest.skip
    def same_object(self):
        self.assertIs(lst, lst.process)
    
    
if __name__ == '__main__':
    unittest.main()