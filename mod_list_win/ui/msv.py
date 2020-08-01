# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msv.ui'
#
# Created: Sat Aug  1 19:10:31 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.verticalLayout_2.addWidget(self.label1)
        self.export_but = QtWidgets.QPushButton(self.centralwidget)
        self.export_but.setObjectName("export_but")
        self.verticalLayout_2.addWidget(self.export_but)
        self.import_old_but = QtWidgets.QPushButton(self.centralwidget)
        self.import_old_but.setObjectName("import_old_but")
        self.verticalLayout_2.addWidget(self.import_old_but)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.verticalLayout_2.addWidget(self.label3)
        self.load_old_but = QtWidgets.QPushButton(self.centralwidget)
        self.load_old_but.setObjectName("load_old_but")
        self.verticalLayout_2.addWidget(self.load_old_but)
        self.load_new_but = QtWidgets.QPushButton(self.centralwidget)
        self.load_new_but.setObjectName("load_new_but")
        self.verticalLayout_2.addWidget(self.load_new_but)
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.verticalLayout_2.addWidget(self.label4)
        self.check_but = QtWidgets.QPushButton(self.centralwidget)
        self.check_but.setObjectName("check_but")
        self.verticalLayout_2.addWidget(self.check_but)
        self.clear_but = QtWidgets.QPushButton(self.centralwidget)
        self.clear_but.setObjectName("clear_but")
        self.verticalLayout_2.addWidget(self.clear_but)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "层级错误", None, -1))
        self.export_but.setText(QtWidgets.QApplication.translate("MainWindow", "导出所选层级", None, -1))
        self.import_old_but.setText(QtWidgets.QApplication.translate("MainWindow", "导入old层级", None, -1))
        self.load_old_but.setText(QtWidgets.QApplication.translate("MainWindow", "加载old层级", None, -1))
        self.load_new_but.setText(QtWidgets.QApplication.translate("MainWindow", "加载new层级", None, -1))
        self.check_but.setText(QtWidgets.QApplication.translate("MainWindow", "对比所选层级", None, -1))
        self.clear_but.setText(QtWidgets.QApplication.translate("MainWindow", "clear", None, -1))

