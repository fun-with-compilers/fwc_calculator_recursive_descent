from enum import Enum, auto

from m02_calculator_code_gen.code_generator.abstract_code_generator import CodeGenerator


class PCodeOp(Enum):
    """
    Instruction list for PCode
    """
    I_CONST = auto()
    POP = auto()
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()


class PCodeGenerator(CodeGenerator):
    """
    Code generator to generate pseudo assembly code
    """

    def __init__(self):
        super().__init__()
        self.text = []

    def __inst(self, op_code: PCodeOp, operand: int or None = None):
        self.text.append(PCodeInstruction(op_code, operand))

    def push_i_const(self, int_const_value: int):
        self.__inst(PCodeOp.I_CONST, int_const_value)

    def pop(self):
        self.__inst(PCodeOp.POP)

    def add(self):
        self.__inst(PCodeOp.ADD)

    def sub(self):
        self.__inst(PCodeOp.SUB)

    def mul(self):
        self.__inst(PCodeOp.MUL)

    def div(self):
        self.__inst(PCodeOp.DIV)

    def __str__(self):
        return '\n'.join(self.text)


class PCodeException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class PCodeInstruction:
    """
    Instruction (Op code + operand) for PCode
    """
    def __init__(self, op_code: PCodeOp, operand: int or None = None):
        self.op_code = op_code
        self.operand = operand

    def __str__(self):
        if self.operand is None:
            return str(self.op_code)
        else:
            return f'{self.op_code} {self.operand}'


class PCodeMachine:
    """
    Class to execute (interpret) P-Code
    """
    def __init__(self):
        self.stack = []
        self.machine_lang = {
            PCodeOp.I_CONST: self.i_const,
            PCodeOp.POP: self.pop,
            PCodeOp.ADD: self.add,
            PCodeOp.SUB: self.sub,
            PCodeOp.MUL: self.mul,
            PCodeOp.DIV: self.div
        }

    def execute_p_code(self, code_gen: PCodeGenerator) -> None:
        self.execute_instruction_list(code_gen.text)

    def execute_instruction_list(self, instructions: list[PCodeInstruction]) -> None:
        for instruction in instructions:
            self.execute_instruction(instruction)

    def execute_instruction(self, instruction: PCodeInstruction) -> None:
        if instruction.op_code not in self.machine_lang:
            raise PCodeException(f'Unknown instruction: {instruction.op_code}')
        handler = self.machine_lang[instruction.op_code]
        if instruction.operand is None:
            handler()
        else:
            handler(instruction.operand)

    def i_const(self, operand: int) -> None:
        self.stack.append(operand)

    def pop(self) -> int or None:
        return self.stack.pop() if 0 < len(self.stack) else None

    def add(self) -> None:
        self._op(lambda left, right: left + right)

    def sub(self) -> None:
        self._op(lambda left, right: left - right)

    def mul(self) -> None:
        self._op(lambda left, right: left * right)

    def div(self) -> None:
        self._op(lambda left, right: left / right)

    def _op(self, fn) -> None:
        right = self.stack.pop()
        left = self.stack.pop()
        result = fn(left, right)
        self.stack.append(result)


def execute_p_code(code) -> int or None:
    """
    Execute PCode on the PCodeMachine
    :param code: code generator or list of instructions
    :return: result
    """
    machine = PCodeMachine()
    if isinstance(code, PCodeGenerator):
        machine.execute_p_code(code)
    elif isinstance(code, list):
        machine.execute_instruction_list(code)
    else:
        raise PCodeException('Input not supported. Should be either string, list of PCodeInstruction or PCodeGen')

    return machine.pop()