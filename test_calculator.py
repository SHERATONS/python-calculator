import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(1, 4), 5)
    
    def test_add_more(self):
        self.assertEqual(self.calc.add(10, 2), 12)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(10, 2), -8)

    def test_sub_more(self):
        self.assertEqual(self.calc.subtract(10, 20), 10)

    def test_multi(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multi_more(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide_more(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

    def test_mod_more(self):
        self.assertEqual(self.calc.modulo(11, 2), 1)

if __name__ == '__main__':
    unittest.main()
