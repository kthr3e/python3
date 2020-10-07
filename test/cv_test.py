import cv2
bgr = cv2.imread('fruit.jpg')
cv2.imshow("fruit", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
