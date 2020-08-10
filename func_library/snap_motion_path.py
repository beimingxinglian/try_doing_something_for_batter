# -*- coding: utf-8 -*-
import pymel.core as pm


def connect_curve_to_motionPath(snap_obj, curve, u_value):
    """

    :param snap_obj:
    :param curve:
    :param u_value:
    :return:
    """
    motionPath_node = pm.pathAnimation(snap_obj, c=curve, fm=True, f=True,
                                       fa='x', ua='y', n='{}_motionPath'.format(snap_obj))
    motionPath_node = pm.PyNode(motionPath_node)
    pm.delete(motionPath_node.uValue.listConnections())
    motionPath_node.uValue.set(u_value)


def get_point_uValue(point, curve):
    """
    获取某个点距离曲线最近点（一般用来求曲线上的点）的uValue
    :param point:点的位置信息
    :param curve:
    :return:
    """
    curve_base = pm.duplicate(curve, rr=1, n=curve+'_base')[0]
    pm.rebuildCurve(curve_base, rt=0, ch=0, kr=0, s=2, d=1)
    nearest_point_on_curve_node = pm.createNode('nearestPointOnCurve', n="{}_nearestPointOnCurve".format(point_obj))
    curve_base.getShape().worldSpace[0] >> nearest_point_on_curve_node.inputCurve
    nearest_point_on_curve_node.inPosition.set(point)
    point_u_value = nearest_point_on_curve_node.parameter.get()
    pm.delete(nearest_point_on_curve_node)
    pm.delete(curve_base)
    return point_u_value


def addAttr_for_move(control, motionpath_obj, attrname='motionPathMove'):
    """

    :param control: 总控制器
    :param motionpath_obj: 吸附在路径上的物体
    :param attrname: 在控制器上添加的属性
    :return:
    """
    if not pm.objExists('{}.{}'.format(control, attrname)):
        control.addAttr(attrname, min=-10, max=10, k=1)
    attr_node = pm.PyNode('{}.{}'.format(control, attrname))
    motionpath_node = motionpath_obj.listConnections(type='motionPath')[0]
    mult_node = pm.createNode('multiplyDivide', n='{}_mult_node'.format(motionpath_obj))
    attr_node >> mult_node.input1X
    mult_node.input2X.set(0.1)

    plus_node = pm.createNode('plusMinusAverage', n='{}_plus_node'.format(motionpath_obj))
    plus_node.input1D[0].set(motionpath_node.uValue.get())
    mult_node.outputX >> plus_node.input1D[1]

    plus_node.output1D >> motionpath_node.uValue


def create_joint_snap_obj(pos_list, name='joint'):
    """
    沿选定物体创建骨骼
    :param obj:
    :param name:
    :return:
    """
    pm.select(cl=1)
    for i, pos in enumerate(pos_list):
    pose = pm.xform(obj, q=1, t=1)
    jnt = pm.joint(n='{}{:0>2}_jnt'.format(name, i))
    jnt.t.set(pose)

