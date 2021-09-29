import cv2 #OpenCV 
import os
import glob
import numpy as np

image = cv2.imread("./rose.tif");
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.resize(image, (2,2))
print(image)
image = cv2.resize(image, (3,3), interpolation=cv2.INTER_LINEAR)
# image = cv2.resize(image, (2,2))
# cv2.imshow("test", image)
print(image)
# down = [
#   [128,128],
#   [64,64],
#   [32,32]
# ]
cv2.imad

# result = [[]]
# for i in down:
#   name = str(i[0])
#   nearest_resize = cv2.resize(image, i, interpolation=cv2.INTER_NEAREST);
#   linear_resize = cv2.resize(image, i, interpolation=cv2.INTER_LINEAR);
#   iml = np.concatenate((nearest_resize, linear_resize), axis=1);
#   result = np.concatenate((result, iml), axis=0);

# cv2.imshow("result", result)

cv2.waitKey() #Үр дүнг шууд гаргахгүй хүлээлгэх. Өөөрөөр бол цонх хаалгахгүй үйлдэл

