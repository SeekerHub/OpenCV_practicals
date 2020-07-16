import cv2
import numpy as np


def getContours(img, cThr=[100, 100], showC=False, minArea=1000, filter=0, draw = False):
    imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgB = cv2.GaussianBlur(imgG, (5, 5), 1)
    imgC = cv2.Canny(imgB, cThr[0], cThr[1])
    kernel = np.ones((5, 5))
    imgD = cv2.dilate(imgC, kernel, iterations=3)
    imgTh = cv2.erode(imgD, kernel, iterations=2)
    if showC:
        cv2.imshow('Canny', imgTh)

    contours, hierarchy = cv2.findContours(imgTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    final = []
    for cnt in contours:
        print('-------------------------')
        print(cnt)
        print('-------------------------')
        area = cv2.contourArea(cnt)
        if area > minArea:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            bbox = cv2.boundingRect(approx)
            if filter > 0:
                if len(approx) == filter:
                    final.append(len(approx), area, approx, bbox, cnt)
            else:
                final.append([len(approx), area, approx, bbox, cnt])
    """Sorting the contours points based on area"""
    final = sorted(final, key=lambda x: x[1], reverse=True)
    if draw:
        for cnt in final:
            cv2.drawContours(img, cnt[4], -1, (0, 0, 255), 3)

    return img, final


def warpImg(img, poinnts, w, h):
    pass
