# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:14:51 2021

@author: Zikantika
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img =cv.imread('f91567483d644cf295a007bd042171d7.jpg')

cv.imshow("Victoria Secrets", img)
k = cv.waitKey(0)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

cv.imshow("Victoria Secrets", dst)
k = cv.waitKey(0)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()