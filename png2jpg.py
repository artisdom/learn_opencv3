#!/usr/bin/env python

import cv2
import numpy

image = cv2.imread("pixhawk.png")
cv2.imwrite('pixhawk.jpg', image)