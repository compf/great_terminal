from abc import abstractmethod,override
from command_parsing.command import *
class CommandManager:
    def __init__(self,commandLoaders):
        self.commands=[]
        for cmd in commandLoaders:
            self.commands.append(cmd.load())
class CommandLoader:
    @abstractmethod
    def load(self):
        pass
class SystemCommandLoader(CommandLoader):
    @override
    def load(self):
        result=[]
        result.append(ChangeDirCommand("cd",[CommandArgument(None,str,None)]))
        

