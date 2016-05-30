#kata: ROMAN NUMBERS
# Wrap an integer and give RomanNumber representation
# for 1 show I
# for 2 show II
# for 1834 show MCCMXXXIV
import unittest
import pdb
from RomanNumber import RomanNumberHelper


class TestRomanNumber(unittest.TestCase):
    def setUp(self):
        self.helper = RomanNumberHelper()

    def test_number_1(self):
        self.assertEqual(self.helper.to_roman(1), 'I')

    def test_number_2(self):
        self.assertEqual(self.helper.to_roman(2), 'II')

    def test_number_3(self):
        self.assertEqual(self.helper.to_roman(3), 'III')

    def test_number_4(self):
        self.assertEqual(self.helper.to_roman(4), 'IV')

    def test_number_5(self):
        self.assertEqual(self.helper.to_roman(5), 'V')

    def test_number_6(self):
        self.assertEqual(self.helper.to_roman(6), 'VI')

    def test_number_7(self):
        self.assertEqual(self.helper.to_roman(7), 'VII')

    def test_number_8(self):
        self.assertEqual(self.helper.to_roman(8), 'VIII')

    def test_number_9(self):
        self.assertEqual(self.helper.to_roman(9), 'IX')

    def test_number_10(self):
        self.assertEqual(self.helper.to_roman(10), 'X')

    def test_number_11(self):
        self.assertEqual(self.helper.to_roman(11), 'XI')

    def test_get_max_decimal_exponent(self):
        self.assertEqual(self.helper.get_max_decimal_exponent(1), 0)
        self.assertEqual(self.helper.get_max_decimal_exponent(5), 0)
        self.assertEqual(self.helper.get_max_decimal_exponent(10), 1)
        self.assertEqual(self.helper.get_max_decimal_exponent(90), 1)
        self.assertEqual(self.helper.get_max_decimal_exponent(555), 2)

    def test_get_digit_by_exp(self):
    # integer=1  exp=0 return 1
    # integer=2  exp=0 return 2
    # integer=10 exp=0 return 0
    # integer=10 exp=1 return 1
    # integer=20 exp=1 return 2
    # integer=10 exp=2 return 0
        self.assertEqual(self.helper.get_digit_by_exp(0,0), 0)
        self.assertEqual(self.helper.get_digit_by_exp(1,0), 1)
        self.assertEqual(self.helper.get_digit_by_exp(2,0), 2)
        self.assertEqual(self.helper.get_digit_by_exp(22,1), 2)
        self.assertEqual(self.helper.get_digit_by_exp(256,1), 5)
    

if __name__ == '__main__':
    unittest.main()