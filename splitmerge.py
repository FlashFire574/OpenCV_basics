import cv2 as cv
import numpy as np
img= cv.imread('cat1.jpg')
cv.imshow('Cat1',img)
blank=np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

merged=cv.merge([b,g,r])
cv.imshow("Merged Image",merged)
cv.waitKey(0)