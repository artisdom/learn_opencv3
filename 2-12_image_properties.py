#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('pixhawk.png')
print(img.shape)
print(img.size)
print(img.dtype)