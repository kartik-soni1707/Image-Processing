import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def region(img,verices):
    mask=np.zeros_like(img)
    match_maskcolor=255
    cv.fillPoly(mask,verices,match_maskcolor)
    mskimg=cv.bitwise_and(img,mask)
    return mskimg
#img=cv.imread('40.jpg')
#img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
def proc(img):
    h=img.shape[0]
    w=img.shape[1]
    roi=[
        (120,512),(520,415),(1000,773)
    ]
    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    edge=cv.Canny(gray,200,210,apertureSize=3)
    cimg=region(edge,
              np.array([roi],np.int32)
               )
    lines=cv.HoughLinesP(cimg,
                         2,
                         np.pi/60,
                         60,
                         None,
                         minLineLength=40,maxLineGap=100 )
    for l in lines:
        x1,y1,x2,y2=l[0]
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),3)
    return img

cap=cv.VideoCapture('D.mp4')
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv.resize(frame,(1024,800))
    # plt.imshow(frame)
    # plt.show()
    frame=proc(frame)
    cv.imshow("fr",frame)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()