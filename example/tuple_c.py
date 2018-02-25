#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:08:41 2017

@author: justinwu
"""

tp6=tuple([66,22,3,46,5,65,7,83,19])
print(tp6)
list1 = list(tp6)
list1.sort()#排序串列
print(list1)
print('-----------')
tp8=tuple(list1)
tp9=tuple(list1)
print(tp8)
print(tp8 == tp9)#比較兩個數組tuple


