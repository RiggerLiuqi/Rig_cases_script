# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------#
# .@FileName:    Lq_delete_GeoShapeOrig
# .@Author:      CousinRig67
# .@Date:        2020-04-21
# .@Contact:     842076056@qq.com
# -------------------------------------------------------------------------------#

import pymel.core as pm


def delete_GeoShapeOrig():
    u"""删除orig节点，选择模型组"""
    parent_obj = pm.ls(sl = True)[0]
    grp_node = parent_obj.node()

    child_objs = pm.listRelatives(parent_obj, pa = True)
    for child_obj in child_objs:
        obj_shapes = child_obj.getShapes()
        for obj_shape in obj_shapes:
            obj_shapeOrig = obj_shape.endswith('ShapeOrig')
            if obj_shapeOrig:
                pm.delete(obj_shape)


delete_GeoShapeOrig()
