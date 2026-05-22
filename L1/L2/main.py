import cv2
import numpy as np

img = cv2.imread("L2/ash.png")
img1 = cv2.imread("L2/pikachu.png")

# # 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
# weighted_sum = cv2.addWeighted(img, 0.5, img1, 0.5, 0)
# cv2.imshow("weighted image", weighted_sum)

# # Subtraction of images
# sub = cv2.subtract(img, img1)
# cv2.imshow("Subtracted image", sub)

# # Image Resize
# cv2.imshow("Image Resize", img)

# resized = cv2.resize(img1, (1000, 1000))
# cv2.imshow("Reduced Image", resized)

# Erosion of an image, corners are trimmed in erosion
# img1 = cv2.imread("L2/pikachu.png", 1)

# Kernel is used for erosion as an input
# kernal = np.ones((7, 7), np.uint8)

# img = cv2.erode(img1, kernal)
# cv2.imshow("eroded image", img)

# # Blurring images
# # Gaussian Blur - used mostly in machine learning preprocessing steps
# # cv2.GuassianBlur(src, kernel_size, simgaX)
# guassian = cv2.GaussianBlur(img1, (2, 2), 0)
# cv2.imshow("Guassian Image", guassian)

# # Median Blur - used in digital processing preserves edges but removes noise
# median = cv2.medianBlur(img1, 5)
# cv2.imshow("Median Blur", median)

# # Bilateral Blur = only sharp edges are perserved here
# # cv2.bilate alfilter(src, d, sigmaColor, sigmaspace)
# bilateral = cv2.bilateralFilter(img1, 9, 75, 75)
# cv2.imshow("Bilateral Blur", bilateral)

cv2.waitKey()
cv2.destroyAllWindows()
