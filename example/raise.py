#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:26:42 2017

@author: justinwu
"""

import sys 

def displaySalary(salary):
    if salary<0:
        raise ValueError("薪水為正")
    print("薪水="+str(salary))

try:
    #f = open('myle.txt')
    Salary = eval(input("請輸入薪水:"))
    displaySalary(Salary)
except OSError as err:
    print("OS error: {0}".format(err)) 
except ValueError:
    print("錯誤:輸入薪水值為正") 
except:
    print("Unexpected error:", sys.exc_info()[0])