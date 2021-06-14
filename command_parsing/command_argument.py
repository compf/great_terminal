from typing import Any


class CommandArgument:
    def __init__(self,name:str,type:type,value:Any):
        self.name=name
        self.type=type
        self.value=value