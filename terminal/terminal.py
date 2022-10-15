from terminal.terminal_state import TerminalState
from command_parsing.command import Command
import subprocess
from command_parsing import command_manager,shell_command
from output_parsing.terminal_output_builder import  TerminalOutputBuilder
class Terminal:
    def __init__(self) -> None:
        self.commands=dict()
        self.terminal_state=TerminalState()
        self.cmdManager=command_manager.CommandManager([command_manager.ShellCommandsLoader(self.terminal_state),command_manager.HistoryCommandLoader(),command_manager.JSOnBasedCommandLoader()])
       


    def execute_command(self,cmd:Command):
        print("execute",cmd.name,cmd)
        if isinstance(cmd,shell_command.ShellCommand):
            print("shell",cmd.name)
            return cmd.execute()
        else:
            return self.execute_external_command(cmd)
    def expand(self,arg:str):
        print("expand",arg)
        if arg.startswith("."):
            print("newarg",self.terminal_state.curr_dir + arg[1:])
            return self.terminal_state.curr_dir + arg[1:]
        else:
            return arg

    def execute_external_command(self,cmd:Command):
        cmd_transformed=[cmd.name]+[ (a.name if   a.name!=None  else "") + self.expand(a.value) for a in cmd.args if a.value!=None]
        
        print("run",cmd_transformed)
        p=subprocess.Popen(cmd_transformed,bufsize=-1,stdout=subprocess.PIPE,shell=False,cwd=self.terminal_state.curr_dir,
        text=True)
        assert p.stdout!=None
        builder=TerminalOutputBuilder(p.stdout)
        result=builder.parse()
        return result
        
    def change_dir(self,cmd:Command):
        new_workdir=cmd.get_unnamed_args()[0].value
        assert new_workdir is not None
        print("change dir",new_workdir)
        self.terminal_state.curr_dir=new_workdir
