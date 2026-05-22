import cv2
# img = cv2.imread("L1/pika.png")

# # cv2.imshow("Final Render", img)
# # # print(img)

# # gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# # cv2.imshow("grayscale", gray_img)
# # print(gray_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # #cv2.IMREAD_COLOR (1) => Specify to load the image in color
# # #cv2.IMREAD_GRAYSCALE (0) =>
# # Specify to load the image in grayscale / black & white
# # #cv2.IMREAD_UNCHANGED (-1) =>
# # Specify to load the image unchanged
img1 = cv2.imread("L1/pika.png", 0)
cv2.imshow("Final Render", img1)
cv2.imwrite("pikablackandwhite.png", img1)
print("Successfully saved")
cv2.waitKey(delay = 5000)
cv2.destroyAllWindows()