from PyQt5.QtWidgets import QApplication, QLineEdit,QListWidget,QWidget,QVBoxLayout
import testing.test
import sys
sys.exit(0)
def main():
    app=QApplication([])
    win=QWidget()
    le=QLineEdit()
    layout=QVBoxLayout()
    ls=QListWidget()
    layout.addWidget(ls)
    layout.addWidget(le)
    win.setLayout(layout)
    win.show()
    app.exec()
main()