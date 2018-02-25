#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:50:09 2017

@author: justinwu
"""

from collections import deque
queue = deque(['阿呆','Eric','John','Michael','小寶','小文'])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)
