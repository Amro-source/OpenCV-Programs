# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:52:29 2021

@author: Zikantika
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('f91567483d644cf295a007bd042171d7.jpg')


blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


cv.imshow("Victoria Secrets", img)
k = cv.waitKey(0)



cv.imshow("Victoria Secrets Blurred", blur)
k = cv.waitKey(0)