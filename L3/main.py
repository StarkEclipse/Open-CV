import cv2

## Grayscaling of an imagwe read as color
img1 = cv2.imread("/Users/onorenosenathanikhuoria/Desktop/Open CV/L3/deku.jpg")
# cv2.imshow("Image", img1)

# gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscaled image", gray_img)

## Using averaging oif pixel method to grayscale the image
# (row, col) = img1.shape[:2]
# for i in range(row):
#     for j in range(col):
#         gray_value = int(sum(img1[i, j]) / 3)
#         img1[i, j] = [gray_value, gray_value, gray_value]
# cv2.imshow("Grayscaled with pixel", img1)

## Rotating Images
# (height, width) = img1.shape[:2]
# center = (width // 2, height // 2)
# angle = 270
# scale = 1.0
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
# rotatedimg = cv2.warpAffine(img1, rotation_matrix, (width, height))
# cv2.imshow("Og image", img1)
# cv2.imshow("Rotated image", rotatedimg)

## Edge detection in an image
# gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
# edges = cv2.Canny(blurred_img, threshold1=300, threshold2=400)
# cv2.imshow("Original Image", img1)
# cv2.imshow("Edge detection", edges)

hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)


cv2.waitKey(0)
cv2.destroyAllWindows()


