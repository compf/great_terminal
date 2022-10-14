
import abc
from output_parsing.terminal_output import TerminalOutput
from typing import List


class OutputParser:
    def __init__(self) -> None:
        self.result_list = []

    def get_result_list(self) -> List[str]:
        return self.result_list

    @abc.abstractmethod
    def parse_line(self, line: str):
        pass
