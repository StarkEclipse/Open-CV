import cv2

img1 = cv2.imread("L4/Wem.jpg")
### Negative values fill shapes

## Draw a line
# startpoint = (0, 0)
# endpoint = (250, 250)
# color = 0, 255, 255
# thickness = 9
# img = cv2.line(img1, startpoint, endpoint, color, thickness)

## Draw a rectanlge
# startpoint = (50, 50)
# endpoint = (250, 250)
# color = 0, 255, 255
# thickness = -9
# img = cv2.rectangle(img1, startpoint, endpoint, color, thickness)

## Draw a circle
# centercoordinates = (120, 50)
# radius = 20
# color = (255, 0, 0)
# thickness = -2
# img = cv2.circle(img1, centercoordinates, radius, color, thickness)

font = cv2.FONT_HERSHEY_COMPLEX
org = 50, 50
fontScale = 1
color = 255, 15, 35
thickness = 4
img = cv2.putText(img1, "Hello", org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
