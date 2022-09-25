from m00_common.parser import SourceHandler
from m00_common.parser.abstract_parser import AbstractParser
from .code_generator import CodeGenerator, execute_p_code, PCodeGenerator, X86AsmCodeGenerator
from .code_generator import Interpreter


class CalculatorCodeGen(AbstractParser):
    """
    This calculator implementation uses the same recursive descent parser we constructed for the m01_calculator_interpreter.
    However, instead of interpreting the expression while parsing, we introduce a new interface, the CodeGenerator.
    The code generator has an interface that is similar to an assembly language, we call it P-Code (https://en.wikipedia.org/wiki/P-code_machine)

    """
    def __init__(self, src: SourceHandler, code_gen: CodeGenerator):
        super().__init__(src)
        self.code_gen = code_gen

    def expression(self):
        self.operators(
            {
                '+': self.code_gen.add,
                '-': self.code_gen.sub
            },
            self.term)

    def term(self):
        self.operators(
            {
                '*': self.code_gen.mul,
                '/': self.code_gen.div
            },
            self.factor)

    def factor(self):
        if self.match_ch('('):
            self.expression()
            self.expect_ch(')')
        else:
            self.number()

    def operators(self, fn_ops, fn_read):
        fn_read()
        while self.look in fn_ops:
            operator = self.get_char()
            self.skip_whitespace()
            fn_read()
            fn_ops[operator]()

    def number(self):
        self.code_gen.push_i_const(self.read_number())


def generate_calculator(formulae: str, gen: CodeGenerator):
    from m00_common.parser import source_from_string
    src = source_from_string(formulae)
    calc = CalculatorCodeGen(src, gen)
    calc.expression()


def interpret_calc(formulae: str) -> int or None:
    gen = Interpreter()
    generate_calculator(formulae, gen)
    return None if gen.empty_stack() else gen.pop()


def p_code_calc(formulae: str) -> int or None:
    gen = PCodeGenerator()
    generate_calculator(formulae, gen)
    return execute_p_code(gen)


def x86_asm_from_expression(formulae: str) -> list[str]:
    gen = X86AsmCodeGenerator()
    generate_calculator(formulae, gen)
    return gen.text
