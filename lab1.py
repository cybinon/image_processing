import cv2 #OpenCV 
import os
import glob

def getFilenames(exts):
    fnames = [glob.glob(ext) for ext in exts][0]
    print(fnames)
    return fnames

def imgProcess(location):
  img = cv2.imread(i)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
  img = cv2.resize(img, [400,500]) # Өөр, өөр хэмжээтэй зургууд дээр тооцоолол хийх боломжгүй 
  return img;


exts = ["*.jpg"] # Ялгах файлын өргөтгөлүүд
res = getFilenames(exts) # Ялгах үйлдэл

count = len(res); # Нийт зургуудын тоо
avg_img = 0 # Анхны утга

for i in res:
  img = imgProcess(i)
  avg_img = avg_img+img/count; # Зургуудын дундаж

for i in res:
  img = imgProcess(i)
  cv2.imshow(i, img)


cv2.waitKey() #Үр дүнг шууд гаргахгүй хүлээлгэх. Өөөрөөр бол цонх хаалгахгүй үйлдэл

