# -*- coding: gbk -*-
from maya import OpenMayaUI
import pymel.core as pm
from PySide2 import QtWidgets
import shiboken2


# 抓取maya mainWindow widget对象
def maya_mainwindow():
    maya_main_window_name = pm.language.melGlobals['gMainWindow']
    maya_main_window = OpenMayaUI.MQtUtil.findControl(maya_main_window_name)
    widget = shiboken2.wrapInstance(long(maya_main_window), QtWidgets.QWidget)
    return widget


def get_file_path():
    """
    Return the path to the current session
    """
    path = pm.sceneName()
    if isinstance(path, unicode):
        path = path.encode("utf-8")
    return path