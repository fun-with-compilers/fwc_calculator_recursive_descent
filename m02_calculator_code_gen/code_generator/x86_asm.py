from m02_calculator_code_gen.code_generator.abstract_code_generator import CodeGenerator


class X86AsmCodeGenerator(CodeGenerator):
    """
    Code generator to generate x86-assembly-ish instructions
    """

    def __init__(self):
        super().__init__()
        self.text = []
        self.operands = 0

    def __inst(self, op_code: str, operands: list[str] or None = None):
        if operands is None or len(operands) == 0:
            instruction = op_code
        else:
            instruction = f'{op_code} {", ".join(operands)}'
        self.text.append(instruction)

    def push_i_const(self, int_const_value: int):
        self.__inst("push", [str(int_const_value)])

    def pop(self):
        self.__inst("pop", ["eax"])

    def add(self):
        self.__inst("pop", ["ebx"])
        self.__inst("pop", ["eax"])
        self.__inst("add", ["eax", "ebx"])
        self.__inst("push", ["eax"])

    def sub(self):
        self.__inst("pop", ["ebx"])
        self.__inst("pop", ["eax"])
        self.__inst("sub", ["eax", "ebx"])
        self.__inst("push", ["eax"])

    def mul(self):
        self.__inst("xor", ["edx", "edx"])
        self.__inst("pop", ["ebx"])
        self.__inst("pop", ["eax"])
        self.__inst("mul", ["ebx"])
        self.__inst("push", ["eax"])

    def div(self):
        self.__inst("xor", ["edx", "edx"])
        self.__inst("pop", ["ebx"])
        self.__inst("pop", ["eax"])
        self.__inst("div", ["ebx"])
        self.__inst("push", ["eax"])

    def __str__(self):
        return '\n'.join(self.text)