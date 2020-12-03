# CST 205
# Charlie Nguyen
# 10/14/20

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLabel, QVBoxLayout)
from PySide2.QtCore import Slot

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()
        self.my_btn = QPushButton("Button 1")
        self.my_lbl = QLabel('Button not clicked')
        self.my_btn.clicked.connect(self.on_click)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl)
        self.setLayout(vbox)

    @Slot()
    def on_click(self):
        self.my_lbl.setText('Button clicked')
        self.repaint()

app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()