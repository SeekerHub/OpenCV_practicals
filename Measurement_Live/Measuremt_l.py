import cv2
import numpy as np
import utils

webcam = False
cap = cv2.VideoCapture(0)
img = cv2.imread('battery.jpg')
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread('battery.jpg')
        img = cv2.resize(img, (0, 0), None, 0.5, 0.5)

    img, conts = utils.getContours(img, showC=True, minArea=50000, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        print(biggest)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('image', img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
