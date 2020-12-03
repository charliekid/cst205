# CST 205
# Charlie Nguyen
# 10/25/20
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit,
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Slot, QUrl


class NewWindow(QWebEngineView):
  def __init__(self, url):
    super().__init__()
    self.load(QUrl(url))

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.url_list = [
      'Pick a value',
      'https://csumb.edu',
      'https://stackoverflow.com/',
      'https://news.ycombinator.com/'
    ]

    self.combo = QComboBox()
    self.combo.addItems(self.url_list)

    self.btn = QPushButton('CLICK ME')

    vbox = QVBoxLayout()
    vbox.addWidget(self.combo)
    vbox.addWidget(self.btn)
    self.setLayout(vbox)

    self.btn.clicked.connect(self.open_win)

    @Slot()
    def open_win(self):
      i = self.combo.currentIndex()
      if i!=0:
        self.new_win = NewWindow(self.url_list[i])
        self.new_win.show()

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())