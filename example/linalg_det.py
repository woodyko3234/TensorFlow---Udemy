#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:56:48 2017

@author: justinwu
"""

import numpy as np
from scipy import linalg as la
A = np.array([[1,2],[3,4]])
print(A)
print(la.det(A))