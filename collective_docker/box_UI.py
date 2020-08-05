# -*- coding: GBK -*-
from PySide2 import QtCore, QtGui, QtWidgets

from func_library import frequency_func
from ui import description

reload(frequency_func)
reload(description)


class DescriptionWidget(QtWidgets.QWidget, description.Ui_Form):
    def __init__(self):
        super(DescriptionWidget, self).__init__()
        self.setupUi(self)


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.maya_mainwindow = frequency_func.maya_mainwindow()
        self.description_widget = DescriptionWidget()
        super(UiMainWindow, self).__init__(self.maya_mainwindow)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("box_window")
        self.setWindowTitle(u'羊神盒子仿制版')
        self.resize(300, 800)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.window_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.setLayout(self.window_layout)

        # 创建一个可调整子控件大小的widget
        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.window_layout.addWidget(splitter2)

        # 创建一个包含滚动条的widget
        self.scroll_widget = QtWidgets.QScrollArea()
        self.vbox_scroll = QtWidgets.QVBoxLayout()
        self.scroll_widget.setLayout(self.vbox_scroll)

        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # button的大小需要锁定，
        self.button_widget.setMinimumSize(300, 4000)

        self.scroll_widget.setWidget(self.button_widget)

        self.vbox = QtWidgets.QVBoxLayout()
        self.button_widget.setLayout(self.vbox)

        splitter2.addWidget(self.scroll_widget)
        splitter2.addWidget(self.description_widget)

        # 增加按钮
        for i in range(30):
            button = QtWidgets.QPushButton()
            button.setText('PushButton{}'.format(i))
            button.setObjectName('PushButton{}'.format(i))
            self.vbox.addWidget(button)