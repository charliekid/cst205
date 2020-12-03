# CST 205
# Charlie Nguyen
# 10/25/20

import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget,
                                QPushButton, QLineEdit, QVBoxLayout, QComboBox)
from PySide2.QtCore import Slot



class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.img_manipulation_list = ["Pick a filter", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

    self.my_combo_box = QComboBox()
    self.my_combo_box.addItems(self.img_manipulation_list)
    self.user_manipulation_label = QLabel("")

    vbox = QVBoxLayout()
    vbox.addWidget(self.my_combo_box)
    vbox.addWidget(self.user_manipulation_label)

    self.setLayout(vbox)
    self.my_combo_box.currentIndexChanged.connect(self.update_ui)

  @Slot()
  def update_ui(self):
    my_text = self.my_combo_box.currentText()
    my_index = self.my_combo_box.currentIndex()
    self.user_manipulation_label.setText(f'You chose {self.img_manipulation_list[my_index]}.')


app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()