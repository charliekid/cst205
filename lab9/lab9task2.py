# CST 205
# Charlie Nguyen
# 10/25/20


import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
                               QVBoxLayout, QComboBox)
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QColor

class NewWindow(QWidget):
  def __init__(self, selected_color):
    super().__init__()

    p = self.palette()
    color = QColor(selected_color)
    p.setColor(self.backgroundRole(), color)
    self.setPalette(p)
    self.text = QLabel(selected_color)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.text)
    self.setLayout(self.layout)

    # Function/Method that changes the background color
    # def change_background_color(self, selected_color):
    #     p = self.palette()
    #     color = QColor(selected_color)
    #     p.setColor(self.backgroundRole(), color)
    #     self.setPalette(p)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # creates values that can be picked from
        self.my_list = ["Pick a value", "red", "orange"]
        # color dictionary
        self.color_diction = {
            "red rgb": "255, 51,51",
            "red hex": "#FF3333",
            "orange rgb": "255, 153, 153",
            "orange hex": "#ffa500"
        }

        # Sets up items and combo box
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(self.my_list)
        self.my_label = QLabel("")

        # set up button to create another window
        self.show_color_btn = QPushButton("Show Color")
        # self.btn_click_status_label = QLabel('Button not clicked')
        self.show_color_btn.clicked.connect(self.on_click)

        # adds combo box to window
        vbox = QVBoxLayout()
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_label)

        # add button
        vbox.addWidget(self.show_color_btn)


        self.setLayout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        rgbString = self.my_list[my_index] + " rgb"
        hexString = self.my_list[my_index] + " hex"
        self.my_label.setText(f'RGB: {self.color_diction[rgbString]}   Hex: {self.color_diction[hexString]}')

    @Slot()
    def on_click(self):
        # self.btn_click_status_label.setText('Button clicked')
        my_index = self.my_combo_box.currentIndex()
        hexString = self.my_list[my_index] + " hex"
        # open_window = NewWindow(self.color_diction[hexString])
        # open_window.show()
        # self.repaint()
        self.new_win = NewWindow(self.color_diction[hexString])
        self.new_win.show()
        self.repaint()


app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()