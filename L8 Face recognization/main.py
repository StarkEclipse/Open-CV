import cv2, sys, numpy, os

# haar_file = 'haarcascade_frontalface_default.xml'
# img = cv2.imread("/Users/onorenosenathanikhuoria/Desktop/Open CV/L8 Face recognization/images.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_cascade = cv2.CascadeClassifier(haar_file)
# faces = face_cascade.detectMultiScale(gray)
# print(faces)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.imshow("Face Detected", img)

# cv2.waitKey(0)

haar_file = 'haarcascade_frontalface_default.xml'
img = cv2.imread("/Users/onorenosenathanikhuoria/Desktop/Open CV/L8 Face recognization/images1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(haar_file)
faces = face_cascade.detectMultiScale(gray)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Face Detected", img)
cv2.waitKey(0)