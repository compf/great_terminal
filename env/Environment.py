from enum import IntEnum
import os
class EnvironmentEnum(IntEnum):
    COMMAND_HISTORY=0
class Environment:
    Instance=None
    def __init__(self) -> None:
        self.map=dict()
class LinuxEnvironment(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.map[EnvironmentEnum.COMMAND_HISTORY]=os.path.expanduser("~/.bash_history")
class WindowsEnvironment(Environment):
    def __init__(self) -> None:
        super().__init__()

if os.name=="nt":
    Environment.Instance=WindowsEnvironment()
else:
    Environment.Instance=LinuxEnvironment()