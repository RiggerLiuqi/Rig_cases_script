# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------#
# .@FileName:    Lq_qureySkInt
# .@Author:      CousinRig67
# .@Date:        2020-04-21
# .@Contact:     842076056@qq.com
# -------------------------------------------------------------------------------#

import pymel.core as pm


def qureySkInt(skName = None):
    u"""查询模型上的蒙皮骨骼"""
    sk = pm.skinCluster(skName, q = True, inf = True)
    sel_skInt = pm.select(sk)


qureySkInt()