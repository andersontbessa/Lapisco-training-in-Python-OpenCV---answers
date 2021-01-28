
#Dilatação: É exatamente o oposto da erosão. Aqui, um elemento de pixel é '1' se pelo menos um pixel sob o kernel for '1'. Portanto, aumenta a região branca na imagem ou o tamanho do objeto em primeiro plano aumenta. Normalmente, em casos como remoção de ruído, a erosão é seguida de dilatação. Porque a erosão remove os ruídos brancos, mas também encolhe nosso objeto. Então, nós dilatamos. Como o ruído acabou, eles não voltarão, mas nossa área de objeto aumenta. Também é útil para unir partes quebradas de um objeto.

import cv2
import numpy as np

image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Input grayscale image', grayscale_image)

# Apply the threshold
ret, threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('Threshold image', threshold_image)

# Create the structuring element
kernel = np.ones((7, 5), np.uint8) #o 7 é onde cresce mais para cima e o 5 onde cresce mais para as laterais 

# Apply the dilation
for i in range(7):
    dilation = cv2.dilate(threshold_image, kernel, iterations=i)#o  iterations= é a grossura. Ele estando com o "i" do for vai crescendo aos poucos a cada for.
#obs: essa dilatação depende do kernel.

    
    cv2.imshow('Dilated image', dilation)
    cv2.waitKey(1000)
#assim tudo dentro do for dá para ver o vaso aumentando.
