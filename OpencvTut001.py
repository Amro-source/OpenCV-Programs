# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:02:53 2021

@author: Zikantika
"""

import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("dog.1048.jpg"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)


