#Detecção de Borda Laplaciana -->
#Ao contrário do detector de bordas Sobel, o detector de bordas Laplaciano usa apenas um kernel. Ele calcula derivadas de segunda ordem em uma única passagem.

import cv2

image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#insere o filtro laplacian
laplace = cv2.Laplacian(grayscale_image, ddepth=cv2.CV_64F, ksize=3)

# Converte para uint8
laplace = cv2.convertScaleAbs(laplace)

#aqui coloca um equalizador na variável laplace
equalized_laplacian = cv2.equalizeHist(laplace)

cv2.imshow('Input grayscale image', grayscale_image)

cv2.imshow('Laplacian filter result', laplace)

cv2.imshow('Equalized Laplacian', equalized_laplacian)

cv2.waitKey(0)
