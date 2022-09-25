import unittest

from m02_calculator_code_gen.calculator_gen import x86_asm_from_expression


class CalculatorX86Test(unittest.TestCase):
    def test_generated_code(self):
        asm = x86_asm_from_expression('5+3*2-9/4')
        self.assertEquals(23, len(asm))


if __name__ == '__main__':
    unittest.main()
