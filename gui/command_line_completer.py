from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import QAbstractListModel,QModelIndex,QStringListModel
from typing import List
from command_parsing import command_manager,command
import re
import shlex
class CommandLineCompleter(QCompleter):
    def __init__(self,manager:command_manager.CommandManager) -> None:
        super().__init__()
        self.commands=manager.commands
        self.data=[cmd.name for cmd in self.commands]
        model=QStandardItemModel()
        parentItem = model.invisibleRootItem()
        for cmd in self.commands:
            item=QStandardItem(cmd.name)
            parentItem.appendRow(item)
            for arg in cmd.args:
                item.appendRow(QStandardItem(arg.name))
        self.setModel(model)
        print([cmd.name for cmd in self.commands])
        self.last_input=""
    def merge_names(self,name1:str,name2:str):
        if name1.endswith("-"):
            name1=name1.rstrip("-")
        return name1 +name2

    def splitPath(self,path:str)->List[str]:
        splitted=shlex.split(path)
        return [splitted[0],splitted[-1]]
    def pathFromIndex(self,index:QModelIndex):
        print("start")
        result=""
        while index.isValid():
            print(index.row())
            result=self.model().data(index)+ " " +result
            index=index.parent()
        print(result)
        #print(index.row(),index.column())
        return self.model().data(index)
   