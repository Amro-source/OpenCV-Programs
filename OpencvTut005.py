# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:31:24 2021

@author: Zikantika
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('f91567483d644cf295a007bd042171d7.jpg')


median = cv.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()



blur = cv.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()



