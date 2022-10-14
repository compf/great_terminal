from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import QAbstractListModel,QModelIndex,QStringListModel
from typing import List
from command_parsing import command_manager,command
import re
import shlex
class CommandLineCompleter(QCompleter):
    def __init__(self,manager:command_manager.CommandManager,cursor_pos_getter) -> None:
        super().__init__()
        self.cursor_pos_getter=cursor_pos_getter
        self.prefix=""
        self.suffix=""
        self.commands=manager.commands
        model=QStandardItemModel()
        parentItem = model.invisibleRootItem()
        for cmd in self.commands:
            item=QStandardItem(cmd.name)
            parentItem.appendRow(item)
            for arg in cmd.args:
                item.appendRow(QStandardItem(arg.name))
        self.setModel(model)
        self.last_input=""

    def splitPath(self,path:str)->List[str]:
        self.suffix=path[self.cursor_pos_getter():]
        path=path[:self.cursor_pos_getter()]
        splitted=shlex.split(path)
        if len(splitted)==1:
            self.prefix=splitted[0]
            return [self.prefix]
        else:
            self.prefix=" ".join(splitted[:-1])
            return [splitted[0],splitted[-1]]
    def pathFromIndex(self,index:QModelIndex):
        result=self.prefix+ " "+self.model().data(index) +self.suffix
        return result
   