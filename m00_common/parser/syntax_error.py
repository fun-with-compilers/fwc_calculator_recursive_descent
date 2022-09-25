from m00_common.parser import SourceHandler


class CalculatorSyntaxError(Exception):
    """
    Syntax error exception
    """
    def __init__(self, src: SourceHandler, msg: str):
        """
        Constructor to initialize exception with source handler, so we can provide location information
        :param src: Source handler
        :param msg: Error message
        """
        self.line = src.line
        self.pos = src.pos
        self.msg = msg

    def __str__(self):
        return f'ERROR at {self.line}:{self.pos}: {self.msg}'
