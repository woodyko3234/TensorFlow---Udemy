#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:22:38 2017

@author: justinwu
"""
import numpy as np
# 建立一個數值從0~11、格式為int64，但是是 3*5 的矩陣
my_reshape_arr = np.arange(15, dtype=np.int64).reshape( (3,5) )
print(my_reshape_arr)
#顯示 [[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]] 的 3*5矩陣


# 建立一個最小值1，最大值100，共分8塊相等間距的矩陣
my_slice_arr = np.linspace(1,100,8)
print(my_slice_arr)
#顯示[   1.           15.14285714   29.28571429   43.42857143   57.57142857
#   71.71428571   85.85714286  100.        ] 的 1*8 矩陣


# 建立一個隨機在0~1之間分布的 2*3 矩陣
my_random_arr = np.random.random( (2, 3) )
print(my_random_arr)
#顯示 [[ 0.2687965   0.38765465  0.48728548]
# [ 0.33212729  0.92145982  0.87586671]]