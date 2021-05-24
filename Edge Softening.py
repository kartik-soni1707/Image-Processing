import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img =cv.imread('lena.jpg',1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.uint8)/25
res=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))
gblur=cv.GaussianBlur(img,(5,5),0)
median=cv.medianBlur(img,5)
biLateral=cv.bilateralFilter(img,9,75,75)

images=[img,res,blur,gblur,median,biLateral]
x=len(images)
for i in range(x):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i]), plt.xticks([]), plt.yticks([])
    plt.show()