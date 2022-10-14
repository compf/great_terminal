from PyQt5.QtWidgets  import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout,QCompleter
#import testing.test
import sys
from gui import command_line_completer, table_view_creator
from terminal import terminal
from command_parsing import command
from command_parsing import command_manager
ui_widgets={
    "le":None,
    "layout":None
}
def return_press():
    term=terminal.Terminal()
    le=ui_widgets["le"]
    layout=ui_widgets["layout"]
    cmd=command.Command.parse_command(None,le.text())
    tbl=term.execute_command(cmd)
    print("table",tbl)
    layout.addWidget(table_view_creator.create_table_view(tbl))
    
def main():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    le.returnPressed.connect(return_press)
    manager=command_manager.CommandManager([command_manager.JSOnBasedCommandLoader()])
    completer=command_line_completer.CommandLineCompleter(manager,lambda : le.cursorPosition())
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