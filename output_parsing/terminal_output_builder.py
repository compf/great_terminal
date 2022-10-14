import io

from output_parsing.simple_line_parser import SimpleLineParser
from output_parsing.table_parser import TableParser

from typing import IO
class TerminalOutputBuilder:
    def __init__(self, stdout:IO[str]):
        self.stdout = stdout
        self.result = []

    def parse(self):
        try:
            cmd_it = iter(self.stdout.readlines())
            while True:
                line = next(cmd_it)

                print("table")
                self.parse_table(line, cmd_it)
               

        except StopIteration:
            pass
        return self.result

    def parse_simple(self,line:str ,cmd_it):
        line_parser = SimpleLineParser()
        line_parser.parse_line(line)
        self.result = line_parser.get_result_list()
    def parse_table(self,line:str,cmd_it):
        table_parser=TableParser()
        table_parser.parse_line(line)
        try:
            while True:
                line=next(cmd_it)
                table_parser.parse_line(line)
        except StopIteration:
            pass
        print("rows",table_parser.rows)
        self.result=([table_parser.header]+table_parser.rows)

