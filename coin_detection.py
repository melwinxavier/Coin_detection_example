import cv2 as cv
import numpy as np

# Read image.
img = cv.imread('coin1.jpg')

#Resizing image
rezimg = cv.resize(img,(800,500))
rezimg.shape

#Blank image
blank = np.zeros(rezimg.shape[:2], dtype='uint8')

#Convert to grayscale
gray = cv.cvtColor(rezimg,cv.COLOR_BGR2GRAY)

#Using blur
gauss = cv.GaussianBlur(gray,(7,7),0)

output = rezimg.copy()

#Apply Hough transform on the blurred image
all_circs = cv.HoughCircles(gauss,cv.HOUGH_GRADIENT,0.5,60,param1=200,param2=30,minRadius=0,maxRadius=300)
all_circs_rounded = np.uint16(np.around(all_circs))

#Draw circles
for (x,y,r) in all_circs_rounded[0, :]:
    cv.circle(output,(x,y),r,(0,255,0),2)
    mask = cv.circle(blank,(x,y),r,255,-1)
    masked = cv.bitwise_and(output,output,mask=mask)

cv.imshow('Masked',masked)
cv.imshow('Coins',output)
cv.waitKey(0)
cv.destroyAllWindows()