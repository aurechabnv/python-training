import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from calculator_ui import Ui_Calculator

class MainWindow(QWidget, Ui_Calculator):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())