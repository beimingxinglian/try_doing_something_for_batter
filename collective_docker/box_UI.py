# -*- coding: GBK -*-
from PySide2 import QtCore, QtGui, QtWidgets

from func_library import frequency_func


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.maya_mainwindow = frequency_func.maya_mainwindow()
        super(UiMainWindow, self).__init__(self.maya_mainwindow)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("box_window")
        self.setWindowTitle(u'羊神盒子仿制版')
        self.resize(500, 800)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.window_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.setLayout(self.window_layout)

        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.window_layout.addWidget(splitter2)

        # todo：上下分割，布局随窗口缩放， 动态增加按钮
        self.bottom = QtWidgets.QFrame()
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        splitter2.addWidget(self.bottom)

        textedit = QtWidgets.QTextEdit()
        splitter2.addWidget(textedit)

        label = QtWidgets.QLabel()
        label.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)
        label.setLineWidth(2)
        splitter2.addWidget(label)
