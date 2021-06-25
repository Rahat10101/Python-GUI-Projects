import cv2

temp = cv2.imread("2.jpg" , cv2.IMREAD_GRAYSCALE)

th = 150

bin_img = cv2.threshold(temp , th , 200 , cv2.THRESH_BINARY)[1]

cv2.imwrite("Sketch2.jpg",bin_img)

