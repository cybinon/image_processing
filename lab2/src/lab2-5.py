import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./lab2/dollar.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()

plt.subplot(3,3,1).imshow(img, cmap="gray");
plt.title("bit 0")

for i in range(8):
  output = (img >> i) & 1
  plt.subplot(3,3,i+2).imshow(output, cmap="gray");

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()