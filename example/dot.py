#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:32:00 2017

@author: justinwu
"""
import numpy as np
a = np.arange(25)
a = a.reshape((5,5)) 
b = np.arange(25)
b = b.reshape((5,5))
print(a + b) 
print(a - b) 
print(a * b) 
print(a / b) 
print(a **2) 
print(a < b)
print(a > b) 
print(a.dot(b))

