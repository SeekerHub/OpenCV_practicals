import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/lena.jpg', -1)
cv2.imshow('Image', img)
"""Opencv read the image in the BGR method and matplotlib reads it in RBG format tahts why we get the difference"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()