from PyQt5.QtWidgets  import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QHBoxLayout,QCompleter,QScrollArea,QAbstractScrollArea,QLayout,QGridLayout,QMainWindow,QPushButton,QShortcut,QFileDialog
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QKeySequence
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
    def __init__(self,le:QLineEdit,layout:QVBoxLayout,window:QWidget,app:QApplication,viewport:QWidget) -> None:
        self.lineEdit=le
        self.vLayout=layout
        self.window=window
        self.app=app
        self.terminal:terminal.Terminal
        self.viewPort=viewport
def return_press():
    INCREASE_BY=200
    term=shared_components.terminal
    le=shared_components.lineEdit
    layout=shared_components.vLayout
    assert le is not None and layout is not None
    cmd=command_parsing.command_parser.parse_command(shared_components.manager,le.text())
    table_Data=term.execute_command(cmd)
    if table_Data!=None:
        table=create_table_view(table_Data)
        command_le=QLineEdit()
        command_le.setReadOnly(True)
        command_le.setText(le.text())
        layout.addWidget(command_le)
        layout.addLayout(table)
        le.setText("")
        shared_components.viewPort.resize(shared_components.viewPort.size().width(),shared_components.viewPort.size().height()+INCREASE_BY)

def open_directory():
    dir=QFileDialog.getExistingDirectory(shared_components.window)    
    shared_components.lineEdit.insert(dir)
def open_file():
    file=QFileDialog.getOpenFileName(shared_components.window)[0]    
    shared_components.lineEdit.insert(file)         
def init_gui():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    MIN_HEIGHT=400
    outer_layout=QGridLayout()
    le.returnPressed.connect(return_press)
    scrollArea=QScrollArea(win)
    viewPort=QWidget(scrollArea)
    viewPort.setMinimumHeight(MIN_HEIGHT)
    
    viewPort.setMinimumWidth(MIN_HEIGHT)
    scrollArea.setMinimumHeight(MIN_HEIGHT)
    scrollArea.setMinimumWidth(MIN_HEIGHT)
    #scrollArea.setMaximumHeight(MIN_HEIGHT)
    scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
    layout=QVBoxLayout(viewPort)
    layout.setSpacing(20)
    layout.minimumSize().setHeight(MIN_HEIGHT)
    layout.minimumSize().setWidth(MIN_HEIGHT)
    viewPort.setLayout(layout)
    outer_layout.addWidget(viewPort,0,0)
    outer_layout.addWidget(le,1,0)
    win.resize(1000,800)
    win.setLayout(outer_layout)
    scrollArea.setWidget(viewPort)
    dir_shortcut=QShortcut(QKeySequence('Ctrl+D'), le, open_directory)
    file_shortcut=QShortcut(QKeySequence('Ctrl+O'), le, open_file)



    return SharedComponents(le,layout,win,app,viewPort)

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