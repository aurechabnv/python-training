from functools import partial

from PySide2 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("Explorateur de fichiers")
        self.setup_ui()
        self.create_file_model()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.add_actions_to_toolbar()
        self.setup_connections()

    def create_widgets(self):
        self.toolbar = QtWidgets.QToolBar()
        self.tree_view = QtWidgets.QTreeView()
        self.list_view = QtWidgets.QListView()
        self.sld_icon_size = QtWidgets.QSlider()
        self.main_widget = QtWidgets.QWidget()

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        self.list_view.setViewMode(QtWidgets.QListView.IconMode)
        self.list_view.setUniformItemSizes(True)
        self.list_view.setIconSize(QtCore.QSize(48, 48))

        self.sld_icon_size.setRange(32, 256)
        self.sld_icon_size.setValue(48)

        self.tree_view.setSortingEnabled(True)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)

    def add_widgets_to_layouts(self):
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.setCentralWidget(self.main_widget)
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.sld_icon_size)

    def add_actions_to_toolbar(self):
        locations = ["home", "desktop", "documents", "pictures", "music", "movies"]
        for location in locations:
            icon = self.ctx.get_resource(f"{location}.svg")
            action = self.toolbar.addAction(QtGui.QIcon(icon), location.capitalize())
            action.triggered.connect(partial(self.change_location, location))

    def setup_connections(self):
        self.tree_view.clicked.connect(self.on_tree_view_clicked)
        self.list_view.clicked.connect(self.on_list_view_clicked)
        self.list_view.doubleClicked.connect(self.on_list_view_double_clicked)
        self.sld_icon_size.valueChanged.connect(self.change_icon_size)

    def change_icon_size(self, value):
        self.list_view.setIconSize(QtCore.QSize(value, value))

    def change_location(self, location):
        path = eval(f"QtCore.QStandardPaths().standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
        path = path[0]
        self.list_view.setRootIndex(self.model.index(path))
        self.list_view.clicked.emit(self.model.index(path))

    def create_file_model(self):
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.rootPath()
        self.model.setRootPath(root_path)
        self.tree_view.setModel(self.model)
        self.list_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(root_path))
        self.list_view.setRootIndex(self.model.index(root_path))

    def on_tree_view_clicked(self, index):
        if self.model.isDir(index):
            self.list_view.setRootIndex(index)
        else:
            self.list_view.setRootIndex(index.parent())

    def on_list_view_clicked(self, index):
        selection_model = self.tree_view.selectionModel()
        selection_model.setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

    def on_list_view_double_clicked(self, index):
        self.list_view.setRootIndex(index)