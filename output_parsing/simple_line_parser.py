from output_parsing.output_parser import OutputParser
from output_parsing.simple_line import SimpleLine


class SimpleLineParser(OutputParser):
    def parse_line(self, line: str):
        return SimpleLine(line)
