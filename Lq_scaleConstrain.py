# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------#
# .@FileName:    Lq_scaleConstrain
# .@Author:      CousinRig67
# .@Date:        2020-04-21
# .@Contact:     842076056@qq.com
# -------------------------------------------------------------------------------#

import pymel.core as pm


def scaleConstrain():
    u"""先选控制器，再选被缩放约束的物体"""
    sel_objs = pm.ls(sl = True)
    sel_con = sel_objs[0]
    sel_children = sel_objs[1:]
    for sel_child in sel_children:
        pm.scaleConstraint(sel_con, sel_child, o = [1, 1, 1], w = 1)


scaleConstrain()
