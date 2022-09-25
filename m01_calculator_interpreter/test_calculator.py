import unittest

from m00_common.calculator_test_base import CalculatorTestBaseWrapper
from .calculator import calculate


class CalculatorParserTest(CalculatorTestBaseWrapper.CalculatorTest):
    def calc_func(self, formulae: str) -> int:
        return calculate(formulae)

if __name__ == '__main__':
    unittest.main()
