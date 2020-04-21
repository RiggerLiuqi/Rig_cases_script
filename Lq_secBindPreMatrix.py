# -*- encoding: utf-8 -*-
"""
@File    : Lq_secBindPreMatrix.py
@Time    : 2020/4/21_13:22
@Author  : cousin liu
@Email   : 842076056@qq.com
"""

import pymel.core as pm


def secBindPreMatrix(skinCluster_name=None):
    u"""控制器的父物体的父逆矩阵关联控制器下的骨骼对应蒙皮节点的BindPreMatrix"""
    sel_ctrls = pm.ls(sl=True)
    ctrls_grp_parentInverseMatrix = []
    for sel_ctrl in sel_ctrls:
        ctrl_grp = pm.listRelatives(sel_ctrl, p=True)[0]
        ctrl_grp_parentInverseMatrix = ctrl_grp.attr('parentInverseMatrix')[0]
        ctrls_grp_parentInverseMatrix.append(ctrl_grp_parentInverseMatrix)
    ctrls_grp_parentInverseMatrix = sorted(ctrls_grp_parentInverseMatrix)
    print ctrls_grp_parentInverseMatrix

    skinCluster_node = pm.PyNode(skinCluster_name)
    skinCluster_bindPreMatrixs = []
    for i in range(len(sel_ctrls)):
        skinCluster_bindPreMatrix = skinCluster_node.attr('bindPreMatrix')[i]
        skinCluster_bindPreMatrixs.append(skinCluster_bindPreMatrix)
    skinCluster_bindPreMatrixs = sorted(skinCluster_bindPreMatrixs)
    print skinCluster_bindPreMatrixs

    connect_nodes = list(zip(ctrls_grp_parentInverseMatrix, skinCluster_bindPreMatrixs))
    print connect_nodes
    for i in range(len(connect_nodes)):
        pm.connectAttr(connect_nodes[i][0], connect_nodes[i][1], force=True)


secBindPreMatrix()