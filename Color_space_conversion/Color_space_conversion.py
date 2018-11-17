import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 


img = cv.imread("Morty.jpg")

cv.namedWindow("Color_conversion",cv.WINDOW_NORMAL)  
cv.imshow('Color_conversion',img) 
cv.waitKey(5000) 
cv.destroyAllWindows()

# Color_conversion
img2 = cv.cvtColor(img,cv.COLOR_BGR2HSV)
img3 = cv.cvtColor(img,cv.COLOR_BGR2YUV)
img4 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img5 = cv.cvtColor(img,cv.COLOR_BGR2YCrCb)

for i in range(1):
    plt.subplot(221), plt.imshow(img2)
    plt.title('HSV Image'), plt.xticks([]),plt.yticks([])
    plt.subplot(222), plt.imshow(img3)
    plt.title('YUV Image'),plt.xticks([]),plt.yticks([])
    plt.subplot(223), plt.imshow(img4)
    plt.title('GRAY Image'), plt.xticks([]),plt.yticks([])
    plt.subplot(224), plt.imshow(img5)
    plt.title('YCrCb Image'),plt.xticks([]),plt.yticks([])
    plt.show()

# find some color
lower_hsv = np.array([26,43,46])
upper_hsv = np.array([34,255,255])
mask = cv.inRange(img2, lower_hsv, upper_hsv)

img =  cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.namedWindow("inRange",cv.WINDOW_NORMAL)  
cv.imshow('inRange',mask) 
cv.imwrite('Find_yellow.jpg',mask)
cv.waitKey(5000) 
cv.destroyAllWindows()


# plt compare
plt.subplot(121), plt.imshow(img)
plt.title('origin Image'), plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(mask)
plt.title('Find_yellow Image'),plt.xticks([]),plt.yticks([])
plt.show()