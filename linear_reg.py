# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:19:00 2018

@author: sangam
"""
import matplotlib.pyplot as plt
from sklearn import linear_model


x_train= [[2],[4],[6],[8],[10],[12],[14],[16]]

y_train =[[4],[6],[7],[10],[12],[15],[17],[19]]

regr = linear_model.LinearRegression()


regr.fit(x_train,y_train)

y_output =regr.predict(22)


print(regr.predict(22))

plt.scatter(x_train,y_train,color="black")

#plt.plot(x_train,y_train,color="green")