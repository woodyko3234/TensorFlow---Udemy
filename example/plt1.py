#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:24:40 2017

@author: justinwu
"""
import numpy as np
import matplotlib.pyplot as plt

data={'a':np.arange(50),
      'c':np.random.randint(0,50,50),
      'd':np.random.randn(50)}
data['b']= data['a']+10*np.random.randn(50)
data['d']=np.abs(data['d'])*100
plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()