import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lab2/Fig0310.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

fig = plt.figure();
x = np.arange(256)
xp = [0, 64, 192, 255]
fp = [0, 16, 240, 255]
table = np.interp(x, xp, fp).astype('uint8')
img1 = cv2.LUT(img, table)

pic_subplot = plt.subplot(3,2,1)
pic_subplot.imshow(img1)
pic_subplot = plt.subplot(3,2,2)
pic_subplot.plot(xp,fp)

xp = [0, 90, 192, 255]
fp = [0, 32, 150, 255]
table = np.interp(x, xp, fp).astype('uint8')
img2 = cv2.LUT(img, table)

pic_subplot = plt.subplot(3,2,3)
pic_subplot.imshow(img2)
pic_subplot = plt.subplot(3,2,4)
pic_subplot.plot(xp,fp)

xp = [0, 115, 128, 100, 255]
fp = [0,  0,  128, 255, 255]
table = np.interp(x, xp, fp).astype('uint8')
img3 = cv2.LUT(img, table)

pic_subplot = plt.subplot(3,2,5)
pic_subplot.imshow(img3)
pic_subplot = plt.subplot(3,2,6)
pic_subplot.plot(xp,fp)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows() 