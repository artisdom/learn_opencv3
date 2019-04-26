#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread('pixhawk.png')
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
