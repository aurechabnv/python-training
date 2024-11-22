from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ma to-do list")
        
        self.main_layout = QVBoxLayout(self)

        self.lw_todos = QListWidget()
        self.le_task_title = QLineEdit()
        self.le_task_title.setPlaceholderText("Tâche à effectuer...")
        self.btn_clear = QPushButton("Tout supprimer")

        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.le_task_title)
        self.main_layout.addWidget(self.btn_clear)

        self.lw_todos.itemDoubleClicked.connect(self.delete_item)
        self.le_task_title.returnPressed.connect(self.add_item)
        self.btn_clear.clicked.connect(self.lw_todos.clear)

    def delete_item(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))

    def add_item(self):
        self.lw_todos.addItem(self.le_task_title.text())
        self.le_task_title.clear()
        

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()