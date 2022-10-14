from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QStandardItemModel,QStandardItem

from output_parsing.terminal_output_builder import TerminalOutputBuilder
def create_table_view(table_parser:TerminalOutputBuilder):
    table_view=QTableView()
    item_model=QStandardItemModel()
    y=0
    x=0
    print("windows",table_parser)
    for r in table_parser:
        for c in r:
            print("qd",c)
            item=QStandardItem(c)
            x+=1
            item_model.setItem(y,x,item)
        x=0
        y+=1
    table_view.setModel(item_model)
    return table_view
