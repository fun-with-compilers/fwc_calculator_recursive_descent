from m02_calculator_code_gen.code_generator.abstract_code_generator import CodeGenerator


class Interpreter(CodeGenerator):
    """
    A P-Code generator that doesn't generate anything actually, but directly interprets the instructions.
    Notice that the functionality is the same we had in m01_calculator_interpreter,
    but now using the code generator interface, so we can generate code and execute interpreter with the same parser
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def empty_stack(self):
        return 0 == len(self.stack)

    def push_i_const(self, int_const_value: int):
        self.stack.append(int_const_value)

    def pop(self) -> int:
        return self.stack.pop()

    def _op(self, fn) -> None:
        """
        Helper function for implementing arithmetic operations.
        Pop right, then pop left and perform fn(left, right), and push back the result
        :param fn: Operator
        """
        right = self.pop()
        left = self.pop()
        res = fn(left, right)
        self.push_i_const(res)

    def add(self):
        self._op(lambda left, right: left + right)

    def sub(self):
        self._op(lambda left, right: left - right)

    def mul(self):
        self._op(lambda left, right: left * right)

    def div(self):
        self._op(lambda left, right: left / right)
