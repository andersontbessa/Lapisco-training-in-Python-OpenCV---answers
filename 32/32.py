import cv2
import numpy as np

image = cv2.imread('image.png')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(grayscale_image, 80, 180)

# Find how many contours are in the image
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(hierarchy)#test
#Contours é uma lista Python de todos os contornos da imagem. Cada contorno individual é um array Numpy de coordenadas (x, y) de pontos de fronteira do objeto. As bordas de algo seria a fronteira.
#o contours é o conjunto de pontinhos amarelo entre as bordas do desenho. Aí cada pontinho desse tem coordenadas X e Y na fronteira, ou seja, nas bordas.


# Create a copy of the image to draw the contours
contour_img = np.copy(image)


# Draw all the contours found
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 3)

# Print the area of each contour, notice that there are areas close to other areas. Therefore, can be considered
# areas of the same object
for i, contour in enumerate(contours): 
    print('Area ' + str(i + 1) + ': ' + str(cv2.contourArea(contour)))#A área de contorno é dada pela função cv.contourArea () ou a partir de momentos, M ['m00'] .


# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Show the contours found
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
