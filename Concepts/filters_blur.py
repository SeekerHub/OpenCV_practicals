import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/water.png', cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)

median = cv2.medianBlur(img, 5)  # to be used when you have salt and paper noise in the filter

"""
LPF         ---> helps in removing the noise and bluring the image
HPF         ---> helps to detect edges
Gaussian F  ---> using different weight kernel in both x and y direction
bilateral F ---> helps in noise removal keeping the  edges sharp
"""
titles = ['image', '2D conv', 'blur', 'gaussian blur', 'median']
images = [img, dst, blur, gblur, median]

for i in range(5):
    # 2 rows and 3 columns
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
