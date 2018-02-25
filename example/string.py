#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:14:54 2017

@author: justinwu
"""
import pandas as pd
data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9'
df = pd.read_csv(data, dtype=object)
print(df)