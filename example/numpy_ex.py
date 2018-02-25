#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:12:56 2017

@author: justinwu
"""

# numpy模組 - 建立矩陣
import numpy as np

# 建立一個 np array陣列
myarr = np.array([[1,2,3],[4,5,6]])    #放入list就會轉換喔!
print(myarr)
#顯示 [[1,2,3],[4,5,6]]的 2*3 矩陣


# 建立一個 全為 0 的 3*5 矩陣，並指定為 int16格式
my_zero_arr = np.zeros((3,5), dtype=np.int16)
print(my_zero_arr)
#顯示 [[0 0 0 0 0]
# [0 0 0 0 0]
# [0 0 0 0 0]] 的 3*5 矩陣


# 建立一個長度為15、數值從0~14、格式為 int64 的一維陣列
my_onedim_arr = np.arange(15, dtype=np.int64)
print(my_onedim_arr)
#顯示 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]



