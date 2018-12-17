import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('professions.ui', self)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())