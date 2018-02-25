#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:16:09 2017

@author: justinwu
"""

import numpy as np

x=[1,2,3,4]
y=[5,6,7]
#輸入一維矩陣x和一矩陣y到meshgrid(x,y)
#回傳(N1,N2,N3,...,Nn)座標的陣列,Ni=len(xi)
xx,yy = np.meshgrid(x,y)
print(xx)
print(yy)