from PyQt5.QtWidgets import QApplication, QMainWindow
from widgets.ui_main import *
from widgets.exit_popup import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Initialize UserInterface
        self.ui = UI_MainWindow()
        self.ui.setupUI(self)

        # Set Application Title
        title = "DesktopManager"
        self.setWindowTitle(title)

        # Show Application
        self.show()

    def closeEvent(self, event):
        """
        Show a MessageBox on closeEvent() to make sure if user
        really wants to exit the application
        """
        reply = ExitPopUp().exec_()
    
        if reply == QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())