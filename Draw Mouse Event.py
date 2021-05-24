import cv2 as cv
import numpy as np

def func(event,x,y,flags,params):
    if(event==cv.EVENT_LBUTTONDOWN):
        cv.circle(img,(x,y),5,(0,255,0),-1)
        points.append((x,y))
        if(len(points)>=2):
            cv.line(img,points[-1],points[-2],(255,0,0),3)
        cv.imshow('image',img)
    if (event == cv.EVENT_RBUTTONDOWN):
        points.clear()
img = cv.imread('b.jpg')
img=cv.resize(img,(512,512))
points=[]
cv.imshow('image',img)
cv.setMouseCallback('image',func)
cv.waitKey(0)
cv.destroyAllWindows()