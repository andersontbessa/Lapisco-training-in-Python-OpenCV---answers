#Canny serve para  detecção de bordas na imagem.

import cv2

#seleciona a imagem
obj_img = cv2.imread ("imgs/paisagem.jpg")

img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(img, 80, 1000)

cv2.imshow("gray", img)
cv2.imshow("canny", canny_image)
cv2.waitKey(0)

cv2.imwrite ("canny.jpg", canny_image)

