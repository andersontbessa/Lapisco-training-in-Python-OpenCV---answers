#////////////////////////////CvFindContours////////////////////////////////////////////////////
#//Mode:
#//    CV_RETR_EXTERNAL -  Recupera apenas os contornos exteriores extremas.
#//    CV_RETR_LIST - Recupera todos os contornos , sem estabelecer quaisquer relacoes hierarquicas .
#//    CV_RETR_CCOMP - Recupera todos os contornos e as organiza em uma hierarquia de dois niveis : no nivel superior sao os limites externos dos componentes, no segundo nivel sao os limites dos buracos.
#//    CV_RETR_TREE - recupera todos os contornos e reconstroi a hierarquia completa de contornos aninhados .
#//
#//Metodo:
#//    CV_CHAIN_APPROX_NONE - Absolutamente todos os pontos de contorno. Ou seja, a cada 2 pontos de um contorno armazenados com este metodo sao vizinhos 8- conectadas entre si.
#//    CV_CHAIN_APPROX_SIMPLE - Comprime segmentos horizontais , verticais e diagonais e deixa apenas os seus pontos finais.
#//    CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS - Aplica um dos sabores do algoritmo de aproximacao cadeia Teh- Chin , ver TehChin89 .

import cv2
import numpy as np

# Read a rgb image
image = cv2.imread('image.png')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Canny filter
canny_image = cv2.Canny(grayscale_image, 80, 180)
 
#o cv2.findContours encontra muitos contornos que estão na imagem.
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the image to draw the contours
contour_img = np.copy(image)

#o cv2.drawContours desenha todos contornos encontrados
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 3)
#passa a cópia da imagem, depois o que companha a variável acima "contours".  -1 é..., o (0, 0, 255) é a cor do contorno, o 3 é a grossura do contorno. 

# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Show the contours found
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
