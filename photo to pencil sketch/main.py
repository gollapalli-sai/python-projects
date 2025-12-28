import cv2
import numpy as np

img = cv2.imread("6.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv = 255 - gray
blur = cv2.GaussianBlur(inv, (21, 21), 0)
sketch = cv2.divide(gray, 255 - blur, scale=256)

cv2.imwrite("mom-dad_sketch.png", sketch)
