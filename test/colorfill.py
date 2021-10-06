import cv2, numpy as np; # Numpy том хэмжээний массив өгөгдөл дээр ашигладаг сан
from sklearn.cluster import KMeans

def visualize_colors(cluster, centroids): 
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins = labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
    start = 0
    for (percent, color) in colors:
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv2.rectangle(rect, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    return rect

image = cv2.imread(zurag) # Зураг уншина
cv2.imshow(zurag, cv2.resize(image, [500,400]))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Сааралтуулна

reshape = image.reshape((image.shape[0] * image.shape[1], 3)) # Зургийн пикселийн массив утгаар боловсруулалт хийдэг

cluster = KMeans(n_clusters=5).fit(reshape) # Sklearn санг ашиглаж ижил утгын өнгүүдийг ялгах үйлдлийг хийж байгаа
visualize = visualize_colors(cluster, cluster.cluster_centers_) # Өнгөнүүдийн RGB кодыг гаргана
visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR) #Ялга хэсгийн өнгийг сэргээх
cv2.imshow('visualize', visualize) #Зураг үзүүлэх
cv2.waitKey()
