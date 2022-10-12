from PyQt5.QtWidgets import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
import testing.test
import sys
from gui import CommandLineItemModel



def main():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    completer=QCompleter(CommandLineItemModel.CommandLineItemModel(),le)
    le.setCompleter(completer)
    layout=QVBoxLayout()
    ls=QListWidget()
    layout.addWidget(ls)
    layout.addWidget(le)
    win.setLayout(layout)
    win.show()
    app.exec()
main()