import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./lab2/dasgal1.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()

bit7 = (img/2)*2
plot = plt.subplot(2,4,1).imshow(bit7)

bit6 = (img/4)*4
plot = plt.subplot(2,4,2).imshow(bit6)

bit5 = (img/8)*8
plot = plt.subplot(2,4,3).imshow(bit5)

bit4 = (img/16)*16
plot = plt.subplot(2,4,4).imshow(bit4)

bit3 = (img/32)*32
plot = plt.subplot(2,4,5).imshow(bit3)

bit2 = (img/64)*64
plot = plt.subplot(2,4,6).imshow(bit2)

bit1 = (img/128)*128
plot = plt.subplot(2,4,7).imshow(bit1)

output = img;
for i in range(len(img)):
  for j in range(len(img[0])):
    if img[i][j]>100:
      output[i][j] = 255
    else:
      output[i][j] = 0

plot = plt.subplot(2,4,8).imshow(output)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()