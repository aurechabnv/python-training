from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication()
main_window = MainWindow()
main_window.show()


app.exec()