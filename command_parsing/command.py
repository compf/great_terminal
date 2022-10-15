from command_parsing.command_argument import CommandArgument
from typing import List
import os
import subprocess
import shlex
from abc import abstractmethod
class Command:
    def __init__(self,name:str,args:List[CommandArgument]):
        self.name=name
        self.args=args
    def get_args_dict(self):
        return dict((c.name,c) for c in self.args)
    def get_unnamed_args(self)->List[CommandArgument]:
        return [a for a in self.args if a.name==""]
    def __hash__(self) -> int:
        return self.name.__hash__()
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o,Command):
            return False
        obj:Command=__o
        return self.name==__o.name
   



    
    