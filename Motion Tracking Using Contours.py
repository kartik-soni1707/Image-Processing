import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
cap=cv.VideoCapture('11.mp4')
ret,frame1=cap.read()
ret,frame2=cap.read()
while cap.isOpened():
    diff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilated=cv.dilate(thresh,None,iterations=3)
    contours,_=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x,y,w,h)=cv.boundingRect(c)
        X=cv.contourArea(c)
        if (X<2700 ):
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow('frame',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    k=cv.waitKey(1)
    if k==27:
        break
cv.waitKey(0)
cv.destroyAllWindows()