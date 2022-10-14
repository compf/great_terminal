from typing import Any,Union


class CommandArgument:
    def __init__(self,name:Union[str,None],type:Union[str,None],value:Union[str,None],required=False):
        self.name=name
        self.type=type
        self.value=value
        self.required=required
        self.forms=[]
        