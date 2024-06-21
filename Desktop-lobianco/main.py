import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from firebase.firebase_setup import initialize_firebase
from firebase.firebase_setup import link_bd

if __name__ == '__main__':
    link_bd()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
