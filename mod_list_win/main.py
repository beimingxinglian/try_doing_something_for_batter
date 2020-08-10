import sys
from PySide2 import QtCore
sys.path.append(r'D:\github\try_doing_something_for_batter')
from mod_list_win import msv_window
from func_library import frequency_func

reload(msv_window)

parentUI = frequency_func.maya_mainwindow()
mod_list_window = parentUI.findChildren(QtCore.QObject, 'mod_list_window')
if mod_list_window:
    for clo_window in mod_list_window:
        clo_window.close()
    box_window = msv_window.ShowWindow()
    box_window.show()
else:
    mod_list_window = msv_window.ShowWindow()
    mod_list_window.show()
