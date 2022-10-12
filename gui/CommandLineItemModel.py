from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QAbstractListModel,QModelIndex
import re
class CommandLineCompleter(QCompleter):
    def splitPath(path:str):
        if re.search(r"\-\-\w+",path):
            # TODO implement completion functionality. i stopped working on that because of bad internet
