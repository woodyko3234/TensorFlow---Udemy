#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:51:23 2017

@author: justinwu
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')


plt.show()

print('---------')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
print('---------')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()