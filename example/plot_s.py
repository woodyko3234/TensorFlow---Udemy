#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:42:54 2017

@author: justinwu
"""

import numpy as np

# 0到5每步0.2
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
# 'r--'紅色虛線,'bs'藍色矩形,'g^'綠色三角形
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()