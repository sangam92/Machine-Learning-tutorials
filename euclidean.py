# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:18:33 2018

@author: sangam
"""

from scipy.spatial import distance
a = (1,2,3)
b = (4,5,6)
dst = distance.euclidean(a,b)
print(dst)