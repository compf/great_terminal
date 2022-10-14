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
    def splitPath(self,path:str)->List[str]:
        splitted=shlex.split(path)
        template=[cmd for cmd in self.commands if cmd.name==splitted[0]]
        template=template[0] if len(template)>0 else None
        if template==None:
            return [path]
        cmd=command.Command.parse_command(template,path)
        data=[path+arg.name for arg in template.args]
        print()
        print(path)
        print(data)
        print()
        self.setModel(QStringListModel(data))
        return [path]
   