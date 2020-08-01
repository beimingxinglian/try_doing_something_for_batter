# -*- coding: gbk -*-
from PySide2 import QtCore
from PySide2 import QtGui


class TreeModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)

    def flags(*args, **kwargs):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEnabled

    def data_show(self, value, namespace=None):
        self.setHorizontalHeaderLabels(['nameSpace: {}'.format(namespace)])
        parent = self.set_data(value)
        self.appendRow([parent])

    def set_data(self, value, parent=None):
        if not parent:
            self.clear()
            parent = QtGui.QStandardItem(value.keys()[0].split('|')[-1])
        all_item = [i for i in value.values()[0]]
        for data_dict in all_item:
            child = QtGui.QStandardItem(data_dict.keys()[0].split('|')[-1])
            parent.appendRow([child])
            self.set_data(data_dict, child)
        return parent
