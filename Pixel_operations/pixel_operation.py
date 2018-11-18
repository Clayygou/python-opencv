import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
import time

time1 = time.time()
color = cv.imread("color.jpg")
ig = cv.imread("ig.jpg")

cv.namedWindow("ig",cv.WINDOW_NORMAL) 
cv.imshow('ig',ig) 

cv.namedWindow("color",cv.WINDOW_NORMAL)
cv.imshow('color',color)

color = color - 128
cv.namedWindow("color_2",cv.WINDOW_NORMAL)
cv.imshow('color_2',color)
cv.imwrite("color_2.jpg",color)

assert color.shape== ig.shape,"The shapes of the two images must be consistent"

def add_demo(ig,color):
	add_demo = cv.add(ig,color)
	cv.namedWindow("add_demo",cv.WINDOW_NORMAL)
	cv.imwrite('add_demo.jpg',add_demo)
	cv.imshow("add_demo",add_demo)
	return add_demo

def subtract_demo(ig,color):
	subtract_demo = cv.subtract(ig,color)
	cv.imwrite('subtract_demo.jpg',subtract_demo)
	cv.namedWindow("subtract_demo",cv.WINDOW_NORMAL)
	cv.imshow("subtract_demo",subtract_demo)
	return subtract_demo


def divide_demo(ig,color):
	divide_demo = cv.divide(ig,color)
	cv.imwrite('divide_demo.jpg',divide_demo)
	cv.namedWindow("divide_demo",cv.WINDOW_NORMAL)
	cv.imshow("divide_demo",divide_demo)
	return divide_demo

def multiply_demo(ig,color):
	multiply_demo = cv.multiply(ig,color)
	cv.imwrite("multiply_demo.jpg",multiply_demo)
	cv.namedWindow("multiply_demo",cv.WINDOW_NORMAL) 
	cv.imshow("multiply_demo",multiply_demo)
	return multiply_demo

def and_demo(ig,color):
	and_demo = cv.bitwise_and(ig,color)
	cv.imwrite('and_demo.jpg',and_demo)
	cv.namedWindow("and_demo",cv.WINDOW_NORMAL)
	cv.imshow("and_demo",and_demo)
	return and_demo

def or_demo(ig,color):
	or_demo = cv.bitwise_or(ig,color)
	cv.imwrite('or_demo.jpg',or_demo)
	cv.namedWindow("or_demo",cv.WINDOW_NORMAL)
	cv.imshow("or_demo",or_demo)
	return or_demo	

def not_demo(ig):
	not_demo = cv.bitwise_not(ig)
	cv.imwrite('not_demo.jpg',not_demo)
	cv.namedWindow("not_demo",cv.WINDOW_NORMAL)
	cv.imshow("not_demo",not_demo)
	return not_demo

def xor_demo(ig,color):
	xor_demo = cv.bitwise_xor(ig,color)
	cv.imwrite('xor_demo.jpg',xor_demo)
	cv.namedWindow("xor_demo",cv.WINDOW_NORMAL)
	cv.imshow("xor_demo",xor_demo)
	return xor_demo		
# Arithmetic operation
add_demo = add_demo(ig,color)
subtract_demo = subtract_demo(ig,color)
multiply_demo = multiply_demo(ig,color)
divide_demo = divide_demo(ig,color)
# bit operation  or logical operation
and_demo = and_demo(ig,color)
or_demo = or_demo(ig,color)
xor_demo = xor_demo(ig,color)
not_demo = not_demo(ig)

print('time : ',time.time()-time1)

for i in range(1):
    plt.subplot(241), plt.imshow(add_demo)
    plt.title('add_demo'), plt.xticks([]),plt.yticks([])
    plt.subplot(242), plt.imshow(subtract_demo)
    plt.title('subtract_demo'),plt.xticks([]),plt.yticks([])
    plt.subplot(243), plt.imshow(multiply_demo)
    plt.title('multiply_demo'), plt.xticks([]),plt.yticks([])
    plt.subplot(244), plt.imshow(divide_demo)
    plt.title('divide_demo'),plt.xticks([]),plt.yticks([])
    plt.subplot(245), plt.imshow(and_demo)
    plt.title('and_demo'), plt.xticks([]),plt.yticks([])
    plt.subplot(246), plt.imshow(or_demo)
    plt.title('or_demo'),plt.xticks([]),plt.yticks([])
    plt.subplot(247), plt.imshow(xor_demo)
    plt.title('xor_demo'), plt.xticks([]),plt.yticks([])
    plt.subplot(248), plt.imshow(not_demo)
    plt.title('not_demo'),plt.xticks([]),plt.yticks([])
    plt.show()

cv.waitKey(0) 
cv.destroyAllWindows()
