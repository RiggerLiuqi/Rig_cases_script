# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------#
# .@FileName:    Lq_renameGrp_And_addCreateCtrl
# .@Author:      CousinRig67
# .@Date:        2020-04-21
# .@Contact:     842076056@qq.com
# -------------------------------------------------------------------------------#

import pymel.core as pm


def renameGrp_And_addCreateCtrl():
    u"""选择骨骼上的组，会根据骨骼名字修改骨骼上组的名字，并在组上添加控制器"""
    sel_grp_objs = pm.ls(sl = True)
    for sel_grp_obj in sel_grp_objs:

        sel_child_obj = pm.listRelatives(sel_grp_obj, c = True)[0]
        parent_obj_name = sel_grp_obj.name()
        child_obj_name = sel_child_obj.name()
        sel_grp_obj.rename(child_obj_name + '_grp')

        ctrl_node = pm.group(sel_child_obj, n = child_obj_name + '_ctrl')
        ctrl_shape = pm.circle(sel_child_obj, n = child_obj_name + '_ctrl')[0].getShape()
        pm.parent(ctrl_shape, ctrl_node, s = True, r = True)


renameGrp_And_addCreateCtrl()