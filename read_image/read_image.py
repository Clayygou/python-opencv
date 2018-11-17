import cv2 as cv
import numpy as np


def get_image_info(image):
	print(type(image))
	print(image.shape)
	print(image.size)
	print(image.dtype)
	print(np.array(image))


img = cv.imread('Rick and Morty.jpg',0)
 
cv.namedWindow("Rick and Morty", cv.WINDOW_NORMAL)
cv.imshow("Rick and Morty",img)
get_image_info(img)

k = cv.waitKey(0)
if k == ord("s"):
	cv.imwrite('Rick and Morty GRAY.jpg',img)
if k == 27:
	cv.destroyAllWindows()

