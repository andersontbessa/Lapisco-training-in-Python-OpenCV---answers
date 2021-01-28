#adaptive Threshold (Limiar Adaptativo) --> o algoritmo calcula o limiar para pequenas regiões da imagem. Portanto, obtemos limites diferentes para regiões diferentes da mesma imagem e isso nos dá melhores resultados para imagens com iluminação variável.

import cv2
import numpy as np


image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# inserindo a adaptive threshold tendo em vista o MEAN
thresholded_image = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
                                                                 #o cv2.ADAPTIVE_THRESH_MEAN_C divide a imagem em segmentos e calcular um limear para cada segmento baseado na vizinhaça
                                                                #o 11 seria o tamanho da vizinhança que vou calcular o linear, tem que ser número ímpares até 11.
                                                                #o 2 seria uma constante "c", essa constante é um valor que eu subtraio da média que eu calculo quando eu realizo aquele procedimento de janelas.

cv2.imshow('Input grayscale image', grayscale_image)

cv2.imshow('Threshold result', thresholded_image)
cv2.waitKey(0)
