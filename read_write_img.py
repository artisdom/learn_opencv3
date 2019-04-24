#!/usr/bin/env python

import cv2
import numpy
# import numpy as np

img = numpy.zeros((3, 3), dtype = numpy.uint8)
print(img)
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)
print(img.shape)
