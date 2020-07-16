import cv2
import numpy as np
from matplotlib import pyplot as plt

mask = cv2.imread('data/j.png', cv2.IMREAD_GRAYSCALE)
# _, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)
kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=1)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)


images = [mask, dilation, erosion, opening, closing, mg]
for i in range(6):
    # 2 rows and 3 columns
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
