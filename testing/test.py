from command_parsing.command_argument import CommandArgument
from command_parsing.command import Command
from terminal.terminal import Terminal
ter=Terminal()
args=[CommandArgument(None,str,"/home/compf/data")]
cmd=Command("ls",args)
ter.execute_command(cmd)