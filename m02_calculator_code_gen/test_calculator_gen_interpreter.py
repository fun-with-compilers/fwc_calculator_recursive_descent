import unittest

from m00_common.calculator_test_base import CalculatorTestBaseWrapper
from .calculator_gen import interpret_calc


class CalculatorInterpreterTest(CalculatorTestBaseWrapper.CalculatorTest):
    def calc_func(self, formulae: str) -> int:
        return interpret_calc(formulae)


if __name__ == '__main__':
    unittest.main()
