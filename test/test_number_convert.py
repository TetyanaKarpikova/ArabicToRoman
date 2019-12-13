import unittest
from webfirst import utils
from webfirst.raising import  InvalidRomanError


class TestNumberConvert(unittest.TestCase):
    def test_to_roman(self):
        data = '1986'
        result = utils.num_to_roman(data)
        self.assertEqual(result, 'MCMLXXXVI')

    def test_negative_arabic(self):
        data = '-1'
        result = utils.num_to_roman(data)
        self.assertEqual(result, 'The number cannot be negative')

    def test_large_arabic(self):
        data = '4000'
        result = utils.num_to_roman(data)
        self.assertEqual(result, 'The number is too large')

    def test_to_arabic(self):
        data = 'MMMCCI'
        try:
            result = utils.roman_to_num(data)
        except InvalidRomanError as er:
            result = ''
        self.assertEqual(result, 3201)

    def test_negative_roman(self):
        data = '-1'
        try:
            result = utils.roman_to_num(data)
        except InvalidRomanError as er:
            result = 'Invalid input string'
        self.assertEqual(result, 'Invalid input string')

    def test_any_string(self):
        data = 'SDFGHJKL'
        try:
            result = utils.roman_to_num(data)
        except InvalidRomanError as er:
            result = 'Invalid input string'
        self.assertEqual(result, 'Invalid input string')

    def test_rus_string(self):
        data = 'ЧЧШШ'
        try:
            result = utils.roman_to_num(data)
        except InvalidRomanError as er:
            result = 'Invalid input string'
        self.assertEqual(result, 'Invalid input string')


if __name__ == '__main__':
        unittest.main()
