import unittest

from . import is_alpha, is_digit, is_white


class ParserUtilsTest(unittest.TestCase):

    def test_is_alpha(self):
        self.assertTrue(is_alpha('a'))
        self.assertTrue(is_alpha('z'))
        self.assertTrue(is_alpha('A'))
        self.assertTrue(is_alpha('Z'))
        self.assertTrue(is_alpha('_'))

    def test_is_non_alpha(self):
        self.assertFalse(is_alpha('0'))
        self.assertFalse(is_alpha('-'))
        self.assertFalse(is_alpha(' '))

    def test_is_digit(self):
        self.assertTrue(is_digit('0'))
        self.assertTrue(is_digit('5'))
        self.assertTrue(is_digit('9'))

    def test_is_not_digit(self):
        self.assertFalse(is_digit('a'))
        self.assertFalse(is_digit('Z'))
        self.assertFalse(is_digit('-'))
        self.assertFalse(is_digit(' '))

    def test_whitespace(self):
        self.assertTrue(is_white(' '))
        self.assertTrue(is_white('\t'))
        self.assertTrue(is_white('\n'))
        self.assertTrue(is_white('\r'))

    def test_not_whitespace(self):
        self.assertFalse(is_white('a'))
        self.assertFalse(is_white('-'))
        self.assertFalse(is_white('0'))
        self.assertFalse(is_white('_'))