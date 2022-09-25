from m00_common.parser import SourceHandler
from m00_common.parser.abstract_parser import AbstractParser


class Calculator(AbstractParser):
    """
    A class that implements calculator as an interpreter.
    Classic interpreters execute the code while parsing without any transformation, compilation, etc.
    This calculator example will immediately interpret the expression while parsing and return the result
    """
    def __init__(self, src: SourceHandler):
        super().__init__(src)

    def expression(self) -> int:
        """
        Entry point: process the rule "expression"
        Read at least one operand, and perform additive operations if there is any operator on the input
        :return: the result of the expression
        """
        # call our utility function "operators".
        return self.operators(
            {
                # Plus sign adds two operands
                '+': lambda left, right: left+right,
                # Minus sign subtract the second operand from the first
                '-': lambda left, right: left-right
            },
            # Reader function is the rule "term"
            self.term)

    def term(self) -> int:
        """
        Process the rule "term": read at least one operand, and perform multiplicative operations if there is any operator on the input
        :return: the result of the expression
        """
        # call our utility function "operators".
        return self.operators(
            {
                # Asterisk multiplies its two operands
                '*': lambda left, right: left*right,
                # Slash divides the first operand with the second
                '/': lambda left, right: left/right
            },
            # Reader function is the rule "factor"
            self.factor)

    def factor(self) -> int:
        """
        Process rule "factor": read a number or an expression if we see parentheses
        :return: Result
        """
        # The next character is parens open?
        if self.match_ch('('):
            # Interpret an expression
            result = self.expression()
            # Expect parens close
            self.expect_ch(')')
            # Return the result
            return result
        else:
            # Simply read a number otherwise
            return self.number()

    def operators(self, fn_ops, fn_read):
        """
        Read an operand using the fn_read function.
        When the next input is an operator (found in fn_ops), read another operand, and call the operator handler function
        to combine our two operands. Repeat this until we see an operator on the input
        :param fn_ops: A dictionary with keys as operators, values as their mapper functions. Operators expected to be binary operators
        :param fn_read: Function to read an operand
        :return: Result
        """
        # Read first operand
        result = fn_read()
        # Do while next input is an operator
        while self.look in fn_ops:
            # Read the operator
            operator = self.get_char()
            # Skop white space
            self.skip_whitespace()
            # Combine previous operand (result) and the next operand into result
            result = fn_ops[operator](result, fn_read())
        # Return the result
        return result

    def number(self) -> int:
        """
        Process the rule "number": read a sequence of digits from the input
        :return: Numeric value
        """
        return self.read_number()


def calculate(formulae: str) -> int:
    """
    Compute the result of an expression given as string
    :param formulae: Expression as string
    :return: Result as a number
    """
    from m00_common.parser import source_from_string
    src = source_from_string(formulae)
    calc = Calculator(src)
    return calc.expression()