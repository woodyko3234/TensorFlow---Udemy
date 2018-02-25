#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:34:32 2017

@author: justinwu
"""

import numpy as np
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(A)
print(linalg.inv(A))
print(A.dot(linalg.inv(A)))