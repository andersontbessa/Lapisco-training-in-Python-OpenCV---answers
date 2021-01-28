#limiar simples -->  O primeiro argumento é a imagem de origem, que deve ser uma imagem em tons de cinza . O segundo argumento é o valor limite que é usado para classificar os valores de pixel. O terceiro argumento é o maxVal que representa o valor a ser dado se o valor do pixel for maior que (às vezes menor que) o valor limite. 

import cv2

obj_img = cv2.imread("imgs/paisagem.jpg")

img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)

ret, threshold_image = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
#ou otsu
print(ret)

cv2.imshow("gray", img)
cv2.imshow("threshold",threshold_image)

cv2.imwrite("threshold.jpg",threshold_image)



