import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread("hotWXZ.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.namedWindow("Contrast",cv.WINDOW_NORMAL)  
# cv.imshow('hotWXZ',img) 
M1,dev1 = cv.meanStdDev(img)
print('MEAN_1 :','\n',M1,'\n','Standard deviation',dev1)

img2 =  np.zeros([img.shape[0],img.shape[1],img.shape[2]],img.dtype)
assert (type(img2) == type(img)) & (img2.shape ==img.shape),"NO Matching"

Contrastimg = cv.addWeighted(img,1.5,img2,2,0)
brightness = cv.addWeighted(img,1,img2,2,40)
# cv.imshow("Contrast",Contrastimg)
M2,dev2 = cv.meanStdDev(Contrastimg)
print('MEAN_2 :','\n',M2,'\n','Standard deviation',dev2)

# plt show
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
Contrastimg = cv.cvtColor(Contrastimg,cv.COLOR_BGR2RGB)
brightness = cv.cvtColor(brightness,cv.COLOR_BGR2RGB)

plt.subplot(131), plt.imshow(img)
plt.title('hotWXZ'), plt.xticks([]),plt.yticks([])
plt.subplot(132), plt.imshow(Contrastimg)
plt.title('Contrastimg'),plt.xticks([]),plt.yticks([])
plt.subplot(133), plt.imshow(brightness)
plt.title('brightness'), plt.xticks([]),plt.yticks([])

plt.show()

# cv.waitKey(0) 
# cv.destroyAllWindows() 