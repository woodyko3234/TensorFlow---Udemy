#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:38:11 2017

@author: justinwu
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
xx,yy=np.meshgrid(x,y,sparse=True)
z=np.sin(xx**2+yy**2)/(xx**2+yy**2)
h=plt.contourf(x,y,z)