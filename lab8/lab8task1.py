# CST 205
# Charlie Nguyen
# 10/14/20

# sys module needed for optional command line arguments
import sys



from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtCore import Qt


my_qt_app = QApplication([])

class ColorWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle('Background')
    p = self.palette()
    p.setColor(self.backgroundRole(), Qt.red)
    self.setPalette(p)



my_window = ColorWindow()
my_window.show()

# my_qt_app.exec_() runs the main loop
# putting it in sys.exit() allows for a graceful exit
sys.exit(my_qt_app.exec_())
