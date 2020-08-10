# -*- coding: GBK -*-
from PySide2 import QtCore, QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from func_library import frequency_func
from ui import description

reload(frequency_func)
reload(description)


class DescriptionWidget(QtWidgets.QWidget, description.Ui_Form):
    def __init__(self, parent=None):
        super(DescriptionWidget, self).__init__(parent=parent)
        self.setupUi(self)


class UiMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.description_widget = DescriptionWidget(parent)
        super(UiMainWindow, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("box_window")
        self.setWindowTitle(u'������ӷ��ư�')
        self.resize(320, 800)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        # ����һ���ɵ����ӿؼ���С��widget
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.main_layout.addWidget(self.splitter)

        # ����һ��������������widget
        self.scroll_widget = QtWidgets.QScrollArea()
        self.scroll_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_widget.setWidgetResizable(True)
        self.scroll_widget.setMinimumSize(300, 500)
        # ����widget��Ű�ť
        self.button_widget = QtWidgets.QTreeView()
        self.scroll_widget.setWidget(self.button_widget)

        self.vbox = QtWidgets.QVBoxLayout()
        self.button_widget.setLayout(self.vbox)

        # �����ɵ�����widget���뵽splitter��
        self.splitter.addWidget(self.scroll_widget)
        self.splitter.addWidget(self.description_widget)

        # ���Ӱ�ť
        button_num = 10
        for i in range(button_num):
            button = QtWidgets.QPushButton()
            button.setText('PushButton{}'.format(i))
            button.setObjectName('PushButton{}'.format(i))
            self.vbox.addWidget(button)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox.addItem(spacerItem)
        self.button_widget.setMinimumHeight(button_num*50)

        # self.signals_connect()

    # def signals_connect(self):
    #     self.description_widget.save_but.clicked.connect()
    #     self.description_widget.cancel_but.clicked.connect()
    #     self.description_widget.edit_but.clicked.connect()


class DockerMaya(MayaQWidgetDockableMixin, UiMainWindow):
    def __init__(self, parent=None):
        print parent
        super(DockerMaya, self).__init__(parent=parent)
