#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:53:38 2017

@author: justinwu
"""


import pandas as pd 
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#預設utf-8編碼
df = pd.read_csv('MI_INDEX.csv', encoding='big5')
print(df)