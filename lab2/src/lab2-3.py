import cv2
import numpy as np
import matplotlib.pyplot as plt


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

img = cv2.imread('./lab2/Fig0310.tif')

plt.figure()

plot = plt.subplot(2,2,1).imshow(img)

img = increase_brightness(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plot = plt.subplot(2,2,2).imshow(img)

output = img;
output = output*0;

for i in range(len(img)):
  for j in range(len(img[0])):
    if(img[i][j]>150):
      output[i][j]=255
    else:
      output[i][j] = 0;
      
plot = plt.subplot(2,2,3).imshow(output)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows() 