# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:34:03 2021

@author: Zikantika
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('jurassic.jpg')


cv.imshow("Victoria Secrets", img)
k = cv.waitKey(0)



color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()