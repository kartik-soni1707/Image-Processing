import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img =cv.imread('b.jpg',cv.IMREAD_GRAYSCALE)
lap=cv.Laplacian(img,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
soblX=cv.Sobel(img,cv.CV_64F,1,0)
soblX=np.uint8(np.absolute(soblX))
soblY=cv.Sobel(img,cv.CV_64F,0,1)
soblY=np.uint8(np.absolute(soblY))
comb=cv.bitwise_or(soblX,soblY)
cny=cv.Canny(img,50,200)
images=[img,lap,soblX,soblY,comb,cny]
x=len(images)
for i in range(x):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray'), plt.xticks([]), plt.yticks([])
    plt.show()