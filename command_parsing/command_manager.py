from abc import abstractmethod
from command_parsing.command import *
from command_parsing import ShellCommands
from env import Environment
class CommandManager:
    def __init__(self,commandLoaders):
        self.commands=[]
        for cmd in commandLoaders:
            print(cmd)
            self.commands.append(cmd.load())
class CommandLoader:
    def load(self):
        pass
class ShellCommandsLoader(CommandLoader):
    def __init__(self,terminalState) -> None:
        super().__init__()
        self.terminalState=terminalState
    def load(self):
        result=[]
        result.append(ShellCommands.ChangeDirCommand("cd",[CommandArgument(None,str,None)],self.terminalState))
        
class HistoryCommandLoader(CommandLoader):
    def __init__(self) -> None:
        super().__init__()
    def load(self):
        pt=Environment.Environment.Instance.map[Environment.EnvironmentEnum.COMMAND_HISTORY]
        print(pt)
        with open(pt) as f:
            for line in f:
                print(line)
