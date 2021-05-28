import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('5.jpg')
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh=cv.threshold(img1,200,255,cv.THRESH_BINARY)
contours,_=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
for c in contours:
    aprx=cv.approxPolyDP(c,0.01*cv.arcLength(c,True),True)
    cv.drawContours(img,[aprx],0,(0,0,0),5)
    x=aprx.ravel()[0]+10
    y = aprx.ravel()[1]-50
    if len(aprx)==3:
        cv.putText(img,'Triangle',(x,y),cv.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
    elif len(aprx)==4:
        cv.putText(img,'Rectangle',(x,y),cv.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
    elif len(aprx)==5:
        cv.putText(img,'Pentagon',(x,y),cv.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
    elif len(aprx)==10:
        cv.putText(img,'Star',(x,y),cv.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
    else:
        cv.putText(img,'Circle',(x,y),cv.FONT_HERSHEY_DUPLEX,2,(0,0,0),2)
img=cv.resize(img,(512,512))
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()