import cv2 as cv
import numpy as np

img=cv.imread('ll.jpg')
cv.imshow('frame',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv.cornerHarris(gray,2,3,0)
dst=cv.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('fr',img)
cv.waitKey(0)
cv.destroyAllWindows()
