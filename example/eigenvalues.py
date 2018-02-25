#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:07:30 2017

@author: justinwu
"""

import numpy as np
from scipy import linalg as la
A= np.array([[1,5,2],[2,4,1],[3,6,2]])
lna,v=linalg.eig(A)
l1,l2,l3 =lna
#Eigenvalue
print(l1,l2,l3)
print('-----')
#Eigenvector
print(v)
print('-----')
print(v[:,0])
print(v[:,1])
print(v[:,2])
v1 = np.array(v[:,0]).T
print('--------')
print(v1)
print(linalg.norm(A.dot(v1)-l1*v1))
