import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def get_image_info(image):
	print(type(image))
	print(image.shape)
	print(image.size)
	print(image.dtype)
	print(np.array(image))

img2 = cv.imread('Rick and Morty.jpg')
img3 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)
img = cv.imread('Rick and Morty.jpg',0)
 
cv.namedWindow("Rick and Morty", cv.WINDOW_NORMAL)
cv.imshow("Rick and Morty",img)

get_image_info(img)

k = cv.waitKey(0)
if k == ord("s"):
	cv.imwrite('Rick and Morty GRAY.jpg',img)
if k == 27:
	cv.destroyAllWindows()

plt.subplot(311), plt.imshow(img,cmap= "gray")
plt.title('GRAY Image'), plt.xticks([]),plt.yticks([])
plt.subplot(312), plt.imshow(img2)
plt.title('BGR Image'),plt.xticks([]),plt.yticks([])
plt.subplot(313), plt.imshow(img3)
plt.title('RGB Image'),plt.xticks([]),plt.yticks([])
plt.show()