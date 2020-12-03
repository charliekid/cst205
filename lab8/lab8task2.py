# CST 205
# Charlie Nguyen
# 10/14/20

import sys
from PySide2.QtWidgets import (QApplication, QPushButton,
                                QHBoxLayout, QVBoxLayout, QWidget)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # horizontal layout with 3 buttons
        h_layout = QHBoxLayout()
        b1 = QPushButton("A")
        b2 = QPushButton("B")
        b3 = QPushButton("C")

        h_layout.addWidget(b1)
        h_layout.addWidget(b2)
        h_layout.addWidget(b3)

        # vertical layout with 3 buttons
        v_layout = QVBoxLayout()
        b4 = QPushButton("D")
        b5 = QPushButton("E")
        b6 = QPushButton("F")

        v_layout.addWidget(b4)
        v_layout.addWidget(b5)
        v_layout.addWidget(b6)

        # outer layer
        main_layout = QHBoxLayout()

        # add previous two inner layouts
        main_layout.addLayout(h_layout)
        main_layout.addLayout(v_layout)

        # set outer layout as a main layout of the widget
        self.setLayout(main_layout)

        # window title
        self.setWindowTitle("Layouts")

        self.show()

app = QApplication([])

# create an instance of MyWindow
w = MyWindow()

sys.exit(app.exec_())
