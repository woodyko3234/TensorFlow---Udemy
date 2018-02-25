#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:44:56 2017

@author: justinwu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.001)
y = np.sin(x)


plt.plot(x, y)
plt.show()  
