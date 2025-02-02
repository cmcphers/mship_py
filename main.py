from PyQt5.QtWidgets import (QApplication, QWidget)
from mainwindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()