import unittest

from m00_common.calculator_test_base import CalculatorTestBaseWrapper
from .calculator_gen import p_code_calc


class CalculatorPCodeTest(CalculatorTestBaseWrapper.CalculatorTest):
    def calc_func(self, formulae: str) -> int:
        return p_code_calc(formulae)


if __name__ == '__main__':
    unittest.main()
