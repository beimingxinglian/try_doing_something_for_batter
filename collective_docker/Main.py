import sys
from PySide2 import QtCore
sys.path.append(r'D:\github\try_doing_something_for_batter')
from collective_docker import box_UI
from func_library import frequency_func

reload(box_UI)

parentUI = frequency_func.maya_mainwindow()
box_window = parentUI.findChildren(QtCore.QObject, 'box_window')
if box_window:
    for clo_window in box_window:
        clo_window.close()
    box_window = box_UI.UiMainWindow()
    box_window.show(dockable=True)
else:
    box_window = box_UI.UiMainWindow()
    box_window.show(dockable=True)


"""
import sys
from PySide2 import QtCore
sys.path.append(r'D:\github\try_doing_something_for_batter')
from collective_docker import box_UI

reload(box_UI)

box_window = box_UI.DockerMaya()

box_window.show(dockable=True)


"""