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
        return [a for a in self.args if a.name==None]

    @staticmethod
    def parse_command(template_command,command_str:str):
        splitted=shlex.split(command_str)
        argList=[]
        arg_dict=dict()
        if template_command!=None:
            arg_dict=template_command.get_args_dict()
        cmd=Command(splitted[0],argList)
        if template_command!=None and template_command.name!=splitted[0]:
            raise ValueError("template command does not match command name")
        last_item=None
        value=None
        name=None
        for arg in splitted[1:]:
            if arg.startswith("--"):
                name=arg
                last_item="key"
            elif last_item=="key":
                value=arg
                last_item="value"
            else:
                name=None
                value=arg
            if name in arg_dict:
                argList.append(CommandArgument(name,arg_dict[name].type if name in arg_dict else "",value))
        return cmd

    



    
    