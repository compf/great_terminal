import argparse
import subprocess
import sys
import re
import json
import types

def add_args(command,argsfile):
    help_command=command+" --help"
    with open(argsfile) as f:
        jsonfile=json.load(f)
        obj=types.SimpleNamespace()
        obj.name=command
        obj.args=[]
        print(obj)

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

          
            print(left,right)
            new_arg=types.SimpleNamespace()
            #print(line)
            names=left.split(",")
            #print(names)
           
            #names=[n.replace(",","").strip() for n in names]
            #print(names)

            new_arg.id=names[0].split("=")[0].replace("]","")
            new_arg.forms=[n.split("=")[0].replace("]","") for n in names]
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

           
    jsonfile.append(obj)
    with open(argsfile,"w") as f:
        json.dump(jsonfile,f,default=vars,indent=2)
    #print(output)
if __name__=="__main__":
    args=sys.argv[1:]
    commands=["ls","mv","cp","cd","rm"]
    for cmd in commands:
        add_args(cmd,args[0])