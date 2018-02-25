#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:14:57 2017

@author: justinwu
"""

import numpy as np 
from scipy import linalg as la
A = np.array([[1,5,2],[2,4,1],[3,6,2]])
lna,v=la.eig(A)
l1,l2,l3=lna
print(l1,l2,l3)
print(v)
print(v[:,0])
print(v[:,1])
print(v[:,2])
print('--------------')
v1=np.array(v[:,0]).T
print(v1)
print(linalg.norm(A.dot(v1)-l1*v1))