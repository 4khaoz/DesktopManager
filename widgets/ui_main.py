from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys

class UI_MainWindow(object):
    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))

        # //////////////////////////////////////////////
        # Setup Main Widget
        # //////////////////////////////////////////////
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setStyleSheet(open(os.path.join(sys.path[0], 'widgets/stylesheet.css')).read())

        # Horizontal Box Layout for Menu-Widget and Work-Widget
        self.MainWidgetLayout = QHBoxLayout(self.MainWidget)
        self.MainWidgetLayout.setSpacing(0)
        self.MainWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWidgetLayout.setAlignment(Qt.AlignLeft)

        MainWindow.setCentralWidget(self.MainWidget)