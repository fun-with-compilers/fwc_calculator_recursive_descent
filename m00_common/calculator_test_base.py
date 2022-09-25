import unittest

from m00_common.parser.syntax_error import CalculatorSyntaxError


class CalculatorTestBaseWrapper:
    class CalculatorTest(unittest.TestCase):
        """
        Base class for all calculator tests. This way we can share test cases among all calculator implementations
        """

        def calc_func(self, formulae: str) -> int:
            """
            This is the only function to be overridden by calculator test cases
            :param formulae: Expression to be computed
            :return: Result of the computation
            """
            raise NotImplemented

        def test_empty(self):
            try:
                self.calc_func("")
            except CalculatorSyntaxError as e:
                self.assertTrue(e.msg.startswith('number expected'))

        def test_syntax_error_non_number(self):
            self.assertRaises(CalculatorSyntaxError, lambda: self.calc_func("5+A"))

        def test_syntax_too_many_operators(self):
            self.assertRaises(CalculatorSyntaxError, lambda: self.calc_func("5**2"))

        def test_const_5(self):
            self.assertEqual(5, self.calc_func("5"))

        def test_const_666(self):
            self.assertEqual(666, self.calc_func("666"))

        def test_const_negative(self):
            self.assertEqual(-123, self.calc_func("-123"))

        def test_add(self):
            self.assertEqual(10, self.calc_func("5+5"))
            self.assertEqual(55, self.calc_func("5+50"))

        def test_sub(self):
            self.assertEqual(0, self.calc_func("5-5"))
            self.assertEqual(-45, self.calc_func("5-50"))

        def test_add_negative(self):
            self.assertEqual(0, self.calc_func("5+-5"))

        def test_add_multi(self):
            self.assertEqual(1 + 2 + 3 + 4 + 5, self.calc_func("1+2+3+4+5"))

        def test_mul(self):
            self.assertEqual(8, self.calc_func("2*4"))

        def test_div(self):
            self.assertEqual(5, self.calc_func("10/2"))

        def test_precedence_1(self):
            self.assertEqual((2 * 4) + (3 * 2), self.calc_func("2*4+3*2"))

        def test_precedence_2(self):
            self.assertEqual((2 * 4) + (3 * 2) + 5, self.calc_func("2*4+3*2+5"))

        def test_parens(self):
            self.assertEqual(2 * (4 + 3) * 2, self.calc_func("2*(4+3)*2"))
