#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:22:15 2017

@author: justinwu
"""

import numpy as np
import matplotlib.pyplot as plt
# 建立一個 10000 normal 平均值為 2,0.5^2標準偏差
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# 畫500柱狀histogram圖
plt.hist(v, bins=500, normed=1)       # matplotlib version (plot)
plt.show()