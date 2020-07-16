import cv2
import numpy as np

img = cv2.imread('C:/Users/Droid/Pictures/vegito.jpeg')
# img = cv2.resize(img, (512, 512))


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
