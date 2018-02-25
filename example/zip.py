#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:57:25 2017

@author: justinwu
"""

a = [1,2,3]
b = [4,5,6]
#zip(*iterables)將*iterables的元素進行配對,儲存在回傳的序對中
zipped = zip(a,b)
for i in zipped:
    print(i)