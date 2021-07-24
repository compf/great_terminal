from command_parsing.command_argument import CommandArgument
from typing import List
import os
from abc import abstractmethod
class Command:
    def __init__(self,name:str,args:List[CommandArgument]):
        self.name=name
        self.args=args
   
    def get_unnamed_args(self)->List[CommandArgument]:
        return [a for a in self.args if a.name==None]


    
    