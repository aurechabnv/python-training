from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ma to-do list")
        
        main_layout = QVBoxLayout(self)

        self.lw_list = QListWidget()
        self.le_text = QLineEdit()
        self.le_text.setPlaceholderText("Tâche à effectuer")
        self.btn_clear = QPushButton("Tout supprimer")

        main_layout.addWidget(self.lw_list)
        main_layout.addWidget(self.le_text)
        main_layout.addWidget(self.btn_clear)

        self.lw_list.itemDoubleClicked.connect(self.delete_item)
        self.le_text.returnPressed.connect(self.add_item)
        self.btn_clear.clicked.connect(self.clear_list)

    def delete_item(self, item):
        self.lw_list.takeItem(self.lw_list.row(item))

    def add_item(self):
        self.lw_list.addItem(QListWidgetItem(self.le_text.text()))
        self.le_text.clear()

    def clear_list(self):
        self.lw_list.clear()
        

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()