import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
mask =cv.imread('1.jpg',0)
#_,mask=cv.threshold(img,200,255,cv.THRESH_BINARY)
kernel=np.ones((5,5),np.uint8)
dil=cv.dilate(mask,kernel)
ero=cv.erode(mask,kernel)
open=cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
close=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
grad=cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel)
th=cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel)
images=[mask,dil,ero,open,close,grad,th]
x=len(images)
for i in range(x):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray'), plt.xticks([]), plt.yticks([])
    plt.show()
