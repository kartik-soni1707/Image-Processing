import cv2 as cv
import numpy as np

def func(event,x,y,flags,params):
    if(event==cv.EVENT_LBUTTONDOWN):
        cv.circle(img,(x,y),5,(0,255,0),-1)
        b = img[x , y ,0]
        g = img[x, y, 1]
        r = img[x, y, 2]
        img1=np.zeros((512,512,3),np.uint8)
        img1[:]=[b,g,r]
        cv.imshow('image1', img1)
        cv.imshow('image',img)

img = cv.imread('lena.jpg')

points=[]
cv.imshow('image',img)
cv.setMouseCallback('image',func)
cv.waitKey(0)
cv.destroyAllWindows()