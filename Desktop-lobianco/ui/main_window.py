from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter, QStackedWidget
from PyQt5.QtCore import Qt
from .menu import create_menu
from .pages.page1 import Page1
from .pages.page2 import Page2
from .pages.page3 import Page3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Lateral com PyQt')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        self.stack = QStackedWidget()
        self.stack.addWidget(Page1())
        self.stack.addWidget(Page2())
        self.stack.addWidget(Page3())

        self.menu_widget = create_menu(self.stack)
        self.menu_widget.setFixedWidth(200)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.menu_widget)
        splitter.addWidget(self.stack)
        main_layout.addWidget(splitter)

        self.stack.setCurrentIndex(0)
