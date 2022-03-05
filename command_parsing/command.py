from command_parsing.command_argument import CommandArgument
from typing import List
import os
import subprocess
import shlex
from command_parsing.man_page_parser import ManPageParser
from abc import abstractmethod
class Command:
    def __init__(self,name:str,args:List[CommandArgument]):
        self.name=name
        self.args=args
   
    def get_unnamed_args(self)->List[CommandArgument]:
        return [a for a in self.args if a.name==None]
    @staticmethod
    def construct_from_string(str):
        splitted=shlex.split(str)
        argList=[]
        cmd=Command(splitted[0],argList)
        read_args_from_man(cmd)
    @staticmethod
    def read_args_from_man(cmd):

        pr=subprocess.Popen("man "+cmd.name +" ",stdout=subprocess.PIPE,shell=True)
        txt=pr.communicate(None)[0].decode()
        print(txt)
        prs= ManPageParser(txt)
        prs.parse()
        #os.popen(,)



    
    