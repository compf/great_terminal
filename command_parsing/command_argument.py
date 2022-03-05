from typing import Any


class CommandArgument:
    def __init__(self,name:str,type:str,value:Any,required=False):
        self.name=name
        self.type=type
        self.value=value
        self.required=required
        self.forms=[]
        