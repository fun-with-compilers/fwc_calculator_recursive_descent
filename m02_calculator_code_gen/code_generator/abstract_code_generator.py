class CodeGenerator:
    """
    https://en.wikipedia.org/wiki/P-code_machine

    A code generator for pseudo-machine code. We may either emit the instructions (see p_code.py) or
    interpret them.
    """

    def __init__(self):
        pass

    def push_i_const(self, int_const_value: int) -> None:
        """
        Push integer constant onto the stack
        :param int_const_value: integer constant value
        """
        pass

    def pop(self) -> int:
        """
        Pops an integer from the stack (remove then return the value)
        :return: The top element of the stack
        """
        pass

    def add(self) -> None:
        """
        Add the two topmost elements on the stack and push the result back
        """
        pass

    def sub(self):
        """
        Pop b, then a from stack, then push back a-b
        """
        pass

    def mul(self):
        """
        Pop b, then a from stack, then push back a*b
        """
        pass

    def div(self):
        """
        Pop b, then a from stack, then push back a-b
        """
        pass


