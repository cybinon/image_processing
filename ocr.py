import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img1 = cv2.imread("jishee.png")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret1, thresh_1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation1 = cv2.dilate(thresh_1, rect_kernel1, iterations = 1)


contours, hierarchy1 = cv2.findContours(dilation1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img1.copy()
file = open("recognized.txt", "w+")
file.write("")
file.close()

for cnt in contours:
  x1, y1, w1, h1 = cv2.boundingRect(cnt)
  rect1 = cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
  cropped1 = img2[y1:y1 + h1, x1:x1 + w1];
  file_1 = open("recognized.txt", "a")

# apply ocr
text_1 = pytesseract.image_to_string(cropped1)

print(text_1)
file_1.write(text_1)
file_1.close()