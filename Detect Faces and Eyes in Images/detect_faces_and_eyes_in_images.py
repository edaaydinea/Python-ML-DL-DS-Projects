"""
author = "Eda AYDIN"

#1: Detect One Face
#2: Detect Multiple Faces
#3: Detect Eyes and Face
#4: Detect Multiple Eyes and Faces
#5: Detect Faces in Video Playform
"""

import numpy as np
import cv2

# 1: DETECT ONE SPACE

# By using Trudeau.jpg
image_c = cv2.imread("Trudeau.jpg")
cv2.imshow("Trudeau Face in Color", image_c)
cv2.waitKey()
cv2.destroyAllWindows()

image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

cv2.imshow("Trudeau Face in Grayscale", image_g)
cv2.waitKey()
cv2.destroyAllWindows()

# By using Scientist.jpg

image_c_of_scientists = cv2.imread("Scientists.jpg")
cv2.imshow("Scientist Face in Color", image_c_of_scientists)
cv2.waitKey()
cv2.destroyAllWindows()

image_g_of_scientists = cv2.cvtColor(image_c_of_scientists, cv2.COLOR_BGR2GRAY)

cv2.imshow("Scientist Face in Grayscale", image_g_of_scientists)
cv2.waitKey()
cv2.destroyAllWindows()

# By using images.jpg

images = cv2.imread("images.jpg")
cv2.imshow("Multiple Faces in Color", images)
cv2.waitKey()
cv2.destroyAllWindows()

# By using Scientist_1.jpg
image_scientists = cv2.imread("Scientist_1.jpg")
cv2.imshow("Multiple Face in Grayscale", image_scientists)
cv2.waitKey()
cv2.destroyAllWindows()

# Face detection by using Trudeau.jpg
face_detection = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
faces = face_detection.detectMultiScale(image_c, 1.1, 5)

"""
CascadeClassifier.detectMultiScale(input image, Scale Factor, Min Neighbours)

Scale Factor: 
- Specifies how much reduction takes place in the image size each time during pyramiding process.
- For 1.2, it means image is reduced by 20% each time it's scaled.

Min Neighbours:
- Parameter specifying how many neighbours each candidate rectangle should have to retain it.
- set it to a number between 3 and 6
- This parameter will affect the quality of the detected faces.
- Higher value results in less detections but with higher quality.
"""

print(faces)
"""
[X,Y,width,height]
When we run the code, the faces array will be shown. 
The first two numbers are the coordinates of the top left rectangle index or corner.
So what happened is the detect faces will going to detect a rectangle around the face. 
Last two numbers are the dimensions of the width and height of my rectangle.
"""

x = faces[:, 0]
y = faces[:, 1]
w = faces[:, 2]
h = faces[:, 3]

cv2.rectangle(image_c, (x, y), (x + w, y + h), (0, 255, 255), 3)

"""
(0,255,255) which means that the color of rectangle will be yellow. 
3 which means that the thickness of rectangle. If we increase the number, the thickness of rectangle will increase. 
"""
cv2.imshow("Single Face Detection", image_c)
cv2.waitKey()
cv2.destroyAllWindows()

# 2 : DETECT MULTIPLE FACES

multiple_faces = face_detection.detectMultiScale(image_c_of_scientists, 1.1, 7)

for (x, y, w, h) in multiple_faces:
    cv2.rectangle(image_c_of_scientists, (x, y), (x + w, y + h), (0, 255, 255), 3)
    cv2.imshow("Multiple Face Detection", image_c_of_scientists)
    cv2.waitKey()

cv2.destroyAllWindows()

# 3 : DETECT EYES AND FACES

face_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")
eye_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

face = face_classifier.detectMultiScale(image_c, 1.2, 5)

for (x, y, w, h) in face:
    cv2.rectangle(image_c, (x, y), (x + w, y + h), (0, 255, 255), 3)
    cv2.imshow("Trudeau Face and Eye Detection in Color", image_c)
    cv2.waitKey()

    # Select the face region
    face_region = image_c[y:y + h, x:x + w]
    eye = eye_classifier.detectMultiScale(face_region)

    for (eye_x, eye_y, eye_w, eye_h) in eye:
        cv2.rectangle(image_c, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 255), 3)
        cv2.imshow("Trudeau Face and Eye Detection in Color", image_c)
        cv2.waitKey()
cv2.destroyAllWindows()

# 4: DETECT EYES IN MORE THAN ONE FACE

multiple_faces_eyes = face_classifier.detectMultiScale(images, 1.2,7)

for (x, y, w, h) in multiple_faces_eyes:
    cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 255), 3)
    cv2.imshow("Faces and Eyes Detection in Color", images)
    cv2.waitKey()

    # Select the face region
    face_regions = images[y:y + h, x:x + w]
    multiple_eyes = eye_classifier.detectMultiScale(face_regions)

    for (eye_x, eye_y, eye_w, eye_h) in multiple_eyes:
        cv2.rectangle(images, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 255), 3)
        cv2.imshow("Scientist Faces and Eyes Detection in Color", images)
        cv2.waitKey()
cv2.destroyAllWindows()


i