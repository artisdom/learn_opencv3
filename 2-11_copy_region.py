#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('pixhawk.png')
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi
cv2.imshow('img', img)
cv2.waitKey(0)
