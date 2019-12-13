import re
from .raising import InvalidRomanError

CONVERT_TABLE = {1000: 'M',
                 900: 'CM',
                 500: 'D',
                 400: 'CD',
                 100: 'C',
                 90: 'XC',
                 50: 'L',
                 40: 'XL',
                 10: 'X',
                 9: 'IX',
                 5: 'V',
                 4: 'IV',
                 1: 'I'
                 }
CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

num_roman_valid = re.compile(
    '^M{0,3}(CM|CD|D{0,3}?C{0,3})(XC|XL|L{0,3}?X{0,3})(IX|IV|V{0,3}?I{0,3})$',
    re.IGNORECASE
)
num_arabic_valid = re.compile('\d+$')
str_error = ''


def num_to_roman(numbers):
    """to convert from string to roman"""
    result = ''
    numbers = int(numbers)
    if numbers > 3999:
        result = 'The number is too large'
    elif numbers < 0:
        result = 'The number cannot be negative'
    else:
        for arab in CONVERT_TABLE:
            while numbers >= arab:
                result += CONVERT_TABLE[arab]
                numbers -= arab
    return result


def roman_to_num(str_rom):
    """to convert numbers from roman to arabic"""

    res = 0
    if not num_roman_valid.match(str_rom):
        # res = -1
        raise InvalidRomanError('Invalid input string')
    else:
        str_rom = str_rom.upper()
        for arabic, roman in CONV_TABLE:
            while str_rom.startswith(roman):
                res += arabic
                str_rom = str_rom[len(roman):]
    return res


