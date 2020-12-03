# # CST 205
# # Charlie Nguyen
# # 10/25/20
#
# import sys
from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLabel, QVBoxLayout)
from PySide2.QtCore import Slot
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         vbox = QVBoxLayout()
#         # Sets up search push button
#         self.search_push_btn = QPushButton("Search")
#         self.btn_click_status_label = QLabel('Button not clicked')
#         self.search_push_btn.clicked.connect(self.on_click)
#
#         # Adds search push button
#         vbox.addWidget(self.search_push_btn)
#         vbox.addWidget(self.btn_click_status_label)
#
#         self.setLayout(vbox)
#
#     @Slot()
#     def on_click(self):
#         self.btn_click_status_label.setText('Button clicked')
#         self.repaint()
#
# app = QApplication([])
# my_win = MyWindow()
# my_win.show()
# app.exec_()
