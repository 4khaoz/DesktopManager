from PyQt5.QtWidgets import *


class ExitPopUp(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exit Application")
        self.setIcon(QMessageBox.Question)
        self.setText("Are you sure you want to exit the application?")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setEscapeButton(QMessageBox.No)

        #self.exec_()