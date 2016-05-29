#kata: ROMAN NUMBERS
# Wrap an integer and give RomanNumber representation
# for 1 show I
# for 2 show II
# for 1834 show MCCMXXXIV
import unittest
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
    
if __name__ == '__main__':
    unittest.main()