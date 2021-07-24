Terminal_Output_Counter=0

class TerminalOutput:
    def __init__(self):
        global Terminal_Output_Counter
        Terminal_Output_Counter+=1
        self.id=Terminal_Output_Counter