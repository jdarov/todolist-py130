# Q1:

def send_message(to, message="Hello", /, *attachments, urgent=False, **meta):
    print(f"To: {to}")
    print(f"Message: {message}")
    print(f"Attachments: {attachments}")
    print(f"Urgent: {urgent}")
    print(f"Metadata: {meta}")

send_message("Alice", "Hi", "file1.txt", "file2.png", urgent=True, sent_by="Josh", priority=1)

# To: Alice = (positional only)
# Message: Hi = (positional but optional)
# Attachments: (file1.txt, file2.png) = (positional, any number of args including 0)
# Urgent: True = (keyword only, since it comes AFTER the *args parameter)
# Metadata: {sent_by: Josh, priority: 1} = (any number of keyword only args seperated by key/value pairs in a **kwargs dict)


""""
write a function that
1. takes a variable sending an email TO that is positional only
2. variable message that is positional only but optional
3. any number of attachment variables
4. one keyword only argument 
5. any number of keyword only arguments 

print each (including a dict)
"""
#Q2: 

def calculate_total(price=50, tax=0.1, discount=0.0, *, tip=0.15):
    return (price - discount) * (1 + tax + tip)

# The call below raises a TypeError:
calculate_total(price=100, discount=10, tip=0.2)

# The bug is tax=0.1, since it is a positional only you can not express it as a keyword argument in the function
# or alternatively you could move the / to just price and keep tax as a default
# To allow price to be a keyword as well you can set a default value and just remove the / entirely

#Q3:

def submit_report(daily, ops, /, *args, sent_by, encrypted, **kwargs):
    print(f'Daily: {daily}')
    print(f'Ops: {ops}')
    print(f'Args: {args}')
    print(f'Sent_by: {sent_by}')
    print(f'Encrypted: {encrypted}')
    print(f'Kwargs: {kwargs}')

submit_report("daily", "ops", "data.csv", sent_by="system", encrypted=True)

#Q1

"""
What will the following code print? answer without running the code 
"""

def make_greeting():
    greeting = "Hello"

    def greet_function(name, greet=None):
        if not greet:
            return f"{greeting} {name}"
        return f"{greet} {name}"
    return greet_function

greet_person = make_greeting()
print(greet_person("John", "Goodbye"))
print(greet_person("Jane"))

#Q2

"""
Wrtie a function named log_function_call that takes a function as an argument.
when decorated function is called, the decorator should print the name of the function
its positional and keyword arguments and keyword arguments and its return value

the decorate function should still execute as normal
"""

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

# portfolio.py module


class Portfolio:
    """A simple portfolio for managing stock holdings."""

    def __init__(self):
        self._holdings = {}

    @property
    def is_empty(self):
        """Checks if the portfolio is empty."""
        return not self._holdings

    def buy(self, ticker, quantity):
        """Buys a number of shares of a stock."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._holdings[ticker] = self._holdings.get(ticker, 0) + quantity

    def sell(self, ticker, quantity):
        """Sells a number of shares of a stock."""
        if ticker not in self._holdings:
            raise KeyError(f"Stock '{ticker}' not found in portfolio.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > self._holdings[ticker]:
            raise ValueError("Cannot sell more shares than you own.")
        
        self._holdings[ticker] -= quantity
        if self._holdings[ticker] == 0:
            del self._holdings[ticker]

    def get_holdings(self):
        """Returns the current holdings as a dictionary."""
        return self._holdings.copy()

############################
# test_portfolio.py
import unittest
from portfolio import Portfolio

class PorfolioTest(unittest.TestCase):
    # Setup
    def setUp(self):
        self.my_folio = Portfolio()
    # Teardown
    def tearDown(self):
        del self.my_folio

    def test_is_empty(self):
        self.assertTrue(self.my_folio.is_empty)
    
    def test_is_not_empty(self):
        # Exercise / Execute
        self.my_folio.buy('ABC', 1)
        # Assert
        self.assertFalse(self.my_folio.is_empty)

    def test_buy_a_share(self):
        self.my_folio.buy('ABC', 1)
        self.assertEqual(self.my_folio._holdings['ABC'], 1)

    def test_valueException_raised(self):
        with self.assertRaises(ValueError):
            self.my_folio.buy('Abc', '2')

    def test_buy_value_is_negative_error(self):
        with self.assertRaises(ValueError):
            self.my_folio.buy('abc', -1)

    def test_is(self):
        self.assertIsNot(self.my_folio._holdings, self.my_folio.get_holdings)

if __name__ == '__main__':
    unittest.main()

"""
Describe the purpose of pip in the python ecosystem.

then, write a specific command line instructions to perform each of the following actions:

1. install a 'requests' package
2. install a specific version of the numpy package, 1.21.0
3. List all packages currenty installed in your active environment
4. remove the 'requests' package
"""


#$ pip install requests
#$ pip install numpy==1.21.0
#$ ??? = pip list
# pip uninstall requests

import unittest
from person import Person
class PersonTest(unittest.TestCase):

    def setUp(self):
        self.person = Person("Josh", 'd', 17)

    def test_is_minor(self):
        self.assertTrue(self.person.is_minor)
    def test_is_not_minor(self):
        self.person.age = 21
        self.assertFalse(self.person.is_minor)
    def test_full_name(self):
        self.assertEqual("Josh d", self.person.full_name)
    def test_negative_age_exception(self):
        with self.assertRaises(ValueError):
            Person("Name", "Last name", -12)