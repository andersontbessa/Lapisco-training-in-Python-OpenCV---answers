import cv2
import numpy as np

image = cv2.imread('test.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicando o hough transform. O HoughCircles em conjunto com o circles = np.uint16(np.around(circles)) serve para detectar circulos
circles = cv2.HoughCircles(grayscale_image, cv2.HOUGH_GRADIENT, 1, 60, 
                           param1=150, param2=25, minRadius=0, maxRadius=0)
#print (circles)#test

try:
    circles = np.uint16(np.around(circles))
except AttributeError:
    print('None circles found! Try change the parameters.')
    exit()

 
# Create a copy of the original image to draw the circles
circles_img = np.copy(image)

# Draw all the circles found
for (x, y, radius) in circles[0, :]: 
    cv2.circle(circles_img, (x, y), radius, (0, 0, 255), 2)
    cv2.circle(circles_img, (x, y), 2, (0, 255, 0), 10) #eu inseri esse exemplo de um ponto no meio do círculo, mais como aprendizado.
#x e y são as coordenadas do centro
#o radius é o raio
#(0, 0, 255) isso é a cor do círculo.
#o 2 do final é o tamanho da borda.


cv2.imshow('Input grayscale image', grayscale_image)

cv2.imshow('Threshold result', circles_img)
cv2.waitKey(0)
