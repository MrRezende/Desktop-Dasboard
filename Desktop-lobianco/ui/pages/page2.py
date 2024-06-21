from PyQt5.QtWidgets import QWidget, QVBoxLayout
from utils.graph_utils import create_graph

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(create_graph())
