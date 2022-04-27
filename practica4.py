import cv2
import numpy as np

imagen = 0*np.ones((400,600,3),dtype=np.uint8)

cv2.line(imagen, (0,0),(600,400),(255,0,0),4)
cv2.line(imagen, (300,0),(300,200),(255,100,255),10)

cv2.rectangle(imagen,(50,80),(200,200),(0,255,0),1)
cv2.rectangle(imagen,(300,80),(450,230),(124,35,162),-1)

cv2.putText(imagen,'Practica_4 usando OpenCV',(10,30),0,1,(255,0,0),2)

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

