import cv2 as cv
import numpy as np
def nth(x):
    pass
cap=cv.VideoCapture(0)
cv.namedWindow('Tracking')
cv.resizeWindow('Tracking',512,256)
cv.createTrackbar('LH','Tracking',0,255,nth)
cv.createTrackbar('LS','Tracking',0,255,nth)
cv.createTrackbar('LV','Tracking',0,255,nth)
cv.createTrackbar('UH','Tracking',255,255,nth)
cv.createTrackbar('US','Tracking',255,255,nth)
cv.createTrackbar('UV','Tracking',255,255,nth)
while(1):
    _,img=cap.read()
    img=cv.resize(img,(512,512))
    cv.imshow('image',img)
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lh=cv.getTrackbarPos('LH','Tracking')
    ls = cv.getTrackbarPos('LS', 'Tracking')
    lv = cv.getTrackbarPos('LV', 'Tracking')
    uh = cv.getTrackbarPos('UH', 'Tracking')
    us = cv.getTrackbarPos('US', 'Tracking')
    uv = cv.getTrackbarPos('UV', 'Tracking')
    l_b=np.array([lh,ls,lv])
    u_b = np.array([uh,us,uv])
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('res',res)
    cv.imshow('image', img)
    cv.imshow('mask', mask)
    k=cv.waitKey(1)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()