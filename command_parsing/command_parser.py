from command_parsing.command import Command,CommandArgument
from command_parsing.shell_command import ShellCommand,ChangeDirCommand
from command_parsing.command_manager import CommandManager
import shlex
def parse_shell_command(name,argList,terminalState):
    if name=="cd":
        return ChangeDirCommand(name,argList,terminalState)
    else:
        return None

def parse_command(manager:CommandManager,command_str:str):
        splitted=shlex.split(command_str)
        argList=[]
        arg_dict=dict()
        template_command=[cmd for  cmd in manager.commands if cmd.name==splitted[0]]
        if len(template_command)>0:
            template_command=template_command[0]
            arg_dict=template_command.get_args_dict()  
        if isinstance(template_command,ShellCommand):
            print("shell command")
            cmd=parse_shell_command(splitted[0],argList,template_command.terminalState)
        else:
            cmd=Command(splitted[0],argList)
        last_item=None
        value=None
        name=None
        for arg in splitted[1:]:
            if arg.startswith("--"):
                name=arg
                last_item="key"
            elif last_item=="key":
                value=arg
                last_item="value"
            else:
                name=""
                value=arg
            if name in arg_dict:
                argList.append(CommandArgument(name,arg_dict[name].type if name in arg_dict else "",value))
        return cmd

    