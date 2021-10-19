import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./lab2/kidnay.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 = img
img2 = img

row = len(img)
col = len(img[0])

plt.figure()
plot = plt.subplot(1,3,1).imshow(img, cmap="gray")

for i in range(row):
  for j in range(col):
    if img1[i][j] > 150:
      img1[i][j] = 255;
    else:
      img1[i][j] = 0;
plot = plt.subplot(1,3,2).imshow(img1, cmap="gray")

for i in range(row):
  for j in range(col):
    if img2[i][j] > 150:
      img2[i][j] = 240
    elif img2[i][j]>70 and img2[i][j]<150:
      img2[i][j] = 50
    else:
      img2[i][j] = 142

plot = plt.subplot(1,3,3).imshow(img2, cmap="gray")



plt.show()

cv2.waitKey()
cv2.destroyAllWindows()