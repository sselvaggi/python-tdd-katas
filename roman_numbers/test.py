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

    def test_number_12(self):
        self.assertEqual(self.helper.to_roman(12), 'XII')

    def test_number_212(self):
        self.assertEqual(self.helper.to_roman(212), 'CCXII')

    def test_number_1999(self):
        self.assertEqual(self.helper.to_roman(1999), 'MCMXCIX')

if __name__ == '__main__':
    unittest.main()