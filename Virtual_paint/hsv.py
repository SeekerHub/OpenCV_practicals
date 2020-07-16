import cv2
import numpy as np


def nothing(x):
    pass


# cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread('data/smarties.png')
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([20, 100, 100])
    high_red = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_red, high_red)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    #
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame)

    cv2.imshow("Red", blue)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
