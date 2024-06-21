from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QTextEdit

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)
        layout.addRow("Nome:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow("Mensagem:", QTextEdit())
