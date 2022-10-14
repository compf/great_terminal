from PyQt5.QtWidgets import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
import testing.test
import sys
from gui import command_line_completer
from command_parsing import command_manager


def main():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    manager=command_manager.CommandManager([command_manager.JSOnBasedCommandLoader()])
    completer=command_line_completer.CommandLineCompleter(manager)
    le.setCompleter(completer)
    layout=QVBoxLayout()
    ls=QListWidget()
    layout.addWidget(ls)
    layout.addWidget(le)
    win.setLayout(layout)
    win.show()
    app.exec()
main()