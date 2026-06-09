import cv2


bakugo = cv2.imread("bakugo.jpg")
deku = cv2.imread("deku.jpg")

print(bakugo.shape)
print(deku.shape)
deku = cv2.resize(deku, (bakugo.shape[1], bakugo.shape[0]))
# blend1 = cv2.addWeighted(bakugo, 0.7, deku, 0.3, 0)

blend2 = cv2.addWeighted(bakugo, 0.5, deku, 0.5, 0)


# blend3 = cv2.addWeighted(bakugo, 0.2, deku, 0.8, 0)


# cv2.imshow("e", blend1)
cv2.imshow("e", blend2)
# cv2.imshow("e", blend3)

cv2.waitKey(0)
cv2.destroyAllWindows()
