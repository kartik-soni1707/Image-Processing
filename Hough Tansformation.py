import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('40.jpg')
img=cv.resize(img,(512,512))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edge=cv.Canny(gray,150,250,apertureSize=3)
lines= cv.HoughLinesP(edge,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for l in lines:
    x1,y1,x2,y2=l[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),5)
cv.imshow('heyy',img)
cv.imshow('ed',edge)
cv.waitKey(0)
cv.destroyAllWindows()
