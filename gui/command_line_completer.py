from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QAbstractListModel,QModelIndex,QStringListModel
from typing import List
from command_parsing import command_manager,command
import re
import shlex
class CommandLineCompleter(QCompleter):
    def __init__(self,manager:command_manager.CommandManager) -> None:
        super().__init__()
        
        self.commands=manager.commands

        self.setModel(QStringListModel([cmd.name for cmd in self.commands]))
        print([cmd.name for cmd in self.commands])
        self.last_input=""
    def merge_names(self,name1:str,name2:str):
        if name1.endswith("-"):
            name1=name1.rstrip("-")
        return name1 +name2

    def splitPath(self,path:str)->List[str]:
        splitted=shlex.split(path)
        template=[cmd for cmd in self.commands if cmd.name==splitted[0]]
        template=template[0] if len(template)>0 else None
        if template==None:
            return [path]
        cmd=command.Command.parse_command(template,path)
        self.data=[self.merge_names(path,arg.name) for arg in template.args]
        #print()
        #print(path)
        #print(data)
        #print()
        self.setModel(QStringListModel(self.data))
        return [path]
    def pathFromIndex(self,index:QModelIndex):
        print("test")
        print(index.row(),index.column())
        return self.data[index.row()]
   