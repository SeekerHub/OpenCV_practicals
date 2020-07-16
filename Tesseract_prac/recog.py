import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv2.imread("hindi2.jpg")
img = cv2.resize(img, None, fx = 0.5, fy = 0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 4"
text = pytesseract.image_to_string(adaptive_thresh, lang="hin")
print(text)

cv2.imshow("IMG", gray)
cv2.imshow("adptive_threhlod", adaptive_thresh)
cv2.waitKey(0)