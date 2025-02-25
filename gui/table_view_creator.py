from PyQt5.QtWidgets import QTableView,QGridLayout,QLabel,QLayout
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from typing import List
from PyQt5 import QtCore
from output_parsing.terminal_output_builder import TerminalOutputBuilder
def create_table_view(table_parser:List[List[str]]) ->QGridLayout:
    grid_view=QGridLayout()
    grid_view.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize);
    #grid_view.setContentsMargins(10,10,10,10)
    item_model=QStandardItemModel()
    y=0
    x=0
    for r in table_parser:
        for c in r:
            lbl=QLabel()
            lbl.setText(c)
            lbl.setFixedHeight(20)
            lbl.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse )
      
            grid_view.addWidget(lbl,y,x)
            grid_view.setRowMinimumHeight(y,30)
            x+=1
        x=0
        y+=1
    return grid_view
