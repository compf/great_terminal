from PyQt5.QtWidgets  import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
#import testing.test
import sys
from typing import Dict,Union
from gui.command_line_completer import CommandLineCompleter
from gui.table_view_creator import create_table_view
from terminal import terminal
from command_parsing.command import Command
from command_parsing.command_manager import CommandManager,JSOnBasedCommandLoader

class GuiComponents:
    def __init__(self,le:QLineEdit,layout:QVBoxLayout,window:QWidget,app:QApplication) -> None:
        self.lineEdit=le
        self.vLayout=layout
        self.window=window
        self.app=app
def return_press():
    term=terminal.Terminal()
    le=gui_components.lineEdit
    layout=gui_components.vLayout
    assert le is not None and layout is not None
    cmd=Command.parse_command(None,le.text())
    table_Data=term.execute_command(cmd)
    assert table_Data is not None
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
    return GuiComponents(le,layout,win,app)

def init_completion(guiComponents:GuiComponents):
    manager=CommandManager([JSOnBasedCommandLoader()])
    completer=CommandLineCompleter(manager,lambda : guiComponents.lineEdit.cursorPosition())
    guiComponents.lineEdit.setCompleter(completer)
def main():
    global gui_components
    gui_components=init_gui()
    init_completion(gui_components)
    gui_components.window.show()
    return gui_components.app.exec()
main()