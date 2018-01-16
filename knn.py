# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:26:36 2017

@author: sangam
"""

from sklearn.neighbors import KNeighborsClassifier


a = [[1],[2],[3],[4],[8],[30],[27],[34],[65],[43]]

b =  [0,0,0,0,0,0,1,1,1,1]

knn =KNeighborsClassifier(n_neighbors=3)

knn.fit(a,b)

print(knn.predict(22))

