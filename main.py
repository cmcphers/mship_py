from PyQt5.QtWidgets import (QApplication, QWidget)
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    app.exec()