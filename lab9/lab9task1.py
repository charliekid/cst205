# CST 205
# Charlie Nguyen
# 10/25/20

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget,
                             QVBoxLayout, QComboBox)
from PySide2.QtCore import Slot


class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    # creates values that can be picked from
    self.my_list = ["Pick a value", "red", "orange"]
    # color dictionary
    self.color_diction = {
        "red rgb" : "255, 51,51",
        "red hex" : "FF3333",
        "orange rgb" : "255, 153, 153",
        "orange hex" : "FF9999"
    }

    # Sets up items
    self.my_combo_box = QComboBox()
    self.my_combo_box.addItems(self.my_list)
    self.my_label = QLabel("")



    # adds combo box to window
    vbox = QVBoxLayout()
    vbox.addWidget(self.my_combo_box)
    vbox.addWidget(self.my_label)

    self.setLayout(vbox)
    self.my_combo_box.currentIndexChanged.connect(self.update_ui)

  @Slot()
  def update_ui(self):
    my_text = self.my_combo_box.currentText()
    my_index = self.my_combo_box.currentIndex()
    rgbString = self.my_list[my_index] + " rgb"
    hexString = self.my_list[my_index] + " hex"
    self.my_label.setText(f'RGB: {self.color_diction[rgbString]}   Hex: {self.color_diction[hexString]}')

app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()