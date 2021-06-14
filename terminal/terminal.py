from terminal.terminal_state import TerminalState
from command_parsing.command import Command
import subprocess
from output_parsing.terminal_output_builder import  TerminalOutputBuilder
class Terminal:
    def __init__(self) -> None:
        self.commands=dict()
        self.commands["cd"]=self.change_dir

        self.terminal_state=TerminalState()


    def execute_command(self,cmd:Command):
        if cmd.name in self.commands:
            return self.commands[cmd.name](cmd)
        else:
            return self.execute_system_command(cmd)

    def execute_system_command(self,cmd:Command):
        cmd_transformed=[cmd.name]+[ (a.name if a.name!=None else "") + a.value for a in cmd.args ]
        print(cmd_transformed)
        p=subprocess.Popen(cmd_transformed,bufsize=-1,stdout=subprocess.PIPE,shell=True,cwd=self.terminal_state.curr_dir,
        text=True)
        
        builder=TerminalOutputBuilder(p.stdout)
        result=builder.parse()
        print(result)
        
    def change_dir(self,cmd:Command):
        self.terminalState.curr_dir=cmd.get_unnamed_args()[0]
