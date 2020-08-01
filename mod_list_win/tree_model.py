# -*- coding: gbk -*-
from PySide2 import QtCore
from PySide2 import QtGui


class TreeModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)

    def flags(*args, **kwargs):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEnabled

    def set_data(self, value, namespace='', parent=None):
        if parent is None:
            self.clear()
            self.setHorizontalHeaderLabels(['nameSpace: {}'.format(namespace)])
            parent = QtGui.QStandardItem(value.keys()[0].split(':')[-1].split('|')[-1])
            self.appendRow(parent)
        all_item = [i for i in value.values()[0]]
        for data_dict in all_item:
            child = QtGui.QStandardItem(data_dict.keys()[0].split(':')[-1].split('|')[-1])
            parent.appendRow([child])
            self.set_data(data_dict, namespace='', parent=child)
        return parent
