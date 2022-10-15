from command_parsing.command import Command,CommandArgument

from abc import *
from typing import List

class ShellCommand(Command):
    def __init__(self, name: str, args: List[CommandArgument],terminalState):
        super().__init__(name, args)
        self.terminalState=terminalState
    @abstractmethod
    def execute(self):
        pass
class ChangeDirCommand(ShellCommand):
    def __init__(self, name: str, args: List[CommandArgument], terminalState):
        super().__init__(name, args, terminalState)
       
    def execute(self):
        arg=self.get_unnamed_args()[0]
        self.terminalState.curr_dir=arg.value
