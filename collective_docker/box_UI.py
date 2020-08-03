# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets

from func_library import frequency_func


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.maya_mainwindow = frequency_func.maya_mainwindow()
        super(UiMainWindow, self).__init__(self.maya_mainwindow)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("box_window")
        self.setWindowTitle('羊神盒子仿制版')
        self.resize(500, 800)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setGeometry(0, 0, 500, 800)
        self.centralwidget.setObjectName("centralwidget")

        self.window_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.setLayout(self.window_layout)


        # todo：上下分割，布局随窗口缩放， 动态增加按钮
        topleft = QtWidgets.QFrame()
        topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)

        bottom = QtWidgets.QFrame()
        bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)

        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        textedit = QtWidgets.QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])
        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        self.window_layout .addWidget(splitter2)
        self.setLayout(self.window_layout )

