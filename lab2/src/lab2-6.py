import cv2
import matplotlib.pyplot as plt


fig, axes = plt.subplots(4,2,figsize=(10,5))
ax = axes.ravel()

coffee = cv2.imread("./lab2/coffee1.tif")
coffee = cv2.cvtColor(coffee, cv2.COLOR_BGR2GRAY)
ax[0].imshow(coffee, cmap="gray")
ax[1].hist(coffee.ravel(), bins=256, histtype='step', color="blue")
ax[1].set_xlim(0,255)

coffee = cv2.imread("./lab2/coffee2.tif")
coffee = cv2.cvtColor(coffee, cv2.COLOR_BGR2GRAY)
ax[2].imshow(coffee, cmap="gray")
ax[3].hist(coffee.ravel(), bins=256, histtype='step', color="blue")
ax[3].set_xlim(0,255)

coffee = cv2.imread("./lab2/coffee3.tif")
coffee = cv2.cvtColor(coffee, cv2.COLOR_BGR2GRAY)
ax[4].imshow(coffee, cmap="gray")
ax[5].hist(coffee.ravel(), bins=256, histtype='step', color="blue")
ax[5].set_xlim(0,255)

coffee = cv2.imread("./lab2/coffee4.tif")
coffee = cv2.cvtColor(coffee, cv2.COLOR_BGR2GRAY)
ax[6].imshow(coffee, cmap="gray")
ax[7].hist(coffee.ravel(), bins=256, histtype='step', color="blue")
ax[7].set_xlim(0,255)

plt.show() 

cv2.waitKey()
cv2.destroyAllWindows()