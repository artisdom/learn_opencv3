#!/usr/bin/env python

import cv2

grayImage = cv2.imread('pixhawk.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('pixhawk_gray.png', grayImage)