from PyQt5.QtWidgets  import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
#import testing.test
import sys
from typing import Dict,Union
from gui.command_line_completer import CommandLineCompleter
from gui.table_view_creator import create_table_view
from terminal import terminal
from command_parsing.command import Command
from command_parsing.command_manager import CommandManager,JSOnBasedCommandLoader
ui_widgets:Dict[str,Union[QLineEdit,QVBoxLayout,None]]={
    "le":None,
    "layout":None
}
def return_press():
    term=terminal.Terminal()
    le=ui_widgets["le"]
    layout=ui_widgets["layout"]
    assert le is not None and layout is not None
    cmd=Command.parse_command(None,le.text())
    tbl=term.execute_command(cmd)
    assert tbl is not None
    layout.addWidget(create_table_view(tbl))
    
def main():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    le.returnPressed.connect(return_press)
    manager=CommandManager([JSOnBasedCommandLoader()])
    completer=CommandLineCompleter(manager,lambda : le.cursorPosition())
    le.setCompleter(completer)
    layout=QVBoxLayout()
    ls=QListWidget()
    ui_widgets["le"]=le
    ui_widgets["layout"]=layout
    #layout.addWidget(ls)
    layout.addWidget(le)
    win.setLayout(layout)
    win.show()
    app.exec()
main()