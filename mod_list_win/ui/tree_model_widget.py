# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_model_widget.ui'
#
# Created: Sat Aug  1 20:43:56 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 448)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.old_view = QtWidgets.QTreeView(Form)
        self.old_view.setObjectName("old_view")
        self.gridLayout.addWidget(self.old_view, 1, 0, 1, 1)
        self.new_view = QtWidgets.QTreeView(Form)
        self.new_view.setObjectName("new_view")
        self.gridLayout.addWidget(self.new_view, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Old", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "New", None, -1))

