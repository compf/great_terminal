
from command_parsing import command
class ManPageParser:
    def construct_from_string(self,command_str:str):
        splitted=shlex.split(command_str)
        argList=[]
        cmd=Command(splitted[0],argList)
        return cmd
    def read_args_from_man(self,cmd:command.Command):

        pr=subprocess.Popen("man "+cmd.name +" ",stdout=subprocess.PIPE,shell=True)
        txt=pr.communicate(None)[0].decode()
        return  txt
    def __init__(self,command:str) -> None:
        cmd=self.construct_from_string(command)
        man_page_text=self.read_args_from_man(cmd)
        self.man_page_text=man_page_text
    def parse(self):
        lines=self.man_page_text.split("\n")
        my_it=iter(lines)
        while True:
            line=next(my_it)
            if line.startswith("SYNOPSIS"):
                self.parse_synopsis(my_it)
            if line.startswith("DESCRIPTION"):
                self.parse_description(my_it)
    def parse_synopsis(self,my_it):
        pass
    def parse_description(self,my_it):
        pass