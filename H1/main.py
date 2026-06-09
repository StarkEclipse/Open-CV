import cv2

img = cv2.imread("H1/flower.jpg")
cv2.imshow("Original Image", img)
print(img)

cv2.waitKey()
cv2.destroyAllWindows()