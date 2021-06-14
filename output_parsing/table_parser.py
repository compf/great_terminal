import io

from output_parsing.output_parser import OutputParser


class TableParser(OutputParser):

    def __init__(self,) -> None:
        self.header=None
        self.rows=[]

    def parse_line(self, line: str):
        splitted=[ln for  ln in line.split(" ") if len(ln)>0]
        if self.header==None:
            self.header=splitted
        else:
            self.rows.append(splitted)


