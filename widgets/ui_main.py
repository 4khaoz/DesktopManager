from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from python.manager import *

import os, sys

class UI_MainWindow(object):
    def __init__(self):
        self.Manager = Manager()


    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QSize(400, 400))

        # //////////////////////////////////////////////
        # Setup Main Widget
        # //////////////////////////////////////////////
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setStyleSheet(open(os.path.join(sys.path[0], 'widgets/stylesheet.css')).read())

        # Horizontal Box Layout for Menu-Widget and Work-Widget
        self.MainWidgetLayout = QVBoxLayout(self.MainWidget)
        self.MainWidgetLayout.setSpacing(0)
        self.MainWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWidgetLayout.setAlignment(Qt.AlignCenter)

        self.PDF_Button = QPushButton(self.MainWidget)
        self.PDF_Button.setText("PDF")
        self.PDF_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.PDF_Button.setMinimumSize(QSize(128, 64))
        self.PDF_Button.clicked.connect(lambda: self.Manager.sortFilesInDirectory("PDF"))

        self.PNG_Button = QPushButton(self.MainWidget)
        self.PNG_Button.setText("PNG")
        self.PNG_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.PNG_Button.setMinimumSize(QSize(128, 64))
        self.PNG_Button.clicked.connect(lambda: self.Manager.sortFilesInDirectory("PNG"))

        self.TXT_Button = QPushButton(self.MainWidget)
        self.TXT_Button.setText("TXT")
        self.TXT_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.TXT_Button.setMinimumSize(QSize(128, 64))
        self.TXT_Button.clicked.connect(lambda: self.Manager.sortFilesInDirectory("TXT"))

        self.MainWidgetLayout.addWidget(self.PDF_Button)
        self.MainWidgetLayout.addWidget(self.PNG_Button)
        self.MainWidgetLayout.addWidget(self.TXT_Button)

        MainWindow.setCentralWidget(self.MainWidget)

