import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import copy

def nothing():
	pass

roi = [100,100]
cv.namedWindow("Fourpeople",cv.WINDOW_NORMAL)
Fourpeople =  cv.imread('Fourpeople.jpg')
# cv.imshow("Fourpeople",Fourpeople)
# print(Fourpeople.shape)
cv.createTrackbar('Y','Fourpeople',0,Fourpeople.shape[0]-roi[0],nothing)
cv.createTrackbar('X','Fourpeople',0,Fourpeople.shape[1]-roi[1],nothing)

switch='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'Fourpeople',0,1,nothing)
while(True):
	# Fourpeople =  cv.imread('Fourpeople.jpg')
	y = cv.getTrackbarPos('Y','Fourpeople')
	x = cv.getTrackbarPos('X','Fourpeople')
	s = cv.getTrackbarPos(switch,'Fourpeople')

	if s == 0:
		cv.imshow("Fourpeople",Fourpeople)
	else:
		# Fourpeople2 = Fourpeople.copy()
		# # Fourpeople2 = copy.deepcopy(Fourpeople)
		# r1 = cv.cvtColor(Fourpeople2[y:(y+roi[0]),x:(x+roi[1])],cv.COLOR_BGR2GRAY)
		# r2 = cv.cvtColor(r1,cv.COLOR_GRAY2BGR)
		# Fourpeople[y:(y+roi[0]),x:(x+roi[1])] = r2
		Fourpeople[y:(y+roi[0]),x:(x+roi[1])] = 0
		cv.imshow("Fourpeople",Fourpeople)
	if cv.waitKey(1) ==27:
		break
cv.destroyAllWindows()

# while(True):
# 	cv.imshow("Fourpeople",Fourpeople)
# 	if cv.waitKey(1) == 27:
# 		break
# 	s = cv.getTrackbarPos(switch,'Fourpeople')
# 	r=cv.getTrackbarPos('R','Fourpeople')
# 	g=cv.getTrackbarPos('G','Fourpeople')
# 	b=cv.getTrackbarPos('B','Fourpeople')

# 	if s == 0:
# 		Fourpeople[:] = 0
# 	else:
# 		# Fourpeople[:] = [b,g,r]
# 		Fourpeople2 = Fourpeople.copy()
# 		r1 = cv.cvtColor(Fourpeople2[r:(r+roi[0]),g:(g+roi[1])],cv.COLOR_BGR2GRAY)
# 		cv.imshow('r1',r1)
# 		r2 = cv.cvtColor(r1,cv.COLOR_GRAY2BGR)
# 		cv.imshow('r2',r2)
# 		Fourpeople[r:(r+roi[0]),g:(g+roi[1])] = r2


import matplotlib.pyplot as plt
img1 = cv.imread("1.png")
img2 = cv.imread("2.png")
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(img1)
plt.title('1.png'), plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(img2)
plt.title('2.png'),plt.xticks([]),plt.yticks([])
plt.show()



# cv.namedWindow("a",cv.WINDOW_NORMAL)
# imga = cv.imread('Fourpeople,jpg')
# print(imga.shape)
# roi = [100,100]
# def roix(valuex):
# 	valuex = int(valuex)
# 	b = a.copy()
# 	valuey = int(cv.getTrackbarPos('y','a')) 
# 	r1 = cv.cvtColor(a[valuey:(valuey+roi[0]),valuex:(valuex+roi[1])],cv.COLOR_BGR2GRAY)
# 	r2 = cv.cvtColor(r1,cv.COLOR_GRAY2BGR)
# 	b[valuey:(valuey+roi[0]),valuex:(valuex+roi[1])] = r2
# 	cv.imshow("a",b)
# def roiy(valuey):
# 	valuey = int(valuey)
# 	b = a.copy()
# 	valuex = int(cv.getTrackbarPos('x','a')) 
# 	r1 = cv.cvtColor(a[valuey:(valuey+roi[0]),valuex:(valuex+roi[1])],cv.COLOR_BGR2GRAY)
# 	r2 = cv.cvtColor(r1,cv.COLOR_GRAY2BGR)
# 	b[valuey:(valuey+roi[0]),valuex:(valuex+roi[1])] = r2
# 	cv.imshow("a",b)

# cv.createTrackbar('x','a',0,a.shape[1]-roi[1],roix)
# cv.createTrackbar('y','a',0,a.shape[0]-roi[0],roiy)