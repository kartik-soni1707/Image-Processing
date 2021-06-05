import cv2 as cv
face_class=cv.CascadeClassifier('hc.xml')
eye_class=cv.CascadeClassifier('hc1.xml')
import numpy as np
from matplotlib import pyplot as plt
cap=cv.VideoCapture(0)
while(cap.isOpened()):
    _,img=cap.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=face_class.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        roi_b=gray[y:y+h,x:x+w]
        roi = img[y:y + h, x:x + w]
        eyes = eye_class.detectMultiScale(roi_b)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 3)
    cv.imshow('frame',img)
    if cv.waitKey(1)==ord('q'):
        break

cv.destroyAllWindows()