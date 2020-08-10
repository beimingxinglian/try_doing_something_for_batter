# -*- coding: utf-8 -*-
import pymel.core as pm
temp = pm.ls(sl=1)
base_mod, bs_mod = temp[-1::-1]
base_shape = base_mod.getShape()

skin_node = base_shape.listConnections(type='skinCluster')[0]
offset = bs_mod.t.get() - base_mod.t.get()

vtx_num = len(base_mod.vtx[:])
bs_vtx_num = len(bs_mod.vtx[:])

if not base_shape.tweakLocation.listConnections(d=0, s=1):
    tweak_set = base_shape.instObjGroups[0].objectGroups[1].listConnections(d=1, s=0)[0]
    tweak_node = tweak_set.usedBy[0].listConnections(s=1, d=0)[0]
    tweak_node.vlist[0].vertex[0] >> base_shape.tweakLocation

changed = {}
if vtx_num == bs_vtx_num:
    for i in range(vtx_num):
        bs_mod_pos = bs_mod.vtx[i].getPosition(space='world')
        base_mod_pos = base_mod.vtx[i].getPosition(space='world')

        offset = base_mod_pos - bs_mod_pos
        rel_pos = pm.getAttr(base_mod_pos.vtx[i])

        target_pos = bs_mod_pos - base_mod_pos

        if target_pos.length() > 0.0001:
            pm.move(base_mod.vtx[i], (1, 0, 0), relative=1)

            pm.move(base_mod.vtx[i], (-1, 1, 0), relative=1)
            pm.move(base_mod.vtx[i], (0, -1, 1), relative=1)
