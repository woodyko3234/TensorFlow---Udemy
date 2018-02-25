#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:04:12 2017

@author: justinwu
"""

import numpy as np

#[A,B]=Meshgrid(a,b)
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a)
print(b)
print(np.size(b))
A=np.ones(np.size(b))*a;
print(np.size(a))
B=b*np.ones(np.size(a))
print(A)
print(B)

