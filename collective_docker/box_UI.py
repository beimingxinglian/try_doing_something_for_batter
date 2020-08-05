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
        self.setWindowTitle(u'������ӷ��ư�')
        self.resize(300, 800)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.window_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.setLayout(self.window_layout)

        # ����һ���ɵ����ӿؼ���С��widget
        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.window_layout.addWidget(splitter2)

        # ����һ��������������widget
        self.scroll_widget = QtWidgets.QScrollArea()
        self.vbox_scroll = QtWidgets.QVBoxLayout()
        self.scroll_widget.setLayout(self.vbox_scroll)

        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # button�Ĵ�С��Ҫ������
        self.button_widget.setMinimumSize(300, 4000)

        self.scroll_widget.setWidget(self.button_widget)

        self.vbox = QtWidgets.QVBoxLayout()
        self.button_widget.setLayout(self.vbox)

        splitter2.addWidget(self.scroll_widget)
        splitter2.addWidget(self.description_widget)

        # ���Ӱ�ť
        for i in range(30):
            button = QtWidgets.QPushButton()
            button.setText('PushButton{}'.format(i))
            button.setObjectName('PushButton{}'.format(i))
            self.vbox.addWidget(button)