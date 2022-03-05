from command_parsing.command_argument import CommandArgument
from command_parsing.command import Command
from terminal.terminal import Terminal
import unittest


ter=Terminal()
args=[CommandArgument(None,str,r"/etc")]
cmd=Command("dir",args)
ter.execute_command(cmd)
#Command.read_args_from_man(Command("useradd",[]))