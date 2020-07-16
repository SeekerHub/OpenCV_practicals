import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/sudoku.png', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
# """Threshold will remain same using trunc"""
_, th3 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
# """when the pixel value is......................"""

"""Adoptive Thresholding --> used for images having diferent illumination """
th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th5 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

images = [img, th1, th2, th3, th4, th5]
for i in range(6):
    # 2 rows and 3 columns
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()