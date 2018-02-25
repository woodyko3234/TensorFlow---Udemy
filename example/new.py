#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:12:37 2017

@author: justinwu
"""
import matplotlib.pyplot as mpt

month1 = [1,2,3,4,5,8,10,12]
month2 = [1,3,4,5,6,7,11,12]
sales1 = [20000,40000,60000,80000,100000,120000,140000,160000]
sales2 = [10000,20000,30000,150000,120000,80000,60000,210000]

mpt.plot(month1,sales1,lw=2,label='Ivy Lin')
mpt.plot(month2,sales2,lw=2,label='Johny Wu')
mpt.xlabel('month')
mpt.ylabel('dollars(million)')
mpt.legend()
mpt.title('matplotlib_example')
mpt.show()