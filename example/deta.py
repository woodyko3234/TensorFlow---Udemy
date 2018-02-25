#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:06:39 2017

@author: justinwu
"""

import numpy as np
from scipy import linalg as la
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(la.det(A))
A = np.array([[1,2],[3,4]])
print(A)
print(la.det(A))