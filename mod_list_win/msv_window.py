# -*- coding: gbk -*-
import json
import os
from PySide2 import QtCore
from PySide2 import QtWidgets

import pymel.core as pm

from func_library import frequency_func
from func_library import hierarchy_func
import mvc_model
from ui import msv
from ui import list_model_widget
from ui import tree_model_widget

reload(frequency_func)
reload(hierarchy_func)
reload(list_model_widget)
reload(msv)
reload(mvc_model)
reload(tree_model_widget)


class ShowWindow(QtWidgets.QMainWindow, msv.Ui_MainWindow):
    def __init__(self):
        self.list_model_widget = list_model_widget.Ui_Form()
        self.tree_model_widget = tree_model_widget.Ui_Form()
        self.maya_mainwindow = frequency_func.maya_mainwindow()
        super(ShowWindow, self).__init__(self.maya_mainwindow)
        self.old_hierarchy = []
        self.new_hierarchy = []
        self.short_objs = {}
        self.added_objs = []
        self.disorder_objs = []
        self.setupUi(self)
        self.setupUi2()
        self.singal_connect()

    def setupUi2(self):
        self.stackedWidget.addWidget(list_model_widget.Ui_Form)
        self.stackedWidget.addWidget(tree_model_widget.Ui_Form)
        self.list_model1 = mvc_model.ListModel(self.listView_1)
        self.list_model2 = mvc_model.ListModel(self.listView_2)
        self.list_model3 = mvc_model.ListModel(self.listView_3)
        self.list_model_widget.listView_1.setModel(self.list_model1)
        self.list_model_widget.listView_2.setModel(self.list_model2)
        self.list_model_widget.listView_3.setModel(self.list_model3)
        self.list_model_widget.listView_1.clicked.connect(self.select_obj1)
        self.list_model_widget.listView_2.clicked.connect(self.select_obj2)
        self.list_model_widget.listView_3.clicked.connect(self.select_obj3)

    def singal_connect(self):
        self.except_but.clicked.connect(self.except_hierarchy)
        self.import_but.clicked.connect(self.import_hierarchy)
        self.check_but.clicked.connect(self.check)

    def select_obj1(self, index=QtCore.QModelIndex()):
        key = self.short_objs.keys()[index.row()]
        obj_name = self.short_objs[key]
        pm.select(obj_name)

    def select_obj2(self, index=QtCore.QModelIndex()):
        obj_name = self.added_objs[index.row()]
        pm.select(obj_name)

    def select_obj3(self, index=QtCore.QModelIndex()):
        obj_name = self.disorder_objs[index.row()]
        pm.select(obj_name)

    def check(self):
        sel_obj = pm.selected()
        if not sel_obj:
            raise RuntimeError('选择一个层级导出')
        elif len(sel_obj) == 1:
            self.new_hierarchy = hierarchy_func.get_hierarchy(sel_obj[0])
        else:
            raise RuntimeError('一次只能导出一个层级')
        data = hierarchy_func.check(self.old_hierarchy.copy(), self.new_hierarchy.copy())
        self.short_objs = {}
        zips = [{m: i} for i in data[0] for m in data[0][i]]
        for short_objs in zips:
            self.short_objs.update(short_objs)
        self.added_objs = data[1]
        self.disorder_objs = data[2]
        self.list_model1.setData(value=self.short_objs.keys())
        self.list_model2.setData(value=self.added_objs)
        self.list_model3.setData(value=self.disorder_objs)

    def except_hierarchy(self):
        sel_obj = pm.selected()
        if not sel_obj:
            raise RuntimeError('选择一个层级导出')
        elif len(sel_obj) == 1:
            self.old_hierarchy = hierarchy_func.get_hierarchy(sel_obj[0])
        else:
            raise RuntimeError('只能选择一个层级')
        file_name = os.path.split(frequency_func.get_file_path())[-1].rsplit('.', 1)[0]
        temp_dir = os.getenv('temp')
        file_temp_path = os.path.join(temp_dir, '{}_hierarchy.json'.format(file_name))
        with open(file_temp_path, 'w') as f:
            json.dump(self.old_hierarchy, f)

    def import_old_hierarchy(self):
        temp_dir = os.getenv('temp')
        file_temp_path = QtWidgets.QFileDialog.getOpenFileName(self.maya_mainwindow, 'Import Hierarchy Json', temp_dir, 'Json (*.json)')
        with open(file_temp_path[0], 'r') as f:
            self.old_hierarchy = json.load(f)

    def import_new_hierarchy(self):
        sel_obj = pm.selected()
        if not sel_obj:
            raise RuntimeError('选择一个层级导出')
        elif len(sel_obj) == 1:
            self.new_hierarchy = hierarchy_func.get_hierarchy(sel_obj[0])
        else:
            raise RuntimeError('只能选择一个层级')

    def clear_data(self):
        self.old_hierarchy = []
        self.new_hierarchy = []
        self.short_objs = {}
        self.added_objs = []
        self.disorder_objs = []


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    foo = ShowWindow()
    foo.show()
    sys.exit(app.exec_())
