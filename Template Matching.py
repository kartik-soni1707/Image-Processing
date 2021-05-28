import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('lena.jpg')
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
mtch=cv.imread('l1.jpg',0)
res=cv.matchTemplate(grey,mtch,cv.TM_CCORR_NORMED)

threshold=0.99
loc=np.where(res >=threshold)
print(loc)
w,h=mtch.shape[::-1]
# cv.rectangle(img, )
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),2)
cv.imshow('heyy',img)
cv.waitKey(0)
cv.destroyAllWindows()
