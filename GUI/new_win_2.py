# CST 205
# Charlie Nguyen
# 10/25/20
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit,
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot, QUrl
from PySide2.QtCore import Qt

class NewWindow(QWidget):
  def __init__(self, url):
    super().__init__()

    p = self.palette()
    p.setColor(self.backgroundRole(), Qt.red)
    self.setPalette(p)
    self.text = QLabel(url)
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.text)
    self.setLayout(self.layout)


class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.my_list = ['sun', 'sky', 'beach']
    self.combo = QComboBox()
    self.combo.addItems(self.my_list)
    self.btn = QPushButton('CLICK ME')
    vbox = QVBoxLayout()
    vbox.addWidget(self.combo)
    vbox.addWidget(self.btn)
    self.setLayout(vbox)

    self.btn.clicked.connect(self.open_win)

  @Slot()
  def open_win(self):
    i = self.combo.currentIndex()
    self.new_win = NewWindow(self.my_list[i])
    self.new_win.show()
    self.repaint()

app = QApplication(sys.argv)
main = MyWindow()
main.show()
sys.exit(app.exec_())