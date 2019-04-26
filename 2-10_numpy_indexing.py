#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('pixhawk.png')
img[:, :, 1] = 0
cv2.imshow('img', img)
cv2.waitKey(0)
