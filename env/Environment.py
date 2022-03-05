from enum import IntEnum
import os
class EnvironmentEnum(IntEnum):
    COMMAND_HISTORY=0
    JSON_COMMANDS=1
    Home_DIRECTORY=2
class Environment:
    Instance=None
    def __init__(self) -> None:
        self.map=dict()
class LinuxEnvironment(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.map[EnvironmentEnum.COMMAND_HISTORY]=os.path.expanduser("~/.bash_history")
        self.map[EnvironmentEnum.JSON_COMMANDS]="data/linux/cmd.json"

class WindowsEnvironment(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.map[EnvironmentEnum.COMMAND_HISTORY]=os.path.expandvars(r"%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt")
        self.map[EnvironmentEnum.JSON_COMMANDS]="data/win/cmd.json"

if os.name=="nt":
    Environment.Instance=WindowsEnvironment()
else:
    Environment.Instance=LinuxEnvironment()