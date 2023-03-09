import cv2
import numpy

img = cv2.imread("your image")
print("Original dimension",img.shape)

dim0 = (640,480)
dim1 = (320,240)
dim2 = (64,48)
dim3 = (32,24)

imgResized0 = cv2.resize(img, dim0, interpolation = cv2.INTER_AREA)
imgResized1 = cv2.resize(img, dim1, interpolation = cv2.INTER_AREA)
imgResized2 = cv2.resize(img, dim2, interpolation = cv2.INTER_AREA)
imgResized3 = cv2.resize(img, dim3, interpolation = cv2.INTER_AREA)

cv2.imshow("resized0",imgResized0)
cv2.imshow("resized1",imgResized1)
cv2.imshow("resized2",imgResized2)
cv2.imshow("resized3",imgResized3)
#
#
# ##SECOND TASK
#
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imgLab = cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
imgYcbcr = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

blue,green,red = cv2.split(img)
h,s,v = cv2.split(imgHSV)
y,cb,cr = cv2.split(imgYcbcr)
l,a,b = cv2.split(imgLab)

splitRGB = numpy.hstack((red,green,blue))
splitHSV = numpy.hstack((h,s,v))
splitYcbcr = numpy.hstack((y,cb,cr))
splitLab = numpy.hstack((l,a,b))

cv2.imshow("Seperated RGB channel",splitRGB)
cv2.imshow("Seperated HSV channel",splitHSV)
cv2.imshow("Seperated YCbCr channel",splitYcbcr)
cv2.imshow("Seperated Lab channel",splitLab)
cv2.imshow("Gray image",imgGray)

cv2.waitKey(0)
