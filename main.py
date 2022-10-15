from PyQt5.QtWidgets  import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
#import testing.test
import sys
import command_parsing.command_parser
from typing import Dict,Union,List
from gui.command_line_completer import CommandLineCompleter
from gui.table_view_creator import create_table_view
from terminal import terminal
from command_parsing.command import Command
from command_parsing.command_manager import CommandManager,JSOnBasedCommandLoader,ShellCommandsLoader,CommandLoader

class SharedComponents:
    def __init__(self,le:QLineEdit,layout:QVBoxLayout,window:QWidget,app:QApplication) -> None:
        self.lineEdit=le
        self.vLayout=layout
        self.window=window
        self.app=app
        self.terminal:terminal.Terminal
        self.manager:CommandManager
def return_press():
    term=shared_components.terminal
    le=shared_components.lineEdit
    layout=shared_components.vLayout
    assert le is not None and layout is not None
    cmd=command_parsing.command_parser.parse_command(shared_components.manager,le.text())
    table_Data=term.execute_command(cmd)
    if table_Data!=None:
        table=create_table_view(table_Data)
        layout.removeWidget(le)
        layout.addWidget(table)
        layout.addWidget(le)
def init_gui():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    le.returnPressed.connect(return_press)
    layout=QVBoxLayout()
    layout.addWidget(le)
    win.setLayout(layout)
    return SharedComponents(le,layout,win,app)

def init_completion(sharedComponents:SharedComponents):
    completer=CommandLineCompleter(sharedComponents.manager,lambda : sharedComponents.lineEdit.cursorPosition())
    sharedComponents.lineEdit.setCompleter(completer)
def init_terminal(shared_components:SharedComponents):
    shared_components.terminal=terminal.Terminal()
    shared_components.manager=CommandManager([ShellCommandsLoader(shared_components.terminal.terminal_state),JSOnBasedCommandLoader()])
def main():
    global shared_components
    shared_components=init_gui()
    init_terminal(shared_components)
    init_completion(shared_components)
    shared_components.window.show()
    return shared_components.app.exec()
main()