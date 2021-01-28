import cv2
obj_img = cv2.imread ("imgs/paisagem.jpg")

img= cv2.cvtColor(obj_img, cv2.COLOR_BGR2HSV)#O HSV, possui H (hue) que consiste na cor mesmo, o S (saturation) é a saturação de cor, muito relacionado a intensidade e o V (value) é o brilho da cor. Com as variações dessas características chegamos a diferentes níveis de cores e com intensidades e brilhos distintos.

h, s, v = cv2.split(img) #o split é usado para vermos os canais de cores. Pega cada variável h,s,v e insire no imshow para mostrar cada canal de cor em imagem.

cv2.imshow ("image", img)
cv2.imshow('canal_n1', h)
cv2.imshow('canal_n2', s)
cv2.imshow('canal_n3', v)

cv2.waitKey(0)

cv2.imwrite("salvo_1.jpg", img)
cv2.imwrite("salvo_2.jpg", h)
cv2.imwrite("salvo_3.jpg", s)
cv2.imwrite("salvo_4.jpg", v)


