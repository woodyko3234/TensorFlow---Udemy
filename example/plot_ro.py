#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:34:44 2017

@author: justinwu
"""
import matplotlib.pyplot as plt
#第三個參數是格式字串點plot,'ro'為顯示紅色圓圈
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()