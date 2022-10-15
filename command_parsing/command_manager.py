from abc import abstractmethod
from command_parsing.command import *
from command_parsing import shell_command
from env import Environment
from typing import MutableSet
import json
class CommandManager:
    def __init__(self,commandLoaders):
        self.commands:MutableSet[Command]=set()
        for cmd in commandLoaders:
            new_commands=cmd.load()
            if new_commands==None:
                continue
            self.commands|=set(new_commands)
class CommandLoader:
    def load(self):
        pass
class ShellCommandsLoader(CommandLoader):
    def __init__(self,terminalState):
        super().__init__()
        self.terminalState=terminalState
    def load(self):
        result=[]
        result.append(shell_command.ChangeDirCommand("cd",[CommandArgument("","path","")],self.terminalState))
        return result
class JSOnBasedCommandLoader(CommandLoader):
    def load(self):
        path=Environment.Environment.Instance.map[Environment.EnvironmentEnum.JSON_COMMANDS]
        with open(path) as f:
            my_json=json.load((f))
        return self.parse_json(my_json)
        
    def parse_json(self,json_array):
        commands=[]
        for json_cmd in json_array:
            cmd_name=json_cmd["name"]
            args=[]
           
            for json_arg in json_cmd["args"]:
                
                forms=json_arg["forms"]
                if forms==None:
                    name=None
                    args.append(CommandArgument(None,None,None))
                    continue
                else:
                    name=forms[0]
                required=True if "required"  in json_arg and  json_arg["required"]==True else False
                id=json_arg["id"]
                type=json_arg["type"]
                arg=CommandArgument(name,type,None,required)
                args.append(arg)
            cmd=Command(cmd_name,args)
            commands.append(cmd)
        return commands

                


                

            

class HistoryCommandLoader(CommandLoader):
    def __init__(self) -> None:
        super().__init__()
    def load(self):
        return None
        pt=Environment.Environment.Instance.map[Environment.EnvironmentEnum.COMMAND_HISTORY]
        with open(pt) as f:
            for line in f:
                pass
