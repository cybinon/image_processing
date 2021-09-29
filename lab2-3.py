import cv2
import numpy as np

img = cv2.imread('Fig0310.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x = np.arange(256)
xp = [0, 64, 192, 255]
fp = [0, 16, 240, 255]
table = np.interp(x, xp, fp).astype('uint8')
img1 = cv2.LUT(img, table)
cv2.imshow("Output1", img1)

xp = [0, 90, 192, 255]
fp = [0, 32, 150, 255]
table = np.interp(x, xp, fp).astype('uint8')
img2 = cv2.LUT(img, table)
cv2.imshow("Output2", img2)

xp = [0, 115, 128, 100, 255]
fp = [0,  0,  128, 255, 255]
table = np.interp(x, xp, fp).astype('uint8')
img3 = cv2.LUT(img, table)
cv2.imshow("Output3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows() 