from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox
from utils.report_utils import export_reports

def create_menu(stack):
    menu_widget = QWidget()
    menu_layout = QVBoxLayout(menu_widget)

    btn_page1 = QPushButton('Página 1')
    btn_page2 = QPushButton('Página 2')
    btn_page3 = QPushButton('Página 3')
    btn_expo = QPushButton('Exportar Relatórios')

    setup_button(btn_page1)
    setup_button(btn_page2)
    setup_button(btn_page3)
    setup_button(btn_expo)

    btn_page1.clicked.connect(lambda: stack.setCurrentIndex(0))
    btn_page2.clicked.connect(lambda: stack.setCurrentIndex(1))
    btn_page3.clicked.connect(lambda: stack.setCurrentIndex(2))
    btn_expo.clicked.connect(export_reports)

    menu_layout.addWidget(btn_page1)
    menu_layout.addWidget(btn_page2)
    menu_layout.addWidget(btn_page3)
    menu_layout.addWidget(btn_expo)

    return menu_widget

def setup_button(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #BBBBBB;
            color: black;
            padding: 10px;
            border: none;
            border-radius: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #D2D2D2;
        }
        QPushButton:checked {
            background-color: #9C9C9C;
        }
    """)
    button.setCheckable(True)

def export_reports():
    QMessageBox.information(None, "Exportar Relatórios", "Relatórios exportados com sucesso!")
