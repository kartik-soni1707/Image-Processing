import cv2 as cv
import numpy as np
def nth(x):
    print(x)
cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,nth)
cv.createTrackbar('G','image',0,255,nth)
cv.createTrackbar('R','image',0,255,nth)
img=np.zeros((450,512,3),np.uint8)
while(1):
    cv.imshow('image',img)
    b=cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    img[:]=[b,g,r]
    k=cv.waitKey(1)
    if k==27:
        break

cv.destroyAllWindows()