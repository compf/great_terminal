import argparse
import subprocess
import sys,os
import re
import json
import types

def add_args(command,argsfile):
    help_command=command+" --help"
    if not  os.path.exists(argsfile):
        jsonfile={}
        obj=types.SimpleNamespace()
        obj.name=command
        obj.args=[]
    else:

        with open(argsfile) as f:
            jsonfile=json.load(f)
            obj=types.SimpleNamespace()
            obj.name=command
            obj.args=[]
    if command in jsonfile:
        return
    output=subprocess.getoutput(help_command )
    new_arg=None
    for line in output.split("\n"):
        line=line.strip()
        if line.startswith("-"):
            splitted=[l for l in line.split("  ") if l!=""]
            left=splitted[0]
            right=""
           
            if len(splitted)>1:
                right=splitted[1]

          
            new_arg=types.SimpleNamespace()
            names=left.split(",")
           
            #names=[n.replace(",","").strip() for n in names]

            new_arg.id=names[0].split("=")[0].replace("]","").replace("[","")
            new_arg.forms=[n.split("=")[0].replace("]","").replace("[","") for n in names]
            new_arg.type="string" if any([n for n in names if "=" in n]) else "flag"

            
            if right!="":
                new_arg.help=right
            else:
                new_arg.help=""
            obj.args.append(new_arg)
        elif new_arg!=None:
             remaining=line
             if len(remaining)>0:
                new_arg.help+="\n"+remaining

           
    jsonfile[obj.name]=obj
    with open(argsfile,"w") as f:
        json.dump(jsonfile,f,default=vars,indent=2)
if __name__=="__main__":
    args=sys.argv[1:]
    commands=["ls","mv","cp","cd","rm"]
    for cmd in commands:
        add_args(cmd,args[0])