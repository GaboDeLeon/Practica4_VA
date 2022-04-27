import cv2
import numpy as np

img_raw = cv2.imread('imagen1.jpg')
r = cv2.selectROI(img_raw)
print(r)
roi_cropped = img_raw[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow("ROI", roi_cropped)
cv2.imwrite("crop.jpeg",roi_cropped)
cv2.waitKey(0)
