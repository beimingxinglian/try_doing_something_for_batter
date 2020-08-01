# -*- coding: gbk -*-
from PySide2 import QtCore
from PySide2 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(ListModel, self).__init__(parent)
        self.list_data = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.list_data)

    def data(self, index=QtCore.QModelIndex(), role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            content = self.list_data[index.row()].split(':')[-1].split('|')[-1]
            return content
        if role == QtCore.Qt.ForegroundRole:
            return QtGui.QColor(255, 0, 0)

    def flags(self, index=QtCore.QModelIndex()):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index=QtCore.QModelIndex(), value=None, role=QtCore.Qt.DisplayRole):
        self.list_data = value
        self.dataChanged.emit(index, index)
        return True
