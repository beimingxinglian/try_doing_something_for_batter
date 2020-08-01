# -*- coding: gbk -*-
import pymel.core as pm


# 大纲排序
def shord_outline(obj):
    obj_child = obj.getChildren()
    obj_child.sort()
    for i in obj_child:
        pm.reorder(i, back=1)


# 获得层级信息
def get_hierarchy(obj_name):
    if not pm.objExists(obj_name):
        raise RuntimeError('提供的层级名称不存在')
    obj_node = pm.PyNode(obj_name) if isinstance(obj_name, basestring) else obj_name
    childrens = [x.name() for x in obj_node.getChildren(type='transform')]
    if childrens:
        hierarchy = {obj_node.name(): [get_hierarchy(i) for i in childrens]}
    else:
        hierarchy = {obj_node.name(): []}
    return hierarchy


# 对比层级信息
def check(old_hier, new_hier):
    _short_objs = {}
    _added_objs = []
    _disorder_objs = []

    mod_childrens = [value.keys()[0] for value in old_hier.values()[0]]
    rig_childrens = [value.keys()[0] for value in new_hier.values()[0]]
    if not (rig_childrens and mod_childrens):
        return {}, [], []
    _short_extend_objs = [x for x in mod_childrens if x not in rig_childrens]
    if _short_extend_objs:
        _short_objs[old_hier.keys()[0]] = _short_extend_objs
        old_hier[old_hier.keys()[0]] = [x for x in old_hier[old_hier.keys()[0]] if x.keys()[0] not in _short_extend_objs]

    _added_extend_objs = [x for x in rig_childrens if x not in mod_childrens]
    if _added_extend_objs:
        _added_objs.extend(_added_extend_objs)
        new_hier[new_hier.keys()[0]] = [x for x in new_hier[new_hier.keys()[0]] if x.keys()[0] not in _added_extend_objs]

    rig_intersection = [x for x in mod_childrens if x in rig_childrens]
    mod_intersection = [x for x in rig_childrens if x in mod_childrens]
    if rig_intersection:
        for m, rig_children in enumerate(rig_intersection):
            if rig_children != mod_intersection[m]:
                _disorder_objs.append(rig_children)
            else:
                return_tuple = check(old_hier.values()[0][m].copy(), new_hier.values()[0][m].copy())
                _short_objs.update(return_tuple[0])
                _added_objs.extend(return_tuple[1])
                _disorder_objs.extend(return_tuple[2])
    return _short_objs, _added_objs, _disorder_objs